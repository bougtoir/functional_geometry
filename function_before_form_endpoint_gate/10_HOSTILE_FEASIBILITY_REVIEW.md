# 10 — Hostile Feasibility Review

Severity: **CRITICAL** (blocks GO), **MAJOR** (must be resolved before preregistration), **MINOR**.

## Reviewer A — Design research

| # | Strongest objection | Severity | Evidence | Resolvable? |
|---|---|---|---|---|
| A1 | "This is a fixation/priming experiment with a new label. Liao & MacDonald 2021 already randomised pre-ideation framing and measured environmental relevance; Collado-Ruiz 2010 manipulated environmental information; Ruiz-Pastor 2020 manipulated circular requirements." | **MAJOR** | 03 rows U01, U03, U05 | Partly. Novelty lies only in the endpoint (impact per FU, FE gate, selected concept) and in the framing level. The manuscript must present this as an extension. |
| A2 | "Collado-Ruiz 2010 is unread; it may already contain an environmental outcome." | ~~CRITICAL~~ **RESOLVED** | 01 §1: full text read; no environmental outcome; named as future work (p. 494) | Resolved. Residual: the 2012 CIIP paper announced a ≈120-designer experiment assessing "sustainability potential"; no published results were found (OpenAlex, Crossref). Folded into A3. |
| A3 | "Scopus/WoS were not searched; design-conference papers (ICED, DESIGN, DETC) are under-indexed in OpenAlex." | **CRITICAL** (for closure) | 02 §1 | Yes, with institutional access and the logged query strings. |
| A4 | "The emphasis design (O2) may produce too weak a manipulation; designers ignore framing paragraphs." | MAJOR | Hu 2021 found effects of problem-statement changes on solution counts, so manipulations of this kind can work | Yes: manipulation checks plus a small pilot of manipulation strength (non-outcome). |
| A5 | "Ross et al. (JMD 2022) may already compare abstract vs specific DfE guidance with an environmental metric." | ~~MAJOR~~ **RESOLVED** | FT: outcomes are decision counts and judge ratings; no LCA; no agreement statistic | Resolved. |

## Reviewer B — LCA methodology

| # | Strongest objection | Severity | Evidence | Resolvable? |
|---|---|---|---|---|
| B1 | "Assumed uses-per-unit and loss rates will decide every reusable-vs-single-use comparison; the endpoint measures the assessor's defaults, not the design." | **CRITICAL** | Known behaviour of reuse LCAs; 05 §7 | Partly. Frozen archetypes, sensitivity, and discernibility rules make this visible. If arm effects vanish under sensitivity, report that honestly. |
| B2 | "Product-only inventories vs service-system inventories are not comparable." | MAJOR | 05 §2 | Yes: infrastructure share is in the FU equation, and F8 system completeness. |
| B3 | "GWP alone is not 'environmental performance'." | MAJOR | — | Yes: a fixed secondary indicator set, and claims limited to the measured indicators. |
| B4 | "Failure-adjusted endpoint (I + I_ref) is arbitrary." | MAJOR | 05 §6 | Partly. It is defensible as "the function is still needed" and is stated as an assumption, with the unadjusted analysis as sensitivity. |
| B5 | "Calling it LCA invites an ISO-compliance objection." | MINOR | — | Yes: call it a "screening LCA endpoint (ISO 14040/44 framework, non-comparative-assertion)". |

## Reviewer C — Experimental design

| # | Strongest objection | Severity | Evidence | Resolvable? |
|---|---|---|---|---|
| C1 | "In the original design, arms differ in permitted solutions; the effect is constraint, not framing." | **CRITICAL** under O1 | Wasserbaur & Sakao 2020; prior gate D4 | **Yes**: O2 (identical permitted set) resolves it; O1 must be abandoned or relabelled as a brief-package estimand. |
| C2 | "Arm C invites system concepts that are less specified, so assessment uncertainty and defaults differ by arm; blinding cannot hide architecture." | MAJOR | 06 §5 | Partly. Low-information flags and per-arm uncertainty are reported. Blinding to *arm* holds even if architecture is visible. |
| C3 | "Conditioning impact on FE pass creates post-randomisation selection bias." | MAJOR | 09 §5 | Yes: the primary endpoint is failure-adjusted over all participants; the conditional estimate is descriptive only. |
| C4 | "Students ≠ professionals; external validity." | MAJOR | Faludi 2020 (professionals), Liao 2021 (mixed) | Partly: expertise stratification. Professional recruitment is a feasibility risk. |
| C5 | "No sample size." | MINOR at this stage | 09 §6 | Yes: after the pilot. |

## Reviewer D — Journal editor

| # | Strongest objection | Severity | Resolvable? |
|---|---|---|---|
| D1 | "Assuming valid results, is this more than an incremental addition to Liao & MacDonald 2021 and Greeley 2025?" | MAJOR | Probably yes, if the endpoint is validated *and* reported as a reusable method. Either outcome direction is then informative because the endpoint measures impact magnitude and functional failure, which rating-based studies cannot. Without a validated endpoint: **no**. |
| D2 | "A null result on one task with students would be unpublishable at a strong venue." | MAJOR | Partly: ≥ 2 tasks; a precision-based (equivalence) null; the endpoint-validation component publishable separately. |
| D3 | "The endpoint-validation study is the real contribution; the framing experiment is secondary." | MINOR (strategic) | This is a reasonable re-ordering. Validating the endpoint first is also the scientifically required order. |

## Summary

The review did not soften any finding. Three CRITICAL items remain open:
- **A3:** prior-art closure is incomplete (Scopus/WoS; possible unpublished or unindexed results of the experiments announced in CIIP 2012). A2 and A5 are resolved by the full texts.
- **B1:** dominance of assumptions; resolvable only by the pilot.
- **C1:** resolved by design choice O2. It is not open if O2 is adopted.

None of these is shown to be **unresolvable**, so the review does not force NO-GO. It also does not permit GO.
