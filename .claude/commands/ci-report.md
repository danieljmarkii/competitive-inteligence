---
description: Run the monthly competitor intelligence update (Slack digest + package brief + workflow retro)
argument-hint: "<YYYY-MM> | <START_DATE> <END_DATE>  (e.g. 2026-10  or  2026-10-01 2026-10-31)"
allowed-tools: Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, Bash(python3 tools/ci_sources.py:*), Bash(curl:*), Bash(python3 tools/landscape_slide.py:*)
---

You are running the **monthly competitive intelligence update** for Quantum Workplace.

## 1. Resolve the date window from the argument
Argument received: `$ARGUMENTS`

- If it is a single `YYYY-MM` (e.g. `2026-10`): set **START_DATE** = first day of that month, **END_DATE** = last day of that month.
- If it is two ISO dates (`YYYY-MM-DD YYYY-MM-DD`): use them directly as START_DATE and END_DATE.
- If empty: default to the **most recently completed calendar month** relative to today, and state which month you chose.
- Echo the resolved window back before you begin: `Window: START_DATE → END_DATE (Month YYYY)`.

## 2. Load the authoritative files, then last run's lessons
Read, in this order, before doing any research:
1. `CI-Context.md` — QW positioning + canonical package taxonomy.
2. `CI-Competitor.md` — competitor list, sources with their proven access `route`, flags, Open source issues.
3. `CI-Prompt.md` — the full methodology, Access Playbook, output spec, and Run Retro rules. **Follow it exactly.**
4. The **Workflow Retro → Open issues** section of the most recent `reports/*-CI-Report.md`. Start there.

## 3. Pre-flight (tool-driven)
- `python3 tools/ci_sources.py check` — source health for every registry source. Record the summary counts: they are the Retro's "before" numbers.
- `python3 tools/ci_sources.py collect <START_DATE> <END_DATE> --news` — writes the evidence pack to `out/<START>_<END>/evidence.md`.
- If the tool cannot reach the network at all, follow CI-Prompt.md's environment-wide-failure rule (test `curl` before falling back to search-only mode).

## 4. Execute
Run the workflow in `CI-Prompt.md` for the resolved window:
- Start from the evidence pack; verify every candidate against its official dated page.
- For competitors with no healthy source, or any source that fails, work the **Access Playbook** in order. Never call a blocked source "no changes."
- Apply the Materiality Gate; classify each change into a QW package or Other / Cross-Platform.
- Keep a running log of every failure and the route that beat it: the Retro needs it.

## 5. Produce and save
Write `reports/<YYYY-MM>-CI-Report.md` containing, in order:
1. **Slack Digest** (per `CI-Prompt.md` → Output 1).
2. **Roadmap Watch** (optional, Output 1b), when a squad meeting needs forward-looking context.
3. **Package Brief** (Output 2), including **Source Health** and the **Coverage report**.
4. **Workflow Retro** (mandatory).

## 6. Retro & curate (mandatory)
Apply CI-Prompt.md → RUN RETRO & SELF-CURATION: update `CI-Competitor.md` (promote / re-route / demote sources with `verified` dates, fill gaps, set `news_query`, bump version), add any new generalizable move to the Access Playbook, re-run `python3 tools/ci_sources.py check`, and record before/after counts in the Retro. Changes are made in the open, on the run's branch, for human review.

## 7. Optional: landscape slide
If asked for a squad-meeting slide, write `reports/<YYYY-MM>-landscape-slide.json` and run `python3 tools/landscape_slide.py reports/<YYYY-MM>-landscape-slide.json reports/<YYYY-MM>-landscape-slide.pptx` (spec: CI-Prompt.md → Output 3).

## 8. Report back
Reply with the Slack Digest TL;DR, the item count, and three lines from the Retro: what broke, what the run fixed in the registry, and the top Open issue. Keep it evidence-led: fewer verified items beats a padded list. Do not invent competitors or sources outside the files.
