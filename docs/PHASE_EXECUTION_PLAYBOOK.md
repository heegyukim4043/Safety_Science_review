# Phase execution playbook: two RQ rounds and reviewed main checkpoints

**Execution design v0.5 | 12 October 2026 | Four RQs.**
This is the current proposed team workflow. Named assignments, scientific decisions, data freezes and approvals remain pending. The scientific S0-S8 stages and outer P1-P8 phases remain in place. P6 now contains **P6A (RQ round 1), midpoint G6A, P6B (RQ round 2), and second evaluation G6**. Earlier one-round P6 diagrams are historical summaries.

![Two rounds of RQ work with midpoint and second evaluation](../diagrams/paper1_rq_rounds_workflow.visual-check.1440x900.light.png)

[Interactive Archify diagram](../diagrams/paper1_rq_rounds_workflow.html) | [Branch work table](../tracking/branch_plan.csv) | [Round checkpoints](../tracking/rq_round_checkpoints.csv) | [RQ work items](../tracking/rq_round_workplan.csv)

## Five methodological layers across the phases

The [methodology-to-phase guide](METHODOLOGY_AND_PHASE_CROSSWALK.md) specifies actions, responsible roles and evidence at every gate. Track actual completion in the [five-method register](../tracking/methodology_plan.csv); use the [evidence check template](../templates/METHODS_COMPLIANCE_CHECK.md).

| Layer | Phase application | Concrete intermediate/final output |
|---|---|---|
| JBI scoping-review methodology | P1 design; P2-P5 selection/charting; P6A/P6B/P7 synthesis | Approved protocol, common eligible-study evidence freeze and accepted RQ/integrated products |
| PRISMA-ScR | Maintain reporting evidence from P1; complete P8/G8 | Item-location checklist, reconciled flow and study/result tables |
| PRISMA-S | P1 and search updates; complete P8/G8 | Exact database/platform strategies, dates, limits, counts, deduplication and reporting checklist |
| PRESS | Before final/update query execution in P1/G1; revisit material query changes | Independent comments, responses and revised strategy |
| OSF preregistration | P1/G1 before formal screening; reconcile amendments through P8 | Formal registration identifier/date, registered version, prior-work disclosure and deviation log |

PRESS and OSF are not documented as completed. Existing discovery searches must be disclosed at registration. Numeric reliability thresholds and the two RQ branch rounds are project specifications. A technical merge or package check does not establish methodological completion.

## 1. Execution order and common rules

`P1-P5 shared preparation -> approved main G5 -> four P6A RQ branches -> midpoint review and main G6A -> four fresh P6B RQ branches -> second review and main G6 -> P7 integration/main G7 -> P8 reporting/main G8`

Gates name accepted main commits. They are not automatic approval from a technical merge, a calendar date or a branch name.

| Work package | Start requirement | Branch arrangement | End requirement |
|---|---|---|---|
| Shared preparation, P1-P5 | Source package G0 and named roles | Phase-specific shared-method branches | Approved protocol, full eligible-study coding and common G5 evidence freeze |
| Analysis phase 1, P6A | Approved G5 main commit and evidence hash | Four RQ round-1 branches | Four source-linked evidence inventories and descriptive products |
| Midpoint evaluation | All round-1 products ready for cross-review | PI checkpoint PR after RQ reviews | Signed action log and accepted main G6A |
| Analysis phase 2, P6B | Approved G6A main commit and common approved input | Four fresh RQ round-2 branches | Resolved review actions and final linked analytical products |
| Second evaluation | All four round-2 products ready for cross-review | PI checkpoint PR after RQ reviews | Accepted main G6 with all final RQ outputs |
| Integration, P7 | Approved G6 | Map/manuscript and measurement-framework branches | Approved common framework and manuscript at G7 |
| Reporting/release, P8 | Approved G7 | Reporting/search and release-QA branches | Verified release package and PI approval at G8 |

All PRs target **main**. Create branches from the recorded gate commit, not an arbitrary latest main head. Individual reviewed PRs may merge while the round/phase gate remains pending. All four RQs must pass before promotion. Plan up to four active analytical branches per round; the PI gate branch follows their review.

