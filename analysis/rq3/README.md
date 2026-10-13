# RQ3 starter kit: pathways and worker OSH evidence

**Status:** planning only; no included-study results. **Owner:** RQ3_LEAD. **Branch:** `analysis/rq3-pathways-outcomes`. **Task:** T23; independent coding specifications: T19 and T20. **Review:** RQ4_LEAD and DATA.

## Question and scope

Through which proposed or tested cognitive, psychosocial, ergonomic, physical-safety, or organizational pathways are exposures linked to worker OSH outcomes, with what empirical support, limitations, and evidence gaps?

Retain two linked subdomains in this one RQ: **RQ3a pathways** and **RQ3b outcomes/empirical support**. A study with outcome evidence may lack a measured mediator; retain outcome evidence and code that pathway gap. A measured association is not automatically causal or a mediation test.

## Inputs and keywords

Use approved study/report/exposure links after S5. Fields include proposed/measured mechanisms, mechanism-test level, OSH outcome/role/measure/window, comparison, effect estimate/CI, analysis unit, temporal order, dose-response test, confounding/bias, causal-support level, gap type and source locator.

Existing-query terms: stress; fatigue; workload; ergonom*; psychosocial risk; health; safety; injur*; accident*; burnout; musculoskeletal. Proposed coverage prompts: autonomy; time pressure; goal conflict; cognitive load; near miss; sleep; organizational pathway; dose response. No dedicated pathway-query export exists. P2_OSH/S2_OSH/W2_OSH and relevant AM/HRC records support retrieval; exact queries remain in [search_log.csv](../../tracking/search_log.csv).

## Deliverables and checks

- `pathway_outcome_map.csv`: linked exposure, proposed/measured/tested pathway, outcome and window, design/support, study/report/evidence IDs.
- `support_and_gaps.csv`: temporal/design/confounding/measurement limitations, estimate details and missing mediation/dose-response evidence.
- `results.md`: synthesis separated by context, pathway and actual endpoint role; distinguish worker states, behavior/near-miss proxies and injury/illness.
- `handoff.md`: common freeze, source locations, unique-study versus estimate denominators and cross-review using the [template](../HANDOFF_TEMPLATE.md).

Keep repeated measures/effects within their study. Do not sum pathway/outcome rows into unique-study counts. RQ3 inputs to RQ4 describe outcome support; prevention-effectiveness requires actual control evaluation. Any code change returns to ADJ/DATA before rerunning analysis.

## Current two-round work

**Round 1:** T23, [round-1 kit](round1/README.md), source-linked inventory/descriptive evidence mapping; PR to main and midpoint G6A. **Round 2:** T37, [round-2 kit](round2/README.md), fresh `analysis/rq3-pathways-outcomes-r2` branch from G6A, action resolution/linked synthesis/final verified claims; PR to main and second evaluation G6.

[Detailed phase playbook](../../docs/PHASE_EXECUTION_PLAYBOOK.md) and [work items](../../tracking/rq_round_workplan.csv) govern the current outputs. Templates in the parent kit describe content; store round-specific products in the corresponding subdirectory. Canonical codes remain controlled.
