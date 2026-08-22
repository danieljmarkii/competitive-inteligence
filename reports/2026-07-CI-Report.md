# CI Report — July 2026

> **window:** 2026-07-01 → 2026-07-31 (America/Chicago) · **run date:** 2026-08-03
> Full run with `WebFetch` live. Direct fetch succeeded for Culture Amp, 15Five, Predictive Index, Perceptyx, Engagedly (blog), Leapsome (blog), Lattice; search route-arounds recovered Betterworks, Qualtrics, Viva Glint, Paylocity, BambooHR, Cornerstone. Note: `web.archive.org` is unreachable from this environment, so the Wayback route-around was unavailable this run.

---

## 1. Slack Digest — July 2026

```text
:wave: Monthly Competitor Update — July 2026  (2026-07-01 to 2026-07-31)
TL;DR: The AI-agent/MCP wave hit HR tech in one month — BambooHR, Leapsome, Betterworks, and Paylocity all shipped agent platforms or MCP connectivity that opens their people data to external AI assistants — while Energage and Engagedly announced a merger combining culture research with an AI talent-management platform.

*Engagement*
• Microsoft Viva / Glint | Refreshed Global Benchmarks | Date: 2026-07
  Glint's external benchmarks are being refreshed on survey data collected July 2025–June 2026, rolling out GA across July/August for more current comparisons in reporting.
  https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463

*Performance*
• Culture Amp | AI Coach in Peer & Upward Feedback | Date: 2026-07-22
  Employees can now use AI Coach assistance while writing peer and upward feedback inside performance review cycles.
  https://updates.cultureamp.com

*Development*
• Cornerstone OnDemand | July Release: Readiness Agents + Performance Assistant | Date: 2026-07
  Cornerstone's July release ships AI Readiness Agents (Proactive Coach, Internal Mobility), a Performance Assistant for manager coaching, and Role Readiness Academies that tie learning to measurable role readiness.
  https://www.cornerstoneondemand.com/resources/article/turning-talent-development-into-workforce-readiness-you-can-measure/

*Other / Cross-Platform*
• BambooHR | Bamboo AI — embedded agents + MCP platform | Date: 2026-07-21
  BambooHR introduced Bamboo AI, a system of AI agents embedded across HR/payroll/talent, plus a shared agent platform letting customers connect BambooHR to external AI tools via APIs, SDKs, and MCP.
  https://www.globenewswire.com/news-release/2026/07/21/3330490/0/en/BambooHR-Introduces-Bamboo-AI-a-Connected-Intelligence-Platform-Built-to-Work-While-Leaders-Focus-on-Empowering-People.html
• Leapsome | New ATS + AI-generated workflows + MCP connectivity | Date: 2026-07-15
  Leapsome launched an ATS (early access), AI-generated workflows/dashboards/competency frameworks, five AI agents, and MCP connectivity — extending its platform from recruiting through compensation on one people-data foundation.
  https://site.leapsome.com/blog/leapsome-ai-people-data-foundation
• Energage + Engagedly | Merger announced | Date: 2026-07-14
  Energage (Top Workplaces, 20+ yrs culture research, 30M+ surveys) and Engagedly (AI talent management) announced a merger uniting engagement measurement, talent management, and employer brand in one company.
  https://engagedly.com/blog/energage-and-engagedly-merge/
• Paylocity | Ignite AI — platform-wide AI + agents | Date: 2026-07-21
  Paylocity launched Ignite AI: embedded agents (Answer & Insight, Payroll Analysis, Candidate Fit, Time Correction, and more) plus an AI Hub dashboard for governing AI use across the org.
  https://www.paylocity.com/company/about-us/newsroom/press-releases/paylocity-launches-ignite-ai-redefining-industry-ai-leadership/
• Betterworks | MCP Server (Beta) | Date: 2026-07-14
  A new Betterworks MCP Server (beta) lets customers securely query Betterworks performance data from AI tools like ChatGPT and Claude.
  https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026
```
```text
No notable changes this window (sources scanned): Perceptyx (blog scanned — July posts are research/thought leadership), PerformYard. Unknown/access-limited or not yet published: Lattice (July roundup not yet posted at run time), Workday Peakon (July notes not yet published), Gallup, SurveyMonkey, Officevibe/Workleap, ADP, UKG.
```

---

## 2. Package Brief — July 2026

