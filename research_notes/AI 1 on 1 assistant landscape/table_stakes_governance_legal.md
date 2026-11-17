# Table-stakes trust, privacy, governance, and compliance features for AI meeting recorders (emphasis: manager-employee 1-on-1s in an HR platform) and the legal environment driving them

Research date: 2026-11-17 (America/Chicago). This is product research, not legal advice; every legal point needs review by counsel before it is relied on.

Verification key used throughout:
- [OPENED] = the page itself was fetched and read.
- [SNIPPET] = taken from a search-result summary; the page was not opened. Treat as a lead to verify.
- Unknown = could not be verified from a source in this pass.

Source-quality warning: much 2026 coverage of AI-notetaker lawsuits and vendor comparisons comes from competing notetaker vendors' blogs (scribbl.co, tldv.io, getvoibe.com, basilai.app, getmeetly.ai, etc.). These have a commercial interest in making rivals look risky. Where they are the only source, it is flagged.

---

## 1. Consent and notice features (announcements, opt-in, opt-out, employee ability to decline, "dual consent")

### Takeaway
A visible or announced notice that recording is happening is universal among bot-based tools; what varies is whether consent is passive (a bot is visible, a banner appears) or active (each participant must agree, and a decline stops capture). The August 2026 Otter ruling refused to treat a visible notetaker as consent at the pleading stage, which raises the bar from "notice" toward "affirmative, logged consent."

