"""Summarize four-RQ routing hints without changing the frozen five-RQ inputs."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


MAPPING = {"RQ1": (1,), "RQ2": (2,), "RQ3": (3, 4), "RQ4": (5,)}
FIELDS = (
    "rq_version", "rq", "legacy_rqs", "candidate_records_not_screened",
    "with_abstract", "without_abstract", "legacy_overlap_removed",
    "human_eligibility_decisions", "agreed_rq_extractions", "source_sha256",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = args.source
    output = args.output or root / "tracking/rq_candidate_readiness.csv"
    old = {}
    hashes = {}
    for number in range(1, 6):
        path = source / f"RQ{number}_candidates_not_screened.csv"
        hashes[number] = hashlib.sha256(path.read_bytes()).hexdigest()
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len({row["record_id"] for row in rows}) != len(rows):
            raise SystemExit(f"Duplicate record IDs in {path.name}")
        if any(row["human_eligibility_status"] != "not_screened" or
               row["human_rq_coding_status"] != "not_coded" for row in rows):
            raise SystemExit("This routing-only summary cannot infer progress from populated decisions")
        old[number] = {row["record_id"]: row for row in rows}
    results = []
    for rq, numbers in MAPPING.items():
        merged = {}
        for number in numbers:
            for record_id, row in old[number].items():
                if record_id in merged and merged[record_id]["abstract_available"] != row["abstract_available"]:
                    raise SystemExit(f"Conflicting abstract flag for {record_id}")
                merged[record_id] = row
        available = sum(row["abstract_available"].lower() in {"1", "true", "yes"} for row in merged.values())
        results.append({
            "rq_version": "four_rq_v0.2", "rq": rq,
            "legacy_rqs": ";".join(f"RQ{number}" for number in numbers),
            "candidate_records_not_screened": len(merged),
            "with_abstract": available, "without_abstract": len(merged) - available,
            "legacy_overlap_removed": sum(len(old[number]) for number in numbers) - len(merged),
            "human_eligibility_decisions": 0, "agreed_rq_extractions": 0,
            "source_sha256": ";".join(f"RQ{number}:{hashes[number]}" for number in numbers),
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(results)
    for row in results:
        print(f"{row['rq']}: {row['candidate_records_not_screened']} unscreened; {row['with_abstract']} with abstracts")


if __name__ == "__main__":
    main()
