# CI Report — September 2026

> **window:** 2026-09-01 → 2026-09-30 (America/Chicago) · **run date:** 2026-10-13
> First run under CI-Prompt v4.0 and CI-Competitor v3.0. All 21 competitors were read through at least one primary surface, using the new pre-flight tool (`tools/ci_sources.py`) plus five parallel research passes (performance suites, listening, HCM suites, talent and mid-market, market-wide press sweep). `WebFetch`, `curl`, and the tool's Python client all worked; the Wayback Machine was intermittent. Compared with July (22 items), coverage is broader because blocked sources were read through public APIs, feeds, and documentation indexes instead of search snippets. Dates are operative (GA / "now available") dates; see the Workflow Retro for what changed in the workflow itself.

---

## 1. Slack Digest — September 2026

```text
:wave: Monthly Competitor Update — September 2026  (2026-09-01 to 2026-09-30)
TL;DR: AI moved into the manager's core loop: 15Five's AI-drafted reviews went GA, Betterworks and Leapsome now turn 1:1 transcripts into goals and follow-ups, and Leapsome auto-drafts survey action plans, while Perceptyx opened its listening data to outside AI agents over MCP.

*Engagement*
• Leapsome | AI-generated survey action plans | Date: 2026-09-10
  Admins can now auto-generate editable action-plan drafts from survey results, with suggested owners and timelines.
  https://www.leapsome.com/app/#/product-updates
• Culture Amp | AI Follow-Ups in surveys | Date: 2026-09-08
  An AI "interviewer" now asks short, personalized follow-up questions based on each rating or comment in Engagement and Lifecycle surveys (AI-enabled, English-only accounts first).
  https://updates.cultureamp.com/156617-uncover-the-why-behind-your-data-with-ai-follow-ups

*Performance*
• Lattice | Goals and competencies in weighted review scores | Date: 2026-09-30
  Admins can blend manager ratings, goals, and competencies into one weighted, auto-normalized score that flows into calibration, alongside new half-point (0.1) rating scales.
  https://lattice.com/blog/september-2026-product-updates
• 15Five | AI-Assisted Reviews (GA) | Date: 2026-09-17
  AI-drafted review answers grounded in evidence from 15Five and connected work tools, including 1-on-1 meeting notes, are now generally available.
  https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
• Betterworks | Conversational Intelligence for 1:1s | Date: 2026-09-15
  1:1s now ingest Zoom or uploaded transcripts to produce shared recaps, private prep briefs, and suggested action items and goal updates.
  https://support.betterworks.com/hc/en-us/articles/48817244144781-Conversational-Intelligence-NextGen

*Recognition & Rewards*
• BambooHR | Recognition & Rewards in Slack with AI suggestions (beta) | Date: 2026-09-14
  Employees get AI-suggested recognition in Slack (message, points, and company value prefilled), with public recognition auto-posted to a channel and reactions synced back.
  https://www.bamboohr.com/product-updates/extend-recognition-into-slack

*Development*
• Betterworks | AI development plans + adaptive learning | Date: 2026-09-15
  Employees can build skill-linked development plans with AI-generated steps and AI-ranked courses from Docebo, LinkedIn Learning, or Udemy, plus AI-matched target roles.
  https://support.betterworks.com/hc/en-us/articles/49233961278861-AI-Powered-Adaptive-Learning-ALU-NextGen
• PerformYard | Talent Development suite | Date: 2026-09-01
  PerformYard launched a separately licensed suite: AI 1:1 prep and goal- and review-quality coaching, a five-level competency library with skill gaps, merit compensation cycles, and an AI-first "Ask PerformYard" builder.
  https://www.performyard.com/articles/introducing-performyard-talent-development

*Other / Cross-Platform*
• Perceptyx | Perceptyx Anywhere | Date: 2026-09-29
  A GA MCP server and API layer bring Perceptyx survey results, nudges, and action plans into Copilot, Claude, ChatGPT, or custom agents under existing confidentiality thresholds; attrition-predicting models are in pilot.
  https://blog.perceptyx.com/perceptyx-launches-perceptyx-anywhere
```
```text
No notable changes this window (sources scanned): Engagedly. Unknown (access-limited or not yet published): Energage (no public product surface), Paylocity (September roundup unpublished; site JS-walled), ADP and UKG in-product changes (press scanned, nothing material).
```

---

## 2. Roadmap Watch — Performance Squad (Slack paste-ready)

```text
:telescope: *Roadmap Watch — Performance Squad*  _(forward-looking; not shipped in September)_
Announced competitor items that overlap QW Performance (Reviews · Goals · 1-on-1s · Feedback), plus what shipped in the first days of October.

*:dart: Lattice — Fall/Winter '26 release (announced 2026-09-02)*  _(highest priority)_
• *Lattice Meetings*: every calendar meeting in one view, with the Lattice AI Agent capturing notes, action items, and summaries that feed reviews.  → overlap: *QW 1-on-1s*
• *Calibration Signals*: an AI pre-read per calibration group that flags people who look over- or under-rated against their performance signals.  → overlap: *QW Performance Reviews* (calibration)
• *Auto-Updates + agentic Slack app*: AI-drafted weekly updates built from Jira, GitHub, Linear, and Notion, submitted from Slack.  → overlap: *QW Goals / Feedback*
• *MCP write-back*: submit updates, feedback, and goals from ChatGPT, Claude, Slackbot, or Glean; admin natural-language analysis of review results this winter.  → overlap: *Other / Cross-Platform* (AI layer)
   https://lattice.com/blog/fall-winter-2026-product-release

*:large_yellow_circle: Shipped in early October (counts toward the October report)*
• *15Five MCP* (Claude, ChatGPT, Gemini; per-user login; write access a separate admin setting) and a *Meeting Assistant* agent that preps managers before 1-on-1s and logs notes and actions after (2026-10-08).  → overlap: *QW 1-on-1s* + AI layer
   https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
• *Culture Amp: Write Goals with AI Coach*, a side-panel conversation that drafts an individual or development goal (2026-10-07).  → overlap: *QW Goals*
   https://updates.cultureamp.com/159466-write-goals-with-ai-coach
• *Betterworks*: goal locks by business period, history hidden from newly assigned managers, and 1:1 AI insights scoped by department (2026-10-06).  → overlap: *QW Goals / 1-on-1s*
   https://support.betterworks.com/hc/en-us/articles/49415183670669-Release-October-6th-2026
• *Workday Rising*: Agent-Ready Tools (MCP) and custom agents GA, Sana inside Claude, Gemini, and Copilot, and an AI goal generator in 2026R2 (2026-10-02 to 10-13).  → overlap: *Other / Cross-Platform*, *QW Goals*
   https://newsroom.workday.com/2026-10-13-Workdays-Trusted-Agent-Platform-Now-Delivers-Headless-Access-to-HR-and-Finance,-Letting-Customers-Build-and-Run-Lawful-AI-Agents

*Takeaway:* the next fight is the 1-on-1. Betterworks and Leapsome (shipped), 15Five (Meeting Assistant), and Lattice (Meetings) are all turning meeting notes into review evidence with an AI agent in the room.

_Roadmap items are not commitments; confirm before acting._
```

---

# 3. Package Brief — September 2026

