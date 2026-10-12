# Screening and extraction SOP (pilot draft)

**Status:** Working version 0.2, 12 October 2026; four RQs and source-plan reliability design restored, PI sign-off pending. Train on mixed examples, then conduct two disjoint random 25-record calibration rounds before formal title/abstract screening. Freeze the definitions, reliability plan, and AI policy in the protocol. Amendments need a date, rationale, affected records, and re-review decision. See the [source-plan audit](SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md).

## 1. Review scope and units

The population is workers or humans simulating work tasks. The concept is an algorithmic/AI decision that creates, allocates, schedules, monitors, paces, evaluates, rewards, or otherwise changes an actual work condition; this includes relevant human–robot collaboration or adaptive automation. Contexts include conventional employment, platform/gig work, and work-like human experiments, coded separately. Retain original empirical studies that measure or manipulate the work condition and report at least one worker response, OSH outcome, measurement property, or control relevant to the RQs. The PI must freeze the final PCC, source-type policy, publication-year boundary, and any grey-literature policy in the registered protocol.

Use three distinct identifiers:

- `record_id`: one deduplicated search record for screening and PRISMA identification.
- `report_id`: one full-text publication/report.
- `study_id`: one underlying study; multiple reports can share the same study ID.

Do not treat multiple outcomes, events, or reports from one study as independent studies.

The current questions are RQ1 exposure characteristics, RQ2 measurement, RQ3 pathways and OSH evidence, and RQ4 controls. RQ3a (pathways) and RQ3b (outcomes/empirical support) are extraction subdomains within RQ3. Legacy RQ3/RQ4 map to current RQ3; legacy RQ5 maps to current RQ4. Use [`../tracking/rq_crosswalk.csv`](../tracking/rq_crosswalk.csv) for historical files. Worker states and proximal indicators remain eligible; distinguish their analytical role from injury/illness and technical safety metrics.

Independent reviewers apply the frozen codebook and do not develop hypotheses/frameworks or interpret final review results. The source names Nam and Staley as lead authors and unresolved-case adjudicators; confirm the named adjudication role in the assignment table. An additional independent adjudicator may be appointed but is not required by the source. Complete documented training, positive/negative/borderline examples, and a written competency check before calibration.

## 2. Title/abstract screening

Reviewer 1 and Reviewer 2 each receive a separate copy of the **same complete** queue. Each edits only `decision`, `exclusion_reason`, and `note` in their own file. Keep `record_id`, citation, abstract, database, and search ID columns unchanged. They should not see each other's decisions until both copies are locked.

Allowed `decision` values: `include`, `exclude`, `uncertain`. Blank means not yet screened. Every `exclude` requires one primary `exclusion_reason`. For uncertainty, use `uncertain` and a brief note. Missing abstract or missing RQ keyword hint is never an automatic exclusion. Advance `include` and `uncertain` records to full-text retrieval or adjudication under the frozen rule.

| Exclusion code | Use when | Boundary rule |
|---|---|---|
| `wrong_population` | Only consumers, patients, or students and no worker/work-task analogue | Keep healthcare workers performing work. |
| `no_algorithmic_work_condition` | No algorithmic decision changes or measures the worker's work condition | Keep algorithmic assignment, surveillance, pacing, or evaluation. |
| `no_worker_response_osh_control` | No worker response, OSH-related outcome, or relevant control | Keep workload, fatigue, autonomy, safety behavior, and exposure measurement studies for full assessment. |
| `technical_only` | Only robot trajectory, collision probability, throughput, or other technical metrics | Keep a human participant's workload, fatigue, safety, or work-condition data. |
| `non_empirical` | Review, conceptual paper, editorial, or guideline without original data | Record adjacent reviews separately for novelty and citation comparison. |
| `outside_date` | Publication year outside the protocol's locked window | Conflicting online/print year is `uncertain` for adjudication. |
| `duplicate_report` | A genuinely duplicate report has been confirmed | Prefer `uncertain` at title/abstract stage; link multiple reports at full text. |

Do not use an automated classifier, keyword match, or RQ hint to make final inclusion/exclusion decisions. AI may help identify formatting errors, possible duplicates, and reading order only.

## 3. Pilot, adjudication, and full text

The existing 93-record [`pilot_record_ids.csv`](../tracking/pilot_record_ids.csv) is a mixed **training pool** retained under its legacy filename. It is not the formal random reliability sample. The separate [`calibration_record_ids.csv`](../tracking/calibration_record_ids.csv) contains two disjoint random 25-record batches from the frozen queue. Its initial draw excludes the mixed training pool to keep training examples separate; record which examples are actually used. The script can exclude prior manifests and draw fresh rounds if further calibration is needed. Selection does not judge eligibility.

Round 1: independently assess 25 random records and preserve the original decisions. Calculate raw agreement, Gwet's AC1, and supplementary Cohen's kappa before reconciliation; classify disagreements as criterion ambiguity, terminology ambiguity, insufficient information, or coder error. Revise examples and retrain. Round 2: assess a new 25-record random sample independently. The source-plan target is **raw agreement >=85% and AC1 >=0.80**. If either is unmet, repeat calibration on fresh records. Meeting targets alone does not resolve substantive ambiguities. Keep training/calibration records in the full screening accounting; any prior judgments affected by a codebook change must be independently redone under the frozen version.

