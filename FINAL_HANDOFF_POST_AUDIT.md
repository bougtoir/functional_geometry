# Final post-audit handoff

## Revision identity and reproducibility

- Clean-build source commit: `1f2498dccc83943de3c890333f34d8ee955fa6a0`.
- The targeted revision was merged through
  https://github.com/bougtoir/wip/pull/518; post-merge review fixes are
  recorded in a separate follow-up pull request.
- Public project repository: https://github.com/bougtoir/functional_geometry.
- The handoff report and regenerated build artifacts are added in a final
  metadata/artifact commit after the clean-build source commit; the exact final
  branch tip is recorded in the follow-up pull request.
- `make all` started from a clean working tree at the source commit and passed.
- Automated verification: 21 tests passed, Python compilation passed, and all
  41 QC checks passed.
- Fixed Monte Carlo seed: `20260924`; draws: `200000`.

## Corrections completed

1. Reverified all 31 cited references with the required audit schema. No
   `UNVERIFIED` record remains.
2. Audited 25 manuscript claims against their cited sources. No
   `DOES_NOT_SUPPORT` or `UNVERIFIED` claim remains.
3. Corrected four patent identities and separated inventor, applicant,
   original-assignee, and current-assignee roles.
4. Re-transcribed US6458450B1 Table 2 and recalculated all nine within-basis-
   weight contrasts from the patent's reported total-usage values.
5. Replaced ambiguous straw “replacement probability” terminology with two
   mathematically distinct formulations:
   - expected additional replacement rate:
     \(R=(1-s)(1+r)+c\);
   - independent per-attempt failure probability:
     \(R=(1-s)/(1-p)+c\).
6. Classified 114→95 mm as an **illustrative reference scenario**, not an
   observed product, optimum, or commercial recommendation.
7. Removed Monte Carlo positive-draw proportions from the abstract and made
   analytical break-even boundaries the primary result.
8. Mapped all four research questions through Methods, Results, Discussion, and
   Conclusions, with unresolved empirical questions explicitly identified.
9. Replaced unsupported author declarations with author-confirmation fields.
10. Regenerated the manuscript, supplement, figures, tables, graphical
    abstract, editable files, audit reports, and revised submission archive
    from code.
11. Bound primary straw break-even values to the configured primary reduction
    while preserving separate fixed 10%, 20%, and 30% reporting rows.
12. Made the analysis rebuild patent contrasts from the observed patent table
    before any downstream figure, registry, or manuscript value is calculated.
13. Added exact, unique coverage checks for all cited references and all 25
    expected claim-audit records.
14. Made the illustrative-width QC phrase derive from configured dimensions.
15. Separated fixed 10%/20%/30% straw comparisons from the configured primary
    case and derived the logistics shortening percentage from packed lengths.

## Patent-audit impact

Patent auditing changed both citations and descriptive claims. US453003A is now
attributed to Oliver Hewlett Hicks; WO2003026472A1 to Helmuth Friedrich;
US20160345786A1 to Olson, Hoadley, and Daul with Georgia-Pacific provenance; and
US6458450B1 to Steinhardt et al. with Procter & Gamble as assignee. The revised
US6458450B1 calculations changed the numerical contrast range because reported
total usage replaced an area-times-sheet-count reconstruction. The evidentiary
interpretation remains weak, patent-reported, non-population evidence.

## Numerical changes and retained results

- US6458450B1 contrast range: `-20.0%` to `+18.3824%`.
- Patent contrast signs: four positive and five negative.
- Illustrative width ceiling, 114→95 mm: `16.6667%`.
- Width break-even longitudinal consumption: `1.20×` baseline.
- A 20% straw shortening breaks even at:
  - `25%` expected additional replacement rate when `c=0`;
  - `20%` independent per-attempt failure probability when `c=0`.
- The straw Monte Carlo was rerun because affected artifacts were rebuilt, but
  it intentionally retained the expected-rate formulation, seed, distributions,
  and draw count. Its numerical summary therefore remained unchanged.
- Primary Monte Carlo medians remained:
  - width: `0.0635944`;
  - center perforation: `0.1497426`;
  - straw: `0.0683046`.

## Verification status

- References without `UNVERIFIED`: `31/31`.
- Claims without unsupported/unverified status: `25/25`.
- Manuscript value registry: 50 traceable values.
- Editable Word equations: `45/45`.
- Abstract: 215 words.
- Main text plus abstract: 6,954 words.
- References: 31.
- Manuscript PDF: 27 pages.
- Revised archive: 28 files and readable.
- Figure assets: five PNG, five PDF, and five editable SVG files.

## Remaining human-only submission items

- Confirm author order, affiliations, postal addresses, corresponding-author
  email, ORCID, and telephone if requested.
- Confirm originality, exclusive submission, and approval by all authors.
- Confirm the final CRediT role list.
- Confirm funding and competing interests in the Elsevier declarations tool.
- Confirm the ethics and generative-AI statements.
- Select a project-level reuse license.
- Create a versioned public release for the submitted commit and insert its DOI
  or other persistent identifier.
- Select classifications, reviewers, exclusions, and other Editorial Manager
  fields.
- Inspect the system-generated submission PDF before approval.

## Exact proposed JCLP upload files

1. `submission/Manuscript.docx`
2. `submission/Title_page.docx`
3. `submission/Cover_letter.docx`
4. `submission/Highlights.docx`
5. `submission/Supplementary_material.docx`
6. `submission/Tables_editable.docx`
7. `submission/Graphical_abstract.png`
8. `submission/Graphical_abstract_editable.pptx`
9. `figures/figure_1_fgo_framework.png`
10. `figures/figure_2_width_compensation_surface.png`
11. `figures/figure_3_observed_contrasts_and_perforation.png`
12. `figures/figure_4_straw_and_logistics_boundaries.png`
13. `figures/figure_5_scenario_uncertainty.png`

Use `submission/Manuscript.pdf` for local visual inspection, not as a
replacement for the editable main manuscript unless the submission system
requests it. The complete review package is
`functional_geometry_JCLP_submission_REVISED.zip`; it is not a single journal
upload item.
