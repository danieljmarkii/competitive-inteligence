# Platform-native meeting AI and transcript-capture technology (state as of 2026-11-17)

Reading notes for the report writer:
- All sources are plain https:// URLs placed next to the fact they support (repo convention: no markdown links).
- "(opened)" = I fetched the page itself. "(search summary)" = the fact came from a search-result summary that listed this URL; the page was not opened individually, so the page-level attribution is less certain. Treat (search summary) pricing as indicative only.
- "Unknown" = could not be verified from a source in this run. Nothing below is guessed.
- Vendor-authored comparison pages (Recall.ai, Nylas, Gladia blogs) are flagged as self-interested.

---

## A1. Zoom (AI Companion, My Notes, ZoomMate)

### Takeaway
Zoom's AI is the broadest native capture surface: AI Companion summaries are bundled into paid Workplace plans, and "My Notes" (AI Companion 3.0) extends note taking to third-party platforms (Teams, Google Meet) and in-person conversations, with a free tier. Zoom states it does not train its own or third-party models on customer content.

### Cited Findings
- AI Companion 3.0 was announced with agentic workflows; My Notes was listed "coming soon" at the December 2025 launch and is meant to capture notes from in-person meetings, Zoom meetings, and platforms like Google Meet and Microsoft Teams — https://investors.zoom.us/news-releases/news-release-details/zoom-launches-ai-companion-30-agentic-workflows-transforming (search summary); https://www.nojitter.com/ai-automation/zoom-ai-companion-3-0-now-generally-available (search summary)
- Zoom's My Notes page says it can "automatically capture, organize, and summarize conversations across Zoom, third party, and in-person meetings"; it "recognizes when you're in a meeting or conversation and asks if you'd like to capture notes"; requires Zoom client 6.7.5 or higher; settings (transcription permissions, voice activity detection) are in the Zoom web portal under Settings > Notes > My Notes — https://www.zoom.com/en/lp/my-notes (opened)
- My Notes tiers on that page: "My Notes Basic" (free, with Workplace Basic): 3 AI note-taking uses/month, summaries for 3 hosted meetings/month, 20 AI queries/month, 40 minutes per meeting. Paid "My Notes": unlimited AI note taking, summaries for all hosted Zoom Meetings, 3 in-person transcription uses/month, billed per user. "ZoomMate": 2,200 AI credits per user per month plus unlimited AI note taking. No dollar amounts shown on the page — https://www.zoom.com/en/lp/my-notes (opened)
- "In-person transcription" is a separate feature for in-person conversations and voice notes; it does not connect to Zoom transcripts or AI summaries and stops automatically when a Zoom Meeting is detected — https://www.zoom.com/en/lp/my-notes (opened)
- Storage: My Notes output is stored in Zoom Hub and Canvas — https://www.zoom.com/en/lp/my-notes (opened)
- Data training: the My Notes FAQ states Zoom does not use customer audio, video, chat, screen sharing, attachments to train Zoom's or its third-party AI models — https://www.zoom.com/en/lp/my-notes (opened)
- Zoom says meeting-summary features generate a temporary transcript that is sent to the relevant model; third-party providers may temporarily retain data for trust and safety or legal reasons but may not train on it — https://community.zoom.com/ai-companion-21/ai-companion-training-data-availability-73894 (search summary)
- Models: Zoom describes a "federated approach" that combines Zoom's own LLM with third-party models; the wording surfaced names Meta Llama 2, OpenAI and Anthropic. The Llama 2 wording looks dated and the originating page was not opened — https://services.northwestern.edu/TDClient/30/Portal/KB/ArticleDet?ID=2893 (search summary; attribution uncertain)
- Admin control: account owners/admins enable or disable AI Companion features (for example Meeting Summary, Smart Recording) at account and group level; a separate "data sharing" toggle was removed from AI Companion settings — https://community.zoom.com/t5/Zoom-AI-Companion/Turn-off-AI-Companion-Data-Sharing/m-p/163172 (search summary)
- Stanford's IT page notes AI Companion features are turned off by default in its deployment — https://uit.stanford.edu/service/zoom/ai (search summary)
- Some institutions restrict AI Companion to lower data classifications and warn about third-party AI bots: Northwestern approves it only for Level 1 and 2 data — https://services.northwestern.edu/TDClient/30/Portal/KB/ArticleDet?ID=2893 (search summary)
- Pricing (secondary sources, conflicting): AI Companion core features are included at no extra cost in paid Workplace plans; Workplace Pro listed at $13.33 (older) or $14.16 per user/month annual; Business $18.33 — https://www.nojitter.com/ai-automation/zoom-ai-companion-3-0-now-generally-available (search summary); https://www.eesel.ai/blog/zoom-pricing (search summary)
- A Zoom community post at the 3.0 launch said AI Companion is available as a standalone subscription for $10/month — https://community.zoom.com/customer-success-forum-23/from-conversation-to-completion-zoom-ai-companion-3-0-73615 (search summary). A third-party analysis dated August 2026 says the $10 standalone option had left Zoom's live pricing pages by mid-2026 — https://www.laxis.com/blog/zoom-ai-companion/ (search summary)
- Pricing trackers report the Custom AI Companion add-on moved from $12 to $20 per user/month in early 2026 — https://pricingsaas.com/companies/zoom/diffs/2026W10 (search summary). One secondary source says ZoomMate launched 2026-06-01 from $20/user/month with 2,200 AI credits as successor to the Custom AI Companion add-on — https://www.eesel.ai/blog/zoom-pricing (search summary; single source, but the 2,200-credit figure matches Zoom's own My Notes page)

