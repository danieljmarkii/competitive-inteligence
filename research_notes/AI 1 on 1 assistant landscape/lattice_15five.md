# Lattice (AI Agent in 1:1s / Lattice Meetings) and 15Five (Kona Notetaker / Meeting Assistant / Kona Coach): 1-on-1 capture and downstream data use

Research date: 2026-11-17. Current-state view. Sources are plain URLs next to each fact (no markdown links, per repo convention).

Reading notes for the report writer:
- "Confirmed (primary)" = stated on the vendor's own help center, subprocessor list, or product page. "Third-party" = pricing trackers, trade press, review sites. "Inferred" = my reasoning, kept in the Inferences blocks only.
- Pages were read through a fetch-and-summarize tool, not as raw HTML. Wording in quotes is as returned by that tool; re-check verbatim before quoting externally.
- Naming. Lattice: "Lattice AI Agent in 1:1s" (GA June 2026), extended in October 2026 into "Lattice Meetings" (1:1s plus group and one-off meetings). 15Five: "Kona Notetaker" is the bot (called "Kona Meeting Assistant" until about October 2026); "Meeting Assistant" is now a separate Agents Hub agent (prep plus notes) that uses Kona Notetaker or Google Meet as its meeting source; "Kona Coach" is the manager-coaching product. 15Five's help center still uses the old and new names side by side.

## 1. Capture mechanism

### Takeaway
Both vendors use a visible meeting bot that joins Zoom, Google Meet, or Microsoft Teams from a calendar connection; neither documents a desktop app, browser extension, or in-person/mobile recording. Lattice is invite-based with an optional admin auto-invite; 15Five is driven by adding bot@15five.com to the calendar invite, with admin-set auto-join or manager choice, and it prefers platform captions over recording.

### Cited Findings

Lattice
- A bot joins the call: Recall.ai is the feature-specific subprocessor that "joins meetings and generates recordings and transcripts." — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Supported platforms: Zoom, Google Meet, Microsoft Teams; requires a connected calendar (Google Calendar or Outlook) and a supported conferencing link. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ ; https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- In-meeting identity and notice: the agent is named "Lattice Agent in 1:1s", posts a chat message explaining what it is capturing, and participants get pre- and post-meeting notifications by Slack and email. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- The agent "announces in the meeting that it is recording and transcribing for Lattice meeting insights." — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Join rules: the agent must be explicitly invited by a participant and never joins automatically unless an admin has enabled auto-add. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Auto-invite (1:1s only): when on, the agent joins all upcoming 1:1s for employees with access and employees can remove it from any meeting; when off, employees invite it manually. The auto-invite setting is hidden if Meetings is enabled. — https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention
- Both participants need access enabled before the agent can be invited; the calendar must be connected through a recurring meeting; the 1:1 agent is not available in ad-hoc meetings. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ ; https://help.lattice.com/hc/en-us/articles/41419452623895-Invite-the-Lattice-AI-Agent-to-your-1-1s
- 1:1 FAQ limits: no group, team, or in-person meetings where only one participant joins; English only. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- October 2026 "Lattice Meetings" widens scope: 1:1s, group meetings, and one-off conversations; the AI Agent can be invited to Zoom, Meet, or Teams calls "including calls with external attendees." — https://lattice.com/blog/october-2026-product-updates
- Removal: either participant can remove the agent in Lattice; removal from the live call depends on the meeting platform's host controls. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ

