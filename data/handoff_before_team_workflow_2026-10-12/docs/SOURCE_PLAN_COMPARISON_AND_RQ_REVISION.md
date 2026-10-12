# Source-plan comparison and four-question revision

**Audit date:** 12 October 2026. **Current working structure:** `four_rq_v0.2`.

This assessment compares `Algorithmic_Work_Exposure_Paper1_Research_Plan.docx` with the README, workstream guide, screening SOP, collection criteria, and task board as they stood immediately before this revision. The original DOCX remains unchanged outside this repository. Its SHA-256 is `df0e81f8e7640cc22c246842bd4f2b30dbd3cfb9c371f11c55cc3234e187b752`.

The parent manuscript skeleton `paper1_draft.md` was also checked. It already retained the descriptive/interpretive field tiers and core alpha/recoding targets in sections 3.5–3.6, but its selection section removed the title/abstract calibration threshold and made PRESS conditional on availability. The concern is therefore partly **inconsistency between the manuscript skeleton and implementation guidance**, not loss of every source specification across all files.

Source locators below use the DOCX's numbered sections. `P###` identifies the one-based top-level body paragraph in `word/document.xml`, counting empty paragraphs and excluding paragraphs inside tables. Tables are numbered in document order. These are audit locators, not Word page numbers. A local pre-revision package backup is retained under the Git-ignored `data/handoff_before_rq_revision_2026-10-12/` folder.

## 1. Strategy: what stayed aligned and what changed

The central purpose remains aligned: operationalize algorithmic work characteristics as measurable occupational exposures, connect them to worker responses and OSH outcomes, and identify modifiable controls. The later package added source integrity, search-gap auditing, exposure time windows, explicit record/report/study units, and reproducible task handoffs. These are useful implementation details.

Three strategic elements were underrepresented: the measurement framework as a final product, the explicit link to Delphi and the later NIOSH study sequence, and the original range of exposure properties and worker-response outcomes. Novelty wording became more conditional after adjacent-review checks; that is an improvement in claim discipline rather than a change of research topic.

| Topic and source locator | Original plan | Package before this revision | Assessment and current action |
|---|---|---|---|
| Purpose and R01 role: sections 1, 17; P006–007, P155–161 | Foundational review, operational exposure framework, and provenance for a future algorithmic-hygiene R01 | Evidence map and later experiments emphasized; Delphi/content-validity sequence less visible | Restore the measurement-framework deliverable and Paper 2–5 linkage; downstream studies remain proposals. |
| Exposure properties: sections 2, 5, 11; P009, P023–028, table 4 | Dose/frequency/variability, authority, reversibility, worker control, predictability, monitoring and adaptation | Unit/time window/notice/override emphasized; reversibility, authority, adaptation, and dose–response less explicit | Add explicit extraction fields and a measurement-framework template. Do not finalize a taxonomy before included-study coding. |
| Outcomes and pathways: section 5; P030–033, table 4 | Safety behavior, worker states, physical load, trust/reliance, and injury/illness when available; organizational pathways included | Actual worker OSH versus technical-only safety distinguished; organizational pathways and worker-state roles less explicit | Retain worker-state/proximal outcomes and organizational pathways. Code each variable's role rather than requiring clinical injury/illness. |
| Novelty: section 14; P145–147 | Conversion of dispersed constructs into an occupational-exposure framework | Explicit hypothesis pending adjacent-review comparison | Keep conditional wording. Four RQs are an organizational improvement, not evidence of novelty. |
| Synthesis: section 12; P126–134 | Descriptive/relational synthesis; exposure × outcome, measurement and control matrices; density heatmap; meta-analysis not primary | Similar matrices, but readiness/count management more prominent | State the descriptive primary plan and retain evidence density, measurement gaps, and dose–response candidates. |
| Journal strategy: section 15; P149–153 | Safety Science first; Journal of Safety Research alternative; check publication route/policies at submission | Largely absent from the handoff | Restore the source's target strategy as a proposal. No current ranking, fee, or policy verification is claimed. |

