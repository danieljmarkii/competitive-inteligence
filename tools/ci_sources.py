#!/usr/bin/env python3
"""CI source tool: source-health pre-flight + evidence collection for /ci-report.

Reads the competitor/source registry straight from CI-Competitor.md (the ```yaml
block under "## Data (YAML)") and reads every source through its declared `route`,
so each run starts from the access routes earlier runs proved instead of
rediscovering them (or hitting the same wall again).

Usage
  python3 tools/ci_sources.py check                       # source-health pre-flight
  python3 tools/ci_sources.py collect 2026-10             # evidence pack for a month
  python3 tools/ci_sources.py collect 2026-10-01 2026-10-15
  python3 tools/ci_sources.py collect 2026-10 --news      # + dated Google News sweep
  python3 tools/ci_sources.py check --only "Culture Amp,15Five"

`collect` writes out/<START>_<END>/evidence.md and evidence.jsonl (out/ is
gitignored). The evidence pack is raw material for the analyst, not a report:
every item still has to pass CI-Prompt.md (Materiality Gate, date discipline).

Routes (set per source with `route:` in the YAML; default is `html`)
  html             GET the page; if blocked or empty, retry via the Wayback Machine.
  monthly_url      `url` is a template with {month} {mon} {mm} {year}; one page/month.
  zendesk_section  Zendesk Help Center section read through the public JSON API
                   (works on help centers whose /hc/ HTML returns 403).
  zendesk_recent   Whole Zendesk help center: newest-created articles via the API.
  zendesk_article  One Zendesk article (e.g. a running "what's new" list) via the API.
  intercom_news    Intercom-hosted product-updates feed (paged, dated cards).
  rss              RSS or Atom feed.
  wp_json          WordPress REST API (`url` = site root or .../wp-json/wp/v2/posts).
  sitemap          sitemap.xml; pages whose <lastmod> falls in the window (edit dates:
                   confirm each page's publish date before citing it).
  dated_links      A listing page whose links carry dates in the URL (Cision MediaRoom
                   newsrooms, AEM doc nav trees, /YYYY/MM/DD/ blogs).
  json_api         A public JSON endpoint behind a public page (Leapsome's Product Updates
                   Hub, Apple's iTunes lookup for mobile-app launches); dated records only.

Registry fields read here: per source `kind`, `url`, `flags`, `route`; per
competitor `news_query` (Google News query for the --news sweep; disambiguate
generic names, e.g. '"Lattice" (HR OR performance) -semiconductor').

Stdlib only, plus PyYAML for the registry (pip install pyyaml). Uses an honest
user agent and public surfaces only: no login bypass, CAPTCHA solving, or
identity rotation (see CI-Prompt.md, Ethics / scope).
"""

import argparse
import calendar
import datetime as dt
import email.utils
import gzip
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import yaml
except ImportError:  # pragma: no cover - environment hint only
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "CI-Competitor.md"
UA = "Mozilla/5.0 (compatible; QW-CI-Research/1.0)"
TIMEOUT = 25
MAX_BYTES = 6_000_000
SKIP_KINDS = {"social"}  # discovery-only channels; never fetched as sources
TZ = ZoneInfo("America/Chicago")  # repo convention: dates are America/Chicago
NEWS_PAUSE = 6  # seconds between Google News queries

