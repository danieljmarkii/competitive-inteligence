# CI — Competitor File (v1.5) — Lean Sources + Navigation Flags

Purpose
- Canonical competitor list (names + aliases) and starting source URLs to monitor for product changes.
- This file is **data**, not methodology. Global crawling/navigation rules live in the Prompt File.

Hard rules
- Do **not** invent competitors outside this file.
- Use the **name** field as the canonical vendor name.
- All URLs must be plain https.

---

## Flags (source behavior hints)
- `index` : the URL is a hub/listing; you must click/open child pages in-window.
- `running_list` : a single long page with many dated entries/sections; find month headers and extract in-window.
- `ui_dynamic` : content often hides behind tabs/accordions; avoid click-reliance (prefer text extraction + find).
- `login` : likely requires authentication; if blocked, record Access limits and do not claim “no notable changes.”
- `search_required` : no reliable release notes; use constrained web search as a fallback.
- `press` : secondary signal source (e.g., PRWeb); downgrade confidence unless corroborated.
- `year_pinned` : URL/title is scoped to a specific year; if it doesn’t match the window year, find the equivalent page(s) for the window year.

## Source kinds (scan order hint)
`release_notes | product_updates | help_center | docs | blog | community | roadmap | status | press`

---

## Data (YAML)
```yaml
version: "1.5"

competitors:
  - name: "15Five"
    aliases: ["Kona", "Emplify (acquired)", "15Five Engage", "15Five Perform"]
    website: "https://www.15five.com/"
    sources:
      - kind: release_notes
        url: "https://success.15five.com/hc/en-us/articles/36062624232219-What-s-New-in-15Five-Product-Releases"
        flags: ["running_list", "ui_dynamic"]
      - kind: help_center
        url: "https://success.15five.com/hc/en-us"
        flags: ["index", "ui_dynamic"]

  - name: "Culture Amp"
    aliases: []
    website: "https://www.cultureamp.com/"
    sources:
      - kind: product_updates
        url: "https://support.cultureamp.com/en/collections/3904790-product-updates"
        flags: ["index"]

      # 2026+ change: Culture Amp moved “new updates” to a public newsfeed starting 2026.
      - kind: product_updates
        url: "https://support.cultureamp.com/en/collections/17746165-2026-product-updates"
        flags: ["index", "year_pinned"]
      - kind: product_updates
        url: "https://support.cultureamp.com/en/articles/13331721-accessing-culture-amp-product-updates-in-2026"
        flags: ["year_pinned"]
      - kind: product_updates
        url: "https://intercom.news/culture-amp"
        flags: ["running_list"]

      # 2025 year-pinned module pages (retain for historical windows)
      - kind: release_notes
        url: "https://support.cultureamp.com/en/articles/10368642-employee-engagement-product-updates-2025"
        flags: ["running_list", "year_pinned"]
      - kind: release_notes
        url: "https://support.cultureamp.com/en/articles/10368650-performance-management-product-updates-2025"
        flags: ["running_list", "year_pinned"]
      - kind: release_notes
        url: "https://support.cultureamp.com/en/articles/10368593-goals-1-on-1s-skills-coach-anytime-feedback-product-updates-2025"
        flags: ["running_list", "year_pinned"]
      - kind: release_notes
        url: "https://support.cultureamp.com/en/articles/10363297-employee-development-product-updates-2025"
        flags: ["running_list", "year_pinned"]

      - kind: help_center
        url: "https://support.cultureamp.com/"
        flags: ["index"]

  - name: "Gallup"
    aliases: []
    website: "https://www.gallup.com/"
    sources:
      - kind: help_center
        url: "https://support.gallup.com/hc/en-us"
        flags: ["index", "ui_dynamic"]

  - name: "Lattice"
    aliases: []
    website: "https://lattice.com/"
    sources:
      - kind: product_updates
        url: "https://lattice.com/product-updates"
        flags: ["index", "running_list", "ui_dynamic"]
      - kind: blog
        url: "https://lattice.com/blog?category_equal=%5B%22Product+Updates%22%5D"
        flags: ["index"]
      - kind: help_center
        url: "https://help.lattice.com/hc/en-us"
        flags: ["index", "ui_dynamic"]

  - name: "Microsoft Viva / Glint"
    aliases: ["Viva Glint", "Glint"]
    website: "https://www.microsoft.com/"
    sources:
      # Primary “release-notes-equivalent” surface
      - kind: blog
        url: "https://techcommunity.microsoft.com/category/viva-glint/blog/viva_glint_blog"
        flags: ["index", "running_list"]

  - name: "Peakon / Workday"
    aliases: ["Workday Peakon Employee Voice", "Peakon Employee Voice"]
    website: "https://www.workday.com/"

  - name: "Qualtrics"
    aliases: ["Qualtrics XM", "Qualtrics EmployeeXM"]
    website: "https://www.qualtrics.com/"
    sources:
      - kind: community
        url: "https://community.qualtrics.com/product-release-notes-96"
        flags: ["index", "ui_dynamic", "search_required"]
      - kind: help_center
        url: "https://www.qualtrics.com/support/"
        flags: ["index"]

  - name: "SurveyMonkey"
    aliases: []
    website: "https://www.surveymonkey.com/"
    sources:
      - kind: release_notes
        url: "https://help.surveymonkey.com/en/surveymonkey/new/"
        flags: ["index", "ui_dynamic"]
      - kind: release_notes
        url: "https://help.surveymonkey.com/en/surveymonkey/new/release-notes-may-2025-dec-2025/"
        flags: ["running_list", "year_pinned"]
      - kind: help_center
        url: "https://help.surveymonkey.com/en/"
        flags: ["index"]

  - name: "ADP"
    aliases: ["ADP Workforce Now", "ADP SmartCompliance"]
    website: "https://www.adp.com/"

  - name: "BambooHR"
    aliases: []
    website: "https://www.bamboohr.com/"
    sources:
      - kind: product_updates
        url: "https://www.bamboohr.com/product-updates/"
        flags: ["index", "ui_dynamic"]
      - kind: help_center
        url: "https://help.bamboohr.com/"
        flags: ["index"]

  - name: "Betterworks"
    aliases: []
    website: "https://www.betterworks.com/"
    sources:
      - kind: release_notes
        url: "https://support.betterworks.com/hc/en-us/sections/360012378232-Release-Notes"
        flags: ["index", "ui_dynamic"]
      - kind: help_center
        url: "https://support.betterworks.com/hc/en-us"
        flags: ["index", "ui_dynamic"]

  - name: "Cornerstone OnDemand"
    aliases: ["CSOD", "Cornerstone"]
    website: "https://www.cornerstoneondemand.com/"

  - name: "Energage"
    aliases: ["Top Workplaces platform"]
    website: "https://www.energage.com/"

  - name: "Engagedly"
    aliases: []
    website: "https://engagedly.com/"
    sources:
      - kind: blog
        url: "https://engagedly.com/blog/?integration=Product+Updates"
        flags: ["index"]
      - kind: help_center
        url: "https://help.engagedly.com/"
        flags: ["index"]

  - name: "Leapsome"
    aliases: []
    website: "https://www.leapsome.com/"
    sources:
      - kind: product_updates
        url: "https://help.leapsome.com/hc/en-us/articles/360004361834-Platform-improvements"
        flags: ["running_list", "ui_dynamic"]
      - kind: help_center
        url: "https://help.leapsome.com/"
        flags: ["index", "ui_dynamic"]
      - kind: roadmap
        url: "https://leapsome.notion.site/leapsome/Leapsome-s-Product-Roadmap-c914ffc89c824e7db33130f3cc5bfb1f"
        flags: ["ui_dynamic"]

  - name: "Officevibe (Workleap)"
    aliases: ["Workleap Officevibe"]
    website: "https://workleap.com/officevibe"
    sources:
      - kind: help_center
        url: "https://help.workleap.com/en/"
        flags: ["index"]

  - name: "Paylocity"
    aliases: []
    website: "https://www.paylocity.com/"
    sources:
      - kind: blog
        url: "https://www.paylocity.com/company/about-us/newsroom/in-the-news/"
        flags: ["search_required", "ui_dynamic"]

  - name: "Perceptyx"
    aliases: []
    website: "https://www.perceptyx.com/"
    sources:
      - kind: release_notes
        url: "https://perceptyxhelp.freshdesk.com/support/solutions/folders/63000237891"
        flags: ["index", "ui_dynamic"]
      - kind: help_center
        url: "https://perceptyxhelp.freshdesk.com/support/solutions"
        flags: ["index", "ui_dynamic"]

  - name: "PerformYard"
    aliases: []
    website: "https://www.performyard.com/"
    sources:
      - kind: help_center
        url: "https://support.performyard.com/"
        flags: ["index"]
      - kind: press
        url: "https://www.prweb.com/"
        flags: ["press", "search_required"]

  - name: "Predictive Index"
    aliases: ["The Predictive Index", "PI", "PI Perform"]
    website: "https://www.predictiveindex.com/"
    sources:
      - kind: release_notes
        url: "https://docs.predictiveindex.com/en/collections/12282995-release-notes"
        flags: ["index"]
      - kind: help_center
        url: "https://docs.predictiveindex.com/en/"
        flags: ["index"]

  - name: "UKG"
    aliases: ["UKG Ready", "UKG Pro", "UKG Pro WFM", "Kronos"]
    website: "https://www.ukg.com/"
    sources:
```
