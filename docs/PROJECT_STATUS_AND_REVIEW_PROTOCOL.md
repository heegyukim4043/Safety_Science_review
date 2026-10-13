# Paper 1: project status and working review protocol

**Shareable status: 12 October 2026. RQ version: `four_rq_v0.2`.** This document summarizes the supplied source plan, search log, export inventory, processing outputs, and working protocol. It can be shared with collaborators alongside this repository. Protocol approval, registration, eligibility screening, and scientific results remain pending. The [source-plan comparison](SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md) records the strategy/methodology changes from the original DOCX.

## 1. Research objective and intended contribution

**Working title:** *Algorithmic work conditions as occupational exposures: a scoping review of measurement, safety and health pathways, and controls*.

The objective is to identify how algorithmic decisions change worker-facing work conditions, determine how these conditions are defined and measured as exposures, map their proposed/tested pathways to occupational safety and health (OSH), and identify controls evaluated in human work contexts. The study-level connection is:

`algorithmic function -> experienced work condition/exposure -> measurement and time window -> pathway -> worker response/OSH outcome -> evaluated control`.

Conventional employment, platform/gig work, and human-robot collaboration (HRC) are distinct contexts. The proposed contribution is a linked exposure and measurement framework supported by an evidence map. A claim that no previous review provides this cross-analysis remains conditional on the completed search and full-text comparison with adjacent reviews. This project produces a review; later Delphi and experimental studies are separate research projects.

| Current RQ | Research question | Intended product | Analytical owner role |
|---|---|---|---|
| **RQ1: exposure characteristics** | Which algorithmic functions and worker-facing work characteristics have been studied as occupational exposures, and how are the exposure dimensions defined? | Function-to-exposure taxonomy with operational definitions | `RQ1_LEAD` |
| **RQ2: operationalization and measurement** | How have exposures been measured in terms of unit, dose/intensity, frequency, variability, time window, reversibility, and worker control, and what measurement properties and gaps are reported? | Measurement matrix and candidate measurement framework | `RQ2_LEAD` |
| **RQ3: pathways and OSH evidence** | Through which proposed or tested cognitive, psychosocial, ergonomic, physical-safety, or organizational pathways are exposures linked to worker OSH outcomes, with what empirical support, limitations, and evidence gaps? | Linked pathway/outcome/design/support and gap map | `RQ3_LEAD` |
| **RQ4: modifiable controls** | Which software/work-design controls have been empirically implemented or evaluated, at what evaluation level, and with what worker response or OSH outcomes? | Human control-evaluation matrix and separate future candidates | `RQ4_LEAD` |

Legacy RQ3 and RQ4 are combined as current RQ3, with **RQ3a pathway** and **RQ3b outcome/support** fields retained. Legacy RQ5 becomes current RQ4. Original source files retain their numbering; use the [crosswalk](../tracking/rq_crosswalk.csv). RQ3a/RQ3b are subdomains of one question. A study can contribute to several RQs.

## 2. What has actually been completed

| Activity | Documented current state | Evidence / interpretation |
|---|---|---|
| Database file collection | Exports exist for 25 of 42 planned search rows from five accessible databases | [Exact search log](../tracking/search_log.csv); 17 rows have no exports |
| Source preservation | 56 raw files inventoried and hashed | [Raw manifest](../tracking/raw_export_manifest.csv) |
| Normalization and provisional duplicate grouping | 10,858 retrieval rows grouped into 6,822 provisional unique records | 4,036 retrieval rows provisionally grouped as repeats; ambiguous matches still require review |
| Automated publication-year partition | 6,592 records fall within the working 2015-2026 queue; 230 provisional records are outside it | Queue preparation only; final period and online/print-year treatment remain unsigned |
| Preliminary RQ routing | Four-RQ candidate counts derived from frozen legacy hints | [Readiness table](../tracking/rq_candidate_readiness.csv); no scientific RQ codes |
| Training/calibration preparation | 93 mixed training IDs; 50 separate random calibration IDs in two disjoint rounds of 25 | [Training IDs](../tracking/pilot_record_ids.csv), [calibration IDs](../tracking/calibration_record_ids.csv); no training or reliability results |
| Collaboration design | English protocol/SOP, task board, four RQ assignment kits, and branch/merge plan prepared | Working documents; named assignees and GitHub setup still pending |
| Human title/abstract and full-text eligibility decisions | **0 documented completed decisions** | No agreed included-study set |
| Agreed study-level extraction, reliability results, and RQ findings | **0 documented completed extractions/results** | Blank templates and planned outputs only |
| PRESS review, protocol approval, OSF registration | **Not documented as completed** | [Decision table](../tracking/collection_decisions.csv) and [amendments](../tracking/protocol_amendments.csv) require PI sign-off |

