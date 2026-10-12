# RQ workstreams and keyword allocation

**Core question:** Which algorithmic functions change workers' actual work conditions, how are those conditions measured, through which pathways are they related to OSH outcomes, and which controls have been evaluated?

Every stream uses the shared concept blocks: `"algorithmic management"`, `"algorithmic control"`, `"algorithmic scheduling"`, `"human-robot collaboration"`, `"human-robot interaction"`, and `"adaptive automation"` where supported by each database. The exact field tags, syntax, limits, and dates are in [`../tracking/search_log.csv`](../tracking/search_log.csv). A term listed below as **additional** is a proposal for a documented search amendment or a full-text coding prompt; it was **not an executed search** merely because it appears here.

| Workstream | Questions and analytical owner | Distinct terms in exported queries | Exported search IDs most relevant to the stream | Additional terms: not yet searched as a dedicated expansion | Required handoff |
|---|---|---|---|---|---|
| **G12 — RQ1 and RQ2** | RQ1: which algorithmic decisions change what work condition? RQ2: how is exposure operationalized and over what unit/time window? | `task allocation`; `task assignment`; `work pacing`; `algorithmic scheduling`; `exposure`; `measur*`; `questionnaire`; `scale`; `log*`; `sensor*` | Common AM/HRC: `P1_AM`, `P3_HRC`, `S1_AM`, `S1B_AM_EXPAND`, `W1_AM`, `W3_HRC`, `I1_HRC`, `I2_ALLOC`, `I3_AM`, `A1_AM`, `A3_HRC`. Measurement: `P5_MEASURE`, `S5_MEASURE`, `W5_MEASURE`. | `monitoring`; `reassignment frequency`; `advance notice`; `pace variability`; `validation`; `reliability`; `recall period` | A study-level function → changed work condition → exposure unit/time window/measure/source table. Separate perceived exposure from event logs and experimental manipulations. |
| **G34 — RQ3 and RQ4** | RQ3: which psychosocial, cognitive, ergonomic, or physical pathways are proposed or tested? RQ4: which worker OSH outcomes are measured and how? | `stress`; `fatigue`; `workload`; `ergonom*`; `psychosocial risk`; `health`; `safety`; `injur*`; `accident*`; `burnout`; `musculoskeletal` | OSH: `P2_OSH`, `S2_OSH`, `W2_OSH`. HRC with workload/worker terms: `P3_HRC`, `W3_HRC`, `I1_HRC`, `A3_HRC`. Also inspect common AM retrieval. | `autonomy`; `time pressure`; `goal conflict`; `cognitive load`; `physical load`; `near miss`; `sleep`; `incident` | A proposed-versus-tested pathway table and an OSH outcome table with design, temporal order, comparison, estimate, unit, and confounding notes. **No dedicated RQ3 pathway query has been exported.** |
| **G5 — RQ5** | Which controls were proposed, implemented, simulated, tested with people, or evaluated in the field? | `intervention*`; `redesign`; `participat*`; `consultation`; `transparency`; `contestab*`; `mitigation`; `explanation`; `human-in-the-loop` | `P6_CONTROL`, `S6_CONTROL`, `W6_CONTROL`, `I4_CONTROL`, `A2_CONTROL`, plus common AM/HRC retrieval. | `pace cap`; `reassignment limit`; `advance notice`; `worker override`; `human review`; `safety constraint` | A control ladder: proposal → simulation → human/lab evaluation → field evaluation of worker OSH outcomes. Record implementation fidelity and feasible variables for subsequent experiments separately. |

**Search-ID prefixes:** `P` PubMed, `S` Scopus, `W` Web of Science, `I` IEEE Xplore, `A` ACM Digital Library. Review-identification searches `P4_REVIEW`, `S4_REVIEW`, and `W4_REVIEW` support the adjacent-review comparison; they are not added to counts of primary studies. `S3_HRC` has a planned query but no export in the current corpus.

## How to divide work without losing studies

1. The information specialist owns syntax and completeness checks across **all** five databases. A workstream lead checks whether the concepts and known sentinel papers for their RQs are covered, then proposes any amendment to the PI.
2. Reviewer 1 and Reviewer 2 independently screen **all 6,592** records under one shared eligibility protocol. A record lacking an RQ keyword hint is still screened. Search hits and RQ-hint lists may overlap.
3. On included studies, both reviewers independently extract the relevant RQ fields and source location. The adjudicator resolves disagreement. G12, G34, and G5 analyze only the agreed extraction.
4. A study can contribute to multiple streams. Use `study_id` for denominators, `report_id` for multiple reports, and `record_id` for search and screening provenance. Never sum the three workstream candidate totals as if they were distinct studies.

Current **unscreened** keyword/seed candidate hints are RQ1 5,079; RQ2 1,105; RQ3 1,831; RQ4 1,944; RQ5 905. Another 1,015 queue records have no RQ hint. These are workload-routing signals, not inclusion decisions or final evidence counts.

## Shared methods and novelty checks

- Compare the draft to adjacent reviews, including Bowdler et al., Matilla-Santander et al., Bao et al., Chen et al., and the distinct Jetha review/protocol. Chen's 167-paper BERTopic review is **one review**, not two.
- Do not infer worker response categories from Chen's abstract. Its four archetypes should be described using source-verified wording; `complementary` means complementary, not automatically collaboration.
- For RQ5, do not describe a proposed control, simulation, or cross-sectional association as evidence of prevention effectiveness.
- The novelty claim is the cross-linking of algorithmic function, exposure unit/time window/measurement, pathway, worker OSH outcome, and evaluated control **if the completed search and adjacent-review comparison continue to support it**.
