# Team assignments, ownership, and handoff requirements

**Assignment design: 12 October 2026; four RQs.** This is a role-based allocation ready for actual names and GitHub handles. No named person has accepted an assignment in the supplied records. Fill [assignments.csv](../tracking/assignments.csv), set the task assignee, and confirm reviewer funding/hours before starting dependent work.

## 1. Shared method and data responsibilities

| Role | Owns | Immediate action | Handoff / review |
|---|---|---|---|
| **PI** | Research scope/RQs, signed protocol, team/funding, integrated interpretation, final release | Sign pending decisions; assign all leads and independent reviewers; confirm registration plan | Approved versions and registration reference; review every protocol/interpretation change |
| **SEARCH** | All database syntax, coverage, actual dates/limits/counts, PRESS process, search amendments | Reconstruct 25 exported search histories; resolve gaps/caps and unexported HRC decision | Exact-query log + PRESS comments/responses + coverage limitations to PI/DATA |
| **DATA** | Immutable exports, provisional duplicate candidates, stable IDs, metadata recovery, packet versions, statistics computation, analysis freeze | Resolve provenance with SEARCH/ADJ; prepare separate reviewer packets; audit hashes | Versioned inputs, ID crosswalk, missingness, freeze manifest and validated count tables |
| **REV1** | First independent screening/coding of the same complete queue and all core fields | Training/competency/calibration, then own reviewer file | Original independent decisions and source-located coding to controlled adjudication |
| **REV2** | Second independent screening/coding of the same complete queue and all core fields; descriptive source verification | Same input/version as REV1, separate file without the other's decisions | Independent originals and verification evidence to controlled adjudication |
| **ADJ** | Calibration/disagreement review, unresolved eligibility/core codes, source-defined adjudication | Confirm Nam/Staley or an approved additional adjudication role; freeze codebook with PI | Reasoned consensus decisions and affected-field recoding decisions; DATA preserves originals |

Reviewers are trained paid non-authors as specified by the source plan, with no hypothesis/framework-development or final interpretation role. Independent decisions are preserved before discussion. The scientific task allocation cannot be replaced by dividing the screening queue into RQ keywords.

## 2. Four separate RQ responsibilities

| Role / branch | Owns after agreed extraction | Required work | Primary outputs and task IDs | Cross-review |
|---|---|---|---|---|
| **RQ1_LEAD** / `analysis/rq1-exposure` | Algorithmic function, changed work condition, exposure construct and definition taxonomy | Verify function versus experienced exposure; map units/contexts; audit taxonomy coverage and source locations | `analysis/rq1/`: taxonomy, function-exposure table, narrative; **T22**; coverage/coding specification for T17 | RQ2_LEAD; DATA checks IDs/counts |
| **RQ2_LEAD** / `analysis/rq2-measurement` | How exposure was operationalized/measured; instrument/log/manipulation properties | Extract from agreed codes the unit, dose/intensity/frequency/variability/time, reversibility/control and validation gaps | `analysis/rq2/`: measurement matrix/narrative; **T30**; coverage/specification for T18; measurement framework coordination **T29** | RQ1_LEAD; DATA checks denominators |
| **RQ3_LEAD** / `analysis/rq3-pathways-outcomes` | Integrated pathways and worker OSH support, retaining RQ3a/RQ3b | Link exposure-pathway-outcome; separate proposed/measured/tested mediators; preserve design, temporal order, estimates/confounding/gaps | `analysis/rq3/`: linked map, support/gap tables, narrative; **T23**; specification for T19/T20 | RQ4_LEAD; DATA checks links |
| **RQ4_LEAD** / `analysis/rq4-controls` | Human empirical control evaluation and separate future candidates | Identify control/comparator/evaluation level/fidelity; distinguish worker response from injury prevention; assess feasible follow-on variables | `analysis/rq4/`: control matrix, separate candidate table, narrative; **T24**; specification for T21 | RQ3_LEAD; DATA checks sources |

One person may hold RQ1_LEAD and RQ2_LEAD if capacity permits, corresponding to the former G12 bundle. G3/G4 remain bundle labels for current RQ3/RQ4 in legacy coordination tables. **Current deliverables, accountable roles and analysis branches are per RQ.** RQ3a/RQ3b may have separate contributors, with one RQ3 lead accountable for their join. Assign a different human reviewer for any PR whose proposed author and cross-reviewer are the same person; PI names that substitute. REV1 and REV2 must remain distinct independent coders.

Keyword expertise supports search coverage and analysis. Search changes still belong to SEARCH and PI; scientific eligibility/core codes still belong to the independent reviewers and ADJ. All four RQ leads use the same approved corpus; a study can be analyzed under more than one RQ.

Use [rq_assignments.csv](../tracking/rq_assignments.csv) for separate existing-query keywords, proposed expansion terms, input fields, owner, branch, outputs and review role. Detailed kits are in [RQ1](../analysis/rq1/README.md), [RQ2](../analysis/rq2/README.md), [RQ3](../analysis/rq3/README.md), and [RQ4](../analysis/rq4/README.md).

