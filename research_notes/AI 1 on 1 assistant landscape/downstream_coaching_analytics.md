# Downstream layer of the AI 1-on-1 market: manager coaching, manager-effectiveness analytics, org-level insights (state as of 2026-11-17)

Evidence-grade legend used throughout:
- (fetched) = I read the page itself.
- (snippet) = seen only in a search-result summary; the page was not opened. Treat as lower confidence and re-verify before quoting.
- (claim) = vendor marketing claim, not independently verified.
All sources are plain URLs. Lattice, 15Five, other HR suites, generic notetakers, platform-native AI and legal are covered by other researchers; they appear here only where a downstream pattern needs a named example.

## 1. Player map: what each does, how it gets conversation data, capture vendor

### Takeaway
Among specialists, the dominant capture pattern is no longer "our own bot": the newer HR-native entrants (Windmill, Betterworks) ingest transcripts that another tool already made, while the bot-based products that have a public infrastructure link use Recall.ai. AI-coaching vendors (Valence, BetterUp) are moving toward work-context ingestion (Microsoft Graph/Work IQ, Teams/Slack, meeting transcripts) but I found no coach that publicly documents scoring managers from 1:1 transcripts.

### Cited Findings

1:1 and meeting-management specialists
- Windmill (AI performance management, Slack agent "Windy"): botless. Transcripts and notes from Zoom, Google Meet, Gong, Granola and Roam "appear inside the meeting view"; "Audio and video stay on the source platform"; Gemini notes can also be integrated. 1:1 data feeds agenda building, action-item carry-forward and a "Catch Me Up" pre-meeting brief that includes feedback received, goals, progress and growth areas. (fetched) https://gowindmill.com/features/one-on-ones
- Windmill states AI is not evaluating anyone's performance; managers write and finalize reviews. Reviews (self, peer, upward) run through Slack via Windy. (snippet) https://help.gowindmill.com/introducing-performance-reviews-on-windmill and https://help.gowindmill.com/windy/meet-windy
- Windmill headline numbers "90% faster reviews" and "93% employee satisfaction" are homepage claims. (snippet, claim) https://gowindmill.com/ . Pricing reported at about $10 per seat per month by a third-party listing. (snippet) https://toolradar.com/tools/windmill-1
- Betterworks "Conversational Intelligence": botless. Retrieves completed Zoom transcripts through the Zoom API ("There's no Betterworks meeting bot joining the call"); for other tools users upload or paste transcripts, notes or summaries. Outputs recaps, action items, goal-progress signals, suggested milestone updates, potential new goals, suggested agenda topics and a private prep brief per participant. Recommendations stay pending until a user reviews, edits, discards or confirms them. Article dated 2026-09-10, written in present tense; shipped/beta label not stated. (fetched) https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Fellow: AI meeting assistant with shared agendas, action items, AI notes/transcripts and an "Ask Fellow" chat over the meeting corpus; positions itself for 1:1s and, increasingly, as a Gong alternative for sales. (snippet) https://fellow.ai/use-cases/one-on-one-meetings and https://fellow.ai/compare/fellow-vs-gong . Fellow says it never uses meeting data to train AI models. (snippet) https://help.fellow.ai/en/articles/8461666-fellow-ai-features
- Fellow is listed under "Used By" for Recall.ai's Meeting Bot API (capture vendor: confirmed as listed by Recall, use case not described). (fetched) https://www.recall.ai/solutions/hr
- Hypercontext / Spinach AI: Spinach's own FAQ says Hypercontext is now part of Spinach AI and accounts and data transition to the Spinach platform; it describes "Spinach AI (formerly Hypercontext)" as combining goals, agendas and notes for 1:1s. No deal date, terms, or statement of who acquired whom was found. (snippet) https://spinach.ai/hypercontext
- Spinach AI today: bot-based meeting assistant (joins meetings, notes, action items, Jira/Slack/Asana), repositioned from agile standups to a broader assistant with "Ask Spinach" and role templates. No acquisition or shutdown news found. (snippet) https://tldv.io/blog/spinach-ai-review/ and https://yardstickresearch.app/tear-sheet/spinach-ai/
- Topicflow: founded 2022; raised $1.8M (2024); continuous-feedback platform covering 1:1s, team meetings, goals, KPIs and reviews; uses AI to prompt managers about timely performance conversations and to analyze meeting transcripts. (snippet) https://www.geekwire.com/2024/topicflow-raises-1-8m-to-rethink-performance-reviews-with-help-from-ai/ . A profile lists "manager effectiveness metrics" among its tools. (snippet, third-party) https://www.hirebase.org/company/topicflow
- Teamflect (Microsoft Teams-native): has a help article on using AI meeting transcripts; its public roadmap lists "AI-Powered Meeting Intelligence" as in progress, and users requested that AI note-taker output flow into Shared Notes instead of being pasted. Notes stay between manager and employee; HR can see whether 1:1s happen. A "Teamflect Agent" preps 1:1s, drafts goals and "flags risks" from performance data inside Teams. (snippet) https://help.teamflect.com/en/articles/16860659-how-to-use-ai-meeting-transcripts-in-teamflect , https://roadmap.teamflect.com/feature-requests/p/meetings-ai-powered-meeting-intelligence , https://teamflect.com/one-on-one-software , https://teamflect.com/ai-agent
- Range: site and help center still present check-ins as the core product; no shutdown evidence found. No AI 1:1 transcript feature found. (snippet) https://www.range.co/help/article/what-are-check-ins
- Confirm: launched a unified AI agents platform (AI HRBP, onboarding, manager coaching, service desk) at Transform in March 2026, built on Organizational Network Analysis and work signals from Slack, Jira and Asana; pricing reported from $8 per person per month. Meeting-transcript ingestion not mentioned. (snippet) https://hrtechedge.com/confirm-unveils-unified-ai-agents-platform-to-replace-fragmented-hr-tools
- Mesh.ai: acquired by Netchex in 2025; relaunched 2026-07-20 as "Mesh", six AI HR teammates for deskless employers (payroll, compliance, scheduling, HR admin). No longer a 1:1 or performance specialist in the knowledge-worker sense. (snippet) https://itbrief.co.uk/story/netchex-launches-ai-hr-teammates-for-deskless-workers
- Kona (15Five; included only as the clearest documented coaching pattern): joins 1:1s on Zoom, Meet or Teams as a bot; "never stores recordings, only transcripts"; transcripts encrypted, kept 30 days, then deleted, and not accessible to HR, managers or employees; notes filtered to "performance-relevant content". Kona Coach (per-manager add-on) gives private post-meeting tips ("visible only to you"), morning briefs and monthly growth reports on behavior trends. Kona-captured content can feed review "Moments". An "HR Outcomes Dashboard" is referenced but its contents are not described. (fetched) https://success.15five.com/hc/en-us/articles/36196491046043
- 15Five and Leadr appear as customer logos on Recall.ai's HR page (capture vendor: listed by Recall, use case not described). (fetched) https://www.recall.ai/solutions/hr
- Rippling: per Recall.ai, Rippling uses Recall meeting data to "generate notes, surface insights on performance and employee satisfaction" and to update task trackers from 1:1 discussions. This is Recall's description, not Rippling's own documentation. (fetched) https://www.recall.ai/solutions/hr . Rippling's own 1:1s pages mention performance context in the meeting but not a recorder or sentiment. (snippet) https://rippling.com/blog/introducing-1-1s
- Smaller HR vendors adding a review-meeting notetaker: Appraisd AI Notetaker (beta per its product video; records via shared screen audio; access limited to review participants; no model training on customer data). (snippet) https://www.appraisd.com/performance-management/ai-notetaker and https://help.appraisd.com/hc/en-us/articles/32019274365981-AI-notetaker . Talos Perform AI Notetaker (structured notes aligned to each review question; "80%" write-up time reduction is a claim). (snippet) https://talos360.co.uk/perform/ai-notetaker/ . Keka PERFORM "AI-Powered 1:1 Meeting Transcription Summary, MS Teams Integration" for alpha customers. (snippet, title only) https://help.keka.com/hc/en-us/articles/42553412708113-PERFORM-AI-Powered-1-1-Meeting-Transcription-Summary-MS-Teams-Integration-Alpha-Customers

