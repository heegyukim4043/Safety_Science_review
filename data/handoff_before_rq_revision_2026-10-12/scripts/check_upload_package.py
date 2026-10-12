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
}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        ["git", "-c", f"safe.directory={root.as_posix()}", "ls-files", "-z"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    tracked = [Path(item.decode("utf-8")) for item in completed.stdout.split(b"\0") if item]
    names = {path.as_posix() for path in tracked}
    missing = sorted(REQUIRED - names)
    if missing:
        raise SystemExit(f"Missing tracked release files: {missing}")
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
    print(f"Upload candidate checked: {len(tracked)} tracked files; English-only text and paths")
    print("Collection criteria present; 42 search rows; 25 exported; 56 raw hashes")
    print("Local data directory is absent from tracked files")


if __name__ == "__main__":
    main()
