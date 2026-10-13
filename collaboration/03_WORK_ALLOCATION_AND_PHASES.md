# 3. Division of work, phases and approvals

**Execution design v0.5 | All named assignments and scientific gates pending.**

## A. Proposed division of responsibility

| Role | Responsibility | Handoff and review |
|---|---|---|
| PI | Scope/protocol, staffing/funding, amendments, gate acceptance and integrated interpretation | Approved versions, registration and checkpoint decisions |
| SEARCH | Exact queries, coverage, dates/limits/counts, PRESS coordination and updates | Verified histories, reviewed strategy and coverage limitations to PI/DATA |
| DATA | Provenance, duplicate candidates, IDs/linkage, separate packets, prespecified statistics and reproducible freezes | Versioned datasets, hashes, denominator/source checks |
| ADJ | Training/calibration, unresolved eligibility/core codes and codebook governance | Reasoned consensus, SOP and affected-code corrections |
| REV1 / REV2 | Independent screening of the same complete queue and independent core coding; descriptive extraction/verification | Separate original judgments and source-located evidence; funding/training required |
| RQ1_LEAD | Exposure taxonomy and function-to-condition analysis | Cross-review by RQ2_LEAD and DATA |
| RQ2_LEAD | Measurement analysis and measurement-framework coordination | Cross-review by RQ1_LEAD and DATA |
| RQ3_LEAD | Integrated pathway/worker OSH analysis | Cross-review by RQ4_LEAD and DATA |
| RQ4_LEAD | Human control evaluation and separate proposals | Cross-review by RQ3_LEAD and DATA |

SEARCH also needs an independent qualified PRESS reviewer. Confirm actual names, weekly hours, availability, funding and different human reviewers for PRs in [assignments](../tracking/assignments.csv), [RQ assignments](../tracking/rq_assignments.csv) and [tasks](../tracking/tasks.csv). Compatible roles can be combined after capacity and review independence are checked; 26 planned branches do not imply 26 staff.

## B. Shared phases before scientific RQ analysis

| Phase | Intermediate goal and output | End gate / accountable acceptance |
|---|---|---|
| **P1** | Signed scope/search/protocol; reconciled queue; roles; PRESS evidence; OSF registration | **G1:** PI accepts plan, evidence and disclosed remaining limits |
| **P2** | Reviewer training and independent calibration with accepted SOP | **G2:** ADJ accepts pre-consensus statistics and substantive-error resolution |
| **P3** | Complete independent title/abstract screening and consensus | **G3:** ADJ accepts complete queue accounting and decisions |
| **P4** | Full-text eligibility, retrieval reasons and report/study linkage | **G4:** ADJ accepts eligible-study registry and reasons |
| **P5** | Independent core coding, descriptive verification, reliability and agreed evidence freeze | **G5:** PI with ADJ/DATA accepts common registry/codebook/evidence versions |

RQ leads may prepare definitions, planned outputs and coverage suggestions during these shared phases. Scientific analysis of included evidence starts after G5. The [phase playbook](../docs/PHASE_EXECUTION_PLAYBOOK.md) gives detailed actions and field/reliability gates.

## C. Two RQ rounds with shared evaluation

`main G5 -> four RQ round-1 branches (P6A) -> midpoint review/main G6A -> four fresh RQ round-2 branches (P6B) -> second review/main G6 -> P7 integration/G7 -> P8 reporting/G8`

| Step | Work and required intermediate result | Acceptance |
|---|---|---|
| **P6A: RQ round 1** | Each lead delivers source-linked inventory, classification, descriptive matrix and missingness/handoff | Four products reviewed against the same approved G5 input |
| **Midpoint G6A** | Cross-review all four products; distinguish blocking issues from transparent evidence gaps; sign actions and round-2 plan | PI records accepted main commit and common input; no unresolved blocking action |
| **P6B: RQ round 2** | Resolve actions; make compatible design/context/measurement comparisons, linked maps, evidence limitations and final claims | Fresh branches start from G6A; each lead delivers verified final product |
| **Second evaluation G6** | Cross-review all four final products and action resolution | PI accepts final common input/outputs; all four must pass before P7 |
| **P7: integration** | Integrate evidence map, measurement framework and manuscript using final RQ outputs | **G7:** PI accepts source-linked integration and verified denominators/claims |
| **P8: reporting/release** | PRISMA-ScR/S checklists, methods/registration/deviation records, reproducible tables/figures and source audit | **G8:** PI approves final release package |

All PRs target `main`. Partial PR merges do not establish phase approval. Record actual gate commit, input hash, evidence, approving person and date. Eligibility/code/search corrections return to shared owners and approved amendments; affected analyses use a new common freeze and are rerun as necessary.

## D. Keyword and product ownership

| Lead | Relevant terms / coverage prompts | Round-1 -> round-2 product |
|---|---|---|
| RQ1 | task allocation/assignment, work pacing, algorithmic scheduling; monitoring, reassignment, authority | Exposure inventory/classification -> source-supported taxonomy and comparisons |
| RQ2 | exposure, measur*, questionnaire, scale, log*, sensor*; validation, time window, dose | Measurement inventory -> measurement/validation gaps and framework inputs |
| RQ3 | stress, fatigue, workload, ergonom*, psychosocial risk, injur*, accident*, burnout, musculoskeletal; pathways | Pathway/outcome/design inventory -> linked empirical-support/gap synthesis |
| RQ4 | intervention*, redesign, participat*, transparency, contestab*, mitigation; overrides, pace caps | Human-control evaluation inventory -> comparator/outcome synthesis and separate proposals |

Expanded prompts are proposed coverage/coding terms, not automatically completed searches. [RQ assignments](../tracking/rq_assignments.csv) distinguish executed-query terms from proposed additions. SEARCH owns approved platform translations and execution records.

## E. Automation, capacity and confirmations

Automate inventories/hashes, metadata normalization candidates, missing-field checks, packet separation, prespecified statistics and approved-code summaries. Human review decides eligibility, ambiguous linkage/core codes, search quality, causal/measurement/control interpretation and gate approval. Analysis-specific scripts require signed schemas and actual agreed data.

Dates are conditional on workload and capacity. Estimate screening/full-text/coding throughput after calibration, then revise task targets; do not promise a fixed completion date from candidate counts. Reviewer files remain separate until original decisions are locked.

| ID | Confirm or revise | Canonical follow-up |
|---|---|---|
| CR09 | Named shared/RQ roles, hours, availability, funding and independence | Assignment tables and task assignees |
| CR10 | Shared screening/coding versus RQ analysis responsibilities, cross-review and file access | SOP, reviewer packets and RQ handoffs |
| CR11 | P1-P8 sequence, P6A/G6A/P6B/G6, branch baselines, merge and failed-gate rules | Phase/branch/checkpoint tables and review-action records |
| CR12 | Capacity-based schedule, automation boundary and data/GitHub distribution arrangements | Revised task dates, AI/tool record and actual access plan |

Use [32 RQ work items](../tracking/rq_round_workplan.csv), [26-branch table](../tracking/branch_plan.csv), [40-task board](../tracking/tasks.csv), [round checkpoints](../tracking/rq_round_checkpoints.csv) and the [workflow diagram](../diagrams/paper1_rq_rounds_workflow.visual-check.1440x900.light.png) during allocation.
