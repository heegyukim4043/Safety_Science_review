# Integrated evidence map and manuscript

**Status:** pending scientific extraction and four accepted RQ analyses. **Owner:** PI. **Branch:** `integration/evidence-map`. **Tasks:** T29 (framework with RQ2_LEAD), T31 (integration), T25/T32 (reporting/release).

## Inputs and intended outputs

Use four accepted RQ PRs with the same agreed evidence freeze and baseline, source-located handoffs, reliability results and study/report registry. Join by study, exposure, measurement, outcome/window and control rather than matching labels alone.

Planned output files in this directory:

- `integrated_evidence_map.csv`: study-level linked evidence, overlapping RQ contributions and traceable source IDs.
- `measurement_framework.csv`: approved candidate framework from the [template](../../templates/measurement_framework.csv); validated measures and proposed future metrics distinct.
- `manuscript.md`: objectives/methods/results/discussion, reporting limits and source-verified novelty comparison.
- `reporting_counts.csv`: reconciled search records, assessed reports, unique included studies and exclusion reasons.
- `handoff.md`: accepted RQ PRs, common input hashes, joins/denominators, changes and final reviews using the [template](../HANDOFF_TEMPLATE.md).

## Integration gate

DATA confirms stable IDs, hashes, missingness, row multiplicity and unique-study denominators. All four leads review construct and interpretation joins; SEARCH reviews search reporting; ADJ resolves scientific coding disputes through a new approved freeze. PI approves the final integrated interpretation and release PR to `main`. Exact staged flow is in the [branch guide](../../docs/RESEARCH_STAGES_AND_BRANCHES.md).

No final PRISMA diagram, numerical review findings or included-study table is populated in this starter package. Later Delphi/experimental designs remain separately labeled follow-on plans.
