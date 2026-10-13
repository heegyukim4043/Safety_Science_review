# Week-one launch plan (12–16 October 2026)

This is a task sequence, not a claim that screening has begun. Named owners and the final protocol are still needed. Update [`../tracking/tasks.csv`](../tracking/tasks.csv) as evidence is produced. Use the [stage/branch plan](RESEARCH_STAGES_AND_BRANCHES.md) and [four-RQ allocation](TEAM_ASSIGNMENTS_AND_HANDOFFS.md); G12/G3/G4 in this checklist are coordination bundles, with separate RQ1_LEAD through RQ4_LEAD assignments.

## Day 1: 12 October

- [ ] PI: review the complete [`collection and eligibility criteria`](COLLECTION_AND_ELIGIBILITY_CRITERIA.md) and sign open items in [`collection_decisions.csv`](../tracking/collection_decisions.csv): PCC, publication window/cutoff, language, source types, HRC boundary, adjacent-review treatment, and adjudication.
- [ ] PI: confirm funding/hours and enter names/GitHub handles for the search lead, data steward, two trained paid non-author reviewers, adjudication role, and four RQ leads in [`../tracking/assignments.csv`](../tracking/assignments.csv). Assign RQ1/RQ2 separately even if one person holds both roles. The source assigns unresolved adjudication to Nam/Staley; an additional separate person is optional.
- [ ] PI: review the [source-plan comparison](SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md), approve four RQs with RQ3a/RQ3b fields, and freeze source reliability targets, field tiers, and AI limits in the protocol decisions.
- [ ] Data steward: compare source-file hashes and counts to the source manifest; freeze the current 6,592-record queue as a provisional version. Do not overwrite source exports or prior human decisions.
- [ ] Search lead: open the exact-query [`search log`](../tracking/search_log.csv). Identify all 25 missing execution times and 23 missing on-screen counts. Log what can be verified from platform histories; leave unverifiable cells blank.

## Days 2–3: 13–14 October

- [ ] Search lead: investigate Scopus screen/export gaps (1,061 versus 1,050; 107 versus 105), possible IEEE `I1_HRC` 1,000-record cap, ACM coverage/total, and the planned-but-unexported Scopus `S3_HRC` query. Record actual findings; propose a documented amendment if a query must be rerun.
- [ ] Data steward and adjudicator: resolve five same-title/conflicting-DOI groups manually; inspect the nine priority references not matched by DOI. Do not auto-merge conflicting identifiers.
- [ ] Data steward: begin staged abstract recovery for 3,034 missing abstracts, recording source and failure reason. Keep all records eligible for human screening meanwhile.
- [ ] G12/G3/G4: verify query and sentinel/adjacent-paper coverage; send additions to the search lead. Mark expansion terms as **proposed**, never as already executed. Audit pathway/organizational and dose–response coverage for integrated RQ3.
- [ ] Search lead: arrange independent PRESS review of final/update queries, archive comments/responses, document missing PsycINFO coverage and the ACM unique-coverage rationale, and distinguish later Embase/CINAHL expansions from original recommendations.

## Days 4–5: 15–16 October

- [ ] PI/search lead: sign/register protocol v1 with four RQs, reliability thresholds/statistic choices, coder design, source types, AI policy, and analysis; record unresolved search gaps and amendments without claiming a completed search.
- [ ] Data steward: prepare separate reviewer packets with identical content and verify count, IDs and hash. The legacy [`pilot manifest`](../tracking/pilot_record_ids.csv) is a 93-record mixed training pool. The new [`calibration manifest`](../tracking/calibration_record_ids.csv) contains two disjoint random 25-record rounds excluding that training pool; regenerate if the frozen queue changes and keep source/seed records.
- [ ] Reviewer 1/2 and adjudication role: schedule training, competency check, round 1, example revision, and fresh round 2 for 19–23 October. Source targets: agreement >=85% and AC1 >=0.80, with kappa also reported; evaluate substantive errors and repeat on fresh records when necessary.
- [ ] Workstream leads: agree on fields and example rows in the blank study registry and evidence-link template. Decide where full texts and locators will be stored.

## Launch gates

Formal screening starts after named/funded trained reviewers, signed/registered protocol and reliability plan, successful calibration and frozen codebook, versioned packets, and documented PRESS/search-gap/update decisions. Search QA and abstract recovery may proceed during training preparation. Replace provisional dates using observed throughput. Full-text work requires a separate 10–15-report calibration with agreement >=90% and AC1 >=0.80. Core coding requires prespecified pre-consensus reliability and recoding rules; see [`../tracking/reliability_plan.csv`](../tracking/reliability_plan.csv).

## Later milestones (provisional)

| Period | Output |
|---|---|
| 19–23 October 2026 | Training/competency check, two random 25-record calibration rounds, disagreement review, codebook v1 |
| From 26 October 2026 | Complete dual title/abstract screening; weekly rate and disagreement reports |
| January–February 2027 | Full-text calibration/dual review, study linkage, descriptive verification and independent core RQ1–4 coding |
| March 2027 | RQ tables, measurement framework, reliability table, adjacent-review comparison, PRISMA flow, manuscript draft |

The current 6,592 records at 40 decisions/hour require about 165 hours **per reviewer** before abstract recovery, training, full-text work, and adjudication. Treat this as a planning assumption and recalibrate after the pilot.
