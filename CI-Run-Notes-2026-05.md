# CI Run Notes — May 2026 (handoff for a fresh session)

> **Purpose:** Capture everything learned during the 2026-05 `/ci-report` attempt so a new session can pick up with full context and produce a clean, well-sourced report. Read this *after* `CLAUDE.md`, `CI-Context.md`, `CI-Competitor.md`, and `CI-Prompt.md`.
> **Window in question:** 2026-05-01 → 2026-05-31 (May 2026).
> **Status:** Partial. Five competitors have *confirmed, dated, in-window* changes. The rest are **Unknown (access-limited)** — NOT "no notable changes" — because of an environment limitation described below.

---

## 1. Critical environment finding — WebFetch was fully blocked

During the 2026-05 run, **every single `WebFetch` call returned HTTP 403**, across ~12 unrelated domains (Zendesk help centers, Intercom, Microsoft Tech Community, lattice.com, releasebot.io, leapsome.com, surveymonkey.com help). The uniformity across unrelated hosts means this is **the remote execution environment's outbound network policy blocking `WebFetch`**, not vendor bot-walls.

**Consequences / rules for the next run:**
- If `WebFetch` 403s on the first 2–3 unrelated domains, assume it is blocked environment-wide. Do **not** keep retrying every source — it wastes the discovery budget.
- With `WebFetch` down, **`WebSearch` is the only collection channel.** Its result *summary* is conservative and unreliable on dates; trust the **Links list** (real indexed URLs) and craft **feature- and date-specific queries** to force the actual release text into the snippet.
- A source you cannot read is **Unknown**, never "No notable changes." (This is already in `CI-Prompt.md` → "No notable changes" gate and Access-limits rule F; the 2026-05 first pass violated it and must not be repeated.)

**To actually fix this:** re-run in an environment whose network policy permits outbound fetch (or run local Claude Code). That alone unlocks the blocked pages below. See https://code.claude.com/docs/en/claude-code-on-the-web for how environment network policies are configured.

---

## 2. Confirmed IN-WINDOW changes (May 2026) — verified by dated search evidence

These five are solid and ready to drop straight into the report. All dates are America/Chicago, ISO-8601.

### Engagement
- **Lattice — Engagement survey filters + Mercer 2025 benchmarks** | Date: 2026-05 | GA | Confidence: High
  Native Job Architecture and Management Type filters in the Engagement filter bar (filter/group by Job Level, Function, Type, Title, Management Type without custom fields); Lattice–Mercer 2025 benchmarks live across 8 regions / 64 countries / 16 industries.
  https://lattice.com/blog/may-2026-product-updates
- **Microsoft Viva / Glint — Copilot-assisted survey comments** | Date: 2026-05 | GA | Confidence: High
  Survey takers get an in-survey Microsoft Copilot to rephrase/refine written feedback. (AI inside the Engagement workflow → classify Engagement, note AI.)
  https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%e2%80%93-volume-3-edition-5-may-2026/4519204
- **Microsoft Viva / Glint — Workplace Metrics in Glint reporting** | Date: 2026-05 | Private Preview | Confidence: Medium
  Viva Insights collaboration / work-life-balance metrics shown alongside survey results; notifications on pattern changes between cycles. Strategic Signal: Platform/Connected.
  https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%e2%80%93-volume-3-edition-5-may-2026/4519204

### Performance
- **Lattice — Reviews experience redesign (+ calibration)** | Date: 2026-05 | GA | Confidence: High | Est. Impact: High
  Manager + IC review UI rebuilt; split "Me" / "My Team" tabs, bulk peer-nomination approvals, calibration improvements for large-scale sessions. Strategic Signal: Manager enablement (single-silo).
  https://lattice.com/blog/may-2026-product-updates

### Development
- **Perceptyx — Develop (multi-agent AI learning)** | Date: 2026-05-14 | GA | Confidence: High | Est. Impact: High
  System of coordinated AI agents that delivers training and validates comprehension + on-the-job application in real time; part of the new "People Activation System" connecting insight → capability → behavior. Strategic Signal: Platform/Connected + AI layer.
  https://blog.perceptyx.com/perceptyx-launches-develop