## Top Themes
- **AI turns the 1:1 into review evidence.** Betterworks ingests Zoom or uploaded 1:1 transcripts into recaps, prep, and goal updates (09-15); Leapsome's Smart Follow-Ups turn meeting transcripts into goals, praise, and requests (09-16); 15Five's AI-Assisted Reviews went GA with drafts grounded in 1-on-1 notes (09-17), and Amaya now analyzes review open text (09-25). Leapsome's review assistant now reads employees' personal Slack and Notion. Lattice (Meetings, Calibration Signals) and 15Five (Meeting Assistant, 10-08) extend this into October.
- **Listening-to-action closes with AI, and trust controls follow.** Leapsome auto-drafts survey action plans (09-10) and anchors survey insights to outcomes (09-07); Culture Amp's AI Follow-Ups probe answers mid-survey (09-08); Qualtrics nudges managers to finish action plans (09-02); Perceptyx's AI Insights went GA. On the trust side, Culture Amp flags sensitive comments before sharing (09-23), while Viva Glint's new Copilot comment rewrite is pitched as an anonymity aid but leaves no trace in reports.
- **Review design gets weighted, connected, and configurable.** Lattice combines ratings, goals, and competencies in one normalized score with decimal scales (09-30); Culture Amp brings goals and custom demographics into review cycles (09-29); Workleap adds hire-date-based probation and anniversary cycles; PerformYard ships a five-level competency library.
- **Development gets an AI planner.** Betterworks (AI development plans with LMS recommendations and role matching, 09-15), PerformYard (Talent Development suite, 09-01), Cornerstone (Team Mode skills workspace with a daily manager briefing), BambooHR (job profiles with role skills, 09-14), and Leapsome (development plans prefilled from reviews, 09-07).
- **People data opens to outside AI.** Perceptyx Anywhere (MCP + APIs, 09-29), BambooHR's MCP server with goal tools (beta, 09-14) and Bamboo AI open beta, Lattice MCP in Glean (09-30), Workleap's agent hub for custom MCP servers, Cornerstone's labor-market MCP tools. Governance is shipping alongside: permission-scoped MCP (Betterworks), audit trails for AI actions (BambooHR), retention controls (Viva Glint, Perceptyx). Context: Culture Amp launched MCP on 2026-08-24, so all three of QW's most frequent rivals now have one.

## Material Changes

### Engagement
```text
• Leapsome | AI-Generated Survey Action Plans | Est. Impact: High
  QW Package: Engagement
  State: GA • Change Type: New • Date: 2026-09-10 • Confidence: High
  What changed (fact): Admins can automatically generate editable action-plan drafts from survey results, with suggested owners and timelines, or trigger generation manually.
  Implication (labeled inference): A direct match for QW's AI-driven action planning in Engagement; differentiation shifts to trust and follow-through.
  Strategic Signal: AI layer — closes the survey-to-action loop.
  Source: https://www.leapsome.com/app/#/product-updates
  Notes: Public Product Updates Hub (no login), read through its JSON endpoint https://www.leapsome.com/api/release-notes; displayDate 2026-09-10. Listed in "AI in Leapsome: Overview & Settings" (help center, edited 2026-09-16).

• Culture Amp | AI Follow-Ups in Engagement and Lifecycle Surveys | Est. Impact: High
  QW Package: Engagement
  State: GA (staged rollout) • Change Type: New • Date: 2026-09-08 • Confidence: High
  What changed (fact): During Engagement and Lifecycle surveys, AI asks short, personalized follow-up questions based on a participant's rating or comment; full follow-up conversations land in the Comments report with search, filtering, and export.
  Strategic Signal: AI layer — AI embedded in the listening moment itself.
  Source: https://updates.cultureamp.com/156617-uncover-the-why-behind-your-data-with-ai-follow-ups
  Notes: Rolling out to AI-enabled Engagement customers using English-only surveys.

• Leapsome | Outcome-Driven Survey Insights with "Ask-Anything" AI | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: New • Date: 2026-09-07 • Confidence: High
  What changed (fact): Admins set outcomes or goals for a survey and get AI insights anchored to them, explore them through cards and a natural-language interface, and create action plans straight from an insight; one-click heatmap tiles with AI summaries followed on 2026-09-08.
  Strategic Signal: AI layer — analytics reframed around outcomes, with a direct path to action.
  Source: https://www.leapsome.com/app/#/product-updates

• Culture Amp | Sensitive Comment Management | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: New • Date: 2026-09-23 • Confidence: High
  What changed (fact): A Sensitive comments tab in a survey's Administrator Report flags comments across eight topics (names and locations, offensive language, harassment, discrimination, threats, possible self-harm), shows why each was flagged, and supports redaction via export before results are shared; Culture Amp never edits comments itself.
  Strategic Signal: Trust/Privacy — comment governance before results are shared.
  Source: https://updates.cultureamp.com/157983-introducing-sensitive-comment-management

• Microsoft Viva / Glint | Copilot Comment Rewrite for Survey Takers | Est. Impact: Medium
  QW Package: Engagement
  State: GA (rolling out end of September; off by default) • Change Type: New • Date: 2026-09 (day Unknown) • Confidence: Medium
  What changed (fact): Authenticated survey takers can have Copilot rewrite all or part of an open-text comment (all survey types except 360s); Microsoft pitches it as reducing recognizable writing patterns. A new admin control, off by default, gates it, and reports and exports do not show which comments were rewritten.
  Implication (labeled inference): Cuts both ways for listening data: more anonymity for participants, less certainty about comment authenticity for analysts.
  Strategic Signal: Trust/Privacy — AI as an anonymity aid inside listening.
  Source: https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-10-september-2026/4559810
  Notes: Learn doc (ms.date 2026-09-17): https://learn.microsoft.com/en-us/viva/glint/setup/rewrite-comments-copilot-viva-glint . M365 Roadmap item 560595 still read "In development" at run time.

• Perceptyx | AI Insights Dashboard (GA) | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: Enhancement • Date: 2026-09 (day Unknown) • Confidence: High
  What changed (fact): AI Insights is now generally available across the platform for customers with a Narrative Analysis Agent or Comment Copilot subscription, turning results into plain-language executive summaries at event close, each point linked to report detail (August had limited it to unrestricted administrators).
  Strategic Signal: AI layer — descriptive summaries for leaders.
  Source: https://perceptyxhelp.freshdesk.com/support/solutions/articles/63000289667-release-notes-september-2026

• Qualtrics | Action Plan Reminders (EX) | Est. Impact: Medium
  QW Package: Engagement
  State: GA • Change Type: New • Date: 2026-09-02 • Confidence: High
  What changed (fact): Managers get email or Microsoft Teams reminders to create and complete action plans on time, for Engagement, Pulse, and Lifecycle projects.
  Strategic Signal: Manager enablement — nudges close the listening-to-action loop.
  Source: https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-september-2-2026-33481
```
Low-impact changes (Engagement):
```text
• Qualtrics | EX heat map multilevel breakouts | 2026-09-30 | GA • Enhancement • Confidence: High | Heat maps break out scores by several fields at once (how confidentiality thresholds apply to intersections: Unknown) | https://community.qualtrics.com/product-release-notes-96/weekly-product-release-notes-september-30-2026-33717
• Culture Amp | Hide factors in shared reports | 2026-09-30 | GA • Enhancement • Confidence: High | Admins choose which factors each shared report shows; top opportunities recalculate on visible factors | https://updates.cultureamp.com/158625-hide-factors-in-shared-reports
• Leapsome | Multiple-choice option trends over time | 2026-09-23 | GA • Enhancement • Confidence: High | Survey dashboards track multiple-choice answers over time | https://www.leapsome.com/app/#/product-updates
• Peakon / Workday | Flexible Listening question model: self-service upgrade | 2026-09-16 | GA • Enhancement • Confidence: High | Eligible customers can self-upgrade (irreversible; becomes required later; others eligible in 27R1) | https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026/september/wednesday--16th-september.html
• 15Five | Amaya on custom Engage surveys | 2026-09-14 | GA • Enhancement • Confidence: High | The AI assistant answers questions about custom surveys and respects each campaign's minimum response count | https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
• Peakon / Workday | Open-ended question frequency at schedule level | 2026-09-09 | GA • Enhancement • Confidence: High | New schedule-level "Only once" option and a "Survey eligibility" section | https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026/september/wednesday--9th-september.html
• Peakon / Workday | Question Library export | 2026-09-09 | GA • Enhancement • Confidence: High | Export every question set, all languages, in one file | https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026/september/wednesday--9th-september.html
• Gallup | Share reports and action plans from mobile | 2026-09-28 | GA • Enhancement • Confidence: High | Q12 reports and engagement or CliftonStrengths action plans share as PDFs from the Gallup Access app | https://support.gallup.com/hc/en-us/articles/55871288474643-Share-Reports-and-Action-Plans-From-the-Gallup-Access-Mobile-App
• Gallup | AI Key Insights on mobile | 2026-09-04 | GA • Enhancement • Confidence: High | The AI summary of Q12 results (strengths, opportunities, recommendations) is now in the mobile app | https://support.gallup.com/hc/en-us/articles/55108815356819-Al-Generated-Key-Insights-Now-Available-on-Mobile
• Microsoft Viva / Glint | Multiple-choice list questions | 2026-09 (day Unknown) | GA • Enhancement • Confidence: High | CSV-uploaded option lists (up to 500, multilingual) with search and multi-select | https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-10-september-2026/4559810
• Perceptyx | Refreshed Activate Metrics (nudge engagement) | 2026-09 (day Unknown) | GA • Enhancement • Confidence: High | Admins track nudge view and reaction rates and nudge health by business unit | https://perceptyxhelp.freshdesk.com/support/solutions/articles/63000289667-release-notes-september-2026
```

