"""Select a reproducible, metadata-only mixed training pool from the local queue.

This script does not judge eligibility or write reviewer decisions. Run it from
the repository root or pass --queue explicitly after obtaining controlled data.
The legacy pilot filename is retained. Use build_calibration_manifest.py for
the separate random 25-record calibration rounds and reliability denominators.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


STREAMS = ("am_related_search_only", "hrc_search_only", "both_streams")
OUTPUT_FIELDS = (
    "record_id",
    "stream_hint_not_eligibility",
    "abstract_available",
    "selection_rule",
    "source_queue_sha256",
)


def discover_queue(repo_root: Path) -> Path:
    matches = list(repo_root.parent.glob("*/survey/processed/screening_queue_2015_2026.csv"))
    if len(matches) != 1:
        raise SystemExit(
            "Pass --queue PATH: expected exactly one sibling survey screening queue."
        )
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, help="Frozen screening queue CSV")
    parser.add_argument(
        "--output", type=Path, default=Path("tracking/pilot_record_ids.csv")
    )
    parser.add_argument("--seed", default="2026-10-12")
    parser.add_argument("--per-cell", type=int, default=20)
    args = parser.parse_args()
    if args.per_cell < 1:
        parser.error("--per-cell must be positive")

    repo_root = Path(__file__).resolve().parents[1]
    queue = args.queue or discover_queue(repo_root)
    source_hash = hashlib.sha256(queue.read_bytes()).hexdigest()
    with queue.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))

    ids = [row["record_id"] for row in records]
    if len(ids) != len(set(ids)):
        raise SystemExit("Queue has duplicate record_id values; stop and resolve first.")

    chosen = []
    for stream in STREAMS:
        for available in (True, False):
            cell = [
                row
                for row in records
                if row["stream_hint_not_eligibility"] == stream
                and bool(row["abstract"].strip()) == available
            ]
            cell.sort(
                key=lambda row: hashlib.sha256(
                    f"{args.seed}:{row['record_id']}".encode("utf-8")
                ).hexdigest()
            )
            for row in cell[: args.per_cell]:
                chosen.append(
                    {
                        "record_id": row["record_id"],
                        "stream_hint_not_eligibility": stream,
                        "abstract_available": str(available).lower(),
                        "selection_rule": f"sha256-rank:{args.seed}:first-{args.per_cell}-per-cell",
                        "source_queue_sha256": source_hash,
                    }
                )

    output = args.output
    if not output.is_absolute():
        output = repo_root / output
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(chosen)
    print(f"Wrote {len(chosen)} training-pool IDs to {output} from {len(records)} queue records")
    print(f"Source SHA-256: {source_hash}")


if __name__ == "__main__":
    main()
