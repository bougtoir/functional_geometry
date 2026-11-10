# 02 — Targeted Literature Search

## 1. Databases actually searched

| Source | Used for | Status |
|---|---|---|
| **OpenAlex API** | 12 new keyword queries (g01–g12); forward citations (`filter=cites:`) and backward references (`referenced_works`) for 4 seed studies; per-candidate records with abstracts | Complete for the queries listed; all pages saved |
| **Crossref REST API** | Same 12 keyword queries; DOI records | Complete for the queries listed |
| **Unpaywall API** | OA status and legal OA location for 30 candidates and the mandatory study | Complete |
| **Semantic Scholar Graph API** | Single-record lookup of Collado-Ruiz 2010 only | Not used as a search database |
| **Publisher landing pages** (ScienceDirect, SpringerLink, MDPI, Cambridge Core), viewed anonymously in the session browser | Abstracts, snippets and OA full texts | Only pages visible without login |
| CORE, UPV RiuNet | Author-repository copy of Collado-Ruiz 2010 | HTTP 403 / no retrievable hit |
| **User-provided full texts** (institutional access) | Collado-Ruiz 2010, Ross et al. 2022, Collado-Ruiz et al. 2012 (CIIP) | Read in full; local-only |
| OpenAlex author record + Crossref author query (Collado-Ruiz) | Follow-up results of the experiments announced in CIIP 2012 | No published results found |

**Not searched: Scopus, Web of Science, Google Scholar.** No institutional credentials were available in this VM, and they were not requested at this gate. **The search is therefore not comprehensive**, and prior-art closure cannot be declared complete (special rule).

All raw responses are under `data/raw/literature_search/` (`openalex/`, `crossref/`, `openalex_citing/`, `openalex_refs/`, `candidate_openalex/`, `candidate_unpaywall/`, `collado_ruiz_2010_access/`). Each is logged in `search_ledger.csv` with UTC time, HTTP status, bytes and SHA-256. OA full texts and publisher HTML are local-only (`data/raw/fulltext/`, gitignored).

## 2. Keyword queries (OpenAlex + Crossref, 2 × 12)

g01 creativity × environmental sustainability of student ideas; g02 brief framing × sustainable ideation experiment; g03 problem framing × environmental impact of concepts; g04 LCA of concepts generated in ideation; g05 design fixation × sustainable design experiment; g06 material substitution vs redesign ideation; g07 abstract vs concrete problem statement experiment; g08 constrained vs open brief creativity; g09 streamlined LCA × conceptual design uncertainty; g10 environmental evaluation of ideas × rater agreement; g11 eco-ideation tool controlled experiment; g12 function-based impact × ideation. Exact strings are in `scripts/run_gate2_search.py`.

## 3. Citation network (OpenAlex)

| Seed | Citing works | References |
|---|---|---|
| Collado-Ruiz & Ostad-Ahmad-Ghorabi 2010 (W2072208931) | 83 | 77 |
| Faludi, Yiu & Agogino 2020 (W3089928046) | 15 | 83 |
| Linsey et al. 2010 (W2065406122) | 409 (3 pages) | 89 |
| Devanathan et al. 2010 (W2123356613) | 174 | 26 |

Screening procedure:
1. Title keyword filter: an environmental term **and** an ideation/experiment term. For Linsey's citing set, an environmental term alone was required. This flagged 210 citing titles and 104 keyword-query titles.
2. Manual title screening selected 29 candidates for record and abstract retrieval (`scripts/candidates.txt`, `candidates2.txt`).
3. OA full texts were retrieved where Unpaywall listed a legal copy. Nine were read or searched in full (see 03, `verification_level`).

**Limits.** Screening of the citing sets was title-level. OpenAlex citation coverage differs from the publisher's: ScienceDirect shows 74 citing works for Collado-Ruiz, OpenAlex 83, Semantic Scholar 87. Backward references were screened by title only.

## 4. What the search found

New studies closer to E3 than any in the prior gate:

1. **Liao & MacDonald 2021** (*Sustainability* 13:5227; FT-P).
   - Design: randomised pre-ideation activity (collage priming vs reading vs none). Task: "a next-generation sustainable washing machine".
   - Outcome: two expert judges rated idea relevance to environmental impact, cost and desirability.
   - Closest *design* to E3: manipulated pre-task framing, environmental outcome. But the endpoint is an expert relevance rating, not a quantity per functional unit.
2. **Greeley et al. 2025** (*Res. Eng. Des.* 36(4); FT-P).
   - Design: sustainable-design lecture before vs after the design task (treatment vs comparison).
   - Outcome: ideas rated for creativity and "environmental sustainability (i.e., material reuse, maximizing utility & accessibility, and corrective measures for use)", using rubric categories.
   - Its literature review notes that a sustainability expert-rating approach has "limited accessibility to domain experts" as a limitation.
3. **Ruiz-Pastor, Mulet, Chulvi & Royo 2020** (*JCP* 124758; FT, repository AAM).
   - Design: 6-3-5 method with vs without circular-economy guided questions.
   - Outcome: creativity, plus a semi-quantitative *circularity* count score.
   - Result: "no significant differences in creativity or circularity" (AAM p. 1); the null is reported.
4. **Ross, Ferrero & DuPont 2022** (*JMD* 144(3):032001; FT, user-provided). Three groups (control / guidelines / GREEn Quiz), toaster redesign, 30 min. Outcomes are counts of sustainability-related design decisions and 3 judges' 1–5 averaged ratings. No LCA, no agreement statistic.
5. **She & MacDonald 2013** (*JMD* 136(1); AB). Priming designers to generate features that *communicate* sustainability. The endpoint is communication, not environmental performance.
6. **Hu, Shealy & Milovanovic 2021** (*Design Science* 7:e5; FT). Problems with vs without added sustainability dimensions, in randomised order. Outcomes: number of solutions and fNIRS. No environmental assessment.
7. **Wasserbaur & Sakao 2020** (*Sustainability* 12:8104; FT). Conceptual paper plus a system-dynamics model of a laundry system. It distinguishes **design fixation** (controllable by the designer) from **design limitation** (imposed constraints, e.g. regulations and requirements). This distinction is central to Gate 5 identification.
8. **Cardin et al. 2013** (*Res. Eng. Des.* 24(3):277; AB; the MIT repository copy returned HTTP 429). An experimental method that evaluates concept-generation procedures by the *quantitative lifecycle performance* (economic, flexibility) of the generated concepts. It is a methodological precedent for scoring generated concepts with a quantitative lifecycle model, not an environmental one.
9. **Faludi et al. 2019** (ICED; FT). Methods change the *categories* of ideas, counted.
10. Context only, not a threat:
    - Krsteska & Du Bois 2026 (*Proc. Des. Soc.*; FT): problem-framing method, student evaluation, qualitative.
    - Escobar et al. 2023 (pedagogical, FT not analysed).
    - Ruiz-Pastor et al. 2021/2022: novelty–circularity metrics.
    - Tyl et al. 2014/2018: eco-ideation mechanisms.

**Not found** in the databases searched: any study that

(a) manipulates the *framing level* of the brief (material / form / function), **and**
(b) scores the participant's *final selected* concept with a functional-unit-based quantitative environmental model, **and**
(c) treats functional failure as a separate outcome.

As required, this absence is **not** treated as proof of novelty (see 04).
