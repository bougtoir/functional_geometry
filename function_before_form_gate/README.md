# Function Before Form — research gate (gate only, no manuscript)

Separate from the FUGD gate (`../fugd_feasibility/`) and from existing CTEP/JCLP outputs, which are unchanged.

Reproduce searches: `python3 scripts/search_literature.py {search|search2|search3|doi FILE|openalex FILE|fulltext FILE}`. Every response is written to `data/raw/` and appended to `data/raw/literature_search/search_ledger.csv` (source, URL, UTC time, HTTP status, path, bytes, SHA-256, terms). Existing files are never overwritten (timestamp suffix).

Committed: Crossref/OpenAlex/Unpaywall metadata (CC0) and processed lists. Local only (gitignored): OA full texts, extracted text, landing pages, Semantic Scholar responses, publisher pages.
