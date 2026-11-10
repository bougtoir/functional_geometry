# Patent metadata and US6458450B1 Table 2 audit

## Audit result

All four targeted records were reopened from locally preserved patent HTML and
facsimiles. Inventor, applicant, original assignee, current assignee, and family
member are now represented as separate concepts in
`data/processed/patent_metadata_audit.csv`.

| Publication | Finding | Repair |
|---|---|---|
| US453003A | The audit concern was correct. The patent is not a Seth W. Wheeler patent. | Corrected to Oliver Hewlett Hicks, *Toilet or wrapping paper*, filed 30 December 1889 and issued 26 May 1891. The specification states that Hicks assigned it to Morgan Envelope Company. |
| WO2003026472A1 | The audit concern was correct. No Kimberly-Clark applicant was identified. | Corrected to Helmuth Friedrich as both applicant and inventor, *Toilet paper*, PCT/DE2002/003505, published 3 April 2003. |
| US20160345786A1 | The audit concern was correct. The A1 publication was not a Kimberly-Clark publication and its exact title was wrong. | Corrected to Olson, Hoadley, and Daul, *Partitionable paper towel*. The applicant/original assignee was Georgia-Pacific Consumer Products LP; the current assignee field records GPCP IP Holdings LLC. |
| US6458450B1 | The Procter & Gamble provenance was correct, but the exact title and inventor/assignee roles were not. | Corrected to seven named inventors, *Tissue paper*, assigned to The Procter & Gamble Company. |

The evidence used in the manuscript is conceptual prior art for the first three
records and the patent-reported Table 2 observations for US6458450B1. No legal
status, patentability, validity, infringement, or freedom-to-operate conclusion
is made.

## US6458450B1 Table 2

The primary patent states immediately before Table 2 that:

- the results are averages from two focus groups of eight panelists each;
- all panelists were women;
- participants selected the amount they believed necessary for post-urinary
  drying;
- samples were two-ply bath tissues;
- widths were 4.5, 5.75, and 7.0 inches;
- total basis weights were 28, 44, and 70 lb/3000 ft²; and
- sheet length, softness, texture, and visual appearance were reported as
  similar.

The nine transcribed rows match the patent table for basis weight, width, area
per sheet, sheets selected, and reported total usage. The regression test
contains the complete nine-row source vector and checks the processed
transcription.

## Contrast direction and corrected range

Each within-basis-weight contrast is defined in the direction:

\[
R = \frac{\text{reported total usage at narrower width}}
         {\text{reported total usage at wider width}},
\qquad
\Delta = 1-R.
\]

Thus positive \(\Delta\) means lower reported mass for the narrower sample.
The revised calculation uses the patent's reported total-usage column directly.
The earlier implementation instead reconstructed usage from rounded area and
sheet-count columns. That proxy preserved all signs but introduced avoidable
rounding differences.

The corrected nine contrasts span:

- minimum material saving: -20.0%;
- maximum material saving: +18.3824%;
- positive contrasts: 4;
- negative contrasts: 5.

No zero contrast occurs. The mixed signs remain the relevant qualitative
finding.

## Evidentiary limitation

These observations are weak, patent-reported, non-population evidence. The
patent does not provide enough information for causal inference, sampling
inference, variance estimation, randomization assessment, or a population
width-response distribution. The observations are not used to fit the primary
Monte Carlo distributions. They serve only to demonstrate that compensation
can change the sign under limited reported conditions.
