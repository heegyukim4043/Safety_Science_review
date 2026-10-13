# Paper 1: collection and eligibility criteria

**Working version:** 0.2, 12 October 2026; `four_rq_v0.2`. This document makes the current evidence-collection rules explicit for team handoff. The PI must sign the unresolved decisions in [`../tracking/collection_decisions.csv`](../tracking/collection_decisions.csv), review the search log, and register/amend the protocol before formal screening. A database export is evidence of retrieval, **not** proof that the search was complete or that any record is eligible. See the [source-plan comparison](SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md).

## 1. Review purpose and question structure

For current per-RQ owners, branches and outputs, see the [team allocation](TEAM_ASSIGNMENTS_AND_HANDOFFS.md) and [RQ assignment table](../tracking/rq_assignments.csv). G12/G3/G4 below denote keyword/coordination bundles; current accountability is separately assigned for RQ1, RQ2, RQ3 and RQ4.

The planned study is a **scoping review and evidence map** of work conditions produced by algorithmic management or related human–robot/adaptive work systems. The linked unit of analysis is:

`algorithmic function → experienced work condition/exposure → exposure definition and measurement → proposed or tested pathway → worker OSH outcome → evaluated control`.

G12 addresses RQ1 (exposure characteristics) and RQ2 (operationalization and measurement). G3 addresses integrated RQ3 (pathways, worker OSH outcomes, empirical support, and evidence gaps), retaining RQ3a/RQ3b extraction subdomains. G4 addresses current RQ4 (modifiable controls). The legacy-to-current mapping is in [`../tracking/rq_crosswalk.csv`](../tracking/rq_crosswalk.csv). A study may answer multiple RQs. The analytical groups do not form separate or mutually exclusive screening populations.

## 2. PCC and primary-study eligibility

| Component | Current working criterion | Apply at screening |
|---|---|---|
| **Population** | Human workers or human participants performing a credible simulation of work tasks. Conventional employees and platform/gig workers are eligible and coded as different contexts. | Exclude consumer-, patient-, or student-only studies without a worker/work-task analogue. A healthcare worker doing their job is a worker. |
| **Concept** | An algorithmic/AI or adaptive automation decision allocates or reallocates tasks, schedules, paces, monitors, evaluates, rewards/penalizes, or otherwise changes a condition a worker can experience. Relevant human–robot collaboration (HRC) may qualify without the phrase “algorithmic management.” | The system must produce, define, measure, or experimentally manipulate a worker-facing work condition. AI use alone is insufficient. |
| **Context** | Conventional employment, platform/gig work, and human work-task experiments. Sector and country are extracted rather than presumed equivalent. | Do not use employment context alone to exclude a study that meets the other criteria. |
| **Evidence requirement** | Original empirical work that defines, measures, or manipulates the relevant condition **and** reports a worker response, OSH-related outcome, exposure measurement property, or relevant control. Qualitative, quantitative, mixed-method, and human experimental evidence can be considered under this rule. | Retain plausible records for full-text assessment when the abstract does not resolve these elements. |
| **Control studies** | Core studies provide original empirical human work/exposure evidence for an implemented/evaluated software- or work-design control. Relevant proposals, reviews, and technical simulations can inform a separate background/candidate-control table. | A control label does not override primary-study eligibility. A proposal or robot-only simulation does not demonstrate worker OSH effectiveness. |

**Exclude from the core empirical synthesis:** robot route/collision/throughput optimization without a human work condition or worker response; diagnostic AI concerning patients only; general AI ethics commentary with no worker-facing work condition; macro labor-market forecasts with no worker exposure; reviews/theory/editorials/guidelines without original data. Keep relevant reviews and guidelines in a **separate background/adjacent-review table** so novelty and citation claims can be checked. A title containing `safety` or matching a keyword is not sufficient for inclusion.

Worker states and proximal indicators remain within the source scope: workload, fatigue, stress, situation awareness, autonomy/control, trust/reliance, physical load, errors, omissions, and hazard-response/near-miss proxies, with injury/illness when available. Code whether each variable is an exposure, mediator, worker-state outcome, safety-behavior proxy, or injury/illness endpoint in that study. Organizational pathways are retained. An outcome association can contribute to RQ3b even when no mediator was measured for RQ3a.