AI manager coaching
- Valence (Nadia): May 2026 announcement of deeper Microsoft 365 integration via Microsoft Graph, beginning to incorporate Work IQ context to give Nadia insight into team dynamics and communication patterns; deeper Copilot integration described as upcoming. Nadia is available inside Microsoft Teams. No source confirms full meeting-transcript ingestion. (snippet) https://valence.co/blog/valence-microsoft-365-may-2026 , https://techintelpro.com/news/ai/enterprise-ai/valence-brings-ai-coaching-deeper-into-microsoft-365 , https://appsource.microsoft.com/product/office/WA200007824
- Valence says Nadia uses calendar and meeting data to identify real team structures and time coaching. (snippet, claim) https://valence.co/ai-and-the-workforce/ai-coaching-workforce-transition-parker-mitchell-valence
- BetterUp AI Coach / Grow: BetterUp's blog says the coach's memory can draw on Microsoft Teams and Slack conversations, meeting transcripts and HR-system reviews. (snippet, vendor-published) https://www.betterup.com/blog/ai-coach-memory . Operates inside Slack and Teams, pulls context from systems such as Workday; an MCP server (mcp.betterup.co) is reported by a third-party review. (snippet) https://workinsiders.com/tools/betterup/
- CoachHub AIMY: conversational AI coach used as between-session support, 80+ languages; no meeting-transcript integration mentioned. (snippet, comparison blogs) https://www.boon-health.com/learn/resources/best-ai-coaching-platforms
- Humu: acquired by Perceptyx in August 2023; nudges (Slack, Teams, email) folded into Perceptyx's platform, branded "Activate". Input is survey data, not conversations. (snippet) https://www.hr-brew.com/stories/2023/08/10/technically-hr-employee-survey-platform-perceptyx-acquires-humu-s-nudge-tech and https://blog.perceptyx.com/ai-is-fueling-our-obsession-and-humu-is-the-key-to-people-evolution
- Yoodli: pivoted from consumer speech coaching to enterprise AI roleplay; $40M Series B led by WestBridge, valuation above $300M (TechCrunch, 2025-12-05); customers named include Google, Snowflake, Databricks. It is a practice/roleplay product, not a 1:1 capture product. (snippet) https://techcrunch.com/2025/12/05/ex-googlers-yoodli-triples-valuation-to-300m-with-ai-built-to-assist-not-replace-people
- DIY signal: investor Tomasz Tunguz described (January 2026) an agent that reviews his own meeting transcripts nightly and scores listening, empathy and questioning. Personal project, not a product. (snippet) https://www.tomtunguz.com/a-coxswain-on-your-shoulder/index.md

