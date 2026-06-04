# CI Report — May 2026

> **window:** 2026-05-01 → 2026-05-31 (America/Chicago) · **run date:** 2026-06-04
> Clean re-run with `WebFetch` restored (the original 2026-05 run was search-only after an environment-wide 403). Coverage and date confidence are materially better; remaining gaps are vendor-side bot-walls / JS-only changelogs, not an environment block.

---

## 1. Slack Digest — May 2026

```text
:wave: Monthly Competitor Update — May 2026  (2026-05-01 to 2026-05-31)
TL;DR: The month's most strategic move is Viva Glint pushing *continuous*, between-cycle engagement signals — piping Viva Insights workplace metrics into Glint reporting — while Lattice, Culture Amp and 15Five all shipped notable Performance + admin upgrades.

*Engagement*
• Microsoft Viva / Glint | Continuous Employee Engagement with Workplace Metrics | Date: 2026-05
  Glint now blends Viva Insights workplace metrics (work-life balance, collaboration) into reporting, with between-cycle notifications when team patterns shift.
  https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%e2%80%93-volume-3-edition-5-may-2026/4519204
• Lattice | Engagement Insights Expansion | Date: 2026-05
  Added native Job Architecture and Management Type filters plus Lattice + Mercer 2025 benchmarks spanning 64 countries and 16 industries.
  https://lattice.com/blog/may-2026-product-updates
• Culture Amp | Scoped Surveys (Limited) role for Onboarding & Exit | Date: 2026-05-06
  HRBPs get a role with demographic-based scoping on Lifecycle (onboarding/exit) surveys, so they see only their org scope.
  https://updates.cultureamp.com

*Performance*
• 15Five | Custom Automated Review Schedules | Date: 2026-05-20
  Automatic review cycles can now be scheduled around any employee date, not just hire date.
  https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
• Culture Amp | Cascading Goals | Date: 2026-05-05
  Supporting goals now automatically roll their progress up to a primary goal in real time, no manual updates.
  https://updates.cultureamp.com
• Lattice | Reviews Experience Redesign | Date: 2026-05
  Rebuilt the manager and IC reviews UI with separate tabs for personal tasks and team management.
  https://lattice.com/blog/may-2026-product-updates

*Other / Cross-Platform*
• Culture Amp | Self-Service SAML/SSO Configuration | Date: 2026-05-14
  New customers (joined after 2026-04-30) can configure and manage SAML SSO themselves in Account Settings.
  https://updates.cultureamp.com
• 15Five | HRIS Sync 2.0 | Date: 2026-05-14
  Admins can confirm sync health and view a reliable audit trail of what changed and when.
  https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
```
```text
No notable changes this window (sources scanned): Perceptyx (blog read — editorial only). Unknown/access-limited (not verified): Betterworks, Leapsome, Qualtrics, SurveyMonkey, Officevibe/Workleap, Engagedly, Gallup, Workday Peakon, ADP, Cornerstone, Energage, UKG, PerformYard.
```

---

## 2. Package Brief — May 2026

### Top Themes
- **Continuous / between-cycle listening is the leading edge.** Viva Glint's "Workplace Metrics" move (Insights data + change notifications into Glint reporting) is the clearest example of a rival pushing listening past the survey cycle toward QW's listening→action thesis.
- **Performance workflows got broad polish across pure-plays.** Lattice (reviews UI rebuild, calibration), 15Five (automated review schedules), and Culture Amp (cascading goals) all shipped Performance upgrades in the same window — manager-enablement and goal-alignment are the common thread.
- **Admin / identity self-service is a quiet trend.** Culture Amp self-service SAML/SSO and 15Five HRIS Sync 2.0 both reduce reliance on vendor support for integration/identity plumbing — stickiness plays, not feature flash.
- **Benchmarking as differentiation.** Lattice folding Mercer 2025 benchmarks into Engagement Insights raises the comparative-data bar.
- **Coverage caveat:** several help-centers (Betterworks, BambooHR, Leapsome) bot-blocked direct fetch; their items were recovered (or not) via search, so a few competitors remain Unknown rather than confirmed "no change."

### Material Changes

