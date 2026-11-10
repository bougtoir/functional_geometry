# Function Before Form — Prior-Art Closure and Endpoint Feasibility Gate

Continuation of `../function_before_form_gate/`, which is unchanged. Gate-only: no manuscript, experiment or simulation.

- `01`–`11`: endpoint feasibility gate. `12`–`21`: full-text reconciliation gate. `22`–`33`: final prior-art and pilot-preparation gate. `FINAL_HANDOFF.md` covers both.
- `scripts/search_literature.py`: copied from the prior gate. ROOT points to this directory.
- `scripts/run_gate2_search.py`: Gate 2 keyword, citation-network and candidate retrieval (`keyword|network|candidates|all`).
- `scripts/cdp_fetch.py`: saves publicly visible pages via the session Chrome (CDP), with ledger rows.
- `data/raw/literature_search/search_ledger.csv`: source, URL, UTC, HTTP status, path, bytes, SHA-256, terms for every retrieval.
- `data/processed/ledger_verification.csv`: re-check of existence, size and hash.

Local-only (gitignored, licence): `data/raw/fulltext/` (including the user-provided PDFs), `data/processed/fulltext_txt/`, the evidence ZIPs. Files whose names end in `_unledgered_failedrun` come from an aborted first run whose ledger write failed. They are kept, not deleted, and are superseded by ledgered re-fetches.
