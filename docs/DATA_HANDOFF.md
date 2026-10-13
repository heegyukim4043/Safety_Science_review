# Data and reviewer handoff

The repository shares research methods, search provenance, source hashes, task records and blank templates. Actual source exports, abstracts, full texts and completed reviewer decisions are not included in this planning release. Agree access arrangements before dependent work; no source data are presented as deposited by this package.

## Source references and versions

- [Raw-export manifest](../tracking/raw_export_manifest.csv): 56 source filenames, databases, search IDs, row counts and original SHA-256 hashes.
- [Search log](../tracking/search_log.csv): exact strategies, execution status and outstanding dates/counts. `export_file` identifies source filenames, not files included in this repository.
- [Preparation summary](../tracking/survey_snapshot_summary.json): provisional corpus counts, not final PRISMA results.
- [Data freezes](../tracking/data_freezes.csv): actual source-queue hash/count and pending agreed-evidence freeze. `source_artifacts/` references in task/freeze records identify externally managed evidence and are not repository downloads.

DATA preserves unchanged sources, source-to-record links and version identifiers. Reconcile the supplied hash/count before delivering reviewer files. A new corpus or eligibility/codebook amendment requires a new version, ID crosswalk and affected-output review.

## Independent reviewer procedure

1. Confirm REV1/REV2 identities, funded hours, training and permitted data access.
2. Deliver identical approved input/IDs in separate working files. Each reviewer sees only their own in-progress judgments.
3. Preserve original decisions until both are locked. Compute pre-consensus reliability, then discuss disagreements and adjudicate unresolved cases.
4. Complete full-text decisions, report/study linkage, independent core coding and descriptive-field verification under the [SOP](SCREENING_AND_EXTRACTION_SOP.md).
5. Release agreed evidence to RQ leads only after G5 approval with registry/codebook/evidence versions and hashes. Never replace independent originals with consensus alone.

## Reproducible preparation tools

Scripts require explicit approved input files. Use `build_pilot_manifest.py --queue <approved-queue.csv>`, `build_calibration_manifest.py --queue <approved-queue.csv>`, and `build_rq_readiness.py --source <candidate-source-directory>`, with a new output path when appropriate. Existing manifests represent prepared IDs, not completed calibration. Do not overwrite used manifests.

These tools support preparation and routing. They do not decide eligibility or generate scientific findings. See [team assignments](TEAM_ASSIGNMENTS_AND_HANDOFFS.md) and [phase playbook](PHASE_EXECUTION_PLAYBOOK.md).