15Five
- Kona Notetaker joins scheduled 1-on-1s as an attendee, added through the calendar invite via bot@15five.com; platforms are Zoom, Google Meet, Microsoft Teams. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Captions first: Kona uses meeting captions when available; if captions are off it asks in the meeting chat for permission to record. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Eligibility: only 1-on-1s between a manager and their direct report (not indirect reports); exactly two participants on the invite; a virtual meeting link is required; in-person meetings are not supported. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide ; https://success.15five.com/hc/en-us/articles/50988686382619
- Third-party notetakers that appear as calendar participants count toward the two-participant limit and can block Kona; local/passive notetakers can run alongside. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Auto-join rules: admins choose the default (auto-join all eligible 1-on-1s, or let each manager decide); where managers decide they pick which recurring 1-on-1s Kona joins. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide ; https://success.15five.com/hc/en-us/articles/50988753869851
- Timing (from search-index snippets of help articles, not fetched in full): calendar sync about hourly; Kona checks for eligible meetings about every minute; joins 1 minute before start; leaves after about 12 minutes if nobody joins. — https://success.15five.com/hc/en-us/articles/50988686382619 ; https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Ad hoc, late, or rescheduled meetings: "Send Kona to 1-on-1" button in the in-app 1-on-1 view or the Slack homepage. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- In-meeting chat commands on all three platforms: "Kona pause", "Kona start", "Kona leave". — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Second meeting source: each company uses one meeting source for Meeting Assistant, either Kona Notetaker or Google Meet; the article says Google Meet meeting notes feed AI-Assisted Reviews "when available." — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together
- Language: spoken input in multiple languages is accepted, but notes, summaries, and action items are always in English. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide

### Inferences
- Both are standard Recall.ai-style bot participants (both vendors list Recall.ai; see section 2). Neither is "botless."
- 15Five's "Google Meet" meeting source looks like ingestion of native Google Meet notes/transcripts rather than a bot, but the help article does not describe the mechanism, so treat as unconfirmed.
- 15Five's captions-first design lets it claim it does not record unless captions are unavailable; Lattice's bot announces recording and transcription outright.

### Gaps
- Bot display name for Kona in the participant list: Unknown (only the bot@15five.com address is documented).
- Lattice: one FAQ line on invite timing was returned garbled ("must be invited 10 minutes before the meeting starts" and "cannot be added before the scheduled start time"); the exact lead-time rule is Unknown.
- Lattice: whether the auto-invite option still exists in any form once Lattice Meetings is enabled (the setting is "hidden") is Unknown.
- Lattice: whether the English-only and no-group limits in the 1:1 FAQ were lifted with Lattice Meetings (group support clearly was) is not reconciled in the sources.
- Help articles disagree on whether 15Five needs a recurring meeting (one says any two-person manager/direct-report meeting, another says recurring 1-on-1s). — https://success.15five.com/hc/en-us/articles/50988686382619 ; https://success.15five.com/hc/en-us/articles/50988761575195

## 2. Underlying technology (bot, transcription, LLM)

### Takeaway
Both vendors are confirmed Recall.ai customers via their own subprocessor lists. Lattice lists OpenAI as its only model provider plus LangSmith for monitoring; 15Five lists both OpenAI and Anthropic, plus Deepgram and Pinecone. Which LLM handles 1-on-1 transcripts specifically is not stated by either vendor.

### Cited Findings

Lattice (all confirmed, primary)
- "Hyperdoc, Inc. (Recall.ai)" — "Meeting transcription bot", United States, listed under Optional Subprocessors (apply only to opted-in features). — https://lattice.com/privacy/subprocessors
- OpenAI — "AI models for AI-powered features", United States, optional subprocessor. — https://lattice.com/privacy/subprocessors
- Langsmith — monitoring and optimization for Lattice AI features, United States, optional. — https://lattice.com/privacy/subprocessors
- Merge — data integration for certain AI features (US, EU), optional. ORY Corp. — authentication for Lattice MCP customers only (US and EU by data residency). — https://lattice.com/privacy/subprocessors
- AWS is listed for hosting and data storage only (US, EU); no mention of Bedrock. Anthropic, AssemblyAI, and Deepgram are not on the list. — https://lattice.com/privacy/subprocessors
- Recall provides Lattice with transcript data and metadata (meeting title, time, participants, speaker attribution); Recall deletes transcripts "within minutes after processing." — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy

