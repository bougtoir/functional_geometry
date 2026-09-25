#!/usr/bin/env python3

import csv
import hashlib
import json
import mimetypes
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "functional-geometry-research/1.0 (public-source archival)"

JCLP_URLS = [
    "https://www.sciencedirect.com/journal/journal-of-cleaner-production/publish/guide-for-authors",
    "https://www.sciencedirect.com/journal/journal-of-cleaner-production/publish/open-access-options",
    "https://www.elsevier.com/subject/environmental-science/journal-of-cleaner-production-family",
    "https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals",
    "https://www.elsevier.com/about/policies-and-standards/publishing-ethics",
    "https://www.elsevier.com/about/policies-and-standards/research-ethics",
    "https://www.elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions/artwork-formats-checklist",
    "https://www.elsevier.com/researcher/author/tools-and-resources/graphical-abstract",
    "https://www.elsevier.com/researcher/author/tools-and-resources/research-data/data-guidelines",
]


def safe_name(value):
    cleaned = "".join(char if char.isalnum() else "_" for char in value)
    return "_".join(part for part in cleaned.split("_") if part)[:140]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extension(url, content_type):
    suffix = Path(urlparse(url).path).suffix
    if suffix and len(suffix) <= 8:
        return suffix
    guessed = mimetypes.guess_extension(content_type.split(";")[0].strip())
    return guessed or ".html"


def normalized_utc(timestamp=None):
    value = timestamp or datetime.now(timezone.utc)
    if value.tzinfo is None:
        raise ValueError("Acquisition timestamps must include a timezone")
    return value.astimezone(timezone.utc)


def write_snapshot(output_dir, source_id, suffix, body, retrieved_at):
    output_dir.mkdir(parents=True, exist_ok=True)
    base = output_dir / f"{safe_name(source_id)}{suffix}"
    timestamp = retrieved_at.strftime("%Y%m%dT%H%M%S%fZ")
    counter = 0
    while True:
        if counter == 0 and not base.exists():
            candidate = base
        else:
            counter_suffix = "" if counter == 0 else f"_{counter:03d}"
            candidate = base.with_name(
                f"{base.stem}_{timestamp}{counter_suffix}{base.suffix}"
            )
        try:
            with candidate.open("xb") as handle:
                handle.write(body)
            return candidate
        except FileExistsError:
            counter += 1


def retrieve(source_id, url, output_root, retrieved_at=None):
    retrieved_at = normalized_utc(retrieved_at)
    access_date = retrieved_at.date().isoformat()
    output_dir = output_root / access_date
    status = "FAILED"
    content_type = ""
    error = ""
    body = b""
    final_url = url
    try:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            status = str(response.status)
            content_type = response.headers.get("Content-Type", "")
            final_url = response.geturl()
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        error = str(exc)
    output = write_snapshot(
        output_dir,
        source_id,
        extension(final_url, content_type),
        body,
        retrieved_at,
    )
    return {
        "source_id": source_id,
        "source_url": url,
        "final_url": final_url,
        "retrieved_utc": retrieved_at.isoformat(),
        "access_date": access_date,
        "status": status,
        "content_type": content_type,
        "local_path": str(output.relative_to(ROOT)),
        "size_bytes": output.stat().st_size,
        "sha256": sha256(output),
        "error": error,
        "usage_note": "Persisted public source snapshot; redistribution depends on source terms.",
    }


def acquire_jclp(retrieved_at):
    output_root = ROOT / "data/raw/jclp_sources/snapshots"
    return [
        retrieve(f"jclp_{index:02d}", url, output_root, retrieved_at)
        for index, url in enumerate(JCLP_URLS, start=1)
    ]


def acquire_crossref(retrieved_at):
    references = ROOT / "data/processed/references_verified_literature.csv"
    output_root = ROOT / "data/raw/literature_crossref"
    records = []
    with references.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            doi = row["doi"]
            url = f"https://api.crossref.org/works/{doi}"
            records.append(
                retrieve(f"crossref_{doi}", url, output_root, retrieved_at)
            )
    return records


def acquire_straw(retrieved_at):
    registry = ROOT / "reports/source_registry.csv"
    output_root = ROOT / "data/raw/straw_sources"
    records = []
    with registry.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            records.append(
                retrieve(
                    row["source_id"],
                    row["url_or_doi"],
                    output_root,
                    retrieved_at,
                )
            )
    return records


def write_ledger(records, retrieved_at):
    path = ROOT / "data/raw/public_source_acquisition_ledger.csv"
    fields = list(records[0])
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        if not exists:
            writer.writeheader()
        writer.writerows(records)
    with path.open(newline="", encoding="utf-8") as handle:
        all_records = list(csv.DictReader(handle))
    summary = {
        "records": len(all_records),
        "records_this_run": len(records),
        "nonempty": sum(int(record["size_bytes"]) > 0 for record in all_records),
        "failed_or_empty": sum(
            record["status"] == "FAILED" or int(record["size_bytes"]) == 0
            for record in all_records
        ),
        "generated_utc": normalized_utc(retrieved_at).isoformat(),
    }
    (ROOT / "data/raw/public_source_acquisition_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    retrieved_at = normalized_utc()
    records = (
        acquire_jclp(retrieved_at)
        + acquire_crossref(retrieved_at)
        + acquire_straw(retrieved_at)
    )
    write_ledger(records, retrieved_at)
    print(
        f"Appended {len(records)} acquisition records; "
        f"{sum(record['size_bytes'] > 0 for record in records)} nonempty snapshots."
    )


if __name__ == "__main__":
    main()