Use one agreed study registry, codebook, evidence-link table and approved input version across the RQs. A study may contribute to several RQs; cross-RQ counts are not additive. Independent eligibility and core coding are completed through REV1/REV2 and ADJ; RQ leads analyze agreed evidence.

## 2. Shared preparation: P1-P5

This is one visual preparation group with five internal approvals. RQ leads can prepare definitions, planned tables and coverage suggestions during this group. Scientific results from included studies begin after G5.

### P1. Search, protocol, roles and source/queue QA -> G1

**Owners:** PI (approval), SEARCH (search provenance), DATA (data management), ADJ (review methods).

1. Preserve the 56 original exports and their hashes. Reproduce the 10,858 retrieval rows, 6,822 provisional unique records and 6,592 working-year queue; distinguish processing counts from final PRISMA counts.
2. Reconcile 42 planned search rows against 25 rows with exports. Recover actual search execution dates/time zones, screen hit counts, limits and export completeness, or record explicit unresolved reasons.
3. Resolve the Scopus 1,061/1,050 and 107/105 discrepancies, possible IEEE 1,000-record cap, ACM coverage, unexported Scopus HRC query and inaccessible database decisions.
4. Adjudicate conflicting DOI groups; preserve ambiguous originals. Recover abstracts with provenance and report failures; missing abstracts do not exclude records.
5. Confirm the publication window/cutoff, source types/languages, PCC/HRC boundaries, four RQs, eligibility, source-located fields, independent coding, reliability targets and AI limits. Distinguish adopted rules from unresolved proposals.
6. Obtain independent PRESS comments/responses for final/update queries; register the signed protocol or record amendments before formal screening.
7. Name PI, SEARCH, DATA, ADJ, distinct paid reviewers and four analytical leads; confirm hours, funding and different human PR reviewers.
8. Approve the planned round-1/round-2 analysis methods, missingness codes, denominators and design/context comparisons before observing analytical findings.

**Branches:** `shared/protocol-search`, `shared/data-qa`, `shared/screening-methods`.

**Outputs:** verified search/coverage log, signed protocol/decisions, approved queue version, reviewer SOP, role roster and registration reference. **Gate:** PI approval of versions and remaining limitations. Metadata preparation alone does not establish G1.

### P2. Reviewer training and calibration -> G2

**Owners:** ADJ; execution REV1/REV2; DATA supplies separate packets and statistics.

1. Train on mixed examples and check competency.
2. Use two disjoint random 25-record rounds, separate from training. Reviewers use identical inputs in separate files and do not see each other's judgments.
3. Lock original decisions, compute pre-consensus agreement, Gwet's AC1 and supplementary kappa, then inspect substantive errors.
4. Refine the rules between rounds and repeat with fresh records if required.

**Outputs:** original decisions, statistic/CI methods, error log and accepted SOP. **Project gate:** agreement >=85% and AC1 >=0.80 plus substantive-error resolution; numeric targets are project choices.

### P3. Full title/abstract review -> G3

**Owners:** ADJ; execution REV1/REV2; DATA performs coverage QA.

1. Both reviewers independently assess the entire approved queue.
2. Track batch IDs and every original judgment; discuss disagreement and adjudicate unresolved cases.
3. Confirm that no record was dropped because of a missing abstract, a ranking position or absent RQ keywords.
4. Reconcile screening/advancement and duplicate-exception counts.

**Outputs:** preserved independent decisions, agreed advancement/reasons and verified record counts. **Gate:** every queue ID accounted for with the required decisions and adjudication.

### P4. Full texts, eligibility and study linkage -> G4

**Owners:** ADJ; REV1/REV2 assess; SEARCH retrieves; DATA links reports/studies.

1. Log retrieval sources, requests, failures and access limits.
2. Calibrate separately on 10-15 full-text reports: project targets >=90% agreement and AC1 >=0.80.
3. Complete independent full-text decisions, consensus and explicit exclusion reasons.
4. Distinguish search records, full-text reports and underlying studies. Verify multiple-report and repeated-sample links manually.