15Five (all confirmed, primary; page effective date September 23, 2026)
- "Hyperdoc Inc. (Recall.ai)" — "API for meetings management", USA. — https://www.15five.com/terms/data-processing-addendum/sub-processors
- "Deepgram, Inc." — "API for meetings management", USA. — https://www.15five.com/terms/data-processing-addendum/sub-processors
- "OpenAI OpCo, LLC" — AI-enabled functionality, USA. "Anthropic, PBC" — AI-enabled services for 15Five products and internal operations, USA. — https://www.15five.com/terms/data-processing-addendum/sub-processors
- "Pinecone Systems, Inc." — vector database for AI embeddings and semantic search, USA. AWS — cloud hosting, USA. Merge and Truto (Yin Yang Inc.) — integrations/unified API. — https://www.15five.com/terms/data-processing-addendum/sub-processors
- AssemblyAI and Nylas are not on the list. — https://www.15five.com/terms/data-processing-addendum/sub-processors
- 15Five's AI data FAQ refers to a single, unnamed "LLM sub-processor" and says data goes from the 15Five web application server to it "entirely within the United States." — https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- Third-party change tracker reports Anthropic was added to 15Five's subprocessor list around May 1, 2026 (third-party, date unverified on the primary page). — https://visualping.io/pages/15five-subprocessors-alerts-4795447

### Inferences
- Lattice: Recall.ai is both bot and transcript generator from Lattice's point of view. The speech-to-text engine inside Recall for Lattice is Unknown. OpenAI as the LLM behind 1:1 summaries and coaching insights is inferred from it being the only model vendor listed; no page ties it to this feature by name.
- 15Five: Recall.ai as the bot and Deepgram as speech-to-text is inferred from each vendor's known business; 15Five labels both only as "API for meetings management." Deepgram may be used only when captions are unavailable; not confirmed.
- 15Five: whether Kona summaries run on OpenAI or Anthropic is Unknown. The help FAQ's singular "LLM sub-processor" wording is out of step with a list that names two.
- Pinecone on 15Five's list is consistent with the Context Layer doing retrieval over platform data including 1-on-1 notes; inferred.

### Gaps
- No Recall.ai, Deepgram, or AssemblyAI customer-story page for Lattice or 15Five was found; none searched exhaustively.
- No engineering blog or job-posting evidence was reviewed.
- Lattice subprocessor page shows no last-updated date.
- Lattice has a page titled "Important Update to Lattice's AI Features" that was not fetched and may name models. — https://lattice.com/trust/ai-update

## 3. Downstream data use

### Takeaway
Both vendors now route 1-on-1 capture into AI-drafted performance reviews, and both stop short of exposing transcript-derived content to HR in documented form. Lattice's shipped chain is summary, action items, next-agenda, two-sided coaching insights, 1:1 brief, Evidence-based Review Drafts, and MCP meeting context. 15Five's is notes and actions into the 1-on-1 agenda, then the Context Layer, which feeds Focus Briefs, AI-Assisted Reviews, and Kona Coach.

### Cited Findings

