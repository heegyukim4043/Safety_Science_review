# Paper 1 review: team handoff

**Study type:** scoping review and evidence map of algorithmic work conditions, worker responses, occupational safety and health (OSH), and evaluated controls. This folder contains a shareable English coordination package **and a local Git-ignored survey snapshot**. It is not a completed systematic search or a set of included studies. The corpus counts below describe the 12 October 2026 snapshot.

**Current RQ structure:** `four_rq_v0.2`. The source DOCX's RQ3/RQ4 are combined into current RQ3; its RQ5 becomes current RQ4. Read the [source-plan comparison and design evaluation](docs/SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md) for the strategy/methodology differences and restoration decisions. This is a working revision pending PI protocol sign-off.

## Share this overview with collaborators

| What collaborators need | Start here |
|---|---|
| Research objective, four RQs, completed work, actual search coverage/strategy, target period, and applied versus planned inclusion/exclusion | [Project status and working protocol](docs/PROJECT_STATUS_AND_REVIEW_PROTOCOL.md) |
| Future method stages, prerequisites, automation boundary, four RQ branches and integration gates | [Research stages and branches](docs/RESEARCH_STAGES_AND_BRANCHES.md) |
| Clear responsibility for shared methods and each RQ, keywords, outputs, cross-review and team handoffs | [Team assignments and handoffs](docs/TEAM_ASSIGNMENTS_AND_HANDOFFS.md) |

**Status:** exports exist for 25 planned queries in five databases; 56 files/10,858 retrieval rows were organized into 6,822 provisional unique records and a 6,592-record working-year queue. Human eligibility decisions, agreed included-study extractions and RQ findings are not documented as completed. Exact execution times, export-completeness checks and final signed criteria remain open. GitHub upload, remote branches/issues and named assignments are not completed by this local update.

## Research purpose, questions, and deliverables

**Working title:** *Algorithmic work conditions as occupational exposures: a scoping review of measurement, safety and health pathways, and controls*.

The review treats work conditions changed by algorithms as workers' occupational exposures. It records the following connections at the study level:

`algorithmic function → experienced work condition/exposure (unit, intensity, time window) → exposure measurement → proposed or tested response pathway → worker OSH outcome → evaluated control`.

Conventional employment, platform/gig work, and human–robot collaboration (HRC) are coded as distinct contexts. The primary products are an operational exposure framework, evidence map, and **measurement framework** to inform the later Delphi/experimental program and a future NIOSH R01. The planned architecture is **JBI + PRISMA-ScR + PRISMA-S + independent PRESS search review + OSF preregistration**. Freeze the RQs, eligibility, coder/reliability plan, AI policy, and analysis before formal screening. Search peer review, registration, screening, and evidence extraction are not yet documented as completed.

| RQ | Question to resolve | Final deliverable |
|---|---|---|
| **RQ1 — exposure characteristics** | Which algorithmic functions and worker-facing work characteristics have been studied as occupational exposures, and how are the exposure dimensions defined? | A function → work condition/exposure taxonomy with operational definitions and event/task/shift/worker units. |
| **RQ2 — operationalization and measurement** | How have exposures been measured in terms of unit, dose/intensity, frequency, variability, time window, reversibility, and worker control, and what measurement properties and gaps are reported? | A self-report/log/observation/manipulation matrix and candidate measurement framework with reliability/validity evidence. |
| **RQ3 — pathways and OSH evidence** | Through which proposed or tested cognitive, psychosocial, ergonomic, physical-safety, or organizational pathways are exposures linked to worker OSH outcomes, with what empirical support, limitations, and evidence gaps? | A linked pathway/outcome/design evidence map with estimates, temporal order, dose–response evidence, and gaps. |
| **RQ4 — modifiable controls** | Which software/work-design controls have been empirically implemented or evaluated, at what evaluation level, and with what worker response or OSH outcomes? | A control × evaluation level × worker-outcome matrix, separating background proposals and follow-on candidates. |