### Cited Findings
HR-platform 1:1 assistants
- Lattice AI Agent in 1:1s: must be invited by a participant and "never joins automatically, unless an admin has enabled auto-add"; on joining it "clearly announces itself in-meeting with a disclosure that the meeting is being recorded and transcribed for Lattice meeting insights"; either participant can remove it "at any time." [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Lattice: when Lattice AI and 1:1s are enabled, all employees with 1:1s enabled receive a notification that AI Agent in 1:1s is on. [SNIPPET] https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention
- 15Five Kona: if captions are off, the Kona Notetaker asks in the meeting chat for permission to record; if recording is denied, no notes are made. No other consent mechanism is described in the privacy article. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731
- 15Five Kona joins as a visible participant; "can begin note-taking automatically or ask for permission to record, based on your Zoom settings"; 15Five supplies a suggested script for managers to introduce Kona to direct reports. [SNIPPET] https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide and https://success.15five.com/hc/en-us/articles/50988761575195
- Leapsome Meeting Notetaker: "all participants get a clear notice for compliance" before recording starts; the delivery mechanism and any opt-in/opt-out are not stated on the page. [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent

General-purpose notetakers
- Fireflies emails participants about an hour before the meeting with a link to decline. [SNIPPET, third-party comparison] https://verifier.org/ai-meeting-notetakers
- Fathom: admins can set "Auto Request Recording Consent" to enabled for all; external participants get an email 24 hours before scheduled meetings; Fathom warns users that some jurisdictions require everyone's consent. [SNIPPET, third-party] https://www.getvoibe.com/resources/is-fathom-safe/
- Read.ai: bot announces itself and needs host approval; any participant can type "opt out" in chat to stop and delete the meeting. [SNIPPET, third-party] https://verifier.org/ai-meeting-notetakers
- Otter recommends combining pre-recording emails with the bot's chat announcement. [SNIPPET, third-party] https://www.getvoibe.com/resources/ai-notetaker-recording-consent-laws/
- Gong: recommends a "consent page" to capture active consent before a participant joins; supports customizable pre-call consent emails and pages in 70+ languages with a link to the customer's privacy policy; if opt-out is allowed and a participant opts out, the meeting proceeds but is not recorded. [SNIPPET, vendor help/blog] https://help.gong.io/docs/security-compliance and https://www.gong.io/blog/security-best-practices-for-the-gong-revenue-ai-os
- Granola (botless): offers a chat message posted when transcription starts and a video watermark; both are opt-in, off by default; setting is under Settings > Labs ("Let others know you're using Granola"), Zoom and Google Meet on macOS; org-wide admin enforcement is reported as Enterprise-only. [SNIPPET] https://www.granola.ai/blog/ai-notetaker-participant-privacy-consent and https://docs.granola.ai/help-center/consent-security-privacy/transparency-solutions/introduction ; Enterprise-only claim from a competitor review: https://tldv.io/blog/granola-review/

Platform-native assistants
- Google Meet Gemini notes: participants see a consent banner; organizers are told to confirm consent from external participants; a Workspace admin can require explicit consent for recording, transcripts, and Gemini notes (off by default). [SNIPPET, third-party guides] https://www.vecosys.com/ai-meeting-notes-consent-checklist/ and https://www.alphonsolabs.com/ai-meeting-notes-consent-checklist/
- Zoom: admins control recording disclaimers and phone-user consent prompts; participants see an AI indicator for native features. One source says Zoom's AI whitepaper states no Zoom indicator is shown to participants when Zoom transcribes a Teams or Google Meet call. [SNIPPET, third-party] https://nhimg.org/ai-meeting-assistant-security-guide
- Microsoft Teams Copilot: with transcription, participants get the transcription notice; in the "without transcription" mode the participant notice is "not stated" in the source found. [SNIPPET, third-party] https://www.reline.so/blog/do-zoom-meet-teams-notify-when-you-record

Guidance on what counts as consent
- SHRM CHRO Jim Link (HR Dive, 2026-09-14): SHRM encourages HR to disclose AI tool use and get approval from everyone present before any recording or transcription; "Transparency is absolutely part of the employee experience." Barnes & Thornburg partner Brian McGinnis: some platforms may not tell participants a recording is running or will be transcribed or reused; with participants in multiple states, HR may need to collect consent manually if the tool lacks an opt-out. [OPENED] https://www.hrdive.com/news/hr-must-set-boundaries-ai-notetakers/830276/
- GDPR commentary: "By joining this call, you consent" is not valid consent under GDPR; employees must be able to refuse without consequences. [SNIPPET, vendor blog] https://meetergo.com/en/magazine/ai-meeting-notes-gdpr

### Inferences
- Table stakes: in-meeting announcement or visible indicator; ability for any participant (including the employee) to remove or stop the recorder; agent not joining unless invited or admin-enabled.
- Common: pre-meeting notification emails (Fireflies, Fathom, Gong); org-level admin setting to force consent prompts (Fathom, Google, Gong).
- Differentiating: per-participant affirmative opt-in that blocks capture until given and is logged (Gong consent page is the closest documented example; 15Five's chat permission request is a lighter version); employee-initiated pause mid-meeting with partial-transcript handling; a recorded consent trail exportable for audit.
- "Dual consent" as QW's draft frames it is not a named standard feature anywhere found. The nearest documented equivalents are Lattice (either party can remove the agent) and 15Five (chat permission; denial means no notes). A true two-sided opt-in where the direct report must affirmatively accept, separately from the manager, would be at or ahead of the HR-platform peers, and it lines up with the direction of the Otter ruling.
- The manager-employee power imbalance weakens passive consent: an employee may not feel free to remove a bot the manager invited. This is an inference from the GDPR "refuse without consequences" point, not a sourced finding about US law.

### Gaps
- Exact wording and delivery of Leapsome's notice; whether the employee can decline: Unknown (page does not state).
- Notion AI Meeting Notes and Fellow consent mechanics: no source retrieved in this pass. Unknown.
- Official Microsoft, Google, and Zoom documentation was not opened; platform-native facts above rest on third-party guides.
- No vendor found that documents a consent log (who consented, when) as an exportable artifact, other than Gong's "documented consent" language in a third-party privacy notice. Unknown whether others have it.

---

## 2. Retention features (defaults, admin-configurable, auto-deletion, audio/video discard, legal hold)

### Takeaway
Among HR-platform peers, the norm is "no audio/video kept, transcripts short-lived or off by default." Lattice stores no transcript unless an admin turns it on; 15Five deletes transcripts after 30 days and exposes them to no one. QW's "customizable transcript retention policy" matches Lattice but is not ahead of it.

### Cited Findings
- Lattice: does not collect audio/video ("Lattice does not collect audio/video data from the meeting"); transcripts are not retained by default; admins can set retention "in one-month increments, up to 12 months"; Recall.ai (the bot infrastructure) deletes its copies "within minutes after processing." The page's FAQ also says retained transcripts follow "the life of contract plus 180 days," which conflicts with the 12-month cap; unresolved. [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Lattice admin path: Admin > Agent in 1:1s > "Store transcripts" toggle. [SNIPPET] https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention
- 15Five Kona: "Kona never stores recordings, only transcripts"; transcripts are encrypted and stored 30 days for quality assurance, then permanently deleted, not archived; 1-on-1 notes (talking points, shared notes, action items) are retained separately until account sanitization 90 days after deactivation or PII deletion of a participant. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731
- 15Five conflict: another 15Five help article is reported to say the recording and transcript are deleted after the meeting ends. [SNIPPET] https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- Leapsome: "Admins control recording, retention, and which meetings it joins"; periods and audio handling not stated. [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent
- Gong: default retention is the lesser of three years and the customer term; admins change it under Admin center > Settings > Data protection & privacy; shortened retention purges irrecoverably; custom periods on request; data deleted 30 days after contract termination. [SNIPPET, vendor] https://help.gong.io/docs/data-retention-policy and https://www.gong.io/platform/trust
- Granola: says it transcribes in real time and deletes audio immediately; a third-party review says notes are kept indefinitely in Granola's US cloud by default. [SNIPPET] https://www.granola.ai/blog/ai-notetaker-participant-privacy-consent ; contradicted on notes retention by https://www.getvoibe.com/resources/is-granola-safe/
- Fathom: automatic deletion is Enterprise-only. Otter: deleted items sit in trash 30 days before purge. Read.ai: audio/video retention at most 2 years. Fireflies: deletes data within 30 days of account closure. [SNIPPET, third-party comparisons] https://verifier.org/ai-meeting-notetakers and https://www.getvoibe.com/resources/is-fathom-safe/
- Fellow: one comparison credits Fellow with configurable zero-day retention. [SNIPPET, Fellow's own blog is among the sources] https://fellow.ai/blog/ai-note-takers-for-fintech/
- Zoom: hosts can optionally keep the transcript; account owners decide whether transcripts are retained for other AI Companion services. Google Meet: transcripts save to the organizer's Drive; Vault retention rules apply. Teams: retention follows Microsoft 365/Purview policy. [SNIPPET, third-party] https://nhimg.org/ai-meeting-assistant-security-guide
- Microsoft Teams Copilot policy values reported as Enabled, EnabledWithTranscript ("On with saved transcript required", the default), EnabledWithTranscriptDefaultOn, Disabled; a mode exists that runs Copilot during the meeting without retaining a transcript. [SNIPPET, third-party] https://www.banthebots.org/explainers/how-to-turn-off-ai-notetakers
- Law-firm guidance: align notetaker retention with litigation holds; set retention limits, deletion workflows, and consent logs; long retention expands hold scope and e-discovery cost. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- Retention must be set per artifact: deleting the video may not delete the transcript or metadata. [SNIPPET] https://www.learnsignal.com/blog/ai-meeting-notes-and-transcription-at-work/

### Inferences
- Table stakes (HR-platform context): no audio/video storage; admin-configurable transcript retention with auto-deletion.
- Common: transcript retention off or short by default (Lattice off; 15Five 30 days).
- Differentiating: legal hold that suspends auto-deletion for named people or matters; separate retention clocks for transcript, summary, and derived signals; a "summary only, never store transcript" mode comparable to Teams' no-transcript Copilot mode.
- The derived artifacts matter more than the transcript. Both Lattice and 15Five keep notes/insights far longer than transcripts. QW's plan to feed signals into performance means the signals, not the transcript, become the long-lived record, and retention messaging should cover them explicitly.

### Gaps
- Legal hold: no HR-platform vendor page found describes one. Lattice's privacy page does not address it. Unknown for 15Five and Leapsome.
- Lattice's 12-month cap versus "contract plus 180 days": unresolved conflict in Lattice's own documentation.
- Official default retention for Otter, Fireflies, Read.ai, Notion: not verified from vendor pages. Unknown.

---

## 3. Access and visibility (transcripts vs summaries; HR admin access; RBAC; sharing)

### Takeaway
The two closest HR-platform competitors both lock HR and admins out of 1:1 transcript content. Lattice limits transcripts and insights to the two participants even under admin impersonation; 15Five exposes raw transcripts to no one at all. Any QW design that lets HR admins read 1:1 transcripts would be an outlier against peers.

### Cited Findings
- Lattice: transcripts visible only to meeting participants; admins, custom role owners, and HRBPs cannot view or download transcripts or insights; "Even users with admin or impersonation access cannot view meeting transcripts or insights" unless they were participants; only participants can download. [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- Lattice has a separate article on configuring custom-role permissions for AI Agent in 1:1s. [SNIPPET, title only] https://help.lattice.com/en-us/articles/16541145-configure-custom-role-lattice-ai-agent-in-1-1s-permissions
- 15Five: transcripts are inaccessible in the app and via the 15Five MCP to HR admins, other managers, 15Five admins, and employees; raw transcripts are not shared for compliance or audit purposes; coaching prompts are visible only to the manager (delivered via Slack, Teams, or the Kona Coach page) and shared only if the manager chooses. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731
- 15Five: notes and summaries are private to the manager and direct report; HR admins cannot see 1:1 note content without the manager's explicit consent; exception: HR admins with Kona Coach access get coaching tips after their own 1-on-1s. [SNIPPET] https://success.15five.com/hc/en-us/articles/42810346409627-Kona-Meeting-Assistant-Setup-and-Support-Guide
- 15Five: Kona 1:1 data can feed "Moments" a review writer sees in AI-assisted review cycles; "AI strictly mirrors existing system permissions." [SNIPPET] https://success.15five.com/hc/en-us/articles/50988127315355-How-15Five-AI-works-together
- Leapsome: "The Meeting Notetaker only surfaces information the user can already see"; "Permissions stay as configured." [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent
- Mayer Brown: limit vendor and internal access to need-to-know personnel; vendor access to recordings can undermine privilege. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk

### Inferences
- Table stakes (HR 1:1 context): participant-only visibility of transcript and summary; HR/admin lock-out from raw 1:1 content; permission mirroring of existing 1:1 privacy rules.
- Common: manager-only coaching output (15Five).
- Differentiating: explicit, employee-visible disclosure of exactly which derived signals leave the 1:1 and who sees them; employee-side view of what the manager's coaching was based on.
- 15Five's asymmetry is a watch item: the employee cannot see the transcript or the manager's coaching prompts, yet 1:1 content can inform review "Moments." That is a surveillance-objection opening QW could position against, if QW gives the employee symmetric visibility.

### Gaps
- Whether a Lattice or 15Five customer's manager's manager can see summaries: not stated by either.
- Access model for Otter/Fireflies/Fathom/Read.ai workspace admins over private meetings: not verified. Unknown.

---

## 4. Editing, redaction, deletion, and sensitive-topic handling

### Takeaway
Participant deletion exists at Lattice; transcript redaction and sensitive-topic auto-exclusion are barely documented anywhere. QW's "transcript review and redaction" appears to be ahead of HR-platform peers on the evidence found, though the evidence is thin.

### Cited Findings
- Lattice: participants can delete transcripts; deletion by one participant removes it only from that person's view; the transcript is permanently deleted only when both delete. Participants can download. Sensitive-topic handling is not addressed on the privacy page. [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy and [SNIPPET] https://help.lattice.com/hc/en-us/articles/40791546070039-Delete-a-Lattice-AI-Agent-Transcript-from-your-1-1
- 15Five: editing and sensitive-topic handling are not addressed in the privacy article; since no user can access the transcript, user redaction of the transcript is not applicable. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731
- Read.ai: typing "opt out" deletes the meeting. [SNIPPET, third-party] https://verifier.org/ai-meeting-notetakers
- Fellow: credited with transcript redaction. [SNIPPET; source list includes Fellow's own blog] https://fellow.ai/blog/ai-note-takers-for-fintech/
- Law-firm risk list relevant to sensitive topics: accommodation discussions can capture ADA-protected medical information that must be kept confidential and separate; recording talk about wages, conditions, or organizing may raise NLRA Section 7 surveillance concerns; transcription errors may fall more heavily on accented speech, raising Title VII concerns if relied on for employment decisions; require human review before relying on AI output. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- In the Otter order, a plaintiff who discussed medical information with a provider stated a claim, while merely labeling a conversation "private" or "sensitive" was not enough. [OPENED, secondary summary of the order] https://www.isbamutual.com/liability-minute/ai-notetaking-privacy-claims-survive-otterai-lawsuit

### Inferences
- Table stakes: participant deletion of a transcript.
- Common: none clearly established.
- Differentiating: employee-initiated redaction before anything is saved or fed downstream; automatic detection and exclusion of health, family, accommodation, union/wage, and small-talk content; a review window before signals flow to performance.
- Lattice's "both must delete" rule means an employee cannot unilaterally remove a transcript the manager wants to keep. A one-sided delete or redact right for the employee would be a clear contrast.
- Sensitive-topic exclusion maps directly to named legal risks (ADA medical confidentiality, NLRA Section 7), so it is defensible as a compliance feature, not only a comfort feature.

### Gaps
- No vendor documentation found for automatic sensitive-topic detection or small-talk exclusion in any of the listed products. Unknown whether any ships it; absence of evidence here reflects limited search depth, not a confirmed market gap.
- Fellow's redaction and pause-recording controls were not verified on Fellow's own documentation.
- Summary-correction workflows (who can edit an AI summary, is the edit tracked) not found for any vendor.

---

## 5. Audit logs, eDiscovery, export, data subject requests

### Takeaway
Little vendor-specific evidence was retrieved on audit logs for 1:1 assistants. Lattice's privacy page does not mention them and 15Five explicitly refuses to release raw transcripts for audit. Audit logging looks like an enterprise-notetaker norm rather than a documented HR-platform 1:1 feature.

### Cited Findings
- Lattice: privacy page does not address audit logs or legal hold; participants can download transcripts; meeting data and insights are "Customer Data" under the Lattice DPA. [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- 15Five: raw transcripts are not shared for compliance or audit purposes and no raw transcript data leaves Kona's internal coaching process. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731
- A third-party comparison table marks audit logs and custom retention as present for several enterprise notetakers; BYOK and legal hold were not covered. [SNIPPET, third-party] https://workgpt.com/en/comparison/enterprise-features
- Fellow is credited with a Super Admin API. [SNIPPET] https://fellow.ai/blog/ai-note-takers-for-fintech/
- Teams transcripts fall under Microsoft 365/Purview retention; Google Meet transcripts under Vault. [SNIPPET, third-party] https://nhimg.org/ai-meeting-assistant-security-guide
- Law-firm recommendation: keep consent logs, retention limits, deletion workflows; define which record controls if AI output and manual notes conflict. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk

### Inferences
- Table stakes: data export and deletion on request (implied by DPA/GDPR posture across vendors).
- Common (enterprise notetakers): admin audit logs.
- Differentiating in the HR 1:1 niche: an audit log of who accessed, exported, redacted, or deleted 1:1 content, visible to the employee as well as the admin; consent-event logging.
- There is a design tension QW should decide deliberately: 15Five's "nobody can ever get the transcript, even for audit" is the strongest anti-surveillance posture but gives the customer nothing to produce or verify; Lattice's participant-download model does the opposite.

### Gaps
- Audit-log scope for Lattice, 15Five, Leapsome, Otter, Fireflies, Fathom, Read.ai, Granola, Notion, Gong: not verified from vendor documentation. Unknown.
- DSAR handling specifics for meeting transcripts (for example a non-user participant's access request): not found.

---

## 6. AI data handling (no-training, ZDR, PII stripping, subprocessors, residency)

### Takeaway
"We do not train on your data" is table stakes for enterprise and HR-platform products; consumer-origin notetakers are split, and default-on training is now a litigation trigger (Otter, Granola).

### Cited Findings
- Lattice: customer data is not used to train Lattice's AI models; no secondary use such as training or cross-customer benchmarking; subprocessors named: Recall.ai (join meetings, generate transcripts) and LangSmith (monitoring/optimization of AI features); data stored "consistent with the customer's Lattice data residency and hosting configuration." LLM provider not named on the page. [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- 15Five publishes a help article on what data 15Five AI submits to its AI sub-processor; contents not read. [SNIPPET, title only] https://success.15five.com/hc/en-us/articles/50989017106843-What-data-does-15Five-AI-submit-to-its-AI-sub-processor
- Otter: privacy policy describes training speech models on de-identified recordings and transcripts; sources disagree on whether opt-out is by request or an in-app toggle. [SNIPPET, third-party] https://www.getvoibe.com/resources/ai-privacy-tracker/ and https://www.speechmark.co/articles/do-ai-notetakers-train-on-your-meetings
- Fathom: uses de-identified customer data to improve models, opt-out available; Team Edition admins can disable for all users. [SNIPPET, third-party] https://www.getvoibe.com/resources/is-fathom-safe/
- Fireflies: states it does not use personal information for training and enforces zero data retention with vendors. [SNIPPET, third-party] https://scribbl.co/post/is-fireflies-ai-safe
- Read.ai: training off by default, opt-in only. [SNIPPET, third-party] https://verifier.org/ai-meeting-notetakers
- Zoom: states it does not use customer audio, video, chat, screen sharing, attachments, or similar content to train Zoom or third-party AI models. [SNIPPET, third-party] https://nhimg.org/ai-meeting-assistant-security-guide
- Residency: Otter US (AWS US West); Fathom US-only; Fireflies US default with EU for enterprise; Gong US or EU region. [SNIPPET, third-party] https://humla.team/blog/where-ai-notetakers-store-your-meetings
- Vendors training on de-identified or aggregated data usually describe it in service terms; counsel should review (McGinnis). SHRM's Link: employers should own their data and control its use. [OPENED] https://www.hrdive.com/news/hr-must-set-boundaries-ai-notetakers/830276/
- Privilege angle: consumer AI tool terms can destroy confidentiality expectations (United States v. Heppner, S.D.N.Y., 2026-02-17, per Mayer Brown). [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk

### Inferences
- Table stakes: contractual no-training on customer content; published subprocessor list; encryption in transit and at rest.
- Common: zero-data-retention terms with LLM providers; EU data residency (often enterprise tier).
- Differentiating: PII stripping before LLM calls; naming the LLM provider and ZDR terms on a public page; customer-selectable region for transcript processing as well as storage.
- Using a meeting-bot subprocessor (Lattice uses Recall.ai) adds a party that touches audio; QW should expect buyers to ask who that is and how fast it deletes.

### Gaps
- Microsoft Copilot and Google Gemini no-training commitments: not retrieved in this pass. Unknown here, though both publish enterprise terms.
- PII stripping: no vendor documentation found. Unknown.
- 15Five and Leapsome LLM providers and ZDR terms: Unknown.

---

## 7. Certifications (SOC 2 Type II, ISO 27001, ISO 42001, HIPAA, GDPR, FedRAMP)

### Takeaway
SOC 2 Type II is universal. ISO 42001 (AI management systems) is emerging as a differentiator, reported for Gong and Fireflies. No FedRAMP evidence was found for any listed vendor.

### Cited Findings
- SOC 2 Type II reported for Fellow, Otter, Fireflies, Fathom; Read.ai states an annual SOC 2 Type II audit (report unverified). [SNIPPET, third-party] https://www.getvoibe.com/resources/ai-privacy-tracker/ and https://fellow.ai/blog/ai-note-takers-for-fintech/
- Gong: ISO 27001, ISO 42001, ISO 27017/27018/27701, PCI DSS, Data Privacy Framework. [SNIPPET] https://www.gong.io/platform/trust
- Fireflies: trust center reportedly lists ISO/IEC 42001; one source says no ISO 27001 claimed. [SNIPPET, competitor blog] https://scribbl.co/post/is-fireflies-ai-safe
- Otter ISO 27001: sources conflict; one says certified, another says policies are "based on the ISO 27001/2 framework" with no certification claimed. [SNIPPET] https://scribbl.co/post/is-otter-ai-safe
- HIPAA BAAs: Fellow, Otter, Fireflies offer them on Enterprise tiers only; Fathom status inconsistent. [SNIPPET, third-party] https://fellow.ai/blog/ai-note-takers-for-fintech/
- Leapsome: footer shows ISO 27001:2022 badge and GDPR-compliant logo; scope not stated. [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent
- 15Five refers readers to its trust site for certifications. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731 (trust site: https://trust.15five.com, not opened)

### Inferences
- Table stakes: SOC 2 Type II; GDPR DPA.
- Common: ISO 27001; HIPAA BAA at enterprise tier.
- Differentiating: ISO 42001; FedRAMP.

### Gaps
- Lattice and 15Five certification lists were not opened. Unknown here.
- FedRAMP: no evidence found for any listed vendor's meeting assistant. Unknown (Microsoft, Google, Zoom have government offerings, not verified in this pass).
- Vendor trust centers were largely not fetched; all certification claims above except Leapsome's badge are second-hand.

---

## 8. Admin controls (enable by group, defaults, SSO/SCIM, BYOK) and works council / union considerations

### Takeaway
Org-level on/off and retention defaults are standard. Group-level enablement, BYOK, and works-council enablement kits were not documented in what was found. In Germany, co-determination is triggered by a tool's objective capability to monitor, so a transcript-plus-coaching-plus-performance-signal product should be assumed to require a works agreement.

### Cited Findings
- Lattice: admin enables/disables AI Agent for 1:1s, can enable auto-add, sets transcript storage, and configures custom-role permissions. [OPENED/SNIPPET] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy and https://help.lattice.com/hc/en-us/articles/41117673875095-Enable-or-Disable-the-Lattice-AI-Agent-for-1-1s-and-Configure-Transcript-Retention
- 15Five: managers are invited to Kona Coach by admins. [SNIPPET, title] https://success.15five.com/hc/en-us/articles/36868337581723
- Leapsome: admins control recording, retention, and which meetings the notetaker joins. [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent
- Zoom account-level deactivation: Account Management > Account Settings > AI Companion. Google: Admin console > Apps > Google Workspace > Google Meet > Gemini settings > Automatic note-taking. Teams: meeting policies in Teams admin center. Admin policies override user preferences in all three. [SNIPPET, third-party] https://www.banthebots.org/explainers/how-to-turn-off-ai-notetakers
- Works councils: German works councils have a mandatory co-determination right over technical systems capable of monitoring behaviour or performance (BetrVG § 87(1) no. 6), triggered by objective capability regardless of employer intent; vendors recommend a works agreement before rollout, and for internal meetings a works agreement can supply the lawful basis in place of individual consent. [SNIPPET, vendor blogs] https://meetkalima.com/blog/works-council-ai-transcription and https://www.sally.io/blog/is-sally-ai-works-council-compliant
- Counterpoint: Hamburg Labour Court order of 2024-01-16 (24 BVGa 1/24) is cited for the proposition that AI use does not always trigger co-determination; the citing article treats it as an exception. [SNIPPET] https://www.innobu.com/en/articles/ai-co-determination-works-councils-utilities-2027.html
- Germany: recording a non-public conversation without consent is a criminal offence under StGB § 201. [SNIPPET, vendor blog] https://www.sally.io/blog/recording-meetings-in-germany-data-protection
- Mayer Brown: employment contexts may require works council involvement; recording discussions of wages, conditions, or organizing may raise NLRA Section 7 concerns in the US. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- Leapsome's page does not mention works councils. [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent

### Inferences
- Table stakes: org-level enable/disable; admin retention default; SSO.
- Common: SCIM; role-based permission configuration.
- Differentiating: enable by department, location, or legal entity (needed to exclude Germany, unionized units, or all-party-consent states); BYOK; a works-council documentation pack (purpose limitation, no individual performance scoring from transcripts, access matrix).
- For unionized US workplaces, introducing recording of 1:1s could be a mandatory bargaining subject. This is an inference; no source retrieved states it for AI notetakers.

### Gaps
- BYOK: no evidence for any listed vendor. Unknown.
- Group-level enablement at Lattice, 15Five, Leapsome: Unknown.
- No primary German source (statute text, BAG decision, DSK guidance) was opened; the works-council points rest on vendor blogs and one law-firm summary.
- Leapsome is Berlin-based and would be the natural benchmark for works-council readiness; its Trust Center was not retrieved.

---

## 9. US recording consent law (one-party vs all-party, Wiretap Act, CIPA, botless capture)

### Takeaway
Roughly a dozen states require all-party consent, and lists differ at the margins. The practical standard law firms recommend is to apply the strictest rule to every meeting. Botless capture does not reduce exposure; it removes the one visible cue that a recording is happening and is now itself being litigated (Granola).

### Cited Findings
- All-party consent states per Mayer Brown (June 2026): California, Connecticut, Florida, Illinois, Maryland, Massachusetts, Michigan, Montana, Nevada, New Hampshire, Pennsylvania, Washington. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- Lists vary: Bloomberg Law commentary (Jan 2026) lists California, Florida, Illinois, Maryland, Massachusetts, Montana, New Hampshire, Pennsylvania, Washington (omits Connecticut, Michigan, Nevada); Clio lists 11 (adds Connecticut and Nevada, omits Michigan). Delaware does not appear in any list retrieved. [SNIPPET] https://news.bloomberglaw.com/us-law-week/ai-notetaking-poses-wiretapping-discovery-and-ethical-pitfalls
- Federal Wiretap Act (ECPA Title I) is one-party consent, except where the interception is for a criminal or tortious purpose, 18 U.S.C. § 2511(2)(d). [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- CIPA § 631(a) goes beyond recording consent: it bars unauthorized third parties from "reading, attempting to read, or learning the contents" of communications, which may expose the notetaker vendor itself; theory still in litigation. [OPENED] same Mayer Brown URL
- California has applied its all-party rule to out-of-state recordings affecting Californians; safest practice is the strictest applicable law. [SNIPPET] https://news.bloomberglaw.com/us-law-week/ai-notetaking-poses-wiretapping-discovery-and-ethical-pitfalls
- Vendor-as-eavesdropper logic from the Otter order: a vendor serving only its customer is usually treated as the customer's tool, but allegedly keeping and using data for its own purposes (training) can make it a third-party eavesdropper under California law; the federal party-consent exception may fail if the recording served a tortious purpose such as training AI for profit. [OPENED, secondary summary] https://www.isbamutual.com/liability-minute/ai-notetaking-privacy-claims-survive-otterai-lawsuit
- Botless: Granola's notifications are off by default and "no bot joins the meeting and no notification appears for meeting participants by default"; Granola is the defendant in a CIPA § 631 putative class action. [SNIPPET] https://www.legal500.com/intelligence/united-states/privacy/ai-note-taking-tools-silent-recording-and-the-consent-problem
- Some states require advance notice to employees about recording/monitoring technologies (Adam Solomon, Hunton Andrews Kurth). [OPENED] https://www.hrdive.com/news/hr-must-set-boundaries-ai-notetakers/830276/

### Inferences
- A vendor that does not use customer content for its own purposes is better placed to argue it is the customer's tool, not a third-party interceptor. That makes a strict no-training, no-secondary-use commitment a legal-exposure control and not only a marketing line.
- For a 1:1 with two known internal participants, all-party consent is operationally easy to collect (two people, both authenticated users). An HR platform has an advantage here over general notetakers dealing with external guests.
- If QW offers desktop/system-audio capture, it should carry the same notice and consent flow as a bot.

### Gaps
- The all-party list is not settled across sources (Connecticut, Michigan, Nevada, Delaware, Oregon are commonly treated inconsistently). A statute-by-statute check by counsel is needed.
- State employee-monitoring notice laws (for example New York, Connecticut, Delaware) were mentioned generically; specifics not retrieved.
- The Otter order itself was not readable (Justia returned HTTP 403); holdings are from secondary summaries.

---

## 10. Litigation (Otter, Fireflies, Granola, Microsoft, others; BIPA voiceprints)

### Takeaway
As of November 2026 the lead case, In re Otter.AI Privacy Litigation, survived a motion to dismiss on its core wiretap, CIPA, and BIPA claims and is in discovery. Suits now also target Fireflies (BIPA voiceprints), Granola (CIPA, botless), and Microsoft Teams (BIPA). No finding of liability has been made in any of them.

### Cited Findings
- Otter: Brewer v. Otter.ai, filed 2025-08-15 in N.D. Cal., now consolidated as In re Otter.AI Privacy Litigation, No. 5:25-cv-06911; alleges covert recording and undisclosed training use. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk ; docket: https://www.courtlistener.com/docket/71118721/brewer-v-otterai-inc/
- Otter ruling: on 2026-08-13 Judge Eumi K. Lee granted in part and denied in part Otter's motion to dismiss; CIPA dismissal was denied; some counts dismissed with leave to amend. [SNIPPET of the order] https://docs.justia.com/cases/federal/district-courts/california/candce/5:2025cv06911/454675/68
- Otter ruling substance (secondary summary): BIPA voiceprint, federal wiretap, California eavesdropping, and intrusion-type claims proceed; the court refused to assume a visible notetaker meant participants agreed to be recorded; voiceprints treated as biometric identifiers under BIPA; plaintiffs plausibly alleged no written notice, no signed release, no public retention/destruction schedule; plaintiffs were non-customers who joined calls where someone else enabled Otter. No court has found Otter liable. [OPENED] https://www.isbamutual.com/liability-minute/ai-notetaking-privacy-claims-survive-otterai-lawsuit
- Otter posture: CFAA claims dismissed; Otter answered 2026-09-17; case in discovery; class certification motion due 2027-05-13. Sources disagree on hearing date (Aug 3 vs 4) and on whether unjust enrichment survived. [SNIPPET, trackers and competitor blogs] https://ailawsuittracker.com/cases/in-re-otter-ai-privacy-litigation-5-25-cv-06911/ and https://scribbl.co/post/otter-ai-lawsuit
- Fireflies: Cruz v. Fireflies.AI Corp. (C.D. Ill., filed 2025-12-18; one source gives No. 3:25-cv-03399) and a second suit (Fricker, N.D. Ill., March 2026) allege the Speaker Recognition feature creates voiceprints without written notice, written release, or a public retention policy; a named plaintiff had no Fireflies account. A consolidated complaint was reportedly filed 2026-06-24 and a motion to dismiss 2026-07-15. Case numbers and dates conflict across sources. [SNIPPET, competitor blogs] https://scribbl.co/post/fireflies-ai-lawsuit and https://tldv.io/blog/ai-meeting-recorder-lawsuits/
- Granola: Chamberlain v. Granola, Inc., No. 3:26-cv-07926 (N.D. Cal., filed 2026-07-30), CIPA § 631, ECPA, intrusion; amended complaint 2026-10-19; alleges recording without notice and default AI training; Granola had not responded on the merits as of early November 2026. [SNIPPET] https://www.legal500.com/intelligence/united-states/privacy/ai-note-taking-tools-silent-recording-and-the-consent-problem and https://www.laxis.com/blog/ai-notetakers-in-court-granola-otter-lawsuits/
- Microsoft Teams: a BIPA suit over Teams live transcription was reportedly filed 2026-02-05 in W.D. Wash. [SNIPPET, vendor blog; unverified] https://www.getmeetly.ai/blog/ai-notetaker-voiceprint-lawsuits/
- Fathom and Read.ai: one source found no privacy case against either as of 2026-08-28. [SNIPPET, competitor blog] https://scribbl.co/post/fireflies-ai-lawsuit
- BIPA damages: $1,000 per negligent violation, $5,000 per intentional or reckless violation. [OPENED] https://www.isbamutual.com/liability-minute/ai-notetaking-privacy-claims-survive-otterai-lawsuit
- An employment case, Waninger v. Marathon, is described by one vendor blog as a termination lawsuit involving a Fireflies notetaker. Not verified against any primary source. [SNIPPET, vendor blog; unverified] https://basilai.app/articles/2026-09-30-waninger-marathon-fireflies-ai-notetaker-termination-lawsuit-hr-playbook.html

### Inferences
- Three recurring allegations define the risk pattern: (1) non-users recorded without their own consent, (2) vendor's own use of content for training, (3) speaker identification creating voiceprints without BIPA-compliant written release and retention schedule.
- Speaker diarization that persists a voice embedding to recognize people across meetings is the BIPA trigger. For a two-person 1:1, attribution can come from meeting-platform metadata without storing a voiceprint; this is a design inference, not a sourced legal conclusion.
- Lattice's use of Recall.ai for "speaker attribution" metadata suggests peers attribute via platform metadata. Whether any voiceprint is created is Unknown.

### Gaps
- Gong and Zoom: no notetaker-specific recording/voiceprint suit found in this pass. Unknown, not confirmed absent. (Zoom's earlier privacy settlement history was not researched.)
- The Fireflies and Microsoft case details come only from vendor blogs with conflicting dates and numbers; dockets were not checked.
- The Otter order's exact count-by-count disposition was not read directly.

---

## 11. EU: GDPR, AI Act emotion-recognition ban, high-risk classification and dates, German co-determination

### Takeaway
Two AI Act provisions bear directly on a 1-on-1 assistant. Emotion inference from employees' biometric data (voice included) has been prohibited since 2025-02-02. AI used for performance evaluation, monitoring, promotion, or termination is high-risk, with obligations now delayed by the Digital Omnibus from 2026-08-02 to 2027-12-02.

### Cited Findings
- Emotion recognition: AI Act Article 5(1)(f) prohibits inferring emotions in workplace and education settings, with a narrow medical/safety exception; the Commission reads the ban as covering workers' emotions, not customers'. [SNIPPET] https://www.insideprivacy.com/artificial-intelligence/european-commission-guidelines-on-prohibited-ai-practices-under-the-eu-artificial-intelligence-act/
- Text-only analysis reportedly falls outside the prohibition as long as no biometric data such as voice, face, or typing behaviour is used; Commission guidelines reportedly adopted 2025-07-29 as C(2025) 5052 final (one earlier source said not yet formally adopted; adoption date not verified against the Commission). [SNIPPET] https://www.praxikon.com/en/posts/emotion-recognition-workplace-ban-ai-act ; earlier status: https://legalblogs.wolterskluwer.com/global-workplace-law-and-policy/the-prohibition-of-ai-emotion-recognition-technologies-in-the-workplace-under-the-ai-act/
- Call-centre example: tracking customers' emotions by voice is out of scope; tracking the employees' own emotions is prohibited. The guidelines describe a narrow training-only carve-out not found in the Act's text, where results cannot affect the person's assessment. [SNIPPET] https://reglog.io/blog/eu-ai-act-emotion-recognition-workplace
- The ban extends to recruitment and probation periods. [SNIPPET] https://www.lewissilkin.com/en/insights/2025/02/17/understanding-the-eu-ai-acts-prohibited-practices-key-workplace-and-advertising-102k011
- High-risk: the Act classifies AI used for recruitment, candidate selection, performance evaluation, task allocation, monitoring of workers, and promotion or termination decisions as high-risk (Annex III). [SNIPPET] https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act
- Digital Omnibus: adopted by Parliament 2026-06-16 and Council 2026-06-29; published as Regulation (EU) 2026/1744 in the Official Journal 2026-07-24; in force 2026-07-27. Annex III high-risk obligations moved from 2026-08-02 to 2027-12-02; Annex I (product-embedded) to 2028-08-02. [SNIPPET] https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ and https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/
- Most transparency obligations stayed on the 2026-08-02 schedule; sources disagree on the scope of a grace period to 2026-12-02 for content-marking by systems already on the market. [SNIPPET] https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html
- High-risk deployer duties include monitoring, log retention, and human oversight; AI literacy duty applies even to non-high-risk uses. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- GDPR: applies if participants are in Europe; lawful basis is hard to fix because content varies; special-category data (health) needs a specific ground such as explicit consent; Member State law may require consent where GDPR does not (communications confidentiality, unauthorized recording); works council involvement may be required. [OPENED] same Mayer Brown URL
- Germany: see section 8 for BetrVG § 87(1) no. 6 and StGB § 201. https://meetkalima.com/blog/works-council-ai-transcription

### Inferences
- A QW feature that scores employee sentiment, tone, stress, or engagement from audio would likely fall in the prohibited category for EU workers. Deriving the same from transcript text appears to sit outside the ban per secondary readings of the guidelines, but a transcript is produced from voice, so the boundary should be confirmed by counsel against the guideline text.
- Summarization and manager coaching are probably not high-risk by themselves; "feeds signals into the performance platform" is the element that most plausibly pulls the system toward Annex III (performance evaluation, monitoring). Product architecture that keeps 1:1 signals advisory to the manager and out of ratings would reduce that pull. Inference, not a sourced classification.
- QW is US-based, but US customers with EU employees bring these rules into scope, and Leapsome (EU-based) will market against them.
- The December 2027 date gives roughly 12 months of runway from now for high-risk readiness; the emotion-recognition ban has no runway.

### Gaps
- The Commission guidelines and the Official Journal text of the Omnibus were not opened; dates and the text-versus-voice distinction rest on law-firm and compliance-blog summaries.
- DPIA (GDPR Art. 35) requirements for employee meeting recording: no source retrieved. It is widely assumed that systematic employee monitoring triggers a DPIA, but this is unsourced here.
- No EU regulator decision (DPA fine or guidance) specific to AI notetakers was found.

---

## 12. US state and local AI employment laws

### Takeaway
The Colorado AI Act never took effect: it was repealed and replaced in May 2026 by a narrower disclosure law effective 2027-01-01. Illinois and Texas rules have been live since 2026-01-01, California's employment ADS rules since 2025-10-01, and California's CPPA ADMT obligations bite on 2027-01-01.

### Cited Findings
- Colorado: SB 24-205 was delayed from 2026-02-01 to 2026-06-30 by SB 25B-004 (signed 2025-08-28), then repealed and replaced by SB 26-189, signed 2026-05-14, a disclosure-and-rights framework for automated decision-making technology, effective 2027-01-01. The original duty of reasonable care against algorithmic discrimination, impact assessments, and risk-management program requirements were dropped. [SNIPPET] https://www.seyfarth.com/news-insights/colorado-enacts-artificial-intelligence-replacement-law.html and https://www.eckertseamans.com/legal-updates/colorado-repeals-and-replaces-its-landmark-ai-statute-what-businesses-need-to-know
- Colorado litigation: xAI sued 2026-04-09 to block SB 24-205; a stipulated order of 2026-04-27 barred enforcement pending a preliminary-injunction ruling; the Attorney General said he would not enforce until rulemaking concluded. [SNIPPET] https://www.carpedatumlaw.com/2026/05/colorados-ai-reset-two-weeks-a-white-house-callout-and-a-pivot-away-from-the-eu-model/
- Illinois HB 3773: effective 2026-01-01; amends the Illinois Human Rights Act; unlawful for an employer's AI use in employment decisions to have a discriminatory effect; requires notice of AI use; covers employers with one or more Illinois employees; IDHR proposed implementing rules with comments closing 2026-06-29. [SNIPPET] https://www.ebglaw.com/insights/publications/workplace-ai-regulation-in-2026-how-employers-can-navigate-the-changing-legal-landscape and https://aiemploymentlawtracker.com/
- California CPPA ADMT regulations: effective 2026-01-01, with compliance for businesses using ADMT in significant decisions (employment included) by 2027-01-01. [SNIPPET] https://aiemploymentlawtracker.com/
- California Civil Rights Council FEHA automated-decision-system regulations: reported effective 2025-10-01; cover records and treat testing as evidence. Date reported by trackers, not confirmed against the agency. [SNIPPET] https://www.ebglaw.com/insights/publications/workplace-ai-regulation-in-2026-how-employers-can-navigate-the-changing-legal-landscape
- Texas TRAIGA (HB 149): effective 2026-01-01; intent standard (no liability on disparate impact alone); enforced exclusively by the state attorney general. [SNIPPET] https://www.ebglaw.com/insights/publications/workplace-ai-regulation-in-2026-how-employers-can-navigate-the-changing-legal-landscape
- NYC Local Law 144: enforced by DCWP since 2023; annual independent bias audit of automated employment decision tools, published summary, candidate notice 10 business days before use. [SNIPPET] https://www.whitefordlaw.com/news-events/client-alert-ai-governance-for-businesses

### Inferences
- These laws attach when AI output is used in an employment decision (promotion, discipline, termination, in some cases performance evaluation). A notetaker that only summarizes is largely outside them; a pipeline from 1:1 transcripts to performance signals moves QW's customers toward notice (Illinois), ADMT notice/opt-out/access rights (California, Colorado from 2027), and recordkeeping (California CRD).
- NYC LL 144 targets hiring and promotion tools; it is unlikely to reach a 1:1 assistant unless outputs substantially assist promotion decisions.
- Customers will expect the vendor to supply the notices, documentation, and bias-testing evidence they need. That is a product requirement, not just a legal footnote.

### Gaps
- Whether California's CPPA ADMT "significant decision" definition would reach AI-derived performance signals from 1:1s: not analyzed in any source retrieved. Unknown.
- Illinois IDHR final rules status after the June 2026 comment period: Unknown.
- State legislature and agency primary pages were not opened; all dates are from law-firm alerts and trackers.
- Any 2026 federal preemption action affecting state AI laws (a "White House callout" is referenced in one Colorado headline) was not researched.

---

## 13. Discoverability, retention guidance, privilege

### Takeaway
Law firms uniformly treat AI meeting transcripts as discoverable ESI and advise against recording performance, disciplinary, investigation, and legal-advice meetings by default. That is direct headwind for a 1-on-1 recorder, since Mayer Brown's default-no list names "performance matters."

### Cited Findings
- Mayer Brown (June 2026): recording performance and disciplinary meetings creates a verbatim, potentially discoverable record in which offhand remarks lose tone and context; recording some meetings and not others creates evidentiary imbalance; recording investigations may discourage candor; transcripts expand litigation-hold scope and e-discovery cost; recommends a tiered model defaulting to no AI notetaker for legal advice, HR investigations, performance matters, trade secrets, and board deliberations; require human review of AI output; define which record controls. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- Privilege cases cited by Mayer Brown: United States v. Heppner, No. 25 Cr. 503 (JSR), 2026 WL 436479 (S.D.N.Y. 2026-02-17), privilege denied for materials prepared on a consumer AI platform; Warner v. Gilbarco, Inc. (E.D. Mich. 2026-02-10), work product not waived unless disclosure materially raises the risk an adversary obtains it, turning on vendor practices. [OPENED] same URL
- Cahill: a notetaker present in a meeting involving legal advice could amount to privilege waiver. [SNIPPET] https://clsbluesky.law.columbia.edu/2026/06/16/cahill-discusses-a-i-note-takers-in-corporate-meetings/
- As of September 2026, no court is reported to have squarely held that an AI meeting-notetaker transcript waived privilege. [SNIPPET, vendor blog] https://basilai.app/articles/2026-07-19-ai-notetaker-discovery-privilege-corporate-meetings-on-device-alternative.html
- Bloomberg Law commentary (Jan 2026) frames AI notetaking as posing wiretapping, discovery, and ethical pitfalls. [SNIPPET] https://news.bloomberglaw.com/us-law-week/ai-notetaking-poses-wiretapping-discovery-and-ethical-pitfalls
- Ogletree published a podcast (2025-10-22) on legal considerations for deploying AI notetakers; contents not reviewed. [SNIPPET, title only] https://ogletree.com/insights-resources/podcasts/2025-10-22/the-ai-workplace-legal-considerations-for-deploying-ai-notetakers/

### Inferences
- The discoverability concern cuts both ways for buyers: a verbatim record can protect a manager who behaved properly and can sink one who did not. Employment counsel at prospects will be a gatekeeper, and will ask first about retention defaults and legal hold.
- Short or zero transcript retention with a durable, reviewed summary is the configuration most consistent with law-firm advice. Lattice (transcripts off by default) and 15Five (30 days, inaccessible) have already landed there.
- An AI summary that mischaracterizes a performance conversation becomes a contested record. Participant review and correction, with the edit history kept, addresses a risk law firms name explicitly.
- Consistency matters: selective recording of only some employees' 1:1s creates the "evidentiary imbalance" problem and possible disparate-treatment arguments.

### Gaps
- No Littler, Fisher Phillips, Seyfarth, Jackson Lewis, Morgan Lewis, or Orrick alert specifically on AI notetakers in 1-on-1s was opened. Fisher Phillips is reported second-hand as calling AI-generated ESI a core discovery battleground in employment cases; not verified.
- No case found in which a 1:1 AI transcript was actually compelled or used as evidence, other than the unverified Waninger v. Marathon reference.

---

## 14. Employee attitudes and effect on candor

### Takeaway
AI notetakers are already common and consent is frequently skipped, but hard evidence on whether recording reduces candor in 1-on-1s was not found. The widely repeated "84% self-censor" figure has no traceable primary source and should not be used.

### Cited Findings
- July 2026 survey of 500 employed US adults (Kolmogorov Law): 33.4% say an AI notetaker or transcription bot has been present in their work meetings; among those, only 34.7% say they were always asked permission first (subsample margin of error about plus or minus 7.6 points). On discovering covert recording, 29.2% would complain to the company or HR, 9.6% would stop attending, 14.2% would do nothing. The sponsor is a law firm; treat as indicative. [SNIPPET] https://www.kolmogorovlaw.com/ai-notetakers-workplace-consent-survey
- Pew Research (2023-04-20): 61% of US adults oppose AI tracking of workers' movements; 70% oppose facial-recognition analysis of employees' facial expressions (9% favor); attendance tracking was the one use with more support than opposition (45% favor, 35% oppose). Predates AI notetakers; general monitoring attitudes only. [SNIPPET] https://www.pewresearch.org/internet/2023/04/20/ai-in-hiring-and-evaluating-workers-what-americans-think/
- Pew-based summary: 56% oppose AI checking whether office workers are at their desks. [SNIPPET] https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/november/AI-monitoring-of-emoloyees/
- "84% of professionals change how they speak when AI is listening" appears in a 2026 marketing blog with no primary source located. Unverified; do not cite as fact. [SNIPPET] https://blog.mean.ceo/ai-meeting-assistant-statistics/
- Law-firm view: recording complaint intakes and witness interviews "may discourage candor." This is professional opinion, not measured data. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- A Reworked article discusses a "trust deficit" in AI-powered performance tracking; contents not reviewed. [SNIPPET, title only] https://www.reworked.co/employee-experience/the-trust-deficit-in-ai-powered-performance-tracking/

### Inferences
- The consent gap (about two-thirds of exposed workers not always asked) supports positioning explicit two-sided consent as a real differentiator in practice, even where vendors nominally offer notice.
- The strongest opposition in Pew's data attaches to emotional/expression analysis, which matches the EU prohibition. Sentiment or emotion features on employee speech are the highest-objection, highest-risk area.
- Absence of candor data is itself a finding: QW cannot currently claim, with evidence, that its controls preserve candor. A customer pilot measuring it would be new evidence.

### Gaps
- No Gartner or Forrester data on employee trust in AI meeting recording was found (likely paywalled). Unknown.
- No peer-reviewed or controlled study on recording and candor in manager-employee conversations was found.
- No survey isolating 1-on-1s from group meetings was found.

---

## 15. Guidance from employment law firms, SHRM, Gartner, Forrester on AI notetakers in HR conversations

### Takeaway
Published guidance is cautious: disclose, get everyone's consent, vet vendor data use, keep humans in the decision, and by default keep notetakers out of performance, disciplinary, and investigation meetings. No guidance was found that addresses purpose-built 1-on-1 assistants inside HR platforms as a distinct category.

### Cited Findings
- SHRM CHRO Jim Link (HR Dive, 2026-09-14): disclose AI tool use; get approval from everyone present before recording or transcription; know where data originates, how it is protected and used; employers should own their data; the final call on HR decisions should rest with a human; treats notetakers as a governance issue requiring tool vetting. [OPENED] https://www.hrdive.com/news/hr-must-set-boundaries-ai-notetakers/830276/
- Brian McGinnis (Barnes & Thornburg), same article: apply the most demanding jurisdiction's consent standard broadly; AI-recorded candidate calls are "considered more high risk than your typical Zoom meeting"; HR most often uses notetakers in recruiting. The article does not address 1:1s, performance conversations, or investigations specifically. [OPENED] same URL
- Mayer Brown recommendations: map participant locations and apply the strictest consent standard; give notice covering purpose, retention, and rights; maintain an approved-vendor list and review contracts for training use and third-party access; tiered meeting model; retention limits, deletion workflows, consent logs; human review; training and escalation for unauthorized notetakers. [OPENED] https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk
- HR Executive ran a piece arguing the Otter lawsuit should be on every HR leader's radar; contents not reviewed. [SNIPPET, title only] https://hrexecutive.com/a-lawsuit-over-ai-notetakers-should-be-on-every-hr-leaders-radar/
- Dykema is reported to recommend banning AI notetakers from board, committee, and executive sessions. [SNIPPET, via vendor blog; not verified at source] https://basilai.app/articles/2026-08-17-ai-notetakers-board-meetings-discovery-privilege-risk.html

### Inferences
- Mayer Brown's checklist maps almost one-to-one onto product features: strictest-standard consent, notice of purpose/retention/rights, no-training contract terms, retention limits with deletion workflow, consent logs, human review. QW's four draft items (retention policy, dual consent, review/redaction, audit log) cover most of it; the missing items are a no-training/no-secondary-use commitment, participant-only access, and human-in-the-loop on any performance use.
- Because generic guidance says "default no" for performance matters, QW's go-to-market needs an answer for the customer's employment counsel explaining why a purpose-built, consented, short-retention 1:1 tool differs from a general notetaker dropped into a performance meeting.

### Gaps
- Gartner and Forrester: nothing retrieved. Unknown.
- No SHRM toolkit or policy template specific to AI notetakers was found; only the CHRO's quoted comments.
- Littler, Fisher Phillips, Seyfarth, Jackson Lewis, Morgan Lewis, Orrick notetaker-specific alerts were not retrieved in this pass.

---

## 16. Synthesis: QW's draft list versus the market

### Takeaway
Of QW's four draft answers to the surveillance objection, configurable retention is table stakes (Lattice has it), an audit log is common in enterprise tools but undocumented among HR-platform 1:1 peers, and dual consent and participant redaction are the two that could differentiate if implemented as true two-sided controls. The list omits three items peers already lead with: no audio/video storage, HR/admin lock-out from 1:1 content, and no training on customer data.

### Cited Findings
- Lattice leads with: invite-only agent, in-meeting announcement, either party can remove, no audio/video, transcripts off by default with admin retention up to 12 months, participant-only access even under admin impersonation, no training or secondary use, named subprocessors. [OPENED] https://help.lattice.com/hc/en-us/articles/40772175958807-Lattice-AI-Agent-in-1-1s-Privacy
- 15Five leads with: chat permission request, no recordings stored, transcripts deleted after 30 days and inaccessible to everyone, manager-only coaching, HR cannot see note content without manager consent. [OPENED] https://success.15five.com/hc/en-us/articles/50988682248731
- Leapsome leads with: notice to all participants, admin control of recording, retention, and which meetings, permission mirroring, ISO 27001:2022. [OPENED] https://leapsome.com/blog/meeting-notetaker-ai-agent
- Legal drivers behind each control: consent (Otter ruling on visible notetaker); no secondary use (vendor-as-eavesdropper theory); no voiceprints (BIPA claims against Otter and Fireflies); short retention and review (discoverability guidance). [OPENED] https://www.isbamutual.com/liability-minute/ai-notetaking-privacy-claims-survive-otterai-lawsuit and https://www.mayerbrown.com/de/insights/publications/2026/06/ai-notetakers-productivity-tool-or-emerging-legal-risk

### Inferences
Classification (researcher judgment from the evidence above; thin where flagged in earlier Gaps):
- Table stakes: in-meeting notice/announcement; either participant can remove or stop the recorder; no audio/video retention; admin-configurable transcript retention with auto-delete; participant-only access with HR/admin lock-out; no training on customer data; subprocessor list; SOC 2 Type II; org-level admin on/off; SSO.
- Common: pre-meeting notification emails; transcripts off or short by default; participant deletion and download; admin audit logs (enterprise notetakers); ISO 27001; EU residency; HIPAA BAA at enterprise tier; zero-data-retention terms with LLM providers.
- Differentiating: affirmative per-participant opt-in with a logged consent record; employee-side unilateral pause, redact, or delete; sensitive-topic auto-exclusion; review window before signals reach performance; legal hold; enablement by group/region/legal entity; no persistent voiceprints by design; ISO 42001; works-council documentation pack; employee-visible audit trail; explicit exclusion of emotion/sentiment inference from voice.
- Biggest unaddressed risk in QW's concept is the "feeds signals into its performance platform" step. It is what triggers EU high-risk analysis, US state ADMT/AI-employment notice duties, the discoverability concern, and the sharpest employee objection. Peers handle it differently: Lattice keeps insights participant-only; 15Five routes 1:1 content into review "Moments" under existing permissions.

### Gaps
- Notion AI Meeting Notes: no governance facts retrieved. Unknown across all feature categories.
- Fellow, Read.ai, Otter, Fireflies, Fathom, Zoom, Microsoft, Google: facts rest mainly on third-party comparisons; vendor trust centers and help centers should be opened before any claim about them is published.
- Feature classification would be firmer with direct vendor documentation for audit logs, legal hold, BYOK, and group-level enablement, none of which were verified for any vendor.
