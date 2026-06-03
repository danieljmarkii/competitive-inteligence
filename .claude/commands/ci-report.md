---
description: Run the monthly competitor intelligence update (Slack digest + package brief)
argument-hint: "<YYYY-MM> | <START_DATE> <END_DATE>  (e.g. 2026-05  or  2026-05-01 2026-05-31)"
allowed-tools: Read, WebFetch, WebSearch, Glob
---

You are running the **monthly competitive intelligence update** for Quantum Workplace.

## 1. Resolve the date window from the argument
Argument received: `$ARGUMENTS`

- If it is a single `YYYY-MM` (e.g. `2026-05`): set **START_DATE** = first day of that month, **END_DATE** = last day of that month.
- If it is two ISO dates (`YYYY-MM-DD YYYY-MM-DD`): use them directly as START_DATE and END_DATE.
- If empty: default to the **most recently completed calendar month** relative to today, and state which month you chose.
- Echo the resolved window back before you begin: `Window: START_DATE → END_DATE (Month YYYY)`.

## 2. Load the authoritative files
Read all three, in this order, before doing any research:
1. `CI-Context.md` — QW positioning + canonical package taxonomy.
2. `CI-Competitor.md` — competitor list, source URLs, source flags.
3. `CI-Prompt.md` — the full methodology and output spec. **Follow it exactly.**

## 3. Execute
Run the workflow defined in `CI-Prompt.md` for the resolved window:
- Scan each competitor's sources; use **runtime URL discovery** when a source is blocked/stale (do not call a blocked source "no changes").
- Apply the Materiality Gate; classify each change into a QW package or Other / Cross-Platform.
- Use `WebFetch` for known source URLs and `WebSearch` for discovery/fallback.

## 4. Produce (in this order)
1. **Slack Digest** — package-organized, ready to paste (per `CI-Prompt.md` → Output 1).
2. **Package Brief** — audit-ready backup (per Output 2), including **Source Health** and a copy/paste block of any blocked/stale URLs for `CI-Competitor.md`.

Keep it evidence-led: fewer verified items beats a padded list. Do not invent competitors or sources outside the files.
