# 05 — Screening-LCA Protocol for Early-Stage Concepts (draft, unvalidated)

Status: **PROTOCOL ONLY — NOT VALIDATED.** No concept has been assessed, and no inventory value has been entered. The protocol follows the ISO 14040/14044 *framework* (goal & scope, functional unit, system boundary, LCI, LCIA, interpretation). It is **not** an ISO-compliant comparative assertion: there is no critical review panel, no full inventory and no public disclosure. It must never be described as one.

## 1. Goal and scope

- **Goal:** rank and scale the environmental impact *per functional unit* of concepts selected by participants, with enough precision to detect between-arm differences that exceed assessment uncertainty.
- **Intended use:** a research endpoint only. It is not product claims or marketing.

## 2. Candidate tasks and functional units (to be screened, not selected)

The functional unit (FU) is the delivered service, not a product count. Candidates:

| Task | Candidate FU | Fairness checks before selection |
|---|---|---|
| T1 Eating utensil | "Transfer of one 300 g single-serve meal portion from container to mouth, hygienically, at point of consumption, over N = 1,000 meals" | Reusable options require a washing inventory (water, energy, detergent) and loss/return rates. Edible or integrated options require a food-safety screen. Behaviour-based options (e.g. finger food, the container as utensil) must still meet the hygiene and accessibility criteria |
| T2 Beverage serving | "Enabling consumption of one 250 mL beverage serving at point of sale, over N = 1,000 servings" | Reuse/return systems need logistics and washing. Dispenser or system designs need an infrastructure share |
| T3 Goods protection | "Protecting and delivering 1 kg of defined goods over a defined distance with damage rate ≤ x" | Product loss must be inside the FU, because damage transfers burden to the product |

A task is retained only if: (a) at least three structurally different architecture classes can be inventoried at the same depth; (b) published full LCAs exist that cover at least two of those classes, for benchmark validation (§8); (c) the FU can be met by single-use, reusable and system/service architectures without redefining it. Final selection is deferred to the pilot (08).

## 3. Functional-equivalence (FE) gate

Pre-specified criteria are scored **before** and **independently of** the LCA. Each is scored pass / fail / indeterminate:

| Criterion | Operational test (example for T1) |
|---|---|
| F1 Required function | Can transfer the defined food types (liquid, semi-solid, solid) as specified |
| F2 Functional adequacy | Meets a minimum capacity, rigidity and usable-duration description |
| F3 Safety | No sharp edges, choking or chemical-migration hazard identified by the description |
| F4 Hygiene | A cleaning/contamination route is defined for reusable options; single-use options are sealed or clean at the point of use |
| F5 Accessibility | Usable by the defined user population (e.g. one-handed use, limited grip) |
| F6 Durability / use cycles | The number of uses is stated or derivable; the archetype default is used if absent (flagged) |
| F7 Operational feasibility | Can be supplied at the defined point of consumption without unavailable infrastructure |
| F8 System completeness | All supporting systems the concept relies on are named |

- **FE outcome:** PASS (all criteria pass), FAIL (any criterion fails), or INDETERMINATE (≥1 indeterminate, none fail).
- No concept is excluded. FE status is a reported secondary outcome.
- In the primary analysis, INDETERMINATE is analysed as FAIL; in a sensitivity analysis, as PASS.

## 4. Minimum inventory per concept (from the standard template, 06)

| Item | Source of value | Type |
|---|---|---|
| Material type(s) | Participant description | Measured from description |
| Mass per unit | Participant estimate, else archetype mass class (S/M/L) | Assumption, flagged |
| Manufacturing process | Description, else the archetype default for the material | Assumption |
| Process energy | Archetype dataset | Secondary data |
| Transport | Fixed scenario, identical for all concepts | Scenario |
| Uses per unit (u) | Description, else archetype default | Assumption, sensitivity-tested |
| Cleaning per use | Archetype washing scenario (dishwasher / hand / industrial) | Scenario |
| Failure/loss rate (r) | Archetype default | Assumption, sensitivity-tested |
| End of life | Fixed regional scenario per material | Scenario |
| Supporting infrastructure | Allocated share per FU (dispensers, return logistics, washing equipment) | Secondary data / assumption |
| Additional system burdens | E.g. food waste caused by a design, as a qualitative flag; quantified only if an archetype exists | Flag |

## 5. Archetype inventory library (to be built and frozen before the pilot)

- One dataset per material × process × mass class, plus scenarios for washing, transport and end of life.
- Sources: a licensed background database (e.g. ecoinvent, licence to be confirmed) or open secondary datasets. Each entry records the dataset name, version and geography.
- **No value is entered in this gate.** None was verified, and inventing one would fabricate data.
- The library is frozen and hashed before any concept is assessed. Assessors may not add datasets after that point; missing archetypes are logged and handled under §7.

## 6. Impact assessment

- **Primary indicator:** climate change, GWP100 (kg CO₂e per FU). It is chosen for interpretability and data coverage.
- **Secondary:** a small fixed set (e.g. fossil resource use, water use). Single-indicator results must not be generalised to "environmental performance".
- Impact per FU for concept *i*:
  `I_i = N/u_i × (production_i + EoL_i) × (1 + r_i) + N × use-phase_i + infrastructure_i`
- **Failure-adjusted (primary) endpoint:** a concept that FAILS the FE gate does not deliver the FU. Its endpoint is `I_i + I_ref`: the concept's burden plus the reference product, which still has to deliver the function. This prevents a non-functional, low-material concept from scoring better than a working one. It is a modelling assumption and must be stated as one.

## 7. Uncertainty and data quality

- Pedigree-matrix data-quality scores per input, with parameter ranges for mass, u and r (triangular or lognormal; the form is fixed before the pilot).
- Monte Carlo propagation (≥ 1,000 draws, seed fixed).
- Report the median and 90% interval per concept. For each concept pair, report *P(I_a < I_b)*.
- Missing information: use the archetype default and set an `assumed` flag. Concepts with more than a pre-specified share of assumed key inputs (mass, u, material) are labelled *low-information*; this label is a reported covariate, not an exclusion rule.
- **Avoid false precision:** report results to two significant figures or rank only, whichever the pilot shows is reliable.

## 8. Validity checks (pilot, see 07/08)

1. **Benchmark validity:** apply the protocol to documented real products for which published full LCAs exist. Check rank agreement with those LCAs, as Bohm et al. (2010) benchmarked virtual concepts against real products.
2. **Inter-assessor reliability** (07).
3. **Sensitivity:** check whether arm-level rankings survive ±50% on mass, u and r and alternative washing scenarios. The ±50% value is a placeholder to be fixed pre-pilot.

## 9. Outcomes the protocol must allow

Function-first better; no difference; material-first better; more creative but higher impact; differences inside the uncertainty band. Any of these is reported as found. Discernibility (*P* > 0.9 or < 0.1) is required before any concept-level superiority statement.