## 3. Date, language, and source-type boundaries

| Rule | Current state | Decision still required |
|---|---|---|
| Publication period | The existing queue is filtered to **2015–2026**. Many planned strings use `2015-01-01` to `2026-10-02`; exported search histories do not fully establish the actual execution timestamp for each query. | PI/search lead must state the rationale for 2015, the final inclusive search cutoff, how online versus print years are handled, and the date of any update search. Do not label the current file date as an executed search date. |
| Language | No language-based exclusion has been applied to the working queue solely by automation. | PI must decide whether any language restriction exists, whether translation is available, and how it will be reported. Do not silently exclude non-English records. Preserve original-language bibliographic titles and abstracts as source data; English documentation does not mean translating source records. |
| Publication/source types | Core analysis is original empirical evidence. Reviews and protocols are separated for context/novelty. Exported database records may include journals, conference publications, and other document types. | PI must lock treatment of conference abstracts/full papers, preprints, dissertations, reports, and grey literature. The existing 5-database file collection cannot be described as covering inaccessible databases or all grey literature. |
| Full-text availability | A record is not excluded merely because its abstract is missing. | Define a documented library/open-copy/author-contact sequence before using `full_text_unavailable`. |

These unresolved items are gates for the final protocol. They are not blanks to fill with assumptions when writing PRISMA or the manuscript.

## 4. Search sources and execution state

The exact field tags, Boolean syntax, phrase marks, limits, status, export file, and available counts for every planned search are in [`../tracking/search_log.csv`](../tracking/search_log.csv). Use **that row-level record**, not the compact keyword table, to reproduce a platform query.

The original DOCX recommends WoS, Scopus, PubMed/MEDLINE, PsycINFO and IEEE, with ACM conditional on unique HCI coverage. PsycINFO is an unfulfilled original recommendation; Embase and CINAHL are later search-plan expansions. Some current discovery queries omit the worker/outcome concept blocks from the source's three-family architecture. Document this broader retrieval and its precision/coverage implications. Obtain independent **PRESS** review of final or update queries before execution and archive comments, responses, and final syntax. No completed PRESS review is currently recorded.

| Source | Exported search IDs in the collected corpus | State |
|---|---|---|
| PubMed | `P1_AM`, `P2_OSH`, `P3_HRC`, `P4_REVIEW`, `P5_MEASURE`, `P6_CONTROL` | Six exports present; not screened |
| Scopus | `S1_AM`, `S1B_AM_EXPAND`, `S2_OSH`, `S4_REVIEW`, `S5_MEASURE`, `S6_CONTROL` | Six exports present; `S3_HRC` is planned with **no export** |
| Web of Science Core Collection | `W1_AM`, `W2_OSH`, `W3_HRC`, `W4_REVIEW`, `W5_MEASURE`, `W6_CONTROL` | Six exports present; not screened |
| IEEE Xplore | `I1_HRC`, `I2_ALLOC`, `I3_AM`, `I4_CONTROL` | Four exports present; possible `I1_HRC` 1,000-record cap needs verification |
| ACM Digital Library | `A1_AM`, `A2_CONTROL`, `A3_HRC` | Three exports present; complete on-screen total/coverage needs verification |

Together these are **25 exported search-plan rows**. Another **17 rows** are planned but lack exports: Scopus `S3_HRC`; Embase on Ovid; APA PsycINFO on Ovid; five CINAHL on EBSCOhost rows; four Europe PMC rows; one OpenAlex discovery row; and four Google Scholar discovery rows. These are **not completed searches**. Embase, PsycINFO, and CINAHL were not accessible for this collected corpus. Review-identification queries (`P4_REVIEW`, `S4_REVIEW`, `W4_REVIEW`) locate adjacent reviews and should not be added to primary-study counts.

The existing search architecture combines common algorithmic management/control and HRC/adaptive-automation concepts with OSH, measurement, control, and review terms. [`../tracking/workstream_keywords.csv`](../tracking/workstream_keywords.csv) distinguishes terms found in exported queries from **additional terms that have not been run as a dedicated expansion**. In particular, there is no exported dedicated RQ3 pathway query. Search leads should evaluate expansion proposals for incremental recall, duplication, sentinel-paper coverage, and feasibility, then document any new query as a protocol amendment.

