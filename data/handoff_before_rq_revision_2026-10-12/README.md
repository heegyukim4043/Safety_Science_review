# Paper 1 review: team handoff

**Study type:** scoping review and evidence map of algorithmic work conditions, worker responses, occupational safety and health (OSH), and evaluated controls. This folder contains a shareable English coordination package **and a local Git-ignored survey snapshot**. It is not a completed systematic search or a set of included studies. The corpus counts below describe the 12 October 2026 snapshot.

## Research purpose, questions, and deliverables

**Working title:** *Algorithmic work conditions as occupational exposures: a scoping review of measurement, safety and health pathways, and controls*.

The review treats work conditions changed by algorithms as workers' occupational exposures. It records the following connections at the study level:

`algorithmic function → experienced work condition/exposure (unit, intensity, time window) → exposure measurement → proposed or tested response pathway → worker OSH outcome → evaluated control`.

Conventional employment, platform/gig work, and human–robot collaboration (HRC) are coded as distinct contexts. The planned methodological framework is JBI scoping-review methodology, with PRISMA-ScR for review reporting and PRISMA-S for search reporting. These are planned methods; the search audit, independent screening, and evidence extraction are still pending.

| RQ | Question to resolve | Final deliverable |
|---|---|---|
| **RQ1 — function and work condition** | Which algorithmic functions changed which worker-facing work conditions? | A function/exposure-definition table with event, task, shift, or worker units. |
| **RQ2 — exposure definition and measurement** | How was exposure operationalized and measured, and over what time window? | A measurement matrix covering self-report, logs, observation, and experimental manipulation, including reliability/validity information. |
| **RQ3 — pathways** | Which cognitive, psychosocial, ergonomic, or physical risk pathways were proposed, observed, or tested? | A map distinguishing proposed pathways from measured and empirically tested pathways. |
| **RQ4 — OSH outcomes** | Which worker OSH outcomes were associated with exposure or affected in an experiment? | A table linking design, temporal ordering, outcomes, effect estimates, and limitations. |
| **RQ5 — controls** | Which controls were proposed, implemented, or evaluated? | A control type × evaluation level × worker OSH outcome table. |

### Novelty verification and pilot examples

The proposed contribution is study-level cross-coding of algorithmic functions, worker-experienced exposure units and time windows, measurement, pathways, OSH outcomes, and evaluated controls. Whether this adds a distinct evidence map remains a **positioning hypothesis** until the completed search and full-text comparison with adjacent reviews support it.

- Count Chen's 167-paper review as **one review**. Do not infer a classification of worker responses from its abstract; preserve the meaning of *complementary* as complementarity.
- Compare Bowdler, Matilla-Santander, Wei's conference abstract, Bao, and Jetha's distinct safety-tool review and living-review protocol. If Wei's completed full report becomes available, compare its tables directly. Keep conference abstracts and protocols identifiable as such.
- Use AMQ (three gig-worker samples, 1,332 participants, 20 items, five dimensions) and COMAMA (six samples including conventional employees, 1,005 participants, 11 items) as provisional RQ2 training examples of perceived-exposure scales. Verify their details and source locations against full text and distinguish them from event logs and experimental manipulations.
- Use the logistics cross-sectional accident/pain associations to practice recording design and confounding limitations under RQ4. Use Bao's HRC review to practice distinguishing allocation optimization from worker OSH outcome evidence. These examples are training and comparison sources, not automatic inclusions.

## Start here

1. The PI assigns names and GitHub handles in [`tracking/assignments.csv`](tracking/assignments.csv). Reviewer 1 and Reviewer 2 must be different, paid, non-author reviewers under the current research plan. The PI names a separate adjudicator.
2. The PI and search lead review the full [`collection and eligibility criteria`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md), sign the open [`collection decisions`](tracking/collection_decisions.csv), resolve [`search-log`](tracking/search_log.csv) gaps, and register any amendment before formal screening.
3. The data steward prepares **separate** Reviewer 1 and Reviewer 2 files from the local frozen screening queue. Each reviewer receives only their own file and the same English [`screening codebook`](docs/SCREENING_AND_EXTRACTION_SOP.md). Pilot 50–100 shared records before full screening.
4. After two independent decisions and adjudication, assign included studies to the three analytical workstreams described in [`docs/WORKSTREAMS.md`](docs/WORKSTREAMS.md). One study may feed several RQs.
5. Update [`tracking/tasks.csv`](tracking/tasks.csv) weekly. Each task has a completion gate and an evidence location. The first-week checklist is in [`docs/WEEK_ONE.md`](docs/WEEK_ONE.md).

