# CI Research — AI 1-on-1 Assistant Landscape

> **type:** ad-hoc competitive research (not a monthly /ci-report run) · **run date:** 2026-11-17 (America/Chicago)
> **QW package impacted:** Performance (1-on-1s), with links to Development and Recognition & Rewards
> **competitor set:** deliberately broader than CI-Competitor.md at the product lead's request

---

## 1. Bottom line up front

- **Capture is no longer scarce.** At least eight HR or performance platforms now have a documented way to get 1-on-1 conversation content into the product: Lattice, 15Five, Leapsome, Betterworks, PerformYard, Deel Engage, Engagedly, and Predictive Index (beta, product retiring 2027-09-30). Zoom, Microsoft Teams, Google Meet, Notion, ChatGPT, and Claude all bundle note taking, and most bot-first notetakers have added a botless desktop recorder. Summaries and action items are commodity.
- **The HR-platform field has split into two capture models.** Lattice and 15Five run a visible meeting bot, and both list Recall.ai as a subprocessor. Leapsome, Betterworks, PerformYard, Deel, and the specialist Windmill avoid a bot: they capture device audio or ingest the transcript Zoom, Teams, or Meet already produced. Among HR suites the botless or ingest route is now the majority pattern.
- **The furthest documented downstream use is the performance review draft.** Lattice (Evidence-based Review Drafts), 15Five (AI-Assisted Reviews, labelled Beta at launch), and Leapsome (review pre-draft, vendor claim) all route 1-on-1 content into reviews. Manager coaching from the conversation is shipped at Lattice (both participants), 15Five (Kona Coach, manager only, paid), and PerformYard (talk-time, monologue, and missed-commitment analysis).
- **No vendor publicly documents an HR or admin dashboard of sentiment, burnout, or flight risk derived from 1-on-1 conversation content.** Lattice and 15Five explicitly lock HR out of transcripts. The nearest exceptions are PerformYard's claim to summarize 1-on-1s "for individuals, teams, or the entire organization", 15Five's HR assistant Amaya listing "1-on-1s" among its data, and Recall.ai's description of Rippling. This conclusion rests on absence of public documentation, which is not proof the feature does not exist.
- **Recognition suggestions, development-plan suggestions, and skills inference from 1-on-1 transcripts were not found at any vendor.** QW's "suggested in-platform actions" and its development and talent vision have no documented direct equivalent. Betterworks' goal-update suggestions are the closest shipped analogue.
- **QW's draft answer to surveillance objections is partly behind and partly ahead.** Configurable transcript retention matches Lattice and is table stakes. An audit log is common in enterprise notetakers but undocumented among HR-platform peers. Dual consent and transcript review and redaction could differentiate if built as true two-sided controls. The draft omits three things peers already lead with: no audio or video storage, HR and admin lock-out from 1-on-1 content, and a no-training commitment.
- **Law is pushing the bar from notice to affirmative, logged consent.** On 2026-08-13 a federal court let core wiretap and biometric claims against Otter proceed and declined to treat a visible notetaker as consent. Granola is being sued over its botless design. Neither a bot nor an invisible recorder is a safe harbor. No court has found any vendor liable.
- **The riskiest part of QW's concept is the longer-term vision, not capture.** Feeding 1-on-1 signal into development and talent workflows is the step that engages EU AI Act high-risk classification (obligations now due 2027-12-02), US state AI-in-employment notice rules, discoverability concerns, and the sharpest employee objection.

---

## 2. How to read this report

- **Evidence grades**, carried through from the research notes:
  - [opened] the page itself was fetched and read. Pages were read through a fetch-and-summarize tool, so quoted wording should be re-checked verbatim before external use.
  - [snippet] taken from a search-result summary; the page was not opened or was blocked.
  - [claim] vendor marketing statement, not independently verified.
  - [3P] third-party or competitor-authored source.
- **Confirmed / Inferred / Unknown** are used for technology vendors. Confirmed means the vendor's own subprocessor list, help center, or an infrastructure vendor's customer page names it. Inferred is researcher reasoning. Unknown means the notes could not verify it.
- **Absence is not proof.** Statements such as "no capture found" or "not documented" mean no public source was found in this run. Vendors have commercial reasons not to advertise some features, HR-visible sentiment in particular.
- **Legal content is research for a product team, not legal advice.** Every legal point needs review by counsel before it is relied on.
- No QW internal metrics or confidential data are used.

---

## 3. The landscape in broad strokes

### 3.1 Five groups of players

- **HR and performance suites that capture 1-on-1s.** Lattice, 15Five, Leapsome, Betterworks, PerformYard, Deel Engage, Engagedly, Predictive Index. They compete on what the transcript connects to (reviews, goals, coaching), not on transcription quality.
- **HR suites that apply AI around the conversation without capturing it.** Culture Amp, Workleap, Workday, Rippling (1-on-1 product), HiBob, BambooHR, Paylocity, UKG, Qualtrics, Perceptyx, Gallup. Their inputs are survey, feedback, and goal data. Several feed engagement signal into the 1-on-1 agenda, which is the reverse direction of QW's proposed flow.
- **General-purpose notetakers.** Granola, Notion, Otter, Fireflies, Fathom, Read AI, Fellow, plus tl;dv, Circleback, Jamie, Krisp, Tactiq. The category has moved from "summary of one meeting" to "meetings as a company context layer" with cross-meeting chat, MCP and API access, and agents. Only Fellow is built around 1-on-1s.
- **Platform-native and big-AI entrants.** Zoom AI Companion and My Notes, Microsoft Teams Copilot and Facilitator, Google Meet Gemini notes, Slack huddle notes, Webex AI Assistant, ChatGPT Record, Claude Meetings. These make basic capture free or bundled for most customers.
- **Specialists and coaching vendors.** Windmill, Teamflect, Topicflow, Spinach (which absorbed Hypercontext), Confirm, Appraisd, Talos, Keka; coaching vendors Valence, BetterUp, CoachHub, Perceptyx Activate; and the sales conversation-intelligence precedent, Gong.

### 3.2 Structural shifts that explain the current state

- **Capture commoditized.** Seven notetakers that started with bots (Otter, Fireflies, Fathom, Read AI, Fellow, Jamie, Krisp) now also offer a desktop recorder, and the botless natives store transcript only, not audio. Notion states its desktop speaker labeling works best "in one-on-one virtual meetings", which is QW's use case. [opened] https://www.notion.com/help/ai-meeting-notes
- **The platforms moved into device-side and in-person capture.** Zoom My Notes covers Zoom, third-party, and in-person meetings [opened] https://www.zoom.com/en/lp/my-notes ; Google added "take notes with me" for in-person meetings in 2026-08 [snippet] https://workspaceupdates.googleblog.com/2026/08/take-notes-with-me-for-in-person-meetings-is-now-available.html ; Teams Facilitator has mobile capture of ad hoc discussions [opened] https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams
- **The standalone 1-on-1 tool category thinned.** Hypercontext is now part of Spinach AI [snippet] https://spinach.ai/hypercontext ; Mesh.ai was acquired by Netchex and relaunched for deskless HR on 2026-07-20 [snippet] https://itbrief.co.uk/story/netchex-launches-ai-hr-teammates-for-deskless-workers ; Fathom was acquired by Superhuman, announced 2026-09-14 [snippet] https://blog.superhuman.com/superhuman-acquires-fathom/ . The 1-on-1 workflow is consolidating into performance suites on one side and general notetakers on the other (researcher inference).
- **HR platforms are embedding capture themselves; notetakers are not integrating into HR platforms.** No general notetaker reviewed shows a packaged integration that pushes meeting content into a performance platform. Fellow's HRIS sync is for user provisioning only. [opened] https://fellow.ai/go/1on1-meeting-tool . This is "no evidence found", not "confirmed absent".
- **MCP exposure of meeting data is near-universal** among notetakers (Granola, Otter, Fathom, Fellow, tl;dv, Circleback) and is arriving in HR suites (Lattice, Culture Amp, PerformYard, 15Five as a claim). [opened] https://www.granola.ai/pricing , https://otter.ai/pricing , https://fathom.ai/pricing , https://fellow.ai/llms.txt
- **Consent became the governance battleground in 2026**, with both the bot model (Otter) and the botless model (Granola) in active litigation and vendors responding with automatic consent messages and admin-enforced consent. See section 7.