## 3. Delivery accountability

| Product / gate | Single accountable role | Executors / contributing roles | Scientific approval |
|---|---|---|---|
| Final search strategy and coverage statement | SEARCH | SEARCH; all RQ leads propose coverage gaps | PI; independent PRESS evidence |
| Protocol/eligibility/reliability sign-off and registration | PI | SEARCH, ADJ, DATA | PI |
| Source/queue freeze and ID crosswalk | DATA | DATA; SEARCH for retrieval; ADJ for ambiguous duplicate decisions | PI/ADJ for relevant scientific decisions |
| Screening/full-text/independent core coding completion | ADJ | REV1, REV2; DATA manages packets/statistics | ADJ with PI for rule changes |
| Each RQ's analysis and source-located narrative | Corresponding RQ lead | RQ authors; DATA checks counts | Cross-review lead; PI resolves substantive interpretation |
| Candidate measurement framework | RQ2_LEAD | RQ1/RQ3/RQ4 leads contribute; DATA joins codes | PI |
| Integrated evidence map and manuscript | PI | Four RQ leads, DATA, SEARCH | PI after recorded cross-review |

`tracking/tasks.csv` separates execution `owner_role` from a single `accountable_role`, specifies `stage_id`, proposed branch, reviewer role and merge gate, and retains acceptance criteria/dependencies. A role column is an assignment design; fill the separate assignee field with the actual person. Set actual dates/status only when evidence is produced.

## 4. Required handoffs between teams

1. **SEARCH -> PI/DATA:** exact platform input, actual date/time/timezone or unresolved reason, limits/collection, hits versus export count, file/hash, PRESS response and update decision. Preserve source strings and previous versions.
2. **DATA -> REV1/REV2:** identical approved IDs/content, separate editable decision files, codebook/protocol version, input hash, training/calibration instructions and controlled location. Each receives their own packet.
3. **REV1/REV2 -> ADJ/DATA:** locked original judgments and source-located codes. Compute pre-consensus reliability before discussion/adjudication; retain disagreements, rationale and recoding history.
4. **ADJ/DATA -> four RQ leads:** agreed study registry and evidence links, report-to-study mapping, source locators, missingness, reliability results, approved codebook/schema and common analysis freeze. No unresolved scientific code silently enters an accepted analysis.
5. **Each RQ lead -> round-1 main/G6A -> fresh round-2 main/G6 -> fresh P7 integration:** RQ table/map, source-located narrative, script/command if applicable, input freeze/hashes/base commit, denominator definitions, limitations, cross-RQ join issues and recorded PR reviews. All four round-1 inventories and T34 establish G6A; all four final round-2 products and T39 establish G6 before P7 starts. Use [HANDOFF_TEMPLATE.md](../analysis/HANDOFF_TEMPLATE.md).
6. **PI/integration -> final reporting:** accepted four-RQ products, joined framework, reconciled records/reports/studies, adjacent-review comparison, completed search/reporting checklists, approved amendments and verified claims.

## 5. First actions for 12 October

- PI: name all roles, confirm reviewer budget/hours, and review the source-plan/4RQ decisions.
- SEARCH: start T02-T06 and prepare T26; RQ leads inspect sentinel/keyword coverage and report proposed additions.
- DATA: verify the source records and begin T07-T09 with ADJ/SEARCH; preserve source files and current manifests.
- RQ leads: read their kits, propose extraction definitions/examples, and create planning issues. Analysis of eligible-study results waits for agreed extraction.
- Repository maintainer: after the user's upload, create labels/issues/branches and apply the review process in the [GitHub guide](GITHUB_WORKFLOW.md). The coordination package does not create remote branches, issues, protections or assignments.

After calibration, estimate screening time using observed throughput. At the existing planning assumption of 40 decisions/hour, 6,592 records imply about 165 hours per reviewer for title/abstract decisions alone; training, recovery, full texts, adjudication and extraction need additional time. Record available hours rather than committing to a finish date from keyword counts.

## Phase checkpoint handoff

Record phase ID, previous approved main checkpoint/commit, destination checkpoint, input version/hash and required phase reviews. Current routing follows the eight-phase guide: phase branches submit reviewed PRs to main; each next phase starts only after all required outputs and approvals establish the new checkpoint. P6 RQ products establish G6 before fresh P7 integration. Scientific decisions stay in controlled storage; a technical merge cannot approve them.

See the [phase work guide](BRANCH_WORKFLOW_GUIDE.md) and complete the checkpoint record before promotion.

## Two-round work allocation v0.5

Each lead owns four work items in P6A and four in P6B. RQ1/RQ2 and RQ3/RQ4 cross-review in both rounds; DATA verifies input/ID/count integrity. PI owns T34 and T39 checkpoint records after all four RQ reviews. P6B uses fresh -r2 branches from G6A. [Detailed phase playbook](PHASE_EXECUTION_PLAYBOOK.md), [work items](../tracking/rq_round_workplan.csv) and [action log](../tracking/rq_review_actions.csv) define owners, output files and acceptance. Named assignments remain pending.
