# 30 — Reliability and Sensitivity Plan (pre-specified; freeze before any assessment)

**ASSESSOR RELIABILITY — NOT TESTED.**

## 1. Reliability statistics and acceptance criteria (to be frozen)

| Target | Statistic | Accept if |
|---|---|---|
| FE status (3 categories) | Gwet AC1 and Cohen's κ, plus % agreement | AC1 ≥ 0.70 **and** κ ≥ 0.60 |
| Impact magnitude | ICC(2,1), absolute agreement, on log impact; Bland–Altman ratio limits | Lower 95% CI bound of ICC ≥ 0.75 |
| Ranking within task | Kendall τ-b between assessors | Lower 95% CI bound ≥ 0.60 (rank-only fallback if the ICC fails) |
| Pairwise dominance | % of pairs with agreed, discernible direction | Reported; the threshold is fixed with the team pre-pilot |
| Benchmark accuracy | τ-b and median \|log ratio\| against the published LCA for the reference cases | τ-b lower bound ≥ 0.60; the median-ratio bound is fixed pre-pilot |

Thresholds are **not revised after outcomes are observed.** The endpoint fails for a task if both the magnitude and rank criteria fail, or if the FE criterion fails, or if the benchmark criterion fails.

## 2. Assumption-dominance specification

Parameters and the circumstances in which they decide rankings:
- **Uses per unit / reuse count:** decisive for reusable vs single-use (break-even dependence; Cottafava 2020; Lee 2025: "reuse rate ... significantly influenced the results").
- **Cleaning (energy, water, detergent; hand vs machine):** can reverse reusable advantages (Potting & van der Harst 2015 compare hand- and dish-washing).
- **Product lifetime and replacement or loss rate:** decisive for reusables with return schemes.
- **Material mass:** decisive within single-use concepts.
- **Manufacturing process:** decisive among material classes.
- **System boundary:** decisive for service and system concepts (infrastructure inclusion).

**Procedure.**
1. Freeze ranges from the benchmark papers (26), with a citation per range.
2. Run Monte Carlo over the joint ranges (seed fixed, ≥ 1,000 draws).
3. Compute the rank-stability share: the fraction of concept pairs with P(order) > 0.9.
4. Run a variance-based sensitivity analysis to identify the dominant parameters.
5. Run a second scenario in which u, r and cleaning are **fixed in the common brief** for all arms.

**Interpretation rule.**
- If the rank-stability share falls below the frozen threshold (e.g. < 50% of pairs) under free parameters, *but* is acceptable with brief-fixed parameters, adopt brief-fixed parameters. This narrows external validity, which must be stated.
- If the share is unacceptable under both, **the endpoint does not support causal interpretation: NO-GO for that task.**