### 3.3 Scale signals (context only)

- Granola: $125M Series C at a $1.5B valuation in 2026-03, up from a $250M valuation in 2025-05. [snippet] https://siliconangle.com/?p=736110 and https://techcrunch.com/2025/05/14/ai-note-taking-app-granola-raises-43m-at-250m-valuation-launches-collaborative-features
- Recall.ai: $38M Series B in 2025-09, $51M total, $250M valuation. [snippet] https://www.axios.com/pro/enterprise-software-deals/2025/09/04/recallai-38-million-series-b-bessemer
- Otter: company-announced $100M ARR milestone in 2025. [snippet] https://www.businesswire.com/news/home/20251222704206/en/
- Fireflies: $1B valuation through a 2025 tender offer. [snippet] https://fireflies.ai/blog/fireflies-1-billion-valuation/

---

## 4. Competitor by competitor: capture, technology, and downstream use

This section answers asks 1 and 2 together. Each entry gives capture method, technology vendors (Confirmed / Inferred / Unknown), everything documented downstream, and what HR or admins can see.

### 4.1 Lattice — AI Agent in 1:1s, extended to Lattice Meetings

**Capture**
- A visible bot joins Zoom, Google Meet, or Microsoft Teams from a connected calendar. It must be invited by a participant and "never joins automatically" unless an admin enables auto-add. It announces in the meeting that it is recording and transcribing, posts a chat message, and participants get pre- and post-meeting notifications by Slack and email. [opened] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy and https://help.lattice.com/hc/en-us/articles/41244807202071-Agent-in-1-1-Meetings-Technical-FAQ
- Generally available since 2026-06. In 2026-10 "Lattice Meetings" widened scope to group and one-off meetings, including calls with external attendees. [opened] https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s and https://lattice.com/blog/october-2026-product-updates
- The 1:1 FAQ lists limits: no in-person meetings, English only. Whether these were lifted with Lattice Meetings is Unknown. No desktop app, browser extension, or mobile recording is documented.

**Technology**
- Confirmed: Recall.ai ("Hyperdoc, Inc. (Recall.ai)", "Meeting transcription bot") as an optional subprocessor; it "joins meetings and generates recordings and transcripts" and deletes its copy "within minutes after processing". OpenAI ("AI models for AI-powered features") is the only model provider listed. LangSmith for monitoring. AWS for hosting. [opened] https://lattice.com/privacy/subprocessors
- Inferred: OpenAI is the LLM behind 1:1 summaries and coaching, because it is the only model vendor listed. No page ties it to this feature by name.
- Unknown: the speech-to-text engine inside Recall.ai for Lattice. Anthropic, AssemblyAI, and Deepgram are not on Lattice's list.

**Downstream use**
- Shipped: topic-based summary, action items with owners, suggested agenda for the next 1:1, coaching insights for both participants, optional transcript, all on the 1:1 page. [opened] https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- Shipped: Evidence-based Review Drafts in Reviews surface insights from 1:1 meetings. [opened] https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- Shipped: a manager 1:1 brief generated from recent recaps and action items. [opened] https://lattice.com/blog/june-2026-product-updates
- Shipped: Lattice MCP lets users bring meeting context into Claude or ChatGPT, limited to existing Lattice permissions. [opened] https://lattice.com/blog/october-2026-product-updates
- Marketing claim only: 1:1 data "can support review writing, calibration, growth conversations, and performance decisions". No specific calibration or growth-plan integration is documented. [claim] https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s
- Not documented (Unknown): talk-time or sentiment analytics, manager-effectiveness scoring, recognition or feedback suggestions, automatic goal updates from transcripts.

**HR and admin visibility**
- Only participants can access transcripts and insights. Admins, HRBPs, and custom-role owners cannot view or download them, and admin impersonation does not grant access. [opened] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Lattice states "no secondary use of customer data, such as benchmarking across customers". Same URL.
- No HR dashboard built on meeting content is documented. Content still reaches reviews indirectly through drafts the manager writes. Whether Lattice's Workforce Intelligence product consumes meeting data was not checked.

**Governance**
- No audio or video collected. Transcripts are not retained by default; admins can turn on "Store transcripts". Participants can download a TXT transcript and delete it; it is permanently deleted only when both participants delete. No training on customer data. [opened] same privacy URL
- **Conflict in Lattice's own documentation on the retention period:** one statement says one-month increments up to 12 months; another says stored transcripts follow contract length plus 180 days. Unresolved; the two may describe selectable options versus a default. [opened] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy and [snippet] https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention
- Audit logs, legal hold, transcript redaction, EU AI Act posture: Unknown.

**Pricing**
- Agent in 1:1s and Lattice Meetings are "included for all Lattice customers at no additional cost"; Review Drafts are included for Performance customers. [opened] https://lattice.com/blog/introducing-the-lattice-ai-agent-in-1-1s and https://lattice.com/blog/october-2026-product-updates

### 4.2 15Five — Kona Notetaker, Meeting Assistant, Kona Coach

**Capture**
- A visible bot (Kona Notetaker, called Kona Meeting Assistant until about 2026-10) joins Zoom, Meet, or Teams when bot@15five.com is on the calendar invite. Admins choose auto-join or let managers decide. It is limited to a manager and their direct report, exactly two participants, virtual only. [opened] https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- It uses platform captions when available; if captions are off it asks in chat for permission to record, and if denied no notes are made. Chat commands "Kona pause", "Kona start", "Kona leave" work for any participant. [opened] same URL and https://success.15five.com/hc/en-us/articles/50988682248731
- A second meeting source exists: a company uses either Kona Notetaker or Google Meet as the source for Meeting Assistant. The mechanism for the Google Meet source is not described; ingestion of native Meet notes is inferred, not confirmed. [opened] https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together

**Technology**
- Confirmed: Recall.ai and Deepgram, both labelled only "API for meetings management"; OpenAI and Anthropic for AI functionality; Pinecone as vector database; AWS hosting (list effective 2026-09-23). [opened] https://www.15five.com/terms/data-processing-addendum/sub-processors
- Inferred: Recall.ai is the bot and Deepgram the speech-to-text, from each vendor's known business. Deepgram may be used only when captions are unavailable.
- Unknown: whether Kona summaries run on OpenAI or Anthropic. A 15Five FAQ refers to a single unnamed "LLM sub-processor", which is out of step with a list naming two. [opened] https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor

**Downstream use**
- Shipped: notes and action items written into the 15Five 1-on-1 agenda; post-meeting summaries by email, Slack, or Teams. [opened] setup guide URL above
- Shipped: meeting data enters the Context Layer and feeds Focus Briefs and AI-Assisted Reviews, where evidence is gathered as "Moments" and AI drafts text while managers select all ratings. AI-Assisted Reviews were labelled Beta in a release note; current status not re-verified. [opened] https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together and https://success.15five.com/hc/en-us/articles/36196491046043
- Shipped: Meeting Assistant sends the manager pre-meeting prep and writes notes and suggested actions afterwards; admins could move to it from 2026-10-12. Same URLs.
- Shipped, paid: Kona Coach gives managers private post-meeting tips, morning briefs, and monthly growth reports on behavior trends, drawing on meeting data alongside engagement scores and feedback trends. [opened] https://success.15five.com/hc/en-us/articles/36196491046043
- Marketing claim: Kona "tracks behavior reports over time" against 15Five's "18 Manager Behaviors". Scoring method is not explained. [claim] https://www.15five.com/products/kona
- Claim only: a "15Five MCP". No help-center documentation for a native MCP server was found. [claim] https://www.15five.com/products/kona
- Not documented (Unknown): talk-time or sentiment analytics, recognition suggestions, goal auto-updates, development-plan feeds.

