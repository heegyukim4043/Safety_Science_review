# Data handoff and reviewer packet control

The English Git package contains coordination documents and blank templates. The original dataset remains in the parent workspace; a verified local copy is in `data/survey_2026-10-12/` and is **ignored by Git**. The user will decide upload separately. Do not describe either copy as publicly deposited or as an included-study dataset.

## Local source map

| Local path relative to this package | What it contains | Current status |
|---|---|---|
| `data/survey_2026-10-12/processed/source_file_manifest.csv` | Source-file names, hashes, and counts | 56 raw exports; preserve untouched |
| `data/survey_2026-10-12/processed/master_records.csv` | Normalized, provisionally deduplicated records | 6,822 provisional unique records |
| `data/survey_2026-10-12/processed/source_hits.csv` | Record-to-database/search provenance | Processing output; not screening decisions |
| `data/survey_2026-10-12/processed/screening_queue_2015_2026.csv` | Complete title/abstract screening queue | 6,592 records; provisional version |
| `data/survey_2026-10-12/processed/reviewer_packets/manifest.json` | Source hash and packet row count | 6,592 rows per reviewer |
| `data/survey_2026-10-12/processed/reviewer_packets/reviewer_1.csv` | Reviewer 1 independent decision file | Empty decision fields; distribute only to Reviewer 1 |
| `data/survey_2026-10-12/processed/reviewer_packets/reviewer_2.csv` | Reviewer 2 independent decision file | Empty decision fields; distribute only to Reviewer 2 |
| `data/survey_2026-10-12/organized/generated/abstract_retrieval_queue.csv` | Missing-abstract work queue | 3,034 records; prioritization is not exclusion |
| `data/survey_2026-10-12/organized/manual/doi_conflict_adjudication.csv` | Manual duplicate-conflict form | Five title/DOI conflict groups pending |
| `data/survey_2026-10-12/organized/generated/priority_43_linkage.csv` | Previous 43-paper seed linkage | 34 DOI-linked; nine need manual matching |

The exact-query snapshot in [`../tracking/search_log.csv`](../tracking/search_log.csv) comes from the original search-plan CSV. Its `export_file` paths are rebased to the local snapshot. Current `rq` metadata use `four_rq_v0.2`, while the original five-question mapping is preserved in `legacy_rq`; **query strings and execution statuses are unchanged**. Execution metadata are incomplete; do not infer dates/counts from modification times or file rows.

The frozen `organized/generated/RQ*_candidates_not_screened.csv` files retain their five legacy labels. Current RQ3 is the union of legacy RQ3/RQ4 by `record_id` (2,958 candidates; 2,325 abstracts), while legacy RQ5 maps to current RQ4. Use [`../tracking/rq_crosswalk.csv`](../tracking/rq_crosswalk.csv) and [`../tracking/rq_candidate_readiness.csv`](../tracking/rq_candidate_readiness.csv); do not rename or edit snapshot files. The mixed 93-record training pool and random 25+25 calibration manifests have separate purposes and contain no decisions.

See [`LOCAL_SURVEY_BUNDLE.md`](LOCAL_SURVEY_BUNDLE.md) for the 90-file copied snapshot and its SHA-256 manifest. The snapshot is read-only; reviewer work goes into separately controlled copies.

## Before giving reviewers data

Record metadata and later agreed-analysis freezes separately in [data_freezes.csv](../tracking/data_freezes.csv). The existing 6,592-record queue is a **provisional bibliographic snapshot**. The four RQ analysis branches require the later approved study/evidence/reliability freeze, released by DATA after T33; no agreed scientific freeze exists yet. RQ leads do not edit canonical consensus inputs from their branches.

1. PI and search lead lock the protocol and identify whether additional search records will be added. If the queue changes, issue a **new packet version**; preserve the old version and an ID crosswalk.
2. Data steward verifies that both reviewer files contain exactly the same `record_id` sequence, each has 6,592 unique IDs, and their source metadata match. Verify that `decision`, `exclusion_reason`, and `note` are blank at delivery.
3. Record the source queue's SHA-256, packet version, delivery date, and assigned reviewer in a local delivery log. The current manifest records source SHA-256 `213be83f0f65c0c49ab4551c5e16bca16d729ef7c5145970ca5ca2c85941123e`; recompute it if the source changes.
4. Deliver Reviewer 1 and Reviewer 2 files separately. Restrict visibility of in-progress decisions until both are locked. Keep adjudication and consensus in separate files; never overwrite either original.
5. Run automated checks on allowable codes, duplicate IDs, excluded rows without reason, and unexplained source-field changes. These checks are administrative; humans decide eligibility.

For extraction, use the updated four-RQ templates outside the frozen snapshot. Core fields are independently double-coded and descriptive fields are extracted once/source-verified by the second reviewer. Mark `rq_version`, current `rq` and `rq_subdomain`; retain `legacy_rq` only when importing older labels. RQ3a/RQ3b are subdomains of current RQ3. Store pre-consensus reliability inputs separately and avoid treating repeated effects as independent units.

Reproduce the current administrative outputs from this repository; use an unused output path for calibration so a previously used manifest is preserved:

```powershell
py -3.9 scripts/build_rq_readiness.py
py -3.9 scripts/build_calibration_manifest.py --exclude-manifest tracking/pilot_record_ids.csv --output data/calibration_rebuild.csv
```

These commands require the local frozen data. They summarize routing hints and draw IDs; they do not perform screening. Do not overwrite a used calibration manifest: pass a new output, fresh seed/round numbers, and a manifest of previously used IDs for later rounds.

## What belongs in GitHub

The coordination package, exact search strings, blank templates, and task status are in Git. The local `data/` survey copy is **not**. If it is later uploaded, choose access controls and keep Reviewer 1 and Reviewer 2 from inspecting each other's in-progress decisions. Otherwise use separately controlled storage and link to its versioned manifest from the GitHub task board.

The parent workspace is not a Git repository; `paper1_review_handoff/` is an independent local Git repository. No remote or GitHub upload has been configured. The user will handle that step separately.
