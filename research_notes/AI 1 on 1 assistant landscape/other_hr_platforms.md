# AI for 1-on-1 meetings at HR / performance / EX platforms other than Lattice and 15Five (current state, 2026-11-17)

Research notes. Scope: Leapsome, Culture Amp, Betterworks, Workleap, Engagedly, PerformYard, Predictive Index, Microsoft Viva, Workday, BambooHR, Rippling, HiBob, Deel Engage, Paylocity, UKG, Qualtrics, Perceptyx, Gallup.

Conventions used in these notes:
- Every fact carries a plain https:// URL. "Unknown" = could not be verified from a source; not a guess.
- Evidence grade tags: [FETCHED] = page was opened and read in this run; [SNIPPET] = taken from a search-index snippet only (page not opened, or blocked); [CLAIM] = vendor marketing claim, not independently verified.
- Access limits (see also "Source Health" at the end): help.leapsome.com and support.betterworks.com returned HTTP 403 to direct fetches; web.archive.org is not reachable from this environment; help.engagedly.com returned 503. Those vendors' help-center facts are therefore [SNIPPET] grade.

Quick classification (detail and sources in the sections below):
- Captures 1:1 conversation content natively (shipped or beta): Leapsome (desktop system audio / in-browser tab audio / pasted transcript), Betterworks (Zoom API transcript retrieval + paste/upload), PerformYard (Zoom/Teams transcript retrieval), Predictive Index (caption-reading meeting bot, beta, product being retired), Engagedly (Marissa Notetaker agent that joins Google/Microsoft conferences), Deel Engage (Google Meet transcript fetch).
- No verified 1:1 transcript capture; AI applied to 1:1s via other data: Culture Amp, Workleap, Workday, Rippling, HiBob, BambooHR, Perceptyx, Qualtrics, Gallup, Paylocity, UKG.
- Special case: Microsoft (capture lives in Teams/Copilot, not in Viva).

---

## 1. Does the vendor capture 1:1 conversation content, and how?

### Takeaway
Six of the eighteen vendors have a verified transcript-capture path for 1:1s, and the dominant pattern outside Lattice/15Five is NOT a visible meeting bot: Leapsome uses desktop system-audio and in-browser tab-audio capture, Betterworks and PerformYard pull the native Zoom (and for PerformYard, Teams) transcript after the meeting, and Deel pulls the Google Meet transcript. Only Predictive Index (beta, caption-scraping bot) and Engagedly (notetaker agent that must be admitted) use a join-the-call participant.

### Cited Findings