Conversation intelligence applied to managers/employees
- Read AI: coaching is a section of every meeting report ("add Read to your meetings, and then view the report after"); pitched as using existing meetings to provide coaching metrics instead of manager coaching. Bot-based. (snippet) https://support.read.ai/hc/en-us/articles/29349563165715-How-does-Read-s-coaching-work and https://www.read.ai/coaching . Read builds an engagement baseline per participant. (snippet) https://techcrunch.com/2024/04/02/read-ai-expands-its-ai-powered-summaries-from-meetings-to-messages-and-emails
- Gong: scorecards with "AI Call Reviewer" that suggests scorecard answers from the transcript or scores calls fully automatically (labelled "Scored by: Gong AI"); model updated 2026-01-27. (snippet) https://help.gong.io/docs/gong-ai-for-scoring and https://help.gong.io/docs/all-about-scorecards
- Microsoft Viva Insights / Copilot Dashboard: aggregation enforced by an admin-set minimum group size that cannot go below five; org insights are hidden when a group falls below threshold. Sources conflict on the default (5 vs 10). (snippet) https://learn.microsoft.com/en-us/viva/insights/privacy/privacy-considerations , https://learn.microsoft.com/en-us/viva/insights/advanced/setup-maint/privacy-settings , https://mc.merill.net/message/MC788977

