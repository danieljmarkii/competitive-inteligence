# CI Feature Deep-Dive — Goal Cycles

> **type:** feature deep-dive (not a monthly window report) · **run date:** 2026-08-10 (America/Chicago)
> **feature under study:** Goal cycles — time-boxed goal-setting periods/cadences, cycle administration, and the goal workflows attached to them
> **QW package impacted:** Performance (Goals) · methodology adapted from CI-Prompt.md v3.4; competitor list per CI-Competitor.md v2.3

---

## 1. Purpose & scope

QW's Performance package includes Goals ("aligned goal creation, tracking, and progress visibility" — CI-Context.md §2). Several competitors organize goal-setting around an explicit **cycle** construct: an admin-defined, time-boxed period (quarterly, annual, custom) that controls when goals are created, updated, closed, and rolled over. This deep-dive maps who has a true cycle concept, how it works, and — per QW's evaluation lens (CI-Context.md §5) — how deeply each vendor's goal cycles connect to the rest of their platform (reviews, 1:1s, check-ins, analytics, AI).

**Competitors covered (all from CI-Competitor.md; none invented):**
- Primary profiles: Lattice, Leapsome, Culture Amp, 15Five, Betterworks
- Secondary sweep: Engagedly, PerformYard, Predictive Index (PI Perform), Officevibe (Workleap), Microsoft Viva (Viva Goals status), BambooHR

Not covered (no meaningful goal-cycle surface expected, or out of goal scope): Gallup, Qualtrics, SurveyMonkey, Peakon/Workday, Perceptyx, Energage, ADP, Paylocity, Cornerstone OnDemand, UKG. These are listening/HCM-centric for this feature; anything found incidentally lands in the watchlist.

**Evidence rules applied:** official vendor surfaces only; blocked sources routed around per CI-Prompt.md (Wayback, feeds, search-index titles/snippets) — never bypassing logins; unverifiable details labeled Unknown; plain https URLs; ISO dates.

---

## 2. TL;DR

(to be completed after synthesis)

---

## 3. Competitor profiles

### Lattice
(pending)

### Leapsome
(pending)

### Culture Amp
(pending)

### 15Five

**Cycle concept & naming.** The OKR feature is named "Objectives" (labels customizable — admins can rename "Objective"/"Key result"). There is no standalone named goal-cycle object; the time-box is the **Time period** field on each objective (e.g., "Q3 2025"), governed by an org-level cadence in admin "Scheduling Details": set the business-calendar end date and how frequently the org sets objectives — monthly, quarterly, annually, or custom — which controls the time-period options offered at creation. Note: "cycles" in 15Five vocabulary means Best-Self Review cycles, not goals.
Sources: https://success.15five.com/hc/en-us/articles/360039474931-Configure-Objectives-feature-settings · https://success.15five.com/hc/en-us/articles/360002682112

**Cycle mechanics.** End-of-period is "Close and assess": closing holds the last known status and completion percentage and prevents further changes (a soft lock), with an optional rating/reflection; closed/archived objectives can be reopened. Admins get bulk close/archive of all past-due objectives from the All objectives page, plus a "Past due" filter. Automated rollover or auto-creation of next-period objectives: Unknown (not documented — methodology guidance has owners manually decide what carries forward at quarter-end). Reminders: objectives appear at the top of each weekly Check-in; dedicated deadline reminders Unknown.
Sources: https://success.15five.com/hc/en-us/articles/360016574411-Close-and-assess-an-objective · https://success.15five.com/hc/en-us/articles/360032868252-Understanding-the-All-objectives-page

**Goal model.** Full OKR structure: objective + up to 5 key results (numeric, percent, or binary, with start/target values and per-KR owners). Four scopes: company, group, individual, self-development (self-development is excluded from review cycles). Parent/child alignment with child visibility now decoupled from the parent (2026-03-11). Weighted OKRs (2025-10-14): editable weights totaling 100%, progress calculated from weighted completion of KRs and child objectives; admin toggle for weight fields (2026-03-26). Statuses on track / behind / at risk, set from the Objectives tab or inside Check-ins. Visibility: public / permission-based / private, plus a Global Objective Viewers role (2026-03-11).
Sources: https://success.15five.com/hc/en-us/articles/50988751840539-Objectives-Feature-Overview · https://success.15five.com/hc/en-us/articles/42109542197915-Weighting-Key-Results-and-child-Objectives