Within RQ3, **RQ3a** retains pathway coding and **RQ3b** retains outcome/empirical-support coding. These are subdomains, not extra headline questions. A study can contribute outcome evidence without measuring a mediator; code the missing pathway rather than inferring it. Use the [old-to-new crosswalk](tracking/rq_crosswalk.csv) for the unchanged five-RQ source files. The merger simplifies presentation, while the full screening and two coding subdomains remain necessary.

Keep the proposed L0–L3 exposure-operationalization description, measurement validation, and exposure–response support as distinct axes. A validated scale and evidence of an exposure–outcome relationship establish different properties; the later draft's combined L4 category has been revised and remains pending codebook approval.

### Novelty verification and pilot examples

The proposed contribution is study-level cross-coding of algorithmic functions, worker-experienced exposure units and time windows, measurement, pathways, OSH outcomes, and evaluated controls. Whether this adds a distinct evidence map remains a **positioning hypothesis** until the completed search and full-text comparison with adjacent reviews support it.

- Count Chen's 167-paper review as **one review**. Do not infer a classification of worker responses from its abstract; preserve the meaning of *complementary* as complementarity.
- Compare Bowdler, Matilla-Santander, Wei's conference abstract, Bao, and Jetha's distinct safety-tool review and living-review protocol. If Wei's completed full report becomes available, compare its tables directly. Keep conference abstracts and protocols identifiable as such.
- Use AMQ (three gig-worker samples, 1,332 participants, 20 items, five dimensions) and COMAMA (six samples including conventional employees, 1,005 participants, 11 items) as provisional RQ2 training examples of perceived-exposure scales. Verify their details and source locations against full text and distinguish them from event logs and experimental manipulations.
- Use the logistics cross-sectional accident/pain associations to practice recording design and confounding limitations under RQ3b. Use Bao's HRC review to practice distinguishing allocation optimization from worker OSH outcome evidence. These examples are training and comparison sources, not automatic inclusions.

## Start here

1. The PI confirms funding, hours, training and names/GitHub handles in [`tracking/assignments.csv`](tracking/assignments.csv). Reviewers must be different, paid non-authors who do not develop hypotheses or interpret final results. Name the adjudication role; the source assigns unresolved cases to Nam/Staley, with any additional separate adjudicator optional.
2. The PI and search lead review the [`collection criteria`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md), sign [`collection decisions`](tracking/collection_decisions.csv), resolve [`search-log`](tracking/search_log.csv) gaps, obtain PRESS review before final queries, and register the protocol/reliability plan or amendments before formal screening.
3. The data steward prepares **separate** reviewer files from the frozen queue. Each reviewer receives only their own file and the English [`SOP`](docs/SCREENING_AND_EXTRACTION_SOP.md). Use the mixed training pool and competency check, then two disjoint random 25-record calibration rounds. Full-text review has a separate 10–15-report calibration gate.
4. Assign four analytical owner roles, RQ1_LEAD through RQ4_LEAD, using the [RQ assignment table](tracking/rq_assignments.csv). After independent coding, adjudication and the approved evidence freeze, each lead analyzes agreed studies in their own RQ directory. One study may feed several RQs; the G12/G3/G4 bundles remain coordination aids.
5. Update [`tracking/tasks.csv`](tracking/tasks.csv) weekly. Each task has a completion gate and an evidence location. The first-week checklist is in [`docs/WEEK_ONE.md`](docs/WEEK_ONE.md).

## Work allocation

| Analytical lead / proposed branch | RQ | Handoff product |
|---|---|---|
| RQ1_LEAD / `analysis/rq1-exposure` | RQ1: function, work condition, exposure definition | Function-to-exposure taxonomy; [RQ1 kit](analysis/rq1/README.md) |
| RQ2_LEAD / `analysis/rq2-measurement` | RQ2: exposure operationalization and measurement | Measurement matrix/framework; [RQ2 kit](analysis/rq2/README.md) |
| RQ3_LEAD / `analysis/rq3-pathways-outcomes` | Integrated RQ3: pathways, worker OSH outcomes, support and gaps | Linked map with distinct RQ3a/RQ3b fields; [RQ3 kit](analysis/rq3/README.md) |
| RQ4_LEAD / `analysis/rq4-controls` | RQ4: modifiable controls | Human control-evaluation matrix and separate proposals; [RQ4 kit](analysis/rq4/README.md) |

