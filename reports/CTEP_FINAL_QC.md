# CTEP final QC — Phase 6

Date: 2026-10-18. Branch `devin/1792323011-ctep-retarget`. **PASS.**

## Mechanical checks

- `make all` (preflight → analysis → manuscript → 22 tests → lint → `make qc`): PASS.
- `run_qc.py`: 53 checks, 0 FAIL (`reports/final_QC.md`, `reports/CTEP_desk_rejection_gate.md` regenerated).
- Abstract: 229 words (limit 150–250). Keywords: 6 (limit 4–6). Reference count: 31.
- Rendered manuscript PDF: title matches title page; all `{{...}}`/`{cite:...}`/`[[...]]` placeholders resolved; 45 OMML equations present in Manuscript.docx; no LaTeX artifacts in extracted text.
- References: Springer name–date format verified mechanically (`(year)` pattern all 31 entries), alphabetized, DOIs as `https://doi.org/...` links; zero UNVERIFIED records in `references_verified_final.csv`.
- Cover letter: 450 words, first-person singular only (zero we/our/us occurrences), CTEP addressee, no JCLP mention.
- Archive `functional_geometry_CTEP_submission_FINAL.zip`: `unzip` listing verified; contains full upload set + `separate_figures/` PNG/PDF/SVG for Figures 1–5.

## Numerical consistency (frozen values vs canonical pipeline)

All headline values regenerated unchanged: 114→95 mm = 16.7%; break-even 1.20 (+20%); 9 patent contrasts −20.0% to +18.4% (4+/5−); task-mix 10/20/30%; straw 25.0% rate vs 20.0% probability at 20% shortening; packing 360/540/600 at 165/132/115.5 mm; MC mean 0.0636/median 0.0685/[−0.0393, 0.1472]. Sources: `results/manuscript_values.csv` → manuscript placeholders (no hard-coded derived values introduced by retarget edits — verified: template diff touches only title, abstract framing sentence, one intro paragraph, declarations block).

## Claim checks

- No population-effectiveness, universal-optimum, full-LCA, transport-emission, patentability/FTO, or universal-PFAS claims introduced.
- FGO remains labeled study-specific analytical lens; contribution framed as integration + falsification framework.
- Data/code availability statement remains true (public repo unchanged; nothing removed).

## Known residual risks (disclosed, not fixable with existing evidence)

- Desk-rejection risk on novelty persists (editorial discretion); mitigated by CTEP's models-and-methods scope and retargeted framing.
- A referee may still request empirical validation; the paper's answer is the staged validation protocols in §4.9.

**Verdict: PASS — package is ready for author completion and submission.**