## Work allocation

| Analytical lead | RQs | Handoff product |
|---|---|---|
| G12 | RQ1–2: function, work condition, exposure definition, measurement | Function-to-exposure and measurement matrix |
| G34 | RQ3–4: mechanisms and worker OSH outcomes | Mechanism/outcome evidence table with design and temporal ordering |
| G5 | RQ5: controls | Control evaluation ladder and worker OSH outcome table |

The three groups **do not screen separate keyword subsets**. Reviewer 1 and Reviewer 2 independently screen the same complete queue. Search terms organize retrieval and domain expertise; they do not define mutually exclusive study sets. Search QA, deduplication, eligibility decisions, full-text review, adjudication, and PRISMA counts are shared tasks.

### Roles, records, and decisions

| Role | Immediate responsibility | Record the work in |
|---|---|---|
| PI | Name the team, approve collection and eligibility rules, sign protocol changes, and approve reporting | [`tracking/assignments.csv`](tracking/assignments.csv), [`tracking/collection_decisions.csv`](tracking/collection_decisions.csv), [`tracking/protocol_amendments.csv`](tracking/protocol_amendments.csv) |
| Search lead | Verify exact database queries, dates, limits, hit counts, export gaps, and any search amendments | [`tracking/search_log.csv`](tracking/search_log.csv), [`tracking/tasks.csv`](tracking/tasks.csv) |
| Data steward | Preserve source provenance; manage provisional IDs, duplicate exceptions, abstract recovery, and versioned reviewer packets | [`docs/DATA_HANDOFF.md`](docs/DATA_HANDOFF.md), [`tracking/raw_export_manifest.csv`](tracking/raw_export_manifest.csv), [`tracking/tasks.csv`](tracking/tasks.csv) |
| Reviewer 1 and Reviewer 2 | Independently screen the **same full queue**, review full texts, and extract included-study evidence | Separate reviewer packets and [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md) |
| Adjudicator | Resolve conflicting screening, extraction, and identifier decisions while preserving both original judgments | [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md), [`tracking/tasks.csv`](tracking/tasks.csv) |
| G12, G34, and G5 leads | Check RQ coverage and synthesize agreed study-level extraction for their assigned questions | [`docs/WORKSTREAMS.md`](docs/WORKSTREAMS.md), [`tracking/workstream_keywords.csv`](tracking/workstream_keywords.csv), [`templates/`](templates/) |

These are **roles awaiting named assignees**, not completed assignments. The editable task board gives each action an owner role, dependency, target date, acceptance criterion, and evidence path. Use [`tracking/weekly_progress.csv`](tracking/weekly_progress.csv) for weekly throughput and unresolved work.

### Procedure and automation