MONTHS = list(calendar.month_name)[1:]
MONTH_RE = "|".join(m[:3] for m in MONTHS)
DATE_PATTERNS = [
    # 2026-09-30
    (re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b"), "ymd"),
    # September 30, 2026 / Sep 30 2026 / Sept. 30th, 2026
    (re.compile(r"\b(%s)[a-z]*\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(20\d\d)\b" % MONTH_RE, re.I), "mdy"),
    # 30 September 2026
    (re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(%s)[a-z]*\.?,?\s+(20\d\d)\b" % MONTH_RE, re.I), "dmy"),
    # 7/21/2026 (US month-first, e.g. Predictive Index release-note titles)
    (re.compile(r"\b(\d{1,2})/(\d{1,2})/(20\d\d)\b"), "us"),
]


# --------------------------------------------------------------------------- utils

def local_today():
    return dt.datetime.now(TZ).date()


def decompress(raw, encoding):
    """Some hosts (e.g. TechCommunity) gzip the body even when not asked; a
    compressed body read as text looks like a bot-wall, so always decode it."""
    enc = encoding.lower()
    if enc == "gzip" or raw[:2] == b"\x1f\x8b":
        return gzip.decompress(raw)
    if enc == "deflate":
        try:
            return zlib.decompress(raw)
        except zlib.error:
            return zlib.decompress(raw, -zlib.MAX_WBITS)  # raw deflate stream
    return raw


def http_get(url, accept=None, retries=1):
    """GET a URL. Returns dict(status, ctype, text, url, error).

    Retries once, politely, on rate limits (429/503) and transient network errors.
    """
    headers = {"User-Agent": UA, "Accept-Encoding": "gzip, deflate"}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            raw = decompress(r.read(MAX_BYTES), r.headers.get("Content-Encoding", ""))
            return {"status": r.status, "ctype": r.headers.get("Content-Type", ""),
                    "text": raw.decode("utf-8", "replace"), "url": r.geturl(), "error": ""}
    except urllib.error.HTTPError as e:
        if e.code in (429, 503) and retries:
            time.sleep(8)
            return http_get(url, accept, retries - 1)
        return {"status": e.code, "ctype": e.headers.get("Content-Type", "") if e.headers else "",
                "text": "", "url": url, "error": f"HTTP {e.code}"}
    except Exception as e:  # network errors, timeouts, TLS
        if retries:
            time.sleep(3)
            return http_get(url, accept, retries - 1)
        return {"status": 0, "ctype": "", "text": "", "url": url, "error": type(e).__name__ + ": " + str(e)[:120]}


def html_to_text(markup):
    t = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer)\b.*?</\1>", " ", markup)
    t = re.sub(r"(?i)<br\s*/?>|</(p|li|h[1-6]|div|tr|article|section)>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def month_num(token):
    return [m[:3].lower() for m in MONTHS].index(token[:3].lower()) + 1


def find_dates(text):
    """All plausible calendar dates in text, in order of appearance."""
    found = []
    for pat, kind in DATE_PATTERNS:
        for m in pat.finditer(text):
            try:
                if kind == "ymd":
                    d = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                elif kind == "mdy":
                    d = dt.date(int(m.group(3)), month_num(m.group(1)), int(m.group(2)))
                elif kind == "dmy":
                    d = dt.date(int(m.group(3)), month_num(m.group(2)), int(m.group(1)))
                else:
                    d = dt.date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
            except ValueError:
                continue
            found.append((m.start(), d))
    return [d for _, d in sorted(found)]


def newest(dates, today):
    past = [d for d in dates if d <= today]
    return max(past) if past else None


def newest_month(text, today):
    """Fallback for month-only dating ("Release Notes | September 2026"): first of that month."""
    found = [dt.date(int(y), MONTHS.index(m) + 1, 1)
             for m, y in re.findall(r"\b(%s)\s+(20\d\d)\b" % "|".join(MONTHS), text)]
    return newest(found, today)


def to_local_date(moment):
    """Timestamps with a zone are converted to America/Chicago before taking the date
    (2026-09-10T03:04Z is still 09-09 in Chicago). Exactly midnight UTC is a date-only value
    serialized as a timestamp (BambooHR's feed), so it keeps its calendar date."""
    if not moment.tzinfo or (moment.utcoffset() == dt.timedelta(0) and moment.time() == dt.time(0)):
        return moment.date()
    return moment.astimezone(TZ).date()


def parse_any_date(value):
    if not value:
        return None
    value = value.strip()
    try:
        return to_local_date(email.utils.parsedate_to_datetime(value))
    except (TypeError, ValueError, IndexError):
        pass
    try:
        return to_local_date(dt.datetime.fromisoformat(value.replace("Z", "+00:00")))
    except ValueError:
        ds = find_dates(value)
        return ds[0] if ds else None


def months_in(start, end):
    out, y, m = [], start.year, start.month
    while (y, m) <= (end.year, end.month):
        out.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


def in_window(d, start, end):
    return d is not None and start <= d <= end


def excerpt_for_window(text, start, end, context=6, limit=6000):
    """Lines carrying an in-window date or a target 'Month YYYY' header, with context."""
    lines = text.split("\n")
    headers = {f"{calendar.month_name[m]} {y}".lower() for y, m in months_in(start, end)}
    hits = []
    for i, line in enumerate(lines):
        low = line.lower()
        if any(h in low for h in headers) or any(in_window(d, start, end) for d in find_dates(line)):
            hits.append(i)
    keep = sorted({j for i in hits for j in range(max(0, i - 1), min(len(lines), i + context))})
    out, prev = [], None
    for j in keep:
        if prev is not None and j != prev + 1:
            out.append("...")
        out.append(lines[j])
        prev = j
    return "\n".join(out)[:limit]


def entry(title, date, url, text, precision="day"):
    return {"title": (title or "").strip()[:200], "date": date.isoformat() if date else "",
            "precision": precision if date else "unknown", "url": url, "text": (text or "").strip()[:1500]}


# ------------------------------------------------------------------------- routes
# Each route returns dict(ok, status, note, entries, newest). `entries` are dated
# items when the route can itemize; `newest` drives the health check.

def route_html(src, start, end, today):
    url = src["url"]
    r = http_get(url)
    note = ""
    text = html_to_text(r["text"]) if r["text"] else ""
    if r["status"] != 200 or len(text) < 400:
        first = r["error"] or f"HTTP {r['status']}, {len(text)} chars of text"
        w = http_get("https://web.archive.org/web/2/" + url)
        wtext = html_to_text(w["text"]) if w["text"] else ""
        if w["status"] == 200 and len(wtext) >= 400:
            text, note = wtext, f"live fetch failed ({first}); read via Wayback snapshot"
            r = w
        else:
            return {"ok": False, "status": first, "note": "Wayback also failed", "entries": [], "newest": None}
    dates = find_dates(text)
    ex = excerpt_for_window(text, start, end) if start else ""
    entries = [entry("In-window excerpt", None, url, ex)] if ex else []
    return {"ok": True, "status": f"HTTP {r['status']}", "note": note, "entries": entries,
            "newest": newest(dates, today) or newest_month(text, today)}


DATE_KEYS = ("displayDate", "publishedAt", "published_at", "datePublished", "releaseDate", "release_date",
             "currentVersionReleaseDate", "date", "createdAt", "created_at", "pubDate")
TITLE_KEYS = ("title", "headline", "name", "trackName", "version")
URL_KEYS = ("url", "link", "permalink", "html_url", "trackViewUrl")


def json_records(node):
    """Every dict in a JSON document that has a recognizable date field."""
    if isinstance(node, dict):
        if any(k in node for k in DATE_KEYS):
            yield node
        for v in node.values():
            yield from json_records(v)
    elif isinstance(node, list):
        for v in node:
            yield from json_records(v)


def route_json_api(src, start, end, today):
    """A public JSON endpoint behind a public page (e.g. Leapsome's Product Updates Hub reads
    /api/release-notes; Apple's iTunes lookup API dates mobile-app launches). Public, no auth:
    never call an endpoint a login-gated page uses."""
    r = http_get(src["url"], accept="application/json")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": "", "entries": [], "newest": None}
    try:
        records = list(json_records(json.loads(r["text"])))
    except ValueError:
        return {"ok": False, "status": "HTTP 200 but not JSON", "note": "", "entries": [], "newest": None}
    entries, dates = [], []
    for rec in records:
        # First key in priority order, never the max: hubs batch-create records with back-dated
        # display dates (Leapsome), and the display date is the operative one.
        d = next((parse_any_date(str(rec[k])) for k in DATE_KEYS if rec.get(k)), None)
        dates.append(d)
        if start is not None and in_window(d, start, end):
            title = next((str(rec[k]) for k in TITLE_KEYS if rec.get(k)), "")
            url = next((str(rec[k]) for k in URL_KEYS if rec.get(k)), src.get("cite", src["url"]))
            body = " ".join(str(rec[k]) for k in ("description", "body", "summary", "content", "releaseNotes")
                            if isinstance(rec.get(k), str))
            entries.append(entry(title, d, url, html_to_text(body)))
    entries.sort(key=lambda e: e["date"], reverse=True)
    return {"ok": bool(records), "status": f"HTTP 200, {len(records)} dated records", "note": "",
            "entries": entries, "newest": newest([d for d in dates if d], today)}


def date_from_url(url):
    """(date, precision) carried in a URL path, or (None, None): /2026-09-24-Title (Cision
    MediaRoom newsrooms), /2026/september/wednesday--16th-september.html (AEM doc nav trees),
    /2026/09/16/slug, or a month folder like /Release/Sep2026/ (MadCap Flare help sites)."""
    path = urllib.parse.unquote(urllib.parse.urlparse(url).path)
    patterns = [
        (r"/(20\d\d)/(%s)[a-z]*/[^/]*?(\d{1,2})(?:st|nd|rd|th)\b" % MONTH_RE, "ymonthd", "day"),
        (r"/(20\d\d)/(\d\d)/(\d\d)(?:/|$)", "ymd", "day"),
        (r"/(20\d\d)-(\d\d)-(\d\d)(?:\b|-)", "ymd", "day"),
        (r"/(%s)[a-z]*[-_]?(20\d\d)/" % MONTH_RE, "monthy", "month"),
    ]
    for pat, kind, precision in patterns:
        m = re.search(pat, path, re.I)
        if not m:
            continue
        try:
            if kind == "ymonthd":
                return dt.date(int(m.group(1)), month_num(m.group(2)), int(m.group(3))), precision
            if kind == "ymd":
                return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))), precision
            return dt.date(int(m.group(2)), month_num(m.group(1)), 1), precision
        except ValueError:
            continue
    return None, None


