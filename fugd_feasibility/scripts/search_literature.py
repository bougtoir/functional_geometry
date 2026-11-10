"""Systematic bibliographic search for the FUGD novelty gate.

Queries Crossref (primary), OpenAlex and Semantic Scholar (secondary, rate-limited)
and stores every raw response under data/raw/literature_search/ without overwriting
earlier snapshots. A machine-readable ledger records URL, UTC time, HTTP status,
local path, size and SHA-256 for each request, including failures.
"""
import csv
import hashlib
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "literature_search"
LEDGER = RAW / "search_ledger.csv"
MAILTO = "bougtoir@gmail.com"

DOMAIN_QUERIES = {
    "01_modular_design": "product modularity modular product design optimization",
    "02_configurable_design": "configurable product design configuration optimization",
    "03_product_architecture": "product architecture optimization",
    "04_product_family": "product family design platform optimization",
    "05_mass_customization": "mass customization literature review",
    "06_cutting_stock": "cutting stock problem stochastic demand",
    "07_assortment_sizes": "assortment problem selection of stock sizes",
    "08_assortment_choice": "assortment optimization discrete choice model",
    "09_dispensing": "dispensing quantity optimization consumable waste",
    "10_choice_configuration": "consumer choice product configuration design optimization discrete choice",
    "11_geometry_behavior": "package size consumption usage volume",
    "12_unit_bias": "unit bias portion size consumption",
    "13_perforation": "perforation tissue paper sheet size consumer use",
    "14_divisible_units": "divisible product unit size waste optimization",
    "15_task_dependent": "task dependent material consumption product use",
    "16_robust_design": "robust design optimization uncertainty product design",
    "17_bilevel_design": "bilevel optimization product design consumer choice",
    "18_resource_efficiency": "design for resource efficiency consumables",
    "19_vial_size": "vial size optimization drug wastage",
    "20_denominations": "optimal coin denominations",
    "21_size_line": "optimal size assortment product line sizes",
    "22_pack_size": "package size decisions",
    "23_paper_towel": "paper towel consumption",
    "24_toilet_paper": "toilet paper consumption",
    "25_select_size": "selectable sheet size perforated roll",
}


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch(url, out_path):
    retrieved = utc_now()
    status = "ERROR"
    body = b""
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"fugd-gate (mailto:{MAILTO})"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                status = str(resp.status)
            break
        except urllib.error.HTTPError as exc:
            status = str(exc.code)
            body = exc.read() or b""
            if exc.code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            break
        except Exception as exc:  # network errors are recorded, not hidden
            status = f"ERROR:{type(exc).__name__}"
            time.sleep(3)
    if out_path.exists():
        stem, suffix = out_path.stem, out_path.suffix
        out_path = out_path.with_name(f"{stem}_{retrieved.replace(':', '')}{suffix}")
    out_path.write_bytes(body)
    digest = hashlib.sha256(body).hexdigest()
    new = not LEDGER.exists()
    with LEDGER.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new:
            writer.writerow(["source", "url", "retrieved_utc", "http_status", "local_path", "bytes", "sha256", "terms_note"])
        writer.writerow([out_path.parent.name, url, retrieved, status, str(out_path.relative_to(ROOT)), len(body), digest,
                         "Bibliographic metadata; Crossref/OpenAlex CC0, Semantic Scholar API terms"])
    return status, body


def crossref(key, query, rows=40):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {"query.bibliographic": query, "rows": rows, "mailto": MAILTO,
         "select": "DOI,title,author,issued,container-title,type,is-referenced-by-count"})
    (RAW / "crossref").mkdir(parents=True, exist_ok=True)
    return fetch(url, RAW / "crossref" / f"{key}.json")


def openalex(key, query, rows=25):
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
        {"search": query, "per-page": rows, "mailto": MAILTO,
         "select": "id,doi,title,publication_year,primary_location,cited_by_count,authorships"})
    (RAW / "openalex").mkdir(parents=True, exist_ok=True)
    return fetch(url, RAW / "openalex" / f"{key}.json")


def s2(key, query, rows=20):
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {"query": query, "limit": rows, "fields": "title,year,venue,externalIds,citationCount,authors"})
    (RAW / "semanticscholar").mkdir(parents=True, exist_ok=True)
    return fetch(url, RAW / "semanticscholar" / f"{key}.json")


def doi_record(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi) + f"?mailto={MAILTO}"
    (RAW / "doi_verification").mkdir(parents=True, exist_ok=True)
    safe = doi.replace("/", "_").replace(":", "_")
    return fetch(url, RAW / "doi_verification" / f"{safe}.json")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "search"
    if mode == "search":
        for key, query in DOMAIN_QUERIES.items():
            print(key, crossref(key, query)[0], flush=True)
            time.sleep(1)
        for key, query in DOMAIN_QUERIES.items():
            print("openalex", key, openalex(key, query)[0], flush=True)
            time.sleep(1)
        for key, query in DOMAIN_QUERIES.items():
            print("s2", key, s2(key, query)[0], flush=True)
            time.sleep(4)
    elif mode == "doi":
        for doi in Path(sys.argv[2]).read_text().split():
            print(doi, doi_record(doi)[0], flush=True)
            time.sleep(0.5)


TARGETED_QUERIES = {
    "t01_ulrich_architecture": "role of product architecture in the manufacturing firm",
    "t02_select_a_size": "select-a-size paper towel half sheet",
    "t03_food_waste_pack_size": "packaging size household food waste portion",
    "t04_dose_strength": "optimal dose strengths tablet sizes wastage",
    "t05_perforation_spacing": "perforation spacing tissue sheet length consumption",
    "t06_sheet_count_usage": "number of sheets used toilet tissue usage behavior",
    "t07_portion_packaging_design": "portion control packaging design consumption reduction",
    "t08_lot_size_rounding": "integer pack size demand rounding waste expected overage",
    "t09_partition_line": "optimal partition of interval demand distribution quantization",
    "t10_tablet_splitting": "tablet splitting scored tablets dose flexibility",
}


def openalex_doi(doi):
    url = f"https://api.openalex.org/works/doi:{doi}?mailto={MAILTO}"
    (RAW / "openalex_abstracts").mkdir(parents=True, exist_ok=True)
    safe = doi.replace("/", "_").replace(":", "_")
    return fetch(url, RAW / "openalex_abstracts" / f"{safe}.json")


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "targeted":
    for key, query in TARGETED_QUERIES.items():
        print(key, crossref(key, query, rows=25)[0], openalex(key, query, rows=20)[0], flush=True)
        time.sleep(1)

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "abstracts":
    for doi in Path(sys.argv[2]).read_text().split():
        print(doi, openalex_doi(doi)[0], flush=True)
        time.sleep(0.5)
