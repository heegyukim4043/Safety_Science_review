"""Draw two disjoint random 25-record calibration batches from a frozen queue.

Only record IDs and source metadata are written. This script makes no eligibility
decision. The legacy mixed pilot manifest is a separate training pool.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import random
from pathlib import Path


FIELDS = ("record_id", "calibration_round", "position_in_round", "selection_rule",
          "random_seed", "source_queue_sha256")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--seed", type=int, default=20261012)
    parser.add_argument("--per-round", type=int, default=25)
    parser.add_argument("--exclude-manifest", type=Path,
                        help="Previously used training/calibration IDs to exclude for fresh rounds")
    parser.add_argument("--first-round", type=int, default=1)
    parser.add_argument("--overwrite", action="store_true",
                        help="Explicitly replace an unused manifest; prefer a new output for later rounds")
    args = parser.parse_args()
    if args.per_round < 1 or args.first_round < 1:
        parser.error("Round number and per-round count must be positive")
    root = Path(__file__).resolve().parents[1]
    queue = args.queue or root / "data/survey_2026-10-12/processed/screening_queue_2015_2026.csv"
    output = args.output or root / "tracking/calibration_record_ids.csv"
    if output.exists() and not args.overwrite:
        raise SystemExit("Output already exists. Use a new --output path; --overwrite is only for an unused manifest.")
    with queue.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["record_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate record IDs in source queue")
    excluded = set()
    if args.exclude_manifest:
        with args.exclude_manifest.open(encoding="utf-8-sig", newline="") as handle:
            excluded = {row["record_id"] for row in csv.DictReader(handle)}
    eligible_ids = sorted(set(ids) - excluded)
    if len(eligible_ids) < 2 * args.per_round:
        raise SystemExit("Too few fresh records for two disjoint rounds")
    selected = random.Random(args.seed).sample(eligible_ids, 2 * args.per_round)
    source_hash = hashlib.sha256(queue.read_bytes()).hexdigest()
    result = [{
        "record_id": record_id,
        "calibration_round": args.first_round + index // args.per_round,
        "position_in_round": 1 + index % args.per_round,
        "selection_rule": "uniform-random-without-replacement",
        "random_seed": args.seed, "source_queue_sha256": source_hash,
    } for index, record_id in enumerate(selected)]
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(result)
    print(f"Wrote two disjoint {args.per_round}-record rounds from {len(eligible_ids)} eligible queue IDs")
    print(f"Source SHA-256: {source_hash}")


if __name__ == "__main__":
    main()