**Outputs:** agreed eligible-report list, study registry/report crosswalk, exclusions and retrieval log. **Gate:** final eligibility and unique-study identity approved.

### P5. Extraction, independent coding, reliability and common freeze -> G5

**Owners:** ADJ (scientific codes), DATA (QA/statistics/package), PI (freeze approval).

1. Independently double-code 100% of core interpretive fields. Extract descriptive fields and verify 100% with the second reviewer.
2. Retain report/page/table/figure locators for exposure, measurement, pathway, outcome and control evidence.
3. Calculate prespecified reliability on locked independent codes before consensus; preserve refinement/recoding history.
4. Resolve disagreements through ADJ, verify required fields/keys/links and characterize unavailable versus unreported information.
5. Package T33: registry, evidence links, codebook/schema, reliability, approved version, hashes and limitations.

**Outputs:** approved agreed-study evidence and a read-only analytical input. **Gate:** PI/ADJ acceptance with DATA integrity checks. This is different from the provisional bibliographic snapshot.

## 3. Analysis phase 1: P6A / RQ round 1

**Purpose:** establish what agreed evidence exists under each RQ, how it is coded and counted, and where the evidence is incomplete.

**Input:** the same approved G5 commit and controlled evidence freeze for all four leads. Record the registry, codebook and evidence-table hashes. The analysis branches own scripts and shareable products; corrections to canonical scientific codes return to ADJ/DATA.

| RQ | Branch / task | Owner and reviewer | Required product |
|---|---|---|---|
| RQ1 | `analysis/rq1-exposure` / T22 | RQ1_LEAD; RQ2_LEAD + DATA | Source-linked exposure taxonomy, function-exposure inventory and descriptive matrix |
| RQ2 | `analysis/rq2-measurement` / T30 | RQ2_LEAD; RQ1_LEAD + DATA | Measurement inventory, operationalization matrix and missingness table |
| RQ3 | `analysis/rq3-pathways-outcomes` / T23 | RQ3_LEAD; RQ4_LEAD + DATA | Linked pathway/outcome/design inventory with RQ3a/RQ3b retained |
| RQ4 | `analysis/rq4-controls` / T24 | RQ4_LEAD; RQ3_LEAD + DATA | Evaluated-control inventory and separate background/proposal register |

### RQ1: function and worker-experienced exposure

1. Check each assigned agreed study's algorithmic function and worker-facing change; distinguish system operation from an experienced work condition.
2. Build source-linked definitions for allocation/reallocation, scheduling/pacing, monitoring/evaluation/reward/penalty and authority/control dimensions where supported.
3. Record event/task/shift/worker unit, work context, exposure time window and permitted multi-label links.
4. Summarize unique studies by function/exposure/context; list unreported definitions and ambiguous mappings for review.

**Files:** `analysis/rq1/round1/exposure_inventory.csv`, `exposure_taxonomy.csv`, `function_exposure_matrix.csv`, `missingness.csv`, `results.md`, `handoff.md`.

### RQ2: operationalization and measurement

1. Identify exposure measures separately from response/outcome measures.
2. Inventory self-report, logs/sensors, observation and experimental manipulation.
3. Tabulate unit, dose/intensity, frequency, duration, variability, recall/time window, reversibility and worker control.
4. Record reported reliability/validity/invariance evidence, population and missing properties; distinguish scale validation from exposure-response support.

**Files:** `analysis/rq2/round1/measurement_inventory.csv`, `operationalization_matrix.csv`, `validation_inventory.csv`, `missingness.csv`, `results.md`, `handoff.md`.

### RQ3: pathways and worker OSH evidence

1. Keep RQ3a pathway codes and RQ3b outcome/support codes linked through study/report/evidence IDs.
2. Distinguish proposed, measured and tested pathways; record a missing mediator rather than inferring one.
3. Classify OSH outcomes and proximal indicators by their source-defined role and time window.
4. Inventory design, analysis unit, temporal order, estimates/CIs, confounding controls and dose-response tests.

**Files:** `analysis/rq3/round1/pathway_outcome_inventory.csv`, `design_support_matrix.csv`, `missingness.csv`, `results.md`, `handoff.md`.