### Inferences
- My Notes on third-party platforms plus the 6.7.5 client requirement and "recognizes when you're in a meeting" language implies device-side (botless) capture through the Zoom desktop client, but the page does not say so explicitly.
- For a QW customer on Zoom, a free or bundled native notetaker already exists for 1-on-1s, so QW's differentiation has to be what happens to the transcript downstream (performance context), not capture.

### Gaps
- Unknown: whether My Notes joins third-party meetings as a bot or captures device audio (page does not state).
- Unknown: what notice other participants get when My Notes captures a Teams/Meet/in-person conversation (page has no statement).
- Unknown: current official list prices for paid My Notes and ZoomMate (zoom.us/pricing not opened).
- Unknown: Zoom retention defaults, data residency options and eDiscovery specifics for AI Companion artifacts; not researched to a primary source.
- Unknown: any Workvivo or manager/1:1-specific AI Companion features; no source found.

---

## A2. Microsoft Teams (Copilot in Teams, Facilitator, intelligent recap)

### Takeaway
Microsoft's meeting AI is gated by licence: Facilitator and Copilot require Microsoft 365 Copilot; intelligent recap is in Teams Premium and Copilot. Governance is the deepest of any platform (Teams admin policies, Purview, tenant switches that now also gate third-party Graph access to transcripts and speaker attribution), and Facilitator is explicitly not supported in 1:1 chats or external meetings.

### Cited Findings
- Facilitator is "an AI-powered agent" producing collaborative real-time notes editable by all participants, AI Q&A, timeline markers, Word document creation, Teams Rooms experience, and "mobile capture of ad-hoc discussions and action items" (GA); Planner task tracking is in public preview — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened; page dated 2026-08-13)
- Facilitator prompts and responses are visible to everyone in the meeting, unlike Copilot in Teams where prompts/responses are private to the user — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened)
- Licence: Facilitator "is included with a Microsoft Copilot license and subject to available capacity"; needs eligible Microsoft 365 base licence + Teams licence + Copilot licence. Only licensed users can initiate; unlicensed users can see notes and responses — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened)
- Limitation: "Currently, Facilitator isn't supported in 1:1 chats, group chats, or external chats and meetings" — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened)
- Storage: Facilitator meeting data is stored as a .loop file in a OneDrive folder titled "Meetings" of the user who initiated Facilitator, and "is treated as meeting transcript data" — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened)
- Admin controls: Facilitator is allowed by default; admins Allow/Block it as an app in Teams admin center (Manage apps) or scope via app permission policies; AI-generated notes are controlled tenant-wide by the IsCollabMeetingNotesFluidEnabled setting (cannot be per-user) — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened)
- Compliance limits: Facilitator AI notes "aren't automatically collected as cloud attachments in Microsoft Purview eDiscovery"; retention labels are not supported for cloud attachments in AI notes; notes do not inherit the meeting's sensitivity label; watermark and prevent-copy settings are not applied; single spoken language only — https://learn.microsoft.com/en-us/microsoftteams/facilitator-teams (opened)
- In-meeting "Meeting AI" toggle: Message Center MC1319216 says from mid-September 2026 licensed organizers and presenters can turn Meeting AI (Copilot and Facilitator) on or off in a meeting; turning Meeting AI on automatically turns on transcription and generates a recap, and turning it off disables recording and transcription; retention/compliance policies and licensing are unchanged — https://mc.merill.net/message/MC1319216 (search summary; third-party mirror of Microsoft Message Center)
- "AI meeting recap without transcript": MC1275312 describes Copilot generating AI recaps from live meeting context even when recording and transcription are not enabled, with no transcript or recording saved, aimed at organisations that restrict keeping transcripts; the entry was revised several times in 2026 and requires Copilot — https://mc.merill.net/message/MC1275312 (search summary)
- Organizers can permanently delete recordings, transcripts, summaries and notes from recap; deletion does not override legal holds or retention policies — https://spaces.collab365.com/posts/microsoft-limits-copilot-features-to-licensed-user-SFKdS7 (search summary)
- Recording/transcript lifecycle: admins set a default expiration for new recordings/transcripts in Teams meeting policy; 120 days is the most commonly cited default; expiration is not retention, and Purview retention policies/labels take precedence — https://learn.microsoft.com/en-ca/microsoftteams/manage-teams-recording-expiration-policy (search summary); https://office365itpros.com/2021/08/03/teams-meeting-recordings-retention/ (search summary)
- A 2025 Message Center post says admins can apply retention policies to the transcript copy in OneDrive, while copies in Exchange Online need separate handling — https://mc.merill.net/message/MC726122/compare/2025-04-04T20-40-25-18Z/2025-04-11T19-04-56-777Z (search summary)
- Pricing (secondary): Microsoft 365 Copilot $30/user/month; Copilot Business $21 standard with $18 promo through December 2026; Business Standard with Copilot $23.50 and Business Premium with Copilot $32 from 2026-07-01 (annual, capped at 300 licences) — https://www.stmicro.net/blog/microsoft-365-copilot-business-july-2026/ (search summary); https://samexpert.com/microsoft-365-copilot-licensing/ (search summary)
- Microsoft raised commercial Microsoft 365 list prices on 2026-07-01 and folded Copilot Chat into base plans — https://www.marketscale.com/industries/software-and-technology/microsoft-365-prices-rise-up-to-43-as-copilot-chat-folds-into-base-plans (search summary)
- Teams Premium listed at $10/user/month (annual) on Microsoft's US business site as displayed 2026-08-18; intelligent recap is in both Teams Premium and Microsoft 365 Copilot; on 2026-04-01 some Premium features moved into base Teams licences — https://redresscompliance.com/microsoft-teams-premium-licensing.html (search summary); https://tomtalks.blog/microsoft-teams-april-2026-licensing-update-microsoft-places-and-advanced-town-hall-and-webinar-features-move-into-teams-core/ (search summary)
- Models: Anthropic Claude is available in Copilot alongside OpenAI models — https://www.computerworld.com/article/3700709/m365-copilot-microsofts-generative-ai-tool-explained.html (search summary)