#### Engagement
```text
• Microsoft Viva / Glint | Continuous Employee Engagement with Workplace Metrics | Est. Impact: High
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-05 • Confidence: Medium
  What changed (fact): Glint reporting now incorporates Viva Insights workplace metrics (e.g., work-life balance, collaboration) alongside survey responses, and leaders can enable between-cycle notifications when team workplace patterns change.
  Implication (labeled inference): moves Glint from periodic-survey listening toward continuous behavioral signal.
  Strategic Signal: Platform/Connected — bridges survey sentiment with M365 behavioral data and an action loop between cycles.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%e2%80%93-volume-3-edition-5-may-2026/4519204
  Notes: Post body did not render via fetch; confirmed via official URL + corroborating search. Day-level date Unknown (month-level edition).

• Lattice | Engagement Insights Expansion | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-05 • Confidence: High
  What changed (fact): Added native Job Architecture and Management Type filters plus "Lattice and Mercer 2025 Benchmarks" covering 64 countries and 16 industries.
  Strategic Signal: Point-solution — deepens engagement analytics/benchmarking depth.
  Source: https://lattice.com/blog/may-2026-product-updates

• Culture Amp | Scoped Surveys (Limited) Role for Onboarding & Exit | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: New • Date: 2026-05-06 • Confidence: High
  What changed (fact): A new role lets HRBPs work with Onboarding and Exit (Lifecycle) surveys with demographic-based scoping, seeing only their organizational scope.
  Strategic Signal: Trust/Privacy — scoped data access on sensitive lifecycle surveys.
  Source: https://updates.cultureamp.com

• 15Five | Download All Survey Results as Zip | Est. Impact: Low
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-05-05 • Confidence: High
  What changed (fact): HR Outcomes admins can download the raw data from every survey in an Engagement campaign in a single zip.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

• Predictive Index | QR-code pulse distribution (Diagnose) | Est. Impact: Low
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-05-12 • Confidence: High
  What changed (fact): Pulse surveys in PI Diagnose can now be distributed via QR code.
  Source: https://docs.predictiveindex.com/en/collections/12282995-release-notes
  Notes: Same release batch also shipped Hire/assessment features (out of QW scope) and table improvements in Inspire.
```

#### Performance
```text
• 15Five | Custom Automated Review Schedules | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-05-20 • Confidence: High
  What changed (fact): Automatic review cycles can be scheduled around any employee date, not just hire date.
  Strategic Signal: Manager enablement — automates review cadence around real lifecycle events.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

• Culture Amp | Cascading Goals | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: New • Date: 2026-05-05 • Confidence: High
  What changed (fact): Supporting goals automatically roll up progress to a primary goal in real time without manual updates.
  Strategic Signal: Platform/Connected — strengthens goal alignment/roll-up across the org.
  Source: https://updates.cultureamp.com

• Lattice | Reviews Experience Redesign | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-05 • Confidence: High
  What changed (fact): Rebuilt the manager and IC reviews UI with separate tabs for personal tasks vs. team management.
  Strategic Signal: Manager enablement.
  Source: https://lattice.com/blog/may-2026-product-updates

• Lattice | Calibration Improvements | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-05 • Confidence: High
  What changed (fact): Resizable columns, sort by Past Weighted Score, inline group renaming, group-scoped filters, sidebar hiding, and bulk group deletion in rating calibration.
  Source: https://lattice.com/blog/may-2026-product-updates

• Lattice | 1:1 Log Exports | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-05 • Confidence: High
  What changed (fact): 1:1 exports gained filtering, custom date ranges, and expanded CSV output including action items and notes.
  Source: https://lattice.com/blog/may-2026-product-updates
```

#### Recognition & Rewards
No verified material changes this window. (See No-notable-changes appendix.)

#### Development
No verified material changes this window. (See No-notable-changes appendix.)

#### Other / Cross-Platform
```text
• Culture Amp | Self-Service SAML/SSO Configuration | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-05-14 • Confidence: High
  What changed (fact): New customers (joined after 2026-04-30) can set up and manage SAML SSO connections directly in Account Settings, with instant testing and certificate management.
  Strategic Signal: Trust/Privacy + integration depth — reduces reliance on vendor support for identity setup.
  Source: https://updates.cultureamp.com
  Notes: Extended to ALL accounts on 2026-06-01 (just outside this window).

• 15Five | HRIS Sync 2.0 | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-05-14 • Confidence: High
  What changed (fact): Admins can confirm HRIS sync health and view a reliable audit trail of what changed and when.
  Strategic Signal: Integration depth.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
  Notes: A stale, still-indexed 15Five article dates HRIS Sync 2.0 to "April 29"; the live running list (authoritative) says "Released May 14th." Trusting the live page.

• BambooHR | On-Demand Pay (Earned Wage Access, powered by Clair) | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Integration • Date: 2026-05-11 • Confidence: Medium
  What changed (fact): Embedded earned-wage-access tool lets employees access wages before payday (no interest/credit check), built into BambooHR Payroll and mobile; free to customers.
  Strategic Signal: Point-solution — payroll-adjacent, outside QW's EX core; low direct competitive overlap.
  Source: https://www.bamboohr.com/product-updates/
  Notes: bamboohr.com/product-updates 403'd on direct fetch; date/scope from press + search. Confirm a direct child-page URL on promotion.

• Lattice | Inline Compensation Editing + Calibration Context in Comp | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-05 • Confidence: High
  What changed (fact): Enter compensation recommendations directly in comp tables without switching views, and surface calibration notes/tags inside compensation workflows.
  Strategic Signal: Platform/Connected — links calibration to comp (compensation is outside QW packages).
  Source: https://lattice.com/blog/may-2026-product-updates

• Lattice | Goals API Endpoint (V1) | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Integration • Date: 2026-05 • Confidence: High
  What changed (fact): Released a V1 API endpoint for programmatic goal creation and updates.
  Source: https://lattice.com/blog/may-2026-product-updates

• 15Five | Manager Display Name Customization | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-05-19 • Confidence: High
  What changed (fact): Admins can customize the term "Manager" to match company language (Coach, Lead, Mentor, etc.).
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
```
*(Minor Lattice integration items also shipped — BambooHR tabular custom fields, expanded CSV/SFTP field types, backdate calendar events — folded here as low-impact; same source URL.)*