### Inferences
- Three capture archetypes now coexist in the HR-adjacent layer: (a) own bot, often on Recall.ai (15Five Kona, Fellow, Rippling per Recall); (b) botless ingestion of someone else's transcript (Windmill: Zoom/Meet/Gong/Granola/Roam; Betterworks: Zoom API plus paste/upload); (c) no capture, context from the work graph (Confirm via ONA; Valence via Microsoft Graph/Work IQ). Archetype (b) is the low-friction route for a platform that does not want to own recording.
- Recall.ai is the only capture/transcription infrastructure vendor I could tie to named HR players from a public page. For Windmill, Betterworks, Topicflow, Teamflect and Spinach the underlying vendor is Unknown.
- The pure "1:1 tool" category has thinned: Hypercontext was absorbed into Spinach, Mesh into Netchex (and repositioned), and Spinach/Fellow now sell as general or sales meeting assistants. The 1:1 workflow is consolidating into performance suites on one side and general notetakers on the other.

### Gaps
- Not verified this run (no usable results or not searched): Pando, Peoplelogic, Mirro, Small Improvements, Zelt, Effy, Rising Team, Cloverleaf, Marlee, Poised, Pinnacle, Chorus/ZoomInfo, Clari, Zoom Revenue Accelerator, Worklytics, Glean. Status and transcript handling for each: Unknown.
- Fellow, Topicflow and Teamflect details are snippet-level; their current plan gating and any admin analytics are Unknown.
- No YC/Product Hunt startup founded 2023 to 2026 and built specifically around recording 1:1s for performance management was confirmed beyond Windmill and Topicflow; searches returned generic notetaker listicles.
- Whether Rippling's "employee satisfaction" insight (Recall's wording) is a shipped, admin-visible feature is Unknown.

## 2. Catalogue of downstream uses of conversation data (named examples, status)

### Takeaway
The well-evidenced, shipped downstream uses are the "close-in" ones: action-item carry-forward, pre-meeting briefs, agenda suggestions, goal-progress suggestions and review evidence. The "far-out" uses the product lead asked about (manager-effectiveness scores, individual sentiment or risk, HR-admin dashboards built on 1:1 content) are almost entirely absent from public vendor documentation.