### Inferences
- Because Facilitator is not supported in 1:1 chats/external meetings and its notes fall outside Purview eDiscovery cloud-attachment collection, Microsoft's flagship note agent is weakest exactly in the manager 1-on-1 scenario; Copilot recap and plain transcription still work for scheduled 1:1 meetings.
- Meeting AI now implies transcription-on, so tenants that enable Copilot meetings will increasingly have a transcript QW could ingest via Graph (subject to the admin switches in B2).

### Gaps
- Unknown: Viva / "People Skills" / Copilot manager 1:1-prep features. No source surfaced in this run; needs a dedicated search.
- Unknown: authoritative Microsoft statement on data residency and no-training for Teams meeting AI (Microsoft's Copilot privacy page https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy was referenced by the Facilitator doc but not opened).
- Unknown: exact participant notice text for Copilot-only (no transcript) meetings.
- Conflict: secondary sources disagree on which recap features need Teams Premium versus Copilot (video recap, recap without transcript reported as Copilot-only).

---

## A3. Google Meet (Gemini "take notes for me")

### Takeaway
Gemini note taking is tied to Gemini/AI-bearing Workspace editions (and consumer AI Pro/Ultra), writes notes to a Google Doc in the organizer's Drive under Vault retention, and in 2026 added an admin-enforced explicit-consent prompt and an in-person variant ("take notes with me").

### Cited Findings
- Admin Help lists supported editions for "Let Google Meet AI take notes for my users" as Gemini Enterprise and AI Meetings and Messaging; the Meet Help Center lists the Gemini Enterprise add-on, Gemini Education Premium add-on, and AI Meetings & Messaging add-on — https://support.google.com/a/answer/15071792 (search summary); https://support.google.com/meet/answer/14754724 (search summary)
- Explicit consent control (April 2026): admins can "require explicit consent from meeting participants before automatic note-taking, recording, and/or transcription begins"; participants "on supported devices must actively agree to be recorded, be transcribed, or have notes enabled"; OFF by default; set at domain, OU or group level; no end-user setting; extended rollout started 2026-05-05 — https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html (opened)
- That post's edition list for consent covering notes + recordings + transcripts: Business Standard and Plus, Enterprise Standard and Plus, Frontline Plus, Google AI Pro for Education add-on (implying Gemini notes are in those editions as of 2026) — https://workspaceupdates.googleblog.com/2026/04/require-explicit-consent-for-take-notes-with-Gemini-recordings-and-transcripts-in-Google-Meet.html (opened)
- "Take notes with me" for in-person meetings became available in August 2026; the post lists consumer Google AI Pro and Ultra, Frontline Plus and Google AI Pro for Education among eligible editions — https://workspaceupdates.googleblog.com/2026/08/take-notes-with-me-for-in-person-meetings-is-now-available.html (search summary)
- Admin controls: Admin console Meet Gemini settings let admins control how AI notes are shared, set a default sharing option, and decide whether hosts can change it; AI notes Docs follow Meet retention policies managed with Vault — https://knowledge.workspace.google.com/admin/meet/let-google-meet-ai-take-notes-for-my-users (search summary)
- Storage: Meet artifacts are saved to the organizer's Drive and follow Drive rules; Vault can manage retention separately — https://developers.google.com/workspace/meet/api/guides/artifacts (opened)
- Developers can pre-configure auto-recording, auto-transcripts and "take notes for me" on a meeting space via the Meet REST API (GA 2025-04-29) — https://developers.google.com/workspace/meet/release-notes (opened)

### Inferences
- Google is the only one of the three majors with a documented admin-enforced per-participant opt-in for AI notes; this raises the bar for any third-party capture QW ships into Workspace tenants.

### Gaps
- Unknown: per-seat price uplift attributable to Gemini notes in late 2026 (edition pricing not researched).
- Unknown: Google's model naming for Meet notes beyond "Gemini", and a primary-source no-training/data-residency statement (not opened).
- Conflict: Admin Help page still lists only "Gemini Enterprise, AI Meetings and Messaging" while Workspace Updates posts list Business/Enterprise editions; treat the edition list as unsettled.

---

## A4. Slack huddle notes and Webex AI Assistant

### Takeaway
Slack bundles AI huddle notes into all paid plans (notes land in a canvas in the huddle thread); Cisco includes AI Assistant with paid Webex plans and governs it in Control Hub. Both are thinly documented on retention and developer access.

### Cited Findings
- Slack: conversation/thread summaries and huddle notes are available to all customers on paid subscriptions per Slack's plan-change help article — https://slack.com/help/articles/39264531104275-Updates-to-feature-availability-and-pricing-for-Slack-plans (search summary); https://www.techradar.com/pro/slack-users-get-more-ai-at-a-more-unified-price-and-every-salesforce-user-now-gets-free-slack-access (search summary)
- Slack: user starts "AI Notes & Transcription" from huddle controls; notes are placed in a canvas automatically shared to the huddle thread — https://www.eesel.ai/blog/slack-ai-huddle-notes-and-action-items (search summary; third-party guide)
- Slack pricing (secondary): Pro $7.25/user/month annual, $8.75 monthly; Business+ rose to $15/user/month — https://fast.io/resources/slack-ai-review-2026/ (search summary)
- Webex: AI Assistant is managed in Control Hub under Organization Settings > "Cisco AI Assistant & AI features"; settings cover in-meeting summaries and Ask AI Assistant, external-participant access, AI summaries and chapters for recordings (recording summaries enabled by default; hosts can turn off), and whether AI Assistant starts with a meeting recording; meeting summaries English only — https://help.webex.com/en-us/article/nyus067/AI-generated-meeting-summaries-in-Control-Hub (search summary); https://help.webex.com/article/9dofjcb/Administer-Cisco-AI-Assistant-in-Control-Hub (search summary)
- Webex: AI Assistant included with paid plans (Starter, Business, Enterprise) per an undated third-party overview — https://www.nojitter.com/ai-assistants-copilots/what-is-the-cisco-ai-assistant-for-webex- (search summary)
- Recall.ai's vendor-authored benchmark states Webex, GoTo and Slack Huddles were excluded from head-to-head testing "because competitors do not support them", i.e. bot coverage for these is thin outside Recall — https://www.recall.ai/recall-ai-competitors (opened; vendor-authored)

### Inferences
- Slack huddles are a real venue for informal 1-on-1s, but there is no evidence of a transcript API; QW would need a bot vendor or desktop capture to reach them.

### Gaps
- Unknown: Slack API access to huddle transcripts/notes, retention of huddle transcripts, admin disable controls (no source found).
- Unknown: Webex data-training policy and Webex transcript API details (not researched to a primary source).

---

## B1. Zoom developer options (no bot, and bot)

### Takeaway
Zoom offers three botless routes: cloud-recording transcript files + webhooks (needs cloud recording and transcription on), the AI Companion meeting summary API/webhook (summary, not full transcript), and RTMS (live audio/video/diarized transcript, GA since June 2025, paid by Developer Pack credits). All depend on the host's account settings.

### Cited Findings
- RTMS "gives your app access to live audio, video, and transcript data from Zoom meetings"; available with Zoom Meetings, Zoom Contact Center and Zoom Video SDK; positioned as replacing bots: "Instead of having participant bots or automated clients in meetings, use RTMS apps to collect the media data from the meeting" — https://developers.zoom.us/docs/rtms/ (opened)
- RTMS for meetings: apps "can auto-start when users join meetings and webinars"; streams started via REST API or JS SDK; delivers "diarized transcripts that include not only what was said but who said it and when"; HD video up to 30 fps; participant join/leave events — https://developers.zoom.us/docs/rtms/meetings/ (opened)
- RTMS cost: "To use RTMS, you'll need Zoom Developer Pack credits on your account"; plan options and concurrent stream limits are on the Developer pricing page; commitments above 500 credits go through sales — https://developers.zoom.us/docs/rtms/meetings/ (opened)
- RTMS reached GA on 2025-06-25 ("all developers can start building with RTMS today") — https://developers.zoom.us/changelog/rtms/june-25-2025/ (search summary). Self-service purchasing was later added — https://devforum.zoom.us/t/rtms-self-service-purchasing-is-now-available/144524 (search summary)
- No public per-minute RTMS rate was found; a developer-forum thread on pricing for external meeting capture reports no published schedule — https://devforum.zoom.us/t/pricing-feasibility-validation-rtms-vs-linux-sdk-for-external-meeting-capture/141332 (search summary)
- Meeting summary API: GET /meetings/{meetingId}/meeting_summary returns the AI Companion summary; webhook event meeting.summary_completed; scopes cited: meeting_summary:read, meeting_summary:read:admin, and granular meeting:read:summary; prerequisites: host on Pro or higher, Meeting Summary with AI Companion enabled, not available for E2EE meetings — https://developers.qodex.ai/zoom-public/zoom-meeting-api/meetings-meetingid-meeting_summary/get-a-meeting-summary (search summary; mirror of Zoom API reference); https://devforum.zoom.us/t/how-to-enable-event-subscription-for-meeting-summary-completed/98966 (search summary)
- Cloud recording transcript: webhook recording.transcript_completed fires only for Cloud Recording transcripts (recording must actually start and audio transcription must be enabled); scopes cited include cloud_recording:read:recording and cloud_recording:read:meeting_transcript; a summary can complete without this event firing — https://community.zoom.com/ai-companion-21/meeting-summary-not-trigger-recording-transcript-completed-event-75486 (search summary)
- Reliability reports: multiple developer-forum threads report missing summary or transcript webhooks despite validated endpoints (unverified user reports) — https://devforum.zoom.us/t/missing-recording-transcript-completed-webhook-events/133118 (search summary); https://devforum.zoom.us/t/ai-companion-meeting-summary-webhook-event-missing/144225 (search summary)

### Inferences
- For QW, the cheapest Zoom path is "consume": subscribe to transcript/summary webhooks through an admin-installed OAuth app. It only works when the customer's hosts record to cloud or use AI Companion, and it yields post-meeting data only. RTMS removes the recording dependency but adds per-usage credits and Marketplace app review.
- All three routes are host-account scoped: a 1-on-1 hosted by someone outside the customer tenant is invisible.

### Gaps
- Unknown: RTMS credit price, participant-notice UX and account settings required (the linked ux-overview and getting-started pages were not opened).
- Unknown: Zoom Meeting SDK bot requirements (raw-data access, Marketplace approval, obligation to show recording consent); no primary source opened.
- Unknown: transcript file format details and plan tier for cloud-recording transcription from official docs.

---

## B2. Microsoft Graph options

### Takeaway
Graph transcript and recording APIs are GA and, since 2025-08-25, no longer metered. Access needs either tenant-wide application permissions (admin consent plus an application access policy) or per-meeting resource-specific consent; from end of July 2026 tenant admins also have two switches that can block Graph transcript access or strip speaker attribution. The Meeting AI Insights API returns Copilot summaries/action items but only for Copilot-licensed users with delegated auth.

### Cited Findings
- "Starting August 25, 2025, the Teams APIs listed in this article are no longer metered, and no billing configuration is required to use these APIs" — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened; updated 2026-11-02)
- Historic pricing for context: earlier Microsoft pages listed transcript APIs at $0.0022 per minute with a 600 minutes/month evaluation quota per tenant per app — https://learn.microsoft.com/en-us/graph/teams-licenses (search summary; page redirected when fetched)
- Scope: apps can fetch transcripts (.vtt) and recordings (.mp4) after a scheduled online meeting or an ad hoc call (PSTN, 1:1, group calls) ends — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened)
- Two permission models: organization-wide application permissions (admin authorizes; app can read transcripts and recordings for all meetings in the tenant; organizer need not install the app) or meeting-specific RSC permissions (app installed in the meeting chat; fetches only that meeting). RSC is not enabled for ad hoc calls — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened)
- Permissions: delegated OnlineMeetingTranscript.Read.All (online meetings), CallTranscripts.Read.All (ad hoc calls); application OnlineMeetingTranscript.Read.All, OnlineMeetingTranscript.Read.Chat (RSC, scheduled private chat meetings only, not channel meetings) — https://learn.microsoft.com/en-us/graph/api/calltranscript-get (opened)
- "To use application permission for this API, tenant administrators must create an application access policy and grant it to a user" — https://learn.microsoft.com/en-us/graph/api/calltranscript-get (opened)
- Tenant admin controls (take effect end of July 2026): (1) "Graph API access to transcripts": when disabled all transcript requests return 403 GraphAccessToTranscriptsDisabled, "There is no request-side workaround"; (2) "Speaker attribution": when disabled, content is retrievable only in the unattributed format application/vnd.microsoft.graph.transcript+text; requesting text/vtt returns 403 SpeakerAttributionNotAllowed. Configured in Teams Admin Center or Set-CsTeamsMeetingConfiguration — https://learn.microsoft.com/en-us/graph/api/calltranscript-get (opened)
- Change notifications: tenant-level (communications/onlineMeetings/getAllTranscripts, communications/adhocCalls/getAllTranscripts), meeting-level, user-scoped (users/{userId}/onlineMeetings/getAllTranscripts) and app-scoped (appCatalogs/teamsApps/{id}/installedToOnlineMeetings/getAllTranscripts) subscriptions exist — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened)
- Limits: "These APIs support private chat meetings, channel meetings, and ad hoc calls only in beta"; the API works only if the meeting hasn't expired; getAll APIs aren't available for ad hoc call instances — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened); https://learn.microsoft.com/en-us/graph/api/calltranscript-get (opened)
- Microsoft's own doc suggests a pattern for avoiding slow admin approval: app sets AutoRecording=true, adds a bot participant to display a banner, and uses RSC — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened)
- Microsoft's doc lists an HR use case (brainstorm on employee health; "engagement and sentiment analysis") as a sanctioned use — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened)
- Meeting AI Insights API: returns AI-generated summaries, action items and mentions; endpoint GET /copilot/users/{userId}/onlineMeetings/{onlineMeetingId}/aiInsights; delegated permissions only; insights only on behalf of a Microsoft 365 Copilot licensed user; can take up to four hours after the call ends; channel meetings not supported; GA status not confirmed (docs variously show v1.0 and beta) — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/meeting-insights (search summary); https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/api/ai-services/meeting-insights/callaiinsight-get (search summary)

