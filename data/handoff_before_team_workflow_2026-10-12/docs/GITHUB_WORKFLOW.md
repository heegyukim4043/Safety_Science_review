# GitHub collaboration workflow

## Repository setup

Use this folder as the repository root or copy its contents into an approved Paper 1 repository. The PI/repository maintainer selects repository visibility and collaborators. Keep the original database exports and independently populated reviewer files outside a public repository. Record the controlled data location and frozen packet version in the relevant issue.

Recommended labels: `shared-search`, `shared-screening`, `G12`, `G3`, `G4`, `needs-adjudication`, `blocked`, `ready-for-review`. G3 owns integrated RQ3 and G4 owns controls RQ4. Use [`../tracking/rq_crosswalk.csv`](../tracking/rq_crosswalk.csv) for legacy source labels. Use task IDs from [`../tracking/tasks.csv`](../tracking/tasks.csv) in issue titles, for example `T17 | G12 | Extract function-to-work-condition evidence`.

## First issues to open

1. **T10–T12 | Lock protocol and roles.** Assign PI, search lead, two independent reviewers, adjudicator, and three workstream leads. Attach protocol version and registration link when available.
2. **T02–T06 | Reconstruct search provenance.** Split into issues by platform if several people can verify histories. Close only with exact query, date/time, on-screen hits or explicit unresolved reason, exported file count, and amendment decision.
3. **T07–T09 | Resolve data exceptions.** Track the five DOI conflicts, nine unmatched priority references, and missing-abstract queue without automatic inclusion/exclusion.
4. **T13–T16 | Calibrate, screen, full text, link studies.** Preserve two random 25-record rounds, source reliability targets and separate full-text calibration. Do not post reviewers' in-progress decisions in a shared issue.
5. **T17–T24 | RQ extraction and synthesis.** Assign G12, G3, and G4; preserve descriptive verification/core double coding and distinct RQ3a/RQ3b fields. Attach study IDs, locators, denominators, and table version.
6. **T25 | Reporting QA.** Check adjacent reviews, PRISMA record/report/study denominators, and every novelty/effect claim against full text.
7. **T26–T29 | Source-method alignment.** Track PRESS, random calibration preparation, pre-consensus reliability and the measurement framework. The [source-plan comparison](SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md) documents the restored specifications and remaining approvals.

## Change process

- Work on a branch named `task/T##-short-description`. Put the task ID in the pull request title.
- A pull request describes **what changed**, the source or record IDs affected, the test/check performed, and whether the protocol or search log needs an amendment.
- Changes to eligibility, search scope, extraction definitions, or evidence interpretation require PI/adjudicator review. A workstream lead reviews its RQ table; the data steward reviews ID/count changes.
- Do not replace a previous search export or reviewer judgment in place. Keep dated/versioned inputs and a crosswalk. Mark a task complete only when the acceptance criterion and evidence path in the task board are satisfied.
- Update [`../tracking/weekly_progress.csv`](../tracking/weekly_progress.csv) every week. Report provisional and final counts separately.

## Working definitions for issue reports

`record` = search/screening unit; `report` = full-text document; `study` = underlying investigation. `RQ hint` = automated preliminary routing label; `RQ code` = human-agreed evidence classification. `Search exported` = a file exists; `search fully documented` additionally requires a verified execution time, platform/collection, exact query, limits, on-screen hits or an explicit missing-data note, and export details.