### Performance
```text
• Lattice | Goals & Competencies in Weighted Scores | Est. Impact: High
  QW Package: Multiple (Performance primary; also Development via competencies)
  State: GA • Change Type: Enhancement • Date: 2026-09-30 • Confidence: High
  What changed (fact): Admins can combine downward review ratings, goals, and competencies into one overall score with adjustable section weights; scores normalize automatically across different rating scales, a missing section's weight is redistributed, and the score flows into calibration.
  Strategic Signal: Platform/Connected — goals, competencies, and reviews in one calibrated score.
  Source: https://lattice.com/blog/september-2026-product-updates
  Notes: Date is the monthly roundup's publication date; individual ship dates are not stated.

• 15Five | AI-Assisted Reviews (GA) | Est. Impact: High
  QW Package: Performance
  State: GA • Change Type: New • Date: 2026-09-17 • Confidence: High
  What changed (fact): AI-Assisted Reviews left beta: 15Five AI gathers evidence ("Moments") from 15Five and connected work tools, including Kona and Google Meet 1-on-1 notes, drafts answers to eligible open-text review questions, and gives managers a conversation guide; the writer decides what stays, and AI never submits a review.
  Strategic Signal: AI layer + Platform/Connected — review drafting grounded in cross-module evidence.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
  Notes: Total Platform and Perform & Goals plans; manual review cycles only. Beta since 2026-06-09. Feature doc: https://success.15five.com/hc/en-us/articles/51435628709147-AI-Assisted-Reviews-Feature-Overview

• Betterworks | Conversational Intelligence for 1:1s | Est. Impact: High
  QW Package: Multiple (Performance primary; also Development)
  State: GA (Phase 1) • Change Type: New • Date: 2026-09-15 • Confidence: High
  What changed (fact): 1:1s pull completed Zoom transcripts with no meeting bot (Zoom AI Companion with transcript retention), or accept uploaded or pasted transcripts from other tools; AI then produces a shared recap, a private prep brief per participant, and suggested action items, agenda topics, and goal creations or updates that users confirm before saving.
  Strategic Signal: AI layer — meeting content becomes goal updates and follow-ups inside the 1:1.
  Source: https://support.betterworks.com/hc/en-us/articles/48817244144781-Conversational-Intelligence-NextGen
  Notes: Phase 1 limits: Zoom is the only native source (Teams "coming soon"); no feedback, recognition, or skills extraction yet. Launch press: https://www.betterworks.com/betterworks-introduces-ai-powered-capabilities-to-give-organizations-real-time-visibility-into-workforce-readiness

• Lattice | Decimal-Point Rating Scales | Est. Impact: Medium
  QW Package: Performance
  State: GA (opt-in) • Change Type: Enhancement • Date: 2026-09-30 • Confidence: High
  What changed (fact): Rating scales accept increments down to 0.1 (e.g., half points on a 5-point scale), and reviews, calibration, analytics, and compensation treat them as real numbers instead of rounding.
  Source: https://lattice.com/blog/september-2026-product-updates

• Culture Amp | Goals in Reviews | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: New • Date: 2026-09-29 • Confidence: High
  What changed (fact): Admins can bring selected individual and development goals (read-only) into new review cycles: managers see them in Manager Reviews, employees in Self Reflections, reviewers can rate or comment on goals, and AI Coach can use goal context when helping complete reviews.
  Strategic Signal: Platform/Connected — goals feed the review moment.
  Source: https://updates.cultureamp.com/158621-goals-in-reviews-now-available
  Notes: Not available in Calibrations.

• Culture Amp | Custom Demographics in Performance Reviews | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-09-29 • Confidence: High
  What changed (fact): Review cycle setup and participation rules can use standard or custom account demographics (territory, business unit, region, cohort) to define and filter manager review populations, with sensitive demographics hidden from roles without access.
  Source: https://updates.cultureamp.com/158614-custom-demographics-now-available-in-performance-reviews
  Notes: Calibration support "coming soon."

• 15Five | Amaya Analyzes Performance-Review Open Text | Est. Impact: Medium
  QW Package: Performance
  State: GA • Change Type: Enhancement • Date: 2026-09-25 • Confidence: High
  What changed (fact): The Amaya AI assistant analyzes open-text answers in performance reviews, returning themes, sentiment, and representative quotes.
  Strategic Signal: AI layer.
  Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

• Leapsome | Smart Follow-Ups from Meeting Transcripts | Est. Impact: Medium
  QW Package: Performance (also Recognition & Rewards)
  State: GA • Change Type: Enhancement • Date: 2026-09-16 • Confidence: High
  What changed (fact): After a meeting, users get one-tap suggestions drawn from the transcript that create goals, praise, absence requests, or private notes.
  Strategic Signal: Platform/Connected — one 1:1 transcript feeds goals, recognition, and HR requests.
  Source: https://www.leapsome.com/app/#/product-updates
  Notes: Builds on Leapsome's Meeting Notetaker and AI 1:1 agenda suggestions (2026-08-05).

• Officevibe (Workleap) | Probation and Anniversary Review Cycles | Est. Impact: Medium
  QW Package: Performance
  State: GA (no beta label) • Change Type: New • Date: 2026-09 (day Unknown; inferred) • Confidence: Likely
  What changed (fact): Review cycles can run on each employee's hire date: "anniversary" cycles start individually or in weekly or monthly cohorts, and "tenure-based" cycles start once at 30, 60, or 90 days, 6 months, or 1 year, with per-person deadlines and automated start and lock dates.
  Strategic Signal: Point-solution — review-cycle automation.
  Source: https://help.workleap.com/en/articles/17006039-probation-anniversary-reviews-run-review-cycles-on-each-employee-s-hire-date
  Notes: Workleap publishes no release notes. Dated by the help article (last updated 2026-09-22) and Intercom article-ID ordering; recurring cycles and per-reviewer locking followed in October.
```
Low-impact changes (Performance):
```text
• Culture Amp | Shared facilitator layouts in calibration | 2026-09-30 | GA • Enhancement • Confidence: High | The facilitator's filters, sort, and columns become every participant's starting view | https://updates.cultureamp.com/158751-shared-facilitator-layouts-now-available
• Lattice | Disable review packet sharing | 2026-09-30 | GA • Policy/Compliance • Confidence: High | Super Admins can block packet sharing and export per cycle so review content stays in-platform | https://lattice.com/blog/september-2026-product-updates
• Lattice | Granular goals permissions | 2026-09-30 | GA • Enhancement • Confidence: High | Company and Department Goals carry separate management permissions | https://lattice.com/blog/september-2026-product-updates
• Culture Amp | Conditional follow-up questions in manager reviews | 2026-09-29 | GA • Enhancement • Confidence: High | Display rules reveal follow-ups based on a manager's earlier answers | https://updates.cultureamp.com/158618-more-relevant-manager-reviews-with-conditional-follow-up-questions
• Culture Amp | Add 1-on-1 topics in bulk | 2026-09-29 | GA • Enhancement • Confidence: High | One topic and note added to many 1-on-1 conversations at once | https://updates.cultureamp.com/158445-add-1-on-1-topics-in-bulk
• 15Five | Salesforce deal data in Focus Briefs and AI-Assisted Reviews | 2026-09-21 | GA • Integration • Confidence: High | Sellers' deals won, opened, and lost plus pipeline movement appear as review evidence | https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases
• Leapsome | Auto-archive stale goals | 2026-09-21 | GA • Enhancement • Confidence: High | Goals archive automatically after 30, 60, or 90 days without activity | https://www.leapsome.com/app/#/product-updates
• Betterworks | Clone a goal to all direct reports | 2026-09-15 | GA • Enhancement • Confidence: High | Managers copy one goal to every direct report in one action | https://support.betterworks.com/hc/en-us/articles/48397034657677-Release-August-25th-2026
• Betterworks | Conversations updates | 2026-09-15 | GA • Enhancement • Confidence: Medium | Per-cycle performance labels, hidden feedback for unbiased evaluation, document uploads, prior-conversation history, feedback word limits | https://support.betterworks.com/hc/en-us/articles/48822904432013-Summer-Release-September-2026
```

