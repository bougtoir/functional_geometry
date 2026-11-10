# 09 — Experimental Identification Audit

## 1. The confound in the original three arms

Original E3 arms:
- **A:** "replace the material of product X"
- **B:** "redesign X keeping its form"
- **C:** "deliver function F with any form"

A and B **forbid** architectures that C permits. Differences can therefore arise from:
1. **framing**: how the problem is represented, which is a cognitive effect (fixation); and
2. **feasible-set restriction**: which solutions are allowed. This is a *design limitation* in the sense of Wasserbaur & Sakao (2020, FT), who separate fixations (controllable by the designer) from limitations (imposed constraints).

If C beats A, that may only show that a larger permitted set contains better solutions. This is the tautology already rejected in the prior gate (D4).

**Under the original design, the estimand is the effect of a design-brief package (framing + constraint), not a framing effect.**

## 2. Options

| Design | Estimand | Pros | Cons |
|---|---|---|---|
| O1 Original 3-arm (constraints differ) | Brief-package effect | Mirrors real briefs; strong manipulation | Confounded; partly tautological; weakest novelty |
| **O2 Emphasis 3-arm (identical permitted set)** | **Framing effect** | Identifies the cognitive effect; smallest design that answers the stated question | Weaker manipulation; manipulation checks needed; null risk higher |
| O3 2×2/3×2 factorial (framing × explicit constraint) | Framing, constraint and interaction | Separates both | ≥ 2× sample; more complex; constraint arm partly tautological |

## 3. Recommendation: **O2 is the minimum design that identifies the intended effect**

In every arm the brief has the following parts:
- **Shared block** (identical text): functional requirement and FU, the FE criteria (F1–F8 in plain language), the environmental objective ("minimise life-cycle environmental impact per FU"), time, materials, and the sentence **"Any material, form, product or system solution is permitted."**
- **Framing paragraph** (the only difference, length-matched ± 10 words):
  - A: the reference product's material is the main environmental problem.
  - B: the reference product's design (geometry, mass, construction) is the main opportunity.
  - C: the need F can be met in many ways; the reference product is one of them.
- **Reference product** shown to all arms identically. Showing it only in A/B would add an example-exposure confound (Jansson & Smith 1991).

**Manipulation checks:**
- A post-task item: "what did the brief ask you to focus on?"
- Independent coding of each final concept's architecture class: same form / same form + new material / new form / system or service.

O3 is justified only if the team also wants the constraint effect. That effect is largely predictable, so O3 is not recommended as the first study.

## 4. Equivalence across arms

Time budget, information pack, worksheet (06 template), resources (paper/CAD), environmental objective and evaluation criteria are all identical and stated in the shared block. The facilitator script is fixed, and sessions are randomised within each session slot.

## 5. Outcomes

| Outcome | Role | Feasibility |
|---|---|---|
| Failure-adjusted impact per FU of the final selected concept (05 §6) | **Primary** | Conditional on 07 reliability |
| FE pass rate | Key secondary (reported alongside, never dropped) | Conditional on κ/AC1 |
| Impact per FU among FE-PASS concepts | Secondary; descriptive (conditioning on a post-randomisation variable) | — |
| Design feasibility (F7) | Secondary | — |
| Similarity to the reference product (architecture class, feature overlap) | Secondary / manipulation check | Coding scheme to be written |
| Diversity of generated concepts | Secondary | Standard variety metrics; no environmental interpretation |
| Search effort (number of concepts, time to selection) | Secondary | Logged |
| Number of FE-feasible alternatives generated | Secondary | Assessed on a sample, owing to cost |
| Assessment uncertainty (interval width) per arm | Secondary | From Monte Carlo |

**Idea count, novelty and diversity are never interpreted as environmental superiority.**

## 6. Provisional analysis framework (no effect sizes, no sample size)

- **Randomisation:** individual participants, stratified by expertise (student / professional) and by task if there are several tasks. Block randomisation; allocation is concealed until the session starts.
- **Model:** linear mixed model on log failure-adjusted impact, with
  - fixed effects: arm, expertise, arm × expertise (pre-specified);
  - random effects: task (or a fixed effect if there are fewer than 5 tasks), session/facilitator.
  - If participants do more than one task (crossover), add a participant random intercept and carry-over checks.
- **FE pass:** mixed logistic model with the same structure.
- **Missing or underspecified concepts:** no exclusion. A participant who submits no final concept is an FE FAIL. Underspecification is handled with archetype defaults and the low-information flag, plus a sensitivity analysis that excludes low-information concepts.
- **Multiple testing:** the primary contrasts are C vs A and C vs B, two-sided, with Holm correction. A vs B is secondary. Secondary outcomes are reported with FDR control and labelled exploratory.
- **Uncertainty propagation:** a sensitivity analysis refits the model across Monte Carlo draws of each concept's impact (multiple-imputation style). It reports whether the arm effect survives assessment uncertainty.
- **Pre-specified sensitivity analyses:**
  - INDETERMINATE treated as PASS;
  - adjudicated vs mean-of-assessors values;
  - alternative washing and end-of-life scenarios;
  - a non-failure-adjusted endpoint;
  - rank-based endpoint.
- **Null results:** use equivalence bounds (TOST). The smallest effect of interest must be justified from the variation of the reference product, not invented. Until then, a null is reported as "not distinguishable at this precision", not as "no effect".
- **Sample size:** **not calculated.** It requires the endpoint's between-concept variance and the assessment error, which only the pilot can provide.
- **Preregistration:** only *after* the reliability pilot passes. Registering an unvalidated endpoint as if it were validated is prohibited.
