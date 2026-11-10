# Clean-environment rebuild

## Procedure

A separate persistent copy was created without the project virtual environment or generated `figures/`, `tables/`, `results/`, `submission/`, and ZIP outputs.

```bash
make setup
make all
```

## Result

- Dependency installation completed from `requirements.txt`.
- Analysis generated five figures and six tables.
- Manuscript and submission archive generation completed.
- Seven analytical tests passed.
- Python compilation passed.
- Eighteen QC checks passed.

## Deterministic analytical checksums

| File | SHA-256 |
|---|---|
| `results/manuscript_values.csv` | `5a2142cccfcc4fec4ff6cb10b9824658235389422b8181f885a276a365d83cb5` |
| `results/monte_carlo_convergence.csv` | `aa6e7eba7cadcba1229d3e3a747eab7b705109d6118a16d3f43a6d7ea93c524b` |
| `tables/table_6_monte_carlo_summary.csv` | `257f81ea11640da59c58e136e971dcc848c137e9ad4be27deb4c983ea5900cf0` |

The checksums were identical between the working checkout and clean rebuild. DOCX, PDF, and ZIP binary hashes differ because office files embed build timestamps; their content-level QC results were identical.