The RQ leads **do not screen separate keyword subsets**. Reviewer 1 and Reviewer 2 independently screen the same complete queue. Search terms organize retrieval and domain expertise; they do not define mutually exclusive study sets. Search QA, deduplication, eligibility decisions, full-text review, adjudication, and PRISMA counts are shared tasks. RQ1/RQ2 can be assigned to the same person if capacity permits, while keeping separate outputs and a different human PR reviewer. G12 denotes their joint coordination; G3/G4 denote current RQ3/RQ4.

### Roles, records, and decisions

| Role | Immediate responsibility | Record the work in |
|---|---|---|
| PI | Name the team, approve collection and eligibility rules, sign protocol changes, and approve reporting | [`tracking/assignments.csv`](tracking/assignments.csv), [`tracking/collection_decisions.csv`](tracking/collection_decisions.csv), [`tracking/protocol_amendments.csv`](tracking/protocol_amendments.csv) |
| Search lead | Verify exact database queries, dates, limits, hit counts, export gaps, and any search amendments | [`tracking/search_log.csv`](tracking/search_log.csv), [`tracking/tasks.csv`](tracking/tasks.csv) |
| Data steward | Preserve source provenance; manage provisional IDs, duplicate exceptions, abstract recovery, and versioned reviewer packets | [`docs/DATA_HANDOFF.md`](docs/DATA_HANDOFF.md), [`tracking/raw_export_manifest.csv`](tracking/raw_export_manifest.csv), [`tracking/tasks.csv`](tracking/tasks.csv) |
| Reviewer 1 and Reviewer 2 | Independently screen the **same full queue**, review full texts, and extract included-study evidence | Separate reviewer packets and [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md) |
| Adjudication role | Resolve unresolved decisions after coder discussion; confirm the source's Nam/Staley role or approved additional adjudicator | [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md), [`tracking/tasks.csv`](tracking/tasks.csv) |
| Four RQ leads | Check their RQ coverage, synthesize agreed extraction, cross-review and contribute to the measurement framework | [`tracking/rq_assignments.csv`](tracking/rq_assignments.csv), [`docs/TEAM_ASSIGNMENTS_AND_HANDOFFS.md`](docs/TEAM_ASSIGNMENTS_AND_HANDOFFS.md), [`analysis/`](analysis/) |

These are **roles awaiting named assignees**, not completed assignments. The editable task board gives each action an owner role, dependency, target date, acceptance criterion, and evidence path. Use [`tracking/weekly_progress.csv`](tracking/weekly_progress.csv) for weekly throughput and unresolved work.

### Procedure and automation

