# CI Research — Account-Settings Fields Owned by the HRIS Integration

> **type:** ad-hoc competitive research · **owner:** Competitive Intelligence · **created:** 2026-08-18
> Prepared for the Foundation Squad review of the Account Settings screen. Track versions in git, not in the filename.
> QW package lens: **Other / Cross-Platform** (admin/config/profile settings). Not a monthly `/ci-report` run.

## The question

On QW's Account Settings screen, some fields a user can edit today (e.g., **work email address**) are actually owned by the **nightly HRIS integration**. A user's edit therefore "lives for a day, then resets" on the next sync. Proposed fix: render those rows **inactive / grayed-out** so the value still displays, plus helper copy along the lines of *"This information comes from the HRIS integration; to change it, contact your administrator."* This brief checks how direct competitors handle the same situation.

Scope note: the directly-comparable competitors are the EX/performance platforms that sit **downstream** of an HRIS and sync employee profile data from it (15Five, Lattice, Leapsome, Culture Amp, Betterworks, Engagedly, PerformYard). BambooHR is included as a system-of-record reference, plus the broader cross-industry convention (identity + HRIS platforms).

---

## Bottom line (BLUF)

1. **Yes — this is a solved, conventional problem, and your instinct matches the better-practice pattern.** Displaying an HRIS-owned field as read-only with helper copy that says where it can actually be changed is the dominant convention across HR-tech, identity, and directory platforms.
2. **Competitors split into two enforcement styles:**
   - **Hard lock** — show the field, disable it (grayed-out / read-only / integration badge), block the edit at the UI, and tell the user where to change it. **This is your proposal.** Used by **15Five, Lattice, PerformYard**.
   - **Soft lock** — leave the field editable, then **silently overwrite** the edit on the next sync. Used by **Betterworks, Engagedly, Leapsome, Culture Amp** (for the data itself). **This is what QW's screen does today.**
3. **The soft-lock / silent-overwrite behavior is documented by vendors as a pitfall to route around, not a feature** — the exact "edit reverts on next sync" confusion you're trying to eliminate. Even the soft-lock vendors that keep the field editable still add *messaging* that the HRIS overrules the field (Leapsome), so the helper-copy half of your idea is close to universal.
4. **Recommendation:** proceed with hard-lock + helper copy. Two refinements worth deciding in the meeting: (a) keep a small **employee-editable lane** for fields the employee genuinely owns (preferred name, pronouns, personal phone, notification prefs) rather than locking everything; (b) point the CTA at **where the value actually changes (the HR system)**, since in a true hard-lock even a QW admin can't override a synced field in-app.

---

## The enforcement spectrum

**Group A — Hard lock (display read-only + helper copy; edit blocked at the UI).** This is the target pattern.
- **15Five** — grayed-out, explicitly locked, "contact your Account Admin."
- **Lattice** — grayed-out + sync/"i" icon, tooltip "Synced with SCIM"; keeps an employee-editable lane (preferred name, pronouns, phone).
- **PerformYard** — read-only with an HRIS/SCIM logo badge; field is hidden from the edit form; copy names the source system ("updates must be made in [Gusto]"). Cleanest reference model.

