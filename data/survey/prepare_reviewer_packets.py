"""Create separate blank title/abstract screening packets from the locked queue.

Run after search reconciliation: python prepare_reviewer_packets.py
Refuses to overwrite packets so human decisions cannot be lost accidentally.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "processed" / "screening_queue_2015_2026.csv"
FIELDS = ["record_id", "title", "year", "doi_list", "abstract", "databases", "search_ids", "year_window_flag", "decision", "exclusion_reason", "note"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="processed/reviewer_packets", help="New output folder relative to survey, or absolute path; never overwrites")
    args = parser.parse_args()
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out
    if out.exists():
        raise RuntimeError(f"Packets already exist; choose a new versioned output folder: {out}")
    with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))
    ids = [row["record_id"] for row in records]
    if len(set(ids)) != len(ids):
        raise RuntimeError("Queue contains duplicate record_id values")
    out.mkdir(parents=True)
    for reviewer in ("reviewer_1", "reviewer_2"):
        with (out / f"{reviewer}.csv").open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            for record in records:
                writer.writerow({name: record.get(name, "") for name in FIELDS})
    manifest = {
        "source": str(SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "records_each": len(records),
        "reviewers": ["reviewer_1", "reviewer_2"],
        "allowed_decisions": ["include", "exclude", "uncertain"],
        "warning": "Distribute separately; do not inspect or merge decisions until both copies are locked.",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
