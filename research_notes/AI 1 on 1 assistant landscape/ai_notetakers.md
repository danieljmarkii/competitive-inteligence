# General-purpose AI meeting notetakers: capture, technology, downstream data use, governance, pricing (current state as of 2026-11-17)

Reading notes for the report writer:
- Evidence tags: **[P]** = read on the vendor's own page via direct fetch in this session. **[S]** = taken from a search-result snippet/summary of the cited URL (page not opened in full; treat as lower confidence and re-verify before quoting). **[3P]** = third-party or competitor-authored source. "Claim" = vendor marketing claim, not independently verified.
- All links are plain https:// URLs placed next to the fact they support.
- Access limits hit: help.openai.com (HTTP 403), support.read.ai (HTTP 403), read.ai/security (404), fellow.ai/1-on-1-meetings (404). No logins or paywalls were bypassed. Wayback was not attempted for these; search snippets were used instead and are tagged [S].
- Vendors prioritized: Granola, Notion, Otter, Fireflies, Fathom, Read AI, Fellow. Coverage of tl;dv, Circleback, Jamie, Krisp, Tactiq is thinner and mostly [S]/[3P].

## 1. Capture mechanism (bot vs botless vs extension vs mobile vs native), speaker identification, and what is stored

### Takeaway
The market has converged on "both": nearly every bot-first vendor (Otter, Fireflies, Fathom, Read AI, Fellow, Jamie, Krisp) now also ships a botless desktop recorder, while the botless natives (Granola, Notion, ChatGPT Record) capture system audio + mic on the user's device and store transcript only, not audio. Speaker attribution is the main quality cost of botless capture: it is strongest in 1:1 calls (two channels = two speakers), which is exactly the QW use case.

### Cited Findings

**Granola (botless native)**
- Does not auto-join or auto-record; the user starts it manually. "Granola doesn't store the audio from meetings"; it "only stores the transcript and any notes you provide from a call." [P] https://www.granola.ai/security
- iPhone app exists and is positioned for in-person meetings only; it has no automated consent messaging. [S] https://www.granola.ai/docs/docs/FAQs/consent-granola
- Windows app exists (automatic consent messaging is not available on it). [S] https://docs.granola.ai/help-center/managing-your-account/automatic-consent-messaging
- Apple Watch support (2026-07-28) and a dictation feature (2026-10-29) are reported only by an aggregator; unverified. [S][3P] https://simplify.jobs/c/Granola
- Speaker identification method (e.g., "Me"/"Them" channel split): Unknown; not confirmed from any source retrieved.

**Notion AI Meeting Notes (botless native, inside the Notion app)**
- Desktop app "captures all sides of the conversation using your system audio and mic"; requires system-audio and screen-recording permissions. Browser: "Only mic inputs will be transcribed. System audio won't be captured." Mobile: phone mic only, best for in-person. [P] https://www.notion.com/help/ai-meeting-notes
- Audio files (AAC, M4A, MP3, WAV) can be uploaded to a Meeting Notes block; daily limit 10 hours per user; 16 languages; speaker labeling English only. [P] https://www.notion.com/help/ai-meeting-notes
- Audio handling: live audio goes directly to sub-processors who "do not store audio"; temporary local copy deleted after processing or within 24 hours; failed-processing audio kept up to 3 days for retry. Optional "Store audio locally" (off by default; owner-enabled) keeps the 10 most recent recordings on the recorder's device only. [P] https://www.notion.com/help/ai-meeting-notes
- Speaker ID: desktop labels speakers best "in one-on-one virtual meetings"; a linked calendar event can supply the other participant's name; group, in-person, browser and mobile labeling has limited reliability. A "Notion Meetings" add-on (desktop, Chrome) adds speaker labels for Google Meet including group calls; Zoom on Mac can show speaker names after a setting/permission (Notion says it "never reads your screen or Zoom chat"). [P] https://www.notion.com/help/ai-meeting-notes
- Launched May 2025 explicitly as a response to Granola-style notetakers. [S] https://techcrunch.com/2025/05/13/notion-takes-on-ai-notetakers-like-granola-with-its-own-transcription-feature

**Otter.ai (bot-first, plus desktop/extension/mobile)**
- Otter Notetaker joins Zoom, Microsoft Teams and Google Meet as a participant (this is the mechanism at issue in the class action). [S] https://uctoday.com/productivity-automation/otter-ai-fails-to-dismiss-core-privacy-claims-in-u-s-court/
- Pricing page lists Zoom/Teams/Meet support, concurrent-meeting limits (1 to 3 notetakers at once), max conversation length (30 min Basic to 4 hours Business), file import, and mp3 export (i.e., audio is stored and exportable); an admin "audio removal" control is listed. [P] https://otter.ai/pricing
- A desktop app is described as a bot-free way to record; a Chrome extension and web "record" can capture a Meet/Zoom session with no notification to other participants, per a third-party reviewer. [S][3P] https://www.getvoibe.com/resources/is-otter-safe/
- Illinois BIPA voiceprint claims against Otter survived dismissal, which implies speaker-identification/voiceprint functionality is alleged; that is an allegation, not a finding. [S] https://idtechwire.com/otter-ai-must-face-voiceprint-claims-under-illinois-biometric-law/

**Fireflies.ai (bot-first, plus botless desktop, mobile, extension)**
- Web dashboard and mobile app flows require the "Fireflies Notetaker" bot to join; the desktop app (Mac/Windows) can record without a bot using device audio, started manually or via auto-detection. [S] https://guide.fireflies.ai/articles/6666374717-how-to-record-meetings-without-a-bot-on-the-fireflies-desktop-app and https://guide.fireflies.ai/articles/1208704416-getting-started-with-the-fireflies-desktop-app
- Video recording is a Business-tier feature (i.e., audio/video is stored, not transcript-only). [P] https://fireflies.ai/pricing
- Speaker talk-time tracking exists (implies diarization). [S][3P] https://www.eesel.ai/blog/fireflies-ai-review

**Fathom (bot-first, botless in beta)**
- Free plan offers a choice of "bot-free or bot capture", with bot-free "in beta"; the feature matrix says bot-free is a beta feature for Mac. [P] https://fathom.ai/pricing
- Botless mode is described as capturing audio and video without a visible participant. [S][3P] https://www.implicator.ai/fathoms-enterprise-push-bets-distribution-can-outrun-accuracy-gaps/
- A third-party profile reports "Fathom 3.0 goes bot-free on Mac" and an iOS app. [S][3P] https://yespress.io/fathom

