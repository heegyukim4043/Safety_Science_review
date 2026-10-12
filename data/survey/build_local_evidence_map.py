"""Merge local Paper 1 search exports without making inclusion decisions.

Requires Python 3.9+, xlrd 2.x for WoS .xls, and bibtexparser 1.x for ACM .bib.
Run from any directory: python build_local_evidence_map.py
"""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import xlrd
import bibtexparser


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "processed"
OUT.mkdir(exist_ok=True)


def clean_doi(value: object) -> str:
    raw = str(value or "").strip().lower()
    raw = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", raw)
    match = re.search(r"10\.\d{4,9}/\S+", raw)
    return match.group(0).rstrip(".,;:)\"]") if match else ""


def clean_title(value: object) -> str:
    raw = unicodedata.normalize("NFKC", html.unescape(str(value or ""))).lower()
    return " ".join(re.findall(r"\w+", raw, flags=re.UNICODE))


def as_year(value: object) -> int | None:
    match = re.search(r"(?:19|20)\d{2}", str(value or ""))
    return int(match.group(0)) if match else None


def clean_abstract(value: object) -> str:
    abstract = str(value or "").strip()
    if abstract.lower().strip("[] ") in {"no abstract available", "abstract not available"}:
        return ""
    return abstract


def read_rows(path: Path):
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            yield from csv.DictReader(handle)
    elif path.suffix.lower() == ".xls":
        sheet = xlrd.open_workbook(str(path), on_demand=True).sheet_by_index(0)
        headers = [str(sheet.cell_value(0, column)) for column in range(sheet.ncols)]
        for number in range(1, sheet.nrows):
            yield {headers[column]: sheet.cell_value(number, column) for column in range(sheet.ncols)}
    elif path.suffix.lower() == ".bib":
        with path.open(encoding="utf-8") as handle:
            yield from bibtexparser.load(handle).entries


def source_record(path: Path, row: dict, number: int) -> dict:
    database = path.parent.name
    if database == "Scopus":
        fields = ("Title", "Year", "EID", "Document Type", "Source title", "Authors", "Author Keywords")
    elif database == "Pubmed":
        fields = ("Title", "Publication Year", "PMID", "", "Journal/Book", "Authors", "")
    elif database == "WOS":
        fields = ("Article Title", "Publication Year", "UT (Unique WOS ID)", "Document Type", "Source Title", "Authors", "Author Keywords")
    elif database == "ACM":
        fields = ("title", "year", "ID", "ENTRYTYPE", "journal", "author", "keywords")
    else:
        fields = ("Document Title", "Publication Year", "", "", "Publication Title", "Authors", "Author Keywords")
    title_field, year_field, id_field, type_field, journal_field, authors_field, kw_field = fields
    title = str(row.get(title_field, "") or "").strip()
    doi = clean_doi(row.get("doi", "") if database == "ACM" else row.get("DOI", ""))
    external_id = str(row.get(id_field, "") or "").strip() if id_field else ""
    search_id = re.sub(r"_\d+$", "", path.stem.strip()) if database in {"WOS", "ACM"} else path.stem.strip()
    return {
        "database": database,
        "search_id": search_id,
        "source_file": str(path.relative_to(ROOT)).replace("\\", "/"),
        "row_number": number,
        "external_id": external_id,
        "doi": doi,
        "title": title,
        "title_key": clean_title(title),
        "year": as_year(row.get(year_field, "")),
        "authors": str(row.get(authors_field, "") or "").strip(),
        "source_title": str(row.get(journal_field, "") or row.get("booktitle", "") or "").strip(),
        "document_type": str(row.get(type_field, "") or "").strip() if type_field else "",
        "keywords": str(row.get(kw_field, "") or "").strip() if kw_field else "",
        "abstract": clean_abstract(row.get("abstract", "") if database == "ACM" else row.get("Abstract", "")),
    }