### Top Themes
- **MCP / AI-agent connectivity is the month's defining move.** Four roster competitors shipped it in the same window — BambooHR (Bamboo AI + MCP), Leapsome (MCP + five agents), Betterworks (MCP Server beta), Paylocity (Ignite AI agents) — with Cornerstone adding Readiness Agents. Rivals are making their people data addressable by external AI assistants (ChatGPT, Claude, Gemini), a direct run at the "connected platform + AI layer" ground QW competes on.
- **Consolidation:** the Energage + Engagedly merger combines two tracked competitors — culture research/recognition brand (Top Workplaces) with an AI talent-management suite — creating a listening + talent + employer-brand platform story.
- **AI is moving into the feedback-writing moment.** Culture Amp put AI Coach into peer/upward feedback and probation reviews; Viva Glint has Copilot-assisted survey commenting in private preview; Cornerstone shipped a Performance Assistant for manager coaching. AI drafting/coaching inside reviews and surveys raises authenticity and trust questions QW can speak to.
- **Global listening table stakes rose quietly:** Viva Glint refreshed benchmarks (Jul 2025–Jun 2026 data), Qualtrics shipped EX25 certified questions in 35 languages, Culture Amp added 27 languages to its Performance Culture Diagnostic template.
- **Integration depth as stickiness:** 15Five shipped a Rippling HRIS connector plus HRIS-sync group filters, continuing its post-HRIS-Sync-2.0 plumbing investment.

### Material Changes

#### Engagement
```text
• Microsoft Viva / Glint | Refreshed Global Benchmarks | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-07 (day Unknown; staged GA "July/August") • Confidence: Medium
  What changed (fact): Glint's external benchmarks are refreshed using Viva Glint survey data collected July 2025–June 2026, giving customers more current external comparisons in reporting.
  Strategic Signal: Point-solution — deepens survey benchmarking within the listening silo.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463
  Notes: TechCommunity page body does not render to fetch (title only); content confirmed via indexed search snippets. Rollout is staged over July/August.

• Microsoft Viva / Glint | Copilot-Supported Survey Commenting | Est. Impact: Low
  QW Package: Engagement
  State: Pilot • Change Type: New • Date: 2026-07 (private preview; GA "later in the summer") • Confidence: Medium
  What changed (fact): Survey takers in a private preview can use an in-survey Copilot experience to polish written feedback before submitting.
  Strategic Signal: AI layer — AI enters the comment-writing moment; authenticity/trust implications for listening data.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463

• Qualtrics | EX25 Certified Questions in 35 Languages | Est. Impact: Low
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-07-22 • Confidence: Medium
  What changed (fact): Updated EX25 methodology questions (short, targeted listening) are now available in 35 languages for global Engagement programs.
  Source: https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-july-22-2026-33475
  Notes: Community release notes are login-walled; content verified from indexed titles/snippets.

• Culture Amp | Performance Culture Diagnostic — 27 New Languages | Est. Impact: Low
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-07-24 • Confidence: High
  What changed (fact): The Performance Culture Diagnostic survey template gained 27 new languages with a localized participant experience across all Tier 2 supported languages.
  Source: https://updates.cultureamp.com
```

#### Performance
```text
• Culture Amp | AI Coach in Peer & Upward Feedback | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-07-22 • Confidence: High
  What changed (fact): Employees can now use AI Coach assistance when completing peer and upward feedback forms during performance review cycles.
  Implication (labeled inference): AI-drafted 360 feedback is becoming default UX in performance tools; QW should have a stance on authenticity safeguards.
  Strategic Signal: AI layer — action-embedded AI inside the feedback workflow.
  Source: https://updates.cultureamp.com

• Culture Amp | AI Highlights & Opportunities in Probation Reviews | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-07-24 • Confidence: High
  What changed (fact): Managers see AI-generated summaries of up to 3 key strengths and 3 growth opportunities during probation reviews.
  Strategic Signal: AI layer — manager-facing summarization in a review moment.
  Source: https://updates.cultureamp.com

• Culture Amp | Map Performance Ratings to Performance Groups | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-07-07 • Confidence: High
  What changed (fact): Admins can map rating choices to four standardized performance groups without changing the rating scales/labels raters see, standardizing downstream reporting.
  Source: https://updates.cultureamp.com

• 15Five | Kona Auto-Join Scope Choice | Est. Impact: Low
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-07-21 • Confidence: High
  What changed (fact): Managers/admins can choose whether the Kona AI assistant auto-joins all 1-on-1 meetings or only newly created ones.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
```

#### Recognition & Rewards
```text
(No verified items this window — see Appendix.)
```