**Read AI (bot-first, plus desktop/mobile apps)**
- Windows, macOS, Android and iOS apps are listed on all plans; audio/video playback is restricted to Enterprise and Enterprise+ (so lower tiers get reports/transcripts without playback); meeting length caps 1 hour (Free) to 8 hours (Enterprise+). [P] https://www.read.ai/plans-pricing
- A competitor's write-up says Read's desktop app has a manual record mode limited to audio, without video or the post-meeting coaching area/participant-level metrics. Competitor source; unverified. [S][3P] https://www.hedy.ai/pdf/posts/de/read-ai-alternative-hedy.pdf

**Fellow (bot + botless + in-person)**
- "Zoom, Google Meet, Microsoft Teams (bot-based)"; botless mode "records audio natively via the desktop app (Mac and Windows) without a visible meeting participant bot joining the call"; "In-person and hybrid meetings with speaker diarization"; claim of "Accurate transcriptions in 92 languages." [P] https://fellow.ai/llms.txt
- "Fellow auto-joins your Zoom, Google Meet, and Microsoft Teams meetings." [P] https://fellow.ai/go/1on1-meeting-tool
- "Zero-Day Retention" option "prevents source recordings and raw transcripts from being created as persistent records after AI processing" (i.e., summary-only storage is configurable). [P] https://fellow.ai/llms.txt

**tl;dv, Circleback, Jamie, Krisp, Tactiq (lower priority)**
- tl;dv: bot-based recorder (video recording); under heavy load free users' meetings may not be recorded, per a reviewer. [S][3P] https://www.laxis.com/blog/tldv-review/
- Circleback: desktop app records Zoom/Teams/Meet without a bot; desktop and mobile apps; free plan covers unlimited online and in-person meetings (plan lineup changed 2026-08-31). [S] https://circleback.ai/releases/new-plans
- Jamie: German vendor; one vendor-linked comparison says "Notetaker bot by default; desktop app records bot-free"; mobile docs say "Jamie cannot record phone calls"; a directory says audio is deleted immediately after transcription (no primary confirmation). [S][3P] https://gtmpicker.pages.dev/compare/jamie-vs-tldv and https://tooldirectory.ai/tools/jamie-ai
- Krisp: "you don't need a bot in your meeting. Krisp works directly at the audio level on your device"; an optional bot is still available for platforms like Zoom. [S][3P] https://meetgeek.ai/comparison/krisp-vs-tactiq
- Tactiq: browser-extension note taker that captures without a bot. [S][3P] https://meetgeek.ai/blog/tactiq-pricing

**Large AI/platform entrants**
- ChatGPT Record (OpenAI): native audio recording in the macOS desktop app only (not iOS/Android); available on Plus, Pro, Business, Enterprise, Edu. Audio files are deleted after transcription; output is a canvas plus transcript. [S] https://help.openai.com/en/articles/11487532-chatgpt-record (direct fetch returned HTTP 403). Max length is disputed in third-party sources: 120 minutes [3P] https://www.sally.io/blog/chatgpt-record-mode-review versus 4 hours [3P] https://sonix.ai/resources/wp-json/wp/v2/posts/3650
- Claude (Anthropic): "Claude Meetings" announced 2026-11-12 in beta for Team and Enterprise plans, Google Meet first; Claude joins as a visible participant, takes notes, answers questions and drafts docs/whiteboards during the call; saves transcript, summary and screen descriptions, not audio. [S] https://venturebeat.com/ai/anthropic-brings-claude-into-google-meet-to-draft-documents-and-whiteboards-during-your-meetings/ and https://aicatchup.com/news/claude-meetings-beta-team-enterprise
- Claude desktop recorder ("Project Parka"): reported only from unreleased code strings in a Mac build (file dates 2026-08-18); Mac-first recorder with speaker-labeled transcript and follow-up tasks assignable to Claude agents. Not announced; Anthropic has not confirmed. Treat as speculation. [S][3P] https://runtimewire.com/article/anthropic-s-project-parka-sits-through-meetings-and-assigns-claude-agents-the-ho
- Google Meet "Take notes for me" (Gemini): native, no bot; all participants are notified when enabled; notes saved as a Google Doc in Drive, transcript optional in its own tab; visual screenshots added to notes (2026-08-03); in-person (no video call) mode from August 2026. [S] https://blog.google/products-and-platforms/products/workspace/take-notes-for-me/ and https://workspaceupdates.googleblog.com/2026/08/visual-screenshots-now-included-in-Google-Meet-meeting-notes.html and https://letsdatascience.com/news/google-meet-adds-in-person-gemini-note-taking-4d0f7c61
- Microsoft Teams (Copilot / Facilitator / Intelligent Recap): native; Facilitator produces AI notes, including for in-person meetings in Teams Rooms on Windows (GA target October 2026) and Android. [S] https://mc.merill.net/message/RM560318 and https://mc.merill.net/message/RM560700
- Zoom: offers an MCP connector for Claude exposing AI meeting summaries, transcripts and recordings (native platform data rather than a third-party bot). [S][3P] https://aeo.washinmura.jp/ai/zvc-japan-%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE/en/news/2026-04-28-zoom-partners-with-claude-to-leverage-me

### Inferences
- Botless capture is now table stakes rather than a differentiator: seven of the twelve named vendors that started with bots have added a desktop recorder. A QW "1-on-1 Assistant" that only offers a visible bot would feel dated to users of Granola/Notion.
- Botless capture's weakest point (speaker attribution in group calls) largely disappears in 1:1s: Notion explicitly says desktop speaker labeling works best in one-on-one virtual meetings.
- Transcript-only storage (Granola, Notion, ChatGPT, Claude Meetings; optional at Fellow) is becoming the privacy-forward default; bot-first vendors still store audio/video and sell playback as an upper-tier feature (Read AI, Fireflies).
- In-person capture via phone is now common (Granola iPhone, Notion mobile, Circleback, Fellow, Google Meet in-person, Teams Rooms), relevant because many 1:1s are face to face.

### Gaps
- Use of native platform APIs (Zoom RTMS, Google Meet Media API, Teams) by any of the named third-party vendors: not found in any source retrieved. Unknown.
- Granola speaker-identification mechanism and whether Granola now has Android: Unknown.
- Whether Otter's and Read AI's desktop apps are fully botless across platforms: only third-party/competitor descriptions found.
- ChatGPT Record max duration and any Windows availability as of November 2026: OpenAI help page was blocked (403); third-party sources conflict.

## 2. Underlying technology: transcription provider, bot infrastructure, LLM providers

### Takeaway
Only Granola names its speech vendors on a public page (Deepgram and AssemblyAI, with OpenAI and Anthropic for LLMs). Recall.ai's customer page confirms Fellow and Circleback as customers. For Otter, Fireflies, Fathom, Read AI and the rest, the transcription engine and bot stack are not confirmed by any source retrieved.

