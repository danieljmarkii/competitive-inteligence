# Source Health history, 2026-05 to 2026-07 runs (archived)

> Archived from `CI-Competitor.md` on 2026-10-13, when the registry moved to self-curation (CI-Competitor.md v3.0, CI-Prompt.md v4.0).
> These were per-run Source Health logs whose suggested replacements were never promoted. The 2026-09 run (see `reports/2026-09-CI-Report.md` → Workflow Retro) promoted or closed every one of them. Kept verbatim for audit; do not edit.
> From 2026-09 onward, each run's Source Health and Workflow Retro live in its own `reports/<YYYY-MM>-CI-Report.md`.

### 2026-07 run (observed 2026-08-03, full run)
> `WebFetch` live all run. Direct fetch clean for Culture Amp, 15Five, Predictive Index, Perceptyx (blog), Engagedly (blog), Leapsome (blog), Lattice hub. `WebSearch` route-arounds recovered Betterworks, Qualtrics, Viva Glint, Paylocity, BambooHR, Cornerstone. **Environment note: `web.archive.org` is unreachable from this environment — the Wayback route-around is unavailable; snippet-recovery is the working fallback for hard 403s.** Full detail in `reports/2026-07-CI-Report.md` → Source Health.

```text
VERIFIED-GOOD primaries this run (keep):
- Culture Amp | https://updates.cultureamp.com | fetched clean, dated (newest 2026-07-24)
- 15Five | https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases | fetched clean, dated (updated 2026-07-24)
- Predictive Index | https://docs.predictiveindex.com/en/collections/12282995-release-notes | fetched clean, dated
- Perceptyx | https://blog.perceptyx.com | fetched clean, dated — better than the bot-walled Freshdesk folder

Blocked / stale / gaps this run:
- Betterworks | https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026 | status: bot_blocked | observed: 2026-08-03
  Suggested replacement (if found): none stable — section Atom feed also 403s; content recovered via search-indexed snippets
- Microsoft Viva / Glint | https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463 | status: bot_blocked | observed: 2026-08-03
  Suggested replacement (if found): none — title renders, body doesn't; recovered via WebSearch (same as 2026-05)
- Qualtrics | https://community.qualtrics.com/product-release-notes-96 | status: login | observed: 2026-08-03
  Suggested replacement (if found): weekly note pages indexed with rich snippets, e.g. .../weekly-product-release-notes-july-22-2026-33475
- Leapsome | https://site.leapsome.com/blog/product-updates-<mon>-<year> (pattern) | status: stale | observed: 2026-08-03
  Suggested replacement (if found): monthly-roundup slugs appear discontinued (jul-2026/july-2026 both 404) — treat https://site.leapsome.com/blog as the index; July launch post: https://site.leapsome.com/blog/leapsome-ai-people-data-foundation
- Lattice | https://lattice.com/blog/july-2026-product-updates | status: 404 | observed: 2026-08-03
  Suggested replacement (if found): not a wall — July roundup not yet published at run date; hub fetched clean. Recheck mid-August.
- Workday Peakon | https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026.html | status: bot_blocked (JS-empty) | observed: 2026-08-03
  Suggested replacement (if found): month child pages resolve when published (e.g. .../2026/june/wednesday--10th-june.html); July pages 404 — likely not yet published
- SurveyMonkey | https://help.surveymonkey.com/en/surveymonkey/new/release-notes/ | status: stale (newest entry 2026-02) | observed: 2026-08-03
  Suggested replacement (if found): https://www.surveymonkey.com/product/features/whats-new/ (live seasonal roundup, undated per-item — pair with newsroom for dates)
- Officevibe (Workleap) | https://help.workleap.com/en/ | status: replaced | observed: 2026-08-03
  Suggested replacement (if found): still none — no live Workleap what's-new surface found; curation gap persists
- Engagedly | https://changelog.engagedly.com | status: bot_blocked | observed: 2026-08-03
  Suggested replacement (if found): https://engagedly.com/blog/ (dated corporate posts fetch clean)
- Paylocity | https://www.paylocity.com/company/about-us/newsroom/in-the-news/whats-new-july-2026/ | status: bot_blocked (JS-empty) | observed: 2026-08-03
  Suggested replacement (if found): dated press releases fetch clean, e.g. .../press-releases/paylocity-launches-ignite-ai-redefining-industry-ai-leadership/
- Cornerstone OnDemand | (no curated source in file) | status: replaced | observed: 2026-08-03
  Suggested replacement (if found): https://www.cornerstoneondemand.com/resources/topics/cornerstone-news/ (dated release articles)
```