Lattice
- Shipped (GA June 2026): topic-based meeting summary, action items with owners, suggested agenda for next 1:1 (carrying forward unresolved items and recurring themes), coaching insights for both participants, optional transcript; all embedded on the Lattice 1:1 page. — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- Coaching insights go to both manager and employee and draw on the conversation ("how each person listened, what was missed, and which dynamics could be strengthened"); in Lattice Meetings, Coaching Insights are 1:1s only. — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s ; https://lattice.com/blog/october-2026-product-updates
- Performance review drafting, shipped: "Evidence-based Review Drafts", an Agent feature in Reviews, surfaces insights from 1:1 meetings; included at no additional cost for Lattice Performance customers. October 2026 post says captured conversations feed these drafts so reviews cover the full period. — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s ; https://lattice.com/blog/october-2026-product-updates
- Manager 1:1 brief, shipped: managers can generate a 1:1 brief on the homepage from recent recaps and action items. — https://lattice.com/blog/june-2026-product-updates
- MCP, shipped (status label not given): via Lattice MCP in Claude or ChatGPT users can "bring meeting context" into those tools, limited to existing Lattice permissions; other MCP tools create and update goals and save manager review summaries. — https://lattice.com/blog/october-2026-product-updates
- Marketing claim: 1:1 data "can support review writing, calibration, growth conversations, and performance decisions"; the Agent is framed as a "people intelligence layer" with HR leaders as an audience. No specific calibration or growth-plan integration is documented. — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- Lattice states captured context is stored alongside goals, feedback, and reviews so managers can use it later. — https://lattice.com/blog/june-2026-product-updates
- No secondary use: "no secondary use of customer data, such as benchmarking across customers." — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Agent analytics charts (plain-language data questions answered from the Analytics engine) shipped in June 2026, but nothing links them to meeting data. — https://lattice.com/blog/june-2026-product-updates

15Five
- Shipped: Kona Notetaker writes notes and action items into the 15Five 1-on-1 agenda and sends post-meeting summaries by email, Slack, or Microsoft Teams; positioned as a "continuous performance record" to support review writing. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Shipped: meeting data enters the Context Layer and is available to Focus Briefs and AI-Assisted Reviews. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together
- Meeting Assistant (Agents Hub agent): before a 1-on-1 sends the manager prep on open items and work changes; after, writes notes and suggested actions into the 1-on-1. Admins could move to Meeting Assistant from October 12, 2026. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together ; https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Performance review drafting: AI-Assisted Reviews draw on the Context Layer for the cycle's performance period, gather evidence as "Moments", and draft eligible open-text answers; when a manager asks for a draft, objectives and 1-on-1 data are included. A help-center release note labels AI-Assisted Reviews as Beta ("Post NEXT Product Release Overview: Agents, Context, and Beta AI-Assisted Reviews"); current status not re-verified. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together ; https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor ; https://success.15five.com/hc/en-us/articles/51287027195035-Post-NEXT-Product-Release-Overview-Agents-Context-and-Beta-AI-Assisted-Reviews
- Private 1-on-1 notes do not become newly visible through AI-Assisted Reviews (search-index snippet of a help article). — https://success.15five.com/hc/en-us/articles/50988711705755
- Manager coaching, shipped: Kona Coach analyzes meeting data alongside engagement scores, feedback trends, and manager effectiveness metrics to give managers coaching tips; after each check-in, review, or 1:1 it identifies what to celebrate, where to focus, and suggested actions; nudges delivered in Slack. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together ; https://www.15five.com/products/kona
- Marketing claim: Kona "tracks behavior reports over time" and is pre-trained on 15Five's "18 Manager Behaviors", managerial best practices, coaching research, and Transform content. Scoring method is not explained. — https://www.15five.com/products/kona ; https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- HR-facing AI: "Amaya" answers HR Admins' natural-language questions using platform data "such as engagement, reviews, Check-ins, 1-on-1s, turnover, and employee attributes"; AI-Powered Recommendations generate actions in the HR Outcomes Dashboard. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together
- Guardrail: "permission-mirroring" (AI never shows data to a user who lacks structural access to the source); 15Five says it does not use AI to build psychological profiles or personality assessments of individuals. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together ; https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- MCP: the Kona product page promotes a "15Five MCP" scoped to each user's permissions, and trade press reports 15Five launched "AI-Assisted Reviews, MCP and Meeting Assistant." A search found no 15Five help-center documentation for a native MCP server; third-party Truto guides exist. — https://www.15five.com/products/kona ; https://techintelpro.com/AI/Agentic-AI/15five-launches-ai-assisted-reviews-mcp-and-meeting-assistant ; https://truto.one/blog/connect-15five-to-claude-sync-okrs-key-results-and-priorities/