### Cited Findings
- Granola: transcription via "best-in-class transcription providers (like Deepgram and Assembly)"; summarization via "AI providers (like OpenAI and Anthropic)"; hosted in a "US-hosted AWS Virtual Private Cloud." Confirmed (vendor page; the word "like" means the list may be non-exhaustive). [P] https://www.granola.ai/security
- Fellow: Recall.ai case study states Fellow built its AI meeting recorder with Recall.ai for Zoom, Google Meet and Microsoft Teams. Confirmed for bot recording. [P] https://www.recall.ai/customers
- Fellow hosting: "Your data is hosted by Amazon Web Services." [P] https://fellow.ai/pricing . Fellow's transcription and LLM vendors are not named on its llms.txt. [P] https://fellow.ai/llms.txt . A Fellow blog says its AI providers are contractually barred from retaining meeting content for training. [S] https://fellow.ai/blog/ai-note-takers-for-fintech/
- Circleback: appears on Recall.ai's customer logo wall (logo only, no description). Confirmed as a customer; scope (bot vs desktop SDK) not stated. [P] https://www.recall.ai/customers
- Recall.ai's customer page does NOT list Otter, Fireflies, Fathom, Read AI, Granola, Notion, tl;dv, Jamie, Krisp or Tactiq. Absence is not proof of in-house infrastructure. [P] https://www.recall.ai/customers
- Other notable Recall.ai customers shown (context for build-vs-buy): ClickUp, HubSpot, Rippling, Ashby, Metaview, BrightHire, Calendly, Attio, Gainsight, monday, Apollo.io, Grain, Sybill, Mindtickle, Jiminny. Recall.ai also sells a Desktop Recording SDK (used by SalesEQ, Mem.ai) for botless capture. [P] https://www.recall.ai/customers
- Notion: audio is sent "directly to sub-processors" who "do not store audio"; the sub-processors are not named on the help page. [P] https://www.notion.com/help/ai-meeting-notes
- Fireflies: security page names no subprocessors; says "our AI vendors don't retain it after processing." [P] https://fireflies.ai/security . Third-party summaries say zero-data-retention applies to AI vendors "such as OpenAI and Anthropic" and that ZDR does not cover data sent through its ChatGPT/Claude connectors. Inferred/secondary. [S][3P] https://baa-atlas.vercel.app/ai/fireflies
- Fireflies real-time voice assistant ("Talk to Fireflies") is built with Perplexity for live web search in meetings. [S] https://fireflies.ai/blog/fireflies-1-billion-valuation/
- Fathom: secondary sources citing Fathom's help center list AI subprocessors as Anthropic, OpenAI and Google; no source names a speech-to-text vendor. A Fathom DPA points to a trust-site subprocessor list (not retrieved). Inferred/secondary. [S] https://fathom.ai/dpa and [3P] https://www.getvoibe.com/resources/is-fathom-safe/
- tl;dv: a third-party comparison describes an Anthropic partnership powering Claude-based summaries; storage described as European data centers (Google Cloud, AWS, Hetzner; Wasabi S3). Secondary, unconfirmed. [S][3P] https://gtmpicker.pages.dev/compare/jamie-vs-tldv and https://www.ki-syndikat.de/tools/tldv/
- Read AI: support article says a subprocessor list exists; the list itself was not retrieved (support site returned 403). [S] https://support.read.ai/hc/en-us/articles/25702259763091-Security-Privacy-Overview
- Krisp: processes "directly at the audio level on your device" (vendor claim quoted by a third party); claims 96% accuracy in 17 languages. Claim. [S][3P] https://meetgeek.ai/comparison/krisp-vs-tactiq
- Jamie: emailed customers on 2026-10-02 that it is "simplifying its list of subprocessors" (details not retrieved; reported by a competitor). [S][3P] https://tldv.io/blog/meetjamie-alternatives/

### Inferences
- The fastest credible build path for a 1:1 assistant is the Fellow pattern: buy capture (Recall.ai bot API and/or Desktop Recording SDK), buy speech-to-text (Deepgram/AssemblyAI class), buy LLMs (OpenAI/Anthropic), and differentiate on workflow and data. HR-tech adjacent vendors (Rippling, Ashby, Metaview, BrightHire) already do this.
- Larger bot-first incumbents (Otter, Fireflies, Fathom, Read AI) most likely run in-house bot infrastructure given their age and absence from Recall.ai's page, but this is inference only.

### Gaps
- Otter: transcription engine (historically described as proprietary), LLM vendors and subprocessor list: not retrieved. Unknown from this session's sources.
- Fireflies, Fathom, Read AI: transcription vendor and bot infrastructure: Unknown.
- Notion: named speech and LLM subprocessors for Meeting Notes: Unknown (not on the help page).
- AssemblyAI and Deepgram customer pages were not checked (tool-call budget); they may name additional vendors.
- Trust-center subprocessor lists (trust.fathom.video, Otter, Fireflies, Read AI) not retrieved.

## 3. Downstream use of meeting data (beyond the summary), including 1:1 and people-management features

### Takeaway
The category has moved from "summary of one meeting" to "meetings as a company context layer": cross-meeting chat, MCP/API access for external agents, team workspaces, and agents that act on notes are now standard at Granola, Otter, Fireflies, Fathom, Read AI, Fellow and Notion. Coaching is real but generic (talk speed, filler words, talk time) or sales-specific (scorecards); none of the general notetakers retrieved offers manager-effectiveness coaching tied to performance data, and only Fellow is purpose-built around 1:1s.

### Cited Findings

**Granola**
- Recipes: saved prompts invoked with "/" in chat; can be scoped to a single meeting or "Multiple meetings", in which case they "appear on the home screen, in folders, people view, company view, or when you select multiple meetings"; shareable with teammates; default and community recipes in a Discover section. [P] https://docs.granola.ai/help-center/getting-more-from-your-notes/recipes
- Shared folders on all plans (marketed as Team Spaces at the March 2026 Series C); MCP server (launched February 2026) with access tiered by plan: Basic = personal notes from last 30 days, Business = personal and public workspace notes, Enterprise = admin-configurable; API access on Business and Enterprise. [P] https://www.granola.ai/pricing and [S] https://siliconangle.com/?p=736110
- Official Claude connector launched February 2026. [S] https://fellow.ai/blog/ai-meeting-notetaker-claude-connector/
- Company says it is working on AI agents that use note content to automate tasks (forward-looking statement at Series C). [S] https://siliconangle.com/?p=736110
- 1:1 content: Granola publishes manager 1:1 template guidance on its blog (content marketing, not a distinct product feature). [S] https://www.granola.ai/blog/one-on-one-meeting-template-for-managers . A "people view" exists as a surface for multi-meeting recipes. [P] https://docs.granola.ai/help-center/getting-more-from-your-notes/recipes