### Inferences
- Graph is now free and the most complete botless route for Teams, but it is the most admin-dependent: Entra admin consent, an application access policy, transcription turned on per meeting, and (since mid-2026) two tenant kill-switches. HR-sensitive tenants may well disable speaker attribution, which would break who-said-what for 1-on-1 analysis.
- The speaker-attribution switch signals Microsoft treating attributed transcripts as a privacy-sensitive asset; QW should design for unattributed input.

### Gaps
- Unknown: whether the two tenant switches default to on or off.
- Unknown: real-time (in-meeting) media access terms for Teams bots (Graph communications/real-time media bots, compliance recording certification); not researched.

---

## B3. Google Meet developer options

### Takeaway
The Meet REST API (GA) gives post-meeting conference records, transcripts, transcript entries, recordings and (since April 2026) Gemini smart notes, with Workspace Events subscriptions. The real-time Meet Media API never left Developer Preview and Google is shutting it down on 2027-01-15, so there is no sanctioned botless real-time path on Meet.

### Cited Findings
- 2026-10-28 release note (Deprecated, Meet Media API): "we have decided to wind down the Google Meet Media API and permanently turn down its endpoints on January 15, 2027"; Developer Preview participants keep access until then; Meet REST API and Meet Add-ons SDK are not affected — https://developers.google.com/workspace/meet/release-notes (opened)
- Media API launched in Developer Preview on 2025-02-24 — https://developers.google.com/workspace/meet/release-notes (opened)
- Media API preview limits: the Cloud project, OAuth principal and all participants in the conference had to be enrolled in the Developer Preview Program — https://developers.google.cn/workspace/meet/media-api/guides/get-started?authuser=0 (search summary); only the 3 most relevant participants' audio/video delivered at a time; connection rejected if client-side encryption or watermarking is on — https://docs.recall.ai/docs/google-meet-media-api (search summary; vendor doc)
- 2026-04-02: smartNotes get and list methods and smartNote.v2 started/ended/fileGenerated event subscriptions became GA — https://developers.google.com/workspace/meet/release-notes (opened)
- 2025-11-12: calendar invitees can receive conference.v2.started and transcript.v2.fileGenerated events (GA) — https://developers.google.com/workspace/meet/release-notes (opened)
- 2025-02-07: all participants can query conference records, artifacts and participant records (GA); a non-sensitive scope meetings.space.settings allows setting up auto-artifacts — https://developers.google.com/workspace/meet/release-notes (opened)
- Artifacts guide: artifacts must be turned on in Meet "before the conference ends"; "you don't have to record the meeting to generate a transcript"; meeting space owners or participants can call get and list; auth via user credentials or domain-wide delegation (service account, no per-user consent) — https://developers.google.com/workspace/meet/api/guides/artifacts (opened)
- "Transcript entries provided by the Meet REST API are deleted 30 days after the conference ends"; entries may not match the Docs transcript file if it was edited; results cannot be filtered — https://developers.google.com/workspace/meet/api/guides/artifacts (opened)