1. **Collection and search:** Confirm the proposed collection rules and actual database coverage in [`docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md). Reconcile each executed query against [`tracking/search_log.csv`](tracking/search_log.csv); proposed terms in the workstream guide are not completed searches.
2. **Data preparation:** Keep the original exports unchanged. Use the source manifest and [`docs/DATA_HANDOFF.md`](docs/DATA_HANDOFF.md) to audit counts, hashes, duplicates, missing abstracts, and packet versions. Local scripts in [`scripts/`](scripts/) support bundle auditing, pilot-manifest generation, and pre-upload checks.
3. **Screening and extraction:** Follow [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md) for the pilot, independent decisions, adjudication, full-text review, and source-located RQ extraction. Blank study and evidence-link tables are in [`templates/`](templates/).
4. **Analysis and reporting:** Four RQ leads use the same approved study-level evidence freeze for descriptive/relational matrices, evidence-density maps, narrative synthesis, and the measurement framework. RQ products are cross-reviewed and merged into `integration/evidence-map`, then reviewed for merger to `main`. Meta-analysis is not the primary plan and requires a separate compatibility assessment. Check adjacent reviews, reliability, and record/report/study denominators before final claims. Follow [`docs/GITHUB_WORKFLOW.md`](docs/GITHUB_WORKFLOW.md).

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

### Calibration, field tiers, and reliability

The original DOCX makes reliability a formal methodological result. Restore its project-specific targets: two fresh random 25-record title/abstract rounds with **agreement >=85% and Gwet's AC1 >=0.80**; **10–15 full-text reports** with **agreement >=90% and AC1 >=0.80**; Cohen's kappa also reported. Review substantive errors as well as targets. The mixed 93-record manifest is a training pool, separate from the random calibration sample.

Descriptive fields are extracted once and **100% verified** by the second reviewer. Core interpretive fields are **100% independently double-coded**. Compute reliability from pre-consensus decisions, including Krippendorff's alpha with 95% CIs and prespecified AC1/AC2 for imbalanced categories. The source target is **>=0.80**; **0.67–0.79** triggers refinement/independent recoding, and **<0.67** triggers reconsideration of categories. Freeze statistic, multi-label, CI and independent-unit rules before results; these are project targets, not universal JBI/PRISMA requirements. See [`tracking/reliability_plan.csv`](tracking/reliability_plan.csv) and the [`SOP`](docs/SCREENING_AND_EXTRACTION_SOP.md).

## Current corpus and limits

The local audit combined **56 exported files from five accessible databases**, yielding **10,858 exported rows**, **6,822 provisionally unique records**, and **6,592 records in the 2015–2026 screening queue**. These are file and processing counts, **not final PRISMA counts**. There are **3,034 records without an abstract**, **five same-title/conflicting-DOI groups**, and **nine of 43 priority references not linked by DOI**. Human screening and final RQ coding have **not started**. RQ keyword hints are overlapping, preliminary routing aids only.

The database exports available locally are from PubMed, Scopus, Web of Science Core Collection, IEEE Xplore, and ACM Digital Library. PsycINFO is an unfulfilled original recommendation; Embase and CINAHL were added in the later search plan. All three were inaccessible and must not be listed as completed searches. Document ACM's unique-coverage rationale and the broader discovery queries that omit worker/outcome blocks. Of 42 search-plan rows, 25 have exports and 17 do not; execution times are missing for all 25 and on-screen hit counts for 23. Resolve or explicitly report these gaps.

The screening queue contains **2,016 AM-only**, **13 AM/HRC-overlap**, and **4,563 HRC-only** retrieval records. These describe search provenance, not confirmed eligibility. HRC therefore accounts for much of the screening workload. The ACM source collection contributes 31 BibTeX files and 1,512 exported rows; all raw row counts can include repeated retrieval of the same study.

### Scope, eligibility, and reporting units

The working PCC covers human workers or people performing a credible work-task simulation; algorithmic/AI or adaptive systems that allocate/reallocate tasks, set pace or schedules, monitor, evaluate, reward/penalize, or otherwise change a worker-facing condition; and conventional, platform, or simulated work contexts. Core empirical studies must define, measure, or manipulate the relevant condition and report a worker response, OSH-related outcome, exposure-measurement property, or relevant human control evidence. Worker states/proximal indicators remain eligible and are coded by their role. Relevant HRC studies may qualify without the phrase *algorithmic management*. Reviews, theory, guidelines, and non-empirical/technical-only control proposals remain separate background/comparison sources.

Exclude robot-only collision, route, or throughput optimization without a human work condition or response; consumer/patient-only AI without a work-task analogue; general ethics commentary without the relevant empirical evidence; and macro employment forecasts without worker exposure. Missing abstracts are not an exclusion criterion. Apply the detailed rules and unresolved decisions in [`docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md).

Use **record** for search and screening, **report** for a full-text document, and **study** for the underlying investigation and main synthesis denominator. Link multiple reports of one study; retain each effect estimate's original analysis unit and repeated-measure structure. Multiple effects, events, shifts, or RQ contributions do not create additional independent studies.