**Notion AI Meeting Notes**
- Summary uses both transcript and the user's typed notes; citations link to transcript lines; selectable summary formats (Auto, sales calls, standups) and custom instruction pages that can be shared. [P] https://www.notion.com/help/ai-meeting-notes
- Suggested "skills" during meetings (e.g., "Catch me up") and after (e.g., "Create follow-up tasks"); Notion Agent can be opened on the note; notes live in a meetings database that inherits workspace permissions; calendar events show "Join and transcribe"; notes can auto-share with internal calendar participants. [P] https://www.notion.com/help/ai-meeting-notes

**Otter.ai**
- AI Chat within and across meetings on all plans (query caps: 20/user/month Basic, 50 Pro, 200 Business/Enterprise); Enterprise AI Chat extends to Gmail, Google Drive, Notion, Jira and Salesforce; channels (private, public links, General channel); AI "workflows" tiered from basic to "unlimited custom AI workflows"; Otter Sales Notetaker; Otter MCP server (listed even on Basic); "Otter API & Webhooks" on Enterprise. [P] https://otter.ai/pricing
- October 2025 enterprise suite positioned meetings as a corporate knowledge base with API and MCP server connecting to Claude and ChatGPT; April 2026 feature lets users search across enterprise tools. [S] https://www.uctoday.com/?p=88785 and https://www.itpro.com/technology/artificial-intelligence/otter-ai-wants-to-bring-agents-to-third-party-systems

**Fireflies.ai**
- Conversation intelligence (talk time, sentiment analysis), analytics and private channels (Business), API with per-plan rate limits, AI credits system. [P] https://fireflies.ai/pricing and [S][3P] https://www.eesel.ai/blog/fireflies-ai-review
- "Talk to Fireflies" live voice assistant with Perplexity web search inside meetings (all plans); "Fireflies Talk" free unlimited dictation on Mac/Windows (September/October 2026). [S] https://fireflies.ai/blog/fireflies-1-billion-valuation/ and https://techcrunch.com/2026/09/29/fireflies-adds-dictation-to-its-desktop-notetaking-apps/
- ChatGPT and Claude connectors exist (third-party summary). [S][3P] https://baa-atlas.vercel.app/ai/fireflies

**Fathom**
- Ask Fathom (single call, "my calls", across team calls; account-wide in beta); shared team workspace, trackers and search (Team); CRM field sync, Deal View, "Coaching metrics & AI scorecards" (Business); "Public API & MCP"; Asana integration. [P] https://fathom.ai/pricing
- Now owned by Superhuman (formerly Grammarly): Fathom is to feed meeting context into Superhuman's email, calendar, docs and its proactive assistant "Go" and agents. [S] https://blog.superhuman.com/superhuman-acquires-fathom/

**Read AI**
- Every plan includes "Meeting coach", "Recommendations, meeting policy, coaching trends" and "Ask Read" search; the meeting report includes metrics such as "talking speed, filler words, bias, and charisma"; "For You Insights" on paid plans; integrations with Notion, Salesforce, HubSpot, Jira, Confluence, Zapier, webhooks (Pro and up). [P] https://www.read.ai/plans-pricing
- Search Copilot (launched March 2025 as enterprise search across meetings, email, chat, docs) gained chat querying and actions (CRM updates, scheduling) in 2026. [S] https://www.geekwire.com/2025/seattle-startup-takes-a-swing-at-enterprise-search-with-new-ai-fueled-discovery-tool/ and https://www.read.ai/ru/post/read-it-whats-new-at-read-ai----february-2026
- "Ada" digital twin (February 2026): email-based assistant that answers questions and schedules on the user's behalf using their Read data; free; enterprise workspaces can rebrand it. [S] https://techcrunch.com/2026/02/26/read-ai-launches-an-email-based-digital-twin-to-help-you-with-schedules-and-answers/
- No dedicated 1:1 or manager-coaching feature found.

**Fellow (the only vendor here built around 1:1s)**
- Self-described as "the only 1on1 AI meeting management software"; 1:1s get "meeting agendas, action items and AI note-taking"; recaps highlight "action items, decisions, and meeting stats" such as speaker time; chaptered recaps; output to Slack, Google Docs, Linear, Zapier and 50+ tools. Claim. [P] https://fellow.ai/go/1on1-meeting-tool
- "Ask Fellow is an in-app AI agent that works across all phases of the meeting lifecycle" with reusable prompt shortcuts and persistent memory; Fellow MCP Server; Claude, n8n, Make, Zapier; Salesforce and HubSpot auto-update. [P] https://fellow.ai/llms.txt
- Plan features include meeting automations (Team), org-wide meeting templates (Business). [P] https://fellow.ai/pricing
- Third-party reviews describe shared 1:1 history, feedback tools and performance-review synthesis from meeting notes as core; not confirmed on a Fellow page in this session. [S][3P] https://thebusinessdive.com/fellow-vs-fathom

**Others**
- tl;dv: sales coaching hub with playbook tracking, objection-handling analysis and rep scorecards; "MCP server, API & webhooks" on Pro. [S][3P] https://www.laxis.com/blog/tldv-review/
- Circleback: post-meeting automations into HubSpot, Notion, Linear, Slack; API, MCP and CLI access even on Free; follow-up email drafting. [S] https://circleback.ai/releases/new-plans
- Tactiq: Claude connector; AI actions metered by credits. [S] https://tactiq.io/learn/ai-meeting-notetaker-with-claude-connector
- ChatGPT Record: output is a canvas in ChatGPT; canvases/transcripts follow workspace conversation retention and are exposed to the Compliance API for Enterprise/Edu. [S] https://help.openai.com/en/articles/11487532-chatgpt-record
- Claude Meetings: acts during the call (answers questions, builds docs and whiteboards), not only afterward. [S] https://venturebeat.com/ai/anthropic-brings-claude-into-google-meet-to-draft-documents-and-whiteboards-during-your-meetings/
- Microsoft Facilitator: now proactively detects "knowledge gaps" and searches the web mid-meeting unprompted; enabling user needs a Microsoft 365 Copilot license, other participants do not. [S] https://uctoday.com/microsoft-teams-copilot-whats-new-in-september-2026 and https://mc.merill.net/message/MC1409304/v/2026-08-26T16-30-26-927Z