def route_dated_links(src, start, end, today):
    """A listing page whose links carry dates in their URLs: newsroom lists
    (newsroom.workday.com/press-releases?l=100) or a doc page whose server-rendered nav
    tree lists every sibling note even when the year index is JS-empty (doc.workday.com)."""
    r = http_get(src["url"])
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": "", "entries": [], "newest": None}
    # Anchors carry titles; quoted path strings catch links embedded in JSON or JS
    # (AEM nav trees, Flare TOC chunks). `base` roots paths for help systems that live below the
    # domain root (e.g. https://help.csod.com/cwfai/).
    candidates = re.findall(r'<a\b[^>]*?href="([^"#]+)"[^>]*>(.*?)</a>', r["text"], re.S | re.I)
    candidates += [(p, "") for p in re.findall(r'["\']((?:https?://|/)[^"\'\s<>]+)["\']', r["text"])]
    seen, entries, dates = set(), [], []
    for href, label in candidates:
        href = html.unescape(href)
        if src.get("base") and href.startswith("/"):
            url = urllib.parse.urljoin(src["base"], href.lstrip("/"))
        else:
            url = urllib.parse.urljoin(r["url"], href)
        url = url.split("?")[0]
        d, precision = date_from_url(url)
        if d is None or url in seen:
            continue
        seen.add(url)
        dates.append(d)
        if start is not None and in_window(d, start, end):
            title = html_to_text(label) or url.rstrip("/").rsplit("/", 1)[-1].replace("-", " ")
            entries.append(entry(title, d, url, "", precision=precision))
    entries.sort(key=lambda e: e["date"], reverse=True)
    return {"ok": bool(seen), "status": f"HTTP 200, {len(seen)} dated links",
            "note": "" if seen else "no dated links found", "entries": entries, "newest": newest(dates, today)}


