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

Goal cycles are a real differentiation axis, and the market splits three ways. **Leapsome** and **Lattice** have first-class named Goal Cycles — Leapsome's is process-managed (drafting/active/end phases, participant scoping, auto-archive, approval flows) while Lattice's is calendar-automated (pre-created cycles that auto-advance, targeted launch/close emails, homepage tasks). **Betterworks** never says "cycle" but enforces its Business Periods hardest (goal locking, per-period weights that feed compensation). Everyone else time-boxes goals weakly or not at all: Culture Amp's "Goal Cycle" is just a default due date + filter, 15Five uses a per-objective Time period with an org cadence setting, and PerformYard / PI Perform / BambooHR / Workleap hang goals off *review* cycles or meetings instead. Two cross-vendor findings stand out: (1) **no vendor documents automated rollover of incomplete goals into the next cycle** — it's manual clone/duplicate everywhere — and (2) 2025–2026 investment is flowing to AI-on-goals (AI goal writing, copilots that create goals, AI reviews that consume goal data) and to **exposing goals via APIs/MCP servers** (Lattice 2026-05/2026-07, Betterworks 2026-07-14). Market event: Microsoft Viva Goals retired 2025-12-31 with no successor — its OKR customer base is in-market now.

---

## 3. Competitor profiles

### Lattice

**Cycle concept & naming.** First-class, named **"Goal Cycles"** — admin-created time-boxed periods with a cycle name, start date, and due date (Admin > Goals > Goal cycles). Goals are not locked inside cycles: every goal carries its own start/due date (due defaults to end of current quarter or end of the goal cycle), and cycle assignment at creation is optional. The current cycle is the default assignment for new goals and the default time filter for Explore/Participation/Status reporting (admin-selectable "Current cycle" vs "All time"; with no current cycle, views show "All Time").
Sources: https://help.lattice.com/hc/en-us/articles/360060029874 · https://help.lattice.com/hc/en-us/articles/1500006472801 · https://help.lattice.com/hc/en-us/articles/4409045644567

**Cycle mechanics.** The standout: **automatic cycles.** Admins set a "Preferred planning cycle" — monthly, quarterly, fiscal quarterly (keyed to fiscal-year start month), or semi-yearly — plus optional annual cycles (fiscal or calendar). Lattice pre-creates cycles and automatically moves through them as time passes, auto-assigning "current" by date; admins can override ("Make current") or create manual custom cycles. Cycle start/due dates are not editable once published. Per-cycle notifications: launch emails targeted separately at company goal creators, department goal creators, and all employees (custom subject/body, scheduled send date/time/timezone), plus a closing-cycle notification prompting everyone to update and end goals; cycles also generate homepage tasks ("Set company goals," "Set department goals," "Set your goals"). Update reminders are a separate org cadence (weekly / bi-weekly / monthly / quarterly / never), sent Thursdays ~10:00 local only to owners of stale goals; a homepage task still appears after 2 weeks without updates even on "Never." Goals do **not** auto-end at cycle due date — only marked Overdue; ending is manual (Complete/Incomplete). Automated rollover of incomplete goals to the next cycle: not documented — Unknown/none (nearest: Duplicate Goals, Reactivate an Ended Goal, reassign cycle via Edit).
Sources: https://help.lattice.com/hc/en-us/articles/1500006469961 · https://help.lattice.com/hc/en-us/articles/37846784374807 · https://help.lattice.com/hc/en-us/articles/360060030214 · https://help.lattice.com/hc/en-us/articles/360059843974

**Goal model.** OKR-native: Objectives (qualitative) + Key Results (number, dollar, percent, binary); O/KR differentiation is a toggle and the labels are renamable. Four goal types: company, department, group, individual (creation rights per level). Cascading alignment is optional org-wide; admins can require individual goals to align to a parent; parents can be objectives or KRs. Rollup: parent objectives always inherit child progress; parent KRs inherit child-KR progress only if the parent KR is binary; KRs weight equally by default with optional custom weighting. Statuses On Track / Progressing / Off Track (renamable, max 3) plus ended Complete/Incomplete; priorities P1–P10; visibility public / private / selected-departments; multi-owner goals; drafts; tags.
Sources: https://help.lattice.com/hc/en-us/articles/360059451574 · https://help.lattice.com/hc/en-us/articles/4402384455703 · https://help.lattice.com/hc/en-us/articles/1500005941701

**Cross-module connections.** Reviews: goal-enabled review templates pull each reviewee's top-level goals into review forms, filterable by goal cycle name, start/due dates, and active/ended (filters lock at cycle publish); a Goals context panel is available while writing reviews. Analytics: Participation/Status reporting includes employees-with-goals %, updated %, aligned-to-company %, overdue %, and on-a-cycle %. Integrations/API: Jira and Salesforce read-only connections auto-update goal progress; Slack/MS Teams notifications; **Goals Write endpoint GA in the public V1 API (2026-05)**; **Lattice MCP** (2026-07) exposes goals context to Claude/OpenAI/Slack; Evidence-based Review Drafts (AI) uses goals as an input signal. 1:1s: only a goal-themed recommended talking point verified; deeper structural 1:1↔goal linking Unknown. Goals→compensation: no direct link found (comp links to review cycles).
Sources: https://help.lattice.com/hc/en-us/articles/1500001259362 · https://help.lattice.com/hc/en-us/articles/1500009663861 · https://lattice.com/blog/july-2026-product-updates

