# RQ4 starter kit: modifiable controls

**Status:** planning only; no included-study results. **Owner:** RQ4_LEAD. **Branch:** `analysis/rq4-controls`. **Task:** T24; independent coding specification: T21. **Review:** RQ3_LEAD and DATA. This is legacy RQ5, not legacy RQ4.

## Question and scope

Which software/work-design controls have been empirically implemented or evaluated, at what evaluation level, and with what worker response or OSH outcomes?

Own the human empirical control matrix. Distinguish technical implementation, human laboratory/task evaluation and workplace evaluation. Preserve the actual comparator, implementation fidelity and measured endpoint. Proposed controls and robot-only simulations belong in a separate background/candidate table; they do not show worker OSH effectiveness.

## Inputs and keywords

Use approved registry/evidence links after S5, including control type/evaluation level/fidelity/worker outcome, comparison, outcome role/time, design, estimate/CI, exposure, worker override and source locator. Use RQ1/RQ2 definitions and measurement, and RQ3 outcome/design support.

Existing-query terms: intervention*; redesign; participat*; consultation; transparency; contestab*; mitigation; explanation; human-in-the-loop. Proposed coverage prompts: pace cap; reassignment limit; advance notice; worker override; human review; safety constraint. Relevant IDs: P6_CONTROL, S6_CONTROL, W6_CONTROL, I4_CONTROL, A2_CONTROL, and common AM/HRC retrieval. See [RQ assignments](../../tracking/rq_assignments.csv).

## Deliverables and checks

- `control_evaluation_matrix.csv`: eligible human control, exposure/comparator, implementation/fidelity, evaluation context, response/OSH endpoint, design/support and evidence IDs.
- `candidate_controls.csv`: separate proposals/technical-only examples and feasible future manipulations with clearly labeled evidence status.
- `results.md`: synthesis of evaluated controls, limits, implementation gaps and proposed later experiments.
- `handoff.md`: common freeze, distinct empirical/background denominators, sources and cross-review using the [template](../HANDOFF_TEMPLATE.md).

Verify that a reported worker response is not described as reduced injury/illness without data. Cross-sectional associations alone do not demonstrate control effectiveness. PI and all RQ leads review follow-on allocation/override, dose-response and control experiments as later proposals.

## Current two-round work

**Round 1:** T24, [round-1 kit](round1/README.md), source-linked inventory/descriptive evidence mapping; PR to main and midpoint G6A. **Round 2:** T38, [round-2 kit](round2/README.md), fresh `analysis/rq4-controls-r2` branch from G6A, action resolution/linked synthesis/final verified claims; PR to main and second evaluation G6.

[Detailed phase playbook](../../docs/PHASE_EXECUTION_PLAYBOOK.md) and [work items](../../tracking/rq_round_workplan.csv) govern the current outputs. Templates in the parent kit describe content; store round-specific products in the corresponding subdirectory. Canonical codes remain controlled.