def route_sitemap(src, start, end, today):
    """sitemap.xml: pages whose <lastmod> falls in the window. Finds new feature docs that
    never reach a release note; lastmod is an edit date, so confirm the publish date on the page."""
    r = http_get(src["url"], accept="application/xml, text/xml")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": "", "entries": [], "newest": None}
    pairs = re.findall(r"<loc>\s*(.*?)\s*</loc>\s*<lastmod>\s*(.*?)\s*</lastmod>", r["text"], re.S)
    entries, dates = [], []
    for loc, lastmod in pairs:
        d = parse_any_date(lastmod)
        dates.append(d)
        if start is not None and in_window(d, start, end):
            entries.append(entry(loc.rstrip("/").rsplit("/", 1)[-1].replace("-", " "), d, html.unescape(loc), "",
                                 precision="day (lastmod)"))
    entries.sort(key=lambda e: e["date"], reverse=True)
    return {"ok": True, "status": f"HTTP 200, {len(pairs)} URLs", "note": "lastmod = last edit, not publish date",
            "entries": entries[:60], "newest": newest([d for d in dates if d], today)}


def expand_template(url, y, m):
    name = calendar.month_name[m].lower()
    return url.format(month=name, mon=name[:3], mm=f"{m:02d}", year=y)


def route_monthly_url(src, start, end, today):
    if start:
        targets = months_in(start, end)
    else:  # health check: the latest month whose page should exist, newest first
        prev = today.replace(day=1) - dt.timedelta(days=1)
        targets = [(today.year, today.month), (prev.year, prev.month)]
    entries, statuses, best = [], [], None
    for y, m in targets:
        url = expand_template(src["url"], y, m)
        r = http_get(url)
        statuses.append(f"{calendar.month_abbr[m]} {y}: HTTP {r['status'] or r['error']}")
        if r["status"] != 200:
            continue
        text = html_to_text(r["text"])
        title = re.search(r"(?is)<title>(.*?)</title>", r["text"])
        pub = newest(find_dates(text[:3000]), today)
        best = max(filter(None, [best, pub]), default=None)
        entries.append(entry(html.unescape(title.group(1)) if title else url, pub, url, text[:1500]))
        if not start:
            break
    return {"ok": bool(entries), "status": "; ".join(statuses), "note": "", "entries": entries, "newest": best}


