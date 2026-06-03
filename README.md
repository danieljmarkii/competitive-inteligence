# Competitive Intelligence — Quantum Workplace

Monthly competitor-update workflow, run from Claude Code.

## What's here

| File | Role | Edit when… |
|------|------|------------|
| `CI-Context.md` | **Ground truth** about QW — positioning + the canonical **package taxonomy** (Engagement, Performance, Recognition & Rewards, Development). | QW's strategy, packages, or features change. |
| `CI-Competitor.md` | **Data** — competitor list, aliases, starting source URLs, and source flags. | You add/remove a competitor or curate source URLs. |
| `CI-Prompt.md` | **Methodology** — how the analysis is run and how output is formatted. | You want to change *how* the report works or looks. |
| `.claude/commands/ci-report.md` | The `/ci-report` slash command that ties it all together. | Rarely — it just orchestrates the three files above. |

> Versions live in each file's header and in git history — **not** in the filename. That keeps the slash command stable.

## How to run

In Claude Code, from this repo:

```
/ci-report 2026-05            # whole month of May 2026
/ci-report 2026-05-01 2026-05-15   # explicit window
/ci-report                    # defaults to last completed month
```

You get two outputs:
1. **Slack Digest** — organized by QW package (Engagement → Performance → Recognition & Rewards → Development → Other / Cross-Platform), with a TL;DR. Paste straight into Slack.
2. **Package Brief** — audit-ready backup with sources, a "no notable changes" appendix, **Source Health**, and a coverage report.

## Maintaining source URLs

URLs in `CI-Competitor.md` are a *starting point*. When a source blocks bots or goes stale, the run:
- finds a live alternate at runtime (official sibling pages → web search → press → social), and
- reports it under **Source Health** with a suggested replacement.

Promote the good replacements into the YAML when convenient — no need to fix everything at once. Tag chronically blocked URLs with the `bot_blocked` flag.

## Quick tour of how a run works

1. `/ci-report` resolves the date window.
2. Reads the three `.md` files.
3. Scans each competitor's sources (with runtime discovery for blocked ones).
4. Filters with the Materiality Gate ("what can a user do differently now?").
5. Classifies each change into a QW package.
6. Emits the Slack Digest + Package Brief.
