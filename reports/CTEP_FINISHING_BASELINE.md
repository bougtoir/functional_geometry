# CTEP finishing baseline — STEP 1

Recorded 2026-10-18 (UTC). Finishing prompt: CTEP_final_novelty_hostile_hardcode_Devin.txt.

## Git state at baseline

- Branch at prompt receipt: `devin/1792323011-ctep-retarget` at `6e12388d1`; PR bougtoir/wip#705 merged as `c3f50f8a7`.
- Finishing work proceeds on new branch `devin/<ts>-ctep-finishing` cut from merged `master` (per merge policy).
- Canonical working tree: `~/repos/wip/functional_geometry/` (single VM, sequential).

## Journal-upload files vs internal audit deliverables

Journal-upload (in `functional_geometry_CTEP_submission_FINAL_REVISED.zip`):

- `submission/Manuscript.docx`, `Manuscript.pdf`
- `submission/Title_page.docx`
- `submission/Cover_letter.docx`
- `submission/Supplementary_material.docx`, `Supplementary_material.pdf`
- `submission/Highlights.docx`, `Highlights.txt`
- `submission/Tables_editable.docx`
- `submission/Graphical_abstract.png`, `Graphical_abstract_editable.pptx`
- `submission/Figures_overview.pptx`
- `submission/separate_figures/*` (png/pdf/svg per figure 1–5)
- `submission/submission_manifest.csv`

Internal audit deliverables (repository only, NOT in zip):

- `reports/CTEP_BASELINE.md`, `CTEP_JOURNAL_GATE.md`, `CTEP_CLOSEST_PRIOR_STUDIES.csv`,
  `CTEP_CITATION_ECOLOGY.md`, `CTEP_NOVELTY_GATE.md` (new this pass),
  `CTEP_ADVERSARIAL_REVIEW.md`, `CTEP_REVISION_ACTIONS.md`,
  `CTEP_FINAL_HOSTILE_REVIEW.md` (new), `CTEP_NUMERIC_HARDCODE_AUDIT.md` (new),
  `CTEP_DATA_TEXT_FIGURE_CONSISTENCY.md` (new), `CTEP_AUTHOR_ACTIONS.md` (new),
  `CTEP_FINAL_QC.md`, `CTEP_desk_rejection_gate.md`, `final_QC.md`
- `FINAL_HANDOFF_CTEP.md`, `reports/MANUAL_SUBMISSION_ITEMS.md`

## Inventory status

| Item | State |
|---|---|
| Canonical manuscript (`submission/Manuscript.docx` ← `manuscript/manuscript_template.md` + `results/manuscript_values.csv`) | EXISTS |
| Submission ZIP | EXISTS (renamed `..._FINAL_REVISED.zip` this pass) |
| Author details | VERIFY: affiliation/address/ORCID confirmed from prior project records; position and institutional email NOT confirmed → flagged |
| Source registry (`data/processed/source_registry.csv`, acquisition ledgers) | EXISTS |
| Closest-prior report (`CTEP_CLOSEST_PRIOR_STUDIES.csv`, 13 rows) | EXISTS |
| Journal-fit gate (`CTEP_JOURNAL_GATE.md`) | EXISTS, verified 2026-10-18 |
| Adversarial review (`CTEP_ADVERSARIAL_REVIEW.md`) | EXISTS; refreshed + final hostile pass this session |
| Final QC (`CTEP_FINAL_QC.md` / `final_QC.md`) | EXISTS; 53 checks PASS after finishing edits |
| `CTEP_NOVELTY_GATE.md` | MISSING → created |
| `CTEP_NUMERIC_HARDCODE_AUDIT.md`, `CTEP_DATA_TEXT_FIGURE_CONSISTENCY.md` | MISSING → created |
| `CTEP_AUTHOR_ACTIONS.md` | MISSING → created |

## Frozen assets reused unchanged

- `results/` tables + Monte Carlo outputs (seed 20260924, 200,000 draws) — NOT re-run; identity verified by run_qc (53 checks: patent contrasts recomputed == stored; MC summaries == registry).
- `figures/` — regenerated only at last full `make all` (11:31); analysis code unchanged since; byte-stable inputs confirmed by QC's patent/registry checks.
- `data/processed/` registries and `data/raw/` acquisition snapshots.