After calibration, two reviewers screen every record in the frozen queue. Resolve disagreements by discussion, then the named adjudication role for unresolved cases. Record the date and reason of each consensus decision. Retrieve full text for all `include` and `uncertain` records under the frozen rule. Before formal full-text review, independently calibrate on **10–15 reports**, including borderline cases; the source target is **raw agreement >=90% and AC1 >=0.80**, with kappa also reported. Both reviewers then independently assess every report. Record one primary full-text exclusion reason with a page or evidence locator. Use `full_text_unavailable` only after logging reasonable library, open-access, and authorized author-request attempts. If eligibility rules change, identify and re-screen affected prior records.

## 4. Independent extraction and synthesis

Use the source's two field tiers. **Descriptive fields** (year, country, sample size, setting, design) are extracted by one reviewer and verified against the source by the second for **100% of records** under the revised working plan. **Core interpretive fields** (function, exposure category/metric, pathway, outcome role/class, control category/evaluation) are independently double-coded for **100% of studies**. Preserve original core extractions, descriptive verification, and a separate consensus version. Record a page, table, figure, or passage locator for interpretive claims. Use `not_reported` for absent information and `not_applicable` for inapplicable items; do not turn unreported results into negative findings.

| RQ | Minimum extraction |
|---|---|
| RQ1 | Algorithmic function; changed work condition; exposure construct and unit; frequency, intensity/dose, duration, variability, authority, reversibility, predictability, monitoring/adaptation, notice, and worker control when reported. |
| RQ2 | Operational definition; self-report/log/observation/experimental manipulation; source and denominator; observation/recall window; measurement reliability, validity, and invariance when reported; measurable dose and manipulability. |
| RQ3a within RQ3 | Proposed/measured/tested cognitive, psychosocial, ergonomic, physical-safety, or organizational pathway; mediator measurement; mediation/experimental test; temporal order and alternatives. |
| RQ3b within RQ3 | Worker state/proximal indicator versus injury/illness; variable role, comparison, estimate, denominator, CI, dose–response evidence, confounding, reverse causation, and consequential evidence gaps. Link to RQ3a without assuming an unmeasured mechanism. |
| RQ4 | Empirically implemented/evaluated software/work-design control; evaluation level, comparison, implementation fidelity, worker response/OSH outcome, and effect uncertainty. Background proposals and technical simulations remain separate from core empirical studies. |

Analytical leads **G12, G3, and G4** receive the agreed study-level extraction. A study can provide outcome evidence without measuring a mechanism; code the missing mechanism rather than excluding the outcome evidence. The same variable (such as fatigue) may be a mediator in one study and an outcome in another; use `outcome_role` and a source locator. Association does not establish causation, and proposed mechanisms/controls do not establish effect. The primary synthesis is descriptive, relational, and narrative; meta-analysis requires separately documented compatibility of definitions, designs, units, and effect measures.

Appraise support by design, comparison, exposure/outcome measurement, temporal order, confounding, and uncertainty. Any formal appraisal tool or certainty framework must be selected for the relevant evidence type and prespecified; no universal study score, GRADE rating, or quality-based exclusion is currently established. Do not infer absence of effect from an empty evidence-map cell.

Use [`../templates/measurement_framework.csv`](../templates/measurement_framework.csv) to translate agreed extraction into candidate exposure definitions/metrics, feasibility, measurement gaps, and later Delphi/experimental questions. Preliminary source categories are starting prompts, not an imposed final taxonomy.

The optional `operationalization_level` is a proposed descriptive axis: L0 named, L1 defined, L2 indicator with unit/source/time window, L3 empirically quantified. It is not an eligibility/quality score. Record measurement reliability/validity and exposure–response support separately; they do not form a combined L4 rank. Approve this later-manuscript addition through collection decision C22 before use.

### Reliability plan and recoding rules

Calculate reliability from **original independent decisions before discussion, consensus, or adjudication**. Use the field/stage plan in [`../tracking/reliability_plan.csv`](../tracking/reliability_plan.csv) and save results in [`../templates/reliability_results.csv`](../templates/reliability_results.csv). Report actual denominators, missing codes, codebook version, statistic and CI method; a CI method must respect the study/report unit. Do not treat repeated effects or exposure links as independent reliability observations. Report multi-label fields with a prespecified category-wise or set-based rule rather than applying nominal alpha to unordered sets without a coding rule.

For core interpretive categories, the source prespecifies percent agreement and **Krippendorff's alpha with 95% CIs**, with Gwet's AC1/AC2 for highly imbalanced nominal/ordinal categories and kappa supplementary where appropriate. Specify the primary coefficient and imbalanced-category rule **before viewing reliability results**; never choose whichever statistic passes. The project target is **>=0.80**. A primary coefficient of **0.67–0.79** triggers refinement and independent recoding of affected fields; **<0.67** triggers reconsideration of the category structure before synthesis. These are project targets from the source plan, not universal reporting-guideline requirements.

Archive every codebook version with its rationale. If a core category changes, both reviewers independently recode all previously coded studies affected by the change. Report reliability as a methodological result with a dedicated stage/field table.

## 5. Reporting and weekly QA

Keep PRISMA identification at the record level, full-text review at the report level, and synthesis at the study level. Report database-specific search strings, dates, limits, exports, deduplication decisions, and unresolved discrepancies. Use PRISMA-ScR for the review and PRISMA-S for search reporting, as specified in the research plan.

Each week the data steward reports: records added/updated, abstracts missing/recovered, each reviewer's completed decisions, pairs completed, disagreements, full texts obtained, full-text exclusions by reason, consensus extractions by RQ, and pending issues. No RQ candidate-hint count may be labeled an included-study count.