## 2. Methodology: consequential differences

| Topic and source locator | Original specification | Package before this revision | Consequence and revised working rule |
|---|---|---|---|
| Method architecture: section 6, table 2 | JBI + PRISMA-ScR + PRISMA-S + PRESS + OSF, including frozen reliability and AI plans | First three visible; PRESS and the full preregistration contents less explicit | Restore all five layers and add a PRESS task. None is reported as completed. |
| Database coverage: section 7; P045–051 | WoS, Scopus, PubMed/MEDLINE, PsycINFO, IEEE; ACM conditional on unique coverage | Actual exports from WoS, Scopus, PubMed, IEEE, ACM; no PsycINFO export; Embase/CINAHL also appear in the expanded plan | PsycINFO is an unfulfilled original recommendation. Embase/CINAHL are later expansions. Document inaccessible coverage and the ACM rationale; do not equate a file collection with the recommended complete search. |
| Query architecture: section 7; P052–053 | System concept + worker context + OSH/worker-state/risk; separate AM and HRC families allowed; PRESS before final search | Some AM queries use only the system concept; broad HRC retrieval is noisy; separate measurement/control searches added | Current searches are broader discovery retrieval. Audit recall and precision and use PRESS for final queries. Changing RQ labels does not itself rerun a search or justify retrospectively excluding records. |
| Coder independence: section 9; P072–088 | Paid non-author coders; no hypothesis/framework/final-interpretation role; training and competency check | Paid non-author reviewers retained, but competency checks and separation from framework interpretation incompletely documented | Restore training/competency and role separation. G12/G3/G4 leads synthesize evidence; independent coders apply the frozen definitions. |
| Title/abstract calibration: section 10.1; P092–097 | Random 25 records, revise, then new random 25; agreement >=85%, AC1 >=0.80; kappa also reported | One mixed 50–100-record pilot; 93-record stratified manifest; threshold explicitly discouraged | Restore two disjoint random rounds and original project targets. Keep the 93-record manifest as a training pool, not the formal random reliability sample. Review error patterns as well as numeric targets. |
| Full-text calibration: section 10.3; P105–110 | 10–15 articles; agreement >=90%, AC1 >=0.80; dual review; unresolved cases to Nam/Staley | Dual review retained; separate full-text calibration and targets omitted | Restore the full-text calibration gate and project targets. Name an adjudication role; an additional separate person is optional, not an original requirement. |
| Descriptive versus interpretive extraction: section 10.4, table 3 | Descriptive fields extracted once and verified; core interpretive fields 100% independently double-coded | Handoff duplicated every field; manuscript section 3.5 retained the source tiers | Align implementation with the manuscript/source: one extraction plus 100% second-person verification for descriptive fields; independent double coding for every core field. |
| Reliability as a result: section 10; P090, P113–118 | Pre-consensus statistics; alpha with 95% CI for core coding; AC1/AC2 for imbalanced categories; >=0.80 target; 0.67–0.79 refine/recode; <0.67 reconsider structure | Manuscript section 3.6 retained core targets, but the handoff SOP omitted detailed statistics/thresholds and a reliability-results template | Restore the implementation plan and blank results template. No statistics are calculated from blank files. These targets are source-plan choices, not universal JBI/PRISMA mandates. |
| Adjudication/governance: sections 10, 16; P110–123, table 5 | Coders discuss after independent decisions; unresolved cases to Nam/Staley; affected fields recoded after changes | Mandatory separate adjudicator and broader PI sign-off | Name the adjudication role, defaulting to the source's lead authors once confirmed. Preserve original judgments and independently recode affected records. |
| AI limits: section 8; P055–070 | Administrative support/prioritization; no final scientific classification, evidence statements, stopping rule, or AI-generated findings | Mostly consistent; automated summaries not always clearly distinguished from AI-created results | Deterministic calculations may summarize human-approved codes. Generative AI does not supply final codes, quotations, or findings. Record tool/version/input and human checks. |
| Controls and eligibility: sections 5, 11; P035–040, table 4 | Worker exposure/outcome relevance; evaluated controls are the question; technical-only papers excluded | Proposal/simulation levels listed, creating ambiguity about whether non-empirical controls enter the core | Core studies must have relevant original human work/exposure evidence. Keep relevant proposals/reviews or robot-only simulations separately; a label such as 'control' does not override eligibility. |
| Practical launch: section 18; P163–169 | Freeze before final search; hire coders and reserve training/coding budget; source notes funding uncertainty | Fixed schedule and unassigned roles; funding unresolved | Dates remain provisional. Confirm funding, availability, PRESS, protocol and calibration before formal work is claimed. |
| Operationalization ladder: later manuscript section 3.5; not specified in the original DOCX | Exposure metrics, measurement properties, and exposure–response support are distinct domains | Added L0–L4 ladder makes L4 either measurement properties or exposure–response evidence | Retain L0–L3 as a proposed measurement-description axis; chart validation and exposure–response support separately. Their combination is not a valid single rank of measurement quality. |