### Recognition & Rewards
```text
• BambooHR | Recognition & Rewards in Slack with AI-Generated Suggestions | Est. Impact: Medium
  QW Package: Recognition & Rewards
  State: Beta • Change Type: Integration • Date: 2026-09-14 • Confidence: High
  What changed (fact): Admins connect Recognition & Rewards to the BambooHR Slack app; employees then get AI-generated recognition suggestions in Slack, each with a prefilled message, point value, and Core Value, which they can send, edit, or dismiss. Public recognition can auto-post to a channel, Slack reactions and replies sync back, and Rewards users get a reminder to spend points before month-end.
  Implication (labeled inference): An HRIS QW customers may already own now ships points-based, AI-nudged recognition in the flow of work; QW's "no rival sells a rewards economy" claim holds for Lattice, Culture Amp, and Leapsome, not for BambooHR.
  Strategic Signal: AI layer — values-tagged recognition suggested in Slack.
  Source: https://www.bamboohr.com/product-updates/extend-recognition-into-slack
  Notes: Pro and Elite plans. BambooHR launched Recognition & Rewards (points, rewards) on 2026-06-04.
```
Low-impact changes (Recognition & Rewards):
```text
• Betterworks | Recognition card on the Manager Homepage | 2026-09-15 | GA • New • Confidence: Medium | Team recognition given and received, coverage vs. company average, who was recognized least recently, and a Give Recognition button | https://support.betterworks.com/hc/en-us/articles/48822904432013-Summer-Release-September-2026
• BambooHR | Automated birthday and work-anniversary celebrations | 2026-09-08 | GA • Enhancement • Confidence: High | Auto-posted celebrations with optional, tenure-based points; R&R settings reorganized | https://www.bamboohr.com/product-updates/automate-employee-milestones-with-redesigned-recognition-and-rewards-settings
```

### Development
```text
• Betterworks | AI Development Plans + Adaptive Learning & Upskilling | Est. Impact: High
  QW Package: Development
  State: GA • Change Type: New • Date: 2026-09-15 • Confidence: High
  What changed (fact): Employees create skill-linked development goals from their Talent Profile, add AI-generated development steps and AI-ranked courses from connected LMSs (Docebo, LinkedIn Learning, Udemy Business) as milestones with progress synced back, and set career aspirations that return AI-recommended target roles with a Skills Match Score; learning recommendations also surface in goals, 1:1s, check-ins, and reviews.
  Strategic Signal: Platform/Connected — 1:1 signals, skills, goals, and learning in one development loop.
  Source: https://support.betterworks.com/hc/en-us/articles/49233961278861-AI-Powered-Adaptive-Learning-ALU-NextGen
  Notes: IDP doc: https://support.betterworks.com/hc/en-us/articles/49233916303757-Individual-Development-Goals-IDP-NextGen ; Docebo integration doc created 2026-09-11.

• PerformYard | Talent Development Suite | Est. Impact: High
  QW Package: Multiple (Development primary; also Performance, Other / Cross-Platform)
  State: GA • Change Type: New • Date: 2026-09-01 • Confidence: High
  What changed (fact): A separately licensed suite with three products: Coaching (AI 1:1 prep, an employee insights page, a goal-quality coach, a review-feedback coach that flags bias and vague or rating-conflicting comments, a form-building coach), Competencies (role-based library with up to five levels and an exportable skill-gap view), and Compensation (budgeted merit cycles with approvals); an AI-first interface lets users describe a review cycle or goals and "Ask PerformYard" builds it.
  Strategic Signal: Platform/Connected — a performance point solution extending into development on shared data.
  Source: https://www.performyard.com/articles/introducing-performyard-talent-development
  Notes: No press release; dated by the launch article and Help Scout docs ("Last updated on September 1, 2026").

• Cornerstone OnDemand | Workforce AI Team Mode: Manager Skills Workspace | Est. Impact: Medium
  QW Package: Development
  State: GA • Change Type: New • Date: 2026-09 (day Unknown) • Confidence: Medium
  What changed (fact): Managers get a permission-gated Team Mode with a daily briefing banner, AI-badged team insights, an inbox of skill validations, a severity-ranked team skills pulse, AI "Focus Areas" and role fit per person, and side-by-side comparison of up to three reports; employees can self-assess skills, request manager or peer validation, and populate skills from a resume.
  Strategic Signal: Manager enablement — AI pushes team skill gaps to managers daily.
  Source: https://help.csod.com/cwfai/Content/Release/Sep2026/TeamModeUpdates.htm
  Notes: Found through the MadCap Flare TOC (the release is not search-indexed or press-released). Footer "Last Published: September 23, 2026"; month verified, day not stated. Cornerstone keeps only the current month's notes online.
```
Low-impact changes (Development):
```text
• Workday | 2026R2 talent updates | 2026-09-19 | GA (setup required) • Enhancement • Confidence: Medium | Career Hub with performance and development tasks, career interests in reviews, learning-linked development items | https://community-content.workday.com/en-us/public/feature-release/workday-success-plans--feature-release-reviews/2026r2-feature-release-review-webinars/2026r2-workday-talent-optimization-skills.html
• Betterworks | Talent and calibration admin | 2026-09-15 | GA • Enhancement • Confidence: Medium | Calibration cycle report, Talent Profile and Calibration in 31 languages, CSV talent import without an HRIS, group-scoped Skills and Succession | https://support.betterworks.com/hc/en-us/articles/48822904432013-Summer-Release-September-2026
• BambooHR | Job Organization with role skills | 2026-09-14 | GA • New • Confidence: High | Job titles become managed job profiles with skills from BambooHR's Skills Library and standardized job codes | https://www.bamboohr.com/product-updates/job-organization-in-bamboohr
• Leapsome | Development plans from reviews with AI autofill | 2026-09-07 | GA • Enhancement • Confidence: High | Create a development plan or PIP from the review conversation, prefilled from feedback, goals, and learning | https://www.leapsome.com/app/#/product-updates
```