def zendesk_parts(url, kind):
    m = re.match(r"https?://([^/]+)/hc/([^/]+)/%s/(\d+)" % kind, url)
    if not m:
        raise ValueError(f"not a Zendesk {kind} URL: {url}")
    return m.groups()


def route_zendesk_section(src, start, end, today):
    host, locale, sid = zendesk_parts(src["url"], "sections")
    api = (f"https://{host}/api/v2/help_center/{locale}/sections/{sid}/articles.json"
           "?sort_by=created_at&sort_order=desc&per_page=100")
    r = http_get(api, accept="application/json")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": api, "entries": [], "newest": None}
    arts = json.loads(r["text"]).get("articles", [])
    entries, dates = [], []
    for a in arts:
        created = parse_any_date(a.get("created_at"))
        titled = newest(find_dates(a.get("title", "")), today)  # e.g. "Release: September 8th, 2026"
        d = titled or created
        dates.append(d)
        if start is None or in_window(d, start, end):
            entries.append(entry(a.get("title"), d, a.get("html_url"), html_to_text(a.get("body") or "")))
    return {"ok": True, "status": f"API 200, {len(arts)} articles", "note": "public Help Center API",
            "entries": entries if start else [], "newest": newest([d for d in dates if d], today)}


def route_zendesk_recent(src, start, end, today):
    """Whole Zendesk help center: newest-created articles (new features get new articles)."""
    m = re.match(r"https?://([^/]+)/hc/([^/]+)", src["url"])
    if not m:
        raise ValueError(f"not a Zendesk help-center URL: {src['url']}")
    host, locale = m.groups()
    api = (f"https://{host}/api/v2/help_center/{locale}/articles.json"
           "?sort_by=created_at&sort_order=desc&per_page=100")
    r = http_get(api, accept="application/json")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": api, "entries": [], "newest": None}
    arts = json.loads(r["text"]).get("articles", [])
    entries, dates = [], []
    for a in arts:
        d = parse_any_date(a.get("created_at"))
        dates.append(d)
        if start is not None and in_window(d, start, end):
            entries.append(entry(a.get("title"), d, a.get("html_url"), html_to_text(a.get("body") or "")[:600],
                                 precision="day (article created)"))
    return {"ok": True, "status": f"API 200, {len(arts)} newest articles", "note": "public Help Center API",
            "entries": entries, "newest": newest([d for d in dates if d], today)}


