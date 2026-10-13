# GitHub phase workflow

**Execution workflow v0.5.** The user uploads separately. This package creates no remote branches, settings, issues or assignments.

## Phase cycle

Use the [two-round branch diagram](../diagrams/paper1_rq_rounds_workflow.html) and [detailed phase playbook](PHASE_EXECUTION_PLAYBOOK.md), the [detailed phase guide](BRANCH_WORKFLOW_GUIDE.md) and [phase merge register](../tracking/phase_merge_plan.csv). Follow `approved main -> fresh phase branches -> reviewed PRs to main -> all phase gates accepted -> recorded main checkpoint -> next phase branches` for P1-P8. The [branch table](../tracking/branch_plan.csv) lists 26 planned branches, their owners, actions, scopes, reviewer roles and start/end checkpoints. Four RQs remain unchanged.

P1 covers S0-S1; P2 calibration; P3 title/abstract review; P4 full texts/linkage; P5 agreed coding/reliability/evidence freeze; P6 four RQ products; P7 synthesis/framework; P8 reporting/release. All phase PRs target `main`. P6A round-1 RQ branches target main/G6A; the midpoint review T34 records the accepted gate. Fresh P6B -r2 branches target main/G6; T39 records second evaluation. Create P7 only after accepted G6 contains all four final round-2 products.

## Before creating branches

1. PI confirms actual names/handles, distinct independent reviewers and funded hours in [assignments](../tracking/assignments.csv).
2. Open [task issues](../.github/ISSUE_TEMPLATE/research_task.md) from the [40-task board](../tracking/tasks.csv). Include task ID, phase, method stage, owner, base checkpoint, expected output, PR target and gate. Auxiliary work streams may use sub-issues under the same task ID.
3. Confirm the previous phase's status is approved and obtain its recorded immutable main commit. Initial G0 denotes the uploaded starting package; it is not a scientific approval.

After remote setup, example commands for the team (replace the placeholder with the actual recorded commit):

```bash
git fetch origin
git switch --detach <recorded-G5-main-commit>
git switch -c analysis/rq1-exposure
```

For P6B, create a fresh round-2 branch from **G6A** after the midpoint review:

```bash
git fetch origin
git switch --detach <recorded-G6A-main-commit>
git switch -c analysis/rq1-exposure-r2
```

For P7, use the recorded **G6** commit:

```bash
git fetch origin
git switch --detach <recorded-G6-main-commit>
git switch -c integration/evidence-map
```

Create all branches in a phase from the same approved baseline. Use the correct base even if main has received one PR from an incomplete later phase. Do not reuse an old merged work branch as the next phase's starting point.

## Review and promotion

Use the [PR template](../.github/pull_request_template.md) and [handoff template](../analysis/HANDOFF_TEMPLATE.md). Attach task IDs, phase/checkpoint, protocol/codebook/evidence versions, input hashes, source locators, commands, checks, denominators, missingness and scientific limitations. Another human reviews the work; if proposed roles share a person, PI names a substitute.

PRs can merge individually after their own checks. The gate remains pending until every required phase branch has an accepted PR, the phase's scientific conditions are met, and DATA has verified versions/counts. Record accepted main commit, evidence location, version/hash, approver and date in the phase register. A technical merge or branch name cannot approve a scientific gate.

The maintainer may create the proposed baseline tag at that accepted main commit, close phase issues and remove merged remote work branches. Tags are optional references, not evidence of completion. Only then fork the next phase.

RQ1/RQ2 and RQ3/RQ4 cross-review in both rounds. RQ3a/RQ3b stay under one RQ3 lead. P6A uses an approved G5 freeze; G6A accepts round-1 inventories and the signed action/analysis plan. P6B uses fresh branches from G6A with an approved common evidence version. Record G6A/G6 in the round-checkpoint register; update outer P6 after T39/G6. P7 joins the accepted round-2 outputs and builds the framework on G6. P8 verifies source claims, reporting and reproducibility on G7 before G8 release approval.

Scientific corrections return to ADJ/DATA, with an approved amendment/new freeze and reruns of affected outputs. A late correction reopens impacted gates; synchronizing code alone does not preserve scientific approval. Preserve earlier versions and decisions.

## Data and settings

Upload English docs, search strings, manifests, blank templates, code, diagrams and approved shareable outputs. Keep full texts and independent reviewer files in the agreed controlled storage. Both reviewers assess the same full queue; RQ keyword bundles divide analytical expertise, not eligibility records.

After upload the maintainer applies the available review/check settings for main. The coordination package does not configure repository protections. Labels may include P1-P8, S0-S8, RQ1-RQ4, needs-adjudication, blocked and ready-for-review. Dates/status change only with actual evidence, using [weekly progress](../tracking/weekly_progress.csv).

## Review-record branches and action tracking

PI owns review/rq-round1 (T34, G5 -> G6A) and review/rq-round2 (T39, G6A -> G6). These PRs record the scientific review and accepted commit after the four RQ product reviews; they do not replace those reviews. Use [round checkpoints](../tracking/rq_round_checkpoints.csv), [32 work items](../tracking/rq_round_workplan.csv), [review actions](../tracking/rq_review_actions.csv) and [review form](../templates/RQ_ROUND_REVIEW.md). Labels may include P6A, P6B, R1, R2, G6A and needs-midpoint-review. Four RQs can work in parallel within a round; round 2 waits for G6A.
