# Week-one launch plan (12–16 October 2026)

This is a task sequence, not a claim that screening has begun. Named owners and the final protocol are still needed. Update [`../tracking/tasks.csv`](../tracking/tasks.csv) as evidence is produced.

## Day 1: 12 October

- [ ] PI: review the complete [`collection and eligibility criteria`](COLLECTION_AND_ELIGIBILITY_CRITERIA.md) and sign open items in [`collection_decisions.csv`](../tracking/collection_decisions.csv): PCC, publication window/cutoff, language, source types, HRC boundary, adjacent-review treatment, and adjudication.
- [ ] PI: enter names/GitHub handles for the search lead, data steward, two paid non-author reviewers, adjudicator, G12, G34, and G5 in [`../tracking/assignments.csv`](../tracking/assignments.csv).
- [ ] Data steward: compare source-file hashes and counts to the local manifest; freeze the current 6,592-record queue as a provisional version. Do not overwrite local source exports or prior human decisions.
- [ ] Search lead: open the exact-query [`search log`](../tracking/search_log.csv). Identify all 25 missing execution times and 23 missing on-screen counts. Log what can be verified from platform histories; leave unverifiable cells blank.

## Days 2–3: 13–14 October

- [ ] Search lead: investigate Scopus screen/export gaps (1,061 versus 1,050; 107 versus 105), possible IEEE `I1_HRC` 1,000-record cap, ACM coverage/total, and the planned-but-unexported Scopus `S3_HRC` query. Record actual findings; propose a documented amendment if a query must be rerun.
- [ ] Data steward and adjudicator: resolve five same-title/conflicting-DOI groups manually; inspect the nine priority references not matched by DOI. Do not auto-merge conflicting identifiers.
- [ ] Data steward: begin staged abstract recovery for 3,034 missing abstracts, recording source and failure reason. Keep all records eligible for human screening meanwhile.
- [ ] G12/G34/G5: verify that the existing query blocks and known sentinel/adjacent papers cover their concepts; send additions to the search lead. Mark expansion terms as **proposed**, never as already executed.

## Days 4–5: 15–16 October

- [ ] PI/search lead: sign protocol v1, record unresolved search gaps, and register the protocol as planned. Give each amendment a version and date.
- [ ] Data steward: generate identical-content, separately editable Reviewer 1 and Reviewer 2 packets from the frozen queue. Confirm row count, unique IDs, and source hash. Distribute each packet separately. Use the reproducible [`pilot ID manifest`](../tracking/pilot_record_ids.csv) as a starting sample and have the PI check that borderline cases are represented.
- [ ] Reviewer 1/2 and adjudicator: schedule 50–100 mixed-record pilot for 19–23 October; review the English SOP before starting.
- [ ] Workstream leads: agree on fields and example rows in the blank study registry and evidence-link template. Decide where full texts and locators will be stored.

## Launch gates

Formal screening starts only after (1) named independent reviewers, (2) signed eligibility protocol/codebook after pilot, (3) frozen and versioned reviewer packets, and (4) a plan for search-log gaps and search updates. Search QA and abstract recovery may proceed in parallel with the pilot. The pilot's observed speed should replace provisional screening dates in the task board.

## Later milestones (provisional)

| Period | Output |
|---|---|
| 19–23 October 2026 | Independent pilot, disagreement review, codebook v1 |
| From 26 October 2026 | Complete dual title/abstract screening; weekly rate and disagreement reports |
| January–February 2027 | Dual full-text review, study/report linkage, independent RQ extraction |
| March 2027 | Agreed RQ tables, adjacent-review comparison, PRISMA flow, manuscript draft |

The current 6,592 records at 40 decisions/hour require about 165 hours **per reviewer** before abstract recovery, training, full-text work, and adjudication. Treat this as a planning assumption and recalibrate after the pilot.