### RQ4: evaluated controls

1. Identify implemented/evaluated software and work-design controls, comparator, context and worker population.
2. Record evaluation level, implementation fidelity, follow-up and worker response/OSH measures.
3. Separate empirical human evaluation from proposals and technical-only simulations.
4. Inventory effects and CIs where reported; separate changes in proxies from demonstrated injury-prevention outcomes.

**Files:** `analysis/rq4/round1/control_inventory.csv`, `evaluation_matrix.csv`, `proposal_register.csv`, `missingness.csv`, `results.md`, `handoff.md`.

**Common acceptance:** every assigned evidence row is accounted for; IDs and source locators are valid; denominators and overlap are explicit; scripts/commands and the input hash reproduce tables; missing data are recorded honestly. Findings remain provisional until reviewed.

## 4. Midpoint evaluation and main G6A

**Task / branch:** T34 / `review/rq-round1`. **Owner:** PI. **Review:** DATA plus four RQ leads; a different person reviews their own authored product.

1. Cross-review RQ1/RQ2 and RQ3/RQ4 products against full-text locators. DATA verifies identities, row coverage, denominators and input hashes.
2. Audit compatibility of exposure IDs, measurement IDs, pathway/outcome links and control identifiers.
3. Review missingness and search coverage. A sparse evidence cell is an analytical finding to qualify; an unexplained missing assigned study or wrong scientific code is a blocking defect.
4. Record every review action in `tracking/rq_review_actions.csv`: source, severity, owner, due condition, resolution evidence and reviewer.
5. Accept a documented round-2 analysis plan: comparisons, unresolved nonblocking limitations, joins, source checks and expected outputs.

**Blocking defects:** invalid sources/IDs, mixed/unapproved inputs, omitted assigned evidence, incorrect scientific codes, inconsistent denominators, unsupported interpretation or incomplete independent-review requirements.

**Gate G6A:** all four round-1 PRs cross-reviewed and accepted, blocking actions resolved, remaining limitations explicitly approved, PI checkpoint PR accepted and approved main commit/input hash recorded. Use `tracking/rq_round_checkpoints.csv` and the checkpoint form.

**If the gate fails:** return actions to their owner; revise/review round 1. Search additions, eligibility changes or core-code corrections go through SEARCH/ADJ/DATA and PI amendment, a newly approved common freeze and affected-output reruns. Reopen impacted gates. Do not repair only one RQ's canonical input.

## 5. Analysis phase 2: P6B / RQ round 2

**Start:** create all four fresh branches from the **recorded G6A main commit**. Use the same approved evidence version across leads and accepted round-1 products. Record any formally amended common version.

| RQ | Fresh branch / task | Main analysis and required product |
|---|---|---|
| RQ1 | `analysis/rq1-exposure-r2` / T35 | Refined source-grounded exposure taxonomy; function/context patterns; linked exposure-measure framework inputs |
| RQ2 | `analysis/rq2-measurement-r2` / T36 | Measurement-property/gap assessment; unit/time/dose compatibility; framework-ready metrics and feasibility limits |
| RQ3 | `analysis/rq3-pathways-outcomes-r2` / T37 | Pathway-outcome-design synthesis; temporal/confounding/dose-response limits; source-linked evidence gaps |
| RQ4 | `analysis/rq4-controls-r2` / T38 | Control-effect/evaluation synthesis; transferability/fidelity limits; separate future experimental candidates |

### RQ1: refine definitions and linked patterns

1. Resolve midpoint actions and verify changed definitions with source locators.
2. Compare functions and worker-facing exposures by conventional employment, platform work and HRC; preserve heterogeneous settings.
3. Join approved RQ2 measurement identifiers to exposure constructs; flag inconsistent units/time windows.
4. Deliver the final taxonomy, descriptive patterns, definition boundaries and source-linked gaps.

**Outputs:** `analysis/rq1/round2/exposure_taxonomy_final.csv`, `exposure_measure_links.csv`, `context_patterns.csv`, `claims.csv`, `results.md`, `handoff.md`.

### RQ2: assess measurement evidence and framework inputs