### Inferences
- With the Media API gone, capture on Meet is: (a) consume Google's own transcript/smart-notes via REST after the meeting (requires the customer edition to have transcripts/Gemini notes and a user to turn them on or pre-configure auto-artifacts), (b) a bot, or (c) desktop capture. This strengthens the business of bot vendors on Meet.
- Structured transcript entries expire after 30 days, so ingestion must be prompt.

### Gaps
- Unknown: Meet add-ons capability to read live captions/audio (a Google developer forum thread asks this; no official answer found) — https://discuss.google.dev/t/how-can-a-public-google-meet-add-on-access-real-time-participant-audio-without-a-bot/385365 (search summary)
- Unknown: OAuth scope sensitivity/verification burden for Meet REST transcript scopes; cost (no API fee was found or ruled out).

---

## B4. Meeting-bot and capture infrastructure vendors

### Takeaway
Recall.ai is the scale leader (Series B, $250M valuation, HR-tech logos including 15Five, Rippling, Deel, Leadr, ClearCompany, BrightHire) at $0.50 per recording hour for both bots and its Desktop Recording SDK. Cheaper hosted rivals sit around $0.35 to $0.80/hour; open-source options (Attendee, Vexa) trade fees for self-hosting.

### Cited Findings
- Recall.ai pricing: Meeting Bot API and Desktop Recording SDK both $0.50 per recording hour pay-as-you-go, prorated to the second; first 5 hours free; startup programme $0.25/hr for first 10,000 hours; built-in transcription +$0.15/hr (third-party STT also supported); storage free 7 days then $0.05/hr per 30 days; Calendar API free; Launch and Enterprise custom; data residency US, EU or JP; BAA on Enterprise; footer references SOC 2, ISO 27001, HIPAA, GDPR, CCPA — https://www.recall.ai/pricing (opened)
- Recall.ai cut pay-as-you-go from $0.70 to $0.50 per recording hour for 2026 — https://www.recall.ai/blog/new-recall-ai-pricing-for-2026 (search summary)
- Recall.ai funding: $38M Series B (September 2025) led by Bessemer; total $51M; $250M valuation — https://www.axios.com/pro/enterprise-software-deals/2025/09/04/recallai-38-million-series-b-bessemer (search summary)
- Recall.ai HR page logos ("Trusted by leading companies, including"): Rippling, Fellow, Deel, 15Five, Leadr, ClearCompany, BrightHire; BrightHire VP Engineering quote: "Offloading our recorder to Recall has been a huge sigh of relief." The page recommends Meeting Bot API (visible bot so participants know), Desktop Recording SDK (botless, virtual/hybrid/in-person) and Calendar API (auto-schedule, filter by "1:1" in title) for 1:1 notetakers — https://www.recall.ai/solutions/hr (opened)
- Recall.ai recruiting page names Greenhouse, Deel and Ashby as using its data for interview notes — https://recall.ai/solutions/recruiting (search summary). Pricing page case studies: ClickUp, Apollo.io, Incident.io, BrightHire — https://www.recall.ai/pricing (opened)
- Platforms shown on Recall pricing page: Google Meet, Microsoft Teams, Zoom, Slack, Webex, GoTo Meeting — https://www.recall.ai/pricing (opened)
- Nylas Notetaker: Free 5 bot hours; Essentials $15/month incl. 10 hours then $0.80/hr; Pro $49/month incl. 70 hours then $0.70/hr ($43 and $0.65 annual); Enterprise custom. Every plan includes bot API, calendar sync, speaker-labelled transcription, recording, AI summaries and action items, UI components, white-labelling, deduplication, per-customer retention settings, custom chat announcements. Platforms: Google Meet, Microsoft Teams, Zoom — https://www.nylas.com/pricing/ (opened)
- Recall.ai's vendor-authored benchmark claims transcription error rates of 22.2% (Meeting BaaS), 27.0% (Skribby), 47.1% (Nylas) and a 12% Zoom recording success rate for Meeting BaaS; treat as self-interested and unverified — https://www.recall.ai/recall-ai-competitors (opened; vendor-authored)
- MeetingBaaS: $0.69/hour pay-as-you-go or subscription per an undated DEV post; other secondary sources say roughly $0.35 to $0.50/hour — https://dev.to/lirim_kon/3-best-alternatives-to-recallai-398n (search summary); https://www.nylas.com/blog/best-meeting-bot-apis/ (search summary; vendor-authored)
- Skribby: about $0.35/hour base, roughly $0.39 to $0.70 with transcription (single third-party guide) — https://www.nylas.com/blog/best-meeting-bot-apis/ (search summary; vendor-authored)
- Attendee: open-source API for managing meeting bots on Zoom/Google Meet, self-hostable or hosted — https://github.com/attendee-labs/attendee (search summary). Case study: Chitti records 18,000+ hours of classes monthly self-hosting Attendee, avoiding per-hour cloud bot pricing — https://attendee-website-2.pages.dev/case_studies/chitti.html (search summary). Gladia documents an Attendee integration — https://docs.gladia.io/chapters/integrations/attendee (search summary)
- Vexa: open source, self-hosted, no per-hour vendor fee (secondary) — https://www.nylas.com/blog/best-meeting-bot-apis/ (search summary)
- Fireflies API: GraphQL API exposes transcripts and core meeting data but not Super Summaries or Custom Apps output; a comparison page says Fireflies lacks webhooks/OAuth 2.0 while tl;dv has public API, webhooks and OAuth 2.0 (weak source) — https://circleback.ai/compare/tldv-vs-fireflies-ai.md (search summary; competitor-authored)
- MeetStream listed at $0.35 per bot-hour (secondary) — https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/ai-meeting-transcription-tooling-landscape (search summary)
- Recall.ai also wraps Zoom RTMS and documented the Meet Media API, i.e. it abstracts botless platform routes as well — https://www.recall.ai/product/rtms (search summary); https://docs.recall.ai/docs/google-meet-media-api (search summary)