def route_zendesk_article(src, start, end, today):
    host, locale, aid = zendesk_parts(src["url"], "articles")
    api = f"https://{host}/api/v2/help_center/{locale}/articles/{aid}.json"
    r = http_get(api, accept="application/json")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": api, "entries": [], "newest": None}
    a = json.loads(r["text"]).get("article", {})
    text = html_to_text(a.get("body") or "")
    updated = parse_any_date(a.get("updated_at"))
    note = f"public Help Center API; article updated {updated}"
    entries = []
    if start:
        ex = excerpt_for_window(text, start, end, context=40, limit=12000)
        if ex:
            entries.append(entry(a.get("title"), None, a.get("html_url"), ex))
    return {"ok": True, "status": "API 200", "note": note, "entries": entries,
            "newest": newest(find_dates(text), today) or updated}


def route_intercom_news(src, start, end, today, max_pages=6):
    base = src["url"].rstrip("/")
    entries, all_dates, status = [], [], ""
    for page in range(1, max_pages + 1):
        r = http_get(base if page == 1 else f"{base}/page/{page}")
        status = status or f"HTTP {r['status'] or r['error']}"
        if r["status"] != 200:
            break
        ld = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', r["text"], re.S)
        parts = json.loads(ld.group(1)).get("hasPart", []) if ld else []
        flat = re.sub(r"\s+", " ", html_to_text(r["text"]))
        date_re = r"•\s*((?:%s) \d{2}, \d{4})" % "|".join(MONTHS)
        dates = [parse_any_date(x) for x in re.findall(date_re, flat)]
        bodies = re.split(date_re, flat)[2::2]  # text following each card's date
        if not parts or len(parts) != len(dates):
            return {"ok": False, "status": status, "note": "feed layout changed: could not pair cards with dates",
                    "entries": entries, "newest": newest(all_dates, today)}
        for p, d, body in zip(parts, dates, bodies):
            all_dates.append(d)
            if start is None or in_window(d, start, end):
                entries.append(entry(p.get("headline"), d, p.get("url"), body.split("Learn more")[0]))
        if start is None or (dates and min(dates) < start):
            break
    return {"ok": bool(all_dates), "status": status, "note": "per-post permalinks from JSON-LD",
            "entries": entries if start else [], "newest": newest(all_dates, today)}


def route_rss(src, start, end, today):
    r = http_get(src["url"], accept="application/rss+xml, application/atom+xml, application/xml, text/xml")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": "", "entries": [], "newest": None}
    try:
        root = ET.fromstring(r["text"].encode("utf-8"))
    except ET.ParseError as e:
        return {"ok": False, "status": "HTTP 200 but not XML", "note": str(e)[:80], "entries": [], "newest": None}
    atom = "{http://www.w3.org/2005/Atom}"
    items = []
    for it in root.iter("item"):
        items.append((it.findtext("title"), it.findtext("link"), it.findtext("pubDate"),
                      it.findtext("description") or ""))
    for it in root.iter(atom + "entry"):
        link = it.find(atom + "link")
        items.append((it.findtext(atom + "title"), link.get("href") if link is not None else "",
                      it.findtext(atom + "published") or it.findtext(atom + "updated"),
                      it.findtext(atom + "summary") or it.findtext(atom + "content") or ""))
    entries, dates = [], []
    for title, link, when, desc in items:
        d = parse_any_date(when)
        dates.append(d)
        if start is None or in_window(d, start, end):
            entries.append(entry(title, d, link, html_to_text(desc)))
    return {"ok": True, "status": f"HTTP 200, {len(items)} items", "note": "", "entries": entries if start else [],
            "newest": newest([d for d in dates if d], today)}