1. **Collection and search:** Confirm the proposed collection rules and actual database coverage in [`docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md). Reconcile each executed query against [`tracking/search_log.csv`](tracking/search_log.csv); proposed terms in the workstream guide are not completed searches.
2. **Data preparation:** Keep the original exports unchanged. Use the source manifest and [`docs/DATA_HANDOFF.md`](docs/DATA_HANDOFF.md) to audit counts, hashes, duplicates, missing abstracts, and packet versions. Local scripts in [`scripts/`](scripts/) support bundle auditing, pilot-manifest generation, and pre-upload checks.
3. **Screening and extraction:** Follow [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md) for the pilot, independent decisions, adjudication, full-text review, and source-located RQ extraction. Blank study and evidence-link tables are in [`templates/`](templates/).
4. **Analysis and reporting:** Use the agreed study-level tables for G12, G34, and G5; check adjacent reviews and record/report/study denominators before writing novelty, effect, or PRISMA claims. The branch and review procedure is in [`docs/GITHUB_WORKFLOW.md`](docs/GITHUB_WORKFLOW.md).

Scripts may automate inventories, integrity checks, preliminary routing hints, and approved-code summaries. **Eligibility, RQ assignment, mechanism interpretation, and claims of control effectiveness require human review and adjudication.**

| Task suitable for automation | Required human check | Output |
|---|---|---|
| File inventory, SHA-256 hashes, search IDs, row counts, fields, and years | Verify actual platform hit counts, filters, execution times, and export completeness | Source manifest and search log |
| CSV/XLS/BibTeX normalization and DOI/ID/title duplicate candidates | Adjudicate conflicting identifiers and ambiguous title/year cases | Master records, source links, and duplicate decision log |
| PMID/DOI metadata and abstract retrieval into missing fields | Verify mismatches and record the retrieval source or failure reason | Recovery log and missingness report |
| Separate reviewer packets with identical IDs, input validation, and disagreement detection | Two reviewers independently assess every record/full text; an adjudicator resolves disagreements | Preserved independent decisions and consensus table |
| Keyword or proposed ASReview reading-order assistance | Complete the full queue; do not use ranking as an exclusion or stopping rule | Priority field, separate from eligibility |
| Study/report linkage candidates and summaries of approved codes | Verify full-text locators, denominators, interpretations, and novelty wording | Agreed study-level tables and figures |
| PRISMA and RQ-matrix counts from approved records | Check exclusion reasons and record/report/study mapping | Reporting tables and supplementary materials |

This table specifies the permitted workflow, not a claim that every automation has been implemented. The available scripts are listed in the folder map. Log each automation's date, tool/version, input, and changes. AI assistance is limited to file/metadata management, duplicate candidates, format checks, and reading-order support; reviewers and authors make the interpretive decisions and verify final evidence statements. Never automatically merge conflicting DOIs.

## Current corpus and limits

The local audit combined **56 exported files from five accessible databases**, yielding **10,858 exported rows**, **6,822 provisionally unique records**, and **6,592 records in the 2015–2026 screening queue**. These are file and processing counts, **not final PRISMA counts**. There are **3,034 records without an abstract**, **five same-title/conflicting-DOI groups**, and **nine of 43 priority references not linked by DOI**. Human screening and final RQ coding have **not started**. RQ keyword hints are overlapping, preliminary routing aids only.

The database exports available locally are from PubMed, Scopus, Web of Science Core Collection, IEEE Xplore, and ACM Digital Library. Embase, PsycINFO, and CINAHL were not accessible in this collection and must not be listed as completed searches. Of 42 search-plan rows, 25 have exported files and 17 do not. Search execution times are missing for all 25 exported searches; on-screen hit counts are missing for 23. These gaps must be reported or resolved from original search histories.

The screening queue contains **2,016 AM-only**, **13 AM/HRC-overlap**, and **4,563 HRC-only** retrieval records. These describe search provenance, not confirmed eligibility. HRC therefore accounts for much of the screening workload. The ACM source collection contributes 31 BibTeX files and 1,512 exported rows; all raw row counts can include repeated retrieval of the same study.

### Scope, eligibility, and reporting units

The working PCC covers human workers or people performing a credible work-task simulation; algorithmic/AI or adaptive systems that allocate/reallocate tasks, set pace or schedules, monitor, evaluate, reward/penalize, or otherwise change a worker-facing condition; and conventional, platform, or simulated work contexts. Core empirical studies must define, measure, or manipulate the relevant condition and report a worker response, OSH-related outcome, exposure-measurement property, or relevant control. Relevant HRC studies may qualify without using the phrase *algorithmic management*. Reviews, theory, and guidelines are retained separately for background and adjacent-review comparison.

Exclude robot-only collision, route, or throughput optimization without a human work condition or response; consumer/patient-only AI without a work-task analogue; general ethics commentary without the relevant empirical evidence; and macro employment forecasts without worker exposure. Missing abstracts are not an exclusion criterion. Apply the detailed rules and unresolved decisions in [`docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md).

Use **record** for search and screening, **report** for a full-text document, and **study** for the underlying investigation and main synthesis denominator. Link multiple reports of one study; retain each effect estimate's original analysis unit and repeated-measure structure. Multiple effects, events, shifts, or RQ contributions do not create additional independent studies.

Before formal screening, resolve and record: (1) the rationale for the 2015 start and actual final search cutoff; (2) language, publication/source types, and grey-literature coverage; (3) the HRC worker/work-task boundary; (4) linkage of multiple reports of the same study; (5) two paid non-author reviewers, an adjudicator, and their available hours; (6) full-text retrieval and unavailability procedures; and (7) AI/automation limits. The PI owns protocol and interpretation approval, the search lead owns query/provenance checks, and the data steward owns source and version integrity.

### RQ-by-RQ evidence readiness

The counts below come from the local `data/survey_2026-10-12/organized/generated/RQ*_candidates_not_screened.csv` snapshot. They combine keyword and priority-source hints; they are **not included-study counts**. Abstract availability describes metadata completeness, not study relevance or quality.