### Search completeness checks still open

- Verify execution date/time and timezone for all 25 exported searches; do not infer them from export timestamps.
- Verify 23 missing on-screen hit counts and distinguish them from exported row counts.
- Resolve Scopus screen/export differences of **1,061 versus 1,050** and **107 versus 105**.
- Investigate whether IEEE `I1_HRC` stopped at 1,000 records and whether a split export is necessary.
- Verify ACM collection/range and on-screen total; decide how to handle `S3_HRC`.
- Record database platform/collection, exact query, field tags, limits, date/time, screen hits, exported rows, file hash, and any rerun as distinct versions.

## 5. Intake, deduplication, and priority records

The current collected corpus comprises **56 raw export files** and **10,858 export rows**. Normalization and machine-generated duplicate candidates produced **6,822 provisionally unique records**, of which **6,592** fall in the working 2015–2026 screening queue. These numbers are file-processing checkpoints, not final PRISMA flow numbers. The original files remain unchanged; the raw-export hashes are in [`../tracking/raw_export_manifest.csv`](../tracking/raw_export_manifest.csv).

Link each screened `record_id` to all contributing database/search IDs. Use exact DOI or stable database identifiers and normalized titles for **duplicate candidates**, but adjudicate ambiguous cases. Five same-title/different-DOI groups await manual decision. Connect multiple full-text `report_id` values to one `study_id` when they report the same study; do not collapse independent studies because titles resemble each other. Preserve pre- and post-update IDs with a crosswalk.

The earlier 43-paper priority list is a **sentinel and comparison set**, not an automatically included sample. Thirty-four are linked by DOI; nine need manual title/author/report verification. Search recall can be checked against verified sentinel papers without forcing their inclusion.

## 6. Screening, missing abstracts, and RQ assignment

Two trained paid non-author reviewers independently judge the **same complete 6,592-record queue** at title/abstract and full text. They use `include`, `exclude`, or `uncertain`, a primary exclusion code for each exclusion, and a named adjudication role. The original source specifies Nam/Staley for unresolved cases; an additional separate adjudicator is optional. The source's two random 25-record calibration rounds, full-text calibration, competency check, reliability statistics/targets, field tiers, and recoding rules are restored in [`SCREENING_AND_EXTRACTION_SOP.md`](SCREENING_AND_EXTRACTION_SOP.md). Independent coders do not develop hypotheses or interpret the final framework.

The queue contains **3,034 records without abstracts**. Recover abstracts or metadata with source/provenance logging; if recovery fails, do not automatically exclude the record. An RQ keyword/seed hint is only a routing aid. Current RQ1–RQ4 pools overlap, and **1,015 records have no hint**; all still receive human screening. The frozen snapshot retains five legacy hint labels; use the crosswalk and union by `record_id` for integrated RQ3. One included study may contribute to multiple RQs. Core fields are independently double-coded; descriptive fields are extracted once and verified for all records. Analytical leads synthesize agreed study-level extraction.

## 7. Reporting units and change control

Use `record` for identification/deduplication/screening flow, `report` for full-text assessment, and `study` for the main synthesis denominator. Label all provisional counts as provisional until search QA, deduplication adjudication, dual screening, and study/report linkage are complete. The planned methods follow the project's JBI scoping-review framework, PRISMA-ScR for review reporting, and PRISMA-S for search reporting; claiming those labels does not establish that current searches are complete.

Before formal screening, the PI signs the open decisions in [`../tracking/collection_decisions.csv`](../tracking/collection_decisions.csv). Freeze RQs, eligibility, coder design, reliability thresholds/statistic rules, AI policy and analysis in the OSF protocol. Enter every substantive search/eligibility amendment in [`../tracking/protocol_amendments.csv`](../tracking/protocol_amendments.csv) with the old and new rule, rationale, approval, affected records, and re-screening decision. Preserve independent reviewer originals and prior search versions. The current four-RQ/source-method revision is a working-document change pending signed protocol approval. Novelty and control-effect claims require full-text verification and adjacent-review comparison.