### Other / Cross-Platform
```text
• Perceptyx | Perceptyx Anywhere: MCP Server + APIs, AI Evaluation, Workforce Models | Est. Impact: High
  QW Package: Multiple (Other / Cross-Platform primary; also Engagement)
  State: GA (Connect: MCP + APIs; Evaluate) / Pilot (Predict models, with Fortune 100 design partners) • Change Type: New • Date: 2026-09-29 • Confidence: High
  What changed (fact): Customers can connect Microsoft Copilot, Claude, ChatGPT, or their own agents to Perceptyx through an MCP server and APIs that return listening results, expert-written actions from a 3,000+ nudge library, and existing action plans, all under the user's Perceptyx permissions and confidentiality and aggregation thresholds. PYX Labs benchmarks how accurately a customer's AI interprets employee feedback; single-tenant models that flag regrettable-attrition and disengagement signals are in development with design partners.
  Implication (labeled inference): The first roster listening vendor to pair MCP access with company-specific attrition prediction, which is Retention Radar's territory, and to state that anonymity thresholds hold inside outside assistants.
  Strategic Signal: AI layer + Trust/Privacy.
  Source: https://blog.perceptyx.com/perceptyx-launches-perceptyx-anywhere
  Notes: State detail from https://go.perceptyx.com/platform/perceptyx-anywhere and https://go.perceptyx.com/platform/mcp ; "Perceptyx Anywhere will expand through 2027." No help-center documentation yet.

• Lattice | Lattice MCP in Glean's Connector Library | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Integration • Date: 2026-09-30 • Confidence: High
  What changed (fact): Lattice MCP is a native connector in Glean, so HR teams can connect Lattice, automate review, update, and feedback flows from Glean, and bring Lattice data into Workforce Intelligence reporting.
  Strategic Signal: AI layer — performance data addressable from enterprise AI platforms.
  Source: https://lattice.com/blog/september-2026-product-updates

• BambooHR | MCP Server + Claude Connector ("AI Connectors") | Est. Impact: Medium
  QW Package: Other / Cross-Platform (also Performance: goals)
  State: Beta • Change Type: Integration • Date: 2026-09-14 • Confidence: High
  What changed (fact): Admins enable AI Connectors for admins, specific access levels, or everyone; users then query and act on BambooHR data from Claude through the BambooHR MCP server, under existing permissions and with confirmation for writes. Tools span 11 areas including employees, reports, time off, hiring, and goals and goal comments.
  Strategic Signal: AI layer — HRIS people data, including goals, readable and writable from external assistants.
  Source: https://www.bamboohr.com/product-updates/bamboohr-ai-connectors
  Notes: Developer docs call it beta: https://documentation.bamboohr.com/docs/mcp-server . ChatGPT and Gemini "in a future release." The formal press launch was 2026-10-08 (out of window); the operative date is first public availability.

• BambooHR | Bamboo AI Open Beta for All Customers | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: Beta • Change Type: Enhancement • Date: 2026-09-14 • Confidence: High
  What changed (fact): Bamboo AI (private beta since 2026-07-21) is in open beta for all customers: a conversational report assistant, payroll run comparison and reminders, a scheduling assistant, AI job-architecture suggestions, a "Needs Your Attention" action inbox, and nightly data-hygiene checks, all permission-scoped with human review before changes apply.
  Strategic Signal: AI layer — embedded, human-reviewed assistants across an HR suite.
  Source: https://www.bamboohr.com/product-updates/bamboo-ai

• SurveyMonkey | Workday and BambooHR HRIS Integrations | Est. Impact: Medium
  QW Package: Other / Cross-Platform (also Engagement)
  State: GA (Enterprise plans; US and EU data centers) • Change Type: Integration • Date: 2026-09-28 • Confidence: Medium
  What changed (fact): Enterprise admins connect Workday or BambooHR, choose employee attributes to sync, and share the connection across the team; users target survey audiences by HRIS attributes and filter results by team, group, or location without manual contact uploads.
  Strategic Signal: Platform/Connected — HRIS-fed audiences push a general survey tool toward EX listening.
  Source: https://help.surveymonkey.com/en/surveymonkey/integrations/workday-integration/
  Notes: No release note or press item; date is the docs' first-publish date (embedded CMS date 2026-09-28), found via the help sitemap. Announced as forthcoming in the 2026-09-01 relaunch. BambooHR twin: https://help.surveymonkey.com/en/surveymonkey/integrations/bamboohr-integration/

• Leapsome | Review Assistant and Leapy Connect to Personal Slack and Notion | Est. Impact: Medium
  QW Package: Other / Cross-Platform (also Performance)
  State: GA • Change Type: Integration • Date: 2026-09-02 • Confidence: High
  What changed (fact): Employees can connect personal Slack (09-02) and Notion (09-17) accounts so the AI review assistant pulls their messages and pages in as review context, relevant Slack context now loads automatically (09-22), and admins can let the Leapy assistant use these connections on demand (09-28).
  Implication (labeled inference): Review AI grounded in private work-tool data raises consent and trust questions QW can answer.
  Strategic Signal: AI layer + Trust/Privacy.
  Source: https://www.leapsome.com/app/#/product-updates

• Betterworks | New Native Mobile App (NextGen) | Est. Impact: Medium
  QW Package: Other / Cross-Platform (also Performance)
  State: GA • Change Type: New • Date: 2026-09-08 • Confidence: High
  What changed (fact): A new native iOS app for NextGen aimed at frontline and deskless employees and managers, starting with 1:1 meetings (agenda, action items, shared notes); the old app is now "Betterworks Classic."
  Strategic Signal: Manager enablement — 1:1 capture for deskless managers.
  Source: https://apps.apple.com/us/app/betterworks/id6795434862
  Notes: Dated by the iTunes lookup API (release 2026-09-08). Android listing not verified.

• Betterworks | SCIM 2.0 Provisioning | Est. Impact: Medium
  QW Package: Other / Cross-Platform
  State: GA • Change Type: Integration • Date: 2026-09-15 • Confidence: Medium
  What changed (fact): Organizations can connect an identity provider through SCIM 2.0 to sync user creation, profile, manager and role changes, departments, and deactivation.
  Strategic Signal: Integration depth.
  Source: https://support.betterworks.com/hc/en-us/articles/48822904432013-Summer-Release-September-2026
  Notes: The SSO help article (edited 2026-08-26) still says SCIM is unsupported and no setup article exists yet, hence Medium.

• Officevibe (Workleap) | Workleap Agent: Personal App Integrations, Custom MCP Servers, HubSpot and Gong | Est. Impact: Medium
  QW Package: Other / Cross-Platform (also Performance)
  State: GA (no beta label) • Change Type: Integration • Date: 2026-09 (day Unknown; inferred) • Confidence: Likely
  What changed (fact): Employees connect their own work apps (19, including Asana, Jira, GitHub, Notion, Slack, Outlook, Teams) so the Workleap Agent can search them on demand when prepping 1:1s or drafting reviews; admins can register any OAuth-protected MCP server; HubSpot and Gong connectors were added. Docs state that content is not synced and that no report or review reads a person's connected apps.
  Strategic Signal: AI layer + Manager enablement.
  Source: https://help.workleap.com/en/articles/16947955-personal-integrations-connect-your-apps-to-the-workleap-agent
  Notes: No release notes or press. Dated by help-article timestamps (custom MCP 2026-09-15, HubSpot 09-23, Gong 09-24) and Intercom article-ID ordering.
```
Low-impact changes (Other / Cross-Platform):
```text
• Lattice | Slack Enterprise org-wide install | 2026-09-30 | GA • Integration • Confidence: High | Install across a whole Slack Enterprise org and post broadcasts such as Praise to any channel | https://lattice.com/blog/september-2026-product-updates
• Lattice | Notification channel selector | 2026-09-30 | GA • Enhancement • Confidence: High | Admins set org-wide allowed channels (email, Slack, Teams) for cycle notifications | https://lattice.com/blog/september-2026-product-updates
• Lattice | Self-localized custom naming | 2026-09-30 | GA • Enhancement • Confidence: High | Custom singular and plural term translations per supported language | https://lattice.com/blog/september-2026-product-updates
• Lattice | e-Signatures for compensation statements | 2026-09-30 | GA • Enhancement • Confidence: High | Employees can be required to e-sign comp statements, tracked with timestamps | https://lattice.com/blog/september-2026-product-updates
• Leapsome | AI and agent retrieval of goals | 2026-09-29 | GA • Enhancement • Confidence: High | AI and agents retrieve all current-year goals with comments and progress history | https://www.leapsome.com/app/#/product-updates
• Betterworks | MCP access scoped to modules and permissions | 2026-09-22 | Beta • Enhancement • Confidence: High | MCP tools honor org-level module availability and each user's permissions | https://support.betterworks.com/hc/en-us/articles/49088998990861-Release-September-22nd-2026
• Betterworks | Global Search for goals, milestones, and teams | 2026-09-22 | GA • Enhancement • Confidence: High | Search now covers goals, milestones, and teams | https://support.betterworks.com/hc/en-us/articles/49088998990861-Release-September-22nd-2026
• Betterworks | SAML SSO SHA-256 by default | 2026-09-08 | GA • Policy/Compliance • Confidence: High | SHA-256 becomes the SAML default; IdP signing failures fixed (09-22) | https://support.betterworks.com/hc/en-us/articles/48755740503565-Release-September-8th-2026
• Betterworks | AI Performance Summary redesign and model routing | 2026-09-15 | GA • Enhancement • Confidence: Medium | Redesigned AI performance summary; Gemma 4 added alongside Llama with per-request routing | https://support.betterworks.com/hc/en-us/articles/48822904432013-Summer-Release-September-2026
• BambooHR | Audit trail for AI-made changes | 2026-09-14 | Beta • Enhancement • Confidence: High | The audit trail shows whether a person, a person via Bamboo AI, or Bamboo AI itself made each change | https://www.bamboohr.com/product-updates/audit-trail-agent-attribution-and-ui-updates-beta
• Leapsome | Survey and review data in the AI widget builder | 2026-09-02 | GA • Enhancement • Confidence: High | Natural-language dashboard widgets can use survey and review questions as data | https://www.leapsome.com/app/#/product-updates
• Microsoft Viva / Glint | Survey-data export APIs (private preview) + Visier connector | 2026-09-02 | Pilot • Integration • Confidence: High | Approved customers export survey responses through Microsoft Graph with audit logging; Visier's connector pulls them into its workforce model | https://techcommunity.microsoft.com/blog/microsoft_365blog/introducing-viva-glint-apis-for-survey-data-export-and-visier-integration/4547896
• Microsoft Viva / Glint | Copilot admin assistant (phase 1) | 2026-09 (day Unknown) | GA • New • Confidence: High | Guidance-only admin Copilot for configuration questions, with deep links; cannot change settings | https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-10-september-2026/4559810
• Microsoft Viva / Glint | Deleted-user data retention controls | 2026-09-01 | GA • Policy/Compliance • Confidence: Medium | Admins choose to retain or erase a deleted user's email and employee ID | https://techcommunity.microsoft.com/blog/viva_glint_blog/news-to-know-%E2%80%93-volume-3-edition-9-august-2026/4552283
• Perceptyx | Self-service reporting groups and permissions | 2026-09 (day Unknown) | GA • New • Confidence: High | Event creators manage reporting groups and data-access tiers inside Advanced Reporting | https://perceptyxhelp.freshdesk.com/support/solutions/articles/63000289667-release-notes-september-2026
• Perceptyx | Data-retention policy controls | 2026-09 (day Unknown) | GA • Policy/Compliance • Confidence: High | Platform admins define retention and cleanup schedules | https://perceptyxhelp.freshdesk.com/support/solutions/articles/63000289667-release-notes-september-2026
• Cornerstone OnDemand | Labor-market MCP tools + HCM skill-data integrations | 2026-09 (day Unknown) | GA (via account manager) • Integration • Confidence: Medium | MCP tools expose labor-market skills data; Oracle Fusion HCM, SAP SuccessFactors, and SFTP skill imports added | https://help.csod.com/cwfai/Content/Release/Sep2026/MCP.htm
• SurveyMonkey | "Today's SurveyMonkey" relaunch | 2026-09-01 | GA (staged) • Enhancement • Confidence: Medium | Redesigned UI and a personalized home that recommends surveys or listening programs; bundles AI features shipped June to August | https://www.surveymonkey.com/newsroom/surveymonkey-introduces-todays-surveymonkey/
• Predictive Index | Retake the Self-Concept | 2026-09-01 | GA • Enhancement • Confidence: High | Employees retake only the Self-Concept part of the assessment; Obi can send retakes | https://docs.predictiveindex.com/en/articles/16516469-9-1-2026-retake-the-self-concept-inspire-obi
```

