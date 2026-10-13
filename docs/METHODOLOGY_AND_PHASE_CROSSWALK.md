# Five methodological layers: implementation and phase gates

**Working implementation plan | 12 October 2026 | Execution design v0.5.**

Paper 1 is a scoping review and evidence map. Its five layers cover review conduct, review reporting, search reporting, search peer review and prospective registration. The [research plan](RESEARCH_PLAN.md) defines the scientific design; the [phase playbook](PHASE_EXECUTION_PLAYBOOK.md) defines execution. This guide makes their methodological requirements reviewable at each gate.

**Current status:** prior discovery exports and a working search log exist. Protocol approval, independent PRESS review, OSF registration, human eligibility decisions, agreed extraction and completed reporting checklists are not documented as completed. Preparing this guide does not complete any of those activities. Record actual evidence in the [five-method register](../tracking/methodology_plan.csv).

## 1. Roles of the five layers

| Layer | Purpose and Paper 1 application | Primary owner; contributors | Phase and gate | Required evidence |
|---|---|---|---|---|
| **JBI scoping-review methodology** | Design and conduct the review: PCC, objectives/RQs, eligibility, protocol, study selection, data charting and synthesis. Apply the approved common procedure across all four RQs. | ADJ; PI, SEARCH, DATA, REV1/REV2 and RQ leads | P1-P7; scientific checks at G1-G7 | Approved protocol, selection/consensus records, study registry, source-linked charting/codebook, accepted RQ products and synthesis |
| **PRISMA-ScR** | Report the scoping review transparently: rationale, protocol, eligibility, sources, selection/charting methods, results, limitations and funding. The extension has 20 essential and two optional reporting items. | PI; ADJ, DATA and all RQ leads | Start records in P1; maintain P2-P7; finish at P8/G8 | Final checklist with manuscript/supplement locations, reconciled selection flow, study tables and limitations |
| **PRISMA-S** | Make the searches reproducible: database/platform, full strategy, dates, limits, supplementary methods, updates, deduplication and counts. The extension has 16 reporting items. | SEARCH; DATA and PI | P1 and any search update; final reporting P8/G8 | Complete search histories/log, coverage-gap decisions, export reconciliation, deduplication description and final item-location checklist |
| **PRESS** | Independently assess the planned electronic search strategy and document revisions before final/update execution. Review RQ-to-concept alignment, logic/proximity, controlled vocabulary, free-text coverage, syntax and limits. | SEARCH coordinates; an independent qualified search reviewer evaluates; PI approves responses | P1/G1; revisit after material search-strategy changes | Dated reviewed strategy, reviewer comments, author responses, revised version and final execution reference |
| **OSF preregistration** | Create a dated protocol record before formal screening and planned analytical work. Disclose earlier discovery searches; specify eligibility, search updates, coding/reliability, AI limits, synthesis and deviations. | PI; SEARCH, ADJ, DATA and RQ leads | P1/G1; amendments tracked throughout; reconcile at P8/G8 | Formal registration URL/identifier, registration date, registered protocol version, prior-work disclosure and amendment/deviation record |

These owners are role assignments awaiting named personnel. The independent PRESS reviewer is distinct from the search author. The Generalized Systematic Review registration template supports scoping reviews. An editable OSF project upload alone is not a formal OSF registration.

## 2. Apply the layers through the existing phases

