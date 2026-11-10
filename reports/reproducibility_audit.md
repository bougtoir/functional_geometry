# Reproducibility audit

## Verdict

The computational package was rebuilt from the checked-in processed inputs with `make all`. Public-source acquisition is separately available through `make acquire` because network responses and source versions can change.

## Environment

- Python: 3.10.12
- NumPy: 2.2.6
- pandas: 2.3.3
- Build commit: 1f54637c4ed4d7ace82c04b295cff530a10324c1
- Fixed random seed: 20260924
- Monte Carlo iterations: 200000

## Commands and status

- `make all`: PASS when this report was generated
- `.venv/bin/python -m pytest -q`: `......................                                                   [100%]
22 passed in 0.48s`
- `.venv/bin/python -m compileall -q scripts tests`: PASS
- Working-tree status at `make all` start: `M README.md
 M config/references.json
 M manuscript/manuscript_template.md
 M reports/MANUAL_SUBMISSION_ITEMS.md
 M scripts/build_submission.py
 M scripts/run_qc.py
 M submission/Cover_letter.docx
 M submission/Figures_overview.pptx
 M submission/Graphical_abstract_editable.pptx
 M submission/Highlights.docx
 M submission/Manuscript.docx
 M submission/Manuscript.pdf
 M submission/Supplementary_material.docx
 M submission/Supplementary_material.pdf
 M submission/Tables_editable.docx
 M submission/Title_page.docx
?? functional_geometry_CTEP_submission_FINAL.zip
?? reports/CTEP_BASELINE.md
?? reports/CTEP_CITATION_ECOLOGY.md
?? reports/CTEP_CLOSEST_PRIOR_STUDIES.csv
?? reports/CTEP_JOURNAL_GATE.md`

## Inputs and provenance

- Public acquisition records: 94
- Nonempty snapshots: 85
- Failed or empty retrievals retained: 9
- Manuscript values: 50 registered values with method and source-file fields
- Selected references: 31 in reports/references_verified_final.csv

Raw public-source snapshots are retained locally under `data/raw`; redistribution remains source-specific. Acquisition metadata include URL, UTC retrieval time, local path, size, SHA-256 checksum, status, and usage note.

## Automated evidence

- Tests: `......................                                                   [100%]
22 passed in 0.48s`
- Python compilation: PASS
- Manuscript PDF: 28 pages
- Submission archive integrity: PASS
- Unresolved rendered placeholders: 0
- Reference records without `UNVERIFIED`: 31/31
- Claim-source records without unsupported status: 25/25

## Remaining manual steps

- Verify the prefilled affiliation/correspondence fields and complete funding, competing-interest, and author-contribution statements.
- Create a versioned public release and insert its DOI or persistent identifier.
- Add an author-selected project license.
- Review the system-generated Editorial Manager PDF.

## Interpretation boundary

The Monte Carlo distributions are transparent scenario distributions. They do not estimate population probabilities. The work is a material-flow and scenario analysis, not a human-use trial or full life-cycle assessment.
