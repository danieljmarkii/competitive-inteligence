# CI Data-Quality Improvement Proposal — DRAFT for review

> **Status:** DRAFT · not yet adopted. Nothing in `CI-Prompt.md`, `CI-Competitor.md`, or `CI-Context.md` has been changed.
> **Author:** CI run (Claude Code) · **Date:** 2026-06-04 · **Prompted by:** two pages the user found by hand (15Five + Culture Amp) that the May run missed.
> **Ask:** review the diagnosis and the proposed fixes; tell me which to implement and answer the open questions in §7.

---

## 0. The trigger

You found two live, dated, in-window pages by ordinary Googling:

- 15Five — `https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases` (your screenshot shows **May 2026 releases**: Custom Automated Review Schedules 05-20, Manager Display Name 05-19, **HRIS Sync 2.0 05-14**, Download All Survey Results as Zip 05-05).
- Culture Amp — `https://updates.cultureamp.com` (your screenshot shows **Self-Service SAML/SSO Configuration, May 14 2026**).

Both fell into the May report's "Unknown — access-limited" bucket. Fair question: why did a human with a search box beat the workflow? The answer is specific and mostly **infrastructural**, not a failure of the methodology files.

---

## 1. Diagnosis — four stacked causes

### Cause A (root): this environment blocks *all* outbound page fetches
I reproduced it today. `WebFetch` returned **HTTP 403 on every URL I tried** — not just the vendor pages, but `example.com`, `en.wikipedia.org`, and `lattice.com`. When unrelated domains all 403 identically, it is the **remote execution environment's outbound network policy**, not vendor bot-walls. (Same finding as the May run; see `CI-Run-Notes-2026-05.md` §1.)

**Implication:** in this environment the agent literally cannot *open* a web page. When you Google-and-click you read the fully rendered HTML; the workflow was limited to search-result snippets. It was researching blindfolded. This is the single biggest reason the two pages were missed — not the URLs in the file.

### Cause B: the `WebSearch`-only fallback is structurally weak for changelogs
Even with search working, the fallback misleads in three ways I confirmed today:

1. **It doesn't surface the best page.** Searching Culture Amp updates repeatedly returned `support.cultureamp.com/...` and never `updates.cultureamp.com`. The clean public newsfeed you found isn't well-indexed for the queries the workflow generates — you only reach it if you already know the subdomain.
2. **It misdates items.** A search for the 15Five HRIS Sync release told me, confidently, that HRIS Sync 2.0 shipped **"April 29th."** Your screenshot of the actual page says **"Released May 14th."** A two-week error that would wrongly push a real in-window item out of the window.
3. **Running-list / changelog content doesn't compress into snippets.** These pages are long, JS-rendered, multi-entry. The one-paragraph search summary can't represent a month of dated bullets, so most items never appear at all.

### Cause C: the chicken-and-egg that makes B worse
WebSearch *can* find these items — but only with **feature-specific** queries. When I searched `Culture Amp SAML SSO self-service May 2026`, it correctly returned the May 14 item. The catch: you can only name "SAML SSO self-service" if you've already read the changelog. The feature names live on exactly the pages the environment won't let us open. So the high-yield queries are unreachable precisely when we need them.

### Cause D: secondary source-curation gaps (real, but not the main story)
Two fixable data issues in `CI-Competitor.md`:

