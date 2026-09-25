# Final quality-control report

Overall automated result: **PASS**.

## JCLP and package checks

| Check | Result | Observed |
|---|---:|---:|
| Abstract is no longer than 250 words | PASS | 215 |
| Main text is within the 6,000–8,000-word target | PASS | 7000 |
| Keyword count is 1–7 | PASS | 6 |
| There are 3–5 highlights | PASS | 5 |
| Each highlight is no longer than 85 characters | PASS | 66 |
| Reference count is no more than 50 | PASS | 31 |
| Reference metadata has structured author and year fields | PASS | 31 |
| Reference entries use author–year formatting | PASS | 31 |
| In-text citations use author–year style | PASS | 31 |
| Every configured reference is cited and listed | PASS | 31/31 |
| Reference list is alphabetically ordered | PASS | 31 |
| Reference audit uses the required schema | PASS | 16 |
| All reference statuses are allowed and none remain unverified | PASS | 31 |
| Reference audit covers every cited reference exactly once | PASS | 31/31 |
| Claim-source audit uses the required schema | PASS | 8 |
| Claim-source audit covers every expected claim exactly once | PASS | 25/25 |
| Claim-source audit has no unsupported or unverified claims | PASS | 25 |
| Figure placeholders are sequential | PASS | [1, 2, 3, 4, 5] |
| Table placeholders are sequential | PASS | [1, 2, 3, 4, 5, 6] |
| Every figure is cited before display in first-appearance order | PASS | [12703, 15511, 28106, 30535, 33247] |
| Every table is cited before display in first-appearance order | PASS | [10397, 15424, 28659, 29952, 31723, 32568] |
| Figure and table captions preserve evidence-status labels | PASS | Figures 3–5; Tables 3 and 5 |
| Supplementary material is cited in the manuscript | PASS | Methods 2.8 |
| No unresolved placeholders remain in the PDF | PASS | 0 |
| Human-only fields use conspicuous AUTHOR ACTION labels | PASS | 10 |
| Manual-submission checklist covers every remaining author action | PASS | 14 |
| Rendered manuscript contains no LaTeX control sequences | PASS | 0 |
| Every template equation is editable Word math | PASS | 45/45 |
| Manuscript-value registry has required fields | PASS | 50 |
| Every manuscript-value source file exists | PASS | 50 |
| Required post-audit values are registry-driven | PASS | 29 |
| Frozen headline values match the canonical registry | PASS | 26 |
| All required headline values appear in the rendered manuscript | PASS | 19 |
| No stale patent-range or 116-mm prose remains | PASS | none |
| Abstract excludes scenario-positive proportions | PASS | excluded |
| The configured width candidate is classified as illustrative | PASS | ILLUSTRATIVE_REFERENCE_SCENARIO |
| Patent contrasts match the current observed patent table | PASS | 9 |
| Frozen patent identities and provenance remain correct | PASS | 4 |
| Straw table separates expected-rate and failure-probability boundaries | PASS | 6 |
| Primary straw Monte Carlo identifies the expected-rate formulation | PASS | EXPECTED_ADDITIONAL_REPLACEMENT_RATE |
| Rendered straw terminology separates rate from failure probability | PASS | separate formulations |
| Graphical abstract separates straw rate and probability terms | PASS | separate formulations |
| Persistent acquisition ledger records public snapshots | PASS | 94 |
| Failed or empty retrievals are disclosed | PASS | 9 |
| Acquisition dates are derived at runtime | PASS | runtime UTC |
| Raw snapshots use collision-safe exclusive creation | PASS | exclusive write |
| Submission archive is readable | PASS | 4230209 |
| Submission archive contains all expected deliverables | PASS | 28 |
| Archive contains raster, publication, and editable vector figures | PASS | 15 |
| Graphical abstract uses editable native PowerPoint shapes | PASS | 5 |
| Rendered manuscript has pages | PASS | 27 |
| Tests pass | PASS | ......................                                                   [100%]
22 passed in 0.45s |
| Python compilation passes | PASS | clean |

## Required author completion

- Add affiliation, postal address, and corresponding-author email.
- Confirm originality, exclusive submission, and approval by all authors.
- Confirm author order and final CRediT roles.
- Confirm funding and complete the Elsevier competing-interest declaration.
- Create a versioned repository release with a persistent identifier.
- Add an author-selected project license.

These fields are not inferred or fabricated by the build.