### Inferences
- HR/performance peers (15Five, Leadr, ClearCompany, Rippling, Deel) appear on Recall's HR page, which suggests "buy capture" is the norm in QW's category. The page shows logos only; it does not say which product each uses or for what.
- At $0.50 to $0.65/hour all-in (capture + built-in transcription), a manager with four 30-minute 1-on-1s a week costs roughly $4 to $6/month in capture COGS (my arithmetic: 2 h/week x 4.33 weeks x $0.50 to $0.65).

### Gaps
- Unknown: official MeetingBaaS, Skribby, Vexa pricing pages, licences (Attendee/Vexa licence terms) and funding; not opened.
- Unknown: Recall.ai customer count / hours recorded; tl;dv API pricing from an official source.
- Unknown: whether Lattice, Culture Amp, Leapsome, Workday use a vendor or build; no source found.

---

## B5. Speech-to-text vendors

### Takeaway
Batch STT is a commodity at roughly $0.15 to $0.30 per audio hour with diarization usually included; it is a small fraction of the capture cost. Only Deepgram's prices were verified on a primary page in this run.

### Cited Findings
- Deepgram (official): Nova-3 monolingual pre-recorded $0.0043/min ($0.258/hr) pay-as-you-go, $0.0036/min on Growth; streaming $0.0048/min; multilingual pre-recorded $0.0052/min; Flux English streaming $0.0065/min; diarization included for pre-recorded, +$0.0020/min streaming; $200 non-expiring free credit; Growth from $4,000/year prepaid — https://deepgram.com/pricing (opened)
- AssemblyAI (secondary): about $0.15/hr Universal-2 pre-recorded and $0.21/hr Universal-3.5 Pro as of late 2026; sources disagree on whether diarization is included or a $0.02/hr add-on — https://dupple.com/learn/assemblyai-pricing (search summary); https://www.costbench.com/software/ai-transcription-apis/assemblyai/ (search summary)
- Gladia (secondary, May 2026 snapshot): $0.61/hr async, $0.75/hr real-time on Starter; Gladia says diarization is bundled on async — https://www.xpay.sh/saas-pricing/gladia (search summary); https://www.gladia.io/blog/cutting-transcription-cost-per-audio-hour-for-meeting-assistants (search summary; vendor-authored)
- Speechmatics (secondary, conflicting): $0.24/hr batch standard per one snapshot — https://www.xpay.sh/saas-pricing/speechmatics (search summary); a different aggregator shows other figures — https://www.costbench.com/compare/assemblyai-vs-speechmatics/ (search summary)
- OpenAI: gpt-4o-mini-transcribe normalised to about $0.18/hr by one comparison — https://diyai.io/ai-tools/speech-to-text/speech-to-text-api-pricing/ (search summary; attribution uncertain)
- Recall.ai resells built-in transcription at $0.15/hr and supports third-party providers — https://www.recall.ai/pricing (opened)