#### Development
```text
• Cornerstone OnDemand | July Release — Readiness Agents, Performance Assistant, Role Readiness Academies | Est. Impact: Medium
  QW Package: Development (also affects Performance)
  State: GA • Change Type: New • Date: 2026-07 (day Unknown) • Confidence: Medium
  What changed (fact): Cornerstone's July release adds Role Readiness Academies (outcome-driven readiness), a Performance Assistant for manager coaching, and Readiness Agents (Proactive Coach Agent, Internal Mobility Agent) that turn skills data, goals, and workforce signals into coaching and mobility actions.
  Strategic Signal: AI layer + Manager enablement — agents that act on connected talent signals, not just dashboards.
  Source: https://www.cornerstoneondemand.com/resources/article/turning-talent-development-into-workforce-readiness-you-can-measure/

• 15Five | Coaching Scheduler | Est. Impact: Low
  QW Package: Development
  State: GA • Change Type: Enhancement • Date: 2026-07-02 • Confidence: High
  What changed (fact): Coaching users pick a preferred date/time first and are matched with an available coach in their timezone, with expanded EMEA/APAC coverage.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
```

#### Other / Cross-Platform
```text
• BambooHR | Bamboo AI — Connected Intelligence Platform | Est. Impact: High
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-21 • Confidence: High
  What changed (fact): BambooHR introduced Bamboo AI, embedded AI agents and intelligence across core HR, payroll, benefits, and talent, plus a shared agent platform where customers/partners build agents and connect BambooHR to external AI tools via APIs, SDKs, and MCP — governed inside the org's existing security model with audit trails.
  Implication (labeled inference): SMB/mid-market buyers will increasingly expect an agent/MCP story from every people-tech vendor, including EX platforms.
  Strategic Signal: AI layer + Platform/Connected — governed agents acting across an HR suite.
  Source: https://www.globenewswire.com/news-release/2026/07/21/3330490/0/en/BambooHR-Introduces-Bamboo-AI-a-Connected-Intelligence-Platform-Built-to-Work-While-Leaders-Focus-on-Empowering-People.html

• Leapsome | ATS + AI-Generated Workflows + MCP Connectivity | Est. Impact: High
  QW Package: Multiple (Other / Cross-Platform primary; touches Development, Performance, Engagement)
  State: GA (AI workflows, dashboards, agents, MCP) / Beta-Early access (ATS) • Change Type: New • Date: 2026-07-15 • Confidence: Medium
  What changed (fact): Leapsome launched an ATS (early access), AI-generated workflows (onboarding/learning paths from prompts), AI-generated competency frameworks and dashboards, five AI agents (Development Coach, Culture Advisor, Data Analyst, PeopleOps Partner, HR Helpdesk), MCP connectivity, and an ADP Workforce Now payroll export integration.
  Implication (labeled inference): Leapsome is explicitly selling the "one connected people-data foundation" story — recruiting through compensation — that QW claims for EX; its agents run across modules.
  Strategic Signal: Platform/Connected + AI layer — cross-module data foundation with agents on top.
  Source: https://site.leapsome.com/blog/leapsome-ai-people-data-foundation
  Notes: Official blog post is undated on-page; 2026-07-15 operative date from the syndicated press release. Custom dashboards stated "later this quarter."

• Energage + Engagedly | Merger Announced | Est. Impact: High
  QW Package: Other / Cross-Platform
  State: GA (announced/closed per announcement) • Change Type: Corporate (M&A) • Date: 2026-07-14 • Confidence: High
  What changed (fact): Energage (Top Workplaces recognition program; 20+ years culture research, 30M+ employee surveys across 80K orgs) merged with Engagedly (AI-powered talent management: performance, development, learning, rewards/recognition, frontline support), backed by NewSpring Growth; the combined company connects employee engagement, talent management, and employer brand.
  Implication (labeled inference): Two single-package-ish competitors just became one multi-package platform story overnight; expect cross-sell into both installed bases.
  Strategic Signal: Platform/Connected — engagement measurement fused to a talent-management suite.
  Source: https://engagedly.com/blog/energage-and-engagedly-merge/
  Notes: Corporate/structural event, not a shipped feature; included because it changes the competitive set itself (both parties are on the roster). No product-integration timeline was stated.

• Paylocity | Ignite AI — Platform AI + Agents | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: New • Date: 2026-07-21 • Confidence: High
  What changed (fact): Paylocity launched Ignite AI, platform-wide AI with agents (Answer & Insight natural-language queries, Payroll Analysis anomaly detection, Candidate Fit, Resume Summary, Data Inspection, Time Correction) plus an Ignite AI Hub dashboard for managing and measuring AI use across the organization.
  Strategic Signal: AI layer — HCM-side agents; the AI-governance hub is the notable pattern.
  Source: https://www.paylocity.com/company/about-us/newsroom/press-releases/paylocity-launches-ignite-ai-redefining-industry-ai-leadership/

• Betterworks | MCP Server (Beta) | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: Beta • Change Type: New • Date: 2026-07-14 • Confidence: Medium
  What changed (fact): A new Betterworks MCP Server (beta) lets customers securely access Betterworks performance data from compatible AI tools such as ChatGPT and Claude; the same release also auto-strips harmful HTML/script content via API.
  Strategic Signal: AI layer — performance data opened to external assistants.
  Source: https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026
  Notes: Help-center article 403s to direct fetch; content verified via indexed snippets and a syndicated announcement ("Betterworks Launches New AI Capabilities That Connect Performance Data to AI Assistants"). No Classic or Engage updates in this sprint.

• 15Five | Rippling HRIS Integration | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Integration • Date: 2026-07-10 • Confidence: High
  What changed (fact): Organizations can set up a Rippling connection directly from the HRIS Connector, with optional SSO configuration.
  Strategic Signal: Integration depth — shipped HRIS connector, stickiness play.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

• Culture Amp | General AI Coach on Home Page | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07-13 • Confidence: High
  What changed (fact): AI Coach is now accessible from a collapsible right-side panel on the Home page, in addition to the full-screen experience — making the assistant a persistent platform surface.
  Strategic Signal: AI layer — assistant promoted to an always-on platform surface.
  Source: https://updates.cultureamp.com

• 15Five | HRIS Group Filters & Exclusion Detail | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07-16 • Confidence: High
  What changed (fact): HRIS sync configuration gains group filters, with excluded groups clearly displayed during sync setup.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

• 15Five | Amaya & Insights — Chart/Table Downloads | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07-16 • Confidence: High
  What changed (fact): Users can download charts as PNG and export tables as CSV from Amaya and Insights for presentations and reports.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

• Microsoft Viva / Glint | Entra Multitenant Sign-In (Auto Tenant Discovery) | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07 (day Unknown) • Confidence: Medium
  What changed (fact): Survey Access adds seamless Entra authorization for multitenant organizations with automatic tenant discovery at sign-in.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463

• Predictive Index | Consolidated Directory, Quick Action Panels, Software Access from Directory | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07-07 • Confidence: High
  What changed (fact): Admins get a consolidated directory table with quick-action panels and can manage software access directly from the directory.
  Source: https://docs.predictiveindex.com/en/articles/15781821-7-7-2026-consolidated-directory-table-quick-action-panels-manage-software-access-from-directory-platform

• Predictive Index | Org Upload Workflow Enhancements | Est. Impact: Low
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Enhancement • Date: 2026-07-21 • Confidence: High
  What changed (fact): The organization data upload workflow was streamlined for admins.
  Source: https://docs.predictiveindex.com/en/articles/15888044-7-21-2026-org-upload-workflow-enhancements-platform
```