### Inferences
- MCP/API exposure of meeting data is now near-universal (Granola, Otter, Fathom, Fellow, tl;dv, Circleback, Fireflies API). Buyers will expect a QW 1:1 Assistant to let their own AI assistants read 1:1 summaries, which raises a sharp governance question for sensitive manager-employee content.
- Coaching in this category is either speech-mechanics (Read AI) or sales-rep scorecards (Fathom, tl;dv). Coaching a manager on the quality of a 1:1 (listening ratio, follow-through on commitments, feedback quality, growth conversations) grounded in goals/performance/engagement data appears to be open white space for QW.
- General notetakers treat a 1:1 as one more meeting; the continuity that matters for 1:1s (agenda carry-forward, commitments across weeks, link to goals and reviews) exists only at Fellow among those reviewed.
- Platform consolidation (Superhuman buying Fathom; Notion, Google, Microsoft, OpenAI, Anthropic bundling capture) means basic transcription and summaries are commoditizing toward zero marginal price.

### Gaps
- Fellow's detailed 1:1 feature set (private notes, feedback, performance-review synthesis, 1:1 templates) could not be confirmed on a first-party page: fellow.ai/1-on-1-meetings returned 404 and the /go/ landing page is thin.
- Granola's list of built-in recipes (whether any are coaching- or 1:1-specific) is not enumerated in the docs page retrieved. Unknown.
- Pre-meeting briefs: not confirmed for any vendor from sources retrieved. Unknown.
- Otter "AI Meeting Agents" feature details beyond the pricing-page labels were not opened.

## 4. Integration with HR / performance platforms (Lattice, 15Five, Workday, etc.)

### Takeaway
No general-purpose notetaker reviewed shows an integration that pushes meeting content into a performance-management platform. The only HR-system tie found is Fellow's HRIS sync, which is for user provisioning, not performance data.

### Cited Findings
- Fellow: "Fellow syncs with your HRIS to make provisioning and de-provisioning automatic." [P] https://fellow.ai/go/1on1-meeting-tool
- Fellow pricing FAQ: "HRIS Sync" listed; Workday, BambooHR and Namely "can also be customized for your Enterprise plan." [P] https://fellow.ai/pricing
- Otter, Read AI, Fathom, Fireflies, Granola integration lists retrieved name CRM, project and knowledge tools (Salesforce, HubSpot, Jira, Confluence, Notion, Asana, Linear, Slack, Gmail, Google Drive) and no HR/performance platform. [P] https://otter.ai/pricing , https://www.read.ai/plans-pricing , https://fathom.ai/pricing , https://fellow.ai/pricing
- Recall.ai's customer wall includes HR-tech vendors Rippling, Ashby, Metaview and BrightHire, i.e., HR platforms are embedding their own capture rather than integrating notetakers. [P] https://www.recall.ai/customers

### Inferences
- The HR/performance link is being built from the HR side (HR platforms embedding capture via Recall.ai) rather than from the notetaker side. QW would be following that pattern, and its data link to goals, feedback and reviews is something general notetakers do not have.
- Via MCP/Zapier/webhooks, a customer could wire any notetaker into an HR tool themselves, but there is no evidence of a packaged integration.

### Gaps
- Full integration directories for each vendor were not exhaustively reviewed; a Lattice/15Five/Workday/Culture Amp connector may exist in a marketplace listing not surfaced here. "No evidence found" rather than "confirmed absent".

## 5. Governance: consent and notification, admin controls, retention, model training, residency, certifications, enterprise controls

### Takeaway
Consent handling has become the central governance battleground in 2026: both the bot model (Otter) and the botless model (Granola) are in active wiretap litigation, and vendors have responded with automatic chat/audio consent messages and admin-enforced consent policies (Notion, Granola, Fireflies, Fellow, Google). Model-training posture now splits vendors: Fireflies and Fellow claim never to train; Granola, Otter and (reportedly) Fathom train on de-identified data by default with opt-out; Read AI is opt-in.

### Cited Findings

**Granola**
- Consent tooling: automatic consent message posted in Google Meet and Zoom chat on macOS only (sent after another speaker is detected; Zoom window must be focused and chat composer empty); not available on Windows or iPhone. Blog also describes a video watermark and admin enforcement for enterprise. [S] https://docs.granola.ai/help-center/managing-your-account/automatic-consent-messaging and https://www.granola.ai/blog/ai-notetaker-participant-privacy-consent and https://docs.granola.ai/help-center/consent-security-privacy/transparency-solutions/for-enterprise-admins
- Training: "We do not allow third parties (like OpenAI or Anthropic) to use your data to train their AI models"; Granola itself trains on anonymized data with opt-out in Settings; "Enterprise users have model training turned off by default." [P] https://www.granola.ai/security
- Retention: per-user transcript retention and auto-deletion on Basic/Business; workspace-wide admin policy and org-wide auto-deletion on Enterprise. Admin controls for sharing, API, MCP and integrations on Enterprise. SSO (Google Workspace, Microsoft, Okta) on Enterprise for 50+ user workspaces; SCIM not mentioned. [P] https://www.granola.ai/pricing and https://www.granola.ai/security
- Certifications/residency: SOC 2 Type 2 (July 2025); GDPR DPA on request; US-hosted AWS; ISO 27001 and HIPAA not mentioned. [P] https://www.granola.ai/security

**Notion**
- Consent: user can paste a consent message in chat, play an audio consent message, or ask aloud; with the Google Meet add-on Notion posts and pins a chat message and shows a recording indicator; owners can "Enforce consent for all workspace members" (automatic audio consent at start of each transcription); Enterprise org owners can set or lock this across workspaces. [P] https://www.notion.com/help/ai-meeting-notes
- Admin: owners can turn Meeting notes on/off for the workspace, enable local audio storage, set a default meetings database; Enterprise "Automatic transcript deletion" keeps summaries but removes transcripts (legal-hold pages excluded); users can "Delete transcript". Available on Business and Enterprise plans. [P] https://www.notion.com/help/ai-meeting-notes

**Otter.ai**
- Plaintiffs allege the Notetaker does not request permission from other participants and that the pre-meeting email notice option is not enabled by default; allegations only. [S] https://hrexecutive.com/?p=165464
- Training: third-party summary says Otter trains on de-identified user data by default with an opt-out in account settings; not verified on Otter's own page. [S][3P] https://www.getvoibe.com/resources/is-otter-safe/
- Controls: Business adds activity logs and usage analytics; comparison table lists custom data retention, audio removal and recording controls (plan mapping unclear); Enterprise has SSO, SCIM, domain capture (100-user minimum) and HIPAA as an add-on. [P] https://otter.ai/pricing
- HIPAA compliance since July 2025; SOC 2 Type II. [S] https://www.businesswire.com/news/home/20250710027730/en