### Inferences
- If QW consumes a platform-produced transcript, STT cost is zero and accuracy/diarization are whatever the platform gives; if QW captures audio, STT adds roughly $0.15 to $0.26/hour.

### Gaps
- Unknown: accuracy positioning (WER benchmarks) from neutral sources; notable customers per STT vendor; which STT Granola, Fireflies and HR platforms use; Rev.ai and gpt-4o-transcribe list prices. None verified.

---

## B6. Botless desktop capture versus bots

### Takeaway
Botless capture records system audio plus microphone on the user's machine: Core Audio process taps (macOS 14.2+) or ScreenCaptureKit on macOS, WASAPI loopback on Windows. It avoids a visible bot and host permission, at the cost of an installed app, OS permissions and harder speaker attribution.

### Cited Findings
- macOS: Core Audio process taps require macOS 14.2 or later; earlier versions need a virtual loopback driver; ScreenCaptureKit is the alternative and needs Screen Recording permission; Apple's documentation for taps is limited — https://www.recall.ai/blog/core-audio-taps (search summary; vendor blog); https://www.recall.ai/blog/how-to-use-screencapturekit-to-record-a-meeting (search summary)
- Windows: WASAPI loopback has long been the standard way to capture system audio and needs no virtual driver — https://www.recall.ai/blog/windows-wasapi (search summary; vendor blog)
- Diarization lever: splitting capture into two channels (microphone = local user, system audio = remote side) supports speaker recognition — https://abit.ee/ru/sowtware/messendzery/notta-bot-free-meeting-recording-transcription-macos-windows-privacy-news-ru (search summary; weak source)
- Recall's Desktop Recording SDK claims "reliable audio and video recording, diarized transcripts with speaker names, and metadata", meeting detection, mute detection, and that a desktop recorder "does not require users to be the host in order to record"; bots join as "a separate participant" while desktop recorders "capture meeting data locally" — https://www.recall.ai/blog/desktop-recording-sdk (opened; vendor blog)
- Zoom positions RTMS as the alternative to "participant bots or automated clients" — https://developers.zoom.us/docs/rtms/ (opened)
- Some enterprises explicitly warn about third-party AI bots in meetings — https://services.northwestern.edu/TDClient/30/Portal/KB/ArticleDet?ID=2893 (search summary)
- Granola (desktop AI notepad) raised $125M Series C at a $1.5B valuation in March 2026, led by Index Ventures, and launched team workspaces and enterprise APIs — https://www.bloomberg.com/news/articles/2026-03-25/ai-notetaker-granola-hits-1-5-billion-value-in-125-million-funding (search summary)