Checklist summary (S = shipped per primary source, C = marketing claim only, U = Unknown / not documented)
- Summaries and action items: Lattice S; 15Five S.
- Next-meeting agenda / prep: Lattice S (suggested agenda, 1:1 brief); 15Five S (Meeting Assistant prep, Focus Briefs).
- Review drafting from 1:1 data: Lattice S (Evidence-based Review Drafts); 15Five S, labelled Beta at launch (AI-Assisted Reviews).
- Manager coaching from the conversation: Lattice S (both participants); 15Five S (Kona Coach, managers only, paid).
- Manager-effectiveness scoring from transcripts: Lattice U; 15Five C ("tracks behavior reports over time"; coaching uses "manager effectiveness metrics", source of those metrics not specified).
- Talk-time or sentiment analytics: Lattice U; 15Five U.
- Feedback suggestions, recognition suggestions, goal/OKR auto-updates from transcripts: Lattice U (MCP goal tools are not transcript-driven); 15Five U.
- Growth/development plans: Lattice C ("growth conversations"); 15Five U.
- Calibration / talent review input: Lattice C; 15Five U.
- HR/admin dashboards built on meeting content: Lattice U (admins blocked from transcripts and insights); 15Five partial (Amaya lists "1-on-1s" among data it can query; whether that includes Kona-captured notes is not specified).
- AI chat/agent context: Lattice S (Agent, 1:1 brief); 15Five S (Context Layer).
- MCP exposure of meeting context: Lattice S; 15Five C.

### Inferences
- Both vendors treat the review draft as the main monetizable downstream use of 1-on-1 capture; neither documents attrition/risk/sentiment scoring from 1-on-1 conversations for HR.
- Lattice's coaching goes to both people in the meeting; 15Five's deeper coaching is a manager-only paid product. This is a real design difference for QW to weigh.
- 15Five's architecture (Context Layer plus vector database) is positioned to let meeting-derived notes reach HR-facing tools such as Amaya, subject to permission-mirroring; the practical boundary for private 1-on-1 notes is not spelled out.

