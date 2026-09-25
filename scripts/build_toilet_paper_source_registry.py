#!/usr/bin/env python3

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/toilet_paper_sources"
METADATA = ROOT / "data/processed/toilet_paper_source_metadata.csv"
OUTPUT = ROOT / "data/processed/source_registry.csv"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_tsv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def classify_capture(row):
    if not row:
        return "NOT_CAPTURED"
    status = row["http_status"]
    size = int(row["file_size_bytes"])
    if status == "200000" and size > 0:
        return "SUCCESS_WITH_CURL_STATUS_ANOMALY"
    if status == "202" and size == 0:
        return "INCOMPLETE_EMPTY_HTTP_202"
    if status == "200" and size > 0:
        return "SUCCESS"
    if status == "200" and size == 0:
        return "INCOMPLETE_EMPTY_HTTP_200"
    if status in {"403", "404"}:
        return f"FAILED_HTTP_{status}"
    return f"REVIEW_HTTP_{status}"


def relative_snapshot(row):
    if not row:
        return ""
    path = Path(row["file_path"])
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return row["file_path"]


def main():
    sources = {row["source_id"]: row for row in read_tsv(RAW / "sources.tsv")}
    acquisitions = {}
    for row in read_tsv(RAW / "acquisition_ledger_2026-09-24.tsv"):
        acquisitions[row["source_id"]] = row

    rows = []
    for metadata in read_csv(METADATA):
        source_id = metadata["source_id"]
        source = sources[source_id]
        acquisition = acquisitions.get(source_id)
        rows.append(
            {
                **metadata,
                "url": source["url"],
                "access_date": (
                    acquisition["retrieved_at_utc"][:10]
                    if acquisition
                    else ""
                ),
                "source_type": source["source_type"],
                "capture_status": classify_capture(acquisition),
                "retrieved_at_utc": acquisition["retrieved_at_utc"] if acquisition else "",
                "content_type": acquisition["content_type"] if acquisition else "",
                "local_snapshot": relative_snapshot(acquisition),
                "file_size_bytes": acquisition["file_size_bytes"] if acquisition else "",
                "sha256": acquisition["sha256"] if acquisition else "",
            }
        )

    fields = list(rows[0])
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
