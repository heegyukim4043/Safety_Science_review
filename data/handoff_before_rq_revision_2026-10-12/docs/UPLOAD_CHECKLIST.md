# English-only upload checklist

The user will upload this repository separately. The intended Git upload contains English documentation, task and decision tables, exact search strings, the 56-file raw-export hash list, and a local snapshot summary. The `data/` folder is excluded from Git and is **not** part of this upload candidate.

Before uploading:

1. Run `py -3 scripts/check_upload_package.py` from the repository root. It checks tracked text and filenames for Korean script, required collection-criteria files, Markdown links, CSV shape, search-log counts, and exclusion of `data/` from Git.
2. Read [`COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](COLLECTION_AND_ELIGIBILITY_CRITERIA.md). Have the PI fill and approve [`collection_decisions.csv`](../tracking/collection_decisions.csv) before formal screening. Unapproved rules remain visibly pending; do not turn them into retrospective claims.
3. Confirm that only intended files are staged with `git status --short` and `git diff --cached --stat`.
4. Keep raw exports, original-language bibliographic records, abstracts, full texts, and reviewer decisions in the local controlled survey snapshot until an explicit data-sharing decision is made. Do not translate original study titles or abstracts in an audit copy.

The English-only requirement applies to **authored upload materials and file paths**. Source records retain their original language for provenance and will require a separate release decision if uploaded later.
