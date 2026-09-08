# Competitor Research: 1:1 Quality Assessment

> **Date:** 2026-09-08 · **Author:** CI Team · **Scope:** Targeted research across QW competitor set

## Executive Summary

Most competitors treat 1:1s as an adoption/hygiene problem ("did it happen?") rather than a quality problem ("was it good?"). Only **two vendors** ship an explicit quality score for 1:1 meetings: **15Five** and **Leapsome**. A handful of others provide indirect quality proxies through composite manager scorecards or participant satisfaction ratings. The majority stop at structural metrics (completion rates, frequency, participation).

This represents a genuine whitespace opportunity. The gap between "managers are having 1:1s" and "those 1:1s are effective" is wide, and only a small corner of the market is attempting to bridge it.

---

## Tier 1: Explicit Quality Scoring

### 15Five (Kona AI) — the most aggressive approach

15Five's AI coach "Kona" joins recurring 1:1 meetings via calendar sync and produces a **Quality Score as a letter grade** (e.g., C+, B-) reflecting how well a manager demonstrated specific leadership behaviors during the conversation. This is based on Kona's qualitative analysis of the actual meeting content.

**How it works:**
- Kona monitors manager behaviors grouped into "AI Coaching Focus Areas"
- Each behavior is scored on three dimensions: **frequency** (how often it appears), **trend** (direction over time), and **quality** (the letter grade)
- Scores roll up into the **AI Coach Insights Report** on the HR Outcomes Dashboard
- The coaching data feeds into the **Manager Effectiveness Indicator (MEI)**, a composite score combining engagement survey results, turnover rates, 1:1 frequency, and upward feedback

**Where it lives:** HR Outcomes Dashboard (Perform or Total Platform tiers only)

**Limitations:** Requires sufficient coaching sessions before data populates. Gated behind higher pricing tiers. Quality grades assess manager behavior specifically, not the overall meeting experience from both sides.

**Strategic signal for QW:** This is the most direct competitor move in this space. 15Five is essentially saying "we can tell you whether your managers are any good at 1:1s" and backing it with AI analysis of real conversations. The MEI composite that rolls 1:1 quality into engagement and turnover data is the kind of cross-package connection QW's thesis values.

---

### Leapsome — named quality metric with trend tracking

Leapsome tracks a **"Meeting Quality" score** surfaced after each 1:1. All participants see a summary covering engagement, meeting quality, preparation, open questions, and clarity of outcomes.

**How it works:**
- A dedicated **"Meeting Quality Trend Over Time"** chart plots the score across a timeline
- Their **AI Meeting Notetaker** joins live calls, transcribes, generates summaries with key decisions and follow-ups, and auto-assigns action items
- Additional metrics: completion rate, meeting count (1:1 vs. team), action item creation/completion, participant satisfaction ratio
- Instant Feedback sentiment can surface as 1:1 talking points, connecting real-time feedback to the next meeting agenda

**Where it lives:** Analytics > Meetings, filterable by timeframe, team, or individual user

**Strategic signal for QW:** Leapsome's approach is more end-to-end than 15Five's because the AI notetaker captures the raw conversation and the quality score is surfaced to both participants (not just HR). The trend chart gives managers a self-improvement loop. However, it is less clear whether the quality score feeds into any broader manager effectiveness or engagement composite.

---

## Tier 2: Composite Manager Scorecards (Indirect Quality Signal)

### Predictive Index (PI Perform) — behavioral data angle

PI Perform's **Accountability Scorecard** rates managers across three pillars: regular check-ins, coaching, and development. It is not a per-meeting quality score but a composite indicator of whether the manager is consistently doing the right management behaviors over time.

**Unique differentiator:** PI integrates behavioral assessment data from the PI Behavioral Assessment to personalize management tips (e.g., how to coach a high-dominance vs. high-patience employee). The Manager Analytics Dashboard tracks 1:1 consistency, constructive feedback frequency, recognition frequency, goal-setting coverage, and action-item completion trends.

**Strategic signal for QW:** The behavioral data overlay is interesting. PI is saying "we know your employee's personality profile, so we can tell you how to adjust your 1:1 approach." This is a different axis than quality scoring, more about personalization.

### Engagedly — participant satisfaction as a quality proxy

Engagedly tracks a **"Participant Satisfaction"** rating on meetings, which functions as a per-meeting quality indicator. The Team Meeting Dashboard shows discussion-point alignment with organizational goals, satisfaction levels, action-item follow-through, and time-in-meetings trends.

Their AI assistant **Marissa** generates performance summaries, suggests talking points for difficult conversations, identifies at-risk employees, and automates meeting summaries. The AI is broader in scope (performance coaching, attrition prediction) rather than tightly focused on meeting quality measurement.

---

## Tier 3: Structural/Adoption Metrics Only

These vendors track whether 1:1s happen and whether participants engage with the tool, but do not assess quality.

