# 29 — Blinded Assessment Package (preparation only)

This package builds on 06 and makes it concrete for TA and TB.

**1. SCD template.** Fields 1–9 as in 06 §1. Minimum required information:
- material class(es);
- mass class (S/M/L, with task-specific gram bands to be fixed);
- process family;
- uses per unit, *or* single-use;
- cleaning route;
- supporting system;
- end of life.

Any field the participant left blank is marked "not specified" by the transcriber, never inferred.

**2. Permitted assumptions.**
- Only the frozen archetype defaults and ranges (30 §2).
- Each default used sets an `assumed` flag on that field.
- A concept with ≥ 3 of {mass, material, uses, cleaning} assumed is labelled **low-information**.

**3. Independent inventory estimation.**
- Each of the two or more assessors maps the SCD to the archetypes alone and runs the same frozen tool version.
- Assessors do not communicate.
- Each records the median, 90% interval and a pedigree data-quality score per input.

**4. Blinding.**
- Assessors are blind to source (pilot: documented product vs reference case; main study: arm), to the other assessor and to the benchmark results.
- SCD IDs are randomised; the key is held by a non-assessing data manager.

**5. Locking and adjudication.**
- FE scores are locked first, then impact scores; each lock is time-stamped and read-only.
- Reliability is computed on the locked independent scores.
- An adjudicator reviews disagreements beyond the pre-set thresholds only after locking. Original scores are archived unchanged.

**6. Data-quality and uncertainty recording.** Per concept: assumed-field count, pedigree scores, Monte Carlo seed, and the P(I_a < I_b) matrix.

**7. Prohibited.** No fabricated or simulated assessor scores, no re-assessment after unblinding, no access to the key before the dataset is locked.