The most consequential implementation deviation was incomplete reliability guidance and its inconsistency with the source/manuscript. The broad discovery search and explicit source auditing are defensible operational adaptations if reported transparently. The source's asserted literature gaps remain hypotheses to verify through the completed review. The proposed operationalization ladder must keep measurement validation separate from evidence of exposure–response relationships.

## 3. Four RQs and the old-to-new crosswalk

The requested arrangement `1, 2, [3–4], 5` is implemented as four consecutively numbered questions. The original DOCX and frozen survey files retain their original numbering; use [`../tracking/rq_crosswalk.csv`](../tracking/rq_crosswalk.csv) whenever importing them.

| Current question | Source question(s) | Current wording | Required output |
|---|---|---|---|
| **RQ1: exposure characteristics** | Legacy RQ1 | Which algorithmic functions and worker-facing work characteristics have been studied as occupational exposures, and how are the exposure dimensions defined? | Function → work condition/exposure taxonomy with operational definitions and units. |
| **RQ2: operationalization and measurement** | Legacy RQ2 | How have these exposures been operationalized and measured in terms of unit, dose/intensity, frequency, variability, time window, reversibility, and worker control, and what measurement properties and gaps are reported? | Measurement matrix and candidate measurement framework. |
| **RQ3: pathways and OSH evidence** | Legacy RQ3 + RQ4 | Through which proposed or tested cognitive, psychosocial, ergonomic, physical-safety, or organizational pathways are algorithmic work exposures linked to worker OSH outcomes, what empirical support and limitations do these relationships have, and where are the evidence gaps? | Linked pathway/outcome/design evidence map and gap table. |
| **RQ4: modifiable controls** | Legacy RQ5 | Which software-design or work-design controls have been empirically implemented or evaluated, at what evaluation level, and with what worker response or OSH outcomes? | Control × evaluation level × outcome matrix; separate background proposals and follow-on candidates. |

RQ3 has two extraction subdomains, **RQ3a (pathways)** and **RQ3b (outcomes and exposure–outcome support)**. They are parts of one question, not additional headline RQs. Link them by `study_id`, `report_id`, exposure, outcome, and time window. A study may report an outcome association without measuring a mediator; retain the outcome evidence and code the pathway as unmeasured. Do not require a complete causal chain in every included study.

### Evaluation of the merger

| Criterion | Assessment | Safeguard |
|---|---|---|
| Conceptual coherence | Improved: pathway and outcome support describe the same exposure–response relationship | Keep exposure and outcome measures linked within each study. |
| Coverage of the original plan | Preserved across four questions | Retain organizational pathways, proxies/worker states, dose–response, and the original evidence-gap question. |
| Separation of constructs | RQ3 can become overloaded | Separate proposed/measured/tested mechanism, outcome role, design, temporal order, and causal-support fields. |
| Workload | Editorial simplification; screening remains unchanged | Both reviewers still screen the same full queue. RQ3a and RQ3b still require distinct coding. |
| Causal interpretation | No stronger inference is created by combining questions | Report association, mediator measurement, mediation analysis, experimental support, and intervention effect separately. |
| Novelty | Number of RQs does not change originality | Verify the integrated measurement/exposure–response/control map against adjacent reviews. |

