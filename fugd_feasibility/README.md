# FUGD novelty feasibility gate

Phase 1–2 gate for "Functional Unit Granularity Design" (successor idea to the CTEP functional-geometry study). Result: **NO-GO** — see `FINAL_HANDOFF.md`.

* `01_EXISTING_RESEARCH_INVENTORY.md` … `05_NOVELTY_FEASIBILITY_GATE.md` — gate deliverables
* `scripts/search_literature.py` — Crossref/OpenAlex/Semantic Scholar retrieval with ledger (`data/raw/literature_search/search_ledger.csv`)
* `scripts/check_equivalence_propositions.py` — exhaustive checks of the reduction claims → `results/equivalence_checks.json`
* Tests: `python -m pytest fugd_feasibility/tests`