| Phase | Intermediate research goal | Method application and evidence to inspect before the gate |
|---|---|---|
| **P1 -> G1: protocol/search preparation** | Establish an approved, reproducible review plan and defensible corpus preparation. | JBI: approve PCC, four RQs, eligibility and charting/synthesis plan. PRISMA-S: reconcile exact strategies, dates, filters, hits, exports and access/cap limitations. PRESS: complete independent review and responses before final/update queries. OSF: formally register the signed protocol with disclosure of existing searches. PRISMA-ScR: start the item-location record and reporting plan. |
| **P2 -> G2: calibration** | Confirm reviewers can apply common criteria consistently. | JBI implementation: independent training/calibration, disagreements and accepted SOP. PRISMA-ScR: preserve selection/charting procedure details. OSF: compare actual procedure with the registered plan; document approved changes. |
| **P3 -> G3: title/abstract screening** | Account for every approved queue record and agree advancement decisions. | JBI implementation: independent decisions, consensus/adjudication and completeness. PRISMA-ScR: retain flow counts and selection procedure. PRISMA-S: preserve duplicate/removal provenance. OSF: log departures from registered eligibility/selection rules. |
| **P4 -> G4: full-text eligibility** | Establish an agreed eligible-study registry with report linkage. | JBI implementation: full-text decisions and source-located reasons. PRISMA-ScR: reports sought, obtained, excluded and included; separate retrieval failure from eligibility exclusion. PRISMA-S: log any supplementary retrieval/search methods and dates. OSF: approve scope/search amendments before dependent work. |
| **P5 -> G5: charting and evidence freeze** | Produce a verified common dataset for the four RQ leads. | JBI implementation: charting/codebook, independent core coding, descriptive-field verification and consensus. PRISMA-ScR: capture data-item definitions and charting methods. OSF: check planned fields/reliability/AI procedure against actual use and record deviations. Freeze registry, codebook and source-linked evidence with hashes. |
| **P6A -> G6A: RQ round 1/midpoint** | Deliver four accepted inventories, classifications, descriptive matrices and missingness accounts. | JBI synthesis plan: use the same G5 evidence input for all RQs. PRISMA-ScR: preserve study characteristics, denominators and source locations for results. OSF: distinguish planned analyses from emerging proposals. Midpoint review records actions and an approved round-2 plan; it does not authorize undocumented protocol changes. |
| **P6B -> G6: RQ round 2/second evaluation** | Resolve actions and accept all four final analytical products. | JBI synthesis plan: make source-linked comparisons/maps with design and measurement limitations. PRISMA-ScR: document analytic choices, results and uncertainty. OSF: disclose analytical deviations and return eligibility/code/search changes through the shared amendment process. PRISMA-S/PRESS apply again if a material search update is required. |
| **P7 -> G7: integration** | Accept the integrated evidence map, measurement framework and manuscript draft. | JBI: integrate the four RQs with unique-study denominators. PRISMA-ScR: connect objectives, methods, results, limitations and conclusions. OSF: reconcile planned versus actual synthesis and label new proposals. SEARCH/DATA maintain PRISMA-S records if the corpus changes. |
| **P8 -> G8: reporting/release** | Deliver a reproducible, reviewed submission package. | Finish PRISMA-ScR and PRISMA-S checklists with exact manuscript/supplement locations. Audit final flow/counts, search gaps, JBI procedure description, PRESS review evidence and OSF registration/deviations. PI signs release only after evidence is linked and unresolved limitations are reported. |

The four RQ branches share these five layers. Their scientific products differ: RQ1 exposure taxonomy; RQ2 measurement matrix/framework; RQ3 pathways and worker OSH outcomes; RQ4 evaluated controls. They use one eligibility process and one approved evidence freeze. They do not run four unrelated review protocols.

## 3. P1 execution sequence and acceptance

1. **PI + ADJ:** approve PCC, four RQs, working publication period/cutoff, source types/languages, HRC boundaries, eligibility, study/report linkage and proposed synthesis. Resolve open decisions in the [collection decision register](../tracking/collection_decisions.csv); do not treat working filters as signed rules.
2. **SEARCH + DATA:** reconstruct existing strategies, actual execution dates/time zones, limits, screen hit counts, export counts/caps and inaccessible-source decisions in the [search log](../tracking/search_log.csv). Preserve originals; report unrecoverable information explicitly.
3. **SEARCH:** prepare the primary MEDLINE/PubMed strategy for independent PRESS review before final execution and database translation. If the actual source order differs because discovery exports already exist, document it. Check translated Scopus, WoS, IEEE and ACM syntax/field behavior and coverage.
4. **Independent search reviewer + SEARCH:** retain dated comments, responses and the revised strategy. PI reviews unresolved recommendations. Materially amended searches require renewed review appropriate to the changes; a routine analytical PR does not require a new PRESS review.
5. **PI:** formally register the agreed protocol before formal screening. State what was already searched/collected, what screening/extraction has occurred, how prior exports will be used and what updates remain. Record the actual registration date and version; never present earlier discovery work as prospectively registered.
6. **SEARCH:** execute the approved final/update strategy according to that plan and log actual results. DATA rebuilds and versions the queue as needed; PI accepts remaining gaps and G1 inputs. The protocol may specify use of prior exports instead of rerunning unchanged strategies, with a documented rationale and update decision.
7. **PI + SEARCH + ADJ:** initialize reporting item-location records. Use the [compliance evidence template](../templates/METHODS_COMPLIANCE_CHECK.md) for each layer. G1 requires actual protocol/PRESS/registration references, not the presence of this guide or a blank checklist.

