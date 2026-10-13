"""Check that the Git upload candidate is English-only and methodologically complete."""

from __future__ import annotations

import csv
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


TEXT_SUFFIXES = {".md", ".csv", ".json", ".py", ".txt", ".html"}
REQUIRED = {
    "collaboration/README.md",
    "collaboration/01_SURVEY_RESULTS_AND_PROCESS.md",
    "collaboration/02_RESEARCH_QUESTIONS.md",
    "collaboration/03_WORK_ALLOCATION_AND_PHASES.md",
    "collaboration/04_RESEARCH_PLAN_REVIEW.md",
    "tracking/collaborator_confirmations.csv",
    "templates/COLLABORATOR_REVIEW_RESPONSE.md",
    "docs/METHODOLOGY_AND_PHASE_CROSSWALK.md",
    "tracking/methodology_plan.csv",
    "templates/METHODS_COMPLIANCE_CHECK.md",
    "docs/PHASE_EXECUTION_PLAYBOOK.md",
    "tracking/rq_round_checkpoints.csv",
    "tracking/rq_round_workplan.csv",
    "tracking/rq_review_actions.csv",
    "templates/RQ_ROUND_REVIEW.md",
    "templates/rq_round1_inventory.csv",
    "templates/rq_round2_claims.csv",
    "diagrams/paper1_rq_rounds_workflow.json",
    "diagrams/paper1_rq_rounds_workflow.html",
    "diagrams/paper1_rq_rounds_workflow.receipt.json",
    "README.md",
    "docs/BRANCH_WORKFLOW_GUIDE.md",
    "diagrams/README.md",
    "templates/PHASE_CHECKPOINT.md",
    "docs/RESEARCH_PLAN.md",
    "docs/COLLECTION_AND_ELIGIBILITY_CRITERIA.md",
    "docs/SCREENING_AND_EXTRACTION_SOP.md",
    "docs/WORKSTREAMS.md",
    "tracking/collection_decisions.csv",
    "tracking/search_log.csv",
    "tracking/raw_export_manifest.csv",
    "docs/SOURCE_PLAN_COMPARISON_AND_RQ_REVISION.md",
    "tracking/rq_crosswalk.csv",
    "tracking/rq_candidate_readiness.csv",
    "tracking/calibration_record_ids.csv",
    "tracking/reliability_plan.csv",
    "templates/measurement_framework.csv",
    "templates/reliability_results.csv",
    "docs/PROJECT_STATUS_AND_REVIEW_PROTOCOL.md",
    "docs/RESEARCH_STAGES_AND_BRANCHES.md",
    "docs/TEAM_ASSIGNMENTS_AND_HANDOFFS.md",
    "tracking/rq_assignments.csv",
    "tracking/stages.csv",
    "tracking/branch_plan.csv",
    "tracking/phase_merge_plan.csv",
    "tracking/data_freezes.csv",
    "analysis/HANDOFF_TEMPLATE.md",
    "analysis/integrated/README.md",
    "analysis/rq1/README.md",
    "analysis/rq2/README.md",
    "analysis/rq3/README.md",
    "analysis/rq4/README.md",
    ".github/ISSUE_TEMPLATE/research_task.md",
    ".github/pull_request_template.md",
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--standalone", action="store_true",
                        help="Validate a prepared upload folder without requiring Git metadata")
    args = parser.parse_args()
    if args.standalone:
        tracked = sorted(path.relative_to(root) for path in root.rglob("*")
                         if path.is_file() and ".git" not in path.relative_to(root).parts
                         and "__pycache__" not in path.relative_to(root).parts)
    else:
        completed = subprocess.run(
            ["git", "-c", f"safe.directory={root.as_posix()}", "ls-files",
             "--cached", "--others", "--exclude-standard", "-z"],
            cwd=root,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        tracked = sorted({Path(item.decode("utf-8")) for item in completed.stdout.split(b"\0") if item})
    names = {path.as_posix() for path in tracked}
    historical = {"diagrams/paper1_branch_workflow.json", "diagrams/paper1_branch_workflow.html",
                                "diagrams/paper1_branch_workflow.visual-check.2048x1320.light.png"}
    missing = sorted(REQUIRED - names - (historical if args.standalone else set()))
    if missing:
        raise SystemExit(f"Missing release-candidate files: {missing}")
    bad_paths = [str(path) for path in tracked if path.parts[0] == "data" or re.search("[\uac00-\ud7a3]", str(path))]
    if bad_paths:
        raise SystemExit(f"Unexpected source data or non-English filenames: {bad_paths}")

    hangul = []
    broken_links = []
    bad_csv = []
    for relative in tracked:
        path = root / relative
        if not path.is_file():
            raise SystemExit(f"Tracked file missing from working tree: {relative}")
        if path.suffix in TEXT_SUFFIXES or path.name in {".gitignore", ".gitattributes"}:
            content = path.read_text(encoding="utf-8-sig")
            if re.search("[\uac00-\ud7a3]", content):
                hangul.append(str(relative))
            if path.suffix == ".md":
                for target in re.findall(r"\]\(([^)]+)\)", content):
                    if not target.startswith(("http://", "https://", "#")) and not (path.parent / target).exists():
                        broken_links.append((str(relative), target))
            if path.suffix == ".csv":
                with path.open(encoding="utf-8-sig", newline="") as handle:
                    rows = list(csv.reader(handle))
                if rows and any(len(row) != len(rows[0]) for row in rows):
                    bad_csv.append(str(relative))
    if hangul or broken_links or bad_csv:
        raise SystemExit(f"Hangul={hangul}; broken links={broken_links}; malformed CSV={bad_csv}")

    with (root / "tracking/search_log.csv").open(encoding="utf-8-sig", newline="") as handle:
        searches = list(csv.DictReader(handle))
    with (root / "tracking/raw_export_manifest.csv").open(encoding="utf-8-sig", newline="") as handle:
        raw = list(csv.DictReader(handle))
    summary = json.loads((root / "tracking/survey_snapshot_summary.json").read_text(encoding="utf-8"))
    if len(searches) != 42 or sum(row["execution_status"] == "export_present_not_screened" for row in searches) != 25:
        raise SystemExit("Search-log counts differ from the documented 42 planned / 25 exported rows")
    if len(raw) != 56 or summary["raw_export_files"] != 56:
        raise SystemExit("Raw export count differs from 56")

    def read_rows(relative: str) -> list:
        with (root / relative).open(encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    crosswalk = read_rows("tracking/rq_crosswalk.csv")
    mapping = {row["legacy_rq"]: row["current_rq"] for row in crosswalk}
    if len(crosswalk) != 5 or mapping != {"RQ1": "RQ1", "RQ2": "RQ2", "RQ3": "RQ3", "RQ4": "RQ3", "RQ5": "RQ4"}:
        raise SystemExit("Unexpected legacy-to-current RQ crosswalk")
    for row in searches:
        if row["rq_version"] != "four_rq_v0.2" or re.search(r"RQ5\b", row["rq"]):
            raise SystemExit(f"Stale current RQ mapping: {row['search_id']}")
        if not row["legacy_rq"]:
            raise SystemExit(f"Missing preserved legacy mapping: {row['search_id']}")
    readiness = read_rows("tracking/rq_candidate_readiness.csv")
    counts = {row["rq"]: (int(row["candidate_records_not_screened"]), int(row["with_abstract"])) for row in readiness}
    if len(readiness) != 4 or counts != {"RQ1": (5079, 3198), "RQ2": (1105, 940), "RQ3": (2958, 2325), "RQ4": (905, 837)}:
        raise SystemExit("Four-RQ snapshot counts do not match the documented union")
    tasks = read_rows("tracking/tasks.csv")
    if any(row["workstream"] in {"G34", "G5"} for row in tasks):
        raise SystemExit("Task board has a legacy workstream in the current column")
    roles = {row["role_id"] for row in read_rows("tracking/assignments.csv")}
    confirmation_rows = read_rows("tracking/collaborator_confirmations.csv")
    if len(confirmation_rows) != 16 or {row["confirmation_id"] for row in confirmation_rows} != {f"CR{i:02d}" for i in range(1, 17)}:
        raise SystemExit("Collaborator register must retain 16 unique CR01-CR16 confirmation items")
    criteria = {row["criterion_id"] for row in read_rows("tracking/collection_decisions.csv")}
    confirmation_groups = {"survey": range(1, 5), "rq": range(5, 9),
                           "allocation": range(9, 13), "plan": range(13, 17)}
    for row in confirmation_rows:
        group = row["section"]
        if group not in confirmation_groups or int(row["confirmation_id"][2:]) not in confirmation_groups[group]:
            raise SystemExit(f"Incorrect four-part review grouping: {row['confirmation_id']}")
        if row["accountable_role"] not in roles or set(row["requested_review_roles"].split(";")) - roles:
            raise SystemExit(f"Unknown collaborator confirmation role: {row['confirmation_id']}")
        if row["criterion_ids"] and set(row["criterion_ids"].split(";")) - criteria:
            raise SystemExit(f"Unknown referenced collection criterion: {row['confirmation_id']}")
        for relative in [row["review_material"], *row["canonical_records"].split(";")]:
            if relative not in names or not (root / relative).is_file():
                raise SystemExit(f"Missing review/canonical record: {relative}")
        if row["status"] not in {"pending", "in_review", "revision_requested", "confirmed"}:
            raise SystemExit(f"Unknown collaborator confirmation status: {row['confirmation_id']}")
        if row["status"] == "confirmed" and not all(row[key].strip() for key in ("response_evidence", "adopted_decision", "approved_by", "approved_at", "applied_version")):
            raise SystemExit(f"Confirmed item lacks response/decision/approval/version: {row['confirmation_id']}")
        if row["status"] != "confirmed" and any(row[key].strip() for key in ("approved_by", "approved_at")):
            raise SystemExit(f"Unconfirmed item cannot claim approval: {row['confirmation_id']}")
    method_rows = read_rows("tracking/methodology_plan.csv")
    expected_methods = {"JBI": "review_conduct", "PRISMA-ScR": "review_reporting",
                        "PRISMA-S": "search_reporting", "PRESS": "search_peer_review",
                        "OSF": "prospective_registration"}
    if len(method_rows) != 5 or {row["framework"]: row["role"] for row in method_rows} != expected_methods:
        raise SystemExit("Method register must contain the five distinct planned layers and roles")
    if len({row["method_id"] for row in method_rows}) != 5:
        raise SystemExit("Method identifiers must be unique")
    valid_method_phases = {"P1", "P2", "P3", "P4", "P5", "P6A", "P6B", "P7", "P8"}
    for row in method_rows:
        if row["primary_owner"] not in roles or set(row["contributing_roles"].split(";")) - roles:
            raise SystemExit(f"Unknown method owner/contributor: {row['framework']}")
        if not row["applicable_phases"] or set(row["applicable_phases"].split(";")) - valid_method_phases:
            raise SystemExit(f"Unknown method phase: {row['framework']}")
        if row["status"] not in {"planned", "in_progress", "completed"} or not row["planned_output_paths"] or not row["gate_checks"]:
            raise SystemExit(f"Missing or invalid method plan: {row['framework']}")
        if row["status"] == "completed" and not all(row[key].strip() for key in ("actual_evidence_reference", "actual_completion", "approved_by")):
            raise SystemExit(f"Method completion lacks actual evidence/date/approver: {row['framework']}")
        if row["status"] == "planned" and any(row[key].strip() for key in ("actual_completion", "approved_by")):
            raise SystemExit(f"Planned method cannot claim completion/approval: {row['framework']}")
    stage_rows = read_rows("tracking/stages.csv")
    stages = {row["stage_id"] for row in stage_rows}
    branch_rows = read_rows("tracking/branch_plan.csv")
    branches = {row["proposed_branch"]: row for row in branch_rows}
    rq_assignments = read_rows("tracking/rq_assignments.csv")
    if len(rq_assignments) != 4 or {row["rq"] for row in rq_assignments} != {"RQ1", "RQ2", "RQ3", "RQ4"}:
        raise SystemExit("Assignment plan must have exactly four current RQ rows")
    for row in rq_assignments:
        rq = row["rq"]
        if row["accountable_role"] != f"{rq}_LEAD" or row["accountable_role"] not in roles:
            raise SystemExit(f"Missing distinct accountable RQ role: {rq}")
        branch = branches.get(row["proposed_branch"])
        if not branch or branch["responsible_role"] != row["accountable_role"] or branch["pr_destination"] != "main" or branch["phase_id"] != "P6":
            raise SystemExit(f"Inconsistent RQ branch responsibility/destination: {rq}")
        round2 = branches.get(row["round2_branch"])
        if branch["execution_round"] != "R1" or not round2 or round2["responsible_role"] != row["accountable_role"] or round2["execution_round"] != "R2":
            raise SystemExit(f"Missing round-specific RQ responsibility: {rq}")
        if not (root / row["deliverable_directory"] / "README.md").is_file():
            raise SystemExit(f"Missing starter kit: {rq}")
        for reviewer in row["cross_review_roles"].split(";"):
            if reviewer not in roles:
                raise SystemExit(f"Unknown cross-review role: {reviewer}")
    if len(stages) != len(stage_rows) or stages != {f"S{i}" for i in range(9)}:
        raise SystemExit("Stage plan must define unique S0-S8 stages")
    task_by_id = {row["task_id"]: row for row in tasks}
    phase_rows = read_rows("tracking/phase_merge_plan.csv")
    phases = {row["phase_id"]: row for row in phase_rows}
    if len(phase_rows) != 8 or set(phases) != {f"P{i}" for i in range(1, 9)}:
        raise SystemExit("Phase plan must contain eight unique sequential phases")
    if len(branch_rows) != len(branches) or len(branches) != 26:
        raise SystemExit("Phase work plan must contain 26 unique branch names")
    round_rows = read_rows("tracking/rq_round_checkpoints.csv")
    rounds = {row["round_id"]: row for row in round_rows}
    if len(round_rows) != 2 or set(rounds) != {"R1", "R2"}:
        raise SystemExit("P6 must define two unique analytical rounds")
    for round_id, base, checkpoint in (("R1", "G5", "G6A"), ("R2", "G6A", "G6")):
        row = rounds[round_id]
        if (row["previous_checkpoint"], row["checkpoint_id"]) != (base, checkpoint):
            raise SystemExit(f"Incorrect round checkpoint chain: {round_id}")
        required = {b["proposed_branch"] for b in branch_rows if b["phase_id"] == "P6" and b["execution_round"] == round_id}
        expected_tasks = {t["task_id"] for t in tasks if t["phase_id"] == "P6" and t["execution_round"] == round_id}
        if len(required) != 5 or set(row["required_branches"].split(";")) != required or set(row["task_ids"].split(";")) != expected_tasks:
            raise SystemExit(f"Round needs four RQ branches and one review branch: {round_id}")
        if row["status"] == "approved":
            if not all(row[k] for k in ("actual_main_commit", "input_version_or_hash", "evidence_path", "approved_by", "approved_at")):
                raise SystemExit(f"Approved round lacks signed evidence: {round_id}")
            if any(task_by_id[t]["status"] != "complete" for t in expected_tasks):
                raise SystemExit(f"Approved round has incomplete tasks: {round_id}")
    if rounds["R1"]["status"] == "approved" and phases["P5"]["status"] != "approved":
        raise SystemExit("G6A cannot be approved before G5")
    if rounds["R2"]["status"] == "approved" and rounds["R1"]["status"] != "approved":
        raise SystemExit("G6 cannot be approved before G6A")
    if phases["P6"]["status"] == "approved" and (rounds["R2"]["status"] != "approved" or phases["P6"]["actual_main_commit"] != rounds["R2"]["actual_main_commit"]):
        raise SystemExit("Outer P6 approval must match accepted second evaluation G6")
    expected_stage_phase = {"S0": "P1", "S1": "P1", **{f"S{i}": f"P{i}" for i in range(2, 9)}}
    for number in range(1, 9):
        phase = phases[f"P{number}"]
        if phase["previous_checkpoint"] != f"G{number - 1}" or phase["checkpoint_id"] != f"G{number}":
            raise SystemExit("Phase checkpoints must follow G0 through G8")
        phase_branches = {row["proposed_branch"] for row in branch_rows if row["phase_id"] == phase["phase_id"]}
        if set(phase["required_branches"].split(";")) != phase_branches or not phase_branches:
            raise SystemExit(f"Phase branch gate mismatch: {phase['phase_id']}")
        expected_tasks = {row["task_id"] for row in tasks if row["phase_id"] == phase["phase_id"]}
        if set(phase["task_ids"].split(";")) != expected_tasks:
            raise SystemExit(f"Phase task gate mismatch: {phase['phase_id']}")
        if phase["status"] == "approved" and not all(phase[key] for key in ("actual_main_commit", "input_version_or_hash", "evidence_path", "approved_by", "approved_at")):
            raise SystemExit(f"Approved phase lacks checkpoint evidence: {phase['phase_id']}")
        for name in phase_branches:
            branch = branches[name]
            gate = rounds[branch["execution_round"]] if phase["phase_id"] == "P6" else phase
            if branch["pr_destination"] != "main" or branch["base_checkpoint"] != gate["previous_checkpoint"] or branch["destination_checkpoint"] != gate["checkpoint_id"]:
                raise SystemExit(f"Inconsistent phase branch base/destination: {name}")
    for task in tasks:
        if task["phase_id"] != expected_stage_phase[task["stage_id"]]:
            raise SystemExit(f"Task stage/phase mismatch: {task['task_id']}")
        phase = phases[task["phase_id"]]
        gate = rounds[task["execution_round"]] if task["phase_id"] == "P6" else phase
        if branches[task["proposed_branch"]]["phase_id"] != task["phase_id"] or task["base_checkpoint"] != gate["previous_checkpoint"] or task["destination_checkpoint"] != gate["checkpoint_id"] or task["pr_destination"] != "main":
            raise SystemExit(f"Task phase branch/checkpoint mismatch: {task['task_id']}")
        branch = branches[task["proposed_branch"]]
        if (task["base_checkpoint"], task["destination_checkpoint"], task["execution_round"]) != (branch["base_checkpoint"], branch["destination_checkpoint"], branch["execution_round"]):
            raise SystemExit(f"Task differs from its branch round: {task['task_id']}")
    if set(task_by_id) != {f"T{i:02d}" for i in range(40)}:
        raise SystemExit("Expected original T00-T33 plus T34-T39 two-round tasks")
    work_items = read_rows("tracking/rq_round_workplan.csv")
    if len(work_items) != 32 or len({w["work_item_id"] for w in work_items}) != 32:
        raise SystemExit("Expected 32 unique RQ round work items")
    for round_id in ("R1", "R2"):
        for rq in ("RQ1", "RQ2", "RQ3", "RQ4"):
            if sum(w["round_id"] == round_id and w["rq"] == rq for w in work_items) != 4:
                raise SystemExit(f"Each RQ needs four work items per round: {round_id}/{rq}")
    for w in work_items:
        task = task_by_id.get(w["parent_task_id"])
        branch = branches.get(w["branch"])
        if not task or not branch or task["workstream"] != w["rq"] or task["execution_round"] != w["round_id"] or task["proposed_branch"] != w["branch"] or branch["base_checkpoint"] != w["base_checkpoint"] or branch["destination_checkpoint"] != w["destination_checkpoint"]:
            raise SystemExit(f"Invalid work item task/round/branch: {w['work_item_id']}")
        if not w["acceptance_criterion"] or not w["output_path"] or w["owner_role"] not in roles:
            raise SystemExit(f"Missing work-item ownership/output/acceptance: {w['work_item_id']}")
        if rounds[w["round_id"]]["status"] == "approved" and (w["status"] != "complete" or not w["evidence_path"]):
            raise SystemExit(f"Approved round has incomplete work-item evidence: {w['work_item_id']}")
    actions = read_rows("tracking/rq_review_actions.csv")
    if len({a["action_id"] for a in actions}) != len(actions):
        raise SystemExit("Review action IDs must be unique")
    for a in actions:
        if not a["action_id"] or a["review_gate"] not in {"G6A", "G6"} or a["required_before_gate"] not in {"G6A", "G6"} or a["owner_role"] not in roles or a["blocking"] not in {"true", "false"}:
            raise SystemExit(f"Invalid review action gate/owner/blocking flag: {a['action_id']}")
        if a["status"] == "accepted" and not all(a[k] for k in ("resolution_evidence", "accepted_by", "accepted_at")):
            raise SystemExit(f"Accepted review action lacks evidence: {a['action_id']}")
        required_round = "R1" if a["required_before_gate"] == "G6A" else "R2"
        if a["blocking"] == "true" and rounds[required_round]["status"] == "approved" and a["status"] != "accepted":
            raise SystemExit(f"Approved gate has an unresolved blocking action: {a['action_id']}")
    if len(task_by_id) != len(tasks):
        raise SystemExit("Task IDs are not unique")
    stage_task_ids = []
    for row in stage_rows:
        for task_id in row["task_ids"].split(";"):
            stage_task_ids.append(task_id)
            if task_id not in task_by_id or task_by_id[task_id]["stage_id"] != row["stage_id"]:
                raise SystemExit(f"Stage/task disagreement: {task_id}")
    if len(stage_task_ids) != len(set(stage_task_ids)) or set(stage_task_ids) != set(task_by_id):
        raise SystemExit("Every task must occur in exactly one method stage")
    for row in tasks:
        if row["accountable_role"] not in roles or row["proposed_branch"] not in branches:
            raise SystemExit(f"Unknown accountable role or branch: {row['task_id']}")
        if not row["merge_gate"] or not row["evidence_path"]:
            raise SystemExit(f"Missing delivery gate/location: {row['task_id']}")
    visited, active = set(), set()
    def visit(task_id: str) -> None:
        if task_id in active:
            raise SystemExit(f"Cyclic task dependency: {task_id}")
        if task_id in visited:
            return
        if task_id not in task_by_id:
            raise SystemExit(f"Missing dependency: {task_id}")
        active.add(task_id)
        for dependency in task_by_id[task_id]["depends_on"].split(";"):
            if dependency and dependency != "none":
                visit(dependency)
        active.remove(task_id)
        visited.add(task_id)
    for task_id in task_by_id:
        visit(task_id)
    freezes = read_rows("tracking/data_freezes.csv")
    for row in freezes:
        if row["status"] == "provisional_not_eligibility_approved":
            artifact = root / row["artifact_path"]
            if not row["sha256"] or not row["record_count"]:
                raise SystemExit("Provisional metadata freeze needs its known hash/count")
            if artifact.exists() and hashlib.sha256(artifact.read_bytes()).hexdigest() != row["sha256"]:
                raise SystemExit("Source queue hash differs from provisional freeze")
        if row["freeze_type"] == "agreed_study_evidence" and row["status"] == "pending" and row["approved_by"]:
            raise SystemExit("Pending agreed-evidence freeze cannot claim approval")
    calibration = read_rows("tracking/calibration_record_ids.csv")
    if len(calibration) != 50 or len({row["record_id"] for row in calibration}) != 50:
        raise SystemExit("Calibration IDs must be 50 unique records")
    if any(sum(row["calibration_round"] == number for row in calibration) != 25 for number in ("1", "2")):
        raise SystemExit("Calibration must contain two disjoint 25-record rounds")
    training = read_rows("tracking/pilot_record_ids.csv")
    if {row["record_id"] for row in training} & {row["record_id"] for row in calibration}:
        raise SystemExit("Initial calibration overlaps the separate training pool")
    actual_tracked = b""
    if not args.standalone:
        actual_tracked = subprocess.run(
            ["git", "-c", f"safe.directory={root.as_posix()}", "ls-files", "data/"], cwd=root, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        ).stdout
    if actual_tracked.strip():
        raise SystemExit("Source data directory has tracked files")
    print(f"Upload candidate checked: {len(tracked)} tracked/untracked candidate files; English-only text and paths")
    print("Collection criteria present; 42 search rows; 25 exported; 56 raw hashes")
    print("Four-RQ crosswalk/counts and independent calibration manifests verified")
    print(f"Four accountable RQ owners; S0-S8; {len(tasks)} tasks with valid dependencies and branch/merge gates")
    print("Eight outer phase gates; 26 branches; G5 -> G6A -> G6 analytical rounds verified")
    print("32 RQ work items; T00-T39 dependencies and round-specific branch handoffs verified")
    print("Source data directory is absent from tracked files")
    print("Five methodology layers, phase/owner fields and evidence-backed completion fields verified")
    print("Four-part collaborator packet and 16 confirmation items verified; actual approvals require evidence")


if __name__ == "__main__":
    main()