**Cross-module connections.** Objectives update inline in weekly Check-ins (including from Slack, 2025-09-24); managers add objective-specific talking points to 1-on-1 agendas; review cycles include an Objectives section with a timeframe filter (objectives with start/end dates inside the selected window are pulled in) and can feed performance-rating calculations; HR Outcomes Dashboard has an Objectives view (% on track vs. at-risk/behind). AI: objectives data powers coaching insights, Focus Briefs, and AI-Assisted Reviews; AI-Assisted Self Reviews draft answers synthesizing Check-ins + Objectives + Kona data (2025-10-17). Objectives→compensation link: Unknown.
Sources: https://success.15five.com/hc/en-us/articles/50988631925915-Enable-Objectives-in-a-performance-review-cycle · https://success.15five.com/hc/en-us/articles/15565493389083-HR-Outcomes-Dashboard-Feature-Overview

**Recent changes (dated, from the What's-new running list).**
- 2025-09-24 — Submit Check-ins from Slack, including OKR updates
- 2025-10-14 — Weighted OKRs
- 2025-10-17 — AI-Assisted Self Reviews (synthesizes Objectives data)
- 2026-02-11 — Amaya AI assistant; New Insights Dashboard
- 2026-03-11 — Global Objective Viewers; custom visibility for aligned objectives
- 2026-03-26 — Objective weights settings toggle
- 2026-05-20 — Custom Automated Review Schedules (review cycles, not goal cycles)
- 2026-06-09 — 15Five Agents & Context Layer; Focus Briefs; AI-Assisted Reviews (Beta)
Source: https://success.15five.com/hc/en-us/articles/50989471559067-What-s-new-in-15Five-Product-releases

**Positioning (labeled as positioning).** OKRs are framed as a weekly-rhythm alignment tool ("review them all, weekly") kept alive through Check-ins and reviews rather than a standalone goal system; sold in Perform, Legacy Focus, and Total Platform packages.
Source: https://www.15five.com/products/perform/okrs-and-goals

### Betterworks
(pending)

---

## 4. Secondary sweep

### Engagedly — has a true, named goal-cycle construct
- Admin settings expose "Enable preset goal cycles" (employees pick a predefined cycle at goal creation) and "Enable custom goal cycles"; marketed cadences are quarterly, semi-annual, annual, or custom.
- Dual model — the product is literally "OKRs & Goals": top-down cascading from top-level initiatives to individual contributors, bottom-up OKR creation, an alignment view, and key results convertible into child goals. Top-level goals exist at organization / department / business-unit levels.
- Product page claims "seamless integration" of goals with Performance (reviews) and Meetings modules plus "Discuss Goals" social features; linkage mechanics unverifiable from fetched pages — Unknown at detail level.
- No dated 2025–2026 goal release notes found on official surfaces. Current marketing pushes "Marissa AI" / "Agentic AI powered OKRs" and "Goal Setting AI Agents" (undated).
- Sources: https://engagedly.com/product/okrs-and-goals/ · https://help.engagedly.com/configure-goals-settings

### PerformYard — no goal cycle; review cycle is the time-box
- Goals are ongoing objects with due dates and active/closed states; the platform's time-box is the admin-created review cycle, not a goal cycle.
- General/SMART goals, explicitly not OKR-first (their copy: OKR software is for org-level strategy alignment; HR goal software focuses on individual and team goals). Cascading goals and alignment-to-company-objectives views are supported.
- Tight review coupling: goal progress is available directly inside performance review forms; review cycles can include a "Goal Creation Form"; separate goal check-in feature.
- Dated 2025–2026 goal changes: Unknown — none found this sweep.
- Sources: https://www.performyard.com/goal-management · https://support.performyard.com/article/61-creating-review-cycles

### Predictive Index (PI Perform) — no cycle; meeting-native goals
- No cycle or period concept; each goal has an individual end date, sub-goals can carry varying due dates as milestones.
- Format-flexible single object covering "the goal, OKR, or project"; measured by sub-goal completion, action items, or tracking a number/percent/dollar amount. Alignment is lightweight sub-goal nesting ("associate this goal with a larger team goal"), not a full org cascade tree.
- Strongest meeting integration in this sweep: at goal creation you set how frequently Perform automatically creates discussion topics to update the goal, pushing goal updates into 1:1/team meeting agendas; discussions and meetings can be spawned from any goal or action item.
- Release notes Sept 2025 → Aug 2026 (checked 2026-08-10) contain no goal/OKR entries — goal capability appears static this window.
- Sources: https://docs.predictiveindex.com/perform/before-meetings/goal-setting/creating-goals/ · https://docs.predictiveindex.com/en/collections/12282995-release-notes

### Officevibe (Workleap) — Goals removed from Officevibe; capability moved to Workleap Performance
- Per the official "Goals transition FAQ": Goals removed from Officevibe on 2026-01-30, replaced by goals in the Workleap Performance product — adding goal hierarchy at personal/team/organizational level, visibility controls, and integration with the full performance cycle (feedback, check-ins, reviews).
- Officevibe's legacy tool was OKR-shaped (one objective + up to five key results, per indexed help-center snippet). In Workleap Performance the time-box is the review cycle ("multiple review cycles a year") while goals are tracked year-round — no named goal-cycle unit found. Suggested goals for managers and cross-team goal reporting are marketed.
- Sources: https://help.workleap.com/en/articles/12044790-goals-transition-faq (404 on direct fetch; content via search-indexed snippet of the official article) · https://workleap.com/performance-management/

### Microsoft Viva Goals — RETIRED (out of the goal-cycles competitive set)
- Confirmed from learn.microsoft.com (doc dated 2024-12-04, last updated 2025-08-21): Viva Goals retired 2025-12-31; feature investment stopped 2024-12-05. Microsoft names **no successor product** — customers were told to export via Graph API/Excel/PowerPoint and transition "to other OKR solutions if desired."
- CI read (labeled inference): former Viva Goals customers are an active in-market buyer pool for goal/OKR tooling through 2026.
- Source: https://learn.microsoft.com/en-us/viva/goals/goals-retirement

### BambooHR — continuous goals + new cascading; review cycles carry the cadence
- No named goal cycle. Goals are continuous objects with due dates and up to 10 weighted milestones (goal % moves with milestone completion); goals can be closed while retaining status-update history. Time-boxing lives on the review side ("Flexible Review Cycles"; quarterly/semi-annual/annual cadences in marketing).
- General/SMART model (AI assistant applies SMART principles), not OKR. New "Cascading Goals": company → department → individual, up to five levels deep, public cascading vs. private individual goals, enabled under Settings > Performance > Goals.
- AI personalized goal suggestions are generated from 1:1s, assessments, job title, and feedback; goals auto-tag to company core values.
- Dated anchor: Connect 2025 press release (2025-10-08) names "performance-aligned cascading goals" among new talent tools; the product-update child pages (Cascading Goals, AI-Powered Goal Creation, Goal Milestones & Cards, Closing Goals) carry no on-page dates — exact ship dates Unknown, 2025-era per press corroboration only.
- Sources: https://www.bamboohr.com/product-updates/cascading-goals · https://www.bamboohr.com/about-bamboohr/press-release/connect-2025-showcase

---

## 5. Comparative synthesis (QW lens)

(to be completed: cycle-construct comparison, cross-package connectedness, AI-on-goals, manager enablement, recency of vendor investment)

---

## 6. Slack-ready digest

(to be completed)

---

## 7. Source Health

(to be completed — copy/pasteable block for CI-Competitor.md)

---

## 8. Coverage report

(to be completed)
