# CTEP audit evidence summary — STEP 8 independent decision

Date: 2026-10-21 (UTC). Scope: audit-evidence retrieval for `functional_geometry_CTEP_submission_FINAL_REVISED.zip`. This document summarizes EXISTING audits plus narrowly scoped NEW verifications performed today (each marked).

## Canonical state (STEP 1)

- Repository: `~/repos/wip` (monorepo), subdir `functional_geometry/`.
- Branch `devin/1792…-ctep-audit-evidence`, base commit `1f54637c4` (master, contains merged PR #707 `83dfdd766` which produced the zip).
- Working tree at audit start: clean except the evidence files added by this task.
- Submission zip SHA-256: `4698e9f719409a174f70fa74b604c3dee61387aba76d743518fa67b676b07b24` — identical on merged master and on the finishing branch; provenance = built at `83dfdd766`, unchanged since (timestamps inside zip 2026-10-18 12:09–12:10).
- Canonical chain: `config/scenarios.json` + `data/processed/*.csv` → `scripts/run_analysis.py` → `tables/*.csv` + `results/manuscript_values.csv` + `figures/` → `scripts/build_submission.py` → `submission/*.docx/.pdf/.pptx` → zip. `scripts/run_qc.py` = 53 automated checks.

## Evidence matrix

| Dimension | Rating | Evidence |
|---|---|---|
| Novelty gate | PASS | EXISTING `reports/CTEP_NOVELTY_GATE.md`, `CTEP_CLOSEST_PRIOR_STUDIES.csv` (13 DOI-verified studies), `CTEP_CITATION_ECOLOGY.md`. GO as (B) integration + falsification framework; rubric fixed a priori (novelty 3/5, CTEP fit 4/5). JCLP "renamed eco-design + elementary arithmetic + assumed behavior" objection explicitly tested — response: no prior study provides pre-implementation pass/fail boundaries or a falsification structure; residual weakness: unvalidated behavioral parameters (disclosed) |
| Hostile review | PASS | EXISTING `CTEP_ADVERSARIAL_REVIEW.md` (pass 1) + `CTEP_FINAL_HOSTILE_REVIEW.md` (pass 2, independent) + `CTEP_REVISION_ACTIONS.md`. Every CRITICAL/MAJOR answered or disclosed; no unfixable CRITICAL. NEWLY VERIFIED 2026-10-21: no new defects found in consistency audit below |
| Analytical hardcoding | PASS | EXISTING `CTEP_NUMERIC_HARDCODE_AUDIT.md` + NEWLY PERFORMED machine-readable table `reports/CTEP_HARDCODE_FINDINGS.csv` (12 findings, file:line evidence). One genuine violation (cover-letter literals) was FIXED at source on PR #707 — now registry-derived. Remaining literals = documented config scenario constants. QC `headline_registry_ok`, `required_rendered_values` (30+ values), patent recompute == stored CSV |
| Data–text–figure consistency | PASS | EXISTING `CTEP_DATA_TEXT_FIGURE_CONSISTENCY.md`. NEWLY VERIFIED 2026-10-21: `run_qc` 53/53 PASS after repairing one self-inflicted stale-literal hit in the consistency report (the audit file quoted the stale strings the scanner looks for — reworded; package contents unaffected). PDF visual spot-check: 28 pages, Figures 1–5 and Tables 1–6 sequential with in-order first citations, page 12 (§2.7–2.8) renders correctly, no placeholders/overflow observed |
| Reference/claim support | PASS | `config/references.json` 31 entries Springer name–date format with DOI links; QC: 0 UNVERIFIED references; `config/claim_audit.json` + `reports/CLAIM_SOURCE_AUDIT.csv` claim→source support check PASS |
| Reproduction/tests | PASS | NEWLY VERIFIED 2026-10-21 on this VM: `.venv/bin/python -m pytest -q` → 22 passed (log: `reports/evidence_test_log_2026-10-20.txt`); `scripts/run_qc.py` → 53 checks PASS; Python 3.10.12, python-docx 1.2.0, python-pptx 1.0.2, pandas 2.3.3, numpy 2.2.6, matplotlib 3.10.9, scipy 1.15.3. Monte Carlo (seed 20260924, 200,000 draws) NOT re-run — frozen outputs verified identical via registry; run_qc `Tests pass` check re-runs pytest inside the pipeline |
| Journal eligibility / zero mandatory APC | PASS | `CTEP_JOURNAL_GATE.md`: official Springer journal-10098 pages accessed 2026-10-18 — scope covers "mathematical and computer-based methods and models"; article type Original research paper; hybrid model, subscription route = no APC/mandatory fees (optional OA £2,790/$4,290/€3,190 not selected). NEWLY VERIFIED only via prior live retrieval record; not re-fetched today — RECONFIRM in the portal at submission (publisher pages can change) |
| Author-only items | INCOMPLETE (by design) | `CTEP_AUTHOR_ACTIONS.md`: email discrepancy (records = bougtoir@gmail.com; institutional biwako address unverified), position title and phone unrecorded → left blank; submission date, attestations, interface-entered declarations, release DOI + license, non-OA route selection remain author tasks |

## Overall decision

**READY AFTER AUTHOR ITEMS.**

- Strongest remaining desk-rejection risk: an editor judges the incremental (B)-class contribution and lack of empirical validation as insufficient for "Original research paper" — irreducible without new empirical work; the manuscript discloses it and offers staged validation protocols. This risk transfers, reduced, to any comparable journal.
- Exact next action: author completes `CTEP_AUTHOR_ACTIONS.md` items (email decision, submission date, declarations, release DOI, license, non-OA selection) then submits via the Springer portal. Do not submit without the author's action.
- Missing evidence: none material. Items marked NEWLY VERIFIED were performed 2026-10-21 with commands/logs; no backdated audits.
