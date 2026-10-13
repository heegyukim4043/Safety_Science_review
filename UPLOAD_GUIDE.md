# Upload this package to the repository root

**Target repository:** https://github.com/heegyukim4043/Safety_Science_review

Copy the contents of this folder into the repository root, preserving paths. Do not upload the outer package folder as a nested repository directory. Include `.github/`, `.gitignore` and `.gitattributes` along with the visible folders. Replace files with matching paths and add the new files; retain any unrelated team work.

| Folder/file | Contents |
|---|---|
| README.md | Concise four-part project overview |
| collaboration/ | Survey, RQs, allocation/phases, plan review and short project brief |
| docs/ | Full scientific plan, methods, SOP and phase/GitHub guides |
| tracking/ | Exact search log, source hashes, assignments, work items and pending decisions/gates |
| analysis/ | Four RQ round-1/round-2 starter kits and shared/integration handoffs |
| templates/ and .github/ | Feedback, coding, checkpoint, issue and PR templates |
| diagrams/ | Current two-round flow and supporting phase diagrams |
| scripts/ | Package validation and explicit-input preparation utilities |

Before upload, run `python scripts/check_upload_package.py --standalone`. After upload, open the README, research plan, collaborator briefings and primary PNG to confirm links. Read `UPLOAD_MANIFEST.csv` for filenames, sizes and hashes. It excludes itself and the validation receipt to avoid circular hashes.

The release shares methods/provenance/coordination, not raw source exports, full texts or reviewer judgments. References under `source_artifacts/` identify externally managed evidence; they are not missing repository downloads. Exact query strings, counts, source hashes and pending scientific status are preserved. Database export filename references are independent of any computer/storage path.

Replace the earlier README/workflow descriptions with this coherent release. The obsolete `docs/LOCAL_SURVEY_BUNDLE.md` and `scripts/audit_local_survey_bundle.py` can be removed from the repository after checking that no retained team content depends on them; this package no longer references them. Earlier diagram files may be kept as history, but use the new two-round diagram for current assignments.

No collaborator invitations, branches, protocol approvals or registrations are created by uploading planning files. Obtain team feedback and record actual assignment/decision evidence before dependent work.