### Cited Findings
- Action-item tracking and carry-forward: Windmill ("remembers action items from previous meetings and carries them forward"), shipped. (fetched) https://gowindmill.com/features/one-on-ones . Betterworks suggested action items, present-tense. (fetched) https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes . 15Five Kona suggested action items, shipped. (fetched) https://success.15five.com/hc/en-us/articles/36196491046043
- Pre-meeting briefs and agenda generation from past meetings: Windmill "Catch Me Up" and Suggested Topics (shipped); Betterworks private prep brief per participant; Kona Coach morning briefs. (fetched; same three URLs as above)
- Goal/OKR progress updates: Betterworks identifies progress, suggests milestone updates and surfaces potential new goals, all pending user confirmation. (fetched) https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Performance-review drafting from meeting evidence: 15Five reviews set to "With 15Five AI" can use Kona-captured content as "Moments"; AI drafts text, managers select all ratings. (fetched) https://success.15five.com/hc/en-us/articles/36196491046043 . Teamflect pulls goals, feedback and past 1:1 notes into the review template. (snippet) https://teamflect.com/one-on-one-software . Talos Perform maps transcript to each review question. (snippet, claim) https://talos360.co.uk/perform/ai-notetaker/
- Continuous feedback capture: Windmill says information from 1:1s, feedback, surveys and reviews "is interconnected"; no specific transcript-to-feedback feature described. (fetched) https://gowindmill.com/features/one-on-ones
- Manager behavior coaching: Kona Coach private post-meeting tips plus monthly growth reports on focus-area progress and behavior trends (shipped, paid add-on, no numeric scores described). (fetched) https://success.15five.com/hc/en-us/articles/36196491046043 . Read AI coaching metrics per meeting (pace, filler words, engagement). (snippet) https://www.read.ai/coaching
- Manager-effectiveness metrics: Topicflow is described by a third-party profile as offering "manager effectiveness metrics"; whether these derive from transcripts is Unknown. (snippet) https://www.hirebase.org/company/topicflow
- Sentiment/engagement at individual level: Read AI engagement and sentiment scores per participant (shipped; see section 3 for reception). (snippet) https://techcrunch.com/2024/04/02/read-ai-expands-its-ai-powered-summaries-from-meetings-to-messages-and-emails
- Insights on performance and employee satisfaction from 1:1 data: attributed to Rippling by Recall.ai. Status and audience Unknown. (fetched) https://www.recall.ai/solutions/hr
- Admin view of 1:1 activity (metadata only): Windmill admins see which 1:1s were held, date and participants only. (fetched) https://gowindmill.com/features/one-on-ones . Teamflect HR sees whether 1:1s are happening. (snippet) https://teamflect.com/one-on-one-software
- "Flags risks": Teamflect Agent, from performance data inside Teams; whether the input includes 1:1 transcripts is Unknown. (snippet) https://teamflect.com/ai-agent
- Nudges in Slack/Teams: Windmill's Windy (Slack); Perceptyx Activate/Humu nudges (survey-driven); Valence Nadia and BetterUp Grow inside Teams/Slack. (snippet) https://help.gowindmill.com/windy/meet-windy , https://blog.perceptyx.com/ai-is-fueling-our-obsession-and-humu-is-the-key-to-people-evolution , https://appsource.microsoft.com/product/office/WA200007824 , https://workinsiders.com/tools/betterup/
- AI agent / chat / MCP over the meeting corpus: Fellow "Ask Fellow"; Spinach "Ask Spinach". (snippet) https://help.fellow.ai/en/articles/8461666-fellow-ai-features and https://yardstickresearch.app/tear-sheet/spinach-ai/ . Lattice's October 2026 product update is titled "Lattice Meetings, New MCP Tools, and More" (title only; covered by another researcher). (snippet) https://lattice.com/blog/october-2026-product-updates
- Calibration/talent-review evidence: Betterworks says conversation context "can support reviews and talent decisions" without describing a feature. (fetched) https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes . Meeting.ai markets searchable transcripts of calibration sessions themselves. (snippet) https://meeting.ai/performance-review-calibration

### Inferences
- A consistent design choice across the evidenced products is "suggest, human confirms": Betterworks' pending recommendations, 15Five's "managers select all ratings", Windmill's "AI is not evaluating anyone's performance". Auto-writing to the system of record without confirmation was not found.
- Recognition suggestions, development/growth-plan suggestions and skills inference from 1:1 transcripts: no shipped named example found among the players in my scope. For QW these look like open whitespace rather than table stakes, with the caveat that the HR-suite researchers may have found examples.

### Gaps
- No evidence found (in scope) for: recognition suggestions from transcripts, growth-plan suggestions from transcripts, skills inference from transcripts, talk-ratio or question-quality metrics specifically for manager-employee 1:1s, or published manager benchmarks.
- Contents of 15Five's HR Outcomes Dashboard for Kona not seen.

## 3. Does anyone expose 1:1-derived sentiment or risk to HR admins? Trust handling and backlash

