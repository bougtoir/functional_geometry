"""Bibliographic retrieval for the Function-Before-Form research gate.

Modes:
  search          Crossref + OpenAlex topic queries (DOMAIN_QUERIES, GAP_QUERIES)
  doi FILE        Crossref /works/{doi} verification for each DOI in FILE
  openalex FILE   OpenAlex DOI lookup (abstract inverted index, OA location)
  fulltext FILE   download open-access full texts listed as "doi url" lines

Every response (including failures) is stored under data/raw/ without
overwriting earlier snapshots; ledger rows record URL, UTC time, HTTP status,
local path, bytes, SHA-256 and terms.
"""
import csv
import hashlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "literature_search"
FULLTEXT = ROOT / "data" / "raw" / "fulltext"
LEDGER = RAW / "search_ledger.csv"
MAILTO = "bougtoir@gmail.com"
FIELDS = ["source", "url", "retrieved_utc", "http_status", "local_path", "bytes", "sha256", "terms_note"]

DOMAIN_QUERIES = {
    "01_functional_modelling": "functional modeling engineering design functional basis",
    "02_fbs": "function behaviour structure framework design",
    "03_functional_decomposition": "functional decomposition conceptual design",
    "04_value_engineering": "value engineering function analysis product",
    "05_design_fixation": "design fixation engineering designers examples",
    "06_functional_fixedness": "functional fixedness problem solving",
    "07_design_by_analogy": "design by analogy problem re-representation",
    "08_triz": "TRIZ inventive problem solving review",
    "09_dfe": "design for environment guidelines product",
    "10_ecodesign": "ecodesign product development review",
    "11_sustainable_design": "design for sustainability evolution product to system innovation",
    "12_pss": "product-service system environmental",
    "13_dematerialization": "dematerialization material efficiency product",
    "14_circular_design": "product design circular economy strategies",
    "15_sufficiency": "sufficiency oriented design business",
    "16_lca_functional_unit": "functional unit life cycle assessment comparison alternatives",
    "17_consequential_lca": "consequential life cycle assessment decision",
    "18_design_space": "design space exploration set-based design",
    "19_requirements": "solution-neutral requirements engineering design",
    "20_lock_in": "design lock-in path dependence technology",
    "21_material_selection": "material selection substitution sustainable product design",
}

GAP_QUERIES = {
    "g01_env_info_creativity": "environmental information creativity designers experiment",
    "g02_eco_ideation": "eco-ideation tool sustainable design idea generation",
    "g03_sustainable_fixation": "sustainability design fixation ideation study",
    "g04_problem_framing": "problem framing design brief effect on design outcomes experiment",
    "g05_function_innovation": "function innovation system innovation ecodesign levels",
    "g06_regrettable_substitution": "regrettable substitution material alternatives",
    "g07_single_use_alternatives": "life cycle assessment single-use plastic alternatives cutlery",
    "g08_packaging_perception": "consumer perception packaging material sustainability life cycle assessment gap",
    "g09_ecodesign_practice": "ecodesign practice companies incremental improvement",
    "g10_abstraction_sustainable": "functional abstraction sustainable design ideation",
    "g11_eco_triz": "TRIZ eco-design",
    "g12_design_commitment": "design determines cost early design commitment",
    "g13_material_driven": "material driven design method",
    "g14_bioplastic_trade_off": "bio-based plastic substitution environmental trade-off",
    "g15_form_preservation": "product archetype familiar form sustainable product design",
}

SECOND_PASS_QUERIES = {
    "s01_brezet_levels": "dynamics in ecodesign practice product improvement redesign function innovation system innovation",
    "s02_gero_prototypes": "design prototypes knowledge representation schema for design",
    "s03_chandrasekaran": "representing function relating functional representation and functional modeling research streams",
    "s04_umeda_fbs": "function behavior state modeler conceptual design",
    "s05_sustainable_ideation_experiment": "sustainability framing ideation novelty experiment designers",
    "s06_ecodesign_method_ideation": "eco-design method comparison ideation environmental impact of concepts",
    "s07_sustainable_design_methods_roadmap": "research roadmap sustainable design methods",
    "s08_design_brief_sustainability": "design brief sustainability requirements students concepts experiment",
    "s09_material_substitution_ecodesign": "material substitution ecodesign strategy companies frequency",
    "s10_ecodesign_strategy_wheel": "lifecycle design strategy wheel new concept development dematerialisation",
    "s11_requirement_framing_fixation": "requirement framing fixation solution-neutral problem formulation",
    "s12_problem_formulation_design": "problem formulation in design creativity outcomes",
    "s13_reusable_vs_single_use": "reusable versus single-use life cycle assessment break-even number of uses",
    "s14_packaging_free": "packaging-free product delivery environmental assessment",
    "s15_function_oriented_eco": "function oriented eco-design need fulfilment alternatives",
}


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ledger_row(row):
    new = not LEDGER.exists()
    with LEDGER.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new:
            writer.writerow(FIELDS)
        writer.writerow(row)


