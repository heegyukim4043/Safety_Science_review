# English-only upload checklist

The user will upload this repository separately. The intended Git upload contains English documentation, task and decision tables, exact search strings, the 56-file raw-export hash list, and a local snapshot summary. The `data/` folder is excluded from Git and is **not** part of this upload candidate.

Before uploading:

1. Run `py -3.9 scripts/check_upload_package.py` from the repository root. It checks tracked and untracked upload-candidate text/paths for Korean script, required methods files, Markdown links, CSV shape, search counts, the four-RQ mapping, calibration IDs, and exclusion of `data/` from Git. Untracked candidate files still require staging/commit by the uploader.
2. Read [`COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](COLLECTION_AND_ELIGIBILITY_CRITERIA.md). Have the PI fill and approve [`collection_decisions.csv`](../tracking/collection_decisions.csv) before formal screening. Unapproved rules remain visibly pending; do not turn them into retrospective claims.
3. Confirm that only intended files are staged with `git status --short` and `git diff --cached --stat`.
4. Keep raw exports, original-language bibliographic records, abstracts, full texts, and reviewer decisions in the local controlled survey snapshot until an explicit data-sharing decision is made. Do not translate original study titles or abstracts in an audit copy.
5. Confirm current four-RQ labels in the README/tasks/templates, preserve legacy labels only where explicitly identified, and include the [source-plan comparison](SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md), crosswalk, reliability plan, and blank measurement-framework template. Working revisions must not be labeled signed/registered amendments before PI approval.

The English-only requirement applies to **authored upload materials and file paths**. Source records retain their original language for provenance and will require a separate release decision if uploaded later.
