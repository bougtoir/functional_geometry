# Final revision response

## Patent metadata and observed-use calculations

- Corrected the identities, titles, inventors, applicants, and assignees for the four audited patents.
- Re-transcribed US6458450B1 Table 2 and calculated contrasts from reported total usage.
- Updated the patent range to −20.0% to +18.4%, with four positive and five negative contrasts.
- Retained the evidence as weak patent-reported, non-population evidence and did not fit it to the Monte Carlo distributions.

## References and claims

- Reverified all 31 cited references in the required registry schema.
- Repaired bibliographic and official-source mismatches; no `UNVERIFIED` citation remains.
- Completed the claim-source audit with no `DOES_NOT_SUPPORT` or `UNVERIFIED` claim.

## Straw replacement mathematics

- Renamed the primary parameter as expected additional replacement rate.
- Retained \(R_{S,\mathrm{rate}}=(1-s)(1+r)+c\), so the 20% shortening boundary is \(r^*=25\%\) at zero shifted burden.
- Added \(R_{S,\mathrm{prob}}=(1-s)/(1-p)+c\), so the independent per-attempt failure boundary is \(p^*=20\%\).
- Defined \(c\) as shifted container/package burden per successful serving, normalized to baseline straw material mass.
- Added zero- and 5%-shift tests for 10%, 20%, and 30% shortening under both formulations.
- Reran the primary Monte Carlo with unchanged expected-rate draws; its numerical output is unchanged because only terminology was corrected.

## Manuscript and submission package

- Classified 114→95 mm as an illustrative reference scenario, not an optimum or commercial recommendation.
- Removed scenario-positive proportions from the abstract while retaining them in the scenario Results and Table 6.
- Mapped all four research questions through Methods, Results, Discussion, and Conclusions.
- Updated figures, tables, supplement, graphical abstract, AI disclosure, data statement, and manual submission list.
- Regenerated the final submission archive and all downstream artifacts from code.