### Lattice
- Binary **participation** tracking (meeting has a new talking point, shared note, item checked off, comment, or action item created = "participated")
- **Participation rate** per manager-employee pair
- Meeting frequency, next scheduled date
- **AI Agent** (free, mid-2026) generates summaries, extracts action items, suggests next agendas, and surfaces coaching insights, but these are qualitative nudges, not scores

### Betterworks
- Conversation completion rates, counts, type breakdown (anytime vs. scheduled)
- **AI 1:1 Summary** with themes, commitments, blockers
- **Blind-spot detection** flags topics managers may be missing
- AI-driven reminders nudge managers to hold 1:1s
- No quality rating or effectiveness index

### Culture Amp
- **1-on-1 Conversations Usage Report** (admin only): org-wide adoption %, department-level breakdown, 7/30 day windows
- **AI Coach** for pre-meeting role-play and suggested talk tracks (prep tool, not evaluator)
- **Assigned Topics** let admins push discussion prompts into 1:1s by demographic segment, but no analytics on whether topics were actually completed
- No post-meeting quality analytics

### PerformYard
- Structural completeness as proxy: agendas populated, action items created/completed, notes captured
- **AI summarization** of 1:1 notes at individual/team/org level
- **Meetings Coach** for pre-meeting prep and post-meeting analysis
- Goal Quality Coach checks goal quality but not meeting quality

---

## Tier 4: No 1:1-Specific Quality Assessment

### Microsoft Viva (Insights + Glint + Copilot)
- **Meeting Effectiveness Survey explicitly excludes 1:1s** (fires only on 5+ participant meetings)
- Manager dashboard shows 1:1 frequency/consistency and zero-1:1 flags
- Copilot generates per-meeting recaps (summary, decisions, action items) but does not score them
- Upcoming Glint + Insights integration (GA targeted Oct 2026) will overlay behavioral metrics on survey data, but nothing 1:1-quality-specific has been announced

### Qualtrics
- No native 1:1 quality feature; everything is survey-driven
- Meeting Feedback Survey template exists, measuring preparation, psychological safety, development focus, trust
- **Qualtrics Assist** generates manager coaching recommendations from engagement data, but not tied to individual meetings
- Can measure perceived 1:1 quality via custom surveys if an org chooses to build one

---

## Approaches Summary

| Approach | Who does it | What it actually measures |
|---|---|---|
| AI-graded quality score (per meeting) | 15Five (Kona) | Manager behavior quality via letter grade |
| Named quality metric + trend | Leapsome | Meeting quality score with timeline chart |
| Composite manager scorecard | Predictive Index | Check-in consistency + coaching + development |
| Participant satisfaction rating | Engagedly | Per-meeting satisfaction from attendees |
| AI summaries + coaching nudges | Lattice, Betterworks, PerformYard | Content extraction, not evaluation |
| Adoption/completion tracking | Culture Amp, Lattice, Betterworks | "Did the 1:1 happen?" |
| Survey-driven perception | Qualtrics | Custom survey items about 1:1 experience |
| Behavioral/structural signals | Microsoft Viva | Frequency, consistency, multitasking |

---

## Implications for QW

**The opportunity is real.** Only 15Five and Leapsome are actively trying to answer "was this 1:1 good?" Everyone else is still answering "did this 1:1 happen?"

**Three design questions worth considering:**

1. **Input signal: what data feeds the quality assessment?**
   - 15Five uses AI analysis of live meeting content (requires calendar/meeting integration)
   - Leapsome uses an AI notetaker that joins calls plus structured in-app data
   - PI Perform uses behavioral assessment profiles (personality data, not meeting content)
   - Qualtrics uses perception surveys (self-reported)
   - Each carries different privacy, integration, and accuracy tradeoffs

2. **Output audience: who sees the quality signal?**
   - 15Five shows quality grades to HR on the Outcomes Dashboard (top-down visibility)
   - Leapsome shows quality to both participants (self-improvement loop)
   - Choosing one over the other (or both) sends a strong message about whether the feature is for manager coaching or organizational oversight

3. **Connection to the broader platform: does quality data flow anywhere?**
   - 15Five's MEI composite rolls 1:1 quality into engagement + turnover data — the strongest cross-package connection in the market
   - Leapsome keeps it within the meetings module
   - QW's thesis about connected packages suggests the 15Five approach (quality signals feeding engagement and performance views) would be the higher-value play, though it is also the harder build

**What "quality" could mean without recording meetings:**
QW does not need to follow 15Five's "AI joins the call" model. Quality signals can be constructed from in-platform data: talking point coverage and completion, action item follow-through rates, goal-progress discussions, whether feedback was exchanged, cadence consistency, and even post-meeting sentiment (a lightweight "how was this 1:1?" pulse). Combining several structural signals into a composite quality indicator is a viable path that avoids the privacy and integration complexity of live meeting analysis.
