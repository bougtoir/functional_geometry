# 24 — Scopus / Web of Science Closure

## 1. Access attempts (2026-11-10 UTC; raw responses with ledger rows)

| Route | Result |
|---|---|
| Scopus Search API | HTTP 401 "Invalid API Key" (`database_access_probe/scopus_probe.json`) |
| Scopus web, via session browser | HTTP 200, but only the public **Scopus Preview** page with "Sign in" / "Check access". No institutional session, so document search is unavailable (`database_access_browser/scopus_browser.*`) |
| WoS Starter API | HTTP 401 "No API key found" |
| WoS web, via session browser | HTTP 403 Cloudflare block (`database_access_browser/wos_browser.*`) |

**Neither database was searched.** No credentials were invented, and no access control was bypassed. **Prior-art closure is not complete.**

## 2. Manual search protocol for the author (university library access)

Run each string once in **Scopus** (Advanced search) and once in **WoS Core Collection** (Advanced search). Use **no date filter**, Article / Conference paper / Review, all languages. Export results (RIS + CSV) and return the files. They will be ledgered under `data/raw/scopus_wos_exports/`, and screening will be recorded as PRISMA-style counts.

**Scopus:**
- S1 `TITLE-ABS-KEY(("design brief*" OR "problem framing" OR "problem statement" OR "design goal*" OR "framing") AND (sustainab* OR environment* OR eco*) AND (ideation OR "concept generation" OR "idea generation" OR "conceptual design") AND (experiment* OR randomi* OR "controlled study"))`
- S2 `TITLE-ABS-KEY(("design fixation" OR fixation) AND (sustainab* OR ecodesign OR "eco-design" OR "design for environment") AND (experiment* OR study))`
- S3 `TITLE-ABS-KEY(("life cycle assessment" OR LCA OR "carbon footprint" OR "functional unit") AND ("generated concepts" OR "design concepts" OR "conceptual designs" OR ideas) AND (experiment* OR participants OR students OR designers))`
- S4 `TITLE-ABS-KEY(("material substitution" OR "material selection") AND ("function*" OR "redesign") AND (ideation OR "concept generation") AND (sustainab* OR environment*))`
- S5 `TITLE-ABS-KEY(("functional equivalence" OR "functional unit") AND (ideation OR "concept generation" OR "design experiment"))`
- S6 `AUTHOR-NAME(Collado-Ruiz) OR AUTHOR-NAME(Ostad-Ahmad-Ghorabi) OR (AUTHOR-NAME(Bastante-Ceca) AND TITLE-ABS-KEY(creativ* OR ideation OR "environmental information"))`

**WoS:** use the same strings, with `TS=(...)` in place of `TITLE-ABS-KEY(...)` and `AU=(...)` in place of `AUTHOR-NAME(...)`.

Also:
- In each database, run forward citations of Collado-Ruiz 2010, Liao & MacDonald 2021, Ruiz-Pastor 2024, Alzayed 2025 and Ross 2022.
- Search TESEO by director "Collado Ruiz, Daniel".

**Stop rule:** NO-GO if any record reports a quantitative, functional-unit-based environmental assessment of experiment-generated concepts under manipulated brief conditions (25 §3).