**HR and admin visibility**
- Transcripts are accessible to no one: not HR, admins, managers, or employees, and not through the MCP. Raw transcripts are not released for compliance or audit. [opened] https://success.15five.com/hc/en-us/articles/50988682248731
- Notes and summaries are visible only to the two participants. Coaching tips are visible only to the manager. [opened] setup guide URL and https://success.15five.com/hc/en-us/articles/36196491046043
- Partial HR path: the HR-facing assistant "Amaya" answers admin questions using platform data "such as engagement, reviews, Check-ins, 1-on-1s, turnover, and employee attributes". Whether that includes Kona-captured notes is not specified. An "HR Outcomes Dashboard" is referenced but its contents were not seen. [opened] https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together
- Documented leak path: a suggested action added to the 1-on-1's action items is visible to anyone who can see those items, for example a global viewer. [opened] https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- 15Five says it does not use AI to build psychological profiles of individuals. Same URL.

**Governance**
- No recordings stored. Transcripts are encrypted, kept 30 days "for quality assurance", then deleted; no configurability is documented. [opened] https://success.15five.com/hc/en-us/articles/50988682248731
- **Conflict:** another 15Five help article is reported to say the recording and transcript are deleted after the meeting ends. [snippet] https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- The AI sub-processor is contractually barred from training on customer data. Audit logs and redaction: Unknown.

**Pricing — sources conflict and none is first-party**
- Kona Notetaker requires the Kona add-on on Perform or Total Platform. [opened] setup guide URL
- A third-party tracker (observed 2026-10-08) reports Meeting Assistant is now bundled into Perform and Total Platform, Kona Notetaker is $2 per employee per month, and Kona Coach is $19 per manager per month. The same tracker says Kona was $29 per manager in 2025-06 before moving to an employee-wide seat in late 2025. [3P] https://www.usagepricing.com/blueprint/activity/15five-2026-10-08-meeting-assistant-bundled
- The 15five.com pricing page was not read. Treat all figures as unverified.

### 4.3 Leapsome — Meeting Notetaker

**Capture — notes conflict**
- Help center (snippet grade, pages returned HTTP 403): three methods. A macOS desktop app that transcribes through system audio; in-browser transcription where the user shares a tab's audio; and pasting a transcript from another tool. [snippet] https://help.leapsome.com/hc/en-us/articles/36398991260445-Different-transcription-methods
- Marketing blog: the notetaker "joins the call" and runs on "the desktop app or any browser". [claim, opened] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- **Conflict:** no meeting-bot participant method appears in help-center snippets. The weight of evidence points to botless capture, but this is unresolved because the help articles could not be opened.
- Status also conflicts: the blog says it is live; a help snippet shows the admin toggle labelled "Meetings - (beta) transcription". [snippet] https://help.leapsome.com/hc/en-us/articles/30845027133213

**Technology**
- Confirmed: AI subprocessors are OpenAI, AWS (Bedrock, SageMaker), Google Cloud (Vertex AI), Cloudflare (Workers AI, MCP server), turbopuffer (vector database), LangSmith, Datadog. Core hosting in Germany. [opened] https://www.leapsome.com/en/subcontractors
- Confirmed absence from the list: no transcription, speech-to-text, or meeting-bot vendor (no Recall.ai, AssemblyAI, Deepgram).
- Inferred: transcription runs on one of the listed AI platforms or on-device. Which one is Unknown.

**Downstream use**
- Summaries, action items with owner and deadline that become tracked tasks linked to goals, talking points. [claim] blog URL above
- A review pre-draft "based on recent 1:1s". Whether it uses raw transcripts or only summaries is Unknown. [claim] same URL
- A "Development Coach" that surfaces coaching opportunities, plus an engagement summary for participants covering meeting quality, preparation, and clarity of outcomes. [claim] same URL
- HR or admin analytics on meeting data: not mentioned.

**Governance**
- Most explicit consent step found among HR suites: before transcription the host either plays an automated consent audio message or ticks a box confirming verbal consent. [snippet] https://help.leapsome.com/hc/en-us/articles/36397795997341
- "Your data is never used to train AI models". [snippet, claim] https://help.leapsome.com/hc/en-us/articles/38176995079709-AI-in-Leapsome-Overview-Settings
- Admins control recording, retention, and which meetings; no retention numbers given. Audio storage, deletion, editing: Unknown.

**Pricing**
- "Included in the Leapsome platform at no extra cost". [claim] blog URL above

### 4.4 Betterworks — Conversational Intelligence

- **Capture:** no bot. Completed Zoom transcripts are retrieved through the Zoom API and matched to the 1:1; "Betterworks does not use a transcription bot for Zoom." Users can also upload or paste transcripts, notes, or summaries from other tools. Teams and Meet native retrieval are not mentioned. Article dated 2026-09-10; GA or beta status not stated. [opened] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- **Technology:** Confirmed transcript source is the Zoom API. LLM provider Unknown.
- **Downstream:** recap, suggested action items and agenda topics, goal-progress identification with suggested milestone updates, potential new goals, and a private "AI Meeting Prep" brief per participant. All recommendations stay pending until a user confirms, edits, or discards them. Feedback, reviews, and "talent intelligence" are named without a mechanism. Same URL.
- **HR visibility:** no HR dashboard, sentiment, or manager-effectiveness metric described.
- **Governance:** consent, retention, and deletion for transcript data are not addressed on the page. Unknown.
- **Pricing:** Unknown.

### 4.5 PerformYard — Meeting Coaching

- **Capture:** users link a Zoom or Microsoft Teams account and PerformYard captures "transcripts once a meeting ends"; an admin switch disables "Video Conferencing & Transcripts". Google Meet retrieval not found. No bot is described; ingestion of the provider's transcript is inferred from the wording. [snippet] https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup
- **Technology:** LLM provider Unknown.
- **Downstream:** the most developed manager-coaching catalogue found. Post-meeting sections, each admin-toggleable: Decisions Made, Missed Commitments, Participation & Inclusion (speaking-time distribution), Quality of Discussion vs. Monologue, Time Management, and Meeting Coaching (top strength, primary development area, one thing to try). Pre-meeting prep draws on goals, feedback, reviews, and survey insights. [opened] https://support.performyard.com/article/516-meeting-coaching-setup
- **HR visibility:** PerformYard says its AI "summarizes 1:1 meetings for individuals, teams, or the entire organization" and surfaces "themes from 1:1 meeting notes". This is the clearest HR-level claim in the set, but it is phrased in terms of meeting notes, so whether transcript content reaches HR-level summaries is unclear. [claim, opened] https://www.performyard.com/ai
- **Governance:** the help article says AI output should be human-reviewed and not be the sole basis for employment decisions. Consent and retention are not addressed.
- **Pricing:** Meeting Coaching requires a "Talent Development license". [opened] setup URL above

### 4.6 Deel Engage — Checkins

- **Capture:** "After a Google Meet call ends, Checkins automatically fetches the transcript". Only Google Meet is named; no bot or recording is described. [opened] https://www.deel.com/solutions/engage/one-on-one-meetings/
- **Technology:** transcript source Google Meet (Confirmed). LLM Unknown. Deel appears as a Recall.ai Meeting Bot API customer, but Recall's recruiting page names Deel for interview notes, so which Deel product uses Recall is Unknown. [opened] https://www.recall.ai/solutions/hr
- **Downstream:** key points and commitments populate notes and action items; suggested talking points; a session summary for review prep. Deel claims conversations "connect directly to goals, reviews, and development plans" with no mechanism given. [claim] Deel URL above
- **Governance:** consent, retention, and deletion not addressed; "The raw transcript is always one tab away", and which roles can open it is not stated.
- **Pricing:** part of Engage; not sold individually.

