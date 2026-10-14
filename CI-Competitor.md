# CI — Competitor File — Source Registry (routes, flags, verification)

> **version:** 3.0 · **owner:** Competitive Intelligence · **last updated:** 2026-10-13
> Track versions in git, not in the filename. Read by `/ci-report` and by `tools/ci_sources.py`.
> **v3.0 (2026-10-13):** every source now records the access `route` that works and the date a run last `verified` it; competitors can carry a `news_query`. The 2026-09 run re-verified the registry, promoted or closed five months of unactioned Source Health suggestions (archived in `reports/source-health-archive-2026-05-to-07.md`), and moved this file to self-curation.

Purpose
- Canonical competitor list (names + aliases) and the **sources** each run reads, each with the route proven to read it.
- This file is **data**, not methodology. How to collect, the Access Playbook, and the curation rules live in `CI-Prompt.md`.
- Sources are a *starting point*, not a closed set. Each run curates this file itself, in the open: promote / re-route / demote with evidence, list every change in the report's Workflow Retro, ship it on the run's PR (`CI-Prompt.md` → RUN RETRO & SELF-CURATION).

Hard rules
- Do **not** invent competitors outside this file.
- Use the **name** field as the canonical vendor name.
- All URLs must be plain https. Never add a URL a run did not verify.

---

## Fields
Per competitor: `name`, `aliases`, `website`, `sources`, optional `news_query` (Google News query for `collect --news`; disambiguates generic names).

Per source:
- `kind` : what the surface is (see Source kinds).
- `url` : plain https. With `route: monthly_url`, a template using `{month}` `{mon}` `{mm}` `{year}` (e.g. `.../{month}-{year}-product-updates`).
- `route` : how to read it; default `html`. One of `html` (GET, Wayback fallback) · `monthly_url` · `zendesk_section` · `zendesk_recent` · `zendesk_article` (public Help Center JSON API; works where `/hc/` HTML 403s) · `intercom_news` · `rss` · `wp_json` · `sitemap` · `dated_links` (listings whose links carry dates: Cision newsrooms, AEM doc nav trees). Implemented in `tools/ci_sources.py`; when to use each is in `CI-Prompt.md` → Access Playbook.
- `flags` : behavior hints (legend below).
- `cite` : optional human-facing URL to cite when `url` is a machine endpoint (e.g. a JSON API behind a public page).
- `verified` : last date a run read useful content through the route (dated, unless flagged `undated`). Absent on sources known to be blocked: they stay listed so the check keeps reporting the wall.

## Flags (source behavior hints)
- `index` : the URL is a hub/listing; you must open child pages in-window.
- `running_list` : a single long page with many dated entries/sections; find month headers and extract in-window.
- `ui_dynamic` : content often hides behind tabs/accordions; avoid click-reliance (prefer text extraction + find).
- `login` : requires authentication; never bypass. Record Access limits and do not claim "no notable changes."
- `bot_blocked` : blocks automated fetches (403/429/captcha/JS-wall) on its HTML. Use the source's `route` or the Access Playbook; do not treat as "no changes."
- `search_required` : no reliable dated surface; use constrained web search / the press sweep.
- `press` : secondary signal source; downgrade confidence unless corroborated.
- `year_pinned` : URL/title is scoped to a specific year; if it doesn't match the window year, find the equivalent page(s) for the window year.
- `stale` : superseded or no longer updated; retained only for fallback or search reconciliation.
- `undated` : live, but entries carry no per-item dates; pair with a dated surface before citing a date.

## Source kinds (scan order hint)
`feed | release_notes | product_updates | help_center | docs | blog | community | newsroom | roadmap | status | press | aggregator | social`
- `feed` : a machine-readable RSS/Atom/JSON feed. **Scan first** when present: dated, one entry per item, and it usually survives bot-walls.
- `newsroom` : the vendor's own dated press releases. Best surface for vendors without a public changelog (HCM suites).
- `aggregator` : a third-party changelog aggregator (e.g. Releasebot). Discovery only: it reveals dated items and URL migrations, but cite the vendor's official page.
- `social` : LinkedIn/X. **Discovery/lead channel only**, never fetched as a source or cited as primary (see `CI-Prompt.md` → Runtime discovery §4).

