"""Build read-only work lists from the Paper 1 provisional search corpus.

This script does not screen studies or assign final research questions. It only
joins search provenance, existing keyword hints, and the 43 prior seed sources.
Generated files are overwritten; files under organized/manual are never overwritten.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
import html
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEARCH = ROOT.parent / "paper1_search"
PROCESSED = ROOT / "processed"
GENERATED = ROOT / "organized" / "generated"
MANUAL = ROOT / "organized" / "manual"
GENERATED.mkdir(parents=True, exist_ok=True)
MANUAL.mkdir(parents=True, exist_ok=True)
RQS = ("RQ1", "RQ2", "RQ3", "RQ4", "RQ5")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_manual_once(path: Path, rows: list[dict], fields: list[str]) -> None:
    if not path.exists():
        write_csv(path, rows, fields)


def title_key(value: str) -> str:
    value = unicodedata.normalize("NFKC", html.unescape(value)).lower()
    return " ".join(re.findall(r"\w+", value, flags=re.UNICODE))


def joined(values: list[str]) -> str:
    return "; ".join(sorted({value for value in values if value}))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    paths = {
        "manifest": PROCESSED / "source_file_manifest.csv",
        "summary": PROCESSED / "processing_summary.json",
        "master": PROCESSED / "master_records.csv",
        "hits": PROCESSED / "source_hits.csv",
        "queue": PROCESSED / "screening_queue_2015_2026.csv",
        "conflicts": PROCESSED / "same_title_conflicting_doi.csv",
        "search_log": SEARCH / "site_search_list_2026-10-02.csv",
        "priority": SEARCH / "priority_source_crosswalk.csv",
        "priority_coverage": PROCESSED / "priority_source_coverage.csv",
    }
    manifest = read_csv(paths["manifest"])
    summary = json.loads(paths["summary"].read_text(encoding="utf-8"))
    master = read_csv(paths["master"])
    hits = read_csv(paths["hits"])
    queue = read_csv(paths["queue"])
    conflicts = read_csv(paths["conflicts"])
    search_log = read_csv(paths["search_log"])
    priority = read_csv(paths["priority"])
    coverage = read_csv(paths["priority_coverage"])

    assert len(manifest) == summary["source_files"]
    assert sum(int(row["exported_rows"]) for row in manifest) == len(hits) == summary["exported_rows"]
    assert len(master) == summary["provisional_unique_records"]
    assert len(queue) == summary["provisional_in_window_screening_queue"]
    assert len({row["record_id"] for row in master}) == len(master)
    assert len({row["record_id"] for row in queue}) == len(queue)
    assert len(priority) == len(coverage) == 43
    assert {row["source_id"] for row in priority} == {row["source_id"] for row in coverage}
    changed = [row["source_file"] for row in manifest if not (ROOT / row["source_file"]).exists() or sha256(ROOT / row["source_file"]) != row["sha256"]]
    if changed:
        raise RuntimeError(f"Raw file hashes changed: {changed[:10]}")

    # Search inventory: preserve unknown run times and screen counts as blanks.
    files_by_search: dict[str, list[dict]] = defaultdict(list)
    for row in manifest:
        files_by_search[row["search_id"]].append(row)
    search_rows = []
    for row in search_log:
        files = files_by_search[row["search_id"]]
        computed = sum(int(file["exported_rows"]) for file in files)
        issues = []
        if files and row["exported_n"] and int(row["exported_n"]) != computed:
            issues.append("export_count_mismatch")
        if row["execution_status"] == "export_present_not_screened" and not files:
            issues.append("export_file_missing")
        if files and not row["run_datetime_timezone"]:
            issues.append("run_datetime_missing")
        if files and not row["hits_shown"]:
            issues.append("screen_hit_count_missing")
        if not files:
            issues.append("no_local_export")
        search_rows.append({
            "site_database_platform": row["site_database_platform"],
            "search_id": row["search_id"],
            "search_group": row["search_group"],
            "rq_in_search_plan": row["rq"],
            "execution_status": row["execution_status"],
            "exact_query_or_history": row["exact_query_or_history"],
            "run_datetime_timezone": row["run_datetime_timezone"],
            "field_and_limits": row["field_and_limits"],
            "hits_shown": row["hits_shown"],
            "logged_exported_n": row["exported_n"],
            "computed_exported_n": computed if files else "",
            "file_count": len(files),
            "source_files": joined([file["source_file"] for file in files]),
            "issue_flags": joined(issues),
        })
    write_csv(GENERATED / "search_inventory.csv", search_rows, list(search_rows[0]))

    # Seed-paper linkage. Pilot RQ hints and current keyword hints remain distinct.
    master_by_id = {row["record_id"]: row for row in master}
    coverage_by_source = {row["source_id"]: row for row in coverage}
    priority_rows = []
    seeds_by_record: dict[str, list[dict]] = defaultdict(list)
    for seed in priority:
        match = coverage_by_source[seed["source_id"]]
        record = master_by_id.get(match["record_id"], {})
        hints = [rq for rq in RQS if seed[f"{rq.lower()}_hint"] == "1"]
        priority_rows.append({
            "source_id": seed["source_id"],
            "seed_label": seed["label"],
            "source_type": seed["source_type"],
            "seed_doi": seed["doi"],
            "seed_rq_hints_not_final": joined(hints),
            "local_match_status": match["local_match_status"],
            "record_id": match["record_id"],
            "local_title": record.get("title", ""),
            "local_year": record.get("primary_year", ""),
            "local_databases": record.get("databases", ""),
            "local_abstract_available": record.get("abstract_available", ""),
            "keyword_rq_hints_not_final": record.get("rq_keyword_hints_not_screening", ""),
            "next_step": "human_verify_match_and_scope" if match["record_id"] else "manual_title_author_year_lookup",
        })
        if match["record_id"]:
            seeds_by_record[match["record_id"]].append(seed)
    write_csv(GENERATED / "priority_43_linkage.csv", priority_rows, list(priority_rows[0]))

    # One record-level candidate index, with both signal types marked explicitly.
    candidate_rows = []
    rq_lists = {rq: [] for rq in RQS}
    unassigned = []
    for record in queue:
        keywords = set(record["rq_keyword_hints_not_screening"].split("; ")) & set(RQS)
        seeds = seeds_by_record.get(record["record_id"], [])
        seed_hints = {rq for seed in seeds for rq in RQS if seed[f"{rq.lower()}_hint"] == "1"}
        row = {
            "record_id": record["record_id"],
            "title": record["title"],
            "year": record["year"],
            "doi_list": record["doi_list"],
            "databases": record["databases"],
            "search_ids": record["search_ids"],
            "stream_hint_not_eligibility": record["stream_hint_not_eligibility"],
            "abstract_available": int(bool(record["abstract"])),
            "priority_source_ids": joined([seed["source_id"] for seed in seeds]),
            "priority_source_types": joined([seed["source_type"] for seed in seeds]),
            "keyword_rq_hints_not_screening": joined(list(keywords)),
            "seed_rq_hints_not_screening": joined(list(seed_hints)),
            "human_eligibility_status": "not_screened",
            "human_rq_coding_status": "not_coded",
        }
        for rq in RQS:
            row[f"{rq.lower()}_keyword_hint"] = int(rq in keywords)
            row[f"{rq.lower()}_seed_hint"] = int(rq in seed_hints)
            if rq in keywords or rq in seed_hints:
                rq_lists[rq].append(row)
        candidate_rows.append(row)
        if not keywords and not seed_hints:
            unassigned.append(row)
    fields = list(candidate_rows[0])
    write_csv(GENERATED / "candidate_rq_index.csv", candidate_rows, fields)
    for rq, records in rq_lists.items():
        write_csv(GENERATED / f"{rq}_candidates_not_screened.csv", records, fields)
    write_csv(GENERATED / "unassigned_keyword_candidates.csv", unassigned, fields)

    # Abstract retrieval queue with existing identifiers and deterministic order.
    hits_by_record: dict[str, list[dict]] = defaultdict(list)
    for hit in hits:
        hits_by_record[hit["record_id"]].append(hit)
    retrieval = []
    for record in queue:
        if record["abstract"]:
            continue
        sources = hits_by_record[record["record_id"]]
        pmids = joined([hit["external_id"] for hit in sources if hit["database"] == "Pubmed"])
        external_ids = joined([f'{hit["database"]}:{hit["external_id"]}' for hit in sources if hit["external_id"]])
        priority_ids = joined([seed["source_id"] for seed in seeds_by_record.get(record["record_id"], [])])
        if priority_ids:
            tier = "1_seed_source"
        elif record["stream_hint_not_eligibility"] != "hrc_search_only":
            tier = "2_am_or_both_streams"
        elif record["doi_list"] or pmids:
            tier = "3_hrc_identifier_available"
        else:
            tier = "4_hrc_title_lookup"
        retrieval.append({
            "retrieval_tier_not_eligibility": tier,
            "record_id": record["record_id"],
            "title": record["title"],
            "year": record["year"],
            "doi_list": record["doi_list"],
            "pmid": pmids,
            "all_external_ids": external_ids,
            "databases": record["databases"],
            "source_files": joined([hit["source_file"] for hit in sources]),
            "priority_source_ids": priority_ids,
            "stream_hint_not_eligibility": record["stream_hint_not_eligibility"],
        })
    retrieval.sort(key=lambda row: (row["retrieval_tier_not_eligibility"], row["title"].lower()))
    write_csv(GENERATED / "abstract_retrieval_queue.csv", retrieval, list(retrieval[0]))

    # DOI conflicts are candidate groups only; no automated adjudication.
    records_by_title: dict[str, list[dict]] = defaultdict(list)
    for record in master:
        records_by_title[title_key(record["title"])].append(record)
    conflict_rows = []
    manual_conflicts = []
    for number, conflict in enumerate(conflicts, 1):
        case_id = f"DOI-C{number:02d}"
        matches = records_by_title[title_key(conflict["title"])]
        case = {
            "case_id": case_id,
            "title": conflict["title"],
            "years": conflict["years"],
            "dois": conflict["dois"],
            "candidate_record_ids": joined([record["record_id"] for record in matches]),
            "source_files": conflict["source_files"],
            "review_status": "human_adjudication_pending",
        }
        conflict_rows.append(case)
        manual_conflicts.append({**case, "decision": "", "verified_source_locator": "", "reviewer": "", "decision_date": "", "notes": ""})
    write_csv(GENERATED / "doi_conflict_review_queue.csv", conflict_rows, list(conflict_rows[0]))
    write_manual_once(MANUAL / "doi_conflict_adjudication.csv", manual_conflicts, list(manual_conflicts[0]))

    # Empty human extraction templates preserve study/report/link levels.
    write_manual_once(MANUAL / "study_registry_template.csv", [], [
        "study_id", "report_id", "record_id", "citation", "year", "country", "sector", "employment_context",
        "design", "participant_n", "independent_unit", "sampling_method", "full_text_locator",
        "reviewer_1", "reviewer_2", "consensus_status", "notes",
    ])
    write_manual_once(MANUAL / "rq_evidence_link_template.csv", [], [
        "link_id", "study_id", "report_id", "rq", "algorithmic_function", "exposure_construct",
        "exposure_unit", "exposure_measure_source", "exposure_time_window", "exposure_frequency",
        "exposure_intensity", "exposure_duration", "exposure_variability", "advance_notice",
        "worker_override", "proposed_mechanism", "measured_mechanism", "osh_outcome",
        "outcome_measure", "outcome_time_window", "comparison", "effect_estimate", "effect_ci",
        "analysis_unit", "confounding_or_bias_note", "control_type", "control_evaluation_level",
        "control_worker_osh_outcome", "source_page_table_quote_locator", "reviewer_1", "reviewer_2",
        "consensus_status", "notes",
    ])

    stats = {
        "stage": "provisional_bibliographic_organization_not_human_screening",
        "source_files": len(manifest),
        "raw_rows": len(hits),
        "provisional_unique_records": len(master),
        "queue_records": len(queue),
        "search_log_rows": len(search_log),
        "searches_with_exports": sum(bool(files_by_search[row["search_id"]]) for row in search_log),
        "searches_without_exports": sum(not files_by_search[row["search_id"]] for row in search_log),
        "searches_missing_run_datetime": sum(bool(files_by_search[row["search_id"]]) and not row["run_datetime_timezone"] for row in search_log),
        "searches_missing_screen_hits": sum(bool(files_by_search[row["search_id"]]) and not row["hits_shown"] for row in search_log),
        "priority_sources": len(priority_rows),
        "priority_matched_by_doi": sum(row["local_match_status"] == "matched_by_doi" for row in priority_rows),
        "priority_not_matched_by_doi": sum(row["local_match_status"] != "matched_by_doi" for row in priority_rows),
        "candidate_counts_by_rq_union_of_keyword_and_seed_hints": {rq: len(rq_lists[rq]) for rq in RQS},
        "unassigned_candidate_records": len(unassigned),
        "records_with_multiple_rq_hints": sum(sum(r[f"{rq.lower()}_keyword_hint"] or r[f"{rq.lower()}_seed_hint"] for rq in RQS) > 1 for r in candidate_rows),
        "missing_abstract_records": len(retrieval),
        "abstract_retrieval_tiers": dict(sorted(Counter(row["retrieval_tier_not_eligibility"] for row in retrieval).items())),
        "doi_conflict_groups": len(conflict_rows),
        "input_sha256": {key: sha256(path) for key, path in paths.items()},
    }
    (GENERATED / "organization_summary.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