## 4. Evidence storage and automation

Use English filenames in the shareable package. Planned directories below are created when actual documents become available; they are not completed artifacts.

- `methods/protocol/`: signed protocol and approved versions.
- `methods/press/`: reviewed query, independent comments, responses and revised query.
- `methods/registration/`: registration identifier/date, exact registered protocol and prior-work disclosure.
- `reporting/prisma_scr/`: item-location checklist, selection flow and supporting tables.
- `reporting/prisma_s/`: item-location checklist and complete search histories.
- [Protocol amendments](../tracking/protocol_amendments.csv): who changed what, why, when, impacted records/outputs and approval/version.

| Automate after schema approval | Human responsibility |
|---|---|
| Query/export inventories, hashes, missing-field alerts and hit/export reconciliation | Verify platform histories, access limits and whether differences are explained |
| Checklist item-location inventory and missing evidence alerts | Judge whether the manuscript actually reports each applicable item adequately |
| Counts and flow diagrams from agreed decision tables | Approve record/report/study linkage, exclusion reasons and final denominators |
| Protocol/codebook version and amendment comparisons | Approve substantive amendments and decide whether screening/coding/analyses must reopen |
| Register-field and artifact-reference checks via `scripts/check_upload_package.py` | Complete independent PRESS review, register on OSF and approve scientific gates |

The upload checker verifies coordination package structure and evidence fields. It cannot certify adherence, judge search quality, perform registration or approve a phase.

## 5. Project choices and completion rules

- Two RQ analysis rounds, GitHub branch/merge gates, paid non-author reviewers, 100% core double coding and numeric agreement/AC1 targets are **Paper 1 specifications**. Do not attribute all of them to the five frameworks.
- Formal critical appraisal is a protocol decision appropriate to the review objective/designs. No universal quality score, GRADE assessment or quality-based exclusion rule has been adopted. If appraisal is selected, prespecify its tool/use and report the actual process/results.
- Study-design, confounding, time-order, exposure/outcome measurement and comparator limitations are recorded regardless of a formal appraisal decision. An association does not establish causation; an exposure scale is not automatically validated in every occupation; a proposed control is not an evaluated effective control.
- A method-register row describes the whole layer's planned evidence. Record partial progress in `notes`. Set `status` to `completed` only when its required evidence has been reviewed; JBI and reporting-layer completion will extend to later phases. PRESS/registration evidence must already be available for G1 even while other layers are ongoing.
- For `completed`, enter an actual evidence reference, actual completion date and approving person. Updating those fields is a human evidence-backed action. A merge or automated package check alone does not establish completion.

## 6. Authoritative sources

- JBI: [current scoping-review chapter](https://jbi-global-wiki.refined.site/space/MANUAL/355862497/10.%2BScoping%2Breviews) and [methodology update notice](https://jbi.global/news/jbi-updates-its-scoping-review-methodology). Record the consulted chapter/version when freezing the protocol.
- Tricco et al. (2018): [official PRISMA-ScR extension](https://www.prisma-statement.org/scoping); [statement DOI](https://doi.org/10.7326/M18-0850).
- Rethlefsen et al. (2021): [official PRISMA-S extension](https://www.prisma-statement.org/prisma-search); [statement DOI](https://doi.org/10.1186/s13643-020-01542-z).
- McGowan et al. (2016): [PRESS guideline primary abstract](https://pubmed.ncbi.nlm.nih.gov/27005575/); [guideline DOI](https://doi.org/10.1016/j.jclinepi.2016.01.021).
- OSF: [registrations and preregistration guidance](https://help.osf.io/article/330-welcome-to-registrations); [Generalized Systematic Review template](https://doi.org/10.17605/OSF.IO/F8QD5).
