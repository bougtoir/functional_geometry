# Straw-source snapshots

Public-source snapshots used by `reports/straw_container_evidence.md` are retained
locally in this directory but are not committed because source redistribution terms
vary.

`reports/acquisition_ledger.tsv` records each file's source/provenance, acquisition
timestamp, retrieval condition, local path, byte size, SHA-256, status, and usage
condition. Failed and partial retrievals are preserved and labelled; they are not
used as valid evidence.

To reconstruct the source set, retrieve each URL in the ledger under its stated
condition, preserve the original response without overwriting earlier snapshots,
and compare its size and SHA-256 with the recorded snapshot. A changed upstream
file is a new source version, not an exact reconstruction.
