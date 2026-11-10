"""Gate 2 targeted search: keyword queries + citation network (OpenAlex/Crossref).
Re-running appends new timestamped raw files and ledger rows; originals are never overwritten."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import search_literature as s

QUERIES = {
    "g01_creativity_env_sustainability_ideas": "creativity environmental sustainability student designers ideas correlation",
    "g02_brief_framing_sustainable_ideation": "design brief framing sustainable ideation experiment",
    "g03_problem_framing_environmental_concepts": "problem framing environmental impact design concepts experiment",
    "g04_lca_generated_concepts": "life cycle assessment of concepts generated in ideation experiment",
    "g05_fixation_sustainable_design": "design fixation sustainable design experiment environmental",
    "g06_material_substitution_ideation": "material substitution versus redesign ideation sustainable product",
    "g07_abstraction_brief_experiment": "abstract versus concrete problem statement design ideation experiment",
    "g08_constraint_brief_creativity": "design constraints brief creativity experiment open versus constrained",
    "g09_early_concept_lca_uncertainty": "streamlined life cycle assessment conceptual design uncertainty early stage concepts",
    "g10_environmental_evaluation_ideas_raters": "environmental evaluation of design ideas raters agreement sustainability",
    "g11_eco_ideation_tools_experiment": "eco-ideation tool controlled experiment environmental performance of ideas",
    "g12_function_impact_ideation": "function-based environmental impact ideation experiment designers",
}
SEEDS = {"collado": "W2072208931", "faludi": "W3089928046", "linsey": "W2065406122", "devanathan": "W2123356613"}
# Reconciliation-gate seeds (forward citations, page 1 = complete for these counts)
SEEDS2 = {"liao2021": "W3158443341", "greeley2025": "W4412040494", "ruizpastor2020": "W3094322850",
          "ross2022": "W3202368076", "collado2011chapter": "W2114455537"}
SEL = "id,doi,title,publication_year,cited_by_count,primary_location,type"

def network2():
    for k, w in SEEDS2.items():
        s.fetch(f"https://api.openalex.org/works?filter=cites:{w}&per-page=200&select={SEL}&mailto={s.MAILTO}",
                s.RAW / "openalex_citing" / f"{k}_citing_p1.json", "openalex_citing")

def probes():
    for src, u, fn in [("scopus_api_probe", "https://api.elsevier.com/content/search/scopus?query=TITLE-ABS-KEY(design%20fixation%20sustainab*)", "scopus_probe.json"),
                       ("wos_starter_probe", "https://api.clarivate.com/apis/wos-starter/v1/documents?q=TS%3D(design%20fixation)", "wos_probe.json")]:
        s.fetch(u, s.RAW / "database_access_probe" / fn, src, terms="Access probe without credentials")

def keyword():
    for k, q in QUERIES.items():
        print(k, s.crossref_search(k, q)[0], s.openalex_search(k, q)[0], flush=True); time.sleep(1)

def network():
    for k, w in SEEDS.items():
        page = 1
        while True:
            u = f"https://api.openalex.org/works?filter=cites:{w}&per-page=200&page={page}&select={SEL}&mailto={s.MAILTO}"
            st, p = s.fetch(u, s.RAW / "openalex_citing" / f"{k}_citing_p{page}.json", "openalex_citing")
            n = json.load(open(p))["meta"]["count"]
            if page * 200 >= n: break
            page += 1
        st, p = s.fetch(f"https://api.openalex.org/works/{w}?select=id,referenced_works&mailto={s.MAILTO}",
                        s.RAW / "openalex_refs" / f"{k}_refs.json", "openalex_refs")
        refs = json.load(open(p))["referenced_works"]
        for i in range(0, len(refs), 50):
            ids = "|".join(r.split("/")[-1] for r in refs[i:i + 50])
            s.fetch(f"https://api.openalex.org/works?filter=openalex:{ids}&per-page=50&select={SEL}&mailto={s.MAILTO}",
                    s.RAW / "openalex_refs" / f"{k}_refs_meta_{i // 50}.json", "openalex_refs_meta")

def candidates(listfile):
    for d in open(listfile).read().split():
        fn = d.replace("/", "_")
        s.fetch(f"https://api.openalex.org/works/doi:{d}?mailto={s.MAILTO}", s.RAW / "candidate_openalex" / f"{fn}.json", "openalex_work")
        s.fetch(f"https://api.unpaywall.org/v2/{d}?email={s.MAILTO}", s.RAW / "candidate_unpaywall" / f"{fn}.json", "unpaywall",
                terms="Unpaywall API metadata"); time.sleep(0.3)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("keyword", "all"): keyword()
    if mode in ("network", "all"): network()
    if mode in ("network2", "all"): network2()
    if mode in ("probes", "all"): probes()
    if mode in ("candidates", "all"):
        for f in ("candidates.txt", "candidates2.txt", "candidates3.txt"): candidates(Path(__file__).parent / f)