### 4.7 Engagedly — Marissa AI Notetaker

- **Capture:** a notetaker that joins the meeting; organizers decide whether to admit it. Enabled for "Google Conference" or "Microsoft Conference" meeting types. Zoom support Unknown. [opened] https://engagedly.com/product/meetings/ and [snippet] https://help.engagedly.com/schedule-one-on-one-meeting-1
- **Technology:** bot vendor, transcription vendor, and LLM all Unknown.
- **Downstream:** notes, summaries, AI-suggested tasks, "meeting reflections". No feed into other modules described.
- **Governance:** admin availability control; no consent, notice, or retention statements found.

### 4.8 Predictive Index — PI Meeting Notetaker (beta)

- **Capture:** opt-in per meeting; joins Zoom, Teams, and Meet as a participant; records no audio or video and builds notes from the conferencing tool's captions. [opened] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker
- **Technology:** bot vendor and LLM Unknown.
- **Downstream:** summary, suggested action items (accept or reject), outline. No feed into reviews or goals.
- **Context:** the same article states Perform is retiring on 2027-09-30. This is not a long-term competitor in this space.

### 4.9 Rippling

- Rippling's own 1:1 pages describe a notes editor with templates, action items, goals, and past feedback, with no recorder. [snippet] https://www.rippling.com/blog/introducing-1-1s
- Recall.ai lists Rippling as a Meeting Bot API customer. **The notes disagree on how to read Recall's page:** one researcher reports it as saying Rippling uses meeting data to "generate notes, surface insights on performance and employee satisfaction"; another cautions the text reads as generic solution copy and that Rippling's known recorder is in Recruiting. Whether Rippling ships 1:1 capture or an admin-visible satisfaction insight is Unknown and needs primary confirmation. [opened] https://www.recall.ai/solutions/hr

### 4.10 HR platforms with no verified 1-on-1 capture

All "no capture" statements here rest on absence in vendor pages and search results, not on a vendor statement.

- **Culture Amp:** no transcript or video integration in 1-on-1 Conversations. [opened] https://support.cultureamp.com/en/articles/9258377-1-on-1-conversations . Its strategy is to meet users in their assistant: an MCP connector for Claude and ChatGPT where 1-on-1s is the only read/write area, at no additional cost "today" [opened] https://support.cultureamp.com/en/articles/16754009-connect-claude-or-chatgpt-to-your-1-on-1-conversations-via-mcp ; and "Enso", announced 2026-10-27, an agent that prepares 1:1 agendas and follows up on commitments [snippet, claim] https://www.cultureamp.com/company/announcements/enso-by-culture-amp-news
- **Workleap:** an agent that books 1:1s and builds agendas from check-ins, pulse signals, and feedback; "HR gets a live view of every 1:1 across the organization" covering completion, cadence, and engagement trends, not conversation content. [claim, opened] https://workleap.com/lp/meeting-automation
- **Workday:** Sana Coach lists Talent Sentiment and Performance Review agents; Goals & Check-Ins is "Coming soon". Review drafts accept "user-uploaded documents", a possible manual route for notes; transcripts are not named. [opened] https://www.workday.com/en-gb/ai-agents/sana/coach.html
- **Microsoft Viva:** capture lives in Teams, not Viva. No Viva-branded manager 1:1 workflow was found; Viva Goals was retired 2025-12-31. [snippet] https://learn.microsoft.com/en-gb/viva/goals/goals-retirement
- **HiBob, BambooHR, Paylocity, UKG, Qualtrics, Perceptyx, Gallup:** no 1-on-1 transcript capture found. Perceptyx and Gallup offer coaching or prep assistants that draw on survey or research data. [snippet] https://www.hibob.com/platform/talent/performance-management/ , https://blog.perceptyx.com/grow-smarter-unlock-greater-leadership-potential-with-ai-coach , https://support.gallup.com/hc/en-us/articles/48408264183827-Gallup-AI

### 4.11 Specialists

- **Windmill:** botless. Transcripts and notes from Zoom, Google Meet, Gong, Granola, and Roam "appear inside the meeting view"; "Audio and video stay on the source platform". Feeds agenda building, action-item carry-forward, and a "Catch Me Up" brief. Notes are private to the two participants; admins see only that a 1:1 was held, its date, and participants. Underlying vendors Unknown. [opened] https://gowindmill.com/features/one-on-ones
- **Teamflect (Teams-native):** has a help article on using AI meeting transcripts; "AI-Powered Meeting Intelligence" is listed as in progress on its roadmap. Notes stay between manager and employee; HR sees whether 1:1s happen. Its agent "flags risks" from performance data; whether transcripts are an input is Unknown. [snippet] https://help.teamflect.com/en/articles/16860659-how-to-use-ai-meeting-transcripts-in-teamflect and https://roadmap.teamflect.com/feature-requests/p/meetings-ai-powered-meeting-intelligence
- **Fellow:** see 4.12.
- **Topicflow:** uses AI to analyze meeting transcripts; a third-party profile lists "manager effectiveness metrics", source of those metrics Unknown. [snippet] https://www.geekwire.com/2024/topicflow-raises-1-8m-to-rethink-performance-reviews-with-help-from-ai/
- **Smaller review-meeting notetakers:** Appraisd (beta, records via shared screen audio), Talos Perform, Keka (alpha, Teams). [snippet] https://www.appraisd.com/performance-management/ai-notetaker , https://talos360.co.uk/perform/ai-notetaker/ , https://help.keka.com/hc/en-us/articles/42553412708113-PERFORM-AI-Powered-1-1-Meeting-Transcription-Summary-MS-Teams-Integration-Alpha-Customers
- **AI coaching vendors:** Valence's Nadia is integrating Microsoft Graph and Work IQ context; no source confirms full transcript ingestion [snippet] https://valence.co/blog/valence-microsoft-365-may-2026 . BetterUp says its coach's memory can draw on meeting transcripts [snippet] https://www.betterup.com/blog/ai-coach-memory . No coach was found that documents scoring managers from 1-on-1 transcripts.

### 4.12 Best-in-class general notetakers

- **Granola**
  - Capture: botless desktop app, started manually; stores transcript and notes, not audio. iPhone app for in-person meetings. [opened] https://www.granola.ai/security
  - Technology (Confirmed, list may be non-exhaustive): transcription providers "like Deepgram and Assembly"; LLMs "like OpenAI and Anthropic"; US-hosted AWS. Same URL.
  - Downstream: Recipes (saved prompts across multiple meetings, with a people view), shared folders, MCP server and API by plan tier. No 1-on-1-specific product feature. [opened] https://docs.granola.ai/help-center/getting-more-from-your-notes/recipes and https://www.granola.ai/pricing
  - Governance: Granola trains on anonymized data with opt-out; off by default for Enterprise. Third parties may not train. Consent message is opt-in and macOS only. [opened] https://www.granola.ai/security ; [snippet] https://docs.granola.ai/help-center/managing-your-account/automatic-consent-messaging
  - Pricing: $0, $14, $35 per user per month. [opened] https://www.granola.ai/pricing
- **Notion AI Meeting Notes**
  - Capture: botless, system audio plus mic in the desktop app; audio is not stored by sub-processors. [opened] https://www.notion.com/help/ai-meeting-notes
  - Technology: speech and LLM sub-processors Unknown (not named on the help page).
  - Downstream: summaries with transcript citations, follow-up task skills, Notion Agent on the note, a meetings database that inherits workspace permissions.
  - Governance: workspace owners can enforce an automatic audio consent message; Enterprise automatic transcript deletion keeps summaries. Same URL.