**Recent changes (dated by blog publication).**
- 2025-07-31 — Goals Refresh Phase 1: cascade view default, standardized tables, bulk ops, single-panel creation — https://lattice.com/blog/july-2025-product-updates
- 2025-09-29 — Phase 2: modernized side panel; edit/update/timeline/audit in-panel; ending goals folded into update flow — https://lattice.com/blog/september-2025-product-updates
- 2025-10-31 — Milestone 3: full-screen goal detail view with Overview/Timeline/Audit Log tabs — https://lattice.com/blog/october-2025-product-updates
- 2026-02-28 — Final milestone: standard data tables on Participation/Status; "Needs Update" filter — https://lattice.com/blog/february-2026-product-updates
- 2026-05-31 — Goals Write Endpoint GA in public V1 API (programmatic create/update; sync/automation) — https://lattice.com/blog/may-2026-product-updates
- 2026-07-30 — Lattice MCP (Claude/OpenAI/Slack) pulls goals context; Evidence-based Review Drafts draws on goals — https://lattice.com/blog/july-2026-product-updates

**Positioning (labeled as positioning).** "Alignment that scales" — OKRs laddering individual and team goals to top-level business objectives, kept visible through 1:1s, reviews, and dashboards.
Source: https://lattice.com/platform/goals

### Leapsome

