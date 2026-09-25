# Functional geometry optimization

Reproducible multi-case quantitative modeling and scenario analysis for reducing material demand through product geometry. The three cases are toilet-paper width reduction, selectable half-width through longitudinal center perforation, and straw shortening through straw–container co-design.

The package is designed for a *Journal of Cleaner Production* Original article. It is not a human-use trial or a full life-cycle assessment.

## One-command reproduction

Python 3.10 and LibreOffice are required.

```bash
make setup
make all
```

`make all` regenerates processed analytical outputs, figures, tables, the editable manuscript, PDF, supplementary and submission files, tests, and quality-control reports.

## Public-source acquisition

```bash
make acquire
```

Acquisition is separate from `make all` because public pages and APIs can change. Snapshots are written under `data/raw/` without overwriting earlier copies. The machine-readable ledger records URLs, UTC retrieval times, status, local path, file size, SHA-256 checksum, and usage notes. Failed and empty captures are retained.

Raw snapshots are intentionally ignored by Git because redistribution rights vary. Checked-in processed data, source registries, and acquisition summaries are sufficient to reproduce the analytical package. Re-running acquisition creates a new snapshot rather than silently replacing the original.

## Main commands

| Command | Purpose |
|---|---|
| `make analysis` | Rebuild models, Monte Carlo results, figures, tables, and manuscript values |
| `make manuscript` | Build DOCX, PDF, editable tables, figure overview deck, highlights, cover letter, graphical abstract, supplement, and ZIP |
| `make test` | Run analytical unit tests |
| `make lint` | Compile Python source and tests |
| `make qc` | Run JCLP, traceability, archive, and reproducibility checks |
| `make all` | Run the complete deterministic build |

## Structure

```text
config/       fixed scenarios and selected references
data/raw/     persistent public-source snapshots and acquisition summaries
data/processed/ redistributable analytical inputs
figures/      publication figures in PNG, PDF, and editable SVG
manuscript/   Markdown manuscript source with dynamic placeholders
reports/      evidence reviews, registries, audits, and JCLP checks
results/      fixed-seed simulations, sensitivity, and value traceability
scripts/      acquisition, analysis, manuscript build, and QC
submission/   generated editable and rendered submission files
tables/       machine-readable manuscript tables
tests/        analytical unit tests
```

## Numerical traceability

All manuscript result placeholders are resolved from `results/manuscript_values.csv`. Each value has an identifier, unit, source file, method, evidence status, and manuscript location. Citation placeholders are rendered in JCLP author–year style from structured author, year, and reference metadata in `config/references.json`; the reference list is ordered alphabetically.

The fixed Monte Carlo seed and iteration count are stored in `config/scenarios.json`. Reported positive proportions are properties of the configured scenario distributions, not empirical population probabilities.

## Evidence labels

- `OBSERVED`: directly recorded public dimensions or source facts.
- `SOURCED`: a coefficient or claim supported by an external source.
- `CALCULATED`: deterministic transformation of identified inputs.
- `ASSUMED_SCENARIO`: transparent hypothetical input used for stress testing.

## Submission output

The generated archive is `functional_geometry_JCLP_submission_FINAL.zip`. It contains the manuscript, rendered PDF, title page, cover-letter draft, highlights, supplement, separate editable tables, a raster-preview overview deck, an editable native-shape graphical abstract, and the manifest. Each analytical figure is included separately as publication-resolution PNG/PDF plus editable SVG source in `separate_figures/`.

The public project repository is https://github.com/bougtoir/functional_geometry. Before journal submission, create a versioned release for the exact submitted commit and insert its DOI or other persistent identifier in the manuscript.

The submitting author must complete affiliation/correspondence fields and confirm originality, exclusive consideration, authorship approval, and final CRediT roles. These facts are not inferred by the build.

## License and source terms

No project-level reuse license has yet been selected. Until the author adds one, ordinary copyright applies to project code and redistributable derived data. External source snapshots retain their original terms. Patent, publisher, product, and standards material must not be redistributed merely because it was publicly retrievable.