**Fireflies.ai**
- Consent: admins can enable a pre-meeting email to all participants (sent 1 hour before) and an editable in-meeting chat message, and can let teammates choose; desktop (botless) app offers an audio consent message and a camera watermark; Fireflies states the user is responsible for consent compliance. [S] https://guide.fireflies.ai/articles/7003995379-do-i-need-to-disclose-that-i-am-recording-meetings and https://guide.fireflies.ai/articles/3917896272-how-consent-notifications-work-on-the-fireflies-desktop-app
- "Fireflies does not use your meeting data to train AI models, and our AI vendors don't retain it after processing." "SOC 2 Type II certified, GDPR compliant, and HIPAA-ready on Enterprise plans"; ISO 42001 certified; HIPAA BAA and FERPA DSA on Enterprise with Private Storage; "Private Storage on Enterprise to store your meeting data at your preferred location"; custom data retention (Enterprise); SSO listed; 256-bit AES at rest. [P] https://fireflies.ai/security
- SCIM and custom data retention are listed on the pricing page without a stated tier. [P] https://fireflies.ai/pricing

**Fathom**
- Team plan and up: HIPAA compliance with a standard BAA; Enterprise: SSO, Okta SCIM provisioning, custom data retention policies. [P] https://fathom.ai/pricing
- Training: secondary sources say Fathom uses de-identified customer data to improve its own models with an individual opt-out, and that Anthropic/OpenAI/Google are barred from training on customer data. Not verified on Fathom's policy. [S][3P] https://www.getvoibe.com/resources/is-fathom-safe/
- Post-acquisition privacy-policy changes under Superhuman are being scrutinized by at least one commentator (free-tier training controls). Not opened; unverified. [S][3P] https://www.beri.net/article/superhuman-fathom-acquisition-privacy-policy-at-collection-free-tier-training-controls

**Read AI**
- Training: support article says the default is opt-out (not contributing), with users able to opt in to contributing data to Read's models; Terms of Service reserve training "subject to ... any applicable opt-in or opt-out mechanisms." [S] https://support.read.ai/hc/en-us/articles/25702259763091-Security-Privacy-Overview and https://read.ai/tos
- Enterprise+ only: HIPAA, SAML SSO and SCIM, domain capture, custom data retention policy, EU and CA hosting. Workspace admin controls from Pro. [P] https://www.read.ai/plans-pricing