class UnionFind:
    def __init__(self, count: int):
        self.parent = list(range(count))

    def find(self, index: int) -> int:
        while self.parent[index] != index:
            self.parent[index] = self.parent[self.parent[index]]
            index = self.parent[index]
        return index

    def union(self, left: int, right: int) -> None:
        a, b = self.find(left), self.find(right)
        if a != b:
            self.parent[b] = a


def merge_records(records: list[dict]) -> list[list[dict]]:
    union = UnionFind(len(records))
    doi_first: dict[str, int] = {}
    source_id_first: dict[tuple[str, str], int] = {}
    by_title: dict[str, list[int]] = defaultdict(list)
    for number, record in enumerate(records):
        if record["external_id"]:
            source_key = (record["database"], record["external_id"])
            if source_key in source_id_first:
                union.union(number, source_id_first[source_key])
            else:
                source_id_first[source_key] = number
        doi = record["doi"]
        if doi:
            if doi in doi_first:
                union.union(number, doi_first[doi])
            else:
                doi_first[doi] = number
        title_key = record["title_key"]
        if len(title_key) >= 25 and len(title_key.split()) >= 4:
            by_title[title_key].append(number)
    for numbers in by_title.values():
        if len({records[number]["doi"] for number in numbers if records[number]["doi"]}) > 1:
            # Same-title records with conflicting DOIs require human adjudication.
            continue
        for left in range(len(numbers)):
            year_left = records[numbers[left]]["year"]
            for right in range(left + 1, len(numbers)):
                year_right = records[numbers[right]]["year"]
                doi_left = records[numbers[left]]["doi"]
                doi_right = records[numbers[right]]["doi"]
                # Different nonempty DOIs may describe distinct papers with the same title.
                if doi_left and doi_right and doi_left != doi_right:
                    continue
                if year_left is None or year_right is None or abs(year_left - year_right) <= 1:
                    union.union(numbers[left], numbers[right])
    groups: dict[int, list[dict]] = defaultdict(list)
    for number, record in enumerate(records):
        groups[union.find(number)].append(record)
    return list(groups.values())


RQ_PATTERNS = {
    "RQ1": r"algorithmic management|algorithmic control|surveillance|monitoring|task allocat|task assign|schedul|work pac|robot|automated decision|autonomy",
    "RQ2": r"measur|questionnaire|scale develop|validat|exposure|work log|sensor|ecological momentary|assessment instrument",
    "RQ3": r"mediat|mechanism|autonomy|time pressure|work pressure|cognit|stress|fatigue|ergonom|psychosocial|fairness",
    "RQ4": r"occupational health|safety|injur|accident|musculoskeletal|burnout|well.?being|stress|fatigue|sleep|mental health|workload",
    "RQ5": r"interven|mitigat|redesign|transparen|participat|contest|human.in.the.loop|consultation|countermeasure|preventive",
}