### Appendix: No notable changes
```text
• Lattice — all packages: No notable changes verified = Unknown (timing).
  Sources scanned: Product Updates hub (fetched clean — newest items June 2026), Blog category (fetched clean — newest roundup June 30). Access limits: none; the July 2026 monthly roundup was not yet published/indexed at run time (2026-08-03). Recheck when https://lattice.com/blog/july-2026-product-updates goes live. Lattiverse '26 announcements (MCP early access, AI Agent expansions) were June-dated and out of window.
• Workday Peakon — all packages: No notable changes verified = Unknown.
  Sources scanned: doc.workday.com release notes (June 2026 pages indexed/live; 2026 index renders empty to fetch; July child pages 404 — likely not yet published). Access limits: JS-rendered index.
• Gallup — all packages: No notable changes verified = Unknown.
  Sources scanned: support.gallup.com (no public dated release-notes surface); web search (no dated July 2026 product items). Access limits: no dated public changelog exists.
• SurveyMonkey — Engagement/Other: No notable changes verified = Unknown.
  Sources scanned: help-center What's New hub + Release Notes page (fetched clean but stale — newest entry February 2026); "What's new: Summer 2026" page (fetched clean — 16 items, none individually dated, so none can be pinned to the July window); newsroom via search (nothing July-dated). Access limits: dated surface is stale; see watchlist.
• Officevibe (Workleap) — all packages: No notable changes verified = Unknown.
  Sources scanned: help.workleap.com (no what's-new surface); web search for a Workleap changelog (none found). Access limits: no live public product-updates surface identified — source curation gap persists.
• Engagedly — product packages: No notable product changes verified = Unknown (merger captured as material item).
  Sources scanned: changelog.engagedly.com (known JS-only/bot_blocked, not readable); blog via fetch/search (merger post verified; L&D-updates post undated). Access limits: JS-only changelog.
• Energage — product packages: No notable product changes identified this window (merger captured as material item).
  Sources scanned: web search + engagedly.com merger announcement. Access limits: no public product changelog.
• ADP — all packages: No notable changes verified = Unknown.
  Sources scanned: web search (no dated July 2026 talent/engagement release found; marketplace/product pages undated). Access limits: no curated dated source in CI-Competitor.md.
• UKG — all packages: No notable changes verified = Unknown (see watchlist for People Assist GA).
  Sources scanned: ukg.com newsroom via search (July items were customer-win press releases — non-material). Access limits: no curated dated source.
• PerformYard — all packages: No notable changes identified this window.
  Sources scanned: web search (only dated launch found was Meetings, 2025-05-13 — out of window); support.performyard.com has no dated release-notes surface. Access limits: no dated changelog.
• Perceptyx — all packages: No notable product changes identified this window.
  Sources scanned: blog.perceptyx.com (fetched clean; 10 July posts reviewed — thought leadership/research; AI Coach post describes an existing capability; Pyx Voice is a research benchmark publication, see watchlist). Freshdesk release-notes folder not re-fetched (historically bot_blocked). 
• Betterworks — Engagement (Engage) & Performance packages: No notable changes this sprint per release note ("no updates to Classic or Engage"); MCP Server captured under Other / Cross-Platform.
• Culture Amp — Recognition & Rewards / Development: No notable changes identified this window (newsfeed scanned clean; July items were Engagement/Performance/Platform).
• 15Five — Engagement / Recognition & Rewards: No notable changes identified this window (running list scanned clean).
• Predictive Index — Engagement / Performance / Recognition & Rewards / Development: No notable changes identified this window (release-notes index scanned clean; July items were Platform/Hire; the Hire co-branded candidate email item is recruiting-scoped and outside QW packages).
• Qualtrics — Performance / Recognition & Rewards / Development: No notable changes identified this window (July 1/22/29 weekly notes reviewed via indexed snippets; remaining items were survey-platform/research-panel scoped, low materiality for QW packages).
• Microsoft Viva / Glint — Performance / Recognition & Rewards / Development: No notable changes identified this window.
• Leapsome / BambooHR / Paylocity / Cornerstone — remaining packages: no additional in-window items beyond those recorded above.
```