These are processing checkpoints. Final PRISMA record/report/study counts must be generated after search QA, duplicate adjudication, independent screening, and report-to-study linkage. Current candidate pool sizes do not establish the amount or strength of eligible evidence.

## 3. Search strategy and collection coverage

The source strategy links algorithmic/HRC concepts with worker/work-context and OSH concepts. Supplied searches implement several retrieval families: broad AM/HRC discovery, OSH, exposure measurement, controls, and adjacent reviews. Some broad discovery queries omit worker/outcome blocks. Retain this as a documented retrieval choice and evaluate coverage during search peer review. **The exact original platform input strings, field tags, limits, exports, and execution gaps are preserved in [search_log.csv](../tracking/search_log.csv).** Compact keywords do not replace these strings.

| Database/platform | Search IDs with exports | Main collection families | Outstanding checks |
|---|---|---|---|
| PubMed | `P1_AM`, `P2_OSH`, `P3_HRC`, `P4_REVIEW`, `P5_MEASURE`, `P6_CONTROL` | AM; OSH; HRC; reviews; measurement; controls | Execution times and on-screen totals |
| Scopus | `S1_AM`, `S1B_AM_EXPAND`, `S2_OSH`, `S4_REVIEW`, `S5_MEASURE`, `S6_CONTROL` | AM/expanded AM; OSH; reviews; measurement; controls | 1,061 vs 1,050 and 107 vs 105 screen/export gaps; `S3_HRC` has no export |
| Web of Science Core Collection | `W1_AM`, `W2_OSH`, `W3_HRC`, `W4_REVIEW`, `W5_MEASURE`, `W6_CONTROL` | AM; OSH; HRC; reviews; measurement; controls | Execution times, collection/filter and total verification |
| IEEE Xplore | `I1_HRC`, `I2_ALLOC`, `I3_AM`, `I4_CONTROL` | HRC; allocation; AM; controls | Possible 1,000-record cap for `I1_HRC` |
| ACM Digital Library | `A1_AM`, `A2_CONTROL`, `A3_HRC` | AM; controls; HRC | Collection/range and screen-total verification; unique HCI coverage rationale |

PsycINFO was recommended in the original plan but unavailable. Embase and CINAHL were later planned expansions, also unavailable. The 17 unexported search rows include these sources, Scopus HRC, and supplementary Europe PMC/OpenAlex/Google Scholar discovery. None can be reported as a completed database search. No new database searches were performed while preparing this handoff.

### Target period: distinguish the three dates

- **Working publication-year window:** 2015-2026, used to prepare the existing queue.
- **Planned query cutoff:** many original strings specify 1 January 2015 through 2 October 2026; inspect each exact row for its limits.
- **Handoff/audit date:** 12 October 2026. This is not a verified database search execution date. All 25 exported searches lack a verified execution timestamp/timezone in the current log; 23 lack on-screen totals.

The PI/search lead must approve the rationale for the lower bound, final inclusive cutoff, online/print-year handling, and update-search plan before formal screening. An update requires a new search version, preserved export, amended provenance, and queue/ID crosswalk.

### RQ-specific keyword ownership

| RQ | Existing-query terms relevant to this RQ | Proposed additions / coding prompts, not dedicated completed expansions |
|---|---|---|
| RQ1 | `task allocation`, `task assignment`, `work pacing`, `algorithmic scheduling` | monitoring; reassignment frequency; advance notice; algorithmic authority |
| RQ2 | `exposure`, `measur*`, `questionnaire`, `scale`, `log*`, `sensor*` | validation; reliability; recall period; dose/intensity; reversibility; variability |
| RQ3 | `stress`, `fatigue`, `workload`, `ergonom*`, `psychosocial risk`, `health`, `safety`, `injur*`, `accident*`, `burnout`, `musculoskeletal` | autonomy; time pressure; goal conflict; cognitive load; near miss; organizational pathway; dose response |
| RQ4 | `intervention*`, `redesign`, `participat*`, `consultation`, `transparency`, `contestab*`, `mitigation`, `explanation`, `human-in-the-loop` | pace cap; reassignment limit; worker override; human review; safety constraint |

The [four-RQ assignment table](../tracking/rq_assignments.csv) maps these terms to owners and branches. Existing G12/G3/G4 keyword bundles remain contextual grouping aids. No dedicated RQ3 pathway query has an export. All RQ leads check coverage and submit proposed changes to the search lead; they do not independently change eligibility or run undocumented searches.

