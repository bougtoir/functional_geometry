# FINAL HANDOFF — Clean Technologies and Environmental Policy (CTEP)

## Verdict

**READY AFTER AUTHOR ITEMS** — the CTEP package is complete and QC-verified; only author-identity, attestation, and portal fields remain. Do not submit without the author's action.

## Selected journal and GO rationale

- Journal: **Clean Technologies and Environmental Policy** (Springer, no. 10098), article type **Original research paper**.
- Why CTEP: its Clean Technology thrust explicitly covers mathematical/computer-based methods and models for designing, analyzing, and measuring the cleanliness of products — a structural fit for a service-normalized screening model, unlike JCLP's empirically weighted desk screen. Evidence: `reports/CTEP_JOURNAL_GATE.md`.
- Novelty classification: **(B) original integration + actionable falsification framework** — defensible for CTEP; not a new field, not repackaging. Evidence: `reports/CTEP_CLOSEST_PRIOR_STUDIES.csv`, `reports/CTEP_CITATION_ECOLOGY.md`, `reports/CTEP_ADVERSARIAL_REVIEW.md`.

## Fee pathway (verified 2026-10-18)

- **Subscription publishing: no APC, zero mandatory charges.** Optional OA APC £2,790 / US$4,290 / €3,190 — do not select. No page/color/submission charges listed. Official page: link.springer.com/journal/10098/how-to-publish-with-us. Re-check at acceptance.

## Response to the JCLP novelty objection

JCLP rejected JCLEPRO-D-26-35955 for insufficient novelty/overlap without review. Answer for CTEP: the paper's contribution was reframed explicitly as a *screening instrument* — break-even conditions and falsification regions that no cited prior study provides — with title, abstract, intro, and cover letter stating the incremental claim. JCLP rejection is not volunteered in the cover letter; answer truthfully if the portal asks. Residual risk: a CTEP editor may still judge the contribution incremental — most likely adverse outcome is a major-revision request for empirical validation, which the paper anticipates via its staged validation protocols (§4.9).

## Exact numerical changes

**None.** All derived values come from the frozen pipeline (`make all` → `results/manuscript_values.csv`); the retarget touched only framing text, reference formatting, declarations, cover letter, title/metadata, and build/QC plumbing.

## Git / PR

- Retarget PR: bougtoir/wip#705 (branch `devin/1792323011-ctep-retarget`) — MERGED 2026-10-18 (`c3f50f8a7`).
- Finishing pass: branch `devin/<ts>-ctep-finishing`; changes: cover-letter literals replaced with registry-derived fields; title page + signature carry verified author metadata (affiliation/address/bougtoir@gmail.com/ORCID); `CTEP_NOVELTY_GATE.md`, `CTEP_FINAL_HOSTILE_REVIEW.md`, `CTEP_NUMERIC_HARDCODE_AUDIT.md`, `CTEP_DATA_TEXT_FIGURE_CONSISTENCY.md`, `CTEP_AUTHOR_ACTIONS.md`, `CTEP_FINISHING_BASELINE.md` added; archive renamed `..._FINAL_REVISED.zip`; QC thresholds aligned to 6 remaining AUTHOR ACTION items. QC 53 checks PASS.
- Merge: user merges on GitHub (Devin cannot merge wip PRs). The public mirror `bougtoir/functional_geometry` uses full-subtree sync via pointer branch `devin/1790254872-functional-geometry-revision` (already fast-forwarded); after the finishing PR merges, fast-forward the pointer again and verify the public tree.

## Tests / rendering

- `make all`: PASS (analysis rebuild, manuscript build, 22 tests, lint, 53 QC checks). See `reports/CTEP_FINAL_QC.md`.
- DOCX: 45 OMML equations, inline figures near first mention, Springer-format alphabetized references with DOI links, separate editable tables, editable graphical abstract (mandatory for CTEP at first submission).

## Author-only items (reports/MANUAL_SUBMISSION_ITEMS.md)

Affiliation + postal address + corresponding email; funding / competing-interests / author-contribution statements (interface-entered); persistent release DOI + project license; subscription (non-OA) route selection; portal classifications and reviewer suggestions; graphical abstract upload; final visual review of the system-generated PDF.

## Exact upload set (submission/)

`Manuscript.docx`, `Title_page.docx`, `Cover_letter.docx`, `Graphical_abstract_editable.pptx` or `.png` (required), `separate_figures/figure_*.pdf|png`, `Tables_editable.docx`, `Supplementary_material.docx`, `Highlights.docx` (optional for CTEP). Full archive: `functional_geometry_CTEP_submission_FINAL_REVISED.zip`.

## EDS fallback

Not executed — CTEP passed scope, fee, and novelty gates.
