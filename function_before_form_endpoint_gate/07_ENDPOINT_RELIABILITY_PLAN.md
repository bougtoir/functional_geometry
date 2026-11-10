# 07 — Endpoint Reliability Plan

**ASSESSOR RELIABILITY — NOT TESTED.** No assessors were recruited in this gate. No agreement statistic has been computed or simulated.

## 1. Measures matched to measurement scale

| Endpoint component | Scale | Agreement measure | Rationale |
|---|---|---|---|
| FE status (PASS/FAIL/IND) | Nominal | Cohen's κ; Gwet's AC1 reported alongside; % agreement | κ can be misleading when one category is very prevalent, so AC1 and raw agreement are reported together |
| Each FE criterion F1–F8 | Nominal | Per-criterion % agreement + κ | Locates the source of disagreement |
| Impact per FU (median) | Ratio, right-skewed | ICC(2,1), absolute agreement, two-way random, on **log** impact; Bland–Altman on log scale (ratio limits of agreement) | The two assessors are a sample of possible assessors; absolute agreement matters. The log scale suits multiplicative error |
| Concept ranking within task | Ordinal | Kendall's τ-b between assessors | The endpoint may be usable as a rank even if magnitudes disagree |
| Pairwise dominance | Binary per pair | % of concept pairs where both assessors agree on direction **and** both call it discernible (P > 0.9 or < 0.1) | Directly tests the decision the study relies on |
| Assumption sensitivity | — | Change in rank agreement under the ± ranges of 05 §8 | Shows whether assumptions dominate |

All of these are reported, whatever the result. No statistic is dropped after the results are seen.

## 2. Pre-specified acceptability rules (to be frozen before the pilot)

Thresholds are fixed **before** any data are seen. Proposed rule, to be confirmed by the team:
- Magnitude usable if the **lower 95% CI bound** of ICC(2,1) on log impact ≥ 0.75. This is the "good" band of the commonly used Koo & Li (2016) guideline; the source was not re-verified in this gate.
- Rank-only use if ICC fails but τ-b lower bound ≥ 0.6. The primary outcome then becomes rank-based. This switch must be declared before the main study, not after.
- FE gate usable if AC1 ≥ 0.7 *and* κ ≥ 0.6.
- **Failure of both magnitude and rank rules → endpoint NO-GO.**

## 3. Pilot size for reliability

- The number of concepts must give an informative ICC confidence interval. A defensible target can only be computed once an anticipated ICC is chosen, and **no ICC is assumed here**.
- Planning range: 30–50 concepts per task, in line with general ICC precision tables. The exact number is fixed in the pilot protocol, with the formula and assumptions stated.

## 4. Feasibility

- Needs 2 (+1 adjudicating) LCA-competent assessors.
- The per-concept time cost is unknown and is a pilot outcome. It is recorded per concept.