Before formal screening, resolve and record the publication window/cutoff, language and source types, HRC boundary, study/report linkage, trained paid reviewers and funding/hours, named adjudication role, full-text retrieval procedure, and AI limits. Also sign off the four-RQ structure, PRESS plan, source reliability targets and field tiers, and the measurement-framework deliverable. The PI owns protocol/interpretation approval, the search lead owns query/provenance checks, and the data steward owns source/version integrity.

### RQ-by-RQ evidence readiness

The counts below map the frozen five-RQ candidate files to four current RQs through [`tracking/rq_crosswalk.csv`](tracking/rq_crosswalk.csv). They combine keyword and priority-source hints and are **not included-study counts**. Integrated RQ3 is a record-ID union: 1,831 + 1,944 − 817 shared = **2,958**. Abstract availability describes metadata completeness, not relevance or quality. Current counts and input hashes are in [`tracking/rq_candidate_readiness.csv`](tracking/rq_candidate_readiness.csv).

| RQ | Unscreened candidates | With an abstract | What is ready | Main work before synthesis |
|---|---:|---:|---|---|
| **RQ1 — function to work condition** | 5,079 | 3,198 | A broad routing pool across AM and HRC searches | Screen out unrelated robotics and distinguish algorithmic functions from measured changes in work conditions. |
| **RQ2 — exposure definition and measurement** | 1,105 | 940 | Dedicated measurement searches and candidate records | Extract exposure unit, time window, data source, and reliability/validity from full text. |
| **RQ3 — pathways and OSH evidence** | 2,958 | 2,325 | Union of legacy pathway and outcome pools | Audit dedicated pathway coverage; distinguish proposed/tested mechanisms, worker outcome roles, design, support, and gaps. |
| **RQ4 — modifiable controls** | 905 | 837 | Dedicated control searches and candidate records | Identify relevant empirical human evaluations and separate background proposals/technical simulations. |

**Readiness judgment:** Bibliographic organization supports search QA and training/calibration preparation; formal decisions follow the protocol gates. No record has a human eligibility decision/final RQ code and no extraction is agreed. RQ pools overlap; **3,237 records had multiple legacy five-RQ hints**, while **1,015 have none** and remain in the queue. That legacy overlap statistic is not a newly computed four-RQ overlap count. Do not add candidate pools or use them as PRISMA inclusion counts.

**Next gates:** reconcile search histories and PRESS/final-query decisions, including `S3_HRC` and pathway coverage; sign protocol/reliability decisions; resolve DOI conflicts and recover abstracts; train/competency-check two reviewers and complete the two random calibration rounds; then dual-screen and independently core-code the full eligible corpus. Track owners and evidence in [`tracking/tasks.csv`](tracking/tasks.csv) and [`docs/WEEK_ONE.md`](docs/WEEK_ONE.md).

## Schedule and completion gates

Dates are planning targets, not evidence that work has occurred. Named reviewers, search/export reconciliation, abstract recovery, and full-text access are the main current dependencies. Recalculate dates using observed pilot throughput and the actual staff calendar.