**Recommendation:** adopt the four-question structure, with the separate RQ3a/RQ3b fields. Keep three analytical workstreams: **G12** for RQ1–2, **G3** for integrated RQ3, and **G4** for controls. The old workstream labels G34/G5 are legacy identifiers and do not imply that four separate people are required.

## 4. Candidate readiness after the merger

Counts are unscreened routing hints, not included-study counts. The new RQ3 is a union by `record_id`: 1,831 legacy RQ3 records + 1,944 legacy RQ4 records − 817 shared records = **2,958**, of which **2,325** have an abstract. Do not sum the two old pools.

| Current RQ | Unscreened candidates | With an abstract | Remaining gap |
|---|---:|---:|---|
| RQ1 | 5,079 | 3,198 | Broad robotics retrieval needs human eligibility assessment. |
| RQ2 | 1,105 | 940 | Full-text measurement properties and metric definitions are not yet extracted. |
| RQ3 | 2,958 | 2,325 | Dedicated pathway-query audit, mechanism/outcome roles, temporal ordering, and empirical support remain unresolved. |
| RQ4 | 905 | 837 | Relevant human evaluations must be distinguished from background proposals and technical simulations. |

See [`../tracking/rq_candidate_readiness.csv`](../tracking/rq_candidate_readiness.csv) and [`../scripts/build_rq_readiness.py`](../scripts/build_rq_readiness.py). The 6,592-record queue is unchanged, all RQ pools can overlap, and there are still no human eligibility decisions or agreed RQ extractions.

## 5. Implementation and approval status

The revised working structure is reflected in the README, SOP, workstream guide, collection criteria, assignments, tasks, weekly report schema, search-log RQ metadata, and extraction templates. Exact query strings and source exports are preserved. The search log retains `legacy_rq` alongside the current `rq`; frozen five-RQ candidate files remain historical inputs. There is no automatic relabeling of scientific evidence.

The working-document revision is logged in [`../tracking/protocol_amendments.csv`](../tracking/protocol_amendments.csv) as **draft revision; PI sign-off pending**. The user's requested organizational change is implemented, but it is not represented as a signed or registered protocol amendment. Reliability targets, descriptive-field verification, funding, search changes, and adjudication names remain explicit decisions in [`../tracking/collection_decisions.csv`](../tracking/collection_decisions.csv).

## 6. Measurement framework and follow-on program

For each candidate exposure, [`../templates/measurement_framework.csv`](../templates/measurement_framework.csv) captures a definition, observable/self-report/experimental measure, dose/unit/time window, reliability/validity evidence, context, feasibility of manipulation, control options, and source-linked gaps. This is a final scholarly deliverable, not merely a count of publications.

The source's follow-on sequence is retained as a proposal: Paper 2 Delphi prioritization/content validity; Paper 3 allocation/reassignment × worker control experiment; Paper 4 reassignment-frequency or work-pace-variability dose–response study; Paper 5 control-feasibility/effect evaluation. Paper 1 identifies feasible variables and evidence gaps; it does not establish the causal or preventive effects that those studies would test. The source favors Safety Science, with Journal of Safety Research as an alternative if injury prevention dominates; journal and publication-route policies are to be checked at submission.

## Methods-design assistance

The `experimental-design` and `scientific-critical-thinking` skills supported this internal comparison and the distinction between measurement, association, causal support, and independent units. This assistance did not produce source-paper eligibility decisions, interpretive codes, quotations, or review findings. It is separate from the included literature.

Kassis, T., Agarwal, V., He, Y., Patel, D., & Brueckner, A. M. (2026). *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents*. arXiv:2609.00065. [doi:10.48550/arXiv.2609.00065](https://doi.org/10.48550/arXiv.2609.00065). Current arXiv record checked on 12 October 2026; no publisher/journal reference was listed.