### Gaps
- No evidence either way on talk-time ratios, sentiment scoring, recognition suggestions, or automatic goal updates for either vendor.
- Lattice: whether Workforce Intelligence (announced; https://lattice.com/blog/lattice-launches-workforce-intelligence-for-ai-era-connecting-people-strategy-to-business-outcomes) consumes meeting-derived data was not checked.
- 15Five: current GA/beta status of AI-Assisted Reviews and of the MCP is Unknown.
- Public API exposure of meeting notes/transcripts: Unknown for both.

## 4. Visibility: who can see transcripts, summaries, and derived insights

### Takeaway
Both vendors restrict meeting content to the two participants and explicitly exclude HR admins. Lattice lets participants download and delete transcripts (when storage is on); 15Five says nobody, including participants, can access transcripts at all.

### Cited Findings

Lattice
- Only meeting participants can access transcripts and insights; admins, HRBPs, and other non-participants cannot view or download them in the platform; custom role owners have no transcript access; admin impersonation does not grant access unless the admin was a participant. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Summary, action items, suggested agenda items, and coaching insights are available to both participants regardless of who invited the agent. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- Participants can download the transcript as a TXT file when transcript storage is enabled. — https://help.lattice.com/en-us/articles/15694164-download-a-lattice-ai-agent-transcript-from-your-1-1
- Users can edit AI-generated action items and agenda items. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- A custom-role permissions article for the agent exists (not fetched). — https://help.lattice.com/en-us/articles/16541145-configure-custom-role-lattice-ai-agent-in-1-1s-permissions

15Five
- Notes and summaries are visible only to the manager and direct report who were in the meeting. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Transcripts are not accessible to HR, admins, managers, or employees ("No one"); "Transcripts are never accessible to anyone." — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide ; https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- Leak path: if a participant adds a suggested action to the 1-on-1's action items, anyone who can see that 1-on-1's action items can see it (for example a global viewer with 1-on-1 access). — https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- If a third participant joins after Kona entered, notes captured before that remain private to the original two (search-index snippet). — https://success.15five.com/hc/en-us/articles/50988686382619
- All participants can receive a copy of the meeting notes. — https://www.15five.com/products/kona

### Inferences
- "HR cannot read your 1:1" is now table stakes for this category; a QW design that gave HR transcript access would be out of line with both competitors.
- Both products still let content become visible indirectly: Lattice through review drafts the manager writes, 15Five through shared action items and existing 1-on-1 visibility roles.

### Gaps
- Skip-level manager visibility: not addressed by either vendor's pages.
- Lattice: visibility rules for group meetings and meetings with external attendees under Lattice Meetings were not found.
- 15Five: whether existing 1-on-1 visibility roles (for example global viewers) can see Kona-written notes once they sit in the 1-on-1 agenda is not stated clearly.

## 5. Governance and table stakes

### Takeaway
Shared baseline: in-meeting announcement, participant-level removal or pause, no audio/video retained by the vendor, no model training on customer data, participant-only visibility. They differ on transcript handling: Lattice stores none by default and lets admins opt in with a configurable period; 15Five keeps encrypted transcripts for a fixed 30 days that no one can view.

### Cited Findings

Lattice
- Consent and notice: explicit invite by a participant (or admin-enabled auto-add); in-meeting recording/transcription announcement and chat message; pre- and post-meeting Slack and email notifications. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy ; https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- Opt-out: either participant can remove the agent from the 1:1 in Lattice at any time. — https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- Admin scoping: Lattice AI must be globally enabled; the agent can be enabled for all employees, specific employees (by fields, user groups, or individuals), or disabled. Since October 2026 one AI settings page with a global AI switch, and admins choose whether new AI features turn on automatically. — https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention ; https://lattice.com/blog/october-2026-product-updates
- Audio/video: "Lattice does not collect audio/video data from the meeting." — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Retention: transcripts are not retained by default; admins toggle on "Store transcripts" and choose a period. Sources conflict on the period: one statement says one-month increments up to 12 months; another says that once storage is on the default is contract length plus 180 days. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy ; https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention
- Deletion: participants can delete transcripts; deleting removes it only from that person's view, and it is permanently deleted only when both delete. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy ; https://help.lattice.com/hc/en-us/articles/40791546070039-Delete-a-Lattice-AI-Agent-Transcript-from-your-1-1
- Encryption: server-side encryption at rest and encryption in transit; Recall deletes its copy within minutes after processing. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Model training: customer data is not used to train Lattice's AI models. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Data residency: meeting data is stored in Lattice's existing cloud infrastructure consistent with the customer's residency configuration; AWS hosting in US and EU. Recall.ai, OpenAI, and LangSmith are all listed as United States. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy ; https://lattice.com/privacy/subprocessors
- Contractual status: meeting data and insights are Customer Data under the Lattice DPA. — https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Lattice's own content acknowledges that recording and transcribing conversations at scale raises legal and ethical concerns. — https://lattice.com/articles/how-to-use-ai-in-meetings

15Five
- Consent and notice: bot is a visible attendee; when captions are off it asks in chat for permission to record. No other participant notice is described. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Opt-out: any participant can pause, restart, or dismiss with chat commands; admins set auto-join or manager-decides; managers choose which recurring 1-on-1s. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide ; https://www.15five.com/products/kona
- Audio/video: Kona never stores recordings or audio/video, only transcripts. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Retention: transcripts are encrypted, stored for 30 days for quality assurance, then deleted. No configurability is documented. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Meeting notes are encrypted at rest and in transit. — https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- Model training and vendor retention: the AI sub-processor's agreement prohibits training on customer data and the sub-processor does not retain submitted data after responding. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together ; https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- Ingestion filters: private calendar events are filtered out before ingestion; files attached to 1-on-1s or Check-ins are not read by AI. — https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together
- Data residency: LLM traffic "entirely within the United States"; every listed subprocessor relevant to meetings and AI is USA; data stored in ISO 27001 compliant data centers in the United States (this describes hosting, not a 15Five ISO certificate). — https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor ; https://www.15five.com/terms/data-processing-addendum/sub-processors ; https://www.15five.com/security
- Certifications: trust center lists SOC 2 Type II and SOC 3 (2025) reports; product page shows AICPA SOC, PIPEDA, and GDPR badges. — https://trust.15five.com/ ; https://www.15five.com/products/kona
- Issue reporting: a "Report a Kona issue" flow exists inside 1-on-1s. — https://success.15five.com/hc/en-us/articles/49091197420315-Report-a-Kona-issue

### Inferences
- 15Five holds a 30-day transcript "for quality assurance" that no customer user can see; that implies vendor-side access for QA, which a privacy-minded buyer may question. Not stated explicitly by 15Five.
- Lattice's "stored only if admin opts in, participant-deletable, admin-invisible" model is the more configurable of the two; 15Five's is simpler but fixed.
- Neither offers an EU-only processing path for the meeting feature on the evidence found (US-located Recall.ai and LLM vendors).

### Gaps
- EU AI Act posture: no statement found for either vendor.
- Audit logs covering agent/notetaker activity: Unknown for both.
- PII redaction or transcript editing: Unknown for both (Lattice allows editing of action and agenda items only; 15Five transcripts are not viewable).
- Lattice certifications (SOC 2, ISO 27001) were not checked in this pass; Lattice points to a SafeBase security portal. — https://lattice.com/trust/schrems-ii
- Lattice retention conflict (up to 12 months versus contract plus 180 days) is unresolved; the two statements may describe selectable options versus the pre-selected default.
- 15Five's de-identification of data before LLM submission: one search snippet says "defined, de-identified data set", but the fetched FAQ did not confirm; treat as unverified. — https://success.15five.com/hc/en-us/articles/19976830547099
- Whether 15Five's own ISO 27001 certification exists: not confirmed.

## 6. Packaging and pricing

### Takeaway
Lattice gives the capture layer away: Agent in 1:1s and Lattice Meetings are included for all customers, with Evidence-based Review Drafts included for Performance customers. 15Five charges for the bot: Kona Notetaker is a paid add-on on Perform and Total Platform (third-party trackers put it at 2 USD per employee per month), while the Meeting Assistant agent was bundled into Perform in October 2026 and Kona Coach is a separate per-manager add-on.

### Cited Findings

Lattice
- Lattice AI Agent in 1:1s is generally available and "included for all Lattice customers at no additional cost." — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s ; https://lattice.com/blog/june-2026-product-updates
- Lattice Meetings (October 2026) is "included at no additional cost for all Lattice customers." — https://lattice.com/blog/october-2026-product-updates
- Evidence-based Review Drafts are included at no additional cost for Lattice Performance customers. — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s

15Five
- Kona Notetaker requires the Kona add-on, available on Perform and Total Platform packages; roles are Account Admins and Managers. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Third-party tracker (observed October 8, 2026): Meeting Assistant is now included in Perform and Total Platform; the paid add-on formerly called Kona Meeting Assistant is now Kona Notetaker; 15Five's help center states "Meeting Assistant is not an add-on"; Kona Notetaker is billed per employee per month on annual billing (company-wide). — https://www.usagepricing.com/blueprint/activity/15five-2026-10-08-meeting-assistant-bundled
- Third-party figures: Kona Notetaker (formerly Kona Meeting Assistant) 2 USD per employee per month; Kona Coach 19 USD per manager per month; Engage 4, Perform 11, Total Platform 16 USD per user per month billed annually. Listings disagree on Perform (8, 10, or 11). — https://www.usagepricing.com/blueprint/activity/15five-2026-10-08-meeting-assistant-bundled ; https://checkthat.ai/brands/15five/pricing ; https://www.softwareadvice.com/hr/15five-profile/
- Third-party history: 15Five acquired Kona in January 2025; Kona priced at 29 USD per manager in June 2025; later moved to an employee-wide seat (tracker gives both November 10, 2025 and December 2025); Agents and Context Layer shipped inside Perform in June 2026. — https://www.usagepricing.com/blueprint/activity/15five-2026-10-08-meeting-assistant-bundled
- 15Five's Context Layer terms reserve the "right to introduce fees for these features at renewal" (as quoted by the tracker; primary terms page not fetched). — https://www.15five.com/15five-context-layer-additional-terms-of-service
- Primary pages for verification (not fetched): https://www.15five.com/pricing ; https://success.15five.com/hc/en-us/articles/50989042213403-What-add-ons-are-available-for-15Five-plans

### Inferences
- With Meeting Assistant bundled and a Google Meet meeting source available, 15Five customers on Google Workspace may get AI 1-on-1 notes without buying the Kona Notetaker bot; the bot add-on then mainly serves Zoom and Teams shops. Plausible but not stated by 15Five.
- Lattice pricing the capture layer at zero sets a hard reference point for any QW add-on price.

### Gaps
- 15Five prices are from third-party trackers only; the 15five.com pricing page was not read directly.
- Lattice plan prerequisites (which base module a customer needs for 1:1s/Meetings) and any usage caps: Unknown.
- Kona Coach's current price (19 versus the earlier 29 USD per manager): unverified on a primary source.

## 7. Customer sentiment

### Takeaway
There is almost no independent, feature-specific sentiment for either product yet. What exists is vendor-selected customer quotes and general platform reviews; no Reddit, Gartner Peer Insights, or LinkedIn commentary on these specific features surfaced in search.

### Cited Findings

Lattice
- Vendor-selected quotes (no metrics): Loftware's Director of Global People Operations says employees "walk away feeling more heard"; Teamwork's People Business Partner says the Agent keeps employee and manager summaries aligned; TurnCommerce People Ops says coaching insights give managers support "right when they need it." — https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- G2 (general Lattice AI, not notetaker-specific, via search snippets): one reviewer calls the AI functionality "a real game changer" for performance reviews; another praises the "Lattice AI bot." — https://www.g2.com/products/lattice-lattice/reviews
- Pre-existing 1:1 friction reported by reviewers: 1:1 calendar sync with Outlook described as glitchy; 1:1s do not adjust automatically when rescheduled. — https://www.tryorbye.com/products/lattice ; https://www.softwareadvice.com/hr/lattice-profile/reviews/

15Five
- Vendor claims only: Kona is "the only meeting assistant designed to preserve psychologically safe 1:1s" and "proven to improve performance, engagement, and retention"; no supporting data on the page. — https://www.15five.com/products/kona
- 15Five's own blog acknowledges leaders and employees asking how to ensure everyone consents to being recorded. — https://www.15five.com/blog/ai-meeting-assistant
- Operational friction documented by 15Five itself: Kona can be blocked by other calendar-visible notetakers, depends on the bot address being on the invite, and has a dedicated issue-reporting flow. — https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide ; https://success.15five.com/hc/en-us/articles/49091197420315-Report-a-Kona-issue

### Inferences
- Both features are young in their current form (Lattice GA June 2026; 15Five repackaged October 2026), which likely explains the thin review record.
- Calendar-sync reliability is a known weak spot for Lattice 1:1s and matters more once a bot depends on calendar events.

### Gaps
- No Reddit, Gartner Peer Insights, or LinkedIn commentary on Lattice Agent in 1:1s or Kona was found in two search passes. G2 review pages were not fetched directly (snippets only).
- No adoption figures (share of 1:1s recorded, opt-out rates) are published by either vendor.
- No independent evidence of employee privacy pushback against either product specifically.