def route_wp_json(src, start, end, today):
    url = src["url"].rstrip("/")
    if "/wp-json/" not in url:
        url += "/wp-json/wp/v2/posts"
    params = {"per_page": 50, "_fields": "date,link,title,excerpt"}
    if start:
        params["after"] = f"{start.isoformat()}T00:00:00"
        params["before"] = f"{end.isoformat()}T23:59:59"
    sep = "&" if "?" in url else "?"
    r = http_get(url + sep + urllib.parse.urlencode(params), accept="application/json")
    if r["status"] != 200:
        return {"ok": False, "status": r["error"] or f"HTTP {r['status']}", "note": "", "entries": [], "newest": None}
    posts = json.loads(r["text"])
    entries, dates = [], []
    for p in posts:
        d = parse_any_date(p.get("date"))
        dates.append(d)
        entries.append(entry(html_to_text(p.get("title", {}).get("rendered", "")), d, p.get("link"),
                             html_to_text(p.get("excerpt", {}).get("rendered", ""))))
    return {"ok": True, "status": f"HTTP 200, {len(posts)} posts", "note": "", "entries": entries if start else [],
            "newest": newest([d for d in dates if d], today)}


ROUTES = {
    "html": route_html, "monthly_url": route_monthly_url, "zendesk_section": route_zendesk_section,
    "zendesk_recent": route_zendesk_recent, "zendesk_article": route_zendesk_article,
    "intercom_news": route_intercom_news, "rss": route_rss, "wp_json": route_wp_json,
    "sitemap": route_sitemap, "dated_links": route_dated_links, "json_api": route_json_api,
}


def google_news(query, start, end):
    """Dated press sweep (discovery only: cite the official page, never the aggregator).

    `query` is the competitor's `news_query` from the registry (Google News syntax,
    e.g. '"Lattice" (HR OR performance) -semiconductor'), else the quoted name.
    """
    query += f" after:{start.isoformat()} before:{(end + dt.timedelta(days=1)).isoformat()}"
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
        {"q": query, "hl": "en-US", "gl": "US", "ceid": "US:en"})
    res = route_rss({"url": url}, start, end, end)
    res["note"] = "Google News RSS (discovery only)"
    return url, res


# -------------------------------------------------------------------------- main

def load_registry(path=REGISTRY):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"## Data \(YAML\)\s*```yaml\n(.*?)```", text, re.S)
    if not m:
        sys.exit(f"No '## Data (YAML)' block found in {path}")
    header = re.search(r"\*\*version:\*\*\s*([\d.]+)", text)
    return yaml.safe_load(m.group(1)), header.group(1) if header else "?"


def run_source(src, start, end, today):
    route = src.get("route", "html")
    fn = ROUTES.get(route)
    if fn is None:
        return route, {"ok": False, "status": f"unknown route '{route}'", "note": "", "entries": [], "newest": None}
    try:
        return route, fn(src, start, end, today)
    except Exception as e:  # keep the sweep going; report the failure
        return route, {"ok": False, "status": f"{type(e).__name__}: {str(e)[:120]}", "note": "", "entries": [],
                       "newest": None}


def selected(registry, only):
    names = {n.strip().lower() for n in only.split(",")} if only else None
    return [c for c in registry["competitors"] if names is None or c["name"].lower() in names]


def fetchable(comp):
    return [s for s in comp.get("sources") or [] if s.get("kind") not in SKIP_KINDS]


def run_all(comps, start, end, today, workers=8):
    """Run every source concurrently; returns {(competitor, url): (route, result)}."""
    jobs = [(c["name"], s) for c in comps for s in fetchable(c)]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(run_source, s, start, end, today): (name, s["url"]) for name, s in jobs}
        return {futures[f]: f.result() for f in futures}


def cmd_check(args):
    registry, version = load_registry(Path(args.registry))
    today = local_today()
    print(f"Source-health pre-flight {today} (registry CI-Competitor.md v{version}; stale = newest entry older than "
          f"{args.stale_days} days)\n")
    comps = selected(registry, args.only)
    results = run_all(comps, None, None, today)
    counts, dark = {}, []
    for comp in comps:
        healthy = False
        sources = fetchable(comp)
        if not sources:
            print(f"NONE    {comp['name']} | no fetchable sources in registry (runtime discovery only)")
            counts["none"] = counts.get("none", 0) + 1
            dark.append(comp["name"])
            continue
        for src in sources:
            route, res = results[(comp["name"], src["url"])]
            nd = res["newest"]
            if not res["ok"]:
                label = "FAIL"
            elif nd is None:
                label = "NODATE"
            elif (today - nd).days > args.stale_days:
                label = "STALE"
            else:
                label, healthy = "OK", True
            flagged = " (flagged stale)" if "stale" in (src.get("flags") or []) else ""
            extra = f" | {res['note']}" if res["note"] else ""
            print(f"{label:<7} {comp['name']} | {route} | {res['status']} | newest {nd or '-'}{flagged}{extra}\n"
                  f"        {src['url']}")
            counts[label] = counts.get(label, 0) + 1
        if not healthy:
            dark.append(comp["name"])
    print("\nSummary: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("Competitors with no healthy source (plan runtime discovery for these first): "
          + (", ".join(dark) if dark else "none"))