- **15Five points at a stale article ID.** File has `.../articles/36062624232219-...`; your working page is `.../articles/50989471559067-...`. The old ID is what search indexes, but it appears to be superseded. Worth promoting the live one (once we can fetch to confirm it's canonical and not a fork).
- **Culture Amp is missing its best surface.** The file lists four `support.cultureamp.com` collections, `intercom.news/culture-amp`, and four 2025 year-pinned pages — but **not** `updates.cultureamp.com`, which is the cleanest, most machine-readable public changelog.

> Bottom line: even with perfect URLs, Cause A means the run still can't read them here. Fixing A unlocks the most. C and D are real and cheap. B is mitigated by the multi-channel design in §3.

---

## 2. Fix Layer 1 — unblock fetching (highest leverage)

Nothing else matters as much as restoring the ability to read a page. Options, roughly in order of preference:

1. **Run `/ci-report` where outbound fetch is allowed.** Either (a) local Claude Code on a machine with normal network, or (b) a web/cloud environment configured with a more permissive network policy. Network policy is chosen when the environment is created — see https://code.claude.com/docs/en/claude-code-on-the-web. **This is the recommended primary fix.**
2. **Add a fetch path that isn't subject to the 403 policy** — e.g., an MCP-provided fetch/proxy tool, or a render/scrape API (Firecrawl/Jina-style "reader" endpoints) wired in as an MCP server. The agent calls the MCP tool instead of `WebFetch`.
3. **Treat email as the fetch channel** (see §3, channel 2) — sidesteps the block entirely because the vendor pushes content to an inbox we *can* read via the Gmail MCP.

If we cannot change the environment, options 2 and 3 become the primary plan rather than a backstop.

---

## 3. Fix Layer 2 — multi-channel listening (the redundancy you asked about)

Today the workflow is single-channel: one or two HTML pages per vendor, read by one fetch tool. If that tool or page fails, the vendor goes dark. A resilient design listens on several channels and **cross-confirms**. Ranked by signal quality × robustness × effort:

**Channel 1 — RSS / JSON changelog feeds (highest value, do first).**
Many "product update" pages are hosted on changelog platforms (Beamer, AnnounceKit, Headway, Intercom, Productboard, Canny) that expose a machine-readable `/rss`, `.atom`, or `.json` feed. Feeds are dated, structured, one-entry-per-item, and frequently *not* behind the same JS/bot wall as the HTML. `updates.cultureamp.com` looks like a hosted changelog and very likely has a feed (need a fetch to confirm the exact path). **Action:** for each vendor, locate and store a feed URL alongside the HTML source; prefer the feed for collection.

**Channel 2 — vendor email digests into a dedicated inbox (most robust here).**
Subscribe a project mailbox to each vendor's "What's New" / product-update newsletter. The vendor then *pushes* dated release notes to us; the agent reads them with the **Gmail MCP** (already connected in this environment), which is unaffected by the `WebFetch` 403. This is the one channel that is bot-block-proof and fetch-policy-proof by construction. Cost: a one-time subscribe per vendor and ~one cycle to populate; a few vendors gate newsletters behind a real account.

**Channel 3 — social (LinkedIn / X) as a *lead* layer, not a primary source.**
Your instinct is right that vendors announce launches socially — but social is noisy, marketing-skewed, and hard to date precisely. Best use: **discovery**. A LinkedIn/X post tells us *that* something shipped and *what it's called*; we then pull the official dated doc (Cause C dissolves, because social hands us the feature name to search). `CI-Prompt.md` already treats social as discovery-only (Runtime Discovery §4); this proposal would formalize it as a standing lead channel rather than a last resort. Practical access: company-page posts via search; a social-listening MCP/API if we want it automated.

**Channel 4 — press wires (secondary, already partly used).**
PRNewswire/BusinessWire/PRWeb catch the *big* launches (this is how the May run got Cornerstone Workforce AI and Perceptyx Develop). Keep as corroboration for high-impact items; weak for routine releases.

**Channel 5 — third-party aggregators & analyst coverage (corroboration).**
Release-note trackers, G2/Capterra "what's new," and analyst blogs (Reworked, Josh Bersin) can confirm dates and fill gaps. Downgrade confidence unless tied to an official page.

**How the channels combine:** feed/email = primary dated evidence → social/press/aggregator = lead generation + corroboration → official doc = citation of record. One change can surface on three channels; we still keep **one record per change** (existing de-dup hierarchy in `CI-Prompt.md`).

---

## 4. Fix Layer 3 — source-curation hygiene (cheap wins)

- Promote `updates.cultureamp.com` into Culture Amp's `sources` (and find its feed for Channel 1).
- Replace/duplicate the 15Five release-notes URL with the live article ID `50989471559067` once a fetch confirms it's canonical.
- Add a `feed` kind (or a `feed_url` field) to the source schema so RSS/JSON endpoints are first-class, not buried.
- Continue the existing Source-Health discipline: the run proposes, a human promotes (no silent YAML rewrites).

---

## 5. Fix Layer 4 — methodology tweaks for `CI-Prompt.md`

Small edits that would have helped this month:

1. **Feed-first collection order:** try `feed_url` → HTML source → search fallback.
2. **Snippet-date distrust rule:** when operating in search-only mode, never accept a release **date** from a search *summary*; require the date to appear in an indexed page title/snippet, else mark `Date: Unknown` (don't guess in *either* direction — the HRIS Sync "April 29" error cut both ways).
3. **Known-changelog probe:** for each vendor, try the common changelog subdomains/paths (`updates.<domain>`, `whatsnew.<domain>`, `<domain>/changelog`, `/release-notes`) during discovery.
4. **Two-pass discovery for the chicken-and-egg:** pass 1 harvest *feature names* from feeds/social/aggregators; pass 2 run feature-specific searches to pin official date + source.

---

## 6. Per-vendor quick wins (illustrative, not exhaustive)

- **15Five** → live article `...50989471559067...`; check for a `/hc` feed; subscribe to product email.
- **Culture Amp** → add `updates.cultureamp.com` + its feed; keep year-pinned 2025 pages for history only.
- **Lattice** → already on the good dated blog template `lattice.com/blog/<month>-<year>-product-updates`; add its blog RSS.
- **Viva/Glint, Perceptyx, Leapsome, Paylocity, SurveyMonkey, Cornerstone** → §5 of the run notes already proposes better dated surfaces; layer feeds/email on top.

---

## 7. Open questions for you

1. **Environment:** can we run `/ci-report` somewhere with outbound fetch (local, or a more permissive web policy)? That's the highest-leverage fix and changes how much of the rest we need.
2. **Email channel:** OK to stand up a dedicated mailbox and subscribe it to vendor newsletters, then have the run read it via the Gmail MCP? (Most robust option in *this* environment.)
3. **Social scope:** do you want active social listening, and if so which surface (LinkedIn company pages? X?) — and is an automated MCP/API acceptable, or keep it manual-lead-only?
4. **Schema change:** comfortable adding a `feed`/`feed_url` concept to `CI-Competitor.md`? It's the cleanest enabler for Channel 1.
5. **Scope of this PR:** should I keep this as a proposal doc only, or also land the two safe curation fixes now (add `updates.cultureamp.com`; flag the 15Five article-ID swap as a Source-Health suggestion)?

---

## 8. Suggested phasing

- **Phase 0 (now):** this draft + the two Source-Health curation notes. No methodology change.
- **Phase 1:** unblock fetch (env or MCP fetch tool) — restores baseline.
- **Phase 2:** add feed URLs per vendor + feed-first collection order in `CI-Prompt.md`.
- **Phase 3:** stand up the email inbox channel via Gmail MCP.
- **Phase 4:** formalize social as a standing lead channel; optional automation.