### Takeaway
I found no vendor that publicly documents an HR-admin dashboard of sentiment, burnout or flight risk derived from 1:1 conversation content, in aggregate or individually. The documented norm is the opposite: content private to the pair, coaching private to the manager, HR sees only that meetings happened. The nearest exceptions are Recall.ai's description of Rippling ("insights on performance and employee satisfaction") and Read AI's per-participant engagement/sentiment scores, and Read is the clearest example of backlash.

### Cited Findings
- Windmill: "1:1 notes and agendas are private to the two participants by default"; admins see only date and participants of held 1:1s; briefs are "built only from work you already have access to". (fetched) https://gowindmill.com/features/one-on-ones
- 15Five Kona: transcripts not accessible to HR, managers or employees; deleted after 30 days; no recordings stored; coaching tips "visible only to you"; notes limited to performance-relevant content; manager can pause or remove Kona. (fetched) https://success.15five.com/hc/en-us/articles/36196491046043
- Betterworks: each participant gets a private prep brief; nothing is written until a user confirms; no HR dashboard, sentiment or manager-effectiveness metric described. (fetched) https://www.betterworks.com/magazine/from-conversation-to-performance-intelligence-how-betterworks-turns-11s-into-more-than-meeting-notes
- Teamflect: notes stay between manager and employee; HR sees whether 1:1s are happening. (snippet) https://teamflect.com/one-on-one-software
- Appraisd: recording access limited to review participants. (snippet) https://www.appraisd.com/performance-management/ai-notetaker
- Rippling (via Recall.ai): meeting data used to "surface insights on performance and employee satisfaction". Who sees these is not stated. (fetched) https://www.recall.ai/solutions/hr
- Microsoft's model for aggregate insight: minimum group size (floor of five) before leaders or managers see group metrics. (snippet) https://learn.microsoft.com/en-us/viva/insights/privacy/privacy-considerations
- Read AI backlash: privacy advocates called its sentiment tool overly invasive and prone to bias (TechCrunch; date not visible in result). (snippet) https://techcrunch.com/?p=2685382 . A review site reports the University of Washington blocked Read AI over security and privacy risks and that it can join meetings without attendees knowing. (snippet, third-party) https://www.eesel.ai/blog/read-ai-reviews . Competitor reviews say individual engagement numbers reaching a manager without employee agreement drive the angriest reviews, and that sentiment analysis raises EU AI Act questions; Read reportedly gives EU/UK users scores without video or facial input. (snippet, competitor-authored) https://www.laxis.com/blog/read-ai-review/ and https://tldv.io/blog/read-ai-review-alternatives/
- Modality matters legally, per one commentary: transcript text analysis is treated differently from voice-tone inference (biometric; restricted under EU rules), yet both can sit in one dashboard. (snippet, low-authority) https://digitaldigest.com/emotion-recognition-ai-workplace-monitoring/
- Practitioner guidance: keep coaching data separate from performance data, with clear rules on what managers can see. (snippet) https://hrreview.co.uk/?p=388361 . A 1:1-notetaker guide advises keeping the record private rather than using it as a performance tool. (snippet, vendor blog) https://scribbl.co/post/ai-notetaker-for-1-on-1-meetings
- Consent baseline (Kolmogorov Law survey via Pollfish, fielded 2026-07-08, n=500 employed US adults, margin about ±4.4%): 33.4% say an AI notetaker has been in their work meetings; of those 167, 34.7% were always asked permission, 25.1% never; 18.8% of all workers discovered after the fact that a meeting was recorded; on discovering repeated secret recording 29.2% would complain to HR, 19% would speak with a lawyer. Commissioned by a law firm; does not cover 1:1s specifically. (fetched) https://kesq.com/stacker-business-economy/2026/07/16/ai-notetakers-have-sat-in-on-1-in-3-us-workers-meetings-but-only-a-third-say-they-were-asked-first/
- Behavior change: a Fellow 2025 survey reportedly found 84% of users change how they speak when an AI notetaker is present. (snippet, vendor survey via secondary page) https://stealthagents.com/research/ai-meeting-assistant-statistics-2026