### Appendix: Low-confidence watchlist
```text
1. UKG People Assist agent GA in Google Gemini Enterprise — GA was "expected July 2026" per the 2026-04-29 announcement; could not confirm it actually went GA in-window. https://www.ukg.com/company/newsroom/ukg-launches-google-clouds-gemini-enterprise-agent-gallery
2. SurveyMonkey "Summer 2026" bundle (AI chat survey editing, Claude connector, Insights automated analysis, Programs) — real shipped features but the seasonal page carries no per-item dates, so July-window membership is unverifiable. https://www.surveymonkey.com/product/features/whats-new/
3. Perceptyx "Pyx Voice" benchmark for AI in employee feedback (2026-07-22) — a published benchmark/research asset rather than a customer feature today, but signals Perceptyx productizing trust-in-AI measurement. https://blog.perceptyx.com/pyx-voice-the-first-benchmark-for-ai-in-employee-feedback
```

### Source Health — 2026-07 run (observed 2026-08-03)
```text
- Betterworks | https://support.betterworks.com/hc/en-us/articles/47375805538573-Release-July-14th-2026 | status: bot_blocked | observed: 2026-08-03
  Suggested replacement (if found): none stable — content recovered via search-indexed snippets; section Atom feed .../sections/360012378232/articles.atom also 403s now; note web.archive.org is unreachable from this environment, removing the Wayback route-around.
- Microsoft Viva / Glint | https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-7-july-2026/4532463 | status: bot_blocked | observed: 2026-08-03
  Suggested replacement (if found): none — title renders, body does not; content recovered via WebSearch (same pattern as 2026-05).
- Qualtrics | https://community.qualtrics.com/product-release-notes-96 | status: login | observed: 2026-08-03
  Suggested replacement (if found): weekly note pages remain indexed with rich snippets, e.g. https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-july-22-2026-33475
- Leapsome | https://site.leapsome.com/blog/product-updates-mar-2026 (pattern) | status: stale | observed: 2026-08-03
  Suggested replacement (if found): monthly-roundup slug pattern appears discontinued (jul-2026 and july-2026 both 404); July content published as a launch post instead: https://site.leapsome.com/blog/leapsome-ai-people-data-foundation — treat site.leapsome.com/blog as the index to drill.
- Leapsome | https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements | status: bot_blocked | observed: 2026-08-03 (not re-fetched; known wall)
  Suggested replacement (if found): (as above)
- Lattice | https://lattice.com/blog/july-2026-product-updates | status: 404 | observed: 2026-08-03
  Suggested replacement (if found): not a wall — the July roundup simply wasn't published yet at run time; hub https://lattice.com/product-updates fetched clean. Re-run this vendor mid-August.
- Workday Peakon | https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026.html | status: bot_blocked (JS-empty) | observed: 2026-08-03
  Suggested replacement (if found): month child pages fetch/index fine when they exist (e.g. .../2026/june/wednesday--10th-june.html); July pages 404 — likely not yet published.
- SurveyMonkey | https://help.surveymonkey.com/en/surveymonkey/new/release-notes/ | status: stale | observed: 2026-08-03
  Suggested replacement (if found): https://www.surveymonkey.com/product/features/whats-new/ (live seasonal roundup, but undated per-item — pair with newsroom for dates)
- Officevibe (Workleap) | https://help.workleap.com/en/ | status: replaced | observed: 2026-08-03
  Suggested replacement (if found): still none — no live Workleap what's-new/changelog surface found; curation gap persists.
- Engagedly | https://changelog.engagedly.com | status: bot_blocked | observed: 2026-08-03 (JS-only; backend feed still unidentified)
  Suggested replacement (if found): https://engagedly.com/blog/ (dated corporate posts; merger announcement verified there)
- Paylocity | https://www.paylocity.com/company/about-us/newsroom/in-the-news/whats-new-july-2026/ | status: bot_blocked (JS-empty) | observed: 2026-08-03
  Suggested replacement (if found): dated press releases fetch clean, e.g. https://www.paylocity.com/company/about-us/newsroom/press-releases/paylocity-launches-ignite-ai-redefining-industry-ai-leadership/
- Cornerstone OnDemand | (no curated source in file) | status: replaced | observed: 2026-08-03
  Suggested replacement (if found): https://www.cornerstoneondemand.com/resources/topics/cornerstone-news/ (dated release articles, e.g. the July-release article used this run)

VERIFIED-GOOD primaries this run (keep):
- Culture Amp | https://updates.cultureamp.com | fetched clean, dated (newest 2026-07-24)
- 15Five | https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases | fetched clean, dated (page updated 2026-07-24)
- Predictive Index | https://docs.predictiveindex.com/en/collections/12282995-release-notes | fetched clean, dated
- Perceptyx | https://blog.perceptyx.com | fetched clean, dated (better than the bot-walled Freshdesk folder)
- Engagedly | https://engagedly.com/blog/... | dated posts fetch clean
- Leapsome | https://site.leapsome.com/blog/... | dated posts fetch clean
```

### Coverage report
```text
Competitors audited: 20/20
Sources fetched: 14 clean (direct WebFetch)   (blocked/stale/JS-empty this run: 12 — see Source Health; WebSearch route-arounds recovered content for Betterworks, Qualtrics, Viva Glint, Paylocity, BambooHR, Cornerstone, UKG)
Items included: 22   (High=3, Medium=7, Low=12)
By package: Engagement=4 · Performance=4 · Recognition & Rewards=0 · Development=2 · Other=12
Most active this window: Culture Amp and 15Five (5 items each)   ← shipping-velocity signal, descriptive only
No-notable-change pairs: see Appendix (11 competitors fully Unknown/no-change; plus package-level pairs for active vendors)
Environment notes: WebFetch live all run; web.archive.org unreachable (Wayback route-around unavailable). Two vendors' July surfaces (Lattice roundup, Peakon July notes) were not yet published at run date 2026-08-03 — a mid-August recheck would close both gaps.
```