### Other / Cross-Platform
- **Cornerstone OnDemand — Cornerstone Workforce AI** | Date: 2026-05-20 | GA | Confidence: High | Est. Impact: High
  AI "workforce readiness" intelligence platform (Cornerstone People Graph + Skills Engine; 55,000+ skill taxonomy); AI agents recommend automatable tasks, adaptively coach managers through performance conversations, accelerate role readiness, surface internal mobility. QW Package: Multiple (Other primary; also Development + Performance). Strategic Signal: Platform/Connected + AI layer.
  https://www.cornerstoneondemand.com/company/news-room/press-releases/cornerstone-launches-cornerstone-workforce-ai-the-intelligence-platform-for-workforce-readiness-built-to-amplify-human-potential-exponentially-with-ai/
  Secondary (May 21, lower impact, fold into notes): AWS AI/Cloud Learning content-library additions; "Workforce Readiness for the Agentic Enterprise" Salesforce integration.
- **SurveyMonkey — Claude (Anthropic) MCP connector** | Date: 2026-05-05 | GA | Confidence: High | Est. Impact: Medium
  MCP connector (Claude connector directory) to create, edit, send, analyze SurveyMonkey surveys inside Claude via natural language. Change Type: Integration. Strategic Signal: AI layer.
  https://www.surveymonkey.com/newsroom/surveymonkey-claude-ai-integration/

**Excluded (non-material) in-window:** Qualtrics SMS-credit billing-model change (2026-05-06, billing, not a feature); Viva Glint planned maintenance 2026-05-31 (reliability).

---

## 3. Active competitors whose notable items fall JUST OUTSIDE the window (Mar–Apr 2026)

This is *why May looks thin* — the big releases front-loaded into March/April. Useful context; do **not** put these in the May report (out of window), but they prove these vendors are shipping and tell you where to look for the next cycle.

