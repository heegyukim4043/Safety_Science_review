# RQ1 starter kit: exposure characteristics

**Status:** planning only; no included-study results. **Owner:** RQ1_LEAD. **Branch:** `analysis/rq1-exposure`. **Task:** T22; independent coding specification: T17. **Review:** RQ2_LEAD and DATA, with a different reviewer if both leads are the same person.

## Question and scope

Which algorithmic functions and worker-facing work characteristics have been studied as occupational exposures, and how are the exposure dimensions defined?

Own the function-to-experienced-exposure taxonomy. RQ2 owns measurement properties; RQ3 owns pathways/outcomes; RQ4 owns control evaluations. Record allocation/reallocation, scheduling/pacing, monitoring/evaluation/reward/penalty and control/authority dimensions only where source evidence supports them.

## Inputs and keywords

Use the approved study registry and agreed evidence-link table after S5. Relevant fields include `study_id`, `report_id`, `algorithmic_function`, `exposure_construct`, `exposure_unit`, `algorithmic_authority`, `exposure_reversibility`, `exposure_predictability`, `adaptation_frequency` and source locator. Preserve context and time-window links.

Existing-query terms: task allocation; task assignment; work pacing; algorithmic scheduling. Additional coverage prompts: monitoring; reassignment frequency; advance notice; authority. Prompt terms are not new executed searches. Check common AM/HRC search IDs and I2_ALLOC through [rq_assignments.csv](../../tracking/rq_assignments.csv).

## Deliverables and checks

- `exposure_taxonomy.csv`: source-supported construct, definition, function, worker-facing condition, unit, context and evidence IDs.
- `function_exposure_matrix.csv`: unique-study counts with explicit context/construct denominators and overlap.
- `results.md`: taxonomy synthesis, definition gaps and source-located examples; separate empirical findings from new proposed definitions.
- `handoff.md`: completed [handoff template](../HANDOFF_TEMPLATE.md), input freeze, commands, checks and cross-review.

Use your own directory for output files and scripts. Do not edit canonical agreed coding from this branch. Confirm every eligible study's exposure versus mere system functionality; source absence is coded missing, never inferred. During P6, submit accepted products to main after common-freeze and denominator checks. The current two-round route uses G6A for midpoint acceptance and G6 for second evaluation; P7 starts after accepted final round-2 outputs.

## Current two-round work

**Round 1:** T22, [round-1 kit](round1/README.md), source-linked inventory/descriptive evidence mapping; PR to main and midpoint G6A. **Round 2:** T35, [round-2 kit](round2/README.md), fresh `analysis/rq1-exposure-r2` branch from G6A, action resolution/linked synthesis/final verified claims; PR to main and second evaluation G6.

[Detailed phase playbook](../../docs/PHASE_EXECUTION_PLAYBOOK.md) and [work items](../../tracking/rq_round_workplan.csv) govern the current outputs. Templates in the parent kit describe content; store round-specific products in the corresponding subdirectory. Canonical codes remain controlled.