| RQ | Unscreened candidates | With an abstract | What is ready | Main work before synthesis |
|---|---:|---:|---|---|
| **RQ1 — function to work condition** | 5,079 | 3,198 | A broad routing pool across AM and HRC searches | Screen out unrelated robotics and distinguish algorithmic functions from measured changes in work conditions. |
| **RQ2 — exposure definition and measurement** | 1,105 | 940 | Dedicated measurement searches and candidate records | Extract exposure unit, time window, data source, and reliability/validity from full text. |
| **RQ3 — pathways** | 1,831 | 1,491 | Candidates from OSH, HRC, and common AM searches | Audit the missing dedicated pathway search; separate proposed pathways from measured or tested mechanisms. |
| **RQ4 — worker OSH outcomes** | 1,944 | 1,550 | Outcome-related candidate records | Separate technical safety outcomes from worker health/injury outcomes and assess design and estimates. |
| **RQ5 — controls** | 905 | 837 | Dedicated control searches and candidate records | Classify proposals, simulations, human evaluations, and field evaluations of worker OSH outcomes. |

**Readiness judgment:** Bibliographic organization is complete enough to launch search QA and prepare the screening pilot; the pilot follows protocol decisions. Evidence synthesis is not yet ready for any RQ: no record has a human eligibility decision or final RQ code, and no included-study extraction has been agreed. The RQ counts overlap: **3,237 queue records have multiple RQ hints**, while **1,015 have none**; the latter remain in the shared screening queue. Do not add RQ candidate counts or use them as PRISMA inclusion numbers.

**Next gates:** (1) complete and reconcile search histories, including the missing Scopus `S3_HRC` export and the RQ3 pathway-search decision; (2) lock eligibility and collection decisions, resolve the five DOI conflicts, and retrieve missing abstracts in priority order; (3) run the shared 50–100-record pilot with two independent reviewers; (4) screen and adjudicate the full queue, then extract study-level evidence for each RQ. Track owners and acceptance evidence in [`tracking/tasks.csv`](tracking/tasks.csv), and follow [`docs/WEEK_ONE.md`](docs/WEEK_ONE.md).

## Schedule and completion gates

Dates are planning targets, not evidence that work has occurred. Named reviewers, search/export reconciliation, abstract recovery, and full-text access are the main current dependencies. Recalculate dates using observed pilot throughput and the actual staff calendar.

| Planned period | Work | Completion evidence |
|---|---|---|
| **12 October 2026** | Freeze/hash 56 source files; audit 10,858/6,822/6,592 provisional counts; start screen/export reconciliation | Frozen manifest, audit log, and discrepancy records. Bibliographic preparation is complete; search reconciliation remains pending. |
| **13–16 October 2026** | Recover abstracts; adjudicate five DOI conflicts; inspect `S3_HRC`, IEEE's possible 1,000-record cap, and Scopus 1,061/1,050 and 107/105 gaps; review searches and approve/register protocol or amendments | Recovery provenance, query/export decisions, approved criteria, protocol version and registration record. |
| **19–23 October 2026** | Two independent reviewers pilot the same 50–100 mixed AM/HRC records, including records without abstracts; revise examples and retrain | Pre-consensus agreement, disagreement types, and revised codebook; no numeric threshold alone establishes readiness. |
| **26 October 2026–15 January 2027, provisional** | Dual title/abstract screening of the full queue, weekly adjudication, abstract recovery, and parallel full-text retrieval | Two original decisions, final consensus/reason for every ID, and weekly throughput reports. |
| **18 January–26 February 2027, provisional** | Dual full-text assessment; study/report linkage; pilot extraction on 10–20 studies, then independent RQ1–5 extraction | Full-text exclusion reasons, study/report crosswalk, and agreed extraction with source locations. |
| **1–26 March 2027, provisional** | RQ matrices, design/evidence appraisal, missingness and sensitivity analyses, denominator QA, adjacent-review comparison, and drafting | PRISMA flow, PRISMA-S search table, evidence tables/maps, source traceability, and draft v1. |
| **April 2027 onward, conditional** | Coauthor source verification, journal/reporting checks, and search update | Submission-ready manuscript after the evidence and staffing requirements are met. |

At the planning rate of 40 title/abstract decisions per hour, 6,592 records require about **165 hours per reviewer**, excluding training, recovery, adjudication, and full-text work. Use actual pilot rates to revise this assumption. Detailed owners, dependencies, and task status are in [`tracking/tasks.csv`](tracking/tasks.csv).

### Analytical outputs and transfer to later experiments

