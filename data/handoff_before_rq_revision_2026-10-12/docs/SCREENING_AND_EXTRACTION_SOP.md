# Screening and extraction SOP (pilot draft)

**Status:** Version 0.1 for team training on 12 October 2026. The PI and two independent reviewers must pilot it on 50–100 mixed AM/HRC records, resolve ambiguities, and freeze version 1 before formal screening. Amendments need a date, rationale, affected records, and re-review decision.

## 1. Review scope and units

The population is workers or humans simulating work tasks. The concept is an algorithmic/AI decision that creates, allocates, schedules, monitors, paces, evaluates, rewards, or otherwise changes an actual work condition; this includes relevant human–robot collaboration or adaptive automation. Contexts include conventional employment, platform/gig work, and work-like human experiments, coded separately. Retain original empirical studies that measure or manipulate the work condition and report at least one worker response, OSH outcome, measurement property, or control relevant to the RQs. The PI must freeze the final PCC, source-type policy, publication-year boundary, and any grey-literature policy in the registered protocol.

Use three distinct identifiers:

- `record_id`: one deduplicated search record for screening and PRISMA identification.
- `report_id`: one full-text publication/report.
- `study_id`: one underlying study; multiple reports can share the same study ID.

Do not treat multiple outcomes, events, or reports from one study as independent studies.

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

Pilot 50–100 records spanning algorithmic management, HRC, abstract present/missing, and obvious/borderline cases. Both reviewers screen them independently. Before discussion, the data steward summarizes agreement and disagreement by exclusion reason. The adjudicator records the final decision and reason while preserving both original judgments. Revise the codebook with examples rather than imposing an arbitrary agreement threshold.

After the pilot, two reviewers screen every record in the frozen queue. Resolve disagreements by discussion or a named adjudicator. Record the date and reason of each consensus decision. Retrieve full text for all records meeting the agreed advancement rule; both reviewers independently assess eligibility again. Record one primary full-text exclusion reason with a page or evidence locator. Use `full_text_unavailable` only after logging reasonable library, open-access, and author-request attempts. If eligibility rules change, identify and re-screen affected prior records.

## 4. Independent extraction and synthesis

Both reviewers independently populate the study registry and RQ evidence-link table for each included study. Record a page, table, figure, or passage locator for interpretive claims. Preserve original extractions and a separate consensus version. Use `not_reported` when a relevant item is absent and `not_applicable` when it cannot apply; do not turn an unreported result into a negative finding.

| RQ | Minimum extraction |
|---|---|
| RQ1 | Algorithmic function; changed work condition; worker exposure unit (event/task/shift/worker); frequency, intensity, duration, variability, predictability, notice, and override rights when reported. |
| RQ2 | Operational exposure definition; self-report/log/observation/experimental manipulation; source and denominator; observation or recall window; reliability and validity when reported. |
| RQ3 | Proposed or measured psychosocial/cognitive/ergonomic pathway; whether mediation or experimental testing occurred; temporal order and alternative explanations. |
| RQ4 | Actual worker OSH outcome versus proxy; design, comparison, estimate, denominator, confidence interval when present; confounding and reverse-causation limits. |
| RQ5 | Control type; proposal, simulation, human/lab test, or field implementation; fidelity; whether worker OSH outcomes were actually evaluated. |

Analytical leads G12, G34, and G5 receive only the agreed study-level extraction. An exposure–outcome association is not automatically causal. A proposed mechanism is not a demonstrated mechanism. A control proposal is not evidence of preventive effect. Only consider meta-analysis for compatible definitions, designs, units, and effect measures; otherwise map and narratively synthesize the evidence.

## 5. Reporting and weekly QA

Keep PRISMA identification at the record level, full-text review at the report level, and synthesis at the study level. Report database-specific search strings, dates, limits, exports, deduplication decisions, and unresolved discrepancies. Use PRISMA-ScR for the review and PRISMA-S for search reporting, as specified in the research plan.

Each week the data steward reports: records added/updated, abstracts missing/recovered, each reviewer's completed decisions, pairs completed, disagreements, full texts obtained, full-text exclusions by reason, consensus extractions by RQ, and pending issues. No RQ candidate-hint count may be labeled an included-study count.