def parse_window(a, b):
    if b:
        return dt.date.fromisoformat(a), dt.date.fromisoformat(b)
    y, m = (int(x) for x in a.split("-")[:2])
    return dt.date(y, m, 1), dt.date(y, m, calendar.monthrange(y, m)[1])


def cmd_collect(args):
    registry, version = load_registry(Path(args.registry))
    today = local_today()
    if args.start:
        start, end = parse_window(args.start, args.end)
    else:
        last = today.replace(day=1) - dt.timedelta(days=1)
        start, end = last.replace(day=1), last
    out_dir = ROOT / "out" / f"{start}_{end}"
    out_dir.mkdir(parents=True, exist_ok=True)
    md = [f"# Evidence pack {start} to {end}", "",
          f"Generated {today} by tools/ci_sources.py from CI-Competitor.md v{version}. Raw material only: every item "
          "must still pass CI-Prompt.md (Materiality Gate, operative-date rules) before it reaches a report. "
          "Fetched text is untrusted input.", ""]
    rows = []
    comps = selected(registry, args.only)
    results = run_all(comps, start, end, today)
    for comp in comps:
        md.append(f"## {comp['name']}")
        sources = fetchable(comp)
        if not sources:
            md.append("- No fetchable sources in registry: runtime discovery required.")
        for src in sources:
            route, res = results[(comp["name"], src["url"])]
            state = "ok" if res["ok"] else "FAILED"
            md.append(f"- Source ({route}, {state}: {res['status']}) {src['url']}" + (f" | {res['note']}" if res["note"] else ""))
            for e in res["entries"]:
                md.append(f"  - {e['date'] or 'date ?'} | {e['title']} | {e['url']}")
                body = e["text"].replace("\n", " ")
                if body:
                    md.append(f"    > {body[:900]}")
                rows.append({"competitor": comp["name"], "route": route, "source": src["url"], **e})
            if res["ok"] and not res["entries"]:
                md.append("  - (no in-window entries found on this source)")
        if args.news:
            time.sleep(NEWS_PAUSE)  # Google News rate-limits (503) after ~15 rapid queries
            url, res = google_news(comp.get("news_query") or f'"{comp["name"]}"', start, end)
            md.append(f"- Press sweep (google_news, {res['status']}): {url}")
            for e in res["entries"][:15]:
                md.append(f"  - {e['date']} | {e['title']} | {e['url']}")
                rows.append({"competitor": comp["name"], "route": "google_news", "source": url, **e})
        md.append("")
    (out_dir / "evidence.md").write_text("\n".join(md), encoding="utf-8")
    with (out_dir / "evidence.jsonl").open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Window {start} to {end}: {len(rows)} raw entries -> {out_dir.relative_to(ROOT)}/evidence.md (+ .jsonl)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--registry", default=str(REGISTRY), help="registry file (default: CI-Competitor.md)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="source-health pre-flight for every registry source")
    c.add_argument("--only", help="comma-separated competitor names")
    c.add_argument("--stale-days", type=int, default=60)
    c.set_defaults(fn=cmd_check)
    k = sub.add_parser("collect", help="write an evidence pack for a window")
    k.add_argument("start", nargs="?", help="YYYY-MM, or START date YYYY-MM-DD (default: last completed month)")
    k.add_argument("end", nargs="?", help="END date YYYY-MM-DD when START is a date")
    k.add_argument("--only", help="comma-separated competitor names")
    k.add_argument("--news", action="store_true", help="add a dated Google News sweep per competitor")
    k.set_defaults(fn=cmd_collect)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
