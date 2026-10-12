# Local survey bundle (not uploaded)

**Snapshot:** `data/survey_2026-10-12/` inside this handoff folder. It is a local copy for team handoff and is excluded from Git by `.gitignore`. The original source of truth remains in the parent workspace's survey folder. The snapshot is not a set of included studies and does not begin human screening.

| Snapshot subfolder | Contents |
|---|---|
| `Scopus/`, `Pubmed/`, `WOS/`, `IEEE EXplore/`, `ACM/` | All 56 original bibliographic exports from the five accessible databases |
| `processed/` | Source manifest, normalized master, provenance, 6,592-record queue, two **blank** independent reviewer packets, and packet manifest |
| `organized/generated/` | Search inventory, priority-paper linkage, provisional RQ candidate lists, missing-abstract queue, DOI conflict queue, and summary |
| `organized/manual/` | Blank manual adjudication and extraction forms |
| Survey root files | Existing survey audit notes, screening codebook draft, processing scripts, and requirements |

Dependency caches `.python_deps/` and `__pycache__/` were omitted. The complete file-level audit manifest is local-only at `data/local_survey_snapshot_manifest.csv`; it retains original filenames for exact reconciliation. The upload-ready [`raw-export manifest`](../tracking/raw_export_manifest.csv) uses English filenames for all 56 exports, and the [`snapshot summary`](../tracking/survey_snapshot_summary.json) gives the total files and bytes without original local-language paths. The audit compares every copied file to the original.

Treat this snapshot as read-only. Give Reviewer 1 and Reviewer 2 separate **working copies** of their respective blank packets. Neither should edit the snapshot packet in place or see the other's in-progress decisions. Keep original decisions until both are locked. If the survey changes, create a new dated snapshot and ID crosswalk; do not overwrite this one.

The snapshot's five-RQ labels are historical. Current documents use four questions; apply [`../tracking/rq_crosswalk.csv`](../tracking/rq_crosswalk.csv), union legacy RQ3/RQ4 by record ID, and map legacy RQ5 to controls RQ4. The unchanged 90-file survey snapshot is distinct from the local pre-revision coordination backup under `data/handoff_before_rq_revision_2026-10-12/`. Both are excluded from Git.

The user will handle GitHub upload separately. The Git commit contains English instructions, search log, blank templates, pilot IDs, task board, raw-export hash manifest, and snapshot summary. The 56 raw exports, abstracts, full queue, complete local-path manifest, and reviewer packets remain **local only**.

All Git-tracked documentation and tracking fields are in English. Local source exports remain faithful to the databases; original-language titles or abstracts are not translated or silently edited. The three Korean-language survey audit notes in the local snapshot are reference files and are excluded from Git.

Recheck from the `paper1_review_handoff` folder with the original workspace present:

```powershell
py -3 scripts/audit_local_survey_bundle.py
```