def fetch(url, out_path, source, terms="Bibliographic metadata; Crossref/OpenAlex CC0"):
    retrieved = utc_now()
    status, body = "ERROR", b""
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": f"fbf-gate (mailto:{MAILTO})"})
            with urllib.request.urlopen(req, timeout=90) as resp:
                body, status = resp.read(), str(resp.status)
            break
        except urllib.error.HTTPError as exc:
            status, body = str(exc.code), exc.read() or b""
            if exc.code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            break
        except Exception as exc:  # network errors are recorded, not hidden
            status = f"ERROR:{type(exc).__name__}"
            time.sleep(3)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        out_path = out_path.with_name(f"{out_path.stem}_{retrieved.replace(':', '')}{out_path.suffix}")
    out_path.write_bytes(body)
    ledger_row([source, url, retrieved, status, str(out_path.relative_to(ROOT)), len(body),
                hashlib.sha256(body).hexdigest(), terms])
    return status, out_path

THIRD_PASS_QUERIES = {
    "t01_faludi_dfe_methods": "Faludi comparing design for environment methods workshop life cycle assessment of concepts",
    "t02_zahner_rerepresent": "fix for fixation rerepresenting and abstracting creative processes design",
    "t03_function_impact_matrix": "function impact matrix sustainability early design",
    "t04_eco_innovation_levels_evidence": "eco-innovation levels product improvement function innovation environmental improvement factor empirical",
    "t05_single_use_alternatives_meta": "single-use plastic alternatives life cycle assessment meta-analysis burden shifting",
    "t06_plastic_ban_substitution": "plastic ban substitution paper bags environmental trade-off",
    "t07_disposable_cutlery_lca": "disposable cutlery life cycle assessment wooden plastic",
    "t08_material_choice_consumer_perception": "consumers perceive material as sustainability cue packaging design lay beliefs",
    "t09_problem_abstraction_level_experiment": "abstraction level of design problem statement experiment idea novelty",
    "t10_solution_neutral": "solution-neutral function structure abstraction engineering design method",
    "t11_eco_design_concepts_lca_students": "student design concepts environmental impact assessment ecodesign intervention",
    "t12_redesign_without_substitution": "lightweighting redesign packaging geometry environmental impact without material change",
    "t13_design_space_sustainable": "design space exploration sustainability early stage alternatives life cycle",
    "t14_form_fixation_example_exposure": "example exposure design fixation form features copying",
    "t15_sustainable_design_tools_effectiveness": "effectiveness of sustainable design tools empirical evaluation outcomes",
}


def safe(doi):
    return doi.replace("/", "_").replace(":", "_")


def crossref_search(key, query, rows=30):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {"query.bibliographic": query, "rows": rows, "mailto": MAILTO,
         "select": "DOI,title,author,issued,container-title,type,is-referenced-by-count"})
    return fetch(url, RAW / "crossref" / f"{key}.json", "crossref")


def openalex_search(key, query, rows=25):
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
        {"search": query, "per-page": rows, "mailto": MAILTO,
         "select": "id,doi,title,publication_year,primary_location,cited_by_count,authorships,type"})
    return fetch(url, RAW / "openalex" / f"{key}.json", "openalex")


def crossref_doi(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi) + f"?mailto={MAILTO}"
    return fetch(url, RAW / "doi_verification" / f"{safe(doi)}.json", "crossref_doi")


def openalex_doi(doi):
    url = f"https://api.openalex.org/works/doi:{doi}?mailto={MAILTO}"
    return fetch(url, RAW / "openalex_works" / f"{safe(doi)}.json", "openalex_doi")


def main():
    mode = sys.argv[1]
    if mode == "search":
        for key, query in {**DOMAIN_QUERIES, **GAP_QUERIES}.items():
            print(key, crossref_search(key, query)[0], openalex_search(key, query)[0], flush=True)
            time.sleep(1)
    elif mode == "search2":
        for key, query in SECOND_PASS_QUERIES.items():
            print(key, crossref_search(key, query)[0], openalex_search(key, query)[0], flush=True)
            time.sleep(1)
    elif mode == "search3":
        for key, query in THIRD_PASS_QUERIES.items():
            print(key, crossref_search(key, query)[0], openalex_search(key, query)[0], flush=True)
            time.sleep(1)
    elif mode in ("doi", "openalex"):
        func = crossref_doi if mode == "doi" else openalex_doi
        for doi in Path(sys.argv[2]).read_text().split():
            print(doi, func(doi)[0], flush=True)
            time.sleep(0.4)
    elif mode == "fulltext":
        for line in Path(sys.argv[2]).read_text().splitlines():
            if line.strip():
                doi, url = line.split(maxsplit=1)
                suffix = ".pdf" if "pdf" in url.lower() else ".html"
                print(doi, fetch(url, FULLTEXT / f"{safe(doi)}{suffix}", "fulltext_oa",
                                 "Open-access full text; local screening copy, not redistributed")[0], flush=True)
                time.sleep(1)


if __name__ == "__main__":
    main()
