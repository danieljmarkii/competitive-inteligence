# CI Report — July 2026

> **window:** 2026-07-01 → 2026-07-31 (America/Chicago) · **run date:** 2026-07-31
> **Environment note:** `WebFetch` was blocked environment-wide this run (control fetch of example.com also 403'd — network-policy block, not vendor bot-walls). Per CI-Prompt §Runtime discovery, the entire run executed in **WebSearch-only mode** (two-pass discovery; dates taken only from indexed titles/snippets/URLs, never from AI search summaries). Coverage is therefore constrained: no primary page was read end-to-end, and quiet competitors are recorded as **Unknown/access-limited**, not "no changes." Recommend a clean re-run from an environment with outbound fetch (as was done for 2026-05) to firm up dates and catch items that never got indexed.

---

## 1. Slack Digest — July 2026

```text
:wave: Monthly Competitor Update — July 2026  (2026-07-01 to 2026-07-31)
TL;DR: Consolidation and the AI-agent land-grab defined July — Energage acquired Engagedly to build a connected engagement + talent platform, while Betterworks and Leapsome shipped MCP connectivity and BambooHR and Paylocity launched platform-wide AI agent suites.

*Engagement*
• Qualtrics | EX25 Certified Questions — translations in 35 languages | Date: 2026-07-22
  Qualtrics' updated EX25 certified engagement question set is now available in 35 languages, aimed at short, targeted listening for global engagement programs.
  https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-july-22-2026-33475
• Microsoft Viva / Glint | Refreshed global benchmarks | Date: 2026-07
  Glint's global benchmarks are being refreshed (GA July–August) using survey data from 2025-07 through 2026-06, with no setup required — following the earlier industry/region/country benchmark refresh.
  https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463

*Development*
• Cornerstone OnDemand | July release — Performance Assistant + AI Development Plans | Date: 2026-07
  Cornerstone's July release adds a Performance Assistant that synthesizes review data into coaching prompts and AI-generated Development Plans with suggested objectives, skills, learning, and tasks.
  https://www.cornerstoneondemand.com/resources/article/turning-talent-development-into-workforce-readiness-you-can-measure/

*Other / Cross-Platform*
• Leapsome | Unified AI platform: AI agents, AI-generated workflows, MCP, new ATS | Date: 2026-07-15
  Leapsome launched five EU-hosted AI agents, prompt-built talent workflows, MCP connectivity for data in/out, an ATS in early access, and an ADP Workforce Now payroll export integration.
  https://site.leapsome.com/blog/leapsome-ai-people-data-foundation
• Energage | Acquisition of Engagedly | Date: 2026-07-14
  Energage (Top Workplaces) merged with talent-management platform Engagedly to build a single platform connecting engagement, talent management, and employer brand (deal completed 2026-07-20).
  https://engagedly.com/blog/energage-and-engagedly-merge/
• Betterworks | MCP Server (Beta) | Date: 2026-07-14
  Betterworks launched a beta MCP server that exposes goals, teams, users, recognition, and hashtags to ChatGPT, Claude, Microsoft Copilot, Gemini, and other MCP-compatible assistants.
  https://www.betterworks.com/betterworks-launches-new-ai-capabilities-that-connect-performance-data-to-ai-assistants
• BambooHR | Bamboo AI | Date: 2026-07-21
  BambooHR introduced Bamboo AI, a system of AI agents embedded in the platform that inherits existing roles, permissions, and compliance rules.
  https://www.bamboohr.com/about-bamboohr/press-release/bamboohr-launches-bamboo-ai
• Paylocity | Ignite AI + Ignite AI Hub | Date: 2026-07-21
  Paylocity launched platform-wide AI agents (resume summary, data inspection, time correction) plus an Ignite AI Hub dashboard for managing and measuring AI use across the org.
  https://investors.paylocity.com/news-releases/news-release-details/paylocity-launches-ignite-ai-redefining-industry-ai-leadership
```
```text
Unknown/access-limited this window (search-only run; primaries unread): 15Five, Culture Amp, Lattice, Gallup, Peakon/Workday, Qualtrics (weekly notes login-walled), SurveyMonkey (help center), ADP, Predictive Index, Perceptyx, Officevibe/Workleap, PerformYard, UKG.
```

---

## 2. Package Brief — July 2026

### Top Themes
- **MCP / AI-assistant interoperability arrived in HR tech.** Betterworks (MCP Server beta, 2026-07-14) and Leapsome (MCP connectivity, 2026-07-15) both shipped Model Context Protocol surfaces in the same week — performance and people data is being opened up to ChatGPT/Claude/Copilot-class assistants rather than kept inside vendor dashboards. This bypasses the vendor UI as the point of insight consumption.
- **Platform-wide AI agent suites from the HRIS/HCM tier.** BambooHR (Bamboo AI, 2026-07-21), Paylocity (Ignite AI + governance Hub, 2026-07-21), and Cornerstone (Workforce AI July release) all launched embedded agent layers with permission-inheritance and admin governance messaging — the AI layer is becoming a platform feature, not a module.
- **Consolidation aimed directly at the connected-platform thesis.** Energage's acquisition of Engagedly (announced 2026-07-14, completed 2026-07-20) explicitly targets "a single platform that connects employee engagement, talent management, and employer brand" — two roster competitors becoming one platform play.
- **AI moving from insight to manager action in Development.** Cornerstone's Performance Assistant + AI-generated Development Plans turn review conversations into coaching prompts and growth paths — squarely in QW's manager-enablement lane.
- **Coverage caveat.** Search-only run (environment fetch block): every primary source was read via indexed titles/snippets, several dates are month-precision, and quiet vendors are Unknown rather than verified-quiet.

### Material Changes

#### Engagement
• Qualtrics | EX25 Certified Questions translations (35 languages) | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-07-22 • Confidence: Medium
  What changed (fact): Updated EX25 certified engagement questions are available in 35 languages, positioned for short, targeted listening in global engagement programs.
  Implication (labeled inference): Lowers Qualtrics' localization barrier in global engagement deals.
  Strategic Signal: Point-solution — deepens the survey silo.
  Source: https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-july-22-2026-33475
  Notes: Community release notes are login-walled; content recovered from indexed snippets — spot-check before external use.

• Microsoft Viva / Glint | Refreshed global benchmarks | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-07 (staged July–August) • Confidence: Medium
  What changed (fact): Global benchmarks refreshed using survey data collected 2025-07 through 2026-06, generally available July/August with no setup; follows the industry/region/country benchmark refresh.
  Implication (labeled inference): Keeps Glint's external-comparison story current in enterprise engagement reporting.
  Strategic Signal: Point-solution — benchmarking depth within the listening silo.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463

• Qualtrics | Response Rate Line Chart Widget for Lifecycle projects | Est. Impact: Low
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-07-29 • Confidence: Medium
  What changed (fact): The response-rate line chart widget can now be used in Lifecycle projects to track project response rate over time.
  Source: https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-july-29-2026-33476

#### Performance
• Betterworks | Calibration identity search + saved views | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-07-14 • Confidence: Medium
  What changed (fact): Calibration cycle pages now support combined search/filter by Employee, Group, and Department, savable as views.
  Source: https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026

• Betterworks | Past Meetings in 1:1s | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: New • Date: 2026-07-14 • Confidence: Medium
  What changed (fact): Managers and employees can backdate ad-hoc 1:1s to capture notes and agenda items from meetings that happened outside Betterworks.
  Source: https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026

#### Development
• Cornerstone OnDemand | July release: Performance Assistant + AI-generated Development Plans | Est. Impact: Medium
  QW Package: Multiple (Development primary; also Performance)
  State: GA • Change Type: New • Date: 2026-07 (day Unknown) • Confidence: Likely
  What changed (fact): New Performance Assistant synthesizes review data into insights and contextual coaching prompts; AI-generated Development Plans turn feedback into growth paths with AI-suggested objectives, skills, learning, and tasks. Content Studio gains insights, benchmarking, and GenAI capabilities.
  Implication (labeled inference): Cornerstone is wiring performance signal directly into development action — a listening→action loop inside the talent suite.
  Strategic Signal: Manager enablement — coaching prompts grounded in review evidence.
  Source: https://www.cornerstoneondemand.com/resources/article/turning-talent-development-into-workforce-readiness-you-can-measure/
  Notes: Official article carries no explicit day; corroborated by Cornerstone's "The July release is here" LinkedIn post (discovery only).

#### Other / Cross-Platform
• Leapsome | Unified AI platform: agents, AI-generated workflows, MCP, new ATS | Est. Impact: High
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-15 • Confidence: Medium
  What changed (fact): Launched five EU-hosted AI agents (Development Coach, Culture Advisor, Data Analyst, PeopleOps Partner, HR Helpdesk), prompt-built workflow automation across the employee lifecycle, MCP connectivity for importing/exporting data, a new ATS in early access, and an ADP Workforce Now payroll export integration. Positioned as EU AI Act compliant and EU-hosted.
  Implication (labeled inference): Leapsome is claiming the "one connected people-data foundation" ground (HRIS + recruiting + performance + engagement + learning + comp) that QW's platform thesis occupies.
  Strategic Signal: Platform/Connected — cross-module data foundation plus an AI layer that acts.
  Source: https://site.leapsome.com/blog/leapsome-ai-people-data-foundation
  Notes: ATS is early access (Beta); launch day sourced from press coverage of the 2026-07-15 announcement.

• Energage | Acquisition of Engagedly | Est. Impact: High
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-14 • Confidence: High
  What changed (fact): Energage (Top Workplaces, 30M+ employee surveys) announced a merger with Engagedly (AI-powered talent management: performance, development, learning, rewards & recognition, frontline support) on 2026-07-14; the transaction completed 2026-07-20. Stated direction is a single platform connecting engagement, talent management, and employer brand.
  Implication (labeled inference): Two roster competitors become one multi-package platform play — a direct analogue to QW's connected engagement+performance+recognition+development positioning, with an employer-brand hook QW lacks.
  Strategic Signal: Platform/Connected — consolidation explicitly aimed at cross-package connection.
  Source: https://engagedly.com/blog/energage-and-engagedly-merge/
  Notes: Corporate action, not a shipped feature — product integration timeline Unknown; watch for combined-platform roadmap announcements.

• Betterworks | MCP Server (Beta) | Est. Impact: High
  QW Package: Other / Cross-Platform
  State: Beta • Change Type: Integration • Date: 2026-07-14 • Confidence: High
  What changed (fact): Beta MCP server lets organizations securely connect Betterworks data — goals, teams, users, recognition, hashtags — to ChatGPT, Claude, Microsoft Copilot, Gemini, and other MCP-compatible assistants, with more capabilities promised through the year.
  Implication (labeled inference): Performance and recognition data becomes consumable wherever leaders already work with AI — weakens the "log into the EX platform for insight" model.
  Strategic Signal: AI layer — performance intelligence embedded in external AI workflows.
  Source: https://www.betterworks.com/betterworks-launches-new-ai-capabilities-that-connect-performance-data-to-ai-assistants

• BambooHR | Bamboo AI | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-21 • Confidence: Medium
  What changed (fact): Introduced Bamboo AI, an embedded system of AI agents and intelligence across the BambooHR platform that follows existing rules, permissions, roles, and compliance settings.
  Implication (labeled inference): The SMB HRIS that recently added a Recognition & Rewards module now has a platform AI layer — raises the bar for connected-AI stories in QW's mid-market.
  Strategic Signal: AI layer — platform-wide agents with permission inheritance.
  Source: https://www.bamboohr.com/about-bamboohr/press-release/bamboohr-launches-bamboo-ai
  Notes: Press release only; rollout staging and per-plan availability unverified.

• Paylocity | Ignite AI + Ignite AI Hub | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-21 • Confidence: Medium
  What changed (fact): Platform-wide AI with agents (Resume Summary, Data Inspection, Time Correction, joining existing benefits/expense/AP agents) plus the Ignite AI Hub, a centralized dashboard for managing and measuring AI use across the organization.
  Implication (labeled inference): Agents are HCM-operational rather than EX-core, but the AI-governance hub is a differentiated admin story HR buyers will start expecting.
  Strategic Signal: AI layer — agent suite plus AI governance for admins.
  Source: https://investors.paylocity.com/news-releases/news-release-details/paylocity-launches-ignite-ai-redefining-industry-ai-leadership

• SurveyMonkey | GetFeedback relaunch (website feedback) | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-22 • Confidence: Medium
  What changed (fact): Relaunched GetFeedback as a self-serve website-feedback product — buttons, behavior-triggered and embedded forms via a single line of code, with a trends dashboard.
  Implication (labeled inference): CX-facing, not EX — low direct threat to QW packages.
  Strategic Signal: Point-solution — website feedback silo.
  Source: https://www.surveymonkey.com/curiosity/announcing-getfeedback/
  Notes: Day precision from press coverage (week-of-2026-07-24 roundups); official post undated in index.

• Microsoft Viva / Glint | Seamless Entra authorization for multitenant orgs | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07 • Confidence: Medium
  What changed (fact): Survey access now supports automatic tenant discovery via Microsoft Entra for multitenant organizations, simplifying sign-in for survey takers.
  Strategic Signal: Trust/Privacy — identity/access plumbing for enterprise listening.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463

### Appendix: No notable changes / Unknown
> Search-only run: no primary source was directly fetched, so most "quiet" pairs are **Unknown — access-limited**, not verified-quiet.

• 15Five — all packages: No notable changes verified = Unknown. Sources scanned: release-notes running list + press via search. Access limits: environment fetch block; no July items indexed (latest indexed release activity: 2026-06-09 AI Assisted Reviews press).
• Culture Amp — all packages: No notable changes verified = Unknown. Sources scanned: updates.cultureamp.com via search (unreadable), status page. Access limits: environment fetch block; only non-material status/maintenance items surfaced for July.
• Lattice — all packages: No notable changes verified = Unknown. Sources scanned: blog roundup pattern + product-updates hub via search. Access limits: environment fetch block; july-2026-product-updates post not yet indexed (June roundup + Lattiverse '26 items are June, out of window). Re-check in early August.
• Gallup — all packages: No notable changes verified = Unknown. Sources scanned: help center + app-store listing via search. Access limits: environment fetch block; only a mobile app store update (2026-07-10) surfaced, content unverifiable.
• Peakon / Workday — all packages: No notable changes verified = Unknown. Sources scanned: web search (no curated release-notes source in file). Access limits: no dated July product announcements indexed; Workday's 2026R2 lands ~September.
• Qualtrics — Performance/Development: No notable changes identified this window (weekly notes surfaced Engagement/platform items only). Access limits: community release notes login-walled.
• SurveyMonkey — Engagement: No notable changes verified = Unknown. Sources scanned: help-center release notes + newsroom via search. Access limits: environment fetch block; help-center release-notes page for 2026 not indexed with July entries.
• ADP — all packages: No notable changes identified this window relevant to QW packages. Sources scanned: media center via search. Access limits: environment fetch block. (A 2026-07-28 Workforce Now HR↔IT provisioning capability was announced — off-package, no direct URL verifiable.)
• BambooHR — Recognition & Rewards: No notable changes verified = Unknown (the Recognition & Rewards module itself shipped ~2026-06-20, prior window; an undated "images in recognition posts" enhancement is on the watchlist).
• Betterworks — Engagement/Recognition & Rewards/Development: No notable changes identified this window. Sources scanned: dated release-note articles via search.
• Cornerstone OnDemand — Engagement/Recognition & Rewards: No notable changes identified this window. Sources scanned: newsroom/resources articles via search.
• Energage — product (non-M&A): No notable changes verified = Unknown. Access limits: no product-update surface curated.
• Engagedly — product (non-M&A): No notable changes verified = Unknown. Sources scanned: changelog.engagedly.com (bot_blocked, JS-only) via search.
• Leapsome — Engagement/Performance/Recognition & Rewards/Development (beyond platform launch): No notable changes verified = Unknown. Access limits: help-center running list bot_blocked; product-updates-jul-2026 blog slug unverified.
• Officevibe (Workleap) — all packages: No notable changes verified = Unknown. Sources scanned: help center + press via search. Access limits: no changelog surface exists; latest indexed launch (Human Capital agent) is 2026-02, out of window.
• Paylocity — Engagement/Performance (module-level, beyond Ignite AI): No notable changes verified = Unknown. Access limits: whats-new-july-2026 page not indexed with content.
• Perceptyx — all packages: No notable changes identified this window. Sources scanned: blog.perceptyx.com via search (2026-07-15 AI benchmark study = thought-leadership, excluded by Materiality Gate; Develop launch was 2026-05, out of window). Access limits: freshdesk release notes unfetchable.
• PerformYard — all packages: No notable changes verified = Unknown. Sources scanned: support portal + press wires via search. Access limits: environment fetch block; nothing dated July indexed.
• Predictive Index — all packages: No notable changes verified = Unknown. Sources scanned: docs.predictiveindex.com release-notes collection via search index. Access limits: environment fetch block; no July 2026 entries indexed (latest: 2026-04/2026-05 era).
• UKG — all packages: No notable changes identified this window. Sources scanned: newsroom via search (July posts were customer-win PRs; UKG Beacon launch was 2025-11-04, out of window).

### Appendix: Low-confidence watchlist
• Microsoft Viva / Glint — Copilot-supported commenting for survey takers: private preview per the July News to Know, GA expected "later in the summer"; also flagged: mapping Viva Insights/Copilot usage metrics to survey items. Watch for the GA date.
• Qualtrics — Frontline Employee Voice (Early Access): listed 2026-07-22 as an exclusive Early Access documentation page — a frontline-listening push worth tracking as it matures toward GA.
• BambooHR — Images in Recognition posts: surfaced via aggregator/press summaries with no verifiable date; if confirmed, it's a Recognition & Rewards enhancement on the heels of the June module launch.

### Source Health — 2026-07 run (observed 2026-07-31)
> **Environment-wide fetch block** (example.com control also 403'd): every fetch below failed for environment reasons — do NOT add `bot_blocked` flags on this evidence alone. Entries marked (env) need re-testing from a fetch-capable environment before curation.

```text
- 15Five | https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): (none — page remains the right primary; re-fetch next run)
- Culture Amp | https://updates.cultureamp.com | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): (none — remains the right primary; July items never surfaced in search index)
- Lattice | https://lattice.com/blog/july-2026-product-updates | status: 404 (not yet published/indexed) | observed: 2026-07-31
  Suggested replacement (if found): https://lattice.com/product-updates/spring-summer-2026 (release hub; mixes June-shipped items — verify dates in-page)
- Predictive Index | https://docs.predictiveindex.com/en/collections/12282995-release-notes | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): (none — no July 2026 entries indexed yet)
- Qualtrics | https://community.qualtrics.com/product-release-notes-96 | status: login | observed: 2026-07-31
  Suggested replacement (if found): weekly note pages indexed with dated titles, e.g. https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-july-29-2026-33476
- Microsoft Viva / Glint | https://techcommunity.microsoft.com/category/viva-glint/blog/viva_glint_blog | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): dated monthly posts, e.g. https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463
- Betterworks | https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): dated release articles, e.g. https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026 ; press page https://www.betterworks.com/press
- BambooHR | https://www.bamboohr.com/product-updates/ | status: bot_blocked | observed: 2026-07-31
  Suggested replacement (if found): press releases https://www.bamboohr.com/about-bamboohr/press-release/ (dated child posts fetch better)
- Leapsome | https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements | status: bot_blocked | observed: 2026-07-31
  Suggested replacement (if found): https://site.leapsome.com/blog/leapsome-ai-people-data-foundation (July launch post; also probe .../product-updates-jul-2026 next run)
- Officevibe (Workleap) | https://help.workleap.com/en/ | status: replaced | observed: 2026-07-31
  Suggested replacement (if found): (still no changelog surface — workleap.com/blog is the closest dated surface)
- Engagedly | https://changelog.engagedly.com | status: bot_blocked | observed: 2026-07-31
  Suggested replacement (if found): https://engagedly.com/blog/ (dated posts; carried the merger announcement)
- SurveyMonkey | https://help.surveymonkey.com/en/surveymonkey/new/ | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): https://www.surveymonkey.com/product/features/whats-new/ ("What's new: Summer 2026" — undated items, use as discovery) + newsroom
- Perceptyx | https://perceptyxhelp.freshdesk.com/support/solutions/folders/63000237891 | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): https://blog.perceptyx.com (dated launch posts)
- Paylocity | https://www.paylocity.com/company/about-us/newsroom/in-the-news/ | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): https://investors.paylocity.com/news-releases/ (dated press releases fetched via index)
- Gallup | https://support.gallup.com/hc/en-us | status: bot_blocked (env) | observed: 2026-07-31
  Suggested replacement (if found): (none)
- Cornerstone OnDemand | (no curated source in file) | status: replaced | observed: 2026-07-31
  Suggested replacement (if found): https://www.cornerstoneondemand.com/company/news-room/press-releases/ + monthly release articles under /resources/article/ (July example in this report)
```

### Coverage report
```text
Competitors audited: 21/21   (all via WebSearch-only; 0 primaries fetched directly)
Sources fetched: 0   (blocked/stale this run: 17 — see Source Health; block was environment-wide, not vendor)
Items included: 13   (High=3, Medium=5, Low=5)
By package: Engagement=3 · Performance=2 · Recognition & Rewards=0 · Development=1 · Other=7
Most active this window: Betterworks (3 items)   ← shipping-velocity signal, descriptive only
No-notable-change pairs: 21 competitor entries recorded (most Unknown/access-limited — see appendix)
```