### 2026-05 re-run (observed 2026-06-04, full run, WebFetch restored)
> Clean re-run of the May 2026 window now that `WebFetch` works again (every fetch had 403'd in the original 2026-05 run). Direct fetch succeeded for Lattice, Predictive Index, Culture Amp, 15Five; `WebSearch` filled the rest. Remaining failures are vendor-side bot-walls / JS-only changelogs, not an environment block — apply the route-around playbook (CI-Prompt §Runtime discovery) before promoting any replacement.

```text
VERIFIED-GOOD primaries this run (promote/keep):
- Lattice | https://lattice.com/blog/<month>-<year>-product-updates | dated monthly roundup, fetched clean (e.g. .../may-2026-product-updates)
- Predictive Index | https://docs.predictiveindex.com/en/collections/12282995-release-notes | dated entries, fetched clean
- 15Five | https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases | fetched clean, dated
- Culture Amp | https://updates.cultureamp.com | fetched clean, dated (no public RSS — see feed-verification note)

Blocked / stale this run (try Wayback + section Atom feed before declaring Unknown):
- Betterworks | https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): individual dated KB "Release: <date>" articles; section Atom feed .../sections/360012378232/articles.atom
- BambooHR | https://www.bamboohr.com/product-updates/ | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): per-feature child pages, e.g. https://www.bamboohr.com/product-updates/embedded-eor-offboarding (find the On-Demand Pay child, shipped 2026-05-11)
- Leapsome | https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://site.leapsome.com/blog/product-updates-<mon>-<year> (verified live: .../product-updates-mar-2026; may-2026 slug 404'd)
- Officevibe (Workleap) | https://help.workleap.com/en/ | status: replaced | observed: 2026-06-04
  Suggested replacement (if found): (changelog.workleap.com does NOT resolve — locate Workleap's real what's-new surface)
- Engagedly | https://changelog.engagedly.com | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): JS-only hosted changelog — find its JSON/RSS backend (AnnounceKit/Beamer/Headway)
- Microsoft Viva / Glint | https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%e2%80%93-volume-3-edition-5-may-2026/4519204 | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): (title renders, body does not via WebFetch; content recovered via WebSearch — fetch partial)
- Qualtrics | https://community.qualtrics.com/product-release-notes-96 | status: login | observed: 2026-06-04
  Suggested replacement (if found): weekly note pages indexed but login-walled, e.g. .../weekly-product-release-notes-may-6-2026-33255
- SurveyMonkey | https://www.surveymonkey.com/curiosity/category/product-news/ | status: stale | observed: 2026-06-04
  Suggested replacement (if found): page lists posts but no per-post dates in HTML-to-text — needs a dated surface
```

### 2026-06 feed verification (observed 2026-06-04)
> **`WebFetch` now works in this environment** — `example.com` and both vendor pages fetched clean (200), reversing the environment-wide 403 the 2026-05 run hit. Re-verified the May 2026 items and hunted for RSS/changelog feeds for both promoted primaries. **Result: neither vendor exposes a public feed — there is no `feed`-kind URL to promote for either.**
>
> - **15Five** (`success.15five.com`, Zendesk Help Center): the "What's new" running list is a *single Zendesk article* (`50989471559067`), not a section/blog, so it has no syndication feed. Probes 404'd / served HTML: `…/50989471559067.atom`, `/hc/en-us/sections.atom`. Page "last updated 2026-05-29 03:56." May 2026 items verified on-page: Custom Automated Review Schedules (05-20), Manager Display Name Customization (05-19), HRIS Sync 2.0 (05-14), Download All Survey Results as Zip (05-05). ⚠️ Date discrepancy: search still indexes the *stale* article dating HRIS Sync 2.0 to "April 29" — the live running list (authoritative) says "Released May 14th." Trust the live page.
> - **Culture Amp** (`updates.cultureamp.com`, Intercom News): no public RSS/Atom/JSON feed exists (Intercom News uses RSS only as an API input, not output). Probes 404'd: `/rss`, `/feed`, `/feed.rss`; no `<link rel="alternate">` in the page head. The newsfeed page is itself the machine-readable surface. May 2026 items verified on-page: Self-Service SAML/SSO (05-14), Scoped Surveys (Limited) Role (05-06), Cascading Goals (05-05). (June 01 SAML "all accounts" item is out of the May window.)

### 2026-06 curation (observed 2026-06-04)
> Triggered by two live, in-window pages found manually that the 2026-05 run missed. Root cause was the environment-wide `WebFetch` 403 (search-only mode), compounded by two source-curation gaps now corrected below. See `CI-Data-Quality-Proposal.md` for the full diagnosis.

```text
- 15Five | https://success.15five.com/hc/en-us/articles/36062624232219-What-s-New-in-15Five-Product-Releases | status: stale | observed: 2026-06-04
  Suggested replacement (if found): https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases  (live running list, last updated 2026-05-28; PROMOTED to primary in sources)
- Culture Amp | (public newsfeed was absent from sources) | status: replaced | observed: 2026-06-04
  Suggested replacement (if found): https://updates.cultureamp.com  (public, no-login, dated newsfeed; PROMOTED to primary in sources)
```

### 2026-05 run (observed 2026-06-04)
> Environment note: this run executed where **`WebFetch` was blocked environment-wide (every fetch 403'd across unrelated domains)** — an outbound network-policy limit, not vendor bot-walls. All collection was via `WebSearch`. The URLs below could not be directly fetched; the suggested replacements are **dated, more-fetchable surfaces** discovered via search. Promote the good ones into each vendor's `sources` list. See `CI-Run-Notes-2026-05.md` for full context.

```text
- 15Five | https://success.15five.com/hc/en-us/articles/36062624232219-What-s-New-in-15Five-Product-Releases | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): (none stable — running list not machine-readable this run; help-doc edits clustered around Engagement/High Fives on 2026-05-28/29, unconfirmed)
- Culture Amp | https://support.cultureamp.com/en/collections/17746165-2026-product-updates | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://www.cultureamp.com/company/newsroom
- Lattice | https://lattice.com/product-updates | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://lattice.com/blog/<month>-<year>-product-updates  (dated monthly blog — stable primary; e.g. https://lattice.com/blog/may-2026-product-updates)
- Microsoft Viva / Glint | https://techcommunity.microsoft.com/category/viva-glint/blog/viva_glint_blog | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): individual dated "News to Know" posts, e.g. https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%e2%80%93-volume-3-edition-5-may-2026/4519204
- SurveyMonkey | https://help.surveymonkey.com/en/surveymonkey/new/ | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://www.surveymonkey.com/curiosity/category/product-news/  (+ https://www.surveymonkey.com/newsroom/)
- Betterworks | https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): (none — individual dated KB articles "Release: <date>", e.g. https://support.betterworks.com/hc/en-us/articles/44556397118477-Release-March-24th-2026)
- Qualtrics | https://community.qualtrics.com/product-release-notes-96 | status: login | observed: 2026-06-04
  Suggested replacement (if found): weekly note pages are indexed but content login-walled, e.g. https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-may-6-2026-33255
- Perceptyx | https://perceptyxhelp.freshdesk.com/support/solutions/folders/63000237891 | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://blog.perceptyx.com  (dated product/launch posts)
- Leapsome | https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://site.leapsome.com/blog/product-updates-<month>-<year>  (dated monthly posts; e.g. .../product-updates-april-2026)
- Paylocity | https://www.paylocity.com/company/about-us/newsroom/in-the-news/ | status: bot_blocked | observed: 2026-06-04
  Suggested replacement (if found): https://www.paylocity.com/company/about-us/newsroom/in-the-news/whats-new-<month>-<year>/  (dated monthly blog)
- Cornerstone OnDemand | (no curated source in file) | status: replaced | observed: 2026-06-04
  Suggested replacement (if found): https://www.cornerstoneondemand.com/company/news-room/press-releases/
- Workday Peakon | (no curated source in file) | status: replaced | observed: 2026-06-04
  Suggested replacement (if found): https://doc.workday.com/en-us/peakon.html  (release dates also well-surfaced by third-party 2026R1/R2 guides)
```