## Appendix: No notable changes
```text
• Energage — all packages: No notable changes verified = Unknown.
  Sources scanned: energage.com feed (newest 2026-07-14), sitemaps (nothing in September), Google News (Top Workplaces awards only). Access limits: no public product surface (help center in-app and login-only; energage.zendesk.com closed; WP JSON 403).
• Engagedly — all packages: No notable changes identified this window.
  Sources scanned: Beamer changelog backend (newest entry 2026-07-14, the merger notice), WP JSON posts and press category, PR Newswire list. Access limits: none. Caveat: 85 help articles were edited in September with no dates or release language; possible unannounced changes, not countable.
• ADP — all packages: No notable changes identified in public channels; in-product changes = Unknown.
  Sources scanned: MediaRoom press list and RSS (September: employment reports, AWS partnership, board nominations, earnings date), Google News. Access limits: in-product release notes are login-only.
• UKG — all packages: No notable changes identified in press channels; in-product changes = Unknown.
  Sources scanned: UKG newsroom (read through the tool; Cloudflare challenges curl and WebFetch), Business Wire releases via FinancialContent syndication, Google News (Gartner MQ awards, a customer win). Access limits: in-product notes login-only.
• Paylocity — all packages: No notable changes verified = Unknown (timing and access).
  Sources scanned: Releasebot aggregator (dated through 2026-09-22; September posts explain Ignite AI agents launched 2026-07-21), Google News (a customer win). Access limits: every paylocity.com path is JS-walled; the September "What's New" roundup was unpublished at run date.
• Microsoft Viva / Glint — Performance / Recognition & Rewards / Development: No notable changes identified this window.
  Sources scanned: Glint board RSS (full September and August editions), Microsoft 365 blog RSS, M365 Roadmap API, Learn docs. Access limits: none.
• Qualtrics — Performance / Recognition & Rewards / Development / Other: No notable changes identified this window.
  Sources scanned: all five September weekly release notes in full (public; the old "login" label did not reproduce), newsroom. Access limits: none. Excluded at the gate: XM Data & AI platform and Healthcare XM (both "available in 2027").
• SurveyMonkey — Performance / Recognition & Rewards / Development: No notable changes identified (not SurveyMonkey product areas).
• Gallup — Performance / Recognition & Rewards / Development / Other: No notable changes identified this window.
  Sources scanned: "Gallup Product Updates" section via the Zendesk API (3 articles total), newest-created help articles, Google News (research and polls only). Access limits: HTML is Cloudflare-blocked; the API is clean.
• Perceptyx — Performance / Recognition & Rewards / Development: No notable changes identified this window.
  Sources scanned: September and August release notes, blog RSS and listing pages 1 to 3. Access limits: none.
• Peakon / Workday — Recognition & Rewards / Other: No notable changes identified this window.
  Sources scanned: all 24 Peakon 2026 release notes, the Workday newsroom (full September list), Google News. Access limits: Release Center login-only. Excluded: Total Benefits (2026-09-24; benefits administration, outside QW packages). Workday's agent and MCP launches are dated 2026-10-13 (Rising).
• Lattice — Engagement / Recognition & Rewards / Development: No notable changes identified this window.
  Sources scanned: September roundup, Fall/Winter release post, Product Updates blog category. Access limits: none.
• Culture Amp — Recognition & Rewards / Development: No notable changes identified this window (newsfeed scanned, all September cards).
• 15Five — Recognition & Rewards / Development / Other: No notable changes identified this window (running list scanned via the Zendesk API).
• Leapsome — Recognition & Rewards: No notable changes identified (praise appears only through Smart Follow-Ups).
• Betterworks — Engagement: No notable changes identified (both September sprint notes: "no updates made to Betterworks Engage").
• BambooHR — Engagement / Performance: No notable changes identified (product-updates feed, 578 items; goals exposure is via the MCP item).
• PerformYard — Engagement / Recognition & Rewards: No notable changes identified (site and help-center sitemaps).
• Predictive Index — Engagement / Performance / Recognition & Rewards / Development: No notable changes identified (release notes; no PI Perform entries in 2026).
• Cornerstone OnDemand — Engagement / Performance / Recognition & Rewards: No notable changes identified (Workforce AI September What's New, 13 topics; classic change log newest 2026-08-21).
• Officevibe (Workleap) — Engagement / Recognition & Rewards / Development: No verified in-window items (help sitemap; September edits were bulk updates). See watchlist.
```