---

## Open source issues (start the next run here)
Unresolved gaps only; each run rewrites this list. Run-by-run history lives in each `reports/<YYYY-MM>-CI-Report.md` (Source Health + Workflow Retro); 2026-05 to 2026-07 logs are archived in `reports/source-health-archive-2026-05-to-07.md`.

```text
- Paylocity: every paylocity.com path serves a Cloudflare JS interstitial to curl and renders empty to WebFetch; the September roundup (/resources/learn/blogs/whats-new-blog-september-2026/) was unpublished on 2026-10-13. Try first: the Releasebot aggregator, then the --news sweep. See the Retro proposal on a JS-rendering route.
- UKG: www.ukg.com challenges curl and WebFetch (Cloudflare), but the newsroom reads through the tool. Full release text: FinancialContent syndication of Business Wire. In-product changes stay Unknown (login-only).
- ADP: in-product release notes are login-only; only the MediaRoom press list is public. In-product changes stay Unknown.
- Energage: no public product surface (help center in-app; Zendesk closed). Watch Engagedly's Beamer changelog for joint post-merger news.
- Officevibe (Workleap): no release notes anywhere; items are dated from help-article timestamps (Likely at best). Re-check for a changelog launch.
- Cornerstone OnDemand: the Workforce AI "What's New" keeps only the current month (prior months 404). Run every month or that month's notes are lost.
- Leapsome: hub entries are batch-published with back-dated displayDates. Re-pull the hub at run time; a run in a month's first days misses late-month items.
- Perceptyx: the blog RSS holds only 10 items. Page https://blog.perceptyx.com/page/2 for a full month.
- Lattice: help center migrated off Zendesk (now https://help.lattice.com/en-us/), with no sitemap. Dated items come from the monthly roundup.
- Calendar: Workday Rising (2026-10-12 to 10-15) and HR Tech (2026-10-20 to 10-22) both land in October. Run the October report after 2026-10-22 and expect high volume.
```

---