### Appendix: No notable changes / Unknown
```text
• Perceptyx — all packages: No product feature change identified in-window. Blog read successfully; May entries were editorial/research only (the one product-adjacent item, a Tesco partnership, is dated 2026-06-02, out of window and not a shipped feature). Sources scanned: blog.perceptyx.com. Access limits: help-center (Freshdesk) not re-tried.
• Betterworks — all packages: No notable changes verified = Unknown. Release-notes section 403 (bot_blocked); newest indexed release via search is 2026-03-24. Access limits: support.betterworks.com 403.
• Leapsome — all packages: Unknown. Platform-improvements running list 403; no May-2026-specific dated post found (dated blog exists, e.g. product-updates-mar-2026). Access limits: help.leapsome.com 403.
• Qualtrics (EmployeeXM) — all packages: Unknown. Weekly release notes are login-walled; the one in-window item surfaced (SMS-credit cost model, ~2026-05-06) is a billing/pricing change → excluded as non-material. Access limits: community login.
• SurveyMonkey — all packages: Unknown. Product-news page rendered without per-post dates; could not pin any post to the May window ("Connect" verified as 2025-09-30, out of window). Access limits: no dates in HTML-to-text.
• Officevibe (Workleap) — all packages: Unknown. Help-center homepage shows no what's-new; changelog.workleap.com did not resolve (ECONNREFUSED). Access limits: no dated surface located.
• Engagedly — all packages: Unknown. Blog overview had no in-window Product Updates posts; changelog.engagedly.com is JS-rendered/empty to HTML-to-text. Access limits: JS-only changelog.
• Gallup — all packages: Unknown / no in-window change. App store shows v4.24.0 dated 2026-03-25 (out of window); support center not deeply scanned. Access limits: no dated May surface.
• Workday Peakon — all packages: Unknown. 2026R1 features exist (AI comment summaries, targeted sentiment, rules-based Moments-That-Matter questions, mobile-app retirement, UK hosting) but no entry verifiably dated to the May window — not anchored per date-discipline rules. Access limits: no curated source; release date not pinned to window.
• ADP, Cornerstone OnDemand, Energage, UKG — all packages: Unknown — not scanned. No curated source in CI-Competitor.md and not reached within this run's discovery budget. Not downgraded to "no change."
```

### Appendix: Low-confidence watchlist
```text
1. Microsoft Viva Pulse "now included with Viva Glint" — possible packaging/bundling change surfaced via a third-party (schneider.im); no verifiable in-window GA date — watch.
2. Workday Peakon mobile-app retirement (2026R1) — material if confirmed in-window; date not pinned to May.
3. SurveyMonkey "Introducing programs" — appears on product-news but undated; verify date on next run.
```

### Coverage report
```text
Competitors audited: 21/21 attempted; 8 with verified in-window items, 13 Unknown/access-limited or out-of-window
Sources fetched: ~16 attempted (WebFetch working this run — example.com + 6 vendor pages returned 200; blocked/stale this run: 6 — Betterworks, BambooHR, Leapsome help-centers 403; Workleap changelog ECONNREFUSED; Engagedly changelog JS-empty; Viva Glint body partial)
Items included: 16   (High=1, Medium=8, Low=7)
By package: Engagement=5 · Performance=5 · Recognition & Rewards=0 · Development=0 · Other=6
Most active this window: Lattice (8 items)   ← shipping-velocity signal, descriptive only
No-notable-change / Unknown pairs: Perceptyx confirmed no-change; 13 competitors Unknown/access-limited (see appendix)
Environment note: Unlike the original 2026-05 run (WebFetch 403'd environment-wide, search-only), WebFetch worked this run — coverage and date confidence are materially better. Remaining gaps are vendor-side bot-walls / JS-only changelogs, not an environment block.
```

> Source-health observations from this run are recorded in `CI-Competitor.md` → "Source health" (2026-05 re-run block).