| Planned period | Work | Completion evidence |
|---|---|---|
| **12 October 2026** | Freeze/hash 56 source files; audit 10,858/6,822/6,592 provisional counts; start screen/export reconciliation | Frozen manifest, audit log, and discrepancy records. Bibliographic preparation is complete; search reconciliation remains pending. |
| **13–16 October 2026** | Recover abstracts; resolve DOI/export gaps; obtain PRESS review; confirm staffing/budget; prepare separate training/calibration IDs and approve/register protocol | Recovery provenance, PRESS comments/responses, final queries, protocol/reliability version and registration record. |
| **19–23 October 2026** | Train/competency-check reviewers; two random 25-record calibration rounds with revision between rounds | Pre-consensus agreement >=85% and AC1 >=0.80, supplementary kappa, resolved disagreement patterns, and frozen codebook. |
| **26 October 2026–15 January 2027, provisional** | Dual title/abstract screening of the full queue, weekly adjudication, abstract recovery, and parallel full-text retrieval | Two original decisions, final consensus/reason for every ID, and weekly throughput reports. |
| **18 January–26 February 2027, provisional** | Calibrate on 10–15 full texts; dual full-text assessment; study/report linkage; pilot charting on 10–20 studies and core RQ1–4 coding | Full-text calibration targets, exclusion reasons, crosswalk, descriptive verification, and two original core extractions with locators. |
| **1–26 March 2027, provisional** | RQ matrices, measurement framework, reliability results, appraisal/gap analyses, denominator QA, adjacent-review comparison, and drafting | PRISMA flow, search table, stage/field reliability table, evidence-density maps, measurement framework, and draft v1. |
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

The source's proposed program is **Paper 2 Delphi prioritization/content validity; Paper 3 allocation/reassignment × worker control; Paper 4 reassignment-frequency or pace-variability dose–response; Paper 5 control-feasibility/effect evaluation**. Paper 1 supplies measurable constructs and gaps. Its target strategy is Safety Science, with Journal of Safety Research as an alternative when injury prevention dominates; publication-route policies and journal requirements remain to be verified at submission.

The review is complete when:

1. The five accessible databases' queries, execution histories, source exports, discrepancies, and inaccessible-source limitations are traceable.
2. Duplicate adjudication, dual screening, full-text decisions, exclusion reasons, and any update-search records follow the documented procedure.
3. RQ1–4 tables and the measurement framework use study-level denominators with source locators; date/source-type/HRC sensitivity is documented. Pre-consensus reliability and recoding histories are reported by stage and core field.
4. Adjacent-review overlap has been checked, novelty matches the evidence, and the PRESS/JBI/PRISMA-ScR/PRISMA-S protocol and journal reporting requirements have been checked against actual work.

## Folder map