### Inferences
- Trust mechanisms seen in shipped products, in order of frequency: pair-only visibility of content; manager-only visibility of coaching; no HR or manager access to raw transcripts; short transcript retention with no audio/video; relevance filtering before anything is stored; human confirmation before data moves into goals or reviews; admin visibility limited to meeting occurrence. Aggregation thresholds exist in the Microsoft work-pattern model but I did not find one applied to 1:1 content by an HR vendor.
- A QW feature that routes 1:1-derived sentiment to an admin dashboard would be ahead of what competitors publicly document, which cuts both ways: differentiation, and no market precedent that employees accept it. The Read AI reception suggests individual-level scores visible to managers are the specific trigger for backlash; aggregate, thresholded, text-only signals are untested rather than proven safe.
- Absence from public docs is not proof of absence in product. Vendors have a reason not to advertise HR-visible sentiment from 1:1s.

### Gaps
- No documented public backlash aimed at an HR-suite 1:1 assistant (as opposed to Read AI or generic notetakers) was found.
- No vendor found that offers employee-owned or opt-in-to-share 1:1 data as an explicit, documented model.
- Rippling's actual feature and audience need primary-source confirmation.

## 4. What the sales conversation-intelligence market (Gong) teaches

### Takeaway
In sales CI, transcript-based scorecards, AI auto-scoring, coaching metrics and deal-risk flags became standard, and the documented trajectory is from human scoring to AI-suggested to fully automatic. Reception evidence is thin but points the same way as Read AI: reps experience it as surveillance.

### Cited Findings
- Gong scorecards: AI Call Reviewer suggests answers per scorecard question from the transcript or reviews whole calls automatically; automatic results are labelled "Scored by: Gong AI"; scorers can accept or change suggestions. (snippet) https://help.gong.io/docs/gong-ai-for-scoring
- Gong frames scorecards as visibility into whether coaching happens, whether reps apply it and whether it affects performance; automatically generated scorecards do not count as active manager coaching in Coaching metrics. Scorecards are plan-gated. (snippet) https://help.gong.io/docs/all-about-scorecards
- Deal health scoring and risk flagging are listed among Gong AI capabilities by a third-party review, which also states reps often resist Gong because it "feels like surveillance". (snippet, low-authority) https://ai-sales-global.pages.dev/reviews/gong-review/
- Convergence of the two markets: Windmill ingests Gong transcripts into 1:1s. (fetched) https://gowindmill.com/features/one-on-ones . Fellow markets itself as a Gong alternative. (snippet) https://fellow.ai/compare/fellow-vs-gong

### Inferences
- If the HR market follows sales CI, the likely sequence is: summaries and action items, then evidence-linked rubric answers suggested by AI (the review "Moments" pattern), then automatic scoring against a rubric, then aggregate risk rollups. HR vendors are at step two today.
- Gong's choice not to count AI-generated scorecards as "manager coaching" is a useful design precedent: measure whether the human did the coaching, separately from what the AI produced.
- The sales analogy is imperfect: sales calls involve an external party and a clear outcome (deal won/lost) to validate scores against; manager 1:1s have neither, and the recorded party is the employee being evaluated.

### Gaps
- No survey or independent data on rep reception of scoring found. Chorus, Clari and Zoom Revenue Accelerator not researched.

## 5. Analyst and practitioner views

### Takeaway
I found no Gartner, Forrester or RedThread research specifically on 1:1 transcripts as a performance-management input. Josh Bersin's public line is that performance management is a large-data evaluation problem AI will take on, without (in what I could see) addressing 1:1 recordings specifically.

