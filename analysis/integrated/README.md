# Integrated evidence map and manuscript

**Status:** pending scientific extraction and four accepted RQ analyses. **Owner:** PI. **Branch:** `integration/evidence-map`. **Phase:** P7, starting from accepted G6 main. **Tasks:** T31 (integration); T29 uses the separate phase-07/measurement-framework branch. P8 T25/T32 reporting/release uses fresh branches after G7.

## Inputs and intended outputs

Use four accepted round-2 RQ PRs after T39/G6 with the same agreed evidence freeze and baseline, source-located handoffs, reliability results and study/report registry. Join by study, exposure, measurement, outcome/window and control rather than matching labels alone.

Planned output files in this directory:

- `integrated_evidence_map.csv`: study-level linked evidence, overlapping RQ contributions and traceable source IDs.
- `measurement_framework.csv`: approved candidate framework from the [template](../../templates/measurement_framework.csv); validated measures and proposed future metrics distinct.
- `manuscript.md`: objectives/methods/results/discussion, reporting limits and source-verified novelty comparison.
- `reporting_counts.csv`: reconciled search records, assessed reports, unique included studies and exclusion reasons.
- `handoff.md`: accepted RQ PRs, common input hashes, joins/denominators, changes and final reviews using the [template](../HANDOFF_TEMPLATE.md).

## Integration gate

DATA confirms stable IDs, hashes, missingness, row multiplicity and unique-study denominators. All four leads review construct and interpretation joins; SEARCH reviews search reporting; ADJ resolves scientific coding disputes through a new approved freeze. PI approves the final integrated interpretation and release PR to `main`. Exact staged flow is in the [branch guide](../../docs/RESEARCH_STAGES_AND_BRANCHES.md).

No final PRISMA diagram, numerical review findings or included-study table is populated in this starter package. Later Delphi/experimental designs remain separately labeled follow-on plans.

## Current two-round input

P6A inventories and G6A precede P6B final linked synthesis and G6. Integrate the accepted analysis/rq1/round2 through analysis/rq4/round2 products, with round-1 and review-action provenance retained. T29 depends on T39; final T31 depends on T39/T29 and approved reliability. [Phase playbook](../../docs/PHASE_EXECUTION_PLAYBOOK.md).
