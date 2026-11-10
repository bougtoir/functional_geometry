# 16 — Targeted Search Closure

## 1. Database access (actual)

| Database | Status in this VM | Evidence |
|---|---|---|
| **Scopus** | **Not accessible.** The Elsevier Search API returned HTTP 401 "Invalid API Key"; no institutional key available | `data/raw/literature_search/database_access_probe/scopus_probe.json` (ledger row) |
| **Web of Science** | **Not accessible.** The Clarivate WoS Starter API returned HTTP 401 "No API key found" | `.../database_access_probe/wos_probe.json` |
| Google Scholar | Not used (no API; automated querying not permitted) | — |
| OpenAlex | Used: keyword queries, forward and backward citations, author records | `openalex/`, `openalex_citing/`, `openalex_refs/`, `openalex_author/` |
| Crossref | Used: keyword queries, author query, DOI records | `crossref/`, `candidate_crossref/` |
| Unpaywall | Used: legal OA locations | `candidate_unpaywall/` |
| Publisher / repository pages | Anonymous only: ScienceDirect, SpringerLink, MDPI, Cambridge Core, UJI repository | `data/raw/fulltext/` (local-only) |
| User-provided full texts | Collado-Ruiz 2010; Ross et al.; Collado-Ruiz et al. 2012 (CIIP) | ledger rows `user_provided` |

No access was fabricated. Scopus/WoS coverage remains **absent**.

## 2. Citation tracing completed

| Seed | Forward (citing) | Backward (refs) | Screened |
|---|---|---|---|
| Collado-Ruiz 2010 | 83 | 77 | title |
| Faludi 2020 | 15 | 83 | title |
| Linsey 2010 | 409 | 89 | title (environmental terms) |
| Devanathan 2010 | 174 | 26 | title |
| **Liao & MacDonald 2021 (new seed)** | 12 | 77 | title |
| **Greeley 2025 (new seed)** | 3 | 73 | title |
| **Ruiz-Pastor 2020 (new seed)** | 19 | 53 | title |
| **Ross 2022 (new seed)** | 15 | 42 | title |
| **Collado-Ruiz 2011 ICoRD chapter (new seed)** | 6 | 49 | title |

Conference proceedings covered:
- Design Society (ICED / DESIGN / Proceedings of the Design Society) and ASME IDETC records, to the extent that OpenAlex/Crossref index them.
- They appear in the citing sets above, e.g. ICED 2019 and PDS 2026.

## 3. New hits from this round

| Study | Relevance | Effect |
|---|---|---|
| **Ruiz-Pastor, Borgianni & Chulvi 2024**, IJDCI, doi:10.1080/21650349.2024.2316915 (FT, OA AAM) | Environmental objectives in **design briefs** plus sustainability stimuli; 34 junior designers; two 30-min problems; blinded two-expert assessment (circularity via the Circular Economy Toolkit, r = 0.62; novelty, r = 0.65) | **Directly overlaps** the "brief → environmental outcome" claim. Its outcome is circularity, not impact per FU. Null result |
| **Alzayed, Starkey, Ritter & Prabhu 2025**, IJDCI, doi:10.1080/21650349.2025.2544267 (AB, closed) | Creativity- vs sustainability-focused **design goal**; rated environmental sustainability | **Directly overlaps** the brief-emphasis manipulation. Null result per abstract. Full text not read |
| Alzayed et al. 2025, *Design Science*, doi:10.1017/dsj.2025.10018 (AB; OA available) | Accuracy of designers' self-evaluated sustainability against experts | Endpoint-relevant: shows that environmental judgements of concepts are noisy |
| Lo Guzzo et al. 2026, *Proc. Des. Soc.*, doi:10.1017/pds.2026.10497 (AB; OA available) | Parametric fast LCA validated against ISO LCA (MAPE < 5%) in early embodiment design | Endpoint-method precedent (later stage than concepts) |
| CIIP 2012 announced experiments (Collado-Ruiz group) | No published results found (OpenAlex author A5036721753; Crossref author query) | Residual risk |

## 4. Is a limited closure defensible without Scopus/WoS?

**Not as "closure".** This round found two directly overlapping studies from 2024–2025 through only five additional seeds. The literature is active, and title-level screening of OpenAlex/Crossref is demonstrably incomplete.

A **limited novelty assessment** is defensible and is documented in 15:
- the endpoint combination N6/N7/N10 was not found in any source searched;
- the manipulation (N1/N3) is not new.

This must be reported as "not found in OpenAlex, Crossref and citation tracing", **not** as "does not exist".

Required to close:
- Scopus and WoS with the query families in 02 §2, plus "design brief" AND (sustainab* OR environment*) AND (experiment* OR randomi*) AND (LCA OR "life cycle" OR "functional unit");
- the full text of Alzayed et al. 2025 (IJDCI);
- an author search for Collado-Ruiz / Bastante-Ceca / Capuz-Rizo, 2012–2016, including theses (RiuNet, TESEO).