- **Otter**
  - Capture: bot joins Zoom, Teams, Meet; desktop, extension, and mobile options. Audio is stored and exportable. [opened] https://otter.ai/pricing
  - Technology: transcription engine, LLM vendors, and subprocessors Unknown from this run.
  - Downstream: AI Chat across meetings, channels, workflows, MCP server, API and webhooks on Enterprise. Same URL.
  - Governance: reported to train on de-identified data by default with opt-out. [3P] https://www.getvoibe.com/resources/is-otter-safe/
- **Fireflies**
  - Capture: bot by default; botless desktop app. Video recording on Business. [opened] https://fireflies.ai/pricing
  - Technology: Unknown. Security page names no subprocessors.
  - Downstream: talk time and sentiment analytics, API, live voice assistant.
  - Governance: "Fireflies does not use your meeting data to train AI models"; SOC 2 Type II, ISO 42001. [opened] https://fireflies.ai/security
- **Fathom**
  - Capture: bot; bot-free in beta for Mac. [opened] https://fathom.ai/pricing
  - Technology: AI subprocessors reported as Anthropic, OpenAI, and Google (secondary); speech-to-text Unknown. [3P] https://www.getvoibe.com/resources/is-fathom-safe/
  - Downstream: Ask Fathom, team workspace, "Coaching metrics & AI scorecards" (sales-oriented), API and MCP. Now owned by Superhuman.
- **Read AI**
  - Capture: bot plus desktop and mobile apps. [opened] https://www.read.ai/plans-pricing
  - Technology: Unknown (support site returned HTTP 403).
  - Downstream: a meeting coach on every plan with metrics such as "talking speed, filler words, bias, and charisma"; per-participant engagement and sentiment scores. No dedicated 1-on-1 or manager feature found.
  - Reception: the clearest backlash example in the notes. Privacy advocates called its sentiment tool invasive, and a review site reports a university blocked it. [snippet] https://techcrunch.com/?p=2685382 ; [3P] https://www.eesel.ai/blog/read-ai-reviews
- **Fellow** (the only notetaker built around 1-on-1s)
  - Capture: bot on Zoom, Meet, Teams; botless desktop app; in-person with diarization. [opened] https://fellow.ai/llms.txt
  - Technology: Confirmed Recall.ai for bot recording [opened] https://www.recall.ai/customers ; AWS hosting. Transcription and LLM vendors Unknown.
  - Downstream: agendas, action items, recaps with speaker time, "Ask Fellow", MCP server. Third-party reviews describe performance-review synthesis from notes; not confirmed first-party.
  - Governance: the most advanced consent posture found. "Fellow never trains on customer data"; consent disclosure events are logged; a "Zero-Day Retention" option; and a 2026-08 governance suite in which attendees agree or decline before joining. [opened] https://fellow.ai/llms.txt ; [snippet] https://www.cfo.com/press-release/20260828-fellows-new-governance-suite-brings-compliance-grade-controls-to-ai-meetin/
  - Tension: "Compliance teams receive workspace-level access to retrieve any meeting record across the organization." [opened] https://fellow.ai/llms.txt
  - Pricing: $7 to $25 per user per month on annual billing. [opened] https://fellow.ai/pricing
- **tl;dv, Circleback, Jamie, Krisp, Tactiq:** thinner coverage, mostly third-party. Circleback appears on Recall.ai's customer wall. [opened] https://www.recall.ai/customers
- **Unknown across the board:** whether Otter, Fireflies, Fathom, or Read AI run in-house bot infrastructure. Their absence from Recall.ai's customer page is not proof.

### 4.13 Platform-native AI and big-AI entrants

- **Zoom:** AI Companion summaries are included in paid Workplace plans; My Notes extends to third-party and in-person meetings with a free tier. Whether My Notes uses a bot or device audio on other platforms is Unknown. Zoom states it does not train its own or third-party models on customer content. Zoom describes a federated model approach; the named models come from an uncertain secondary source. [opened] https://www.zoom.com/en/lp/my-notes
- **Microsoft Teams:** intelligent recap is in Teams Premium and Microsoft 365 Copilot; Facilitator needs a Copilot licence and "isn't supported in 1:1 chats, group chats, or external chats and meetings". [opened] https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams . A "recap without transcript" mode exists for compliance-sensitive tenants; rollout timing conflicts across mirrors. [snippet] https://mc.merill.net/message/MC1275312 . Uses Microsoft's own speech pipeline.
- **Google Meet:** Gemini "take notes for me" is native, notifies participants, and saves to a Google Doc under Vault retention. Since 2026-04 admins can require explicit participant consent (off by default). Eligible editions are listed inconsistently across Google pages. [opened] https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html
- **Slack and Webex:** Slack huddle notes are in all paid plans; Webex AI Assistant is managed in Control Hub. Retention and developer access are thinly documented. [snippet] https://slack.com/help/articles/39264531104275-Updates-to-feature-availability-and-pricing-for-Slack-plans
- **ChatGPT Record (OpenAI):** macOS desktop recording; audio deleted after transcription; disabled by default for Enterprise and Edu. [snippet, page returned HTTP 403] https://help.openai.com/en/articles/11487532-chatgpt-record
- **Claude Meetings (Anthropic):** announced 2026-11-12 in beta for Team and Enterprise, Google Meet first; joins as a visible participant and saves transcript and summary, not audio. [snippet] https://venturebeat.com/ai/anthropic-brings-claude-into-google-meet-to-draft-documents-and-whiteboards-during-your-meetings/ . A reported Claude desktop recorder is based on unreleased code strings only and is speculation.
- **No manager-specific 1-on-1 product was found from any platform or big-AI entrant.** A Microsoft community post from 2026-04 reports Copilot did not produce a structured 1:1 agenda from prior meetings. [snippet] https://techcommunity.microsoft.com/discussions/microsoft365copilot/using-copilot-to-help-with-11-meeting-prep-for-managers/4508256

---

## 5. What is done with the data downstream: the pattern across vendors

### 5.1 Well-evidenced and shipped

- **Summaries and action items:** every capturing vendor.
- **Pre-meeting prep and agenda carry-forward:** Lattice, 15Five, Betterworks, PerformYard, Windmill, Deel.
- **Review drafting from 1-on-1 evidence:** Lattice (shipped), 15Five (Beta at launch), Leapsome (claim), Deel and Betterworks (implied, no mechanism).
- **Goal progress suggestions:** Betterworks only, pending user confirmation.
- **Manager coaching from the conversation:** Lattice (both participants), 15Five Kona Coach (manager only), PerformYard (admin-configurable, includes speaking-time and monologue analysis), Leapsome (claim).
- **MCP or assistant access to meeting context:** Lattice (shipped), PerformYard (snippet), Culture Amp (1-on-1 objects, not transcripts), 15Five (claim).

### 5.2 Claimed in marketing, no documented mechanism

- Calibration and talent-review input: Lattice, Betterworks.
- Development or growth plans: Lattice ("growth conversations"), Deel ("development plans").
- Compensation: PerformYard ("review outcomes feed comp and growth plans"), Deel ("compensation trajectory").

### 5.3 Not found at any vendor in scope

- Recognition suggestions from transcripts.
- Development-plan or skills inference from transcripts.
- Published manager benchmarks or numeric manager-effectiveness scores from 1-on-1 transcripts.
- An HR or admin dashboard of sentiment, burnout, or flight risk derived from 1-on-1 conversation content.

### 5.4 The HR-dashboard question specifically

