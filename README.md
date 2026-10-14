# Competitive Intelligence — Quantum Workplace

Monthly competitor-update workflow, run from Claude Code. Each run produces the report **and** leaves the workflow better than it found it.

## What's here

| File | Role | Edit when… |
|------|------|------------|
| `CI-Context.md` | **Ground truth** about QW — positioning + the canonical **package taxonomy** (Engagement, Performance, Recognition & Rewards, Development). | QW's strategy, packages, or features change. |
| `CI-Competitor.md` | **Source registry** — competitors, aliases, sources with their proven access `route` and `verified` date, flags, open source issues. | Every run curates it; also when you add/remove a competitor. |
| `CI-Prompt.md` | **Methodology** — how the analysis runs, the tested Access Playbook, output formats, and the Run Retro rules. | You want to change *how* the report works or looks. |
| `.claude/commands/ci-report.md` | The `/ci-report` slash command that ties it all together. | Rarely. |
| `tools/ci_sources.py` | Source-health pre-flight + evidence-pack collector. Reads each source through its registry `route`. | A new access route is worth automating. |
| `tools/landscape_slide.py` | One-slide competitive landscape PPTX for squad meetings. | The slide format changes. |
| `reports/` | Run reports (`<YYYY-MM>-CI-Report.md`), slides, deep-dives. | Each run. |
| `CLAUDE.md` | **Project memory** auto-loaded by Claude Code — the operating contract and non-negotiable conventions. | When the workflow's rules or file roles change. |

> Versions live in each file's header and in git history — **not** in the filename. That keeps the slash command stable.

## How to run

In Claude Code, from this repo:

```
/ci-report 2026-10                 # whole month of October 2026
/ci-report 2026-10-01 2026-10-15   # explicit window
/ci-report                         # defaults to last completed month
```

You get `reports/<YYYY-MM>-CI-Report.md` containing:
1. **Slack Digest** — organized by QW package, with a TL;DR. Paste straight into Slack.
2. **Roadmap Watch** (optional) — announced-but-unshipped competitor items that overlap a squad's roadmap.
3. **Package Brief** — audit-ready backup with sources, a "no notable changes" appendix, **Source Health**, and a coverage report.
4. **Workflow Retro** — what broke, what worked, what the run changed in the registry, and open issues for next month.

Optionally, a one-slide landscape deck for squad meetings: `python3 tools/landscape_slide.py reports/<YYYY-MM>-landscape-slide.json reports/<YYYY-MM>-landscape-slide.pptx`.

## The tools (run them any time)

```
python3 tools/ci_sources.py check                    # health of every registry source, in seconds
python3 tools/ci_sources.py collect 2026-10 --news   # evidence pack -> out/2026-10-01_2026-10-31/evidence.md
```

`check` labels each source OK / STALE / FAIL / NODATE and lists competitors with no healthy source, so a run spends its discovery budget where it's needed. `collect` pulls dated, in-window entries from every source (plus a dated Google News sweep with `--news`). Requires Python 3 and PyYAML.

## How the workflow learns

Before 2026-10, a run *proposed* replacements for blocked sources and a human was supposed to promote them. Nobody owned that step, so every run rediscovered the same walls. Now:

1. **Pre-flight** reads every source through its proven `route` (e.g. the Zendesk Help Center API for help centers whose HTML returns 403).
2. **During the run**, failures are worked through the **Access Playbook** in `CI-Prompt.md`: a short, ordered list of moves that each worked in a real run.
3. **The Retro** applies what was learned: new routes and verified sources go into `CI-Competitor.md`, generalizable tricks into the playbook, and everything is listed in the report and visible in the PR diff for review.

## Quick tour of how a run works

1. `/ci-report` resolves the date window and reads the three `.md` files plus last month's Retro.
2. Pre-flight: `check` + `collect` (evidence pack).
3. Verifies candidates against official dated pages; works the Access Playbook for anything blocked.
4. Filters with the Materiality Gate ("what can a user do differently now?") and classifies each change into a QW package.
5. Writes the Digest + Brief (+ Roadmap Watch), then the Retro, and curates the registry.