1. Resolve midpoint measurement and missingness actions.
2. Compare operationalizations with compatible units, intensity/dose definitions and time windows; document incompatibilities rather than converting them without justification.
3. Assess reported measurement properties and applicability by instrument, population and setting. Do not treat a validated questionnaire as causal exposure-response evidence.
4. Prepare source-linked candidate metrics with feasibility, reliability/validity gaps, worker control/reversibility and priorities for later Delphi/experiments.

**Outputs:** `analysis/rq2/round2/measurement_assessment.csv`, `metric_candidates.csv`, `validation_gaps.csv`, `claims.csv`, `results.md`, `handoff.md`.

### RQ3: synthesize pathways, outcomes and empirical support

1. Resolve source/design/linking actions while keeping RQ3a/RQ3b distinct.
2. Stratify descriptive/narrative synthesis by study design, context, temporal order and outcome role using approved analysis rules.
3. Report compatible estimates and limitations: confounding, repeated observations, exposure measurement and missing mediator/temporality.
4. Distinguish proposed mechanisms, associations and stronger design-supported claims; produce an explicit evidence-gap map.

**Outputs:** `analysis/rq3/round2/pathway_outcome_support.csv`, `design_context_patterns.csv`, `evidence_gaps.csv`, `claims.csv`, `results.md`, `handoff.md`.

Do not infer an unmeasured mediator or pool incompatible effects. Meta-analysis requires a separate compatibility assessment and protocol decision. Any formal appraisal tool or certainty scheme requires prespecification; no unregistered composite evidence score is assumed.

### RQ4: synthesize control evaluation and follow-on candidates

1. Resolve midpoint classification and outcome/comparator actions.
2. Compare evaluated controls by evaluation design, implementation fidelity, population, exposure and worker outcome.
3. Describe reported effects, uncertainty and transferability; distinguish proxy improvements from demonstrated preventive outcomes.
4. Create a separate candidate register for later experiments: modifiable variable, proposed comparator, exposure unit/time window, outcome and feasibility questions, each grounded in source evidence or explicitly labeled as a new hypothesis.

**Outputs:** `analysis/rq4/round2/control_evidence_synthesis.csv`, `evaluation_limits.csv`, `future_candidate_register.csv`, `claims.csv`, `results.md`, `handoff.md`.

### Common round-2 verification

- Join compatible exposure/measurement/pathway/outcome/control identifiers and explain unmatched links.
- Use unique-study denominators; retain report/effect/analysis-unit information.
- Report missingness and heterogeneous designs/settings; do not count statistical significance votes as effect strength.
- Use prespecified subgroup/sensitivity checks when the data and methods permit; record why a planned comparison could not be done.
- Link every substantive claim to supporting evidence, source locators and interpretive limitations.
- Resolve all midpoint actions or record approved nonblocking limitations; preserve before/after files and review evidence.

## 6. Second evaluation and main G6

**Task / branch:** T39 / `review/rq-round2`. **Owner:** PI; review DATA and four leads.

1. Cross-review all four final RQ products, rerun scripts and verify source-supported claims.
2. Verify common input hashes, closed/reviewed midpoint actions, denominator consistency and cross-RQ joins.
3. Check the separation of measurement validation, pathway testing, worker OSH evidence and control effectiveness.
4. Audit the adjacent-review positioning: count Chen's 167-paper review once; include Bowdler, Matilla-Santander, Bao and the distinct Jetha review/protocol; retain other verified comparators in the comparison register.
5. Confirm the integration handoff and all remaining limitations. Novelty remains source-dependent; no completed-search claim is inferred from the current exports.

**Gate G6:** all four round-2 PRs and the second-review PR accepted, no blocking action remains, reproducible final products on an approved common input, PI acceptance and main commit recorded. G6A must already be approved. The outer P6 register is approved only when G6 and all round-1/round-2 requirements are satisfied.

## 7. Integration phase: P7 -> G7

**Owners:** PI (`integration/evidence-map`, T31), RQ2_LEAD (`phase-07/measurement-framework`, T29). **Input:** accepted G6 round-2 products.

