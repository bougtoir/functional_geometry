# Post-audit targeted revision plan

## Snapshot

- Canonical repository: `bougtoir/wip`
- Base revision: `c6ce46d8` (`origin/master`)
- Revision branch: `devin/1790254872-functional-geometry-revision`
- Canonical project directory: `functional_geometry/`
- Canonical manuscript source: `manuscript/manuscript_template.md`
- Canonical analysis entry point: `scripts/run_analysis.py`
- Canonical submission builder: `scripts/build_submission.py`
- Canonical quality-control entry point: `scripts/run_qc.py`
- Existing submission archive: `functional_geometry_JCLP_submission.zip`
- Existing generated manuscript: `submission/Manuscript.docx` and
  `submission/Manuscript.pdf`
- Existing supplementary file: `submission/Supplementary_material.docx`
- Existing analytical configuration: `config/scenarios.json`
- Existing value traceability registry: `results/manuscript_values.csv`

The working tree was clean when the revision branch was created. The revision
starts from the current `master` after the original functional-geometry pull
request was merged. Existing validated analyses will be retained unless a
corrected definition, parameter, or source changes their output.

## Issue-to-output map

| Phase / audit issue | Root sources and code to inspect or repair | Downstream outputs | Reanalysis requirement | Verification |
|---|---|---|---|---|
| Patent metadata repair | Persisted Google/WIPO patent records; `data/processed/patent_source_registry.csv`; `config/references.json`; patent reports | Reference registry, prior-art report, manuscript, supplement, captions, cover letter | Metadata-only unless Table 2 values differ | Cross-source identity agreement; no inventor/applicant/assignee conflation |
| Full reference reverification | `config/references.json`; existing verification files; primary publisher, DOI, agency, standards, and patent records | `reports/references_verified.csv`; manuscript references | No numerical reanalysis | Requested schema; identity-level statuses; no `UNVERIFIED` citation |
| Claim-to-source audit | Manuscript citations and source passages | `reports/CLAIM_SOURCE_AUDIT.csv`; repaired claims/citations | No numerical reanalysis unless a quantitative source is removed | No `DOES_NOT_SUPPORT` or `UNVERIFIED` row remains |
| Straw replacement mathematics | `scripts/fgo_model.py`; `config/scenarios.json`; `scripts/run_analysis.py` | Table 4, sensitivity output, Figure 4, Monte Carlo labels, value registry, manuscript, supplement | Existing simulation is mathematically an additional-use rate because it applies `(1+r)`; values remain valid after terminology repair. Add a separate true-probability sensitivity model. | Symbolic equations; numerical tests at 10%, 20%, and 30%; shifted-burden checks |
| 114→95 mm scenario status | `config/scenarios.json`; source registries; manuscript | Scenario labels, table/figure captions, cover letter, graphical abstract | No output-value change expected | Explicitly “illustrative reference scenario,” never estimated optimum or recommendation |
| Abstract / Monte Carlo emphasis | Manuscript source and value registry | Abstract and generated manuscript | Retain Monte Carlo; no distribution deletion | Abstract emphasizes exact boundaries and contains no scenario-positive proportions |
| JCLP desk-rejection defense | Introduction, Discussion, Conclusion, cover letter | Manuscript and cover letter | No numerical reanalysis | Claims limited to a service-normalized falsification framework; no effectiveness or full-LCA claim |
| Research-question logic | Four Introduction questions and section structure | Methods–Results–Discussion–Conclusion mapping | No numerical reanalysis | Each question has an explicit method, result, discussion, and conclusion disposition |
| US6458450B1 special audit | Persisted primary patent HTML; observed Table 2 CSV; extraction/contrast code | Raw-value table, nine contrasts, manuscript values, tests, reports | Recalculate contrasts programmatically | Exact nine rows; range; four positive/five non-positive; participant and task context |
| Numerical consistency | Config, generated tables, value registry | All manuscript and submission artifacts | Regenerate values from code | Cross-document checks for all specified boundaries, packing counts, seed, draws, and intervals |
| Figure/table audit | Figure and table builders; captions and placeholders | Five figures, six tables, manuscript, supplement, graphical abstract | Regenerate affected displays from code | Sequential citations; observed/scenario labels; corrected straw terminology |
| Current JCLP guidance | Official live JCLP guide and Elsevier policies | `reports/JCLP_requirements.md`; QC rules; upload guidance | No analysis | Current date, primary URLs, exact limits/status |
| Manual author items | Title page, declarations, cover letter, availability text | `reports/MANUAL_SUBMISSION_ITEMS.md` | None | No invented affiliation, address, email, ORCID, funding identifier, DOI, or attestation |
| Data/code availability | README, repository contents, manifest, acquisition ledgers | Manuscript statement, handoff report | Final clean build | Every availability claim literally matches versioned or documented local content |
| AI disclosure | Actual use in this project and current Elsevier policy | Manuscript disclosure and QC | None | Devin disclosed accurately; no unused system listed; correct location before references |
| Clean reproducibility | Makefile and complete pipeline | All generated artifacts and updated reproducibility audit | Final `make all` required | Clean command success; tests; package integrity; no manual post-build edits |
| Hard-coding audit | Config, builders, figures, tables, manuscript placeholders | Centralized named parameters and traceable results | Regenerate affected outputs | No result literals bypass the value registry; scenario constants documented |
| Final integrity and adversarial review | Entire corrected package | Final review, response, QC, and handoff reports | Fix and rebuild any material finding | Editor + two reviewers; all defensible critical/major/minor fixes implemented |
| Revised submission package | Corrected canonical outputs | `functional_geometry_JCLP_submission_REVISED.zip` | Generated only after final build | Clear upload set, readable archive, no internal audit files in journal-upload set |

## Sequential execution and stopping rules

1. Repair and verify patent provenance first, because reference and claim audits
   depend on correct identities.
2. Reverify all cited sources and repair unsupported claims before manuscript
   language is finalized.
3. Correct the straw terminology and add the distinct probability formulation
   before regenerating any affected analytical display or prose.
4. Revise the manuscript, supplement, cover letter, highlights, graphical
   abstract, and traceability registry through source code only.
5. Run the complete build and tests.
6. Conduct the hostile editor/reviewer audit before the final mechanical gate.
7. Repair all scientifically defensible findings, rebuild, and then create the
   revised archive and final handoff.

No controlled behavioral-effect estimate will be invented. Patent observations
will remain weak, non-population evidence. Scenario Monte Carlo outputs will
remain explicitly non-empirical. Negative and conditional results will be
preserved.
