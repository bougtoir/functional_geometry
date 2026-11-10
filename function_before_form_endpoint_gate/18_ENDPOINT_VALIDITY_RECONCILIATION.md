# 18 — Endpoint Validity Reconciliation

**Central risk (not minor).** The screening LCA may measure the *assessor's assumptions* rather than the participant's design. This file states what can be pre-specified, revises the failure-adjusted endpoint, and defines the test of assumption dominance. **Nothing here is validated.**

## 1. Pre-specification feasibility for two candidate tasks

| Element | T1 Single-serve meal utensil service | T2 Single beverage serving service |
|---|---|---|
| Functional unit | Transfer of one defined meal portion (mixed liquid/semi-solid/solid) from container to mouth at the point of consumption; N = 1,000 meals | Consumption of one 250 mL hot or cold beverage at the point of sale; N = 1,000 servings |
| Functional adequacy | Handles all three food textures; rigid enough for the specified load; usable for the meal duration | Holds the volume without leakage; thermal handling safe for hot drinks; usable for the consumption duration |
| Safety / hygiene | No sharp edges, choking hazards or migration-prone materials; a cleaning route for reusables; clean at point of use | Food-contact suitable; a cleaning route for reusables; lid/spill safety for take-away |
| System boundary | Cradle-to-grave per FU: materials, manufacture, transport (fixed scenario), use (cleaning), losses, EoL, plus an infrastructure share (washing equipment, return logistics) | Same, including dispensing equipment and return or deposit logistics |
| Reference service | Single-use utensil as currently supplied (archetype) | Single-use cup as currently supplied (archetype) |
| Minimum design description | 06 SCD fields 1–9 (materials, mass class, process, use pattern, supporting system, EoL) | Same |
| Material / manufacturing assumptions | Frozen archetype library (05 §5); mass classes | Same |
| Use-cycle assumptions | Uses per unit u: archetype default with a range | Same; return rate for deposit schemes |
| Replacement / failure | Loss / breakage rate r: default with a range | Same, including non-return rate |
| Supporting infrastructure | Washing per use (scenario set); share of equipment | Washing; dispenser; reverse logistics |
| Impact categories | Primary: climate change (GWP100). Secondary: fossil resource use, water consumption, plus one toxicity- or particulate-type category (method and version fixed pre-pilot, e.g. EF 3.x or ReCiPe midpoint) | Same |
| Uncertainty / data quality | Pedigree scores, parameter ranges, Monte Carlo, discernibility (05 §7) | Same |

**Feasibility judgement.**
- Both tasks can be pre-specified on paper.
- **Both are reuse-sensitive.** Rankings between single-use and reusable concepts will depend strongly on u, r and washing scenarios.
- A third, less reuse-dominated task should be screened before the final selection. T3 (goods protection, with product loss inside the FU) is a candidate.

**Burden shifting.**
- A concept is flagged if it improves GWP but worsens any secondary category beyond a pre-set relative margin.
- Flags are reported per arm. GWP alone is never called "environmental performance".

## 2. Failure-adjusted endpoint: reassessment

The previous protocol (05 §6) added the reference-product burden to every FE-FAIL concept (`I_i + I_ref`). **This is withdrawn as the primary rule.** It treats every failure as if it occurred in use. The four failure situations differ:

| Situation | Real burden | Treatment in E3 |
|---|---|---|
| 1 Concept rejected at the design stage (fails F1–F8 on paper) | **None.** Nothing is produced | Not given an impact. Recorded as FE = FAIL in the hierarchical outcome (§3) |
| 2 Manufactured but unusable | Production burden plus the reference service still needed | Not observable in a design experiment. Applies only in an *implementation scenario*, as a sensitivity analysis (§5) |
| 3 Fails during use (breakage, loss) | Partial service; replacement | Modelled **within** FE-PASS concepts via the failure/loss rate r, not as a penalty |
| 4 Requires backup service | Backup share | Modelled **within** the system inventory (e.g. a share of single-use backup) when the concept depends on it (F8) |

## 3. Primary outcome: hierarchical (ITT, no conditioning)

For every randomised participant:
1. **Level 1:** FE status of the final concept (PASS > INDETERMINATE > FAIL; a missing concept counts as FAIL).
2. **Level 2:** among concepts at the same FE level, failure-free impact per FU (05 §6 without the I_ref term), compared using discernibility (P(I_a < I_b) > 0.9 → a "win"; otherwise a tie).

**Analysis.** A pairwise hierarchical comparison across arms (win-ratio / win-probability type) over all participant pairs from two arms.
- It uses every participant.
- It does not condition on FE.
- It makes functional failure visible: no failing concept can "win" on low material use.

**Reported separately (secondary):**
- the FE-PASS proportion per arm (ITT);
- the impact distribution among FE-PASS concepts (descriptive only);
- the proportion of non-evaluable (INDETERMINATE or low-information) concepts per arm.

**Why not condition on FE-PASS.** FE status is a post-randomisation outcome. Comparing impact only among PASS concepts compares different sub-populations, a principal-stratification problem. Such a comparison is not a causal effect of framing unless strong, untestable assumptions hold. It is therefore descriptive only, optionally with bounds.

**Sensitivity analyses.**
- (a) Original `I_i + I_ref` rule (Situation 2 logic).
- (b) INDETERMINATE treated as PASS.
- (c) Level-2 ties defined at P > 0.8 and at P > 0.95.
- (d) Impact-only analysis among PASS concepts, labelled descriptive.

## 4. Assumption dominance

Parameters likely to dominate rankings: uses per unit (u); cleaning energy, water and detergent per use; loss or non-return rate (r); manufacturing yield; transport distance and mode (fixed scenario, but varied in sensitivity); material mass (participant estimate vs mass-class default).

**Test (pre-pilot).**
1. Define a defensible range for each parameter, frozen with sources before any concept is assessed.
2. For each concept pair in the pilot set, sample the joint parameter space (Monte Carlo over the ranges). Compute the **rank-stability share**: the fraction of pairs whose ordering holds with P > 0.9 across the space.
3. Run a variance-based global sensitivity analysis to name the dominant parameters.
4. **Pre-specified failure rule.** If most concept pairs (the threshold, e.g. > 50%, is fixed pre-pilot) reverse order within the defensible ranges, **the environmental endpoint is not validated** for that task. The task is dropped or narrowed (e.g. reuse parameters fixed by the brief and stated to all arms).

**Mitigation by design.**
- Fixing u, r and the washing scenario *in the common brief* (e.g. "assume the service operates in a canteen with an industrial dishwasher") removes the assessor's discretion over these parameters. It also keeps the design space identical across arms.
- It narrows external validity, which must be stated.

## 5. Status

The endpoint is credible **in principle** only if it passes the §4 dominance test, plus assessor agreement and benchmark validity (19). **Not validated.**