**Group B — Soft lock (field stays editable; silently overwritten on next sync).** This is where QW sits today.
- **Betterworks** — edit allowed, reverted on next sync; docs tell admins to "update it in your HRIS" instead.
- **Engagedly** — per-employee "Change Source" governs ownership; edits are erased on next sync unless the source is switched off the HRIS.
- **Leapsome** — overwrite-on-sync, **but** the employee-facing profile still says the HRIS "will overrule your profile settings… contact your HRIS Admin." (Messaging present even though the field isn't hard-disabled.)
- **Culture Amp** — no employee self-service at all; imports overwrite by default; adds an opt-in per-employee **Name lock** and an automatic **identity-change sync block**.

> Evidence caveat: for several Group A/B vendors the *behavior* is well-corroborated but the exact **visual treatment** (grayed-out vs. editable-but-reverted) could not be screenshot-confirmed because their help centers bot-block automated fetches (see Method & evidence quality). Verified-by-direct-fetch: 15Five, PerformYard, Engagedly, and the industry references. Search-index-corroborated: Lattice, Leapsome, Culture Amp, Betterworks.

---

## Competitor detail (verbatim microcopy where captured)

### 15Five — closest to your proposal (primary-source verified)
- Synced fields render **grayed-out and read-only**. Live microcopy:
  > "Greyed-out fields in your account settings cannot be edited by you directly. There are two reasons a field may be greyed out. Admin-controlled fields — Your Account Admin has restricted editing permissions for that field… HRIS or SCIM-managed fields — Your organization uses an HRIS integration or SCIM provisioning to sync employee data into 15Five. Fields managed by the integration are locked to prevent manual edits from conflicting with the synced data." … "In both cases, contact your Account Admin to request changes to greyed-out fields."
- **Source attribution is generic** — it says "an HRIS integration or SCIM provisioning," not the specific vendor (no "synced from Workday").
- Sync is one-way (HRIS → 15Five), daily; admins choose which employees and fields sync.
- Note: 15Five's brand-new **HRIS Sync 2.0** (2026-04-29 infra + 2026-05-14 audit/observability) did **not** change this field-locking behavior — it's long-standing, settled UX.
- Sources:
  - https://success.15five.com/hc/en-us/articles/10120946011931-Manage-my-account-settings
  - https://success.15five.com/hc/en-us/articles/360045931291-Update-an-Employee-s-Account-Settings
  - https://success.15five.com/hc/en-us/articles/13921199539483-HRIS-Connector

### Lattice — grayed-out + "Synced with SCIM"; smart editable-lane carve-out
- HRIS/SCIM-owned identity fields (email, title, department, manager) render **grayed-out with a sync / "i" icon**. Hovering the SCIM lock shows a banner: **"Synced with SCIM"** (names the mechanism, not the vendor).
- **Keeps an employee-editable lane:** employees can always self-edit **preferred first/last name, pronouns, phone, photo, time zone** — and those are **not** overwritten by sync — while legal name/email/title stay HRIS-owned. Good model for "lock the HRIS fields, keep the personal ones editable."
- Documents the **silent-overwrite trap directly**: a field that is *mapped but not locked* accepts a manual edit with no warning and then gets overwritten on the next sync — i.e., QW's current problem, described in a competitor's own docs as something to avoid.
- Sources:
  - https://help.lattice.com/hc/en-us/articles/22266551943319-SCIM-Integration-Which-fields-will-be-locked-and-which-will-remain-unlocked
  - https://help.lattice.com/hc/en-us/articles/7689935927319-Auto-Sync-Job-Architecture-Default-Fields-with-an-HRIS
  - https://help.lattice.com/hc/en-us/articles/360059481274-Lattice-Name-Fields

### Leapsome — soft-lock data, but still shows the "HRIS overrules" message
- Employee-facing Personal Settings copy:
  > "If your company is using HRIS, some of the information will be automatically brought to Leapsome, and the HRIS will overrule your profile settings in Leapsome. In this case, please contact your HRIS Admin internally."
- Admin/integration doc: "Once the integration is enabled, your HRIS will be the 'source of truth'… Any manual changes made directly in Leapsome will be overwritten by the integration with the next synchronization."
- Attribution generic ("HRIS"). Admins control ownership via attribute **mapping** (leaving a field "Not mapped" keeps it locally editable). One carve-out survives sync: manually added **Teams**.
- Visual treatment (grayed vs. editable-but-reverted) not verbatim-confirmed — documented behavior is overwrite-on-sync + the "HRIS overrules" message.
- Sources:
  - https://help.leapsome.com/hc/en-us/articles/8123626457373-Personal-Settings
  - https://help.leapsome.com/hc/en-us/articles/4409220990993-Synchronize-custom-attributes-from-Personio-BambooHR-or-HiBob-with-Leapsome

### PerformYard — the cleanest reference model (primary-source verified)
- Connected fields are **read-only, badged with an HRIS/SCIM logo, and hidden from the edit form** entirely. Microcopy:
  > "you may see an HRIS or SCIM logo next to some fields, which indicates that the field is managed by your HRIS and cannot be edited." … "for any connected fields, you will no longer be able to edit these data fields within PerformYard… updates to that information must be made in Gusto."
- **Names the source system** in the per-integration copy, and offers **per-field admin ownership toggles** (admins check a box / pick which fields to connect; unconnected fields stay locally editable).
- Because the field is non-editable and removed from the edit form, there is **no silent-overwrite** path — the conflict is prevented, not reconciled after the fact.
- Sources:
  - https://support.performyard.com/article/89-employee-details
  - https://support.performyard.com/article/178-hris-management
  - https://support.performyard.com/article/144-gusto-integration

### Betterworks — soft lock via overwrite; "update it in your HRIS" workflow
- With an active integration the HRIS is system-of-record; manual edits (individual or CSV) are **overwritten on the next sync**:
  > "Any changes made through other user management options (i.e. uploading a file or making individual updates) will be overwritten by the BambooHR integration during the next data sync. This same principle applies to other HRIS integrations as well."
- To change a name, an admin must "update the employee's name in their HRIS," and it flows over on the next sync.
- Whether the profile UI also grays-out/disables the field is **Unknown** — help center is bot-blocked (403); behavior confirmed via search extraction, exact microcopy not.
- Sources:
  - https://support.betterworks.com/hc/en-us/articles/115002660691-Integrations-BambooHR
  - https://support.betterworks.com/hc/en-us/articles/360032136951-User-Management-Users-Individual-Update

### Engagedly — per-employee "Change Source" mechanic
- Governs HRIS data by a per-employee **source** rather than field-level locking. Admins can open and edit any record, but for an HRIS-sourced employee:
  > "Change Source: Update the employee information synced from an HRIS platform such as BambooHR, ADP, or Namely by changing the employee's source." … "if the employee's source is changed back to their HRIS platform, the changes made are erased following the sync."
- Names the actual system. No hard UI lock evidenced (control is source + overwrite). Separate role-based field permissions exist but are unrelated to HRIS ownership.
- Sources:
  - https://help.engagedly.com/access-user-management

### Culture Amp — no self-service; overwrite + two safeguards
- Employees have **no self-service editing** of profile demographics (they can only self-report inside a survey; values then show **view-only**). Admin edits are **overwritten** by the next import by default.
- Two safeguards worth noting: an opt-in per-employee **Name lock** ("the locked name will not change as part of the import process"), and an automatic **sync block** when identity fields change:
  > "If a combination of an employee's Name, Date of Birth, Email or Employee ID are changed, the sync will be blocked to prevent an employee accidentally getting access to another employee's private information, such as performance reviews."
- The identity-change sync block is directly relevant to QW's trust/confidentiality non-negotiable.
- Per-field UI microcopy and source-system naming: **Unknown** (Intercom article bodies don't render to automated fetch; behavior confirmed via search).
- Sources:
  - https://support.cultureamp.com/en/articles/7048546-changing-an-employee-s-name-in-culture-amp
  - https://support.cultureamp.com/en/articles/7048557-how-to-sync-hris-data-from-workday

### BambooHR — system-of-record reference: field-level access model
- As the HRIS itself, BambooHR frames this as **field-level access control**. For any field, an employee gets one of four states:
  1. **No Access** — field is **hidden** from the user entirely.
  2. **View Only** — field is **shown read-only**.
  3. **Edit** — user can change it.
  4. **Edit access with approval** — "you or the person you set as the approver has to verify any changes."
- Useful framing: "No Access = hide, View Only = show read-only" is the more granular version of the show-vs-hide question, and the **edit-with-approval** tier is a middle ground if QW ever wants employees to *request* a change rather than just be told to contact an admin.
- Source (help center is login-gated; from BambooHR's first-party blog):
  - https://www.bamboohr.com/blog/access-levels-bamboohr

### Cross-industry convention (identity + HRIS systems of record)
The same read-only-plus-source-attribution pattern is the norm well beyond EX platforms — useful as "this is industry standard, not just a competitor quirk":
- **SAP SuccessFactors:** "the fields in the Live Profile User Information block… will be read only. These fields can only be updated by the HRIS Sync process to ensure data consistency." — https://userapps.support.sap.com/sap/support/knowledge/en/2791383
- **Okta:** "If the user profile was imported from an external profile source such as… a Human Resources Information System (HRIS)… it will not be possible to edit the attributes in Okta." … "the update must be done in the profile source and then imported." — https://support.okta.com/help/s/article/Unable-to-edit-user-profile-attributes
- **Microsoft Entra ID:** "you must use Windows Server Active Directory to update their identity, contact info, or job info. After making updates, you must wait for the next synchronization cycle to complete." — https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-user-profile-info
- **Guru:** synced profile fields show "Some fields are pulled from an external source" and can't be edited in-app. — https://help.getguru.com/docs/view-your-employee-org-chart-and-sync-from-your-hris

---

## What this means for the Account Settings screen

**Your core proposal is validated — proceed with it.** Show the value, disable the row, add helper copy, point to where it changes. That is the hard-lock pattern used by 15Five, Lattice, and PerformYard and the cross-industry norm. Decisions worth settling with the squad:

1. **Show read-only, don't hide.** For a field the user legitimately needs to see (their own work email), display it grayed-out rather than hiding it — so they know the value exists and that it's authoritative elsewhere. (Hiding is reserved for "no legitimate need to see," e.g., BambooHR's No-Access tier.) Your "displays the email address, grayed out" instinct is right.

2. **Lock the HRIS-owned fields, but keep an employee-editable lane.** Don't blanket-lock the whole screen. Follow Lattice's split: HRIS owns legal name / work email / title / department / manager; the employee keeps **preferred name, pronouns, personal phone, notification preferences, password**, etc. Decide the exact field list against your actual HRIS field map.

3. **Point the CTA at where the value actually changes.** "Contact your administrator" is common (15Five, Leapsome), but note the nuance: in a true hard-lock, **even a QW admin can't override a synced field in-app** — it has to change in the HR system. So the most accurate CTA points to the HR system first, admin second. Draft options below.

4. **Generic vs. named source.** Most peers keep it generic ("your HR system," "your HRIS") — simplest, and it's what 15Five/Lattice/Leapsome do. Naming the specific system (PerformYard: "must be made in Gusto") is more actionable but requires surfacing the connected system per tenant. Recommend **generic to start**, named source as a later enhancement.

5. **Make the lock and the sync agree.** The lock only fixes the *symptom*. Ensure the fields you disable are exactly the ones the nightly sync owns, so there's no field that's editable in the UI yet overwritten by sync (the Lattice "mapped-but-not-locked" trap). Ideally the same field-ownership map drives both the UI's disabled state and the sync's write scope.

6. **Optional guardrails to put on the roadmap (not needed for v1):**
   - **Field-level admin config of ownership** (PerformYard / Leapsome "Not mapped") — let admins decide which fields are HRIS-owned.
   - **Edit-with-approval** (BambooHR) — employees *request* a change that routes to an approver, instead of a dead-end "contact your admin."
   - **Identity-change sync safety block** (Culture Amp) — if Name/DOB/Email/Employee ID change, hold the sync to prevent a mis-sync exposing one employee's data to another. Directly reinforces QW's trust/confidentiality non-negotiable.

## Suggested microcopy (steal-worthy, adapt to voice)

- **Generic + admin CTA (closest to your draft, matches 15Five/Leapsome):**
  > "This information syncs from your HR system and can't be edited here. To update it, contact your HR administrator."
- **Generic + where-to-change + who-to-contact (most accurate for a true hard-lock):**
  > "This field is managed by your organization's HR system. To change it, update it there, or contact your HR administrator."
- **Named-source variant (PerformYard style, if the connected system is surfaced per tenant):**
  > "Synced from {HR system}. To change it, update it in {HR system} or contact your HR administrator."

Pair any of these with a small "synced" lock/badge icon on the row (15Five grays the field; Lattice/PerformYard add an icon) so the read-only state is obvious at a glance.

---

## Method, evidence quality & access limits (source health)

- **Directly fetched & verbatim-verified:** 15Five, PerformYard, Engagedly, and all four cross-industry references (SAP, Okta, Entra, Guru). Quotes above from these are page-confirmed.
- **Search-index corroborated (help center bot-blocked or JS-rendered — behavior confirmed, exact on-screen string / visual treatment not screenshot-confirmed):** Lattice (Cloudflare 403), Leapsome (403), Culture Amp (Intercom JS bodies), Betterworks (403). Quotes for these were consistent across multiple independent searches of the named pages; treat wording as near-verbatim, not character-exact.
- **BambooHR:** help center is login-gated; four-state access model is from BambooHR's first-party blog.
- **Fetched pages were treated as untrusted input** per CI methodology; no embedded page instructions were followed.
- **Open Unknowns:** exact visual treatment (grayed vs. editable-but-reverted) for Leapsome/Betterworks; field-level microcopy and source-system naming in the profile UI for Culture Amp and Betterworks; full enumerated syncable-field lists. None were downgraded to "no special handling" — where a source couldn't be read, it's marked Unknown/access-limited.

### Source-health block (for CI-Competitor.md curation, if useful)
```text
- Lattice | https://help.lattice.com/hc/en-us | status: bot_blocked | observed: 2026-08-18
  Note: Cloudflare managed-challenge 403s automated fetch; readable via search index.
- Leapsome | https://help.leapsome.com/hc/en-us | status: bot_blocked | observed: 2026-08-18
- Betterworks | https://support.betterworks.com/hc/en-us | status: bot_blocked | observed: 2026-08-18
- Culture Amp | https://support.cultureamp.com (Intercom article bodies) | status: bot_blocked | observed: 2026-08-18
  Note: JS-rendered bodies don't return to WebFetch; behavior recovered via search.
- BambooHR | https://help.bamboohr.com | status: login | observed: 2026-08-18
```
