"""Audit the local survey snapshot against original files without changing either."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


DATA_DIRS = (
    "Scopus", "Pubmed", "WOS", "IEEE EXplore", "ACM", "processed", "organized"
)
RAW_DIRS = set(DATA_DIRS[:5])


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def discover_source(repo_root: Path) -> Path:
    matches = list(repo_root.parent.glob("*/survey"))
    if len(matches) != 1:
        raise SystemExit("Pass --source PATH: expected one sibling survey folder.")
    return matches[0]


def expected_paths(source: Path) -> set[Path]:
    paths = {file.relative_to(source) for file in source.iterdir() if file.is_file()}
    for directory in DATA_DIRS:
        child = source / directory
        if not child.is_dir():
            raise SystemExit(f"Missing source directory: {child}")
        paths.update(file.relative_to(source) for file in child.rglob("*") if file.is_file())
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument(
        "--manifest", type=Path, default=Path("data/local_survey_snapshot_manifest.csv")
    )
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    source = args.source or discover_source(repo_root)
    snapshot = args.snapshot or repo_root / "data/survey_2026-10-12"
    if not snapshot.is_dir():
        raise SystemExit(f"Missing local snapshot: {snapshot}")

    expected = expected_paths(source)
    actual = {file.relative_to(snapshot) for file in snapshot.rglob("*") if file.is_file()}
    if expected != actual:
        missing = sorted(str(x) for x in expected - actual)
        extra = sorted(str(x) for x in actual - expected)
        raise SystemExit(f"File-set mismatch; missing={missing}; extra={extra}")

    rows = []
    for relative in sorted(expected, key=lambda p: p.as_posix().casefold()):
        original = source / relative
        copied = snapshot / relative
        digest = sha256_file(original)
        if digest != sha256_file(copied):
            raise SystemExit(f"Hash mismatch: {relative}")
        rows.append({
            "relative_path": relative.as_posix(),
            "role": "raw_export" if relative.parts[0] in RAW_DIRS else "working_or_documentation",
            "bytes": original.stat().st_size,
            "sha256": digest,
        })

    with (source / "processed/source_file_manifest.csv").open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        listed = list(csv.DictReader(handle))
    if len(listed) != 56:
        raise SystemExit(f"Expected 56 listed raw exports, found {len(listed)}")
    by_path = {row["relative_path"]: row for row in rows}
    for item in listed:
        relative = item["source_file"].replace("\\", "/")
        if relative not in by_path or by_path[relative]["sha256"] != item["sha256"]:
            raise SystemExit(f"Raw export manifest mismatch: {relative}")

    manifest = args.manifest
    if not manifest.is_absolute():
        manifest = repo_root / manifest
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("relative_path", "role", "bytes", "sha256"))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Matched {len(rows)} files ({sum(x['bytes'] for x in rows)} bytes)")
    print("Verified all 56 raw exports against the existing source manifest")
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