1. Create fresh branches from G6; integrate final round-2 products and retain round-1 provenance.
2. Join exposure to measurement first, then pathways/outcomes and evaluated controls through approved study/evidence identifiers.
3. Produce a unified evidence map with study-level denominators and clearly marked sparse or unsupported links.
4. Build the measurement framework: constructs, units, dose/intensity/frequency/time, data sources, worker control, feasibility and validation priorities.
5. Draft integrated results/discussion and novelty/contribution comparisons; distinguish evidence-backed findings from future hypotheses.
6. Reconcile all figures/tables/narrative statements with source tables; review with all four RQ leads and DATA.

**Gate G7:** accepted map, framework, manuscript, verified joins/counts/claims and PI approval. T31's final integration follows the approved measurement-framework output T29.

## 8. Reporting/release phase: P8 -> G8

**Owners:** PI with SEARCH/DATA and all RQ leads.

1. Produce reconciled PRISMA-ScR flow/counts and PRISMA-S search details; disclose inaccessible databases and unresolved coverage.
2. Report prespecified reliability, recoding/amendments, independent reviewer arrangements and AI/automation assistance.
3. Verify source locators, adjacent-review comparison and every central claim.
4. Reproduce outputs, check English docs/CSV schemas/links and shareable file boundaries.
5. Obtain named final human approvals and record the accepted main release commit.

**Outputs:** manuscript, tables/figures, method/codebook/search supplements, reproducibility/release manifest and reviewed upload package. **Gate G8:** PI acceptance. The user/team handles GitHub upload and manuscript submission separately.

## 9. Automation and human decisions

| Stage | Automatable work | Human decision required |
|---|---|---|
| P1-P5 | Hashes, normalization candidates, metadata retrieval, packet separation, coverage/schema checks, prespecified statistics | Search strategy, eligibility, study linkage, core codes, reliability acceptance, approved freeze |
| P6A | Approved-code inventories, missingness and unique-study counts, source-ID checks, descriptive tables | Classification/source verification, denominator interpretation and missingness meaning |
| G6A | Action-log completeness, file/hash/ID checks, branch/work-item coverage | Review quality, blocking/nonblocking decisions and promotion |
| P6B | Joins, approved stratified summaries, reproducible figures and source-link checks | Evidence interpretation, causal/preventive limits and future hypotheses |
| G6/P7/P8 | Reproduction, consistency/link checks, approved-count reporting and package QA | Scientific claims, integrated framework and final approval |

Currently available scripts cover metadata/readiness, sampling and package integrity. Analysis-specific computations require implementation against the signed schema and approved data. Blank templates and pending checklists are not analysis results.

## 10. Work records and handoff procedure

- [40-task board](../tracking/tasks.csv): original task IDs preserved; T34-T39 add the two reviews and four round-2 tasks.
- [26-branch table](../tracking/branch_plan.csv): 20 prior branches plus four round-2 branches and two review-record branches.
- [Round checkpoints](../tracking/rq_round_checkpoints.csv): G5 -> G6A -> G6, approval evidence and accepted commits.
- [32 RQ work items](../tracking/rq_round_workplan.csv): four items per RQ per round, owner/reviewer/output/acceptance/status.
- [Review action log](../tracking/rq_review_actions.csv): blocking flags, owners, resolution evidence and review acceptance.
- [Review form](../templates/RQ_ROUND_REVIEW.md), [checkpoint form](../templates/PHASE_CHECKPOINT.md) and [analysis handoff](../analysis/HANDOFF_TEMPLATE.md).

Before each round: name people, approve the base commit/input, create task issues and fresh branches, and assign a different human reviewer. During a round: update work items and actions, submit reviewed PRs to main, preserve versions. At the gate: PI/DATA verify all required branches and evidence, record approvals and permit the next round.

Dates remain dependency/throughput dependent. Existing screening/full-text targets are provisional; the added analysis round does not imply the old March analytical dates remain feasible. Estimate reviewer/lead hours from observed workload and approved-study counts. At the current status, start with P1 decisions and role assignment; RQ planning can begin, while formal analytical rounds wait for G5.