| Output from agreed study-level codes | Human verification before interpretation |
|---|---|
| Function × work condition × sector/employment context | Does the same term represent different work conditions across contexts? |
| Exposure × measurement method × time window | Have perceived exposure, observed events, and experimental manipulations been distinguished? |
| Pathway × OSH outcome × study design | Was the pathway proposed, measured, or tested, and does the design establish temporal ordering? |
| Control × implementation/evaluation level × worker outcome | Does the evidence evaluate control of the relevant exposure and an actual worker outcome? |
| Evidence gaps and candidate variables for later experiments | Does an empty cell reflect retrieval/measurement gaps, or a studied null effect? |

Transfer candidate variables to later experiments only when the review supports reproducible exposure definitions, manipulable conditions, and outcome measures. Record proposed experimental hypotheses separately from reviewed intervention effects. Automation may summarize agreed codes; human reviewers verify every denominator, interpretation, and source location.

The review is complete when:

1. The five accessible databases' queries, execution histories, source exports, discrepancies, and inaccessible-source limitations are traceable.
2. Duplicate adjudication, dual screening, full-text decisions, exclusion reasons, and any update-search records follow the documented procedure.
3. RQ1–5 tables use study-level denominators and link every quantitative entry and evidence statement to a full-text location; sensitivity to publication dates, source types, and HRC boundaries is documented.
4. Adjacent-review overlap has been checked, novelty wording matches the completed evidence, and PRISMA-ScR, PRISMA-S, and journal reporting requirements have been reviewed.

## Folder map

| Path | Purpose |
|---|---|
| [`docs/WEEK_ONE.md`](docs/WEEK_ONE.md) | First-week sequence and decision gates |
| [`docs/WORKSTREAMS.md`](docs/WORKSTREAMS.md) | RQ questions, actual search terms, additional terms, and outputs |
| [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md) | Eligibility, independent screening, adjudication, extraction, and evidence grading rules |
| [`docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md) | Complete working collection criteria, database coverage, exclusions, and unresolved protocol decisions |
| [`docs/DATA_HANDOFF.md`](docs/DATA_HANDOFF.md) | Local data paths, reviewer packet delivery, and version checks |
| [`docs/LOCAL_SURVEY_BUNDLE.md`](docs/LOCAL_SURVEY_BUNDLE.md) | Inventory and handling rules for the 90-file local `data/` snapshot |
| [`docs/UPLOAD_CHECKLIST.md`](docs/UPLOAD_CHECKLIST.md) | English-only and collection-criteria checks before the user's later upload |
| [`docs/GITHUB_WORKFLOW.md`](docs/GITHUB_WORKFLOW.md) | Branches, issues, pull requests, and review rules |
| [`tracking/assignments.csv`](tracking/assignments.csv) | Names and GitHub handles to fill before work starts |
| [`tracking/tasks.csv`](tracking/tasks.csv) | Task owners, dates, status, dependencies, and acceptance gates |
| [`tracking/weekly_progress.csv`](tracking/weekly_progress.csv) | Weekly screening, extraction, and issue counts |
| [`tracking/workstream_keywords.csv`](tracking/workstream_keywords.csv) | Three editable keyword/search-ID bundles for assignment |
| [`tracking/pilot_record_ids.csv`](tracking/pilot_record_ids.csv) | Reproducible 50–100-record pilot ID list; no abstracts or decisions |
| [`tracking/search_log.csv`](tracking/search_log.csv) | Snapshot of exact queries and execution gaps; verify against platforms |
| [`tracking/protocol_amendments.csv`](tracking/protocol_amendments.csv) | Dated record of approved search and eligibility changes |
| [`tracking/collection_decisions.csv`](tracking/collection_decisions.csv) | PI sign-off table for collection criteria that are not yet locked |
| [`tracking/raw_export_manifest.csv`](tracking/raw_export_manifest.csv) | English file names and SHA-256 hashes for the 56 raw exports |
| [`tracking/survey_snapshot_summary.json`](tracking/survey_snapshot_summary.json) | English-only summary of the local 90-file snapshot |
| [`templates/`](templates/) | Blank study registry and evidence-link tables |
| [`scripts/`](scripts/) | Local bundle audit, pilot-manifest, and upload-package checks |

## Source of truth and upload boundary

The original records and processing scripts remain in the parent workspace's survey folder. A byte-identical 90-file copy of the selected survey contents is at `data/survey_2026-10-12/`; this local `data/` folder is excluded from Git. The user will handle any upload separately. See [`docs/LOCAL_SURVEY_BUNDLE.md`](docs/LOCAL_SURVEY_BUNDLE.md) before giving reviewers working copies. If eligibility or search decisions change, update the signed protocol and amendment log first; do not edit source exports or overwrite independent reviewer decisions.