## Appendix: Low-confidence watchlist
```text
1. Officevibe (Workleap) | "Feedback to monitor" | Date: Unknown (help doc last updated 2026-09-02) | AI flags anonymous feedback that may signal a safety concern (self-harm, threats, harassment, distress) and emails designated HR contacts, without revealing the author's identity. High relevance to QW's anonymity positioning. https://help.workleap.com/en/articles/16789929-feedback-to-monitor
2. Predictive Index | MCP connector for Obi (Claude, Copilot, ChatGPT) | State: Pilot ("pre-beta"; request early access) | Date: Unknown (docs visible from about 2026-09-18). https://docs.predictiveindex.com/en/articles/16444686-what-is-the-predictive-index-mcp-connector
3. Peakon / Workday | 2026R2 listening items (Talent Sentiment agent, Peakon and Workday Wellness integration, People Analytics Peakon integration) | Named on public R2 feature pages; production dates and state unverifiable (Release Center login-only). https://community-content.workday.com/en-us/public/feature-release/workday-success-plans--feature-release-reviews/2026r2-feature-release-review-webinars/2026r2-workday-peakon-employee-voice.html
```

## Source Health — 2026-09 run (observed 2026-10-13)
Every fix below was applied to `CI-Competitor.md` v3.0 in this run (see Workflow Retro).
```text
- Betterworks | https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes | status: bot_blocked (HTML and Atom) | observed: 2026-10-13
  Replacement (verified this run): same section via the public Help Center API (route: zendesk_section)
- Leapsome | https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements | status: stale (frozen 2026-02-16) | observed: 2026-10-13
  Replacement (verified this run): https://www.leapsome.com/api/release-notes?page=1&limit=100 (route: json_api; cite https://www.leapsome.com/app/#/product-updates)
- Leapsome | https://site.leapsome.com/blog/product-updates-mar-2026 (monthly pattern) | status: stale (discontinued after 2026-04) | observed: 2026-10-13
  Replacement (verified this run): the hub above
- Gallup | https://support.gallup.com/hc/en-us | status: bot_blocked (Cloudflare) | observed: 2026-10-13
  Replacement (verified this run): https://support.gallup.com/hc/en-us/sections/53122467937811-Gallup-Product-Updates (route: zendesk_section)
- Lattice | https://lattice.com/blog/may-2026-product-updates | status: stale (month-pinned) | observed: 2026-10-13
  Replacement (verified this run): https://lattice.com/blog/{month}-{year}-product-updates (route: monthly_url)
- Lattice | https://help.lattice.com/hc/en-us | status: 404 (help center migrated off Zendesk) | observed: 2026-10-13
  Replacement (verified this run): https://help.lattice.com/en-us/ (undated)
- Culture Amp | https://support.cultureamp.com/en/collections/17746165-2026-product-updates | status: 404 | observed: 2026-10-13
  Replacement (verified this run): none needed; https://updates.cultureamp.com (route: intercom_news, per-post permalinks)
- Culture Amp | five 2025/2026 year-pinned help articles | status: stale (newest 2026-07-23) | observed: 2026-10-13
  Replacement (verified this run): removed; the newsfeed is the live surface
- SurveyMonkey | https://help.surveymonkey.com/en/surveymonkey/new/release-notes/ | status: stale (newest 2026-02) | observed: 2026-10-13
  Replacement (verified this run): https://www.surveymonkey.com/product/features/whats-new/ (now dated), https://www.surveymonkey.com/newsroom/ , https://help.surveymonkey.com/sitemap-en.xml (route: sitemap)
- Workday Peakon | https://doc.workday.com/peakon/en-us/workday-peakon-employee-voice/product-updates/release-notes/2026.html | status: bot_blocked (JS-empty) | observed: 2026-10-13
  Replacement (verified this run): any 2026 child page's nav tree (route: dated_links)
- Peakon / Workday | (no source in file) | status: replaced | observed: 2026-10-13
  Replacement (verified this run): https://newsroom.workday.com/press-releases?l=100 (route: dated_links)
- ADP | (no source in file) | status: replaced | observed: 2026-10-13
  Replacement (verified this run): https://mediacenter.adp.com/press-releases?l=100 (route: dated_links); www.adp.com newsroom returns 403
- UKG | (no source in file) | status: replaced | observed: 2026-10-13
  Replacement (verified this run): https://www.ukg.com/company/newsroom (readable through the tool only; Cloudflare challenges curl and WebFetch)
- BambooHR | https://www.bamboohr.com/product-updates/ | status: bot_blocked (JS shell) | observed: 2026-10-13
  Replacement (verified this run): https://www.bamboohr.com/product-updates/feed/ (route: rss)
- BambooHR | https://help.bamboohr.com/ | status: JS shell (no text) | observed: 2026-10-13
  Replacement (verified this run): removed; https://documentation.bamboohr.com/docs/mcp-server for AI status
- Paylocity | https://www.paylocity.com/company/about-us/newsroom/in-the-news/whats-new-<month>-<year>/ | status: replaced (blog moved) + bot_blocked (JS interstitial) | observed: 2026-10-13
  Replacement (verified this run): none readable; new pattern https://www.paylocity.com/resources/learn/blogs/whats-new-blog-{month}-{year}/ (blocked), discovery via https://releasebot.io/updates/paylocity/paylocity
- Cornerstone OnDemand | (no source in file) | status: replaced | observed: 2026-10-13
  Replacement (verified this run): https://help.csod.com/cwfai/Data/Tocs/PrimaryTOC_Chunk0.js (route: dated_links), https://help.csod.com/sa/Content/SingleArchitecture/Whats_New/ChangeLog_for_SA.htm , https://www.cornerstoneondemand.com/sitemaps/press/sitemap.xml (route: sitemap)
- Engagedly | https://changelog.engagedly.com | status: bot_blocked (JS-only) | observed: 2026-10-13
  Replacement (verified this run): https://changelog.engagedly.com/loadMoreNews?app_id=mZiIYhKZ41992&language=EN&publicPage=true&page=0 (Beamer backend)
- Engagedly | https://engagedly.com/blog/?integration=Product+Updates | status: stale (newest 2024-05-31) | observed: 2026-10-13
  Replacement (verified this run): https://engagedly.com/wp-json/wp/v2/posts?categories=472 (route: wp_json)
- Energage | (no source in file) | status: replaced | observed: 2026-10-13
  Replacement (verified this run): https://www.energage.com/feed/ (route: rss; stale since 2026-07-14); no public product surface exists
- Officevibe (Workleap) | https://help.workleap.com/en/ | status: replaced (no what's-new surface) | observed: 2026-10-13
  Replacement (verified this run): https://help.workleap.com/sitemap.xml (route: sitemap), https://www.prnewswire.com/news/workleap/ , https://workleap.com/category/news
- PerformYard | https://www.prweb.com/ | status: replaced (not a PerformYard source) | observed: 2026-10-13
  Replacement (verified this run): https://www.performyard.com/sitemap.xml and https://support.performyard.com/sitemap.xml (route: sitemap; the help center is Help Scout, not Zendesk)
- Microsoft Viva / Glint, Qualtrics, Perceptyx | edition URLs, community release notes, Freshdesk folder | status: earlier bot_blocked / login labels did not reproduce | observed: 2026-10-13
  Replacement (verified this run): Glint board RSS + Microsoft 365 blog RSS (route: rss); Qualtrics index (html); Perceptyx folder (html) + blog RSS
- web.archive.org | status: intermittent (worked early in the run; "Temporarily Offline" and resets from about 01:22 UTC) | observed: 2026-10-13
```