- **Workday Peakon** — 2026R1 GA **2026-03-14**: AI comment summaries, targeted sentiment analysis, rules-based survey triggers, **Peakon iOS/Android mobile app retirement**, UK AWS hosting. (Source: Workday 2026R1 release guides.)
- **Qualtrics** — **X4, 2026-03-17 to 03-19**: conversational feedback (AI follow-up probing) + predictive attrition analytics ("listening → manager action"). Reworked.co coverage.
- **Culture Amp** — **2026-03-24**: Performance Culture Quadrant (PCQ) + AI Coach diagnostic, now available to Engage customers.
- **Engagedly** — **2026-04-15**: AI Talent Mobility, powered by Marissa AI agents (skills-based readiness/mobility).
- **Leapsome** — **April 2026** monthly drop: cross-module AI Copilot (spans absences/payroll/meetings/goals/reviews/surveys/learning), Timeline Canvas workflow builder, inline AI assist in review editor, Slack survey modal. (https://site.leapsome.com/blog/product-updates-april-2026)
- **15Five** — Growth Studio **2026-04-22**, succession critical-role ID **2026-04-25**, AMAYA AI agent + Insights Dashboard **Feb 2026**, revamped nav/Scoped IT Admin role **April 2026**.
- **Paylocity** — April 2026 "What's New" (AI-powered search, Market Pay via Salary.com, etc.); Elevate Solutions **2026-04-21**.
- **BambooHR** — Shift Scheduling **2026-04-27**; Performance Management settings/scheduling + custom-report performance data (dates unconfirmed, likely Q1–Q2).
- **UKG** — UKG Ready Release 104 (spring 2026).
- **Workleap / Officevibe** — Barley compensation acquisition **2025-07-07**.
- **PerformYard** — Meetings (2025-05-12) + Surveys (2025-07-09).
- **Predictive Index** — PI Meeting Notetaker beta (doc updated 2026-02-12).

---

## 4. Genuine MAY leads to chase FIRST in the next session (unconfirmable here)

These are the highest-probability in-window items that I could not confirm because the primary pages are `WebFetch`-blocked. Start here:

1. **Leapsome — May 2026 monthly update.** Leapsome posts a monthly blog; April is confirmed live, so try `https://site.leapsome.com/blog/product-updates-may-2026` (and `www.leapsome.com/blog/product-updates-may-2026`). Very likely a real, material May drop.
2. **15Five — late-May Engagement / High Fives activity.** Help-center articles for **Engagement Score, Engagement Report, High Fives Feature Overview, and Engagement survey settings were all re-edited May 28–29, 2026.** Those are doc-edit timestamps (not proof of a feature change per date-rule G4), but the clustering around recognition + engagement is a strong tell. Open the running list `https://success.15five.com/hc/en-us/articles/36062624232219-What-s-New-in-15Five-Product-Releases` and confirm.
3. **Betterworks — April/May releases.** Releases are titled "Release: <date>" (March 24 confirmed). Find the post-March-24 entries under `https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes`.
4. **Qualtrics — weekly notes May 13 / 20 / 27, 2026.** Indexed but community-login-walled (e.g., `.../weekly-product-release-notes-may-6-2026-33255`). May 6 was only SMS billing; the later May weeks were unread.
5. **Culture Amp — May newsfeed.** PCQ was March; confirm whether anything shipped to the public newsfeed in May (AI Comment Comparisons doc carried a May-1 *edit* stamp — verify it's a release, not a doc refresh).

---

## 5. Source-URL improvements (promote into `CI-Competitor.md` → `sources`)

The Zendesk/Intercom/Freshdesk help centers are the worst offenders for bot-blocking. Prefer these **dated, more-fetchable surfaces**. These are recorded in `CI-Competitor.md` → "Source health" as suggested replacements this run; a human should promote the good ones into each vendor's `sources` list.

- **Lattice** → dated monthly blog posts `https://lattice.com/blog/<month>-<year>-product-updates` (stable, dated) instead of the JS-rendered `/product-updates` hub.
- **Microsoft Viva / Glint** → individual "News to Know" posts (monthly, dated) rather than the category hub.
- **Perceptyx** → `https://blog.perceptyx.com` (dated launch posts) over the Freshdesk solutions folder.
- **Leapsome** → `https://site.leapsome.com/blog/product-updates-<month>-<year>` monthly posts over the `help.leapsome.com` "Platform improvements" running list.
- **Paylocity** → `https://www.paylocity.com/company/about-us/newsroom/in-the-news/whats-new-<month>-<year>/` monthly blog.
- **SurveyMonkey** → `https://www.surveymonkey.com/curiosity/category/product-news/` + newsroom, over the `help.surveymonkey.com` release-notes hub.
- **Cornerstone** → newsroom press releases `https://www.cornerstoneondemand.com/company/news-room/press-releases/` (no curated source today; add one).
- **Workday Peakon** → third-party release guides surface 2026R1/2026R2 dates well; official `https://doc.workday.com/en-us/peakon.html`. (No curated source today.)

---

## 6. Recommended way to run the next session

1. Read `CLAUDE.md` + the three authoritative files, then **this file**.
2. Confirm whether `WebFetch` works (one test fetch). If it 403s on 2–3 unrelated domains, switch to `WebSearch`-only mode and label all unread sources **Unknown**.
3. Reuse the five confirmed items in §2 verbatim.
4. Spend the discovery budget on the §4 leads (Leapsome May, 15Five late-May, Betterworks, Qualtrics weekly, Culture Amp newsfeed) — in that order.
5. Keep the §3 items OUT of the May report (out of window) but note the cadence in Top Themes ("enterprise suites front-loaded spring releases into March").
6. In the Slack digest footer and the Brief's appendix, use **"Unknown — access-limited (sources unreachable)"** for any vendor whose primary page you could not read — never "No notable changes."
7. Refresh `CI-Competitor.md` → "Source health" with whatever blocked/replaced this run.