### Cited Findings
- Josh Bersin (February 2026 interview transcript) argues performance management means assessing people on "lots and lots of data" and that AI will do that work; meeting transcripts not mentioned. (snippet) https://arist.com/resources/blogs/josh-bersin-and-arist-the-moment-is-now-for-ai-in-hr
- Bersin wrote "Can AI Do Performance Reviews? Rippling Says Yes" (October 2024) and "Perceptyx Acquires Humu: HR Tech Is Harder Than It Seems"; titles only seen. (snippet) https://joshbersin.com/2024/10/can-ai-do-performance-reviews-rippling-says-yes/ and https://joshbersin.com/?p=38678
- Bersin published "The Rise of the Supermanager" on 2026-11-15, with new research on AI's effect on management; content not read. (snippet) https://joshbersin.com/
- Gartner's Nader Henein (via Computerworld, relayed by a secondary page) said allowing third-party AI notetakers into Teams meetings may reduce IT's ability to control access to sensitive information. (snippet, secondary) https://stealthagents.com/research/ai-meeting-assistant-statistics-2026
- Vendor-side framing that "meeting AI is becoming the manager coaching layer" (pattern detection across many 1:1s). Vendor opinion. (snippet) https://upmeet.ai/en/blog/meeting-ai-is-becoming-the-manager-coaching-layer
- SHRM 2026 figure relayed by a vendor blog: 61% of workers trust senior leaders when they discuss AI, ranging from 80% of directors and above to 47% of individual contributors. (snippet, secondary) https://wellhub.com/en-us/blog/wellness-and-benefits-programs/ai-resentment-at-work-rebuild-trust/

### Inferences
- The analyst conversation in 2026 is about agents and "superagents" in HR broadly; 1:1 transcript use is being driven by vendor product marketing rather than by analyst frameworks.

### Gaps
- No RedThread, Forrester or HR Tech/UNLEASH 2025-2026 session coverage on this topic was found. A "Forrester 2026" notetaker-abandonment figure and a "Gartner 38% of agreed actions missed" figure appear only on secondary stats pages and should not be used without the originals.
- Bersin's specific position on recording 1:1s: Unknown.

## 6. Evidence on adoption and outcomes

### Takeaway
There is no independent evidence that AI-captured 1:1s improve follow-through, review quality or manager effectiveness. What exists is vendor claims, one adoption anecdote, and one adjacent trial showing AI coaching did not beat structured written reflection.

### Cited Findings
- Windmill claims "90% faster reviews" and "93% employee satisfaction", and that top teams "saved hundreds of hours on their 1:1s". (claim) https://gowindmill.com/ and https://gowindmill.com/features/one-on-ones
- Talos claims 80% less write-up time. (snippet, claim) https://talos360.co.uk/perform/ai-notetaker/
- Topicflow adoption anecdote: customers mostly bought for reviews; within a few months 30% of managers were actively using it for 1:1s and team meetings. Source is a designer's personal portfolio, not the company. (snippet) https://portfolio-1gw.pages.dev/topicflow-meetings
- A 2026 randomized trial (as relayed by HR Review) found an AI career coach improved short-term goal progress versus no support but did not beat structured written reflection. (snippet, secondary) https://hrreview.co.uk/?p=388361
- Transcript accuracy limits any score built on it: one test reported live transcription near 50% accurate rising to about 80% post-call; overlapping speech causes misattribution. (snippet, low-authority) https://techpoint.africa/guide/best-ai-notetakers-tested/ and https://www.assemblyai.com/blog/top-ai-notetakers
- Validation analog: an arXiv study compares LLM-rated scores from classroom-observation transcripts against human raters. Not about workplace 1:1s. (snippet) https://arxiv.org/pdf/2609.18274

### Inferences
- Outcome evidence is a market-wide gap. A vendor that publishes credible before/after data on action-item completion or review quality would stand out.
- Speaker misattribution is a sharper risk in a performance context than in general notetaking, because an utterance attributed to the wrong person becomes evidence about them.

### Gaps
- No peer-reviewed or analyst study of AI 1:1 capture and manager effectiveness found. Kona, Lattice and similar outcome claims are with the HR-suite researchers.