## Coverage report
```text
Competitors audited: 21/21
Sources fetched: about 400 requests across the tool and five research passes (registry after curation: 55 sources)
Items included: 74   (High=8, Medium=21, Low=45)
By package: Engagement=18 · Performance=18 · Recognition & Rewards=3 · Development=7 · Other=28
Most active this window: Betterworks (12), Leapsome (9), Lattice (9), Culture Amp (8)   ← shipping-velocity signal, descriptive only
No-notable-change pairs: 68 (see Appendix)
Environment notes: WebFetch, curl, and the tool's Python client all live, with different results per site; web.archive.org intermittent; Google News rate-limits after about 15 rapid queries. HR Tech (2026-10-20 to 10-22) and Workday Rising (2026-10-12 to 10-15) fall in October, so October will be heavier.
```

---

# 4. Workflow Retro

```text
Pre-flight (before curation, registry v2.4): 42 fetchable sources: OK=11 STALE=6 FAIL=9 NODATE=16 · 5 competitors with no sources · no healthy source: 13 of 21 (Gallup, Peakon / Workday, SurveyMonkey, ADP, Betterworks, Cornerstone OnDemand, Energage, Engagedly, Leapsome, Officevibe (Workleap), Perceptyx, Predictive Index, UKG) · runtime 2m36s
After curation (registry v3.0):            55 sources: OK=39 STALE=5 FAIL=2 NODATE=9 · 0 competitors with no sources · no healthy source: 1 of 21 (Energage: no public product surface) · runtime 5s

Why the workflow wasn't learning (root cause):
- Source Health only proposed replacements; "a human promotes them" had no owner, so five months of suggestions sat unactioned and every run re-hit the same walls.
- /ci-report's allowed-tools were Read, WebFetch, WebSearch, Glob: a run could not save its report or edit the registry even if it wanted to.
- The route-around list was untested: its top move (Wayback) was "unreachable" via WebFetch in 2026-07, and the Zendesk Atom feeds it recommended 403 like the HTML.

What broke, and what worked:
- Betterworks | /hc/ HTML + Atom 403 (every run since 2026-05) → Zendesk Help Center JSON API (all 146 notes, dated)
- Leapsome | help-center running list frozen, monthly blog discontinued → public Product Updates Hub's JSON endpoint (264 dated entries)
- Gallup | Cloudflare 403 on HTML → Zendesk API revealed a new dated "Gallup Product Updates" section
- Microsoft Viva / Glint | "title only" via WebFetch → curl reads full bodies (gzip-encoded); board RSS carries full posts; some launches post on the Microsoft 365 board
- Workday Peakon | year index JS-empty → nav tree embedded in any child page lists every dated note
- Cornerstone | no source; newsroom client-rendered → MadCap Flare TOC exposed an unindexed monthly "What's New"
- Engagedly | JS-only changelog → Beamer backend (loadMoreNews)
- UKG | Cloudflare challenges curl and WebFetch → the tool's Python client reads the newsroom
- Officevibe (Workleap) | no changelog anywhere → Intercom help sitemap + article timestamps (Likely-confidence dating)
- SurveyMonkey | stale release notes → per-item-dated What's New + help sitemap (found the HRIS integrations) + email newsletter leads
- Qualtrics, Perceptyx, Glint | inherited "login" / "bot_blocked" labels → did not reproduce; re-test inherited labels every run
- Paylocity | JS interstitial on every path, all clients → unresolved (Releasebot for discovery)
- Energage | no public product surface → unresolved (structural)

Registry changes applied (CI-Competitor.md v3.0):
- Schema: per-source `route`, `verified`, `cite`, and per-competitor `news_query`; new `undated` flag; `newsroom` and `aggregator` kinds.
- All 21 competitors re-verified; 5 previously source-less competitors (Peakon / Workday, ADP, Cornerstone OnDemand, Energage, UKG) now have sources.
- Promoted/re-routed: Betterworks (zendesk_section, sitemap, press index, iTunes lookup), Leapsome (json_api hub, zendesk_recent), Gallup (zendesk_section), 15Five (zendesk_article, zendesk_recent), Culture Amp (intercom_news permalinks), Lattice (monthly_url template, new help center), Glint (board RSS, M365 blog RSS), Peakon / Workday (dated_links nav tree and newsroom), ADP (dated_links), BambooHR (rss), Cornerstone (Flare TOC, change log, press sitemap), Engagedly (Beamer backend, wp_json press), Workleap (help sitemap, PR Newswire, news), PerformYard (sitemaps), Predictive Index (MCP docs, news sitemap, feed), SurveyMonkey (What's New, newsroom, help sitemap), Qualtrics (newsroom), Perceptyx (blog RSS, MCP page), UKG (newsroom), Paylocity (new blog pattern, flagged bot_blocked; Releasebot).
- Removed: dead or superseded URLs (Culture Amp 404 collection and year-pinned pages, Leapsome frozen article and roundup pattern, BambooHR JS-shell help center, Lattice old help root, PerformYard's prweb.com root, Paylocity's old in-the-news pattern).
- news_query added for generic names (Lattice, Gallup, ADP, UKG, Energage, Qualtrics) and aliases (Workleap Agent, Amaya, Sana, Bamboo AI).
- Five months of Source Health logs archived to reports/source-health-archive-2026-05-to-07.md; the file now carries only Open source issues.

Playbook changes applied (CI-Prompt.md v4.0):
- New tested Access Playbook (10 moves), replacing the untested list: try all three clients; Zendesk Help Center API; feeds and CMS APIs (Beamer, Cision MediaRoom, Adobe query-index, public SPA JSON); documentation-platform indexes (MadCap Flare, AEM nav trees, Intercom/Help Scout sitemaps); Wayback (now marked intermittent); dated Google News sweep (pacing, date post-filtering, wire mirrors); sitemaps with real lastmod; email newsletters as leads.
- Date discipline: Chicago-time conversion (midnight UTC = date-only); seasonal roll-ups and back-dated hubs; JSON-LD/RSS republish stamps; dating aids (iTunes lookup, readme.io updatedAt, M365 Roadmap API).
- Output: compact one-line format for Low items; optional Roadmap Watch and landscape slide; mandatory Workflow Retro.
- Process: pre-flight with tools/ci_sources.py; the run saves its report and curates the registry in the open; /ci-report can now write files.

Proposals needing human sign-off:
- Digest size: this run lists 9 items (target 5–8) because coverage tripled (74 verified items vs 22 in July). Proposal: set the target to 6–10.
- Roster: add R&R pure-plays (Workhuman, Achievers, Awardco, Bonusly, Nectar)? BambooHR's points-based, AI-suggested recognition shows R&R pressure now also comes from HRIS suites; the August board review flagged the pure-play gap.
- JS-rendering route: Chromium and Playwright are preinstalled in the cloud environment; a rendering route would read JS-only pages such as Paylocity's roundups. Scope it to rendering public pages; never to solving CAPTCHAs or managed challenges.
- Cadence: Cornerstone keeps only the current month online and Leapsome back-dates its hub, so run on the 3rd to 7th of each month, and run October after 2026-10-22 (Workday Rising and HR Tech).

Open issues for next run (start here; mirrored in CI-Competitor.md):
- Paylocity: JS interstitial on every path → try first: Releasebot + --news, then the proposed rendering route.
- Energage: no public product surface → watch Engagedly's Beamer changelog for joint post-merger news.
- ADP, UKG: in-product release notes login-only → press channels only; label in-product changes Unknown.
- Officevibe (Workleap): undated releases → help sitemap + article timestamps; watch for a changelog launch.
- Cornerstone OnDemand: "What's New" keeps only the current month → never skip a month.
- Leapsome: back-dated hub entries → re-pull at run time.
- October volume: Workday Rising + HR Tech → run after 2026-10-22.
```
