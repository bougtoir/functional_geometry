# 04 Mathematical equivalence audit (PHASE 2.3)

## FUGD stated minimally

Task t ~ P with requirement vector q_t (area, or width w_t and length l_t). Design d specifies a unit set U(d) (e.g. a sheet of width W, length L split into k_w × k_l cells), user policy π(t, d) chooses a multiset of units with supply s(t, d). Objective: min_d E_t[ material(s) / success(t, s) ] + manufacturing terms, subject to manufacturability.

## Reductions (all exact under the stated conditions)

| Variant | Reduces to | Variable transformation |
|---|---|---|
| Rational user, one unit size a, combinations allowed, area requirement | Single-denomination covering / vial-size overage | supply = a·⌈R/a⌉ (P5: identical to min-cover over denomination set {a}) |
| Rational user, several unit sizes, combinations allowed | Denomination (coin-change covering) design; vial-size set design (Hatswell & Porter 2018) | units ↔ denominations/vials, R ↔ amount/dose |
| Rational user, choose one unit (no combination), smallest that covers | 1-D assortment problem with scrap substitution cost (Pentico 1974/1976); p-median (Tryfos 1986) | sizes ↔ stocked sizes; overage ↔ scrap cost |
| Width + length requirement, aligned perforation grid a × b, contiguous rectangle | Product of two 1-D roundings (P4); with cell-set choice = discrete 2-D assortment (Pentico 1988) | (w_t, l_t) ↔ two-quality demand |
| Stochastic / tolerant choice among offered sizes | Choice-based assortment (Talluri & van Ryzin 2004; Akchen & Caro 2025) | choice probabilities over units |
| Designer anticipating user best response | Bilevel program with lower level = above covering problem (Colson et al. 2007) | — |
| Uncertain task distribution / choice model | Two-stage stochastic or robust product-line design (Bertsimas & Mišić 2017) | — |
| Two-outcome (full/half) selection with probability p | **Existing CTEP model** `center_perforation_material_ratio` | k-unit generalisation is the mixture Σ_j p_j·(j/k)·m_j; its break-even is the same linear identity |
| Count/habit-based selection (take n units regardless of size) | Unit-bias consumption model (Geier et al. 2006) | material = n·a, i.e. the CTEP width model with ε = −1 |
| Habit + under-supply triggers retake | Existing straw failure model `straw_material_ratio_failure_probability` | retained fraction ÷ success probability |

Conclusion: every FUGD variant we could formulate is, after renaming, an existing problem class. Manufacturing constraints (minimum cell size, perforation strength, discrete blade spacing) restrict the feasible set but do not change the class.

## Non-triviality check (the user's explicit condition)

Verified exhaustively by `scripts/check_equivalence_propositions.py` → `results/equivalence_checks.json` (tests: `tests/test_equivalence_propositions.py`, 4 passed).

* **P1 (nested refinement).** If a′ divides a, then a′⌈R/a′⌉ ≤ a⌈R/a⌉ for every R (a⌈R/a⌉ is a multiple of a′ that is ≥ R). Exhaustive check: 5 280 comparisons, 0 violations. Hence under rational selection "more (nested) partitions never increase material" — exactly the trivial result the user asked us to rule out; it holds.
* **P2.** 0 ≤ overage < a, so E[supply] ≤ E[R] + a; the benefit of refinement is bounded by one unit and vanishes as a → 0. 0 violations.
* **P3 (non-nested refinement).** Finer but non-dividing units can increase supply (e.g. a = 3 → 2 at R = 3: 3 → 4). 16 coarse/fine pairs with counterexamples. This is the well-known non-monotonicity of denomination/assortment systems, not a new phenomenon.
* **Interior optima.** Under rational choice the optimum is the finest manufacturable nested granularity (corner solution). An interior optimum appears only when an additional cost rises with granularity: handling effort (the least-effort criterion of van Hove 2001), perforation strength/manufacturing penalty (CTEP penalty term), or misselection/retake (CTEP straw failure term). None of these functions is measured for tissue; any interior optimum would therefore be produced by an assumed convex penalty — the artefact the brief prohibits.

## Ratings

* B (mathematical originality) = 0: no variant escapes reduction.
* C (algorithmic originality) = 0: small instances are solved by enumeration; large ones by existing DP/IP/assortment methods.