- **Documented norm is the opposite of an HR dashboard:** content private to the pair, coaching private to the manager, HR sees only that meetings happened (Lattice, 15Five, Windmill, Teamflect).
- **Nearest exceptions:** PerformYard's org-level 1-on-1 summaries [claim] https://www.performyard.com/ai ; 15Five's Amaya [opened] https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together ; Recall.ai's description of Rippling (disputed, section 4.9); Read AI's per-participant sentiment scores, which drew backlash.
- **A reference model for aggregate insight exists outside 1-on-1s:** Microsoft Viva Insights enforces a minimum group size that cannot go below five. Sources conflict on the default (5 or 10). [snippet] https://learn.microsoft.com/en-us/viva/insights/privacy/privacy-considerations . No HR vendor was found applying an aggregation threshold to 1-on-1 content.
- **A consistent design choice is "suggest, human confirms":** Betterworks' pending recommendations, 15Five's "managers select all ratings", Windmill's statement that AI is not evaluating anyone's performance, PI's accept or reject.
- **Sales conversation intelligence shows a possible trajectory.** Gong moved from human scorecards to AI-suggested answers to fully automatic scoring labelled "Scored by: Gong AI", and it does not count AI-generated scorecards as manager coaching. [snippet] https://help.gong.io/docs/gong-ai-for-scoring and https://help.gong.io/docs/all-about-scorecards . The analogy is imperfect: a 1-on-1 has no external party and no won-or-lost outcome to validate against.
- **Outcome evidence is missing market-wide.** No independent study shows AI-captured 1-on-1s improve follow-through, review quality, or manager effectiveness. Available numbers are vendor claims.

---

## 6. Table stakes, common, and differentiating features

The classification is researcher judgment from the evidence. It is thinner where vendor documentation was not opened (audit logs, legal hold, BYOK, group-level enablement).

### 6.1 Table stakes

- In-meeting announcement or visible indicator, and any participant able to remove or stop the recorder (Lattice, 15Five).
- No audio or video retained (Lattice, 15Five, PI, Granola, Notion).
- Admin-configurable transcript retention with auto-deletion (Lattice; Leapsome by claim).
- Participant-only visibility with HR and admin lock-out from raw 1-on-1 content (Lattice, 15Five, Windmill).
- No training on customer data (Lattice, 15Five, Leapsome, Fellow, Fireflies, Zoom).
- Published subprocessor list, encryption in transit and at rest, SOC 2 Type II, GDPR DPA, org-level admin on or off, SSO.

### 6.2 Common

- Pre-meeting notification emails (Lattice, Fireflies, Fathom).
- Transcripts off or short-lived by default (Lattice off; 15Five 30 days).
- Participant deletion and download of transcripts (Lattice).
- Manager-only coaching output (15Five).
- Admin audit logs in enterprise notetakers (Otter activity logs, Fellow consent logs); undocumented among HR-platform 1-on-1 peers.
- Zero-retention terms with LLM providers, EU residency at enterprise tier, ISO 27001, HIPAA BAA at enterprise tier.
- Human confirmation before AI output becomes a system record.

### 6.3 Differentiating

