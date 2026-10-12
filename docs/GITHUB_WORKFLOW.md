# GitHub collaboration workflow

**Local handoff, 12 October 2026.** The user will upload separately. This guide specifies the intended remote workflow; no remote branch, issue, repository setting or assignment is created by preparing these files.

## 1. Repository setup and first issues

Use this folder as the repository root. Upload English documentation, exact search strings, metadata/manifests, blank templates, code and approved shareable outputs. The local `data/` snapshot and independently populated reviewer packets are excluded from Git. Record the controlled input location and approved version in each handoff.

The PI/maintainer names actual people and GitHub handles in [assignments.csv](../tracking/assignments.csv), then creates issues using the [research-task template](../.github/ISSUE_TEMPLATE/research_task.md). The [task board](../tracking/tasks.csv) provides execution roles, one accountable role, stage, dependencies, proposed branch, reviewer and merge gate.

Suggested labels: `shared-search`, `shared-data`, `shared-screening`, `RQ1`, `RQ2`, `RQ3`, `RQ4`, `needs-adjudication`, `blocked`, `ready-for-review`. Put the task ID and stage/RQ in each issue title, for example `T22 | S6/RQ1 | Exposure taxonomy`. RQ3a/RQ3b are coding subdomains under the RQ3 label. G12/G3/G4 remain coordination bundles, not the current accountable role names.

Open issues in this order:

1. T11: assign PI, SEARCH, DATA, distinct independent REV1/REV2, ADJ and four RQ leads; confirm funding/hours.
2. T02-T09/T26: search provenance/export completeness, DOI conflicts, sentinel linkage, staged abstract recovery and independent PRESS.
3. T10/T12: sign scope/period/criteria/reliability/AI rules and register the protocol/amendments.
4. T13-T16: training and two random 25-record rounds, full queue dual screening, separate full-text calibration, full-text review and study linkage.
5. T17-T21/T28/T33: independent coding/verification, pre-consensus reliability, scientific adjudication and common agreed-evidence freeze.
6. T22/T30/T23/T24: four RQ analyses on the common approved freeze. Leads may prepare methods/issues before evidence is available.
7. T29/T31/T25/T32: measurement framework, integration, reporting/claim checks and release review.

T00/T01/T27 record completed metadata preparation only. All scientific stage gates and named assignments remain pending until documented.

## 2. Branches and where to merge

The [stage/branch guide](RESEARCH_STAGES_AND_BRANCHES.md) provides the full method gates. The editable [branch plan](../tracking/branch_plan.csv) records writable scope and cross-review.

| Proposed branch | Owner | PR destination |
|---|---|---|
| `shared/protocol-search` | SEARCH; PI approves | `main` |
| `shared/data-qa` | DATA | `main` |
| `shared/screening-methods` | ADJ | `main` |
| `analysis/rq1-exposure` | RQ1_LEAD | `integration/evidence-map` |
| `analysis/rq2-measurement` | RQ2_LEAD | `integration/evidence-map` |
| `analysis/rq3-pathways-outcomes` | RQ3_LEAD | `integration/evidence-map` |
| `analysis/rq4-controls` | RQ4_LEAD | `integration/evidence-map` |
| `integration/evidence-map` | PI | `main` |

Each RQ writes to its own `analysis/rqN/` directory. Only DATA/ADJ release canonical scientific-input changes through a new approved freeze; RQ branches read those inputs. `shared/screening-methods` carries SOP/templates/code and approved summaries, while independently populated reviewer decisions remain in separate controlled storage.

Create shared preparation branches first. After shared method PRs and S5, create the integration and RQ branches from the same reviewed `main` baseline. Record the agreed-analysis freeze, commit and hashes. Example commands for the uploader/team, after remote setup:

```bash
git switch main
git pull --ff-only
git switch -c integration/evidence-map
```

Create your RQ branch from that same recorded `main` commit in your own checkout, for example:

```bash
git switch main
git switch -c analysis/rq1-exposure
```

For a smaller task, create `task/T##-description` from its responsible shared/RQ branch and target a PR back to that parent. Always inspect the parent/base before editing. Branch existence or successful technical merge does not establish scientific completion.

## 3. PR review and integration sequence

Use the [PR template](../.github/pull_request_template.md) and completed [RQ handoff template](../analysis/HANDOFF_TEMPLATE.md). State changes, task IDs, source evidence, protocol/codebook version, input freeze/hashes, denominator, verification, missingness and amendment impact.

- SEARCH/PI review scope, criteria and search changes; attach independent PRESS evidence for final/update strategy.
- ADJ reviews unresolved scientific decisions. DATA reviews stable IDs, schema, source hashes, report-study links and numerical joins.
- RQ1 and RQ2 leads cross-review; RQ3 and RQ4 leads cross-review. If roles share the same person, PI appoints a different human reviewer for that PR.
- Merge accepted RQ1/RQ2 products into the integration branch, verify the exposure-measure join, then merge accepted RQ3/RQ4 products. Work may proceed in parallel.
- All four accepted products must use the same approved evidence freeze. DATA checks unique-study denominators and overlap; PI/all leads review the combined interpretation and framework.
- Open the final integration PR to `main` after T31 and reporting checks. Record the final reviewers/acceptance and user-controlled release.

If scope/codes change, document the scientific decision/amendment, release a new common freeze, synchronize branches and rerun affected outputs. Resolve conflicting evidence rows by their IDs and approved scientific decisions. Do not choose `ours` or `theirs` as a substitute for adjudication.

The maintainer should require this review process for changes to `main` and the integration branch using the repository's available settings. Settings are not configured by this local package. A responsible lead closes a task only when its acceptance criterion and actual evidence path are satisfied, then updates [weekly_progress.csv](../tracking/weekly_progress.csv).

## 4. Operational definitions

`record` = retrieval/screening unit; `report` = full-text document; `study` = underlying investigation. `RQ hint` = preliminary routing; `RQ code` = agreed scientific classification. `Export present` means a file exists. A documented search also needs verified execution details or an explicit unresolved-data statement. An agreed-analysis freeze is different from the provisional bibliographic snapshot.

All reviewers screen the same full approved queue. RQ expertise and branch ownership divide analysis responsibility; they do not remove no-hint or missing-abstract records from independent eligibility assessment.