### Inferences
- For a 1-on-1, two-channel desktop capture gives near-perfect two-speaker separation when both people are remote (mic vs system audio); it degrades for in-person 1-on-1s on one device, where acoustic diarization is needed.
- Tradeoffs for QW: a bot is visible (built-in notice, no install, works on any device, but can be blocked by host/admin and feels intrusive in a sensitive 1-on-1); desktop capture is invisible to the other party (so consent/notice must be built by QW), requires IT to deploy a signed app and grant macOS audio/screen permissions, and covers in-person and any platform including Slack huddles.
- Zoom My Notes, Google "take notes with me" and Facilitator mobile capture show the platforms themselves moving to device-side and in-person capture.

### Gaps
- Unknown: quantified accuracy difference between bot and botless diarization (no neutral source).
- Unknown: exact macOS permission prompts for taps versus ScreenCaptureKit on current macOS, MDM pre-approval options, and Windows consent behaviour; only vendor blogs surfaced.
- Unknown: whether Granola's capture is botless per a primary source (widely described so, not verified here).

---

## B7. Build versus buy

### Takeaway
Evidence in this run points to "buy capture, build the insight layer": HR and recruiting platforms appear as Recall.ai logos, vendors bundle bots + calendar + STT for under $1/hour, and platform changes (Meet Media API shutdown, new Teams tenant switches) make owning capture a moving target.

### Cited Findings
- HR/people platforms shown as Recall.ai customers: Rippling, Deel, 15Five, Leadr, ClearCompany, BrightHire, plus Fellow (meeting notes) — https://www.recall.ai/solutions/hr (opened)
- BrightHire describes offloading its recorder to Recall as "a huge sigh of relief", i.e. a product that previously built capture moved to buy — https://www.recall.ai/solutions/hr (opened)
- A large self-hoster exists: Chitti records 18,000+ hours/month on self-hosted open-source Attendee to avoid per-hour fees — https://attendee-website-2.pages.dev/case_studies/chitti.html (search summary)
- Platform risk examples: Google shutting down Meet Media API on 2027-01-15 — https://developers.google.com/workspace/meet/release-notes (opened); Microsoft adding tenant switches that return 403 for Graph transcript access or speaker attribution — https://learn.microsoft.com/en-us/graph/api/calltranscript-get (opened)
- Microsoft removed metering from transcript APIs on 2025-08-25, making "consume the native transcript" free on Teams — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts (opened)

### Inferences
- A pragmatic QW architecture is hybrid: (1) consume native transcripts where the customer already produces them (Graph, Zoom webhooks/summary API, Meet REST), which is cheapest and inherits the customer's own notice/retention governance; (2) fall back to a bought bot or desktop SDK where no native transcript exists.
- "Consume" depends on customer licences (Copilot/Teams Premium, Gemini editions, Zoom paid) and on admins enabling transcription and third-party access; coverage will be uneven across QW's customer base.

### Gaps
- Unknown: direct statements from Lattice, Culture Amp, Leapsome, Workday, 15Five about their capture architecture; searches returned nothing.
- Unknown: share of notetaker products that build versus buy; no survey or neutral data found.