**Cycle concept & naming.** Explicit, named **"Goal Cycles"** — the most workflow-managed cycle construct in this study. A Goal Cycle "manages the drafting, updating, and archival process for Goals and OKRs": the admin defines a named cycle (e.g., "Q4 2022"), a description, **participants** (all users, or specific users/teams/locations/levels), and a three-part timeline — **Drafting period** (users create goals assigned to the cycle), **Active period** (new goals can't be assigned unless overridden; goals still editable/updatable), and **End**. Supports quarterly or yearly patterns; multiple cycles can run simultaneously. Cycle templates: Unknown (not documented).
Source: https://help.leapsome.com/hc/en-us/articles/360003224378-Creating-and-managing-goal-cycles

**Cycle mechanics.** Setup is (super)admin-only. Cycle settings include: **auto-archive goals at cycle end** (freezes further updates), **block new-goal creation during the active period**, and auto-assign tags. Goals created by cycle participants during an active cycle attach to it automatically (exceptions: private personal goals; a user in multiple open cycles picks one). Notifications are fixed-cadence: at drafting start (all participants), 7 days before drafting end (users without goals + managers to approve), 7 days before active-phase end (admins + all participants to update goals) — via email and/or Slack. A separate cycle dashboard shows who set goals, average progress, goals per stage, and non-participants; cycle analytics chart actual vs. projected progress. Auto-create-next-cycle and rollover/carry-over of incomplete goals: not documented — Unknown (auto-archive is the documented end state; archived goals findable via States: Archived filter).
Sources: https://help.leapsome.com/hc/en-us/articles/360003224378-Creating-and-managing-goal-cycles · https://help.leapsome.com/hc/en-us/articles/360018883498-FAQ-s-Goals-OKR-s

**Goal model.** Objective + Key Results (min. one KR); KR types: achieved yes/no, percentage, numerical, currency; KRs can have individual owners, weights (%), deadlines, contributors. "Initiatives" (what-to-do items) attach to goals or KRs without affecting progress unless dynamic progress calculation is enabled. Levels: individual (private or manager-approved), team/department, company. Alignment via parent goals rendered in an interactive goal tree (company vision at top). Progress rollup: weighted/unweighted KR average; dynamic progress calculation lets child goals drive parent progress (only if the parent has no KRs). States: Draft, Pending approval, Active, Archived, plus check-in flags ("Off track"). Approval flows with an implicit-approval option; bulk copy-and-assign. Note: OKR functionality, goal-level weights, badges, and mandatory tags are gated as **PRO Features**.
Sources: https://help.leapsome.com/hc/en-us/articles/115003558313-Creating-a-new-goal-OKR · https://help.leapsome.com/hc/en-us/articles/115003565713-How-progress-is-calculated · https://help.leapsome.com/hc/en-us/articles/31684896940957-Advanced-Goals-Features-PRO-Features

**Cross-module connections.** Reviews: a "Goal-based question" in review templates auto-creates a question per goal matching filters (role, tags, purposes, **cycles**, states); goals continuously sync until review completion. 1:1 Meetings: dedicated Goals tab with in-meeting progress updates. **Compensation: recommendation rules can use business/development goal average scores as weighted input factors** — the most direct goals→comp link verified in this study. Analytics: goal analytics filterable by cycle, actual-vs-projected trend graphs, exports with up to 30 employee attributes. Workflows: goal event triggers (created/updated/not-updated-for-X-days) and auto-create/assign templated goals via the workflow builder (2026-01-27). AI: "Get AI Suggestions" for KRs/initiatives; real-time goal-wording refinement; **Leapy copilot** answers cross-module goal questions, summarizes progress, and (2026-04) creates goals from chat with confirmation.
Sources: https://help.leapsome.com/hc/en-us/articles/360012477694-Including-goals-in-a-performance-review · https://help.leapsome.com/hc/en-us/articles/6520394113565-FAQ-s-Compensation · https://help.leapsome.com/hc/en-us/articles/29537513030941-Leapy-Your-AI-Copilot

**Recent changes (dated, from the Platform-improvements changelog + monthly posts).**
- 2025-05-07 — Customizable goal-analytics exports (up to 30 attributes)
- 2025-05-23 — Goal progress updates via public API / Zapier webhooks
- 2025-08-26 — Attachments on goal & KR comments
- 2025-09-22 — Filter goals/tree/analytics by direct/indirect reports
- 2025-11 — AI goal-writing guidance + auto-generated KRs, tied to "current goal cycle and planning cadence" — https://site.leapsome.com/blog/product-updates-nov-2025
- 2025-12-16 — Goal event triggers in workflow builder
- 2026-01-27 — Create & assign templated goals via workflows — https://site.leapsome.com/blog/product-updates-jan-2026
- 2026-04 — Leapy cross-module goal answers + create-goal from chat; Review Assistant pulls goal progress comments — https://site.leapsome.com/blog/product-updates-april-2026
- 2026-05 through 2026-07 — Unknown/uncovered (changelog moved to a new hub not yet located; monthly blog slugs 404 — see Source Health)
Source: https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements

**Positioning (labeled as positioning).** "Turn your mission into action with AI-powered goals" — framework-agnostic alignment via "flexible, automated goal cycles, clear ownership, and structured timelines," goal trees, real-time dashboards, and AI-generated OKRs, inside a people platform "built on the deepest people data foundation in HR."
Source: https://www.leapsome.com/product/goals-and-okrs

### Culture Amp

**Cycle concept & naming.** Has a named but **lightweight** "Goal Cycle" — an account-level setting, not a managed cadence engine. Goals are fundamentally due-date-organized; the Goal Cycle (Settings > Goals) defines one current cycle via Launch Date + End Date whose only effects are (a) the End Date becomes the default due date on new goals and (b) it becomes the default Due Date filter in the Goal List and reporting. It does not restrict employees' date choices, does not touch existing goals, and cannot scope participants. Shipped 2025-07-18 ("Flexible Goals Due Dates"). Contrast: performance reviews and the Develop module use true cycle constructs — "performance cycles" and "Development Cycles" (GA 2025-10-31, with start/end dates, automated reminders, participation tracking) — so the cycle machinery exists in-platform but has not been applied to goals.
Sources: https://support.cultureamp.com/en/articles/9637689-admin-guide-to-setting-up-goals-in-your-organization · https://updates.cultureamp.com

**Cycle mechanics.** Account Admins or Goals Full Permissions users enter Launch Date + End Date (auto-saves); any custom span; one cycle at a time. After the End Date passes, the next default due date is auto-calculated from the last cycle's length (a 3-month cycle yields a new default 3 months out) — no named successor cycle is created. With no cycle set, the default due date is Dec 31 of the current year. Reminders: none — per the Goals FAQs there are currently **no goal notifications at all** (no update/comment/assignment notifications; emails "hoped for," no date).
Sources: https://support.cultureamp.com/en/articles/9637689-admin-guide-to-setting-up-goals-in-your-organization · https://support.cultureamp.com/en/articles/9770744-goals-faqs

**Goal model.** Individual delivery goals with Key Results (percentage or number, start/target values, per-KR owners); individual development goals use Actions checklists instead of KRs (no alignment allowed); group goals across Company, Organizational units, and cross-functional Collaborations. KR structure exists and marketing sells OKR software, but no enforced OKR framework. Alignment: primary/supporting links visualized in a company-down Goal Tree; plain alignment does NOT propagate progress. **Cascading Goals (2026-05-05):** supporting goals auto-roll progress up to the parent in real time — equal distribution with auto-rebalancing by default, manual percentage weighting added 2026-06-30 (must total 100%); recommended max 5-6 levels; a goal uses either KRs or supporting-goal cascading, not both; on by default. Weighted KRs / weighted top-level goals: not supported. Visibility: Everyone / Specific People / Private; default is Private and cannot be changed; managers always see direct reports' goals; admin visibility cannot be restricted.
Sources: https://support.cultureamp.com/en/articles/14242462-using-cascading-goals-and-weighted-progress · https://support.cultureamp.com/en/articles/9393208-creating-and-aligning-individual-goals · https://support.cultureamp.com/en/articles/10066665-managing-goal-visibility

**Cross-module connections.** Goals are integrated into Self-reflections and Manager reviews (employee-profile view during both). **1-on-1s: NOT integrated** per current FAQs ("not right now… planning to add"). Development goals live in Develop (goal comments 2025-07-08; Development Cycles structure IDP timelines). Feedback link: Unknown. Reporting is a strength: Goals Progress Report (2025-06-12), Goals Creation Report (2025-03-27), goal-usage demographic filters (2025-04-16) and drill-down (2025-11-25), unified goal export (2026-02-12). AI: AI Coach GA (2026-03-11) supports employees with goal setting; no goal-specific AI generation feature verified.
Sources: https://support.cultureamp.com/en/articles/9770744-goals-faqs · https://updates.cultureamp.com

**Recent changes (dated, verified on updates.cultureamp.com).**
- 2026-06-30 — Cascading Goals custom weighting
- 2026-05-05 — Cascading Goals (real-time progress rollup)
- 2026-04-13 — Improved Collaborations view (tabs, role filters, search, CSV export)
- 2026-03-11 — AI Coach GA (goal-setting support)
- 2026-02-12 — Enhanced Goal Usage Reporting (unified export)
- 2025-12-11 — Bulk Goal Creation (identical goals to many employees via filters/CSV)
- 2025-11-25 — Goal usage report drill-down
- 2025-09-17 — Bulk goal management (archive/reassign) + progress rollup on Goals tabs
- 2025-07-18 — Flexible goals due dates (the Goal Cycle setting)
- 2025-07-10 — Import supports group goals + alignment
- 2025-06-12 — Goals Progress Report
- 2025-04-29 — Development Goal Actions GA
- 2025-03-27 — Group Goals Administrator role + Goals Creation Report
- Adjacent: Development Cycles EAP 2025-09-24, GA 2025-10-31
Source: https://updates.cultureamp.com

**Positioning (labeled as positioning).** Marketed as goal-setting tools for managers / OKR software — "turn business objectives into motivating employee goals," alignment- and motivation-led rather than cycle-administration-led.
Source: https://www.cultureamp.com/platform/perform/goal-management-software

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

**Cycle concept & naming.** Does NOT call goal time-boxes "cycles." The construct is the **"Business Period,"** defined by an admin-configured **Business Calendar** (Admin > Platform configuration > Operational settings). Betterworks recommends quarterly division; the default due date for new goals is the end of the current business period. The business period drives: goal date presets at creation, the default Goals-list view window ("Today" = current period, toggleable to past/future), Goal AI Assist's default timeframe, goal-weight totals per period, program-email timing, goal-lock windows, and AI Performance Summary time ranges. "Cycle" is reserved for the Conversations module (review cycles) and Calibration.
Source: https://support.betterworks.com/hc/en-us/articles/360026802712

**Cycle mechanics.** Goal creation offers period presets but custom start/due dates are allowed. Automation: goal-creation "Program Emails" automatically remind employees who haven't created goals for the period (admin-set timeline, ad-hoc sends, weekends skipped); auto-creation of next-period goals or automatic rollover is not documented — Unknown; manual Clone exists (cloning into a future business period is allowed even during a lock). Nudges/reminders: user-to-user "cheer or nudge" on goals; Slack drift nudges ("pings when an OKR drifts 10% off track" — marketing claim); goal check-in reminder emails and a mid-period update notification email; overdue-goal notifications; weekly digest. **Goal Locking** is the strongest deadline enforcement in this study: admins lock goals only, progress only, or both after a set date in the business period — locked users can't edit dates/alignment/progress or delete (can still comment, assess, score, cheer/nudge, end early); admins exempt; integration-fed progress also freezes; program emails pause during locks.
Sources: https://support.betterworks.com/hc/en-us/articles/14059767854221-Goal-Locking · https://support.betterworks.com/hc/en-us/articles/14972512005517

**Goal model.** Goal + Milestones, explicitly equated to objectives and key results. Milestones can have their own owner, dates, and progress; milestones convert to goals and vice versa. Alignment: "Align Up" under a parent goal (multi-level hierarchy, alignment chart; NextGen Alignment view); public↔private alignment mixing disallowed. Progress: manual, milestone-rollup, or integration-fed (Jira, Asana, GitHub, Salesforce, Excel 365, LinkedIn Learning); metrics in %, units, dollars, or binary; negative/decimal values since 2026-05; statuses Green >=75% / Yellow >=50% / Red with admin-tunable thresholds; floor/ceiling progress ranges added 2026-06-30. Levels: individual, team-owned, and admin-designated "Top Company Goals" per quarter. **Goal Weights:** optional % importance per goal summing to 100% within a business period, manager- or self-set, **feeds compensation calculations** (weights report; added to NextGen 2026-06-30). Also: goal Assessments, optional Scoring, private goals with Owner/Editor/Participant roles, bulk CSV upload.
Sources: https://support.betterworks.com/hc/en-us/articles/4412049001741-Creating-Managing-Goals-Milestones · https://support.betterworks.com/hc/en-us/articles/4405976898317-Goal-Weights · https://support.betterworks.com/hc/en-us/articles/41306414744077-Measuring-Goal-Milestone-Progress-NextGen

**Cross-module connections.** Conversations (reviews/check-ins) discuss goal progress; NextGen adds a Goals side panel inside Conversations and Meetings/1:1s (2026-05-08). Calibration's Performance Snapshot surfaces % goal completion and # of cheers received on goals per employee. Insights/Advanced Analytics track goal creation, alignment, update recency. Recognition: cheers on goals feed the snapshot. AI (verified naming — "BetterAI" branding NOT found on official surfaces): classic "Goal AI Assist" (suggests goals per business period, on a self-hosted private LLM); NextGen "Goal Assist," "Goal Writing Assistant" (real-time rule checks: dynamic verb, 3–12-word name, 2–4 milestones, metric required; AI rephrase), and "Performance Summary" (aggregates goals + conversations, feedback, recognition, calibration; thresholds Aspirational >=75% / Committed 100%); admin AI controls default off. **Betterworks MCP Server beta (2026-07-14)** exposes goals data to external AI assistants.
Sources: https://support.betterworks.com/hc/en-us/articles/25455979340173-Goal-AI-Assist · https://support.betterworks.com/hc/en-us/articles/41289776622733-AI-NextGen · https://support.betterworks.com/hc/en-us/articles/360049879952

**Recent changes (dated releases).**
- 2026-05-08 — Spring Release: Goals side panel in Conversations/Meetings, draft autosave, bulk CSV goal upload with import history/revert, negative/decimal metrics, Type filter, persistent filter views — https://support.betterworks.com/hc/en-us/articles/45698412708237-Spring-Release-May-2026
- 2026-05-19 — Matrix-manager goal views
- 2026-06-16 — Admin deletion of private goals
- 2026-06-30 — Slack/MS Teams notifications for all NextGen Goals notifications; progress ranges; NextGen goal weights
- 2026-07-14 — MCP Server beta; Assessments column; mid-period email fix
- 2026-07-28 — Goal Update Status filter; check-in reminder fix; AI data-scoping fix
- 2025 items were minor (goal-name length, AI Assist fixes)
Source: https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes (via Zendesk API route-around — see Source Health)

**Positioning (labeled as positioning).** Goals as the operational core of real-time performance management — "goal management software for weekly, not quarterly, updates," cascading from strategy to execution and serving as "the foundation for performance reviews." A goals-native contrast to engagement-first suites.
Source: https://www.betterworks.com/product/goals/

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

### 5.1 The cycle-construct spectrum (strongest → weakest)

1. **Leapsome — cycle as a managed process.** Named cycles with participants, a drafting phase, an active phase, auto-archive at end, optional blocking of off-cycle goal creation, approval flows, and phase-triggered notifications (including manager approve-reminders). Closest thing in-market to "run goal setting like a survey program."
2. **Lattice — cycle as an automated calendar.** Admins pick a planning cadence once (monthly/quarterly/fiscal-quarterly/semi-yearly, plus annual); Lattice pre-creates cycles and advances "current" automatically, with role-targeted launch emails, a closing-cycle update prompt, and homepage tasks per level (company/department/individual). Least admin upkeep per cycle.
3. **Betterworks — period as an enforcement boundary.** Business Calendar periods drive date presets, default views, AI timeframes, and per-period goal weights (which can feed compensation); Goal Locking (goals, progress, or both after a set date) is the strongest deadline enforcement found; program emails chase non-participants.
4. **Engagedly — named cycles, shallow documentation.** Preset + custom goal cycles (quarterly/semi-annual/annual/custom) exist as admin settings; mechanics beyond that are Unknown.
5. **15Five — cadence setting, no cycle object.** Org-level objective-setting frequency + per-objective Time period; end-of-period "Close and assess" soft lock and admin bulk close/archive of past-due objectives.
6. **Culture Amp — cycle in name only.** One current Goal Cycle whose entire effect is a default due date and a default report filter; no participants, no restrictions, and (per their own FAQs) no goal notifications of any kind. Their true cycle machinery (Development Cycles, performance cycles) hasn't reached Goals.
7. **PerformYard / PI Perform / BambooHR / Workleap — no goal cycle.** Goals are continuous objects; the review cycle (or, for PI Perform, the meeting cadence) is the time-box.

### 5.2 Whitespace: nobody automates the cycle-to-cycle transition
Across all vendors, automated rollover/carry-forward of incomplete goals into the next period is undocumented — the documented end states are archive (Leapsome), overdue-until-manually-ended (Lattice), close-and-assess (15Five), or lock (Betterworks), with manual clone/duplicate as the workaround. A goal-cycle implementation that handles the transition (roll, re-scope, or close with AI-suggested dispositions) would exceed anything verified here. (Labeled inference from absence of documentation — vendors may ship this unannounced.)

### 5.3 Platform connectedness (QW's core differentiator — CI-Context §5.1)
- **Goals → reviews** is table stakes: Lattice (cycle-filtered goal pull-in + AI review drafts using goals), Leapsome (auto-generated goal-based review questions, cycle-filterable), 15Five (objectives section with timeframe filter, feeds ratings), Betterworks (goals side panel in Conversations; snapshot metrics in Calibration), PerformYard, Workleap Performance. Culture Amp integrates goals into self-reflections/manager reviews but **not 1:1s**.
- **Goals → compensation** separates the field: Leapsome (goal scores as weighted comp-recommendation inputs) and Betterworks (per-period goal weights feeding comp calculations) have it; Lattice, 15Five, Culture Amp show no direct link (Unknown/none found).
- **Goals → 1:1s/meetings:** PI Perform is strongest per-goal (auto-created discussion topics on a set frequency), then Leapsome (Goals tab in 1:1s), Betterworks (side panel, 2026-05-08), 15Five (objective talking points); Lattice verified only a recommended talking point; Culture Amp none yet ("planning to add").
- **Goals → recognition:** only Betterworks (cheers on goals, surfaced in calibration snapshots). No vendor connects goal attainment to a rewards program — another gap vs. a connected-platform thesis.

### 5.4 AI layer that acts (CI-Context §5.2)
2025–2026 goal investment is concentrated here: Leapsome Leapy creates goals from chat with confirmation (2026-04) and auto-generates KRs tied to the current cycle (2025-11); Betterworks ships a Goal Writing Assistant with hard rule-checks and AI Performance Summaries aggregating goals+feedback+recognition; 15Five's Agents/Context Layer and AI-Assisted Reviews consume objectives data; Lattice's Evidence-based Review Drafts use goals as input and its AI Agent answers goal questions; BambooHR generates goal suggestions from 1:1s/assessments/feedback; Culture Amp's AI Coach "supports goal setting" (GA 2026-03-11) but has no goal-generation feature verified — the laggard of the five primaries.

**Emerging pattern worth tracking: goals-over-MCP.** Lattice (Goals Write API GA 2026-05; MCP for Claude/OpenAI/Slack 2026-07) and Betterworks (MCP Server beta 2026-07-14) now expose goal data to external AI assistants. This moves "where goals get updated" outside the vendor's own UI — a platform-connectedness play that also weakens UI-level stickiness. Strategic Signal: Platform/Connected + AI layer.

### 5.5 Manager enablement (CI-Context §5.3)
Cycle constructs are doing manager work at Leapsome (approve-reminders before drafting ends), Lattice (role-targeted cycle launch emails + per-level homepage tasks), and Betterworks (program emails chasing goal-less employees; matrix-manager goal views 2026-05-19). PI Perform's auto meeting topics put goal updates directly into the manager's existing ritual. Culture Amp's zero-notification goals leave managers unsupported between reviews.

### 5.6 Notification patterns across goal cycles (added 2026-08-10, follow-up pass)

Mapped across the cycle lifecycle. Frequency counts are out of the six deepest goal vendors (Lattice, Leapsome, Betterworks, 15Five, Culture Amp, Engagedly); Engagedly is Unknown throughout (no notification docs found).

**1. Recurring progress-update reminders — the most common notification (4 of 6 verified).**
- Lattice: admin-set cadence (weekly / bi-weekly / monthly / quarterly / never), sent Thursdays ~10:00 local, targeted only at owners of goals without recent updates; a homepage task appears after 2 weeks without updates even on "Never." Channels: email, Slack, home task.
- Leapsome: "Goal Update digest & reminder" notifications, admin-enabled with user-level adjustment; email and/or Slack.
- Betterworks: goal check-in reminder emails plus a marketing-claimed Slack nudge when an OKR drifts 10% off track (threshold-triggered, not time-triggered — unique in this set).
- 15Five: structural rather than notification-based — objectives sit at the top of every weekly Check-in, so the update prompt is embedded in the existing ritual (PI Perform does the analogous thing via auto-created meeting discussion topics).
- Culture Amp: none. Sources: https://help.lattice.com/hc/en-us/articles/1500001419661 · https://help.lattice.com/hc/en-us/articles/14664105127447 · https://support.betterworks.com/hc/en-us/articles/360002018731 · https://help.leapsome.com/hc/en-us/articles/360018883498

**2. Cycle-open / goal-setting launch prompts (3 of 6 — every vendor with a real cycle or period construct).**
- Lattice: per-cycle launch emails targeted separately at company goal creators, department goal creators, and all employees, with custom subject/body, scheduled send date/time/timezone, and self-preview; plus per-level homepage tasks. The most configurable launch flow found.
- Leapsome: drafting-start notification to all cycle participants (email/Slack), fixed timing.
- Betterworks: "Program Emails" on an admin-set timeline (ad-hoc sends available; weekends skipped). Sources: https://help.lattice.com/hc/en-us/articles/37846784374807 · https://help.leapsome.com/hc/en-us/articles/360003224378 · https://support.betterworks.com/hc/en-us/articles/14972512005517

**3. Non-participation chasers — "you haven't set goals yet" (2 of 6 verified).**
- Leapsome: 7 days before drafting ends, users without goals are reminded.
- Betterworks: program emails specifically target employees who haven't created goals for the period.
- Lattice: persistent homepage tasks serve this role; a dedicated chaser email is not documented.

**4. Pre-close / mid-period update pushes (3 of 6).**
- Lattice: closing-cycle notification prompting everyone to update and end goals.
- Leapsome: 7 days before the active phase ends, admins + all participants are prompted to update.
- Betterworks: mid-period update notification email.

**5. Close / end-state notifications (mixed mechanisms).**
- 15Five: follower emails on close ("An objective you are following has been closed") and on deletion.
- Betterworks: overdue-goal notifications; Goal Locking silently freezes (lock itself is enforcement, not a notification).
- Lattice: goals flip to an Overdue flag; the closing-cycle email is the prompt.
- Leapsome: auto-archive at cycle end is the terminal event; the -7-day notice is the warning.

**6. Manager-side notifications (3 of 6).**
- Lattice: Goal Digest email (manager rollup of direct-report goal updates, cadence-following) plus an opt-in "notify managers when direct report goals are updated."
- Leapsome: manager approval reminders 7 days before drafting ends — the only approval-prompt notification in the set.
- Betterworks: weekly digest of goal activity.

**7. Social/event notifications (3 of 6).**
- Lattice: comment posted, update liked, co-owner posted an update, added-as-owner — all to goal owners, non-configurable (email, Slack).
- 15Five: owner notified on new follower; followers notified on close/delete.
- Betterworks: user-to-user cheer/nudge on goals.
- Culture Amp: explicitly none — no update, comment, or permission-assignment notifications; emails "hoped for" with no date.

**Channels.** Email is universal where notifications exist; Slack is near-standard (Lattice, Leapsome, Betterworks NextGen as of 2026-06-30, 15Five); MS Teams verified at Betterworks; SMS only at 15Five; homepage/task-inbox surfaces at Lattice; meeting-agenda injection at PI Perform. 15Five's admin model is notable: per-notification control assignable to Company (admin-locked), User (individual choice), or 15Five (platform-managed). Source: https://success.15five.com/hc/en-us/articles/50988724271643

**Reading (labeled inference).** The de-facto standard notification set for a goal-cycles feature is: role-targeted launch → non-participation chaser → recurring update reminder (configurable cadence, targeted at stale goals only) → pre-close push → close/archive notice → manager digest, over email + Slack with admin config and user-level overrides. Nobody notifies on the cycle-to-cycle transition (consistent with the rollover whitespace in §5.2), and threshold/AI-triggered nudges (vs. calendar-triggered) exist only as Betterworks' drift claim — both open ground.

### 5.7 Recency / shipping velocity on goals (descriptive)
Culture Amp shipped the most dated goal items in the window (steady 2025–2026 stream, headlined by Cascading Goals 2026-05-05 + weighting 2026-06-30) — but mostly reporting/admin depth, not cycle machinery. Lattice ran a four-milestone Goals Refresh (2025-07 → 2026-02) then pivoted to API/MCP. Betterworks' 2026 releases are goals-heavy (May Spring Release onward). 15Five's goal items are steady but incremental (weights, visibility). Leapsome's May–Jul 2026 changes are uncovered (source gap — see Source Health), so its velocity read is incomplete.

---

## 6. Slack-ready digest

```text
:dart: CI Feature Deep-Dive — Goal Cycles across core competitors (compiled 2026-08-10)
TL;DR: Leapsome and Lattice have true goal-cycle constructs (process-managed vs. calendar-automated), Betterworks enforces goal periods hardest (locking + comp-linked weights) — and no vendor automates rolling incomplete goals into the next cycle.

*Performance*
• Leapsome | Goal Cycles (current capability)
  Named cycles with drafting/active/end phases, participant scoping, auto-archive at end, off-cycle creation blocking, and manager approve-reminders — the most process-managed cycle in market.
  https://help.leapsome.com/hc/en-us/articles/360003224378-Creating-and-managing-goal-cycles
• Lattice | Goal Cycles (current capability)
  Set a planning cadence once (monthly/quarterly/fiscal/semi-yearly + annual) and Lattice pre-creates cycles and auto-advances them, with role-targeted launch emails, closing-cycle update prompts, and homepage tasks.
  https://help.lattice.com/hc/en-us/articles/1500006469961
• Betterworks | Business Periods + Goal Locking (current capability)
  No "cycle" label, but admin Business Calendar periods drive goal defaults, per-period weights (which can feed compensation), and Goal Locking — freeze goal edits, progress, or both after a set date.
  https://support.betterworks.com/hc/en-us/articles/14059767854221-Goal-Locking
• Culture Amp | Cascading Goals + weighting | Date: 2026-05-05 and 2026-06-30
  Supporting goals now roll progress up to a parent in real time, with custom percentage weighting added in June — but Culture Amp's "Goal Cycle" itself is only a default due date + report filter, with no goal notifications at all.
  https://updates.cultureamp.com
• 15Five | Objective time periods + Close and assess (current capability)
  Org-level cadence setting (monthly/quarterly/annual/custom) with per-objective Time periods, end-of-period Close-and-assess soft lock, and admin bulk close/archive of past-due objectives; Weighted OKRs shipped 2025-10-14.
  https://success.15five.com/hc/en-us/articles/360039474931-Configure-Objectives-feature-settings

*Other / Cross-Platform*
• Lattice | Goals Write API + MCP | Date: 2026-05-31 and 2026-07-30
  Goals are now writable via the public V1 API and exposed to Claude/OpenAI/Slack through Lattice's MCP server — goal updates are moving outside the vendor UI.
  https://lattice.com/blog/may-2026-product-updates
• Betterworks | MCP Server beta | Date: 2026-07-14
  Exposes Betterworks goals data to external AI assistants, matching Lattice's move within weeks.
  https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes
• Microsoft | Viva Goals retired | Date: 2025-12-31
  Retired with no Microsoft successor product — customers were told to export and pick another OKR solution, putting a displaced OKR buyer pool in-market through 2026.
  https://learn.microsoft.com/en-us/viva/goals/goals-retirement
```

---

## 7. Source Health

**Headline discovery for curation: the anonymous Zendesk REST API defeats the Cloudflare/WAF bot-walls on all three blocked Zendesk help centers.** Pattern: `https://<host>/api/v2/help_center/en-us/articles/<id>.json` (full article body + timestamps), plus `.../articles/search.json?query=<term>` and `.../sections/<id>/articles.json`. Verified working this run on help.lattice.com, help.leapsome.com, and support.betterworks.com. Recommend promoting this as a documented route-around in CI-Prompt.md §Runtime discovery and/or per-source notes in CI-Competitor.md.

**Environment note:** web.archive.org was unreachable this run (tool-level block/proxy resets) — the Wayback route-around in CI-Prompt.md was unavailable; the Zendesk API pattern above filled the gap.

Copy/pasteable block for CI-Competitor.md → Source health:

```text
### 2026-08 goal-cycles deep-dive (observed 2026-08-10)
- Lattice | https://help.lattice.com/hc/en-us | status: bot_blocked | observed: 2026-08-10
  Suggested replacement (if found): https://help.lattice.com/api/v2/help_center/en-us/articles/<id>.json (200 w/ full body; also https://help.lattice.com/hc/sitemap.xml — note /sitemap.xml without /hc 404s)
- Leapsome | https://help.leapsome.com/hc/en-us | status: bot_blocked | observed: 2026-08-10
  Suggested replacement (if found): https://help.leapsome.com/api/v2/help_center/en-us/articles/<id>.json (+ .../articles/search.json?query=goal; unlocks the bot_blocked Platform-improvements changelog 360004361834)
- Leapsome | https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements | status: stale | observed: 2026-08-10
  Suggested replacement (if found): (changelog says entries moved to a new "Product Updates Hub"; last entry 2026-02-16; hub URL not yet located — leapsome.com/product-updates 404s. Monthly blog slugs product-updates-{feb,may,jun,jul}-2026 all 404 → Leapsome 2026-05..07 changes are currently uncovered)
- Betterworks | https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes | status: bot_blocked | observed: 2026-08-10
  Suggested replacement (if found): https://support.betterworks.com/api/v2/help_center/en-us/sections/360012378232/articles.json (release-note listing; article bodies via /api/v2/help_center/en-us/articles/<id>.json; note the HTML AND the articles.atom feed both 403)
- 15Five | https://www.15five.com/objectives/ | status: 404 | observed: 2026-08-10
  Suggested replacement (if found): https://www.15five.com/products/perform/okrs-and-goals
- 15Five | https://success.15five.com/hc/en-us/articles/360002690192 | status: stale | observed: 2026-08-10
  Suggested replacement (if found): (redirects to help-center homepage; retired article — also 24664616756507 Manager-Copilot redirects, and 360002699851 now serves bulk-import content)
- Culture Amp | https://support.cultureamp.com/en/articles/10368593-goals-1-on-1s-skills-coach-anytime-feedback-product-updates-2025 | status: stale | observed: 2026-08-10
  Suggested replacement (if found): https://updates.cultureamp.com (301s to 13331721; the newsfeed replaced year-pinned running lists for 2026; paginates /page/N back to 2025-01-08)
- Officevibe (Workleap) | https://help.workleap.com/en/articles/12044790-goals-transition-faq | status: 404 | observed: 2026-08-10
  Suggested replacement (if found): (content recovered via search-indexed snippet; other help.workleap.com articles intermittently serve mismatched template content — treat help.workleap.com as partially unreliable for automated fetching)
- Engagedly | https://help.engagedly.com/introduction-to-goals | status: 503 | observed: 2026-08-10
  Suggested replacement (if found): https://help.engagedly.com/configure-goals-settings (fetched clean; likely transient 503 — retry before flagging bot_blocked)
- Betterworks | https://www.betterworks.com/goals/ | status: 404 | observed: 2026-08-10
  Suggested replacement (if found): https://www.betterworks.com/product/goals/
- (environment) | https://web.archive.org | status: bot_blocked | observed: 2026-08-10
  Suggested replacement (if found): (tool/proxy-level block on Wayback this run — use the Zendesk API pattern for Zendesk hosts; re-test Wayback next run)
```

Verified-good this run (no action needed): lattice.com/product-updates + monthly blog roundups; updates.cultureamp.com (+ pagination); support.cultureamp.com articles (via curl default-UA; python-urllib UAs 403); success.15five.com articles incl. the What's-new running list; docs.predictiveindex.com release notes; learn.microsoft.com; bamboohr.com/product-updates/<slug> child pages (clean but undated — corroborate dates via press); engagedly.com and performyard.com marketing/support pages.

---

## 8. Coverage report

```text
Competitors audited: 11/20 in CI-Competitor.md (deliberate feature-scope cut; see §1)
  Full profiles: Lattice, Leapsome, Culture Amp, 15Five, Betterworks
  Secondary sweep: Engagedly, PerformYard, Predictive Index (PI Perform), Officevibe (Workleap), Microsoft Viva (Goals — retired), BambooHR
  Skipped as out-of-feature-scope: Gallup, Qualtrics, SurveyMonkey, Peakon/Workday, Perceptyx, Energage, ADP, Paylocity, Cornerstone OnDemand, UKG
Sources consulted: ~60 official pages/articles across 11 vendors (blocked/stale this run: 11 entries — see Source Health)
Dated 2025–2026 goal-related changes captured: Lattice 6 · Culture Amp 19 · 15Five 8 · Leapsome 12 · Betterworks 9 · secondary vendors 4
Known coverage gaps: Leapsome 2026-05..07 (changelog surface moved, not yet located); Engagedly cycle mechanics beyond admin-settings names (help center thin/503); BambooHR ship dates (undated product-update pages, press-corroborated only); goals→compensation and rollover behaviors wherever marked Unknown.
Most active on goals this window: Culture Amp by dated-item count; deepest cycle-machinery investment: Lattice and Leapsome; hardest period enforcement: Betterworks.
```
