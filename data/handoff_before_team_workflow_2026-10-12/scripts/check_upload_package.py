"""Check that the Git upload candidate is English-only and methodologically complete."""

from __future__ import annotations

import csv
import json
import re
import subprocess
from pathlib import Path


TEXT_SUFFIXES = {".md", ".csv", ".json", ".py", ".txt"}
REQUIRED = {
    "README.md",
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
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
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
    missing = sorted(REQUIRED - names)
    if missing:
        raise SystemExit(f"Missing release-candidate files: {missing}")
    bad_paths = [str(path) for path in tracked if path.parts[0] == "data" or re.search("[\uac00-\ud7a3]", str(path))]
    if bad_paths:
        raise SystemExit(f"Unexpected local data or non-English filenames: {bad_paths}")

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
    calibration = read_rows("tracking/calibration_record_ids.csv")
    if len(calibration) != 50 or len({row["record_id"] for row in calibration}) != 50:
        raise SystemExit("Calibration IDs must be 50 unique records")
    if any(sum(row["calibration_round"] == number for row in calibration) != 25 for number in ("1", "2")):
        raise SystemExit("Calibration must contain two disjoint 25-record rounds")
    training = read_rows("tracking/pilot_record_ids.csv")
    if {row["record_id"] for row in training} & {row["record_id"] for row in calibration}:
        raise SystemExit("Initial calibration overlaps the separate training pool")
    actual_tracked = subprocess.run(
        ["git", "ls-files", "data/"], cwd=root, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if actual_tracked.strip():
        raise SystemExit("Local data directory has tracked files")
    print(f"Upload candidate checked: {len(tracked)} tracked/untracked candidate files; English-only text and paths")
    print("Collection criteria present; 42 search rows; 25 exported; 56 raw hashes")
    print("Four-RQ crosswalk/counts and independent calibration manifests verified")
    print("Local data directory is absent from tracked files")


if __name__ == "__main__":
    main()