## 4. Inclusion and exclusion: what was applied versus planned

**Applied to the supplied files:** format normalization, provisional duplicate-candidate grouping, a working year-window partition, and preliminary keyword/priority-reference routing. These are automated preparation rules. **The scientific inclusion/exclusion criteria below have not yet been applied through completed independent human screening.**

| Dimension | Working inclusion criterion | Working core exclusion / separate-background treatment |
|---|---|---|
| Population | Human workers or people undertaking a credible work-task simulation; conventional, platform/gig and HRC settings coded separately | Consumer/patient-only AI without a work-task analogue |
| Concept | Algorithmic/AI/adaptive decisions that change worker-facing allocation, schedule/pace, monitoring, evaluation, reward/penalty, or control conditions | General AI use, ethics commentary or employment forecasts without relevant worker exposure |
| Evidence | Original empirical definition, measurement or manipulation of the condition, plus worker response, OSH-related outcome, measurement property, or relevant human control evidence | No relevant original empirical evidence; reviews/theory/protocols/guidelines retained separately for context/comparison |
| HRC | Human work-condition evidence can qualify without the phrase algorithmic management | Robot-only routing/collision/throughput optimization without relevant human evidence |
| Outcomes | Worker states/proximal indicators and injury/illness endpoints, with their actual study role explicitly coded | A keyword such as safety does not independently establish eligibility |
| Controls | Empirically implemented/evaluated software or work-design controls with relevant human work evidence | Proposals and technical-only simulations belong in a separate candidate/background table |
| Missing metadata | Missing abstract or absent RQ hint remains in the screening workflow | Neither is an automatic exclusion |
| Date, language, publication type | Final signed rules pending | No inferred language restriction; conference/preprint/grey-literature treatment and full-text-unavailable procedure require a decision |

The [full criteria](COLLECTION_AND_ELIGIBILITY_CRITERIA.md) and [decision table](../tracking/collection_decisions.csv) govern final rule approval. Record each full-text exclusion's principal reason. Preserve the record/report/study distinction: a retrieval record is not a report, and multiple reports or effects need not represent distinct studies.

## 5. Readiness and open limitations

| RQ | Overlapping unscreened candidate records | With abstracts | Agreed included studies / extraction |
|---|---:|---:|---|
| RQ1 | 5,079 | 3,198 | Not established |
| RQ2 | 1,105 | 940 | Not established |
| RQ3 | 2,958 | 2,325 | Not established |
| RQ4 | 905 | 837 | Not established |

Current RQ3 is a union of the two legacy pools: 1,831 + 1,944 - 817 shared IDs. Do not sum RQ pools. The overall queue includes 1,015 records without an RQ hint and 3,034 without abstracts. Retrieval provenance is AM-only 2,016, AM/HRC overlap 13, and HRC-only 4,563; it does not establish study eligibility. Five conflicting-DOI groups and nine of 43 priority references without DOI linkage await manual resolution.

The largest immediate needs are search provenance/export reconciliation, signed scope/cutoff decisions, named/funded independent reviewers, abstract/full-text recovery, and successful calibration. RQ3 needs pathway/outcome linkage; RQ4 needs empirical human evaluation to support any effectiveness claim. Candidate abundance is a workload signal.

## 6. Planned methodology and next action

Use the working JBI scoping-review design, PRISMA-ScR and PRISMA-S reporting architecture, independent PRESS review of final/update queries, and OSF preregistration. The source-method specifications are retained in the [SOP](SCREENING_AND_EXTRACTION_SOP.md): trained paid non-author coders; the same full queue for both reviewers; two separate random 25-record calibration rounds; separate 10-15-report full-text calibration; 100% independent double coding of core interpretive fields; 100% second-source verification of descriptive fields; and pre-consensus reliability with prespecified refinement/recoding rules. Formal appraisal tools remain a protocol decision. Meta-analysis is not the primary analysis plan.

Approved extraction supports descriptive matrices, study-level relational maps and narrative synthesis. Keep exposure operationalization, measurement validation, causal support, evidence density, and control-effectiveness claims distinct. AI/admin automation does not supply final eligibility decisions or scientific codes.

Start with the [research stages](RESEARCH_STAGES_AND_BRANCHES.md), [team allocation](TEAM_ASSIGNMENTS_AND_HANDOFFS.md), and [12-16 October launch checklist](WEEK_ONE.md). All names remain unassigned; the PI must enter actual people/handles and hours. Upload and branch creation will be performed separately by the user/team.