Leapsome (priority 1)
- Three capture methods are documented: a Mac desktop app, in-browser transcription, and pasting a transcript manually. The desktop app is macOS only. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/36398991260445-Different-transcription-methods
- The Mac app transcribes through system audio, so meetings held in Zoom, Google Meet or Teams can be captured without a per-platform integration. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/36389064496413-Leapsome-desktop-app-for-meeting-transcription-Mac
- In-browser flow: user grants microphone access and selects the browser tab to share audio from, then confirms participant consent to start. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/30845206461597-Meetings-in-browser-transcription
- Pasted transcripts from another tool are supported; because Leapsome is not recording, the consent flow does not apply to that route. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/36398991260445-Different-transcription-methods
- Marketing blog says the Meeting Notetaker "joins the call", runs on "the desktop app or any browser", and covers 1:1s, team meetings and project syncs. [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- Conflict to note: the blog's "joins the call" wording is not matched by the help center, which lists only desktop system audio, in-browser tab audio and paste; no meeting-bot participant method was found in help-center snippets. https://www.leapsome.com/blog/meeting-notetaker-ai-agent ; https://help.leapsome.com/hc/en-us/articles/36398991260445-Different-transcription-methods
- Status: blog says "The Meeting Notetaker is live in Leapsome today" [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent ; a help-center snippet shows the admin toggle is still labelled "Meetings - (beta) transcription" in the Feature Access Matrix. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/30845027133213

Culture Amp (priority 2)
- No transcript, recording, or video-platform integration is described in the 1-on-1 Conversations help article; the only integrations are calendar (Google, Outlook, iCal) and Slack/Teams reminders. [FETCHED] https://support.cultureamp.com/en/articles/9258377-1-on-1-conversations
- Searches of cultureamp.com and support.cultureamp.com returned no notetaker/transcript feature for 1-on-1s. Treat as "does not have 1:1 transcript capture" as of this run (absence of evidence; not a vendor statement). https://support.cultureamp.com/en/articles/9258377-1-on-1-conversations

Betterworks (priority 3)
- "Conversational Intelligence": for Zoom 1:1s, completed meeting transcripts are retrieved through the Zoom API and matched to the corresponding 1:1 in Betterworks. FAQ: "No. Betterworks does not use a transcription bot for Zoom." [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Users can also upload or paste transcripts, notes, or summaries from other meeting/transcription tools. [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Teams and Google Meet native retrieval are not mentioned on that page (published 2026-09-10). [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Press coverage describes the feature as analyzing transcripts "from meeting transcription applications" used in manager-employee discussions. [SNIPPET] https://itbrief.co.uk/story/betterworks-adds-ai-tools-to-boost-workforce-readiness

Workleap (Officevibe / Workleap Performance) (priority 4)
- The 1:1 agent page describes scheduling, briefs, agendas and completion tracking; it does not mention transcribing or recording meetings. [FETCHED] https://workleap.com/lp/meeting-automation
- Officevibe one-on-ones page describes manually kept notes with previous notes, recognition and goals available in the meeting; no transcript. [SNIPPET] https://officevibe.com/one-on-ones
- Treat as "does not have 1:1 transcript capture" as of this run (absence of evidence).

Engagedly (priority 5)
- "Marissa AI Notetaker" captures meeting notes and summaries; per the product-page FAQ it can join meetings and organizers decide whether to admit it (i.e., a join-the-call participant). [FETCHED] https://engagedly.com/product/meetings/
- When scheduling a one-on-one, "Marissa Notetaker" can be enabled only if admins enabled it for the organization and the meeting type is "Google Conference" or "Microsoft Conference". [SNIPPET] https://help.engagedly.com/schedule-one-on-one-meeting-1
- Zoom support: Unknown (not named in the sources found). Whether a verbatim transcript is stored or shown: Unknown.

PerformYard (priority 6)
- Users connect a Zoom or Microsoft Teams account to auto-generate meeting links and "capture transcripts once a meeting ends, no manual uploading required". [SNIPPET] https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup
- Admins can disable "Video Conferencing & Transcripts", which stops existing meetings from automatically retrieving transcripts. [SNIPPET] https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup
- Google Meet transcript retrieval: not found (Google appears only as a calendar integration). [SNIPPET] https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup
- Mechanism is retrieval of the conferencing provider's transcript via the linked user account, not a PerformYard bot (inference from the wording "automatically retrieving transcripts"; no bot is described). https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup

Predictive Index — PI Perform (priority 7)
- "PI Meeting Notetaker" is in beta ("may be changed or removed in the future"), opt-in per meeting from a Perform workspace ("Invite PI Meeting Notetaker"). [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker
- It joins Zoom, Microsoft Teams and Google Meet as a normal meeting participant (anonymous join on Teams; only teams.microsoft.com links; Zoom webinars unsupported). [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker
- It does not record audio or video; it uses the captions from the video-conferencing tool to produce notes. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker
- Important current-state context: the same article states Perform and Diagnose are retiring on 2027-09-30 and admins should export data. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker

Microsoft Viva / Teams Copilot (priority 8)
- Capture lives in Teams, not Viva: Copilot in Teams meetings works from the meeting transcript / speech-to-text data and meeting chat. [SNIPPET] https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1
- Microsoft has a message-center item for "AI meeting recap without transcript to meet compliance policies" (summaries generated without saving transcript or recording; tenant-wide admin control). Rollout timing conflicts between mirrors (late July 2026 vs October 2026). [SNIPPET] https://mc.merill.net/message/MC1275312 ; https://www.itelio.com/en/microsoft-message-center/MC1275312
- Viva's role is measurement of recap usage (Copilot Dashboard / Viva Insights "meetings recapped" metrics), not capture. [SNIPPET] https://mc.merill.net/message/MC1085574
- No dedicated Viva/Copilot "manager 1:1" product was found; a Microsoft community post (April 2026, no replies) reports Copilot did not produce a structured 1:1 agenda or flag open action items from prior meetings. [SNIPPET] https://techcommunity.microsoft.com/discussions/microsoft365copilot/using-copilot-to-help-with-11-meeting-prep-for-managers/4508256
- Viva Goals was retired 2025-12-31, removing the Viva module closest to performance workflows. [SNIPPET] https://learn.microsoft.com/en-gb/viva/goals/goals-retirement

Workday (Peakon, agents) (priority 9)
- Sana Coach page mentions no meeting transcript or recording capture. [FETCHED] https://www.workday.com/en-gb/ai-agents/sana/coach.html
- No source found describing 1:1 transcript capture in Workday Peakon Employee Voice. Treat as "does not have" (absence of evidence).

Lower-priority vendors (short statements)
- Deel Engage: HAS capture. "After a Google Meet call ends, Checkins automatically fetches the transcript"; only Google Meet is named; no bot or recording is described; "The raw transcript is always one tab away." [FETCHED] https://www.deel.com/solutions/engage/one-on-one-meetings/
- Rippling: No verified 1:1 transcript capture. Rippling 1:1s is a doc-style notes editor with templates, action items, goals and past feedback. [SNIPPET] https://www.rippling.com/blog/introducing-1-1s ; https://www.rippling.com/products/hr/performance-management . Rippling's native recording/transcription is in Recruiting (Interview Assistant), per a third-party blog. [SNIPPET, third party] https://interviewersignal.com/blog/ai-notetaker-for-rippling
- HiBob: No verified 1:1 transcript capture. HiBob's AI is described as summarizing reviews, drafting feedback and goals, and surfacing survey themes. [SNIPPET] https://www.hibob.com/platform/talent/performance-management/ . Note: "HeyBob" (heybob.ai) is an unrelated notetaker product, not HiBob. https://heybob.ai/meetings/
- BambooHR: No native 1:1 transcript capture or 1:1 AI summary found; only third-party agents/integrations surfaced (e.g., Arahi, Noota for interviews). [SNIPPET, third party] https://arahi.ai/ai-agent/bamboohr/meeting-notes ; https://www.noota.io/integrations/bamboohr
- Paylocity: No 1:1 transcript capture found; AI pages describe the AI Assistant and predictive insights. [SNIPPET] https://www.paylocity.com/products/capabilities/ai/
- UKG: No 1:1 transcript capture found; Bryte AI is described as an HR/workforce assistant. [SNIPPET] https://secure.businesswire.com/news/home/20251104883551/en/UKG-Bryte-AI-Revolutionizes-How-Employees-Find-Help-and-Information
- Qualtrics: No 1:1 transcript capture found; Manager Assist works from survey/open-text and other listening data. [SNIPPET] https://www.qualtrics.com/articles/news/qualtrics-announces-manager-assist-empowering-managers-to-own-their-teams-engagement-and-success/
- Perceptyx: No 1:1 transcript capture found; Activate delivers nudges and an AI Coach in Teams/Slack/email. [SNIPPET] https://blog.perceptyx.com/how-perceptyx-uses-ai-nudges-to-drive-behavior-change-at-scale
- Gallup: No 1:1 transcript capture found; "Gallup AI" in Gallup Access helps users prepare for one-on-one conversations. [SNIPPET] https://support.gallup.com/hc/en-us/articles/48408264183827-Gallup-AI

### Inferences
- The "botless" route is the majority pattern among performance-suite competitors that capture 1:1s (Leapsome, Betterworks, PerformYard, Deel). It trades a visible consent signal (bot in the participant list) for lower friction, and pushes consent handling to either an explicit in-app flow (Leapsome) or to the conferencing platform's own transcription notice (Betterworks, PerformYard, Deel — inferred, since those vendors rely on the platform's native transcript).
- Native-transcript ingestion makes capture dependent on the customer's Zoom/Teams/Meet licence and admin settings for transcription; single-platform coverage (Betterworks = Zoom; Deel = Google Meet; PerformYard = Zoom + Teams) is a visible gap versus system-audio capture (Leapsome) or a multi-platform bot (PI).
- "Paste/upload a transcript" (Leapsome, Betterworks) is a cheap universal fallback that also covers in-person or third-party-notetaker cases.
- No vendor in this set was found to document mobile / in-person recording for 1:1s (Leapsome's in-browser microphone flow may technically cover it, but that is not stated).

### Gaps
- Leapsome: could not open help-center articles (HTTP 403), so the exact relationship between "Meeting Notetaker agent" (blog) and "meeting transcription (beta)" (help center), and whether any bot-join method exists, is unresolved.
- Engagedly: "Manage the notetaker agent for meetings" help article not retrieved (503); Zoom support and transcript storage Unknown.
- Culture Amp, Workleap, Workday, HiBob, Rippling, BambooHR, Paylocity, UKG, Qualtrics, Perceptyx, Gallup: "no capture" is based on absence in vendor pages/search results, not on an explicit vendor statement.
- Microsoft: no Microsoft Learn page was found (in this run) that describes a Viva-branded manager 1:1 workflow; the People/HR agent landscape in M365 Copilot was not verified.

---

## 2. Underlying technology: bot/transcription vendors and LLM providers

### Takeaway
Only Leapsome's stack is confirmable from a public subprocessor list (OpenAI, AWS Bedrock/SageMaker, Google Vertex AI, Cloudflare Workers AI; no speech-to-text or meeting-bot vendor listed). For every other vendor the transcription/bot vendor and LLM provider are Unknown from public sources; several avoid a third-party recorder entirely by consuming Zoom/Teams/Meet-native transcripts or captions.

### Cited Findings
- Leapsome subprocessors (Annex III of DPA), AI Services section — CONFIRMED: OpenAI Ireland Ltd. (generative AI for smart features; US), Amazon Web Services EMEA (Bedrock, SageMaker AI; global nearest/best-performing data center), Google Cloud EMEA (Vertex AI; global), Cloudflare (Workers AI; generative AI, MCP server, CDN), turbopuffer (vector database; EEA Germany), LangChain LangSmith (observability/prompt evaluation; EEA Netherlands), Datadog AI Observability (EEA Germany). Core hosting: AWS and MongoDB in Germany. [FETCHED] https://www.leapsome.com/en/subcontractors
- Leapsome: no transcription, speech-to-text, or meeting-recording subprocessor (Recall.ai, AssemblyAI, Deepgram, etc.) appears on that list. Nylas is listed, but only as the recruiting email connector. [FETCHED] https://www.leapsome.com/en/subcontractors
- Leapsome's subprocessor list lists Cloudflare as providing an "MCP server", confirming MCP infrastructure exists. [FETCHED] https://www.leapsome.com/en/subcontractors
- Betterworks: transcript source is the Zoom API (CONFIRMED by vendor); LLM provider not named ("uses AI"). [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- PerformYard: transcript source is the user's linked Zoom or Teams account (CONFIRMED by vendor snippet); LLM provider not named — the AI page says only "PerformYard's models are optimized for the specific language and tone" of performance management. [SNIPPET] https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup ; [FETCHED] https://www.performyard.com/ai
- Predictive Index: notetaker uses the conferencing tool's own captions (so no separate speech-to-text is needed); bot vendor and LLM not named. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker
- Deel: transcript source is Google Meet (CONFIRMED by vendor); LLM not named. [FETCHED] https://www.deel.com/solutions/engage/one-on-one-meetings/
- Engagedly: bot/transcription vendor and LLM not named on the product page. [FETCHED] https://engagedly.com/product/meetings/
- Recall.ai's HR solutions page shows logos for Rippling, Deel, 15Five, Fellow, Leadr, ClearCompany and BrightHire; Rippling and Deel are listed under "Used By" for the Meeting Bot API. Leapsome, Culture Amp, Engagedly, PI and Betterworks are NOT named on that page. [FETCHED] https://www.recall.ai/solutions/hr
- Microsoft: Copilot in Teams uses Microsoft's own speech-to-text/transcript pipeline. [SNIPPET] https://support.microsoft.com/en-us/office/get-started-with-copilot-in-microsoft-teams-meetings-0bf9dd3c-96f7-44e2-8bb8-790bedf066b1

### Inferences
- Leapsome's absence of a speech-to-text subprocessor, combined with AWS/Google/OpenAI/Cloudflare AI services being listed, suggests transcription runs on one of those listed AI platforms (e.g., a hosted speech model) or on-device in the desktop app. INFERRED, not confirmed; which one is Unknown.
- Rippling and Deel being Recall.ai Meeting Bot API customers does not establish that their 1:1 products use Recall: Rippling's known recorder is the Recruiting Interview Assistant, and Deel's Checkins page describes fetching the Google Meet transcript rather than a bot. Which Rippling/Deel products use Recall is Unknown. (The Recall page copy about generating notes and performance insights from 1:1 content reads as generic solution copy; do not attribute it to a specific customer without checking the page manually.)
- PI's caption-scraping design is characteristic of a third-party meeting-bot API, but no vendor is named; attribution is Unknown.

### Gaps
- LLM providers for Betterworks, PerformYard, Engagedly, PI, Deel, Culture Amp (AI Coach), Workleap: not found in pages opened this run. Trust centers / subprocessor lists for these vendors were not fetched (budget) — a follow-up should check: betterworks.com trust/subprocessors, performyard.com security/privacy pages, engagedly.com trust, deel.com subprocessors, cultureamp.com subprocessors, workleap.com trust.
- Infrastructure-vendor customer pages for AssemblyAI, Deepgram and Nylas were not checked for these HR vendors.
- Leapsome subprocessor page has no visible version date.

---

## 3. Downstream use of transcript-derived data (shipped vs beta vs announced)

### Takeaway
Among capturing vendors, the furthest downstream reach is Leapsome (review pre-drafts from recent 1:1s, goal-linked tasks, a Development Coach with meeting-quality summaries) and PerformYard (admin-configurable manager coaching including speaking-time and monologue analysis, plus org-level 1:1 summaries for HR). Betterworks routes transcript signals into goals with human confirmation; Deel positions transcripts as a year-long evidence base for reviews. No vendor in this set was found to publish a transcript-derived sentiment/risk dashboard for HR.

### Cited Findings

Leapsome
- Outputs: structured summaries (discussion points, decisions, open questions), action items with owner and deadline that become tracked tasks linked to goals, 1:1 talking points or projects; a searchable record attached to the meeting. [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- Help center: after a meeting ends Leapsome generates an AI summary, action items and talking points saved directly to the relevant meeting. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/36389064496413-Leapsome-desktop-app-for-meeting-transcription-Mac
- Reviews: "pre-writes a review draft based on recent 1:1s" for employees and managers to revise. [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- Coaching: "Development Coach" surfaces coaching opportunities and prompts managers to share feedback; participants see an engagement summary covering meeting quality, preparation, open questions and clarity of outcomes. [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- HR/admin analytics on meeting data: not mentioned. [FETCHED] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- MCP: Cloudflare is listed as providing an "MCP server" in the subprocessor list; whether meeting transcripts are exposed through it is Unknown. [FETCHED] https://www.leapsome.com/en/subcontractors

Betterworks
- Generated: meeting recap, suggested action items and agenda topics, goal-progress identification with suggested milestone updates, potential new goal opportunities, and a private "AI Meeting Prep" brief for future 1:1s drawing on recent meetings, open action items and current goals. [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- AI recommendations stay pending until a user reviews and confirms; users can edit or discard them before they enter Betterworks records. [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Feedback, reviews and "talent intelligence" are named as areas that become more useful when connected, but no specific mechanism is described; HR analytics/dashboards from transcripts are not described. [FETCHED][CLAIM] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- GA/beta status: not stated on the page (published 2026-09-10). https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes

PerformYard
- "Meeting Coaching" AI Coach inputs: meeting transcripts, agendas, notes and action items, plus employee goals, performance reviews, feedback and survey results. [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup
- Post-meeting analysis sections (each admin-toggleable): Decisions Made; Missed Commitments (action items from transcript and notes); Participation & Inclusion (speaking-time distribution); Quality of Discussion vs. Monologue; Time Management (planned agenda vs actual flow); Meeting Coaching (Top Strength, Primary Development Area, One Thing to Try Next Meeting). [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup
- Pre-meeting prep sections (admin-toggleable): Suggested Agenda Items, Goals For Discussion, Recent Feedback (past 30 days), Recent Reviews, Survey Insights; uses a recap of the previous three meetings. [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup
- HR/admin level: AI "summarizes 1:1 meetings for individuals, teams, or the entire organization"; examples include "Surfacing themes from 1:1 meeting notes" and "Parsing 1:1 meeting notes into coaching themes"; "Meeting notes inform goals; review outcomes feed comp and growth plans." [FETCHED][CLAIM] https://www.performyard.com/ai
- MCP: a product update adds MCP access so users can query goals, meetings, feedback, completed reviews and saved reports through connected AI assistants, and prepare for 1:1s / add agenda items from the assistant. [SNIPPET] https://www.performyard.com/ (exact page not opened; verify)
- Disclaimer in help article: AI output should be human-reviewed and not be the sole basis for employment decisions. [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup

Predictive Index
- Output is a meeting summary, suggested action items (accept/reject before they go live) and a more detailed outline, stored in the workspace History tab. No downstream feed into reviews/goals is described. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker

Engagedly
- Notetaker produces meeting notes and summaries; users can review and add AI-suggested tasks based on meeting discussions. No feed into other modules is described on the product page. [FETCHED] https://engagedly.com/product/meetings/
- Marissa AI can generate "meeting reflections" from discussion points and notes; the meetings agent summarizes key notes and supports search by topic/keyword. [SNIPPET] https://help.engagedly.com/add-and-manage-meeting-reflections ; https://help.engagedly.com/getting-started-with-meeting-agent

Deel Engage (Checkins)
- AI extracts "key points and commitments" from the Google Meet transcript and populates notes and action items; AI-suggested talking points from unresolved items; one-click session summary "useful for async follow-up or review prep". [FETCHED] https://www.deel.com/solutions/engage/one-on-one-meetings/
- Reviews: "By the time review season opens, managers have a full year of documented conversations ready to summarize." FAQ: conversations "connect directly to goals, reviews, and development plans" and the 1:1 "contributes to a worker's growth and compensation trajectory" (no mechanism given). [FETCHED][CLAIM] https://www.deel.com/solutions/engage/one-on-one-meetings/

Microsoft
- Teams intelligent recap provides AI notes, chapters and suggested tasks; M365 Copilot adds in-meeting/after-meeting chat. [SNIPPET, third party] https://www.leadwithai.co/guides/copilot-teams-meetings
- No documented flow from Teams 1:1 transcripts into Viva (Glint/Insights) HR-facing people analytics was found; Viva Insights reports aggregate recap usage counts. [SNIPPET] https://mc.merill.net/message/MC1085574

### Inferences
- Transcript-to-review-draft is now table stakes messaging among capturing vendors (Leapsome explicit; Deel and Betterworks implied), but only Leapsome states an actual pre-drafted review from recent 1:1s.
- PerformYard is the clearest example in this set of transcript-derived manager-effectiveness coaching (talk-time, monologue, missed commitments) with admin-configurable sections — the closest analogue to a "coach the manager" capability for QW's concept.
- Human-in-the-loop confirmation before AI output becomes a system record (Betterworks pending recommendations; PI accept/reject action items; PerformYard disclaimer) is a common design pattern.
- None of the vendors publicly documents transcript-derived sentiment, attrition-risk or engagement signals surfaced to HR. This is either an unoccupied space or a deliberately avoided one (trust risk).

### Gaps
- Shipped vs beta labels are missing for Betterworks Conversational Intelligence and PerformYard Meeting Coaching.
- Whether Leapsome's review pre-draft uses raw transcripts or only the AI summaries is Unknown.
- API/MCP exposure of transcripts specifically (as opposed to meetings metadata) is Unknown for Leapsome and PerformYard.
- Recognition and development-plan feeds from transcripts: not found at any vendor (Deel claims a development-plan connection without mechanism).

---

## 4. Vendors without transcript capture: what AI they apply to 1:1s and what feeds it

### Takeaway
Non-capturing vendors apply AI before and around the conversation rather than to it: agenda/brief generation from survey, feedback and goal data (Workleap, Culture Amp Enso), conversational coaching chatbots (Culture Amp AI Coach, Perceptyx AI Coach, Gallup AI, Workday Sana Coach), and assistant/MCP access to 1:1 objects (Culture Amp, PerformYard). Their input data is structured platform data, not conversation content.

### Cited Findings

Culture Amp
- 1-on-1 Conversations contains agenda topics (carry over if unchecked), admin "Assigned Topics" targeted by role/team/location (not editable by managers/employees), action items, check-in sliders, "Highlights & challenges", and personal notes. No AI is described in this article. [FETCHED] https://support.cultureamp.com/en/articles/9258377-1-on-1-conversations
- AI Coach is a conversational coaching interface; in Performance it offers a confidential space to gather thoughts, role-play and draft follow-ups; summaries it produces are of the chat itself, not of a meeting. [SNIPPET] https://support.cultureamp.com/en/articles/12331162-ai-coach-in-performance ; https://www.cultureamp.com/platform/ai-coach
- MCP connector (Claude and ChatGPT tested): 1-on-1s is the only read/write area — assistants can read agendas, add topics or notes and manage action items, limited to conversations the user belongs to; Engagement and Performance data are read-only; access follows role permissions. Available on any subscription at no additional cost "today", subject to per-organization registration/approval and an admin "Activate MCP" toggle. [FETCHED] https://support.cultureamp.com/en/articles/16754009-connect-claude-or-chatgpt-to-your-1-on-1-conversations-via-mcp
- A search snippet for the same article states the assistant sees topics and action items but not the text of notes already saved on them. [SNIPPET; not confirmed in the fetched summary] https://support.cultureamp.com/en/articles/16754009-connect-claude-or-chatgpt-to-your-1-on-1-conversations-via-mcp
- "Enso by Culture Amp" (announced 2026-10-27) is described as an agentic partner that can prepare 1:1 agendas and talking points, schedule huddles and follow up on commitments, with leader approval per action or by permission; first available in Slack, Claude and ChatGPT. [SNIPPET][CLAIM; announced] https://www.cultureamp.com/company/announcements/enso-by-culture-amp-news ; https://www.cultureamp.com/blog/enso-brings-culture-amp-mission-to-agentic-era

Workleap
- Agent "books the meetings, prepares the briefs, tracks completion"; "The agent pulls check-ins, pulse signals, and feedback data to build a personalized agenda for each employee meeting"; HR gets a live view of completion rates, cadence and engagement trends. GA/beta status and pricing not stated. [FETCHED][CLAIM] https://workleap.com/lp/meeting-automation
- Workleap blog: live engagement signals feed 1:1 agendas, and managers are prompted if an employee's pulse responses indicate a dip in morale. [SNIPPET] https://workleap.com/blog/best-1-on-1-meeting-tools

Workday
- Sana Coach agents: Talent Sentiment (signals from Workday Peakon Employee Voice) and Performance Review (drafts from Workday data, user-uploaded documents and supported third-party signals) are listed without a "coming soon" label; Feedback, Leadership Coaching and Goals & Check-Ins are labelled "Coming soon". Goals & Check-Ins is described as managing goal alignment and automated check-ins. [FETCHED] https://www.workday.com/en-gb/ai-agents/sana/coach.html
- Performance Review drafts accept "user-uploaded documents" — a possible manual route for meeting notes/transcripts, but transcripts are not named. [FETCHED] https://www.workday.com/en-gb/ai-agents/sana/coach.html

Rippling
- 1:1s: templates powered by HRIS data, doc-style notes editor, action items, goals and past feedback shown in-meeting. A Rippling resource offers AI prompts that build a 1:1 agenda from recent meetings, Slack messages and open follow-ups (marketing guide; not confirmation of a native 1:1 AI feature). [SNIPPET] https://www.rippling.com/blog/introducing-1-1s ; https://www.rippling.com/resources/hiring-performance-ai-prompts-eoy

HiBob
- AI helps summarize reviews, draft feedback and goals, and surface survey themes; nothing specific to 1-on-1 conversations found. [SNIPPET] https://www.hibob.com/platform/talent/performance-management/

Perceptyx
- Activate (built on the Humu foundation acquired in 2023) delivers nudges in Teams, Slack and email; AI Coach (launched 2025-04-02) gives conversational coaching personalized to the manager's goals and team feedback, including role-play for difficult conversations and tailored questions to use in a meeting; admin dashboard shows aggregate coaching engagement over 90 days. [SNIPPET] https://blog.perceptyx.com/how-perceptyx-uses-ai-nudges-to-drive-behavior-change-at-scale ; https://blog.perceptyx.com/grow-smarter-unlock-greater-leadership-potential-with-ai-coach ; https://perceptyxhelp.freshdesk.com/support/solutions/articles/63000285950

Qualtrics
- Manager Assist provides AI-supported views and coaching from survey results, open-text comments and continuous listening; no 1:1 meeting tool or conversation guide confirmed. [SNIPPET] https://www.qualtrics.com/articles/news/qualtrics-announces-manager-assist-empowering-managers-to-own-their-teams-engagement-and-success/

Gallup
- "Gallup AI" (included with a Gallup Access subscription) can be used to prepare for one-on-one conversations or team meetings, explore strengths and generate development ideas, drawing on Gallup research rather than outside internet sources. [SNIPPET] https://support.gallup.com/hc/en-us/articles/48408264183827-Gallup-AI

BambooHR, Paylocity, UKG
- No 1:1-specific AI found in this run (see section 1 for the general AI pages). https://www.paylocity.com/products/capabilities/ai/ ; https://secure.businesswire.com/news/home/20251104883551/en/UKG-Bryte-AI-Revolutionizes-How-Employees-Find-Help-and-Information

### Inferences
- Survey-led vendors (Culture Amp, Workleap, Perceptyx, Qualtrics, Gallup) differentiate on feeding listening/engagement signals into the 1:1 agenda or into manager coaching — the inverse direction of QW's proposed flow (conversation signals out to the platform). A QW assistant could plausibly do both directions.
- Culture Amp's strategy as of November 2026 is "meet users in their assistant" (MCP into Claude/ChatGPT, Enso in Slack) rather than own the meeting capture. A user could pair a general-purpose notetaker with the MCP connector to write notes and action items into Culture Amp 1-on-1s; this is an inference, not a documented workflow.
- Workday's coming-soon Goals & Check-Ins agent indicates the enterprise HCM suites are approaching check-ins via agents on structured data, not via transcript capture.

### Gaps
- Culture Amp Enso availability (GA vs staged) and exact 1:1 capabilities not verified by opening the announcement page.
- Whether Workleap's agent is GA and how it is priced.
- BambooHR, Paylocity, UKG: product documentation for performance/1:1 modules was not opened; statements rest on search results only.

---

## 5. Visibility: who can see transcripts, summaries and derived insights

### Takeaway
Published visibility rules are thin. Where stated, the default is participant-scoped: Leapsome says existing permissions apply, PI restricts summaries to workspace members, Betterworks prep briefs are private per participant, Deel keeps the raw transcript one tab away inside the check-in. HR-level visibility of transcript-derived content is explicitly claimed only by PerformYard (org-wide 1:1 summaries) and, for non-transcript 1:1 metadata, by Workleap.

### Cited Findings
- Leapsome: "Permissions stay as configured"; the notetaker "only surfaces information the user can already see"; the transcript is accessible in the meeting itself. [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent ; [SNIPPET] https://help.leapsome.com/hc/en-us/articles/36389064496413-Leapsome-desktop-app-for-meeting-transcription-Mac
- Betterworks: AI Meeting Prep briefs are "private" to each participant; visibility of recaps, transcripts and recommendations beyond that is not specified. [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- PerformYard: managers generate pre- and post-meeting coaching content; who else can view it is not stated in the setup article. HR/admins are described as getting a high-level view of accomplishments and key discussions across teams. [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup ; [FETCHED][CLAIM] https://www.performyard.com/ai
- Predictive Index: "Only members of a specific workspace can access AI summaries generated in that workspace"; summaries are not shared outside unless a user copies them. A chip shows the notetaker is in use. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker ; PI marketing says Perform sends automated meeting summaries to all participants. [SNIPPET] https://predictiveindex.com/software/perform
- Engagedly: users' own notes can be private or shared with participants; whether AI-generated notes follow the same rule is not stated. [FETCHED] https://engagedly.com/product/meetings/
- Deel: private notes are "Visible only to the author"; shared agenda is co-built; employees can browse past sessions; "The raw transcript is always one tab away" (which roles can open it is not stated). [FETCHED] https://www.deel.com/solutions/engage/one-on-one-meetings/
- Culture Amp: Personal Notes "are visible only to the author (manager or individual contributor)"; topics, action items and check-ins are visible to both participants; admin visibility is not addressed in the article. [FETCHED] https://support.cultureamp.com/en/articles/9258377-1-on-1-conversations
- Workleap: "HR gets a live view of every 1:1 across the organization" (completion, cadence, engagement trends — not conversation content). [FETCHED][CLAIM] https://workleap.com/lp/meeting-automation
- Workday Sana Coach: drafts stay "in the manager's hands", with citations back to source; feedback responses are synthesised into themes preserving rater anonymity. [FETCHED] https://www.workday.com/en-gb/ai-agents/sana/coach.html

### Inferences
- No vendor in this set publicly states that HR admins can read 1:1 transcripts. Vendors appear to avoid stating HR access either way; an explicit "HR cannot read transcripts; HR sees only aggregated/opt-in signals" position would be differentiating and is currently unclaimed.
- PerformYard's org-level 1:1 summaries are described in terms of "meeting notes", so it is unclear whether transcript content flows into HR-level summaries.

### Gaps
- Leapsome's Meetings "Visibility & Access Rights" help article exists but could not be opened (403). https://help.leapsome.com/hc/en-us/sections/4408851223441-Meetings
- HR-admin and skip-level access to transcripts: Unknown for all capturing vendors.
- Whether employees (direct reports) can see manager-coaching outputs at PerformYard or Leapsome's Development Coach output: Unknown beyond Leapsome's "participants see an engagement summary" claim.

---

## 6. Governance: consent, opt-out, retention, audio storage, deletion, editing, model training, residency

### Takeaway
Leapsome has the most explicit consent mechanism found (host must either play an automated consent audio message or tick a box confirming verbal consent before transcription starts) and states no training on customer data. Vendors that ingest native platform transcripts publish essentially nothing about consent, retention or deletion for that data. Retention periods, audio storage and transcript editing/redaction are Unknown for every vendor in this set.

### Cited Findings

Leapsome
- Consent: before transcription starts the host confirms consent either by playing an automated consent audio message to participants (if an admin has enabled it) or by checking a box stating all participants have given verbal consent; the host can replay the consent audio at any time. [SNIPPET] https://help.leapsome.com/hc/en-us/articles/36397795997341 (consent article, one of several in the "Meeting transcription in Leapsome" section) ; section index https://help.leapsome.com/hc/en-us/sections/36396613572765-Meeting-transcription-in-Leapsome
- Marketing: "Before recording starts, all participants get a clear notice for compliance"; admins control recording, retention and which meetings it joins. [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- Admin enablement: transcription is enabled per role in Settings > Employees > Feature Access Matrix > AI Features > "Meetings - (beta) transcription". [SNIPPET] https://help.leapsome.com/hc/en-us/articles/30845027133213
- AI can be disabled entirely by admins; turning AI off immediately stops AI processing. Two help articles describe the control location differently (a super-admin "Automatically enable AI features" toggle vs the Feature Access Matrix). [SNIPPET] https://help.leapsome.com/hc/en-us/articles/38176995079709-AI-in-Leapsome-Overview-Settings ; https://help.leapsome.com/hc/en-us/articles/30192934732061-Understanding-Leapsome-AI-and-controlling-AI-settings
- Model training: "No training on your data: Your data is never used to train AI models"; data encrypted in transit and at rest. [SNIPPET][CLAIM] https://help.leapsome.com/hc/en-us/articles/38176995079709-AI-in-Leapsome-Overview-Settings
- Residency: core platform hosting in Germany (AWS, MongoDB); AI processing via OpenAI is listed as US and AWS Bedrock / Google Vertex / Cloudflare Workers AI as global "nearest or best-performing data center". [FETCHED] https://www.leapsome.com/en/subcontractors
- Audio stored or not, retention period, transcript deletion/editing: Unknown (not in any snippet; pages blocked).

Betterworks
- Human confirmation gate on AI recommendations; consent requirements for transcript use, retention and deletion are not addressed on the product page. [FETCHED] https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes

PerformYard
- Company-level switch for "Video Conferencing & Transcripts"; per-user account linking; admin toggles for each coaching section. [SNIPPET] https://support.performyard.com/article/336-calendar-and-video-conferencing-integration-setup ; [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup
- HR admins can exclude specific words or phrases from AI output and turn review-summary content on or off (general AI controls). [FETCHED] https://www.performyard.com/ai
- Consent and retention: not addressed in the setup article. [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup

Predictive Index
- Opt-in per meeting; no audio or video recorded, no visual input captured; summaries cannot be edited; pause/resume not supported; no consent announcement described beyond the bot's presence as a participant and an in-use chip; retention not specified. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker

Engagedly
- "Admins control whether the notetaker is available to the organization"; organizers enable/disable it per meeting and decide whether to admit it. No consent, recording-notice or retention statements on the product page. [FETCHED] https://engagedly.com/product/meetings/

Deel
- Consent, retention and deletion are not addressed on the Checkins page; sessions are generated automatically for every manager–direct report pair once Checkins is enabled. [FETCHED] https://www.deel.com/solutions/engage/one-on-one-meetings/

Culture Amp (non-capture)
- MCP: admin-activated, organization registration required, turning it off immediately revokes access org-wide, acts with the individual user's permissions. [FETCHED] https://support.cultureamp.com/en/articles/16754009-connect-claude-or-chatgpt-to-your-1-on-1-conversations-via-mcp
- AI Coach conversations are stored within the Culture Amp platform to allow anonymized analysis that helps improve AI Coach. [SNIPPET] https://www.cultureamp.com/platform/ai-coach

Microsoft
- Tenant-wide admin controls for Teams AI recap; a "recap without transcript" mode exists/rolls out for compliance-sensitive tenants (timing conflict noted in section 1). [SNIPPET] https://mc.merill.net/message/MC1275312

### Inferences
- Vendors relying on Zoom/Teams/Meet-native transcripts effectively delegate the notice-and-consent step to the conferencing platform's own "transcription started" notification and to the customer's conferencing admin policy. None of them says so explicitly.
- "No audio/video stored" (PI) and "no bot" (Betterworks) are used as trust signals; Leapsome leads with explicit consent and "no training". A QW assistant would be compared against all three messages.
- Retention configurability is claimed only by Leapsome (admin-controlled, no numbers).

### Gaps
- Retention periods, audio storage, deletion, transcript editing/redaction, and audit logs: Unknown for all vendors (not found on any page opened).
- Certifications (SOC 2, ISO 27001) and DPA terms specific to transcript data: trust centers were not opened in this run.
- Leapsome's legal/jurisdictional guidance for all-party-consent regimes: not found.

---

## 7. Packaging and pricing

### Takeaway
Where stated, 1:1 transcript AI is bundled rather than sold as a paid add-on: Leapsome says the notetaker is included at no extra cost; Deel Checkins is part of Engage (not sold individually); Culture Amp's MCP access is on any subscription at no additional cost. PerformYard is the exception in gating Meeting Coaching behind a "Talent Development" licence. No list prices for these features are public.

### Cited Findings
- Leapsome: Meeting Notetaker is "included in the Leapsome platform at no extra cost". [FETCHED][CLAIM] https://www.leapsome.com/blog/meeting-notetaker-ai-agent
- PerformYard: Meeting Coaching requires a "PerformYard Talent Development license"; the "Intelligence Layer" is described as included "in every plan". [FETCHED] https://support.performyard.com/article/516-meeting-coaching-setup ; [FETCHED][CLAIM] https://www.performyard.com/ai
- Deel: Checkins is part of Engage within Deel HR; Engage tools "cannot be purchased individually"; no prices listed. [FETCHED] https://www.deel.com/solutions/engage/one-on-one-meetings/
- Culture Amp: MCP connector available on any subscription, "no additional cost today". [FETCHED] https://support.cultureamp.com/en/articles/16754009-connect-claude-or-chatgpt-to-your-1-on-1-conversations-via-mcp
- Predictive Index: notetaker applies to all Perform users on the PI2 platform (beta); Perform retires 2027-09-30. [FETCHED] https://docs.predictiveindex.com/en/articles/11824395-enabling-pi-meeting-notetaker
- Gallup: Gallup AI is included with a Gallup Access subscription. [SNIPPET] https://support.gallup.com/hc/en-us/articles/48408264183827-Gallup-AI
- Microsoft: intelligent recap is in Teams Premium; in-meeting/after-meeting Copilot requires a Microsoft 365 Copilot licence. [SNIPPET, third party] https://www.leadwithai.co/guides/copilot-teams-meetings
- Betterworks, Engagedly, Workleap: no pricing or plan gating stated on the pages opened. https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes ; https://engagedly.com/product/meetings/ ; https://workleap.com/lp/meeting-automation

### Inferences
- Competitors are positioning 1:1 capture as a retention/attach feature of the performance suite, not a revenue line. Charging separately for a QW 1-on-1 Assistant would run against the current norm, except where it is packaged with a coaching/development tier (PerformYard pattern).
- Dependence on the customer's Zoom/Teams/Google licence for native transcripts shifts part of the cost to the customer at Betterworks, PerformYard and Deel.

### Gaps
- No per-seat prices found for any vendor's 1:1 AI.
- Plan gating for Betterworks Conversational Intelligence and Engagedly Marissa Notetaker: Unknown.

---

## Source Health (access limits encountered in this run)
- https://help.leapsome.com — HTTP 403 on every direct fetch (three articles tried). Facts taken from search-index snippets only. Replacement sources used: https://www.leapsome.com/blog/meeting-notetaker-ai-agent and https://www.leapsome.com/en/subcontractors (both fetched).
- https://support.betterworks.com/hc/en-us/articles/42449959219725-Meetings-NextGen — HTTP 403. Replacement: Betterworks magazine article (fetched).
- https://help.engagedly.com/getting-started-with-meeting-agent — HTTP 503. "Manage the notetaker agent for meetings" article not retrieved.
- https://docs.predictiveindex.com/en/articles/11954313-9-15-25-pi-meeting-notetaker-perform — HTTP 404 (release note); the enabling article was fetched instead.
- https://web.archive.org — not reachable from this environment; no Wayback fallbacks were possible.
- Not attempted (budget): G2 reviews; trust centers / subprocessor lists for Betterworks, PerformYard, Engagedly, Deel, Culture Amp, Workleap, PI; AssemblyAI / Deepgram / Nylas customer pages.