**Fellow**
- "Fellow never trains on customer data" (all plans). SOC 2 Type II, HIPAA, GDPR, AES-256. [P] https://fellow.ai/llms.txt
- "Admins can configure recording and access permissions at the organization, team, or individual user level." "Compliance teams receive workspace-level access to retrieve any meeting record across the organization." "Consent disclosure events and timestamps are logged for regulatory review"; pause/resume events logged. Retention "fully configurable from a defined number of days to indefinite"; "Zero-Day Retention" option. [P] https://fellow.ai/llms.txt
- Governance suite (press release 2026-08-28): attendees must agree or decline recording before joining, with real-time notice to organizers if consent is withheld. [S] https://www.cfo.com/press-release/20260828-fellows-new-governance-suite-brings-compliance-grade-controls-to-ai-meetin/
- SSO (Okta, OneLogin), domain control and user provisioning on Enterprise; "Custom storage time" marked "coming soon" on the pricing page (conflicts in emphasis with llms.txt's configurable retention). [P] https://fellow.ai/pricing
- A competitor's 2026 review rated Fellow's consent handling high-risk; it likely predates the August governance suite. [S][3P] https://blog.buildbetter.ai/do-they-own-your-data-fellow-privacy-policy-reviewed-2/

**Others**
- tl;dv: markets GDPR, EU hosting, EU AI Act compliance and privately hosted AI for enterprise; its own security overview reportedly notes AI processing can run in Europe or the US. [S][3P] https://www.laxis.com/blog/tldv-review/
- Jamie: EU-hosted; audio reportedly deleted right after transcription. [S][3P] https://tooldirectory.ai/tools/jamie-ai
- Circleback: security details at security.circleback.ai (not opened); SSO and compliance controls on Enterprise. [S][3P] https://tooldirectory.ai/tools/circleback
- ChatGPT Record: workspace owners toggle Record in Workspace Controls; disabled by default for Enterprise and Edu; audio deleted after transcription; canvases and transcripts covered by the Compliance API. [S] https://help.openai.com/en/articles/11487532-chatgpt-record
- Google Meet: admins can turn off automatic note-taking in the Admin console and (April 2026) can require explicit participant consent before note-taking, recording or transcription begins; one guide says that setting is off by default. [S] https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html and https://www.leadwithai.co/guides/gemini-in-google-meet
- Microsoft Facilitator: participants can stop its proactive behavior by removing Facilitator from the meeting. [S] https://mc.merill.net/message/MC1409304/v/2026-07-28T16-13-52-447Z

### Inferences
- A defensible 2026 baseline for a 1:1 product is: explicit, logged consent from the employee (not just notice), transcript-only or zero-retention options, admin-set retention, a no-training commitment, and SOC 2 Type II. Fellow's "agree or decline before joining" plus consent logs is the most advanced consent posture found and is the bar QW would be compared against.
- Fellow's statement that compliance teams can retrieve "any meeting record across the organization" illustrates the tension specific to 1:1s: enterprise discoverability versus employee candor. How QW answers "who besides my manager can see this?" will be a primary trust question.
- Default-on training with opt-out (Granola, Otter, reportedly Fathom) is now a litigation liability (it is pleaded in both the Otter and Granola complaints); a "never trains" posture is a cheap differentiator.

### Gaps
- Otter's first-party consent settings and training/opt-out language were not retrieved; only complaint allegations and third-party summaries.
- ISO 27001 status for all vendors: not confirmed for any vendor in this session (Fireflies shows ISO 42001, not 27001). Unknown.
- Audit-log availability by vendor: only Otter ("activity logs", Business) and Fellow (consent/pause logs) surfaced. Others Unknown.
- Data-residency options beyond Read AI (EU/CA on Enterprise+), Fireflies (Private Storage), tl;dv/Jamie (EU), Granola (US only): Unknown.
- Notion's model-training policy specific to Meeting Notes was not on the help page retrieved.

## 6. Pricing tiers and scale signals (late 2026)

### Takeaway
List prices cluster at $0 free tiers, roughly $7 to $20 per user per month for individual/team tiers, and $25 to $40 for enterprise tiers, with SSO/SCIM/retention/HIPAA gated to the top tier almost everywhere. Scale signals: Granola is a $1.5B unicorn (March 2026), Fireflies $1B (2025 tender), Otter reported $100M ARR (2025), and Fathom was acquired by Superhuman (September 2026).

### Cited Findings

**Pricing (per user per month, USD unless noted)**
- Granola: Basic $0 (30-day limited history); Business $14 (unlimited history, API, shared folders); Enterprise $35 (SSO for 50+ users, workspace-wide retention/auto-deletion, training off by default, admin control of sharing/API/MCP). [P] https://www.granola.ai/pricing
- Notion AI Meeting Notes: included on Notion Business and Enterprise plans (plus eligible mobile subscriptions with Notion AI); no separate price on the help page. [P] https://www.notion.com/help/ai-meeting-notes
- Otter: Basic free (300 min/month, 30 min per conversation); Pro $16.99 monthly / $8.33 annual list (promotional prices also shown); Business $30 monthly / $19.99 annual (unlimited meeting transcription, 4-hour max); Enterprise custom (SSO, SCIM, domain capture at 100-user minimum; HIPAA add-on). [P] https://otter.ai/pricing
- Fireflies: Free, Pro, Business, Enterprise tiers; the pricing page as fetched showed no prices. Business adds video recording, analytics, private channels; Enterprise adds HIPAA/BAA and Private Storage. Prices Unknown from primary source. [P] https://fireflies.ai/pricing . Third-party reports cite user complaints about unexpected AI-credit costs. [S][3P] https://www.eesel.ai/blog/fireflies-ai-review
- Fathom: Free $0; Premium $20 monthly / $16 annual; Team $19 / $15 (2-user minimum; HIPAA BAA); Business $34 / $25 (CRM field sync, coaching metrics and AI scorecards); Enterprise about $35 annual (SSO, SCIM, custom retention). [P] https://fathom.ai/pricing
- Read AI: Free (5 meetings/month, 1-hour cap); Pro $15 annual / $19.75 monthly; Enterprise $22.50 / $29.75 (5+ licenses; audio/video playback); Enterprise+ $29.75 / $39.75 (SSO/SCIM, HIPAA, retention policy, EU/CA hosting). Volume discounts 10% at 100+, 15% at 500+, 20% at 1,000+. [P] https://www.read.ai/plans-pricing
- Fellow: Free (5 lifetime AI recordings/user); Team $7 annual / $11 monthly (10 AI recordings/user/month); Business $15 / $23 (unlimited AI recordings, CRM); Enterprise $25 annual (starts at 10 users; SSO, domain control, user provisioning, HRIS sync). [P] https://fellow.ai/pricing
- tl;dv: third-party sources conflict: Pro about $18; Business quoted from $59 to $98. Unverified. [S][3P] https://www.claap.io/blog/tl-dv-pricing
- Circleback: new Free/Pro/Business/Enterprise lineup from 2026-08-31; Pro reported at $15, older sources cite $20.83 to $30. Unverified. [S] https://circleback.ai/releases/new-plans and [3P] https://dupple.com/tools/circleback
- Jamie: third-party sources conflict (Plus about EUR 25, Pro EUR 39 to 47, Team EUR 33 to 39 per seat). Unverified. [S][3P] https://tldv.io/blog/meetjamie-alternatives/
- Krisp: conflicting ($8 Pro vs $16 Core); free tier reportedly replaced by a 7-day trial. Unverified. [S][3P] https://www.activepieces.com/blog/krisp-pricing-2026-free-pro-business-plans-compared.md
- Tactiq: Free (10 transcripts, 5 AI credits/month); Pro about $8 annual. Unverified. [S][3P] https://meetgeek.ai/blog/tactiq-pricing
- ChatGPT Record: included in ChatGPT Plus ($20/month), Pro, Business, Enterprise, Edu. [S][3P] https://fireflies.ai/blog/how-to-use-chatgpt-for-meetings/
- Claude Meetings: requires a paid Claude plan; notes/transcripts free during the Team/Enterprise beta. [S][3P] https://fourweekmba.com/ai-claude-meetings-joins-google-meet-docs-free-for-90-days/
- Google "Take notes for me": included in Workspace Business Standard and above per one guide; extended to consumer Google AI Pro/Ultra in June 2026. Another source says a $20 Gemini add-on is required (likely outdated). [S][3P] https://www.leadwithai.co/guides/gemini-in-google-meet and https://www.eweek.com/news/google-meet-gemini-ai-notes-pro-ultra/
- Microsoft: Facilitator/Intelligent Recap features require a Microsoft 365 Copilot license; third-party sources quote $30 and $21 per user per month for different Copilot SKUs. [S][3P] https://microsoft.github.io/mwkorea/monthlycopilot/CopilotFacilitatorChannel/

**Scale signals**
- Granola: $125M Series C at $1.5B valuation (March 2026, Index Ventures lead; up from $250M valuation in May 2025); total raised reported between about $176M and $192M (sources disagree); customers named include Vanta, Gusto, Asana, Mistral AI. [S] https://siliconangle.com/?p=736110 and https://implicator.ai/granola-raises-125-million-at-1-5-billion-valuation-for-ai-notetaker/ and https://techcrunch.com/2025/05/14/ai-note-taking-app-granola-raises-43m-at-250m-valuation-launches-collaborative-features
- Otter: company-announced $100M ARR milestone in 2025; user figures of 35 million vs 40 million across sources; no 2026 ARR figure found. [S] https://www.businesswire.com/news/home/20251222704206/en/ and [3P] https://sacra.com/c/otter/
- Fireflies: $1B valuation via tender offer/secondary (mid-2025), no primary raise since its 2021 Series A, reportedly profitable since 2023; user counts conflict (10M users/200K orgs vs 20M+ users/500K orgs). [S] https://fireflies.ai/blog/fireflies-1-billion-valuation/ and [3P] https://www.fast.io/resources/fireflies-ai-review-2026.md
- Fathom: $17M Series A (press release 2026-04-15, Telescope Partners; note that implicator.ai describes an October 2025 feature expansion, so round timing should be re-verified); acquired by Superhuman, announced 2026-09-14, terms undisclosed; one source reports 400,000+ monthly users. [S] https://www.businesswire.com/news/home/20260415965820/en/ and https://blog.superhuman.com/superhuman-acquires-fathom/ and https://www.goodwinlaw.com/en/news-and-events/news/2026/09/announcements-otherindustries-goodwin-advises-fathom-on-acquisition-by-superhuman
- Read AI: $50M Series B in October 2024 at a reported $450M valuation; about $81M total; "5M+ monthly active users" company-reported in 2026 per a third-party profile; no 2026 round found. [S] https://theprint.in/tech/ai-startup-read-announces-new-funding-at-450-million-valuation/2332273/ and [3P] https://yespress.io/read-ai
- Fellow: founded 2017; $30.5M total raised. [P] https://fellow.ai/llms.txt
- Circleback: YC-backed; about $2.5M seed (November 2024). [S][3P] https://simplify.jobs/c/Circleback
- tl;dv: "over 2 million users" per a third-party source. [S][3P] https://www.ki-syndikat.de/tools/tldv/

### Inferences
- Enterprise governance (SSO, SCIM, retention, training-off, HIPAA) is priced at roughly $25 to $40 per user per month across the category; summaries themselves are free. A 1:1 Assistant priced as an add-on is competing against "free with the tools we already have" (Notion, Google, Microsoft, ChatGPT, Claude).
- Fellow at $7 to $25 is the direct price anchor for a 1:1-oriented meeting tool with enterprise controls.

### Gaps
- Fireflies current list prices: not shown on the fetched pricing page. Unknown from primary source.
- First-party pricing for tl;dv, Circleback, Jamie, Krisp, Tactiq not fetched; third-party figures conflict.
- No 2026 revenue figures found for any vendor other than Granola's "revenue grew 2.5x since January" growth claim. [S] https://implicator.ai/granola-raises-125-million-at-1-5-billion-valuation-for-ai-notetaker/
- Notion Business/Enterprise plan prices not captured.

## 7. Controversies and litigation, and vendor responses

### Takeaway
Two pending N.D. Cal. class actions define the legal risk: In re Otter.AI Privacy Litigation (bot model; core CIPA wiretap and Illinois BIPA claims survived a motion to dismiss in August 2026) and Chamberlain v. Granola (botless model; filed July 2026, no ruling). Neither has reached the merits, but together they show that neither a visible bot nor an invisible desktop recorder is a safe harbor without affirmative participant consent.

### Cited Findings
- In re Otter.AI Privacy Litigation (N.D. Cal., Judge Eumi K. Lee): consolidates four proposed class suits filed August to September 2025 alleging the Notetaker joined Zoom/Teams/Meet calls and recorded, transcribed and retained communications without required consent and used them to train models. On 2026-08-13 the court granted the motion to dismiss in part and denied it in part; CIPA wiretap claims and BIPA voiceprint claims proceed; the judge reportedly rejected the argument that appearing in the attendee list constitutes consent. Otter declined to comment on the ruling. No merits finding. [S] https://uctoday.com/productivity-automation/otter-ai-fails-to-dismiss-core-privacy-claims-in-u-s-court/ , https://www.bairdholm.com/blog/core-privacy-claims-against-ai-note-taking-platform-survive-dismissal/ , https://www.mealeys.com/mealeys/articles/2517873 , https://hrexecutive.com/?p=165464 , https://idtechwire.com/otter-ai-must-face-voiceprint-claims-under-illinois-biometric-law/
- Chamberlain v. Granola, Inc., No. 3:26-cv-07926 (N.D. Cal.), filed 2026-07-30: proposed nationwide class and California subclass; federal Wiretap Act and CIPA claims; core theory is that the no-visible-bot design records non-consenting participants without notice and that Granola marketed this as a differentiator; also alleges recordings feed model training by default. An amended complaint on 2026-10-19 is reported by one source only. Granola had not responded in court as of the latest source (October 2026). Allegations only. [S] https://btlaw.com/en/insights/alerts/2026/what-the-granola-class-action-means-for-companies-building-and-deploying-conversation-capture-tools , https://www.hklaw.com/en/insights/publications/2026/08/the-wave-continues-to-build , https://ppc.land/granola-sued-for-recording-meetings-without-consent-to-train-ai-models/ , https://www.laxis.com/blog/ai-notetakers-in-court-granola-otter-lawsuits/ ; complaint PDF: https://storage.courtlistener.com/recap/gov.uscourts.cand.475308/gov.uscourts.cand.475308.1.0.pdf (not opened)
- Granola's product response (timing relative to the suit not established): automatic chat consent message, video watermark, and admin enforcement for enterprise. [S] https://www.granola.ai/blog/ai-notetaker-participant-privacy-consent
- Fireflies published a "responsible guide to AI notetakers" (September 2025) and documents opt-in/opt-out consent controls. [S] https://www.businesswire.com/news/home/20250915520061/en and https://guide.fireflies.ai/articles/7003995379
- Fellow shipped a governance suite with pre-join consent capture (August 2026), positioned for regulated industries. [S] https://ffnews.com/news/fellow-unveils-advanced-ai-governance-controls-for-enterprise-meeting-privacy
- Google added an admin setting to require explicit participant consent for Gemini note-taking (April 2026); Notion added workspace-enforced audio consent. [S] https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html and [P] https://www.notion.com/help/ai-meeting-notes
- Bot virality/uninvited bots: institutional guidance warns about Otter's Notetaker auto-joining via calendar access ("An uninvited guest"), with fixes being to disable auto-join, revoke calendar access or remove the extension; a third-party review of Read AI is titled "Opt-In AI Training, but a Bot That Spreads"; a university publishes meeting-bot guidelines. [S][3P] https://www.carleton.edu/ai/blog/an-uninvited-guest-what-you-should-know-about-otter-ais-notetaker/ , https://www.getvoibe.com/resources/is-read-ai-safe.md , https://uwaterloo.ca/information-systems-technology/about/policies-standards-and-guidelines/artificial-intelligence-ai/meeting-bots-guidelines
- Microsoft's proactive Facilitator behavior drew privacy concern in trade press. [S][3P] https://www.neowin.net/amp/microsoft-teams-getting-an-ai-feature-that-sounds-like-magic-but-may-trigger-privacy-alarms/
- HR-trade coverage frames both rulings as an employer liability issue for AI meeting assistants. [S] https://hrexecutive.com/?p=165464 and https://hrexecutive.com/?p=164878

### Inferences
- For a manager-employee 1:1 product the consent problem is structurally easier (both parties are known employees of the customer and can be consented via policy plus in-product acknowledgment) but ethically harder (power asymmetry: an employee may not feel free to decline). Vendors' move toward per-meeting affirmative consent (Fellow) and admin-enforced disclosure (Notion, Google) indicates where expectations are heading.
- Default-on model training is being pleaded as an aggravating fact in both complaints; QW should expect buyers' legal teams to ask about it.
- BIPA exposure attaches to voiceprints; speaker identification by voice (rather than by channel or calendar identity) carries distinct biometric risk.

### Gaps
- Exact list of claims dismissed vs surviving in the Otter order was not read from the order itself; only trade-press and law-firm summaries.
- Whether Otter changed product defaults (e.g., enabling consent notices by default) after the ruling: no source found. Unknown.
- Granola's formal legal response and the content of the reported amended complaint: not confirmed.
- Any litigation against Fireflies, Read AI, Fathom or others specifically: a third-party headline references Fireflies alongside Otter and Granola (https://blog.buildbetter.ai/ai-notetaker-lawsuits-2026-how-to-record-meetings-legally/) but the page was not opened; Unknown.
- Reddit and G2 user-sentiment sources were not reviewed (tool-call budget).