- Affirmative per-participant opt-in that blocks capture until given and is logged (Fellow's agree-or-decline; Gong's consent page; Google's admin-enforced consent).
- Employee-side unilateral pause, redact, or delete. Lattice requires both participants to delete before a transcript is permanently removed.
- Automatic exclusion of sensitive topics. No vendor documentation was found; 15Five says notes are filtered to "performance-relevant content". Absence here reflects limited search depth.
- A summary-only mode that never stores a transcript (Fellow Zero-Day Retention; Teams recap without transcript).
- Legal hold, enablement by group or legal entity, BYOK: no evidence for any vendor.
- An employee-visible audit trail of access, export, redaction, and deletion.
- No persistent voiceprints by design; explicit exclusion of emotion inference from voice.
- ISO 42001 (reported for Fireflies and Gong); a works-council documentation pack.

### 6.4 QW's draft answer measured against the market

- **Customizable transcript retention policy:** table stakes. Lattice already offers off-by-default storage with an admin-set period. Not a differentiator by itself. The longer-lived record at both Lattice and 15Five is the notes and insights, not the transcript, so retention messaging needs to cover derived artifacts.
- **Dual consent:** not a named standard feature anywhere in the notes. Nearest equivalents are Lattice (either party can remove the agent), 15Five (chat permission; denial means no notes), and Leapsome (host confirms consent). A true two-sided opt-in where the direct report affirmatively accepts would be at or ahead of HR-platform peers and in line with Fellow.
- **Transcript review and redaction:** ahead of HR-platform peers on the evidence found, which is thin. Lattice allows editing of action and agenda items only; 15Five transcripts are not viewable. Fellow is credited with redaction in a source that includes its own blog.
- **Audit log:** an enterprise-notetaker norm rather than a documented HR 1-on-1 feature. 15Five explicitly refuses to release raw transcripts for audit, which is the opposite design choice.
- **Missing from the draft, and already led with by peers:** no audio or video storage; HR and admin lock-out from 1-on-1 content; no training or secondary use of customer data; human-in-the-loop on any performance use.

---

## 7. The legal and regulatory environment driving these features

Research for a product team, not legal advice.

### 7.1 US recording consent

- Roughly a dozen states require all-party consent. One law-firm list: California, Connecticut, Florida, Illinois, Maryland, Massachusetts, Michigan, Montana, Nevada, New Hampshire, Pennsylvania, Washington. Lists differ at the margins. [opened] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- The federal Wiretap Act is one-party consent, with an exception where interception is for a criminal or tortious purpose. California's CIPA § 631(a) may expose the notetaker vendor itself. Same URL.
- Recommended practice is to apply the strictest standard to every meeting. Same URL.

### 7.2 Litigation (no finding of liability in any case)

- **In re Otter.AI Privacy Litigation (N.D. Cal.):** on 2026-08-13 the court granted in part and denied in part Otter's motion to dismiss. Wiretap, California eavesdropping, and Illinois BIPA voiceprint claims proceed. The court declined to assume a visible notetaker meant participants agreed to be recorded. The order itself was not readable; holdings are from secondary summaries. [opened, secondary] https://www.isbamutual.com/liability-minute/ai-notetaking-privacy-claims-survive-otterai-lawsuit
- **Chamberlain v. Granola (N.D. Cal., filed 2026-07-30):** targets the botless design and default model training. Allegations only. [snippet] https://btlaw.com/en/insights/alerts/2026/what-the-granola-class-action-means-for-companies-building-and-deploying-conversation-capture-tools
- **Fireflies and Microsoft Teams:** BIPA voiceprint suits are reported only by competitor or vendor blogs with conflicting case details; dockets were not checked. One of the research notes lists Fireflies litigation as Unknown. [3P] https://scribbl.co/post/fireflies-ai-lawsuit
- **Three recurring allegations:** non-users recorded without their own consent; the vendor's own use of content for training; speaker identification creating voiceprints without a written release.
- **Vendor-as-eavesdropper logic:** a vendor that keeps and uses data for its own purposes can be treated as a third-party interceptor. A strict no-training, no-secondary-use commitment is therefore a legal-exposure control (researcher inference from the secondary summary).

### 7.3 Discoverability and law-firm guidance

- Mayer Brown (2026-06) recommends a tiered model that defaults to no AI notetaker for legal advice, HR investigations, and performance matters, and advises retention limits, deletion workflows, consent logs, and human review. It also flags ADA medical confidentiality, NLRA Section 7 surveillance concerns, and transcription-error bias. [opened] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- SHRM's CHRO (2026-09-14) urges disclosure and approval from everyone present before recording. [opened] https://www.hrdive.com/news/hr-must-set-boundaries-ai-notetakers/830276/
- No guidance was found that treats purpose-built 1-on-1 assistants inside HR platforms as a distinct category.

### 7.4 European Union

- **Emotion recognition:** AI Act Article 5(1)(f) prohibits inferring employees' emotions in the workplace, in application since 2025-02-02. Secondary readings say text-only analysis without biometric data falls outside the ban; the Commission guideline text was not opened. [snippet] https://www.insideprivacy.com/artificial-intelligence/european-commission-guidelines-on-prohibited-ai-practices-under-the-eu-artificial-intelligence-act/ and https://www.praxikon.com/en/posts/emotion-recognition-workplace-ban-ai-act
- **High-risk:** AI used for performance evaluation, monitoring of workers, and promotion or termination is high-risk. The Digital Omnibus moved those obligations from 2026-08-02 to 2027-12-02. [snippet] https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- **GDPR and Germany:** "by joining you consent" is not valid consent; employees must be able to refuse without consequences [snippet, vendor blog] https://meetergo.com/en/magazine/ai-meeting-notes-gdpr . German works councils have co-determination rights over systems capable of monitoring behaviour or performance; this rests on vendor blogs, no primary German source was opened. [snippet] https://meetkalima.com/blog/works-council-ai-transcription

### 7.5 US state AI-in-employment rules

- Illinois HB 3773, effective 2026-01-01, requires notice of AI use in employment decisions. Texas TRAIGA effective 2026-01-01. California CPPA automated-decision rules require compliance for employment decisions by 2027-01-01. [snippet] https://www.ebglaw.com/insights/publications/workplace-ai-regulation-in-2026-how-employers-can-navigate-the-changing-legal-landscape and https://aiemploymentlawtracker.com/
- Colorado's AI Act was repealed and replaced in 2026-05 by a narrower disclosure law effective 2027-01-01. [snippet] https://www.seyfarth.com/news-insights/colorado-enacts-artificial-intelligence-replacement-law.html
- These attach when AI output is used in an employment decision. A summarizer is largely outside them; a pipeline from transcripts into performance or talent decisions moves customers toward them (researcher inference). All dates are from law-firm alerts and trackers, not primary pages.

### 7.6 Employee attitudes

- A law-firm-commissioned survey (fielded 2026-07, n=500 employed US adults) found 33.4% had an AI notetaker in work meetings and only 34.7% of those were always asked permission. It does not isolate 1-on-1s. [opened] https://kesq.com/stacker-business-economy/2026/07/16/ai-notetakers-have-sat-in-on-1-in-3-us-workers-meetings-but-only-a-third-say-they-were-asked-first/
- A widely repeated "84% change how they speak" figure could not be traced to a primary source and should not be used.
- No controlled study on recording and candor in manager-employee conversations was found.

---

## 8. QW's technical options for capture

### 8.1 Three routes

- **Visible bot.** Built-in notice, no install, works on any device. Can be blocked by a host or admin, and feels intrusive in a sensitive conversation. This is the Lattice and 15Five route.
- **Botless desktop capture.** Records system audio plus microphone on the user's machine (Core Audio taps on macOS 14.2 or later, or ScreenCaptureKit; WASAPI loopback on Windows). Covers any platform and in-person meetings. Requires IT to deploy an app and grant OS permissions, and QW must build its own notice and consent because the other party sees nothing. Two-channel capture separates two remote speakers well. [snippet, vendor blog] https://www.recall.ai/blog/core-audio-taps
- **Ingest the transcript the platform already made.** Cheapest, and inherits the customer's own notice and retention governance. Coverage depends on customer licences and admin settings. This is the Betterworks, PerformYard, Deel, and Windmill route. A paste or upload fallback (Leapsome, Betterworks) covers everything else.

### 8.2 Platform API constraints for ingestion

- **Microsoft Teams (Graph):** transcript APIs are no longer metered since 2025-08-25. Access needs tenant admin consent plus an application access policy, or per-meeting resource-specific consent. Since the end of 2026-07 two tenant switches can block Graph transcript access entirely or strip speaker attribution. Whether they default on or off is Unknown. [opened] https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts and https://learn.microsoft.com/en-us/graph/api/calltranscript-get
- **Zoom:** cloud-recording transcript webhooks (need cloud recording and transcription on); the AI Companion summary API (summary, not full transcript); and RTMS for live diarized transcripts, paid in Developer Pack credits with no public per-minute rate found. All are host-account scoped. Developer-forum threads report missing webhooks (unverified user reports). [opened] https://developers.zoom.us/docs/rtms/meetings/
- **Google Meet:** the REST API gives post-meeting transcripts and Gemini smart notes; transcript entries are deleted 30 days after the conference. Google is shutting down the real-time Meet Media API on 2027-01-15, so there is no sanctioned botless real-time path on Meet. [opened] https://developers.google.com/workspace/meet/release-notes and https://developers.google.com/workspace/meet/api/guides/artifacts
- **Slack huddles:** no evidence of a transcript API. Unknown.

### 8.3 Build versus buy, with costs

- **Recall.ai:** $0.50 per recording hour for both the Meeting Bot API and the Desktop Recording SDK; built-in transcription adds $0.15 per hour; US, EU, or JP residency. Its HR page shows 15Five, Rippling, Deel, Leadr, ClearCompany, BrightHire, and Fellow. [opened] https://www.recall.ai/pricing and https://www.recall.ai/solutions/hr
- **Nylas Notetaker:** $0.70 to $0.80 per hour beyond plan allowances. [opened] https://www.nylas.com/pricing/
- **Cheaper hosted rivals and open source:** MeetingBaaS, Skribby, MeetStream at roughly $0.35 to $0.69 per hour (secondary sources); Attendee and Vexa are self-hostable. [snippet] https://www.nylas.com/blog/best-meeting-bot-apis/
- **Speech-to-text:** Deepgram Nova-3 pre-recorded is $0.0043 per minute, about $0.26 per hour, with diarization included. Other vendors' prices are secondary. [opened] https://deepgram.com/pricing
- **Indicative unit cost (researcher arithmetic):** a manager with four 30-minute 1-on-1s a week costs roughly $4 to $6 per month in bought capture plus transcription. Ingesting a native transcript has no capture or speech-to-text cost.
- **Evidence leans toward "buy capture, build the insight layer":** HR peers appear as Recall.ai logos, BrightHire describes offloading its recorder as "a huge sigh of relief", and platform changes (Meet Media API shutdown, new Teams switches) make owned capture a moving target. No neutral data on build-versus-buy share was found.
- **A hybrid is the pattern the evidence supports (researcher inference):** ingest native transcripts where the customer already produces them, and fall back to a bought bot or desktop SDK elsewhere.

---

## 9. What changed since the March 2026 internal brief

- **"Only Lattice and 15Five had shipped in-meeting transcription among HR platforms" no longer holds.** The notes document capture at Leapsome, Betterworks, PerformYard, Deel Engage, Engagedly, and Predictive Index (beta), plus smaller vendors (Appraisd, Talos, Keka in alpha) and the specialist Windmill. Most of these are not in-meeting bots; they are botless or ingest models. The notes do not establish when each shipped, so some may predate 2026-03. The notes date Lattice's general availability to 2026-06.
- **"Kona cost $29 per manager per month" is outdated.** A third-party tracker reports $29 per manager was the 2025-06 price, that Kona moved to an employee-wide seat in late 2025, and that current figures are $2 per employee per month for Kona Notetaker and $19 per manager per month for Kona Coach, with the Meeting Assistant agent bundled into Perform in 2026-10. None of this is verified on a 15Five page. [3P] https://www.usagepricing.com/blueprint/activity/15five-2026-10-08-meeting-assistant-bundled
- **"Granola had raised $43M at a $250M valuation" describes 2025-05.** Granola raised a $125M Series C at a $1.5B valuation in 2026-03. Total raised is reported between about $176M and $192M. [snippet] https://siliconangle.com/?p=736110
- **"Betterworks had no capture" is superseded.** Conversational Intelligence retrieves Zoom transcripts through the Zoom API and accepts pasted or uploaded transcripts (article dated 2026-09-10). [opened] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- **"Leapsome's capture model was unclear" is partly resolved.** Help-center snippets describe three methods: macOS desktop system audio, in-browser tab audio, and pasted transcripts. A marketing blog still says the notetaker "joins the call", and the help center could not be opened, so a residual conflict remains.
- **Other updates worth carrying forward:** Lattice extended capture to group and external meetings (2026-10); 15Five renamed and repackaged its products (2026-10); Fathom was acquired by Superhuman (2026-09); the Otter ruling (2026-08-13) and the Granola suit (2026-07-30) changed the consent picture; Google announced the Meet Media API shutdown (2026-10-28); Microsoft added tenant switches over Graph transcript access (2026-07); the EU high-risk deadline moved to 2027-12-02.

---

## 10. Implications and open questions for QW

**This section is analysis, not fact.** It draws only on the evidence above.

### 10.1 Implications

- **Capture will not differentiate; the link to QW's own data can.** Customers on Zoom, Teams, Meet, Notion, ChatGPT, or Claude already have free or bundled notes. General notetakers have no connection to goals, feedback, reviews, recognition, or engagement data, and none was found integrating with a performance platform.
- **"Records or consumes a transcript" is the right framing, and "consumes" deserves equal weight.** The majority of HR-suite competitors that capture 1-on-1s avoid a bot. A bot-only launch would match Lattice and 15Five but look dated next to Leapsome, Betterworks, and botless notetakers. An ingest-plus-paste path is cheap and sidesteps part of the consent burden, at the cost of uneven coverage.
- **Suggested in-platform actions appear to be open space.** Recognition suggestions and development-plan suggestions from 1-on-1 content were not found at any vendor. Betterworks' goal suggestions show the accepted pattern: suggest, then require human confirmation.
- **Manager coaching is contested, but coaching grounded in engagement and performance data is less so.** Lattice, 15Five, PerformYard, and Leapsome all coach from the conversation. The survey-led vendors (Culture Amp, Workleap, Perceptyx) feed engagement signal into the 1-on-1. QW could run both directions; no vendor was found documenting both.
- **Pricing has a hard reference point of zero.** Lattice and Leapsome include capture at no extra cost; 15Five reportedly bundled its agent. The exceptions tie a charge to a coaching or development tier (PerformYard, Kona Coach).
- **The draft trust answer needs three additions to reach parity** (no audio or video storage, HR and admin lock-out, no training or secondary use) before its two potential differentiators (two-sided consent, employee redaction) count for much.
- **An HR sentiment dashboard would be ahead of what any competitor publicly documents, which cuts both ways.** It would differentiate, and there is no market precedent that employees accept it. Read AI's reception suggests individual-level scores visible to managers are the specific trigger. Aggregate, thresholded, text-only signal is untested, not proven safe. For EU workers, inferring emotion from voice is prohibited outright.
- **The development and talent vision is where legal exposure concentrates.** It is the element that most plausibly engages EU high-risk classification, US state notice duties, and discoverability concerns. Keeping 1-on-1 signal advisory and human-confirmed, as peers do, reduces that pull.
- **Employment counsel at prospects will be a gatekeeper.** Published guidance defaults to "no notetaker" for performance matters. QW will need a clear account of why a consented, short-retention, purpose-built tool differs from a general notetaker.

### 10.2 Open questions

- Which party can see what? Specifically: can the employee see the manager's coaching, can a skip-level manager see summaries, and can HR see anything beyond meeting occurrence? Neither Lattice nor 15Five documents skip-level visibility.
- Does QW side with 15Five ("nobody can ever retrieve the transcript, even for audit") or Lattice (participants can download and delete)? The audit log in QW's draft implies the Lattice side.
- Can an employee decline, pause, or redact unilaterally, and what happens to downstream signal when they do?
- What is the retention clock for derived signals, as distinct from the transcript?
- How will speaker attribution work without persisting a voiceprint, and how will the product behave when a Teams tenant disables speaker attribution?
- What share of QW's customers already produce native transcripts on Zoom, Teams, or Meet? This determines whether ingest alone is viable. Not answerable from the notes.
- Will QW expose 1-on-1 content through an MCP server or API, given that buyers increasingly expect it and that the content is unusually sensitive?
- Can QW produce outcome evidence (action-item completion, review quality, candor) from a pilot? No competitor has published any.
- Does Lattice's Workforce Intelligence, 15Five's HR Outcomes Dashboard, or Rippling consume meeting-derived data? All three are unverified and would change the HR-dashboard conclusion.

---

## 11. Source Health and evidence quality

### 11.1 Blocked or unreachable sources

- https://help.leapsome.com — HTTP 403 on every direct fetch. Leapsome help-center facts are snippet grade. Replacements used: https://www.leapsome.com/blog/meeting-notetaker-ai-agent and https://www.leapsome.com/en/subcontractors
- https://support.betterworks.com/hc/en-us/articles/42449959219725-Meetings-NextGen — HTTP 403. Replacement: the Betterworks magazine article.
- https://help.engagedly.com/getting-started-with-meeting-agent — HTTP 503.
- https://docs.predictiveindex.com/en/articles/11954313-9-15-25-pi-meeting-notetaker-perform — HTTP 404.
- https://help.openai.com/en/articles/11487532-chatgpt-record — HTTP 403.
- https://support.read.ai — HTTP 403; https://read.ai/security — 404; https://fellow.ai/1-on-1-meetings — 404.
- The Otter order on Justia — HTTP 403; holdings are from secondary summaries.
- https://web.archive.org — not reachable from the research environment; no archived fallbacks were possible.

### 11.2 Not fetched (candidates for a follow-up pass)

- https://www.15five.com/pricing and https://success.15five.com/hc/en-us/articles/50989042213403-What-add-ons-are-available-for-15Five-plans (would settle Kona pricing).
- https://lattice.com/trust/ai-update (may name models) and Lattice's custom-role permissions article.
- Trust centers and subprocessor lists for Betterworks, PerformYard, Engagedly, Deel, Culture Amp, Workleap, Predictive Index, Otter, Fireflies, Fathom, Read AI.
- AssemblyAI, Deepgram, and Nylas customer pages.
- G2, Reddit, and Gartner Peer Insights reviews of the specific features.
- Primary legal texts: the Otter order, the EU Commission guidelines, the Digital Omnibus, German statutes, and state agency pages.

### 11.3 Main unverified areas

- **Technology vendors** are Unknown for most players. Only Lattice, 15Five, Leapsome, Granola, and Fellow (bot only) have a confirmable stack. Which LLM handles 1-on-1 transcripts specifically is not stated by any HR vendor.
- **Pricing** for 15Five is third-party only. Zoom, Microsoft, and Google prices are secondary and conflicting.
- **Governance details** for capturing HR vendors other than Lattice and 15Five: retention periods, audio storage, deletion, redaction, and audit logs are Unknown for all of them.
- **Audit logs, legal hold, BYOK, and group-level enablement** were not verified for any vendor, so the table-stakes classification is weakest there.
- **"No capture" findings** for Culture Amp, Workleap, Workday, HiBob, BambooHR, Paylocity, UKG, Qualtrics, Perceptyx, and Gallup rest on absence of evidence.
- **Shipped versus beta status** is missing for Betterworks Conversational Intelligence and PerformYard Meeting Coaching, and is contradictory for Leapsome.
- **Litigation details** for Fireflies and Microsoft come only from competitor or vendor blogs.
- **Not researched or not found:** Pando, Peoplelogic, Mirro, Small Improvements, Zelt, Effy, Rising Team, Cloverleaf, Poised, Chorus, Clari, Zoom Revenue Accelerator, Worklytics, Glean; Gartner, Forrester, and RedThread research on this topic.
- **Source-quality caution:** much 2026 coverage of notetaker lawsuits and vendor comparisons comes from competing notetaker vendors' blogs with a commercial interest in making rivals look risky. Recall.ai's and Nylas's comparison pages are likewise self-interested.
