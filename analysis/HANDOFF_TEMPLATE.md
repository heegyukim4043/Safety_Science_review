# RQ analysis handoff

Copy this template into your RQ directory when actual work starts. Fill verified values; the current package contains no completed eligible-study analyses.

- RQ / task ID:
- Accountable lead / contributors / cross-reviewer:
- PR / proposed branch:
- Protocol and codebook versions:
- Agreed evidence freeze ID / input paths / SHA-256 hashes:
- Shared baseline commit:
- Corpus/batch coverage / pending or omitted fields:
- Study denominator and context-specific denominators:
- Report / evidence-link / effect-estimate units and multiplicity rules:
- Source-located tables and narrative paths:
- Analysis commands / tool versions / outputs, if applicable:
- Verification performed and discrepancies resolved:
- Missingness / design / measurement / causal limitations:
- Cross-RQ join keys and issues requiring ADJ/DATA review:
- Protocol or data amendments affecting this output:
- Cross-review comments/responses and acceptance date:
- PI/integration decision:

Every numerical claim must be reproducible from agreed codes and its stated denominator. Every substantive evidence claim must retain a report/source locator. Reading-order hints are not evidence codes. Scientific disagreements return to adjudication and a versioned data correction before merging corrected analysis.

## Phase checkpoint handoff

Record phase ID, previous approved main checkpoint/commit, destination checkpoint, input version/hash and required phase reviews. Current routing follows the eight-phase guide: phase branches submit reviewed PRs to main; each next phase starts only after all required outputs and approvals establish the new checkpoint. P6 RQ products establish G6 before fresh P7 integration. Scientific decisions stay in controlled storage; a technical merge cannot approve them.

See the [phase work guide](../docs/BRANCH_WORKFLOW_GUIDE.md) and complete the checkpoint record before promotion.

## RQ round fields, when applicable

- Execution round: R1 / P6A or R2 / P6B
- Previous approved gate and main commit: G5 or G6A
- Destination: G6A midpoint or G6 second evaluation
- Work-item IDs and review-action IDs:
- Blocking actions resolved / accepted nonblocking limits:
- Four-RQ cross-review evidence and common input hash:

Use the [round checkpoint register](../tracking/rq_round_checkpoints.csv) for acceptance.