## Data (YAML)
```yaml
version: "3.0"

competitors:
  - name: "15Five"
    aliases: ["Kona", "Emplify (acquired)", "15Five Engage", "15Five Perform", "Amaya"]
    website: "https://www.15five.com/"
    news_query: "\"15Five\""
    sources:
      # PRIMARY: live "What's new" running list, read through the public Zendesk Help Center API
      # (one article; month headers "September 2026 Releases"; each item says "Released <Month> <day>").
      - kind: release_notes
        url: "https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases"
        route: zendesk_article
        flags: ["running_list"]
        verified: "2026-10-13"
      # Newest-created help articles: new features get new "Feature Overview" articles.
      - kind: help_center
        url: "https://success.15five.com/hc/en-us"
        route: zendesk_recent
        flags: ["index"]
        verified: "2026-10-13"
      # Discovery/lead only — never fetched or cited.
      - kind: social
        url: "https://www.linkedin.com/products/15five/"
        flags: ["search_required"]

  - name: "Culture Amp"
    aliases: []
    website: "https://www.cultureamp.com/"
    news_query: "\"Culture Amp\""
    sources:
      # PRIMARY: public product-updates newsfeed (Intercom News). Server-rendered; JSON-LD carries a
      # per-post permalink for every card (https://updates.cultureamp.com/<id>-<slug>): cite those, not
      # the feed root. No public RSS exists (verified 2026-06-04: /rss, /feed, /feed.rss all 404).
      - kind: product_updates
        url: "https://updates.cultureamp.com"
        route: intercom_news
        flags: ["running_list"]
        verified: "2026-10-13"
      # Help-center collection; feature docs linked from newsfeed posts.
      - kind: help_center
        url: "https://support.cultureamp.com/en/collections/3904790-product-updates"
        flags: ["index", "undated"]
        verified: "2026-10-13"
      # Corporate/product announcements live at https://www.cultureamp.com/company/announcements/<slug>
      # (JSON-LD datePublished), e.g. the MCP launch (2026-08-24): .../culture-intelligence-in-daily-tools.
      # Removed 2026-10-13: 2026-product-updates collection (404) and the five 2025/2026 year-pinned
      # help articles (stale since 2026-07); intercom.news/culture-amp mirrors the primary.

  - name: "Gallup"
    aliases: ["Gallup Access", "Q12", "CliftonStrengths"]
    website: "https://www.gallup.com/"
    # Generic name: restrict the press sweep to the workplace product.
    news_query: "\"Gallup Access\" OR (\"Gallup\" (Q12 OR \"employee engagement\" OR CliftonStrengths) (launch OR app OR platform OR feature))"
    sources:
      # PRIMARY (found 2026-10-13): dated "Gallup Product Updates" section. HTML and Atom are
      # Cloudflare-403'd; the public Help Center API reads it cleanly. Closes the long-standing
      # "no dated public changelog" gap.
      - kind: release_notes
        url: "https://support.gallup.com/hc/en-us/sections/53122467937811-Gallup-Product-Updates"
        route: zendesk_section
        flags: ["bot_blocked"]
        verified: "2026-10-13"
      - kind: help_center
        url: "https://support.gallup.com/hc/en-us"
        route: zendesk_recent
        flags: ["index", "bot_blocked"]
        verified: "2026-10-13"

  - name: "Lattice"
    aliases: []
    website: "https://lattice.com/"
    # Generic name: exclude Lattice Semiconductor and other "lattice" noise.
    news_query: "\"Lattice\" (HR OR \"performance management\" OR employees OR \"Sarah Franklin\") -semiconductor -FPGA"
    sources:
      # PRIMARY: dated monthly roundup, published on the month's last day (e.g. 2026-09-30).
      - kind: blog
        url: "https://lattice.com/blog/{month}-{year}-product-updates"
        route: monthly_url
        flags: ["running_list"]
        verified: "2026-10-13"
      # Product Updates blog category: catches seasonal launch/roadmap posts
      # (e.g. .../blog/fall-winter-2026-product-release, 2026-09-02) between roundups.
      - kind: blog
        url: "https://lattice.com/blog?category_equal=%5B%22Product+Updates%22%5D"
        flags: ["index"]
        verified: "2026-10-13"
      - kind: product_updates
        url: "https://lattice.com/product-updates"
        flags: ["index", "undated"]
        verified: "2026-10-13"
      # Help center migrated off Zendesk by 2026-10 (old /hc/en-us root 404s; old /hc/... article links
      # redirect to /en-us/articles/<id>-<slug>). No sitemap; use for feature docs, not dates.
      - kind: help_center
        url: "https://help.lattice.com/en-us/"
        flags: ["index", "undated"]
        verified: "2026-10-13"

  - name: "Microsoft Viva / Glint"
    aliases: ["Viva Glint", "Glint"]
    website: "https://www.microsoft.com/"
    news_query: "\"Viva Glint\""
    sources:
      # PRIMARY: TechCommunity board RSS; carries full post bodies ("News to Know", monthly).
      # pubDate is the LAST EDIT time: take publish dates from the post page (datePublished).
      - kind: feed
        url: "https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=viva_glint_blog"
        route: rss
        verified: "2026-10-13"
      # Blog index (curl reads it; the old "bot_blocked / title only" was a WebFetch artifact and a
      # gzip-encoded body). Dated cross-check: M365 Roadmap API
      # https://www.microsoft.com/releasecommunications/api/v1/m365 (filter titles on "Glint").
      - kind: blog
        url: "https://techcommunity.microsoft.com/category/viva-glint/blog/viva_glint_blog"
        flags: ["index"]
        verified: "2026-10-13"
      # Some Glint launches post on the Microsoft 365 board, not the Glint board (e.g. the survey-data
      # export APIs, 2026-09-02). Filter items on "Glint".
      - kind: feed
        url: "https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=microsoft_365blog"
        route: rss
        verified: "2026-10-13"

  - name: "Peakon / Workday"
    aliases: ["Workday Peakon Employee Voice", "Peakon Employee Voice", "Workday", "Sana"]
    website: "https://www.workday.com/"
    news_query: "\"Peakon\" OR (\"Workday\" (Peakon OR \"employee voice\" OR talent OR Sana OR agents))"
    sources:
      # PRIMARY (Peakon): the 2026 year index renders JS-empty, but any release-note child page embeds
      # a nav tree (JSON) linking every note with its date in the URL (89 links, 2025-2026, on 2026-10-13).
      - kind: release_notes
        url: "https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026/june/wednesday--10th-june.html"
        route: dated_links
        flags: ["index"]
        verified: "2026-10-13"
      # PRIMARY (Workday platform/talent): Cision MediaRoom list, dated in each link (?l=100 = full list;
      # the ?pagetemplate=rss feed carries only the 5 newest).
      - kind: newsroom
        url: "https://newsroom.workday.com/press-releases?l=100"
        route: dated_links
        flags: ["index"]
        verified: "2026-10-13"
      # Feature lists per release (R1/R2) without login; production dates need a partner deck or
      # customer IT notice (Release Center is login-only). Corporate/M&A: 8-K item codes at
      # https://data.sec.gov/submissions/CIK0001327811.json (read filings via WebFetch; www.sec.gov
      # blocks undeclared tools).
      - kind: docs
        url: "https://community-content.workday.com/en-us/public/feature-release/workday-success-plans--feature-release-reviews/2026r2-feature-release-review-webinars/2026r2-workday-peakon-employee-voice.html"
        flags: ["year_pinned", "undated"]
        verified: "2026-10-13"

  - name: "Qualtrics"
    aliases: ["Qualtrics XM", "Qualtrics EmployeeXM"]
    website: "https://www.qualtrics.com/"
    news_query: "\"Qualtrics\" (EmployeeXM OR \"employee experience\" OR EX OR launch OR unveils)"
    sources:
      # PRIMARY: weekly product release notes. Index and every weekly note were public on 2026-10-13
      # (the old "login" label did not reproduce). Operative date = the note's "Features Released On
      # Or Before <date>" section; "Starting On & After" is next week's preview. No RSS (all paths 404);
      # the sitemap lists placeholder topic IDs that 404, so follow the index links, don't guess IDs.
      - kind: release_notes
        url: "https://community.qualtrics.com/product-release-notes-96"
        flags: ["index"]
        verified: "2026-10-13"
      - kind: newsroom
        url: "https://www.qualtrics.com/news/"
        flags: ["index"]
        verified: "2026-10-13"

  - name: "SurveyMonkey"
    aliases: ["Momentive"]
    website: "https://www.surveymonkey.com/"
    news_query: "\"SurveyMonkey\""
    sources:
      # PRIMARY: What's New now carries per-item dates (it did not in 2026-07).
      - kind: product_updates
        url: "https://www.surveymonkey.com/product/features/whats-new/"
        verified: "2026-10-13"
      - kind: newsroom
        url: "https://www.surveymonkey.com/newsroom/"
        flags: ["index"]
        verified: "2026-10-13"
      # Discovery: new feature docs (e.g. Workday/BambooHR HRIS integrations, first published
      # 2026-09-28) never reached the release notes. lastmod is an edit date; read the page's embedded
      # CMS "date" field for first publish.
      - kind: docs
        url: "https://help.surveymonkey.com/sitemap-en.xml"
        route: sitemap
        flags: ["index"]
        verified: "2026-10-13"
      - kind: release_notes
        url: "https://help.surveymonkey.com/en/surveymonkey/new/release-notes/"
        flags: ["stale"]
        verified: "2026-10-13"

  - name: "ADP"
    aliases: ["ADP Workforce Now", "ADP SmartCompliance", "ADP Assist", "ADP Lyric", "StandOut"]
    website: "https://www.adp.com/"
    # Unqualified "ADP" returns fantasy-football ADP and the National Employment Report.
    news_query: "\"ADP\" (\"ADP Assist\" OR \"Workforce Now\" OR Lyric OR StandOut OR \"human capital\") -fantasy -football"
    sources:
      # Cision MediaRoom: dated press list (www.adp.com newsroom returns 403). In-product release notes
      # are login-only, so in-product changes stay Unknown.
      - kind: newsroom
        url: "https://mediacenter.adp.com/press-releases?l=100"
        route: dated_links
        flags: ["index"]
        verified: "2026-10-13"

  - name: "BambooHR"
    aliases: ["Bamboo AI"]
    website: "https://www.bamboohr.com/"
    news_query: "\"BambooHR\""
    sources:
      # PRIMARY: product-updates RSS (578 dated items on 2026-10-13). The HTML hub is a JS shell.
      # Full index with productArea (maps to QW packages) and planType:
      # https://www.bamboohr.com/product-updates/query-index.json . Child pages carry a meta
      # publication-date. Newsroom paths 404: find press via the --news sweep (GlobeNewswire).
      - kind: feed
        url: "https://www.bamboohr.com/product-updates/feed/"
        route: rss
        verified: "2026-10-13"
      # AI connector / MCP status (beta vs GA).
      - kind: docs
        url: "https://documentation.bamboohr.com/docs/mcp-server"
        flags: ["undated"]
        verified: "2026-10-13"

  - name: "Betterworks"
    aliases: ["Betterworks NextGen", "Betterworks Classic"]
    website: "https://www.betterworks.com/"
    news_query: "\"Betterworks\""
    sources:
      # PRIMARY: bi-weekly "Release: <date>" notes. /hc/ HTML and the section Atom feed 403 on curl and
      # WebFetch (every run since 2026-05); the public Help Center API returns all of them, dated.
      # Seasonal roll-ups ("Summer Release - September 2026") re-list earlier features: de-dup them
      # against the bi-weekly notes, and watch those notes for pre-announced go-live dates.
      - kind: release_notes
        url: "https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes"
        route: zendesk_section
        flags: ["index", "bot_blocked"]
        verified: "2026-10-13"
      # Discovery: real per-URL lastmods surface launch posts (/magazine/<season>-<year>-product-release)
      # and root-level press releases. lastmod is an edit date.
      - kind: docs
        url: "https://www.betterworks.com/sitemap.xml"
        route: sitemap
        flags: ["index"]
        verified: "2026-10-13"
      # Dated press index. Business Wire is walled to curl and WebFetch; Betterworks hosts identical
      # copies at https://www.betterworks.com/<release-slug> (text there, date from this index).
      - kind: newsroom
        url: "https://www.betterworks.com/press"
        flags: ["index"]
        verified: "2026-10-13"
      # Mobile: Apple iTunes lookup API dates app launches that appear in no release note
      # (new NextGen app 1.0 released 2026-09-08).
      - kind: docs
        url: "https://itunes.apple.com/lookup?id=6795434862&country=us"
        route: json_api
        cite: "https://apps.apple.com/us/app/betterworks/id6795434862"
        verified: "2026-10-13"

  - name: "Cornerstone OnDemand"
    aliases: ["CSOD", "Cornerstone", "Cornerstone Workforce AI"]
    website: "https://www.cornerstoneondemand.com/"
    news_query: "\"Cornerstone OnDemand\" OR \"Cornerstone Workforce AI\""
    sources:
      # PRIMARY (found 2026-10-13): Workforce AI monthly "What's New" on a MadCap Flare help site. The
      # shell is JS-empty, but the TOC chunk lists every release topic (/Content/Release/<MonYYYY>/<Topic>.htm,
      # server-rendered; "Last Published" footer gives the day). ONLY THE CURRENT MONTH IS RETAINED: prior
      # months 404, so a skipped month is lost. Freshness: https://help.csod.com/cwfai/Data/HelpSystem.xml (BuildTime).
      - kind: release_notes
        url: "https://help.csod.com/cwfai/Data/Tocs/PrimaryTOC_Chunk0.js"
        route: dated_links
        base: "https://help.csod.com/cwfai/"
        cite: "https://help.csod.com/cwfai/Content/WhatsNew.htm"
        flags: ["running_list"]
        verified: "2026-10-13"
      # Classic platform (Galaxy / Single Architecture): dated change log incl. bi-weekly patches.
      - kind: release_notes
        url: "https://help.csod.com/sa/Content/SingleArchitecture/Whats_New/ChangeLog_for_SA.htm"
        flags: ["running_list"]
        verified: "2026-10-13"
      # Press: per-URL lastmod (watch for bulk edits of old pages; read the on-page date).
      - kind: newsroom
        url: "https://www.cornerstoneondemand.com/sitemaps/press/sitemap.xml"
        route: sitemap
        verified: "2026-10-13"
      # Release articles land in resources; the news listing is client-rendered (Algolia).
      - kind: blog
        url: "https://www.cornerstoneondemand.com/resources/topics/cornerstone-news/"
        flags: ["index", "ui_dynamic"]

  - name: "Energage"
    aliases: ["Top Workplaces platform", "Energage + Engagedly"]
    website: "https://www.energage.com/"
    # Unqualified "Energage" returns Top Workplaces award coverage.
    news_query: "\"Energage\" (launch OR platform OR product OR Engagedly OR integration)"
    sources:
      # No public product changelog: the help center is in-app (login) and energage.zendesk.com is closed.
      # Post-merger joint product news is most likely to appear on Engagedly's changelog (see Engagedly).
      - kind: blog
        url: "https://www.energage.com/feed/"
        route: rss
        flags: ["search_required"]
        verified: "2026-10-13"

  - name: "Engagedly"
    aliases: ["Marissa AI"]
    website: "https://engagedly.com/"
    news_query: "\"Engagedly\""
    sources:
      # PRIMARY: Beamer changelog backend (the changelog.engagedly.com page is JS-only; no RSS exists).
      # Dated entries with permalinks; page=N for more. Product id is in the page's inline script.
      - kind: release_notes
        url: "https://changelog.engagedly.com/loadMoreNews?app_id=mZiIYhKZ41992&language=EN&publicPage=true&page=0"
        cite: "https://changelog.engagedly.com"
        verified: "2026-10-13"
      # Press-releases category (WordPress REST; category 472). The "Product Updates" category (460)
      # is stale since 2024-05-31.
      - kind: newsroom
        url: "https://engagedly.com/wp-json/wp/v2/posts?categories=472"
        route: wp_json
        verified: "2026-10-13"
      - kind: help_center
        url: "https://help.engagedly.com/"
        flags: ["index", "undated"]
        verified: "2026-10-13"

  - name: "Leapsome"
    aliases: ["Leapy"]
    website: "https://www.leapsome.com/"
    news_query: "\"Leapsome\""
    sources:
      # PRIMARY (found 2026-10-13): the public Product Updates Hub at
      # https://www.leapsome.com/app/#/product-updates (the app marks the route public: no login) reads
      # this public JSON endpoint: 264 dated entries, displayDate = operative date (UTC; the tool converts
      # to CT). Entries are batch-published with back-dated displayDates, so re-pull at run time; a run in
      # the first days of a month can miss late-month items. Also accepts module=, featured=true, aiFeature=true.
      - kind: feed
        url: "https://www.leapsome.com/api/release-notes?page=1&limit=100"
        route: json_api
        cite: "https://www.leapsome.com/app/#/product-updates"
        verified: "2026-10-13"
      # Help center: corroboration via the public Zendesk search API (HTML 403s).
      - kind: help_center
        url: "https://help.leapsome.com/hc/en-us"
        route: zendesk_recent
        flags: ["index", "bot_blocked"]
        verified: "2026-10-13"
      - kind: roadmap
        url: "https://leapsome.notion.site/leapsome/Leapsome-s-Product-Roadmap-c914ffc89c824e7db33130f3cc5bfb1f"
        flags: ["ui_dynamic"]
      # Removed 2026-10-13: "Platform improvements" running list (help.leapsome.com article 360004361834;
      # frozen at 2026-02-16, now points to the hub) and the monthly blog roundup pattern
      # site.leapsome.com/blog/product-updates-<mon>-<year> (discontinued after April 2026).
      # Blog JSON-LD dates and www.leapsome.com sitemap lastmods are republish/bulk stamps: never operative dates.

  - name: "Officevibe (Workleap)"
    aliases: ["Workleap Officevibe", "Workleap", "Workleap Agent", "Pingboard", "Team Health & Feedback"]
    website: "https://workleap.com/officevibe"
    news_query: "\"Workleap\" OR \"Officevibe\""
    sources:
      # No release notes, changelog, RSS, or what's-new page anywhere (changelog.workleap.com does not
      # resolve; /whats-new etc. 404). Product changes surface only as new Intercom help articles: filter
      # by lastmod, read lastUpdatedDate from each article's embedded JSON. Undated releases: date them by
      # doc timestamps (Confidence: Likely at best).
      - kind: help_center
        url: "https://help.workleap.com/sitemap.xml"
        route: sitemap
        flags: ["index", "search_required"]
        verified: "2026-10-13"
      # De facto AI changelog: https://help.workleap.com/en/collections/13569920-workleap-ai
      # (Workleap Agent / MCP articles with lastUpdated stamps).
      - kind: newsroom
        url: "https://www.prnewswire.com/news/workleap/"
        flags: ["index", "press"]
        verified: "2026-10-13"
      # On-page "Published on" dates; ignore Webflow JSON-LD dates (site-rebuild stamps).
      - kind: blog
        url: "https://workleap.com/category/news"
        flags: ["index"]
        verified: "2026-10-13"

  - name: "Paylocity"
    aliases: ["Ignite AI"]
    website: "https://www.paylocity.com/"
    news_query: "\"Paylocity\""
    sources:
      # Monthly roundup moved to /resources/learn/blogs/whats-new-blog-<month>-<year>/ (August 2026
      # edition published 2026-09-16). Every paylocity.com path serves a Cloudflare JS interstitial to
      # curl and renders empty to WebFetch; investors.paylocity.com and GlobeNewswire return Akamai 403.
      - kind: blog
        url: "https://www.paylocity.com/resources/learn/blogs/whats-new-blog-{month}-{year}/"
        route: monthly_url
        flags: ["bot_blocked", "ui_dynamic"]
      # Third-party aggregator with dated full text and official links: discovery only, cite the official URL.
      - kind: aggregator
        url: "https://releasebot.io/updates/paylocity/paylocity"
        verified: "2026-10-13"

  - name: "Perceptyx"
    aliases: ["Cultivate", "Humu"]
    website: "https://www.perceptyx.com/"
    news_query: "\"Perceptyx\""
    sources:
      # PRIMARY: one dated "Release Notes | <Month YYYY>" article per month (LISTEN / ANALYZE / ACT /
      # PLATFORM), published early the following month. Read fine on 2026-10-13; the old "bot_blocked"
      # label did not reproduce.
      - kind: release_notes
        url: "https://perceptyxhelp.freshdesk.com/support/solutions/folders/63000237891"
        flags: ["index"]
        verified: "2026-10-13"
      # Launch announcements (e.g. Perceptyx Anywhere, 2026-09-29). RSS holds only the 10 newest
      # posts: page https://blog.perceptyx.com/page/2 to cover a whole month.
      - kind: feed
        url: "https://blog.perceptyx.com/rss.xml"
        route: rss
        verified: "2026-10-13"
      # MCP / Perceptyx Anywhere state (undated product page: which parts are GA vs design-partner).
      - kind: docs
        url: "https://go.perceptyx.com/platform/mcp"
        flags: ["undated"]
        verified: "2026-10-13"

  - name: "PerformYard"
    aliases: ["PerformYard Talent Development", "Ask PerformYard"]
    website: "https://www.performyard.com/"
    news_query: "\"PerformYard\""
    sources:
      # No changelog, RSS, newsroom, or what's-new page (all 404). Launches land as dated articles
      # (e.g. /articles/introducing-performyard-talent-development, 2026-09-01); the site sitemap has real
      # per-URL lastmods and surfaces them.
      - kind: docs
        url: "https://www.performyard.com/sitemap.xml"
        route: sitemap
        flags: ["index"]
        verified: "2026-10-13"
      # Help Scout Docs (not Zendesk: the Zendesk API routes do not apply). New article IDs + lastmod
      # reveal new features; articles show "Last updated on <date>" only.
      - kind: help_center
        url: "https://support.performyard.com/sitemap.xml"
        route: sitemap
        flags: ["index"]
        verified: "2026-10-13"
      # Removed 2026-10-13: https://www.prweb.com/ (a press-wire homepage, not a PerformYard source;
      # the --news sweep covers press).

  - name: "Predictive Index"
    aliases: ["The Predictive Index", "PI", "PI Perform", "Obi"]
    website: "https://www.predictiveindex.com/"
    news_query: "\"Predictive Index\" OR \"PI Perform\""
    sources:
      # PRIMARY: release notes; each entry has an explicit "Date released" and an M/D/YYYY title.
      # Entries labelled "Tentative release window" are roadmap, not shipped.
      - kind: release_notes
        url: "https://docs.predictiveindex.com/en/collections/12282995-release-notes"
        flags: ["index"]
        verified: "2026-10-13"
      # Watch: MCP connector docs (pre-beta as of 2026-10; not in the release notes).
      - kind: docs
        url: "https://docs.predictiveindex.com/en/collections/19719980-the-predictive-index-mcp"
        flags: ["index", "undated"]
        verified: "2026-10-13"
      # Press: the newsroom path is /news-press/news/ (/newsroom/ and /press/ 404); its news sitemap is dated.
      - kind: newsroom
        url: "https://www.predictiveindex.com/news-sitemap.xml"
        route: sitemap
        verified: "2026-10-13"
      - kind: feed
        url: "https://www.predictiveindex.com/feed/"
        route: rss
        verified: "2026-10-13"

  - name: "UKG"
    aliases: ["UKG Ready", "UKG Pro", "UKG Pro WFM", "Kronos", "UKG Bryte", "People Assist"]
    website: "https://www.ukg.com/"
    # Unqualified "UKG" returns UK garage music and kindergarten ("UKG") noise.
    news_query: "\"UKG\" (site:businesswire.com OR \"UKG Pro\" OR \"UKG Ready\" OR Bryte OR \"People Assist\")"
    sources:
      # Newsroom (dated cards). Readable through tools/ci_sources.py's plain urllib client on 2026-10-13,
      # while curl and WebFetch get a Cloudflare managed challenge on all of www.ukg.com: different clients
      # get different answers. Never try to solve the challenge. Business Wire blocks curl and WebFetch;
      # read full release text via FinancialContent syndication:
      # https://investor.wedbush.com/wedbush/article/bizwire-<YYYY>-<M>-<D>-<title-slug>
      - kind: newsroom
        url: "https://www.ukg.com/company/newsroom"
        flags: ["index"]
        verified: "2026-10-13"
```
