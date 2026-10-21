# CTEP retarget — Phase 0 baseline

Date (UTC): 2026-10-18
Working tree: `bougtoir/wip` master @ `c4fcd240d` (clean), `functional_geometry/` canonical project.

## Verified state (carried from JCLP package)

- Package-producing commit: `492e00371` (per FINAL_HANDOFF_JCLP.md); handoff commit `97c8b8e49`.
- Canonical manuscript source: `manuscript/manuscript_template.md` (331 lines; `{{num:...}}`/`{{pct:...}}` placeholders resolved from `results/manuscript_values.csv` at build time — derived values are not hard-coded).
- Canonical artifacts present: `submission/{Manuscript.docx, Manuscript.pdf, Title_page.docx, Cover_letter.docx, Highlights.docx/.txt, Supplementary_material.docx/.pdf, Tables_editable.docx, Figures_overview.pptx, Graphical_abstract.png/_editable.pptx}`, figure SVG/PDF/PNG for Figures 1–5, `submission_manifest.csv`.
- Data: `data/processed/` (patent contrasts etc.); Monte Carlo gzip CSVs under `results/`; `config/scenarios.json` scenario registry; `config/references.json`; `config/claim_audit.json`.
- Reports inventory: CLAIM_SOURCE_AUDIT, adversarial review + revision response, HARD_CODING_AUDIT, JCLP desk-rejection gate (CONDITIONAL PASS), JCLP_requirements, patent metadata audit, reproducibility/clean-rebuild/logic audits, source registry, references_verified_final.csv (0 UNVERIFIED).
- Tests/QC previously: 22 tests, 53 QC checks PASS; `make all` clean build PASS; public mirror https://github.com/bougtoir/functional_geometry verified by tree hash.
- Prior handoff verdict: READY FOR AUTHOR COMPLETION AND SUBMISSION (JCLP). JCLP then desk-rejected JCLEPRO-D-26-35955 for insufficient novelty/overlap (no external review).

## Frozen headline values (consistency checkpoints, from manuscript_values.csv)

- 114→95 mm nominal 16.7% area reduction; longitudinal break-even ratio 1.20 (+20%).
- 9 patent contrasts, −20.0% to +18.4%, 4 positive / 5 negative (verified identities: US453003A Hicks; WO2003026472A1 Friedrich; US20160345786A1 Olson et al./Georgia-Pacific; US6458450B1 Steinhardt et al./P&G).
- Center perforation: task-mix savings 10/20/30%; two halves for one task → zero area saving.
- Straw 20% shortening, zero shifted burden: 25.0% expected-additional-replacement-rate break-even vs 20.0% independent per-attempt failure probability (distinct formulations; 10%/30% rows 11.1/14.3% wait — see table_4: 11.1%/25.0%/42.9% rate; 10%/20%/30% probability).
- Integer packing (hypothetical): 165/132/115.5 mm → 360/540/600 units per carton.
- MC: seed 20260924, 200,000 draws; width MC mean 0.0636, median 0.0685, p2.5 −0.0393, p97.5 0.1472.

## Rules for retarget

- Analyses FROZEN; rerun only on specific discrepancy. Methods/Results essentially frozen; retarget edits limited to title, abstract, intro, discussion, conclusions, cover letter, journal-specific apparatus.
- No new empirical claims; no fabrication; single-author I/my cover letter; zero mandatory fees required (non-OA subscription route must be verified CURRENT).
- Submission to a journal only by the author; Devin prepares package + PR only.