| Path | Purpose |
|---|---|
| [`docs/SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md`](docs/SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md) | Source DOCX strategy/methodology audit, four-RQ evaluation, and source locators |
| [`docs/WEEK_ONE.md`](docs/WEEK_ONE.md) | First-week sequence and decision gates |
| [`docs/WORKSTREAMS.md`](docs/WORKSTREAMS.md) | RQ questions, actual search terms, additional terms, and outputs |
| [`docs/SCREENING_AND_EXTRACTION_SOP.md`](docs/SCREENING_AND_EXTRACTION_SOP.md) | Eligibility, independent screening, adjudication, extraction, and evidence grading rules |
| [`docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md`](docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md) | Complete working collection criteria, database coverage, exclusions, and unresolved protocol decisions |
| [`docs/DATA_HANDOFF.md`](docs/DATA_HANDOFF.md) | Local data paths, reviewer packet delivery, and version checks |
| [`docs/LOCAL_SURVEY_BUNDLE.md`](docs/LOCAL_SURVEY_BUNDLE.md) | Inventory and handling rules for the 90-file local `data/` snapshot |
| [`docs/UPLOAD_CHECKLIST.md`](docs/UPLOAD_CHECKLIST.md) | English-only and collection-criteria checks before the user's later upload |
| [`docs/GITHUB_WORKFLOW.md`](docs/GITHUB_WORKFLOW.md) | Branches, issues, pull requests, and review rules |
| [`docs/PROJECT_STATUS_AND_REVIEW_PROTOCOL.md`](docs/PROJECT_STATUS_AND_REVIEW_PROTOCOL.md) | Shareable account of objectives, searches, period, criteria, actual progress and remaining gaps |
| [`docs/RESEARCH_STAGES_AND_BRANCHES.md`](docs/RESEARCH_STAGES_AND_BRANCHES.md) | S0-S8 methods, dependencies, automation and scientific merge gates |
| [`docs/TEAM_ASSIGNMENTS_AND_HANDOFFS.md`](docs/TEAM_ASSIGNMENTS_AND_HANDOFFS.md) | Shared-role responsibilities, four RQ owners, cross-review and handoff rules |
| [`tracking/stages.csv`](tracking/stages.csv), [`tracking/branch_plan.csv`](tracking/branch_plan.csv) | Editable stage and proposed branch plans |
| [`tracking/rq_assignments.csv`](tracking/rq_assignments.csv) | Four RQ owners, keywords, field scope, branch and product allocation |
| [`tracking/data_freezes.csv`](tracking/data_freezes.csv) | Current provisional metadata snapshot and pending agreed-analysis freeze |
| [`analysis/`](analysis/) | Four RQ starter kits, integrated-output guide and handoff template; no scientific results yet |
| [Issue template](.github/ISSUE_TEMPLATE/research_task.md), [PR template](.github/pull_request_template.md) | Task accountability, input version, scientific review and merge evidence |
| [`tracking/assignments.csv`](tracking/assignments.csv) | Names and GitHub handles to fill before work starts |
| [`tracking/tasks.csv`](tracking/tasks.csv) | Task owners, dates, status, dependencies, and acceptance gates |
| [`tracking/weekly_progress.csv`](tracking/weekly_progress.csv) | Weekly screening, extraction, and issue counts |
| [`tracking/workstream_keywords.csv`](tracking/workstream_keywords.csv) | Three editable keyword/search-ID bundles for assignment |
| [`tracking/pilot_record_ids.csv`](tracking/pilot_record_ids.csv) | Legacy-named 93-record mixed training pool; not the formal reliability sample |
| [`tracking/calibration_record_ids.csv`](tracking/calibration_record_ids.csv) | Two disjoint random 25-record calibration rounds; IDs only, no decisions |
| [`tracking/rq_crosswalk.csv`](tracking/rq_crosswalk.csv) | Five legacy questions mapped to four current questions and workstreams |
| [`tracking/rq_candidate_readiness.csv`](tracking/rq_candidate_readiness.csv) | Current routing counts and source hashes; RQ3 union removes overlap |
| [`tracking/reliability_plan.csv`](tracking/reliability_plan.csv) | Source calibration/core-coding statistics, targets, and field-tier rules |
| [`tracking/search_log.csv`](tracking/search_log.csv) | Snapshot of exact queries and execution gaps; verify against platforms |
| [`tracking/protocol_amendments.csv`](tracking/protocol_amendments.csv) | Dated record of approved search and eligibility changes |
| [`tracking/collection_decisions.csv`](tracking/collection_decisions.csv) | PI sign-off table for collection criteria that are not yet locked |
| [`tracking/raw_export_manifest.csv`](tracking/raw_export_manifest.csv) | English file names and SHA-256 hashes for the 56 raw exports |
| [`tracking/survey_snapshot_summary.json`](tracking/survey_snapshot_summary.json) | English-only summary of the local 90-file snapshot |
| [`templates/`](templates/) | Blank study registry, versioned RQ links, measurement framework, and reliability results |
| [`scripts/`](scripts/) | Bundle audit, mixed training pool, random calibration, RQ-readiness summary, and upload checks |

## Source of truth and upload boundary

The original records and processing scripts remain in the parent workspace's survey folder. A byte-identical 90-file copy of the selected survey contents is at `data/survey_2026-10-12/`; this local `data/` folder is excluded from Git. The user will handle any upload separately. See [`docs/LOCAL_SURVEY_BUNDLE.md`](docs/LOCAL_SURVEY_BUNDLE.md) before giving reviewers working copies. If eligibility or search decisions change, update the signed protocol and amendment log first; do not edit source exports or overwrite independent reviewer decisions.

The original DOCX and frozen survey snapshot retain their five-RQ numbering. Current documents/metadata use four RQs with a crosswalk; search queries and execution statuses are unchanged. This internal design comparison used scientific-agent procedural skills, disclosed and cited in the source-plan audit; it supplies no included-study decisions or review findings.