def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    queue_path = OUT / "screening_queue_2015_2026.csv"
    if queue_path.exists():
        with queue_path.open(encoding="utf-8-sig", newline="") as handle:
            prior = list(csv.DictReader(handle))
        decision_fields = ("reviewer1_decision", "reviewer2_decision", "consensus_decision", "exclusion_reason", "full_text_status", "rq1_final", "rq2_final", "rq3_final", "rq4_final", "rq5_final")
        if any(any(row.get(field, "").strip() for field in decision_fields) for row in prior):
            raise RuntimeError("Screening decisions exist: archive and reconcile the queue before rebuilding it")
    records = []
    file_manifest = []
    for path in sorted(ROOT.rglob("*")):
        if path.parent.name not in {"Scopus", "Pubmed", "WOS", "IEEE EXplore", "ACM"}:
            continue
        if path.suffix.lower() not in {".csv", ".xls", ".bib"}:
            continue
        file_records = [source_record(path, row, number) for number, row in enumerate(read_rows(path), 2)]
        records.extend(file_records)
        file_manifest.append({
            "source_file": str(path.relative_to(ROOT)).replace("\\", "/"),
            "database": path.parent.name,
            "search_id": file_records[0]["search_id"] if file_records else re.sub(r"_\d+$", "", path.stem),
            "exported_rows": len(file_records),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    write_csv(OUT / "source_file_manifest.csv", ["source_file", "database", "search_id", "exported_rows", "sha256"], file_manifest)
    same_title: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        if len(record["title_key"]) >= 25:
            same_title[record["title_key"]].append(record)
    conflict_rows = []
    for matches in same_title.values():
        dois = sorted({r["doi"] for r in matches if r["doi"]})
        if len(dois) > 1:
            conflict_rows.append({
                "title": matches[0]["title"],
                "years": "; ".join(map(str, sorted({r["year"] for r in matches if r["year"]}))),
                "dois": "; ".join(dois),
                "source_files": "; ".join(sorted({r["source_file"] for r in matches})),
                "decision": "manual_adjudication_needed",
            })
    groups = merge_records(records)
    master_rows = []
    hit_rows = []
    for group in groups:
        canonical = max(group, key=lambda r: (bool(r["abstract"]), len(r["abstract"]), bool(r["doi"]), len(r["title"])))
        dois = sorted({r["doi"] for r in group if r["doi"]})
        years = sorted({r["year"] for r in group if r["year"] is not None})
        source_names = sorted({r["database"] for r in group})
        search_ids = sorted({r["search_id"] for r in group})
        external_ids = sorted({r["external_id"] for r in group if r["external_id"]})
        source_anchor = external_ids[0] if external_ids else min(r["source_file"] + ":" + str(r["row_number"]) for r in group)
        stable_key = dois[0] if dois else canonical["title_key"] + "|" + str(years[0] if years else "") + "|" + source_anchor
        record_id = "P1-" + hashlib.sha1(stable_key.encode("utf-8")).hexdigest()[:12]
        searchable = " ".join([canonical["title"], canonical["abstract"], canonical["keywords"]]).lower()
        rq_hints = [rq for rq, pattern in RQ_PATTERNS.items() if re.search(pattern, searchable)]
        master_rows.append({
            "record_id": record_id,
            "title": canonical["title"],
            "years_seen": "; ".join(map(str, years)),
            "primary_year": canonical["year"] or (years[0] if years else ""),
            "doi_list": "; ".join(dois),
            "authors": canonical["authors"],
            "source_title": canonical["source_title"],
            "document_types_seen": "; ".join(sorted({r["document_type"] for r in group if r["document_type"]})),
            "databases": "; ".join(source_names),
            "search_ids": "; ".join(search_ids),
            "source_hit_count": len(group),
            "abstract_available": int(bool(canonical["abstract"])),
            "abstract": canonical["abstract"],
            "keywords": canonical["keywords"],
            "rq_keyword_hints_not_screening": "; ".join(rq_hints),
            "year_window_flag": "missing_year_check" if not years else ("outside_2015_2026" if all(y < 2015 or y > 2026 for y in years) else ("mixed_years_check" if any(y < 2015 or y > 2026 for y in years) else "in_window")),
            "multiple_dois_check": int(len(dois) > 1),
            "screening_decision": "pending_human_screening",
        })
        for record in group:
            hit_rows.append({
                "record_id": record_id,
                "database": record["database"],
                "search_id": record["search_id"],
                "source_file": record["source_file"],
                "row_number": record["row_number"],
                "external_id": record["external_id"],
                "doi": record["doi"],
                "year": record["year"] or "",
            })
    master_rows.sort(key=lambda r: (r["primary_year"] or 0, r["title"].lower()), reverse=True)
    hit_rows.sort(key=lambda r: (r["record_id"], r["database"], r["source_file"], r["row_number"]))
    write_csv(OUT / "master_records.csv", list(master_rows[0].keys()), master_rows)
    write_csv(OUT / "source_hits.csv", list(hit_rows[0].keys()), hit_rows)
    write_csv(OUT / "same_title_conflicting_doi.csv", ["title", "years", "dois", "source_files", "decision"], conflict_rows)
    hrc_search_ids = {"P3_HRC", "W3_HRC", "I1_HRC", "I2_ALLOC", "A3_HRC"}
    queue_rows = []
    for row in master_rows:
        if row["year_window_flag"] == "outside_2015_2026":
            continue
        ids = set(row["search_ids"].split("; "))
        stream = "both_streams" if ids & hrc_search_ids and ids - hrc_search_ids else ("hrc_search_only" if ids & hrc_search_ids else "am_related_search_only")
        queue_rows.append({
            "record_id": row["record_id"],
            "stream_hint_not_eligibility": stream,
            "title": row["title"],
            "year": row["primary_year"],
            "year_window_flag": row["year_window_flag"],
            "doi_list": row["doi_list"],
            "abstract": row["abstract"],
            "databases": row["databases"],
            "search_ids": row["search_ids"],
            "rq_keyword_hints_not_screening": row["rq_keyword_hints_not_screening"],
            "reviewer1_decision": "",
            "reviewer2_decision": "",
            "consensus_decision": "",
            "exclusion_reason": "",
            "full_text_status": "",
            "rq1_final": "",
            "rq2_final": "",
            "rq3_final": "",
            "rq4_final": "",
            "rq5_final": "",
        })
    queue_rows.sort(key=lambda r: ({"am_related_search_only": 0, "both_streams": 1, "hrc_search_only": 2}[r["stream_hint_not_eligibility"]], r["title"].lower()))
    write_csv(queue_path, list(queue_rows[0].keys()), queue_rows)
    priority_file = ROOT.parent / "paper1_search" / "priority_source_crosswalk.csv"
    priority_coverage = []
    if priority_file.exists():
        doi_index = {doi: row for row in master_rows for doi in row["doi_list"].split("; ") if doi}
        with priority_file.open(encoding="utf-8-sig", newline="") as handle:
            for source in csv.DictReader(handle):
                doi = clean_doi(source.get("doi", ""))
                match = doi_index.get(doi)
                priority_coverage.append({
                    "source_id": source["source_id"],
                    "label": source["label"],
                    "source_type": source["source_type"],
                    "doi": doi,
                    "local_match_status": "matched_by_doi" if match else ("doi_not_in_exports" if doi else "prior_source_has_no_doi"),
                    "record_id": match["record_id"] if match else "",
                    "databases": match["databases"] if match else "",
                    "abstract_available": match["abstract_available"] if match else "",
                })
        write_csv(OUT / "priority_source_coverage.csv", list(priority_coverage[0].keys()), priority_coverage)
    by_db = Counter(r["database"] for r in records)
    summary = {
        "source_files": len({r["source_file"] for r in records}),
        "exported_rows": len(records),
        "rows_by_database": dict(sorted(by_db.items())),
        "provisional_unique_records": len(groups),
        "provisional_duplicate_rows": len(records) - len(groups),
        "unique_records_with_abstract": sum(r["abstract_available"] for r in master_rows),
        "unique_records_outside_2015_2026": sum(r["year_window_flag"] == "outside_2015_2026" for r in master_rows),
        "unique_records_mixed_years_check": sum(r["year_window_flag"] == "mixed_years_check" for r in master_rows),
        "unique_records_missing_year_check": sum(r["year_window_flag"] == "missing_year_check" for r in master_rows),
        "multiple_dois_to_check": sum(r["multiple_dois_check"] for r in master_rows),
        "same_title_conflicting_doi_groups": len(conflict_rows),
        "priority_sources_matched_by_doi": sum(r["local_match_status"] == "matched_by_doi" for r in priority_coverage),
        "provisional_in_window_screening_queue": len(queue_rows),
        "queue_by_search_stream": dict(Counter(r["stream_hint_not_eligibility"] for r in queue_rows)),
        "method": "Database record ID or DOI exact match plus normalized exact title within one publication year when at least one DOI is missing; different nonempty DOIs not auto-merged; automated and provisional; no inclusion decisions",
    }
    (OUT / "processing_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
