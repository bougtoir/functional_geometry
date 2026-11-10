# 05 Novelty feasibility gate (PHASE 2.4)

## Decision: **NO-GO**

Rule applied (fixed in the brief before scoring): NO-GO if A, D or E lacks a clear contribution; total score is not used.

| Criterion | Score (0–5) | Basis |
|---|---|---|
| A Problem-setting originality | 1 | Choosing selectable unit sizes for stochastic requirements is the assortment / vial-size / denomination problem (02, 03); selectable perforations and tablet score lines are prior art. Only the product domain (tissue) is new. |
| B Mathematical originality | 0 | Every variant reduces exactly to an existing class (04). |
| C Algorithmic originality | 0 | Enumeration / existing DP-IP suffices. |
| D Added design-decision value | 1 | Under rational choice the answer is "finest nested granularity manufacturable" (P1, P2) — trivial. Under any other choice model the decision is determined by unmeasured parameters, and the k-unit result is the same linear break-even identity as the existing CTEP centre-perforation model. Nothing a designer could act on beyond the existing break-even screen. |
| E Empirical / scientific testability | 1 | Predictions are testable in principle (nested refinement; unit-bias count behaviour), but P1 is tautological and unit bias is already established in food. Testing in tissue needs task-requirement and selection data that do not exist publicly and cannot be generated here (human-subject trial). |

A, D and E all fail → NO-GO. Per the brief, PHASE 3 onward (formal model, implementation, manuscript, journal selection, submission package) is **not** executed.

## Hostile check of this verdict

* *"The combination (task + choice + manufacturing) is new even if each part is not."* — Combining a known objective with known constraints is an application, and the combination's only new output (an interior optimum) would come from assumed penalties. The JCLP desk rejection already rejected this level of contribution.
* *"Tissue is an unstudied domain."* — True for behaviour; that makes it an empirical gap, which a model paper cannot close.
* *"Search incomplete (Semantic Scholar 429; no Scopus/WoS)."* — Accepted as a limitation. It cannot overturn the verdict: the reductions in 04 are proofs, independent of whether further applied papers exist.

## Condition for re-opening (would be a different study)

Re-run this gate only if measured data become available, e.g. a pre-registered user study (ethics approval required) recording task type, requirement (area/width/length), units taken and retakes under ≥3 perforation granularities, plus converting-line data on perforation strength vs cell size. With such data the contribution would be empirical (testing unit-bias and least-effort predictions for divisible consumables), and A/D/E would need re-scoring.
