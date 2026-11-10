# 01 Existing research inventory (PHASE 1)

Branch: `devin/1794281295-fugd-novelty-gate` (fork of the `functional_geometry` work; nothing in `functional_geometry/` outside `fugd_feasibility/` was modified).

## 1. Assets

| Asset | Location | Status / content |
|---|---|---|
| CTEP final manuscript | `submission/Manuscript.docx`, `manuscript/manuscript_template.md`, `functional_geometry_CTEP_submission_FINAL_REVISED.zip` | "A service-normalized screening framework for geometric source reduction in disposable products"; desk-rejected (see `reports/CTEP_desk_rejection_gate.md`) |
| JCLP manuscript | `functional_geometry_JCLP_submission_FINAL.zip`, `FINAL_HANDOFF_JCLP.md` | Earlier framing; desk-rejected for insufficient novelty (`reports/JCLP_desk_rejection_gate.md`) |
| Core analytical model | `scripts/fgo_model.py` | Closed-form material ratios and break-even boundaries (functions listed in §2) |
| Toilet-paper width reduction | `toilet_width_material_ratio`, `toilet_width_saving`, `longitudinal_break_even_ratio` | M = (w_new/w_old)^(1+ε); break-even length ratio w_old/w_new |
| Centre longitudinal perforation | `center_perforation_material_ratio`, `center_perforation_break_even_probability` | M = (1−p)·m_full + p·0.5·m_half; break-even p with optional penalty |
| Straw–container co-design | `straw_material_ratio_*`, `straw_*_break_even`, `exact_hollow_cylinder_mass_g`, `max_integer_pack` | Retained length × replacement/failure inflation + shifted container burden; packing count |
| Monte Carlo | `run_monte_carlo` (seed 20260924, 200 000 draws, `config/scenarios.json`); `results/monte_carlo_*.csv.gz`, `monte_carlo_convergence.csv`, `one_way_sensitivity.csv` | Scenario (assumed) distributions, not measured |
| Public patent / spec data | `data/processed/patent_source_registry.csv` (15 rows), `pg_patent_table2_observed.csv`, `pg_patent_table2_width_contrasts.csv` (9 contrasts), `toilet_paper_source_metadata.csv` | Only observed behavioural contrasts in the project: patent focus-group sheet counts by width |
| References | `reports/references_verified_final.csv`, `data/processed/references_verified_literature.csv` (63 rows) | DOI-verified |
| Numeric registry | `results/manuscript_values.csv` (50 values with evidence status) | Canonical source for manuscript numbers |
| Reproducibility tests | `tests/test_analysis.py` | `22 passed` on this branch (project `.venv`) |
| Hostile / adversarial reviews | `reports/CTEP_FINAL_HOSTILE_REVIEW.md`, `CTEP_ADVERSARIAL_REVIEW.md`, `FINAL_ADVERSARIAL_REVIEW.md`, `adversarial_review.md` | Prior criticism, incl. behaviour assumed not measured |
| Hard-code audits | `reports/CTEP_NUMERIC_HARDCODE_AUDIT.md`, `CTEP_HARDCODE_FINDINGS.csv`, `HARD_CODING_AUDIT.md` | Registry-driven numbers |
| Prior novelty gate | `reports/CTEP_NOVELTY_GATE.md`, `CTEP_CLOSEST_PRIOR_STUDIES.csv` | Earlier GO was for a *screening/falsification instrument*, not a new optimisation problem |

## 2. What the existing models actually are

All three cases are one-line expected-value identities with a single break-even boundary:

* width: material ratio r^(1+ε) with r = w_new/w_old; break-even ε* such that ratio = 1;
* centre perforation: two-outcome mixture (full / half), break-even selection probability p*;
* straw: retained fraction × (1 + extra replacement) or ÷ (1 − failure), plus shifted burden.

None contains a decision variable that is optimised; each evaluates a fixed design against a baseline.

## 3. Evidence from the two desk rejections (treated as research data)

* JCLP: "insufficient novelty" — the break-even arithmetic was judged elementary.
* CTEP: re-positioned as a screening/falsification framework; desk-rejected. Common thread in both gate reports: (i) mathematical content is elementary; (ii) behaviour/task distributions are assumed, not measured; (iii) no empirical validation.

Implication for this gate: a successor contribution must add something the editors did not see — either non-trivial mathematics, decision value that the break-even identities cannot deliver, or measured data. Renaming the same mixture model would repeat the JCLP failure.

## 4. Measured vs assumed inventory

| Quantity | Status |
|---|---|
| Sheet dimensions, roll specifications, patent focus-group sheet counts | Measured / published (public patents, specifications) |
| Usage elasticity ε, half-sheet suitability p, task-unit multipliers, straw failure/replacement rates | Assumed scenario distributions |
| Task requirement distribution (area, width, length per use) | **Not available** |
| User selection behaviour under different perforation granularities | **Not available** |
| Manufacturing loss / perforation strength vs granularity | Qualitative only (tissue converting literature) |
