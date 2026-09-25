# Redesign before substitution: functional geometry optimization of disposable products

## Abstract

Material substitution dominates debate about disposable products, yet upstream removal of dimensions that contribute little to function may avoid material before substitution, recycling, or disposal is considered. We define functional geometry optimization (FGO) as a study-specific, service-normalized analytical lens and apply it to toilet-paper width, longitudinal center perforation, and straw–container co-design. Public product, standard, patent, and literature records were classified as observed evidence, sourced coefficients, calculations, or explicit scenarios. Analytical break-even models were combined with integer packing and fixed-seed Monte Carlo stress tests; the analysis is neither a human-use trial nor a full life-cycle assessment. In an illustrative {{num:baseline_width_mm}}-to-{{num:primary_candidate_width_mm}}-mm toilet-paper scenario, the nominal reduction was {{pct:primary_width_zero_compensation_saving}}, but benefit disappeared at {{num:primary_width_break_even_longitudinal_ratio}} times baseline longitudinal consumption. {{int:patent_contrast_count}} weak patent-reported contrasts ranged from {{pct:patent_saving_min}} to {{pct:patent_saving_max}}, with {{int:patent_positive_contrasts}} positive and {{int:patent_negative_contrasts}} negative. Center-perforation benefit depended on the share of half-width-suitable tasks and units selected; using two halves eliminated area saving for a task. For {{pct:straw_primary_length_reduction}} straw shortening and zero shifted burden, break-even was a {{pct:straw_primary_expected_replacement_rate_break_even}} expected additional replacement rate but a {{pct:straw_primary_failure_probability_break_even}} independent per-attempt failure probability. Hypothetical packing changed discontinuously from {{int:logistics_baseline_units_per_carton}} to {{int:logistics_mid_units_per_carton}} or {{int:logistics_short_units_per_carton}} units per carton. Geometry redesign is therefore a conditional cleaner-production strategy whose value depends on adequacy, response, manufacturing yield, compatibility, and logistics.

**Keywords:** material efficiency; source reduction; ecodesign; consumables; rebound; geometry

## 1. Introduction

Cleaner production places prevention ahead of treatment by seeking to avoid resource use and waste at their source {cite:unep_cp,epa_p2}. For products, that orientation asks not only which material should be used and how it should be recovered, but also how much product must be supplied to deliver a defined service. Material-efficiency research similarly emphasizes providing material services with less material production rather than equating environmental progress with any single downstream route {cite:allwood2011,allwood2013}. The service denominator matters especially for short-lived consumables, where large numbers of low-mass items create recurrent material flows and where a nominally lighter item can fail to reduce material per successful use.

Existing eco-design frameworks cover material choice, lightweighting, durability, manufacturing, distribution, use, and end of life {cite:bovea2012,ardente2014}. Circular-economy design adds slowing, closing, and narrowing resource loops, while warning that these strategies interact with product systems and business models {cite:bocken2016,geissdoerfer2017}. Geometry is present within these traditions but is often treated as one engineering variable among many. For consumables, however, spatial allocation and dispensing granularity directly determine the smallest quantity a user can select. A roll that varies only in pull length but not width, or an accessory sized independently of its container, may impose material because the available geometry is coarser than the task.

Service-normalized resource accounting provides a useful foundation. Material Input per Service Unit explicitly relates input to delivered service {cite:liedtke2014}. The same logic implies that a geometric intervention must be assessed per adequate event rather than per sheet, item, or package. A narrower sheet has less area at a fixed length, but users may pull more length, fold differently, repeat use, or reject it. A shorter straw has less material at a fixed cross-section, but difficult positioning, residual liquid, buckling, or replacement can erase that advantage. Consequently, nominal mass reduction is only a physical upper bound.

We use *functional geometry optimization* (FGO) as a study-defined term for minimizing material or scenario burden per successful functional unit by changing spatial dimensions or dispensing granularity subject to performance, behavioral, manufacturing, compatibility, safety, regulatory, and logistics constraints. FGO is not proposed as a mature field or a replacement for established eco-design. Targeted exact-phrase searches did not identify it as an established cleaner-production label. Its contribution is instead an explicit analytical synthesis: geometry is connected to function and behavior, and claims are stated as break-even conditions and falsification regions.

This modest positioning is important because reduced weight alone is not a sufficient environmental result. Dematerialization may shift burden among materials, processes, protection, transport, and end of life {cite:vandervoet2004}. Likewise, circular and efficiency measures can trigger direct or system rebound {cite:castro2022,metic2022,lowe2024}. A product that is used more intensively, replaced more often, or packed less efficiently can have a worse service-normalized outcome despite a lower nominal unit mass. The appropriate question is therefore not whether less geometry *can* use less material, which is algebraically obvious, but whether a feasible design remains below the baseline after all attributable responses.

Short-lived consumables are a useful stress test. A review of resource-efficient design for consumables found that many general recommendations for durable products do not transfer directly {cite:willskytt2021}. Consumables are depleted through heterogeneous tasks, their minimum dispensing units influence use, and their function may depend on handling conventions that are poorly represented in product catalogues. They also expose a recurrent evidence problem: dimensions are observable, but task demand and compensatory behavior often are not. This creates a temptation to treat the geometric reduction fraction as an achieved saving. The present study instead treats missing behavior as an uncertainty to be disclosed and tested.

Three connected cases were selected. First, toilet-paper width reduction changes area continuously but may induce longitudinal compensation. Second, a longitudinal center perforation adds width selection to a product already selectable in length, creating two-dimensional discretization of consumption. Third, straw shortening is examined as an accessory–container co-design problem rather than as removal of an arbitrary length. These cases span continuous dimension change, discrete dispensing change, and joint-product geometry while retaining a common service-normalized estimand.

The cases also expose different forms of prior art. Reduced-width toilet paper and longitudinally partitioned paper have long patent histories, so this study makes no product-invention, patentability, or freedom-to-operate claim {cite:us453003,us20160345786,wo2003026472}. The research contribution lies in a reproducible quantitative framework, not in claiming that narrower rolls, center perforations, or shorter straws have never been proposed. Prior art is used as evidence of concepts and limited observations, not proof of population behavior or commercial performance.

Four research questions structure the analysis. First, under what exact behavioral and engineering conditions does geometric reduction lower material per successful event? Second, how does adding a selectable dimension alter mismatch between task requirements and minimum dispensed quantity? Third, when do packaging and integer logistics convert unit-level savings into system-level improvements? Fourth, which missing measurements would most efficiently falsify or validate the modeled benefits? The study answers these questions with public evidence, analytical boundaries, transparent scenarios, uncertainty analysis, and future validation protocols. It deliberately accepts negative and conditional findings.

## 2. Methods

### 2.1 Study design and evidence states

The study was designed as a reproducible multi-case quantitative modeling and scenario analysis using verified public product, standards, patent, and literature records. It was not designed as a human-use experiment, observational consumption study, market survey, or full life-cycle assessment. Environmental comparisons were retained only where published sources defined a functional unit and boundary; the main outcome was finished-product material per successful functional event.

Source acquisition followed a persistent-snapshot protocol. Public pages, Crossref metadata responses, documents, and product records were saved locally where retrieval and usage terms allowed. The acquisition ledger records URL, UTC retrieval time, HTTP outcome, destination, file size, SHA-256 checksum, and redistribution note. Failed and empty retrievals were retained in the ledger rather than silently excluded. Original snapshots were separated from processed registries and calculated outputs.

Every input or output was assigned one of four evidence states. **OBSERVED** denotes a value transcribed from a public product, standard, patent, or study record. **SOURCED** denotes a coefficient or relationship reported by an external source. **CALCULATED** denotes a deterministic transformation of observed or scenario inputs. **ASSUMED_SCENARIO** denotes a transparent value or distribution selected for stress testing when empirical evidence was unavailable. Simulation outputs inherit the scenario label and are never described as observed frequencies.

The evidence search was targeted, not systematic. It covered cleaner production, material efficiency, eco-design, source reduction, rebound, packaging optimization, toilet-paper geometry and dispensing, straw geometry and life-cycle comparison, standards, and patent prior art. Bibliographic metadata were checked through DOI, Crossref, publisher, or official-organization records where possible. The targeted design supports model construction and claim verification but cannot establish exhaustive coverage or prove that a term or design has never appeared.

The evidence base is summarized in Table 1. Its central limitation is asymmetry between geometry and behavior: product dimensions and technical descriptions are often public, whereas task-level adequacy, acceptance, and consumption response are rarely available. This asymmetry determined the analytical strategy. Observed dimensions anchor examples, exact equations identify break-even boundaries, and unobserved responses are varied across named scenarios rather than imputed as facts.

The four research questions were mapped prospectively to methods and outputs. RQ1 used the width, center-perforation, and straw break-even equations; RQ2 used the task-mixture and two-dimensional dispensing model; RQ3 used integer packing under unchanged- and redesigned-packaging boundaries; and RQ4 used sensitivity, adverse-case stress tests, and an explicit future-validation protocol. Results and Discussion retain this ordering, and unresolved empirical questions remain labeled unresolved.

[[TABLE:1]]

### 2.2 Functional unit, estimand, and FGO framework

The toilet-paper functional unit was one successful use event meeting a prespecified adequacy and hygiene criterion. The straw functional unit was one successfully consumed beverage serving meeting liquid-access, residual-liquid, leakage, usability, and failure criteria. These are proposed study definitions that require empirical operationalization. They avoid the misleading denominators “one sheet,” “one roll,” or “one straw,” which do not guarantee equivalent service.

For design \(k\), the primary estimand was

\[
\Delta_M = 1-\frac{E[M_k\mid\text{successful functional event}]}
{E[M_0\mid\text{successful functional event}]}.
\]

The material term includes all attempts, repeats, rejected units, and attributable manufacturing loss required to obtain one successful event. A positive value denotes lower material demand; zero is break-even; a negative value denotes harm. Secondary outputs were material and packed volume per 1,000 successful events, units per carton, and functional transport density. Environmental-impact language was avoided unless external coefficients and system boundaries supported it, consistent with life-cycle functional-unit principles {cite:iso14040,iso14044}.

Figure 1 presents the causal structure. Observed geometry and task requirements generate a counterfactual design; function, response, process yield, and shifted burden then determine material per successful service. The structure separates a theoretical physical minimum from engineering-feasible and behaviorally feasible outcomes. A theoretical reduction can therefore coexist with a no-benefit behavioral result.

[[FIGURE:1]]

We define Geometry Utilization Efficiency only as a scenario diagnostic:

\[
GUE=\frac{M_{\min,\ functionally\ feasible\ under\ stated\ constraints}}
{M_{\mathrm{supplied\ baseline}}}.
\]

The numerator changes when constraints change, so GUE is not treated as a universal product property or established sustainability metric. Theoretical GUE excludes response and process limits; engineering-feasible GUE includes manufacturing and compatibility; behaviorally feasible GUE includes acceptance, compensation, failure, and replacement. An observed GUE should be reported only after empirical task-level measurement.

### 2.3 Toilet-paper width model

Let baseline and candidate widths be \(W_0\) and \(W_1\), and let total longitudinal tissue consumed per successful event be \(L_0\) and \(L_1\). With unchanged basis mass and process yield, the material ratio is

\[
R_W=\frac{W_1L_1}{W_0L_0}=r_Wr_L,
\]

where \(r_W=W_1/W_0\) and \(r_L=L_1/L_0\). The exact break-even is \(r_L^*=1/r_W\). Thus narrowing is beneficial only while the proportional increase in longitudinal consumption remains below the inverse width ratio.

The compensation elasticity was defined as

\[
\epsilon_{LW}=\frac{d\ln L}{d\ln W}.
\]

Under a constant elasticity between widths, \(L_1/L_0=(W_1/W_0)^{\epsilon_{LW}}\), giving \(R_W=(W_1/W_0)^{1+\epsilon_{LW}}\). Because \(W_1/W_0<1\), material saving requires \(\epsilon_{LW}>-1\), with exact break-even at \(-1\). This is an analytical identity, not an empirical estimate.

Observed width and use records were retained where source provenance was adequate. One patent table provided paired width/use observations for limited focus-group conditions {cite:us6458450}. Those contrasts were recalculated from the table but were not pooled into a population elasticity, because assignment, participant characteristics, task standardization, uncertainty, and generalizability were insufficient. Candidate widths were therefore used to map response surfaces, not to claim an optimal commercial width.

The illustrative reference scenario used a {{num:baseline_width_mm}}-mm baseline and {{num:primary_candidate_width_mm}}-mm candidate. No commercial, standard-derived, literature-derived, or engineering-optimal status is claimed for the candidate. Additional candidates of 100, 90, and 80 mm tested the geometry. Table 2 reports zero-compensation, moderate-compensation, and exact break-even values. Figure 2 maps the full width–elasticity surface. Adequacy loss, repeat use, altered folding, stronger basis mass, process loss, and rejection were represented as multiplicative penalties in stress tests.

[[TABLE:2]]

[[FIGURE:2]]

### 2.4 Center perforation and two-dimensional dispensing

A longitudinal center perforation divides a sheet of area \(a=WS\) into half-units \(h=a/2\), where \(S\) is transverse pitch. The intervention does not automatically save 50%, because tasks differ and users may select multiple halves. Let \(p\) be the proportion of events for which half width is functionally suitable and let \(m_h\) be the expected number of half-units used for such an event relative to one baseline full sheet. For the remaining events, let the full-task multiplier be \(m_f\). Before process and acceptance penalties,

\[
R_{CP}=(1-p)m_f+p\frac{m_h}{2}.
\]

This simple mixture exposes the key boundary. Half-width availability is valuable only when a sufficient share of tasks can use it without excessive extra units or failure. If \(m_h=2\), those tasks consume the same area as a full sheet and contribute no saving. If failed half-width selection is followed by a full sheet, the failed half itself must remain in the numerator.

The general task model distinguishes minimum area, minimum intact width, and topology. For an area-only task, the minimum number of half-units is the ceiling of required area divided by half-unit area. If intact full width is required, an even number of halves is imposed and separate pieces are not assumed equivalent. This prevents an area-only model from silently treating two narrow pieces as functionally identical to one intact sheet.

Four designs were compared conceptually using common task distributions: conventional width/conventional pitch, narrower fixed width, conventional width/center perforation, and narrower width/center perforation. This \(2\times2\) structure separates the main effects of width and dispensing granularity and reveals interaction. It also avoids attributing all gains of a combined intervention to the perforation.

The reported task mixtures were explicitly hypothetical: 25%, 50%, and 75% of tasks were half-width-suitable, with 1.2 half-units per suitable task. Manufacturing penalties represented altered perforation strength, cross-tearing, web breaks, conversion yield, and roll integrity. Existing partitionable-paper prior art confirms that longitudinal lines of weakness are feasible concepts but nontrivial converting problems {cite:us20160345786}.

### 2.5 Straw–container co-design

Straw length was modeled jointly with container access rather than optimized in isolation. Commercial systems document that straw selection depends on package dimensions, shape, and beverage properties {cite:tetra_systems}. ISO 18188 supplies a polypropylene-straw specification context but does not establish a universal minimum length for all containers and users {cite:iso18188}. The feasible length must satisfy insertion-point geometry, reach to the liquid-access region, protrusion for handling, angular tolerance, residual-liquid requirements, leakage constraints, and structural stability.

For a hollow cylindrical straw with outer diameter \(D_o\), inner diameter \(D_i\), density \(\rho\), and length \(L_s\), exact mass is

\[
m=\rho\pi L_s\frac{D_o^2-D_i^2}{4}.
\]

At fixed cross-section and density, mass is proportional to length. Let \(s\) be the length-reduction fraction, \(r\) the expected number of additional replacement straws per successful serving, and \(c\) the attributable container or package burden per successful serving normalized to baseline straw material mass. The expected-rate material ratio is

\[
R_{S,\mathrm{rate}}=(1-s)(1+r)+c.
\]

The expected additional replacement-rate break-even is \(r^*=(1-c)/(1-s)-1\); at zero shifted burden this becomes \(s/(1-s)\). This rate is not a failure probability. For a separate independent per-attempt failure probability \(p\), the expected attempts to first success are \(1/(1-p)\), giving

\[
R_{S,\mathrm{prob}}=\frac{1-s}{1-p}+c
\]

and \(p^*=1-(1-s)/(1-c)\). At zero shifted burden, \(p^*=s\). The additive placement of \(c\) follows its definition as burden incurred once per successful serving; a per-attempt burden would require a different equation. Failure and replacement summarize multiple pathways but do not imply behavioral equivalence; future tests should record positioning difficulty, incomplete access, residual liquid, buckling, leakage, rejection, and repeat use separately.

Observed configurations in the source registry included 100-mm, 98/152-mm, and 102/165-mm examples. They demonstrate design diversity but were not labeled inefficient baselines. No source linked all required container dimensions, insertion location, fill geometry, protrusion, and usability criteria well enough to calculate a universal minimum. The analysis therefore reports normalized shortening boundaries and treats container burden explicitly rather than manufacturing an unsupported optimum.

Mechanical and material substitution evidence was used only as context. Paper and plastic straws differ in water resistance, stiffness, failure mode, production, and end-of-life assumptions {cite:gutierrez2019}. Published comparisons use incompatible functional units and regional systems {cite:tetra2019,zanghelini2020,moy2021,chitaka2020}. They were not pooled into a universal ranking.

### 2.6 Packaging and logistics

Transport response was modeled under both payload and volume constraints. A reduction in item mass changes vehicle demand only if payload is binding or if package mass changes materially. A reduction in geometry changes volume only if packaging is redesigned and integer packing crosses a threshold. Accordingly, the model reports units per carton, carton dimensions, cartons per pallet or vehicle where specified, kilograms per 1,000 successful events, cubic metres per 1,000 events, and functional uses per vehicle.

Integer packing was evaluated by enumerating orientations and taking the product of floor divisions along carton axes. This produces step functions: a continuous length reduction can have no logistics effect until an additional row or layer fits, after which the effect can be discontinuous. Packaging research similarly emphasizes volume optimization and system-level box design rather than proportional conversion from product weight to transport benefit {cite:wever2011,garciaarca2020}.

Because linked commercial secondary-packaging specifications were incomplete, the integer-packing example is deliberately labeled hypothetical. The carton and unit cross-section are transparent assumptions intended to demonstrate discontinuity, not to estimate a market-average shipment. Both unchanged-packaging and optimized-repacking scenarios were retained, and zero logistics benefit was included as a stress test.

### 2.7 Uncertainty, convergence, and classification

Monte Carlo analysis propagated uncertain response rather than sampling error from a measured population. A fixed seed of {{int:monte_carlo_seed}} and {{count:monte_carlo_iterations}} draws were used. For the illustrative {{num:baseline_width_mm}}-to-{{num:primary_candidate_width_mm}}-mm width case, elasticity followed a triangular distribution from −1.2 to 0.15 with mode −0.35; successful-event adequacy ratio ranged from 0.95 to 1.00 with mode 0.99; and process penalty ranged from 0% to 2%. For center perforation, half-suitable task share followed Beta(3,3), half-task unit multiplier followed a triangular distribution from 1.0 to 1.8 with mode 1.15, success ratio ranged from 0.96 to 1.00, and process penalty ranged from 0% to 2%. For {{pct:straw_primary_length_reduction}} straw shortening, the expected additional replacement rate ranged from 0 to 0.35 with mode 0.05, and shifted container burden ranged from 0% to 5%. This primary straw Monte Carlo uses the expected-rate formulation; the independent per-attempt failure-probability formulation was evaluated separately by analytical boundary and one-way sensitivity.

These distributions are transparent scenario distributions, not fitted empirical distributions. Reported means, medians, 95% simulation intervals, and proportions above zero describe the configured uncertainty space. Convergence was checked at 10,000, 50,000, 100,000, and {{count:monte_carlo_iterations}} draws. One-way sensitivity varied elasticity, task mix, expected additional replacement rate, and independent failure probability. Stress tests included zero and strong compensation, zero logistics benefit, packing inefficiency, manufacturing penalty, low acceptance, high replacement, conservative functional minima, alternative functional units, and removal of PFAS considerations.

Outcomes were classified as **ROBUST BENEFIT** when saving remained positive across prespecified adverse assumptions, **CONDITIONAL BENEFIT** when sign changed within a plausible scenario range, and **NO BENEFIT/HARM** when the modeled ratio reached or exceeded baseline. Because the uncertainty distributions are not empirical, a high proportion of positive draws does not by itself establish robust benefit. Analytical boundaries and adverse-case stress tests control the classification.

### 2.8 Reproducibility

All calculations, figures, tables, and manuscript values were generated from versioned code and machine-readable configuration. The fixed-seed pipeline writes full compressed simulation draws, convergence diagnostics, sensitivity results, and a manuscript-value registry linking each reported number to a source file and method. Figures are exported as PDF and high-resolution PNG, tables as CSV and editable Word, and manuscript figures as an editable slide deck. Detailed scenario definitions, stress tests, and validation protocols are provided in the Supplementary material. Tests cover exact break-even identities, vectorized calculations, hollow-cylinder proportionality, and integer packing. Devin, an AI software-engineering assistant by Cognition AI, supported literature organization, code generation, reproducibility checks, and drafting; the author reviewed the sources, equations, code, outputs, and prose and remains responsible for the work. Analytical figures were generated directly from code rather than generative image tools. The intended reproduction command is `make all`.

## 3. Results

### 3.1 Evidence base, framing, and prior art

The evidence registry contained public source records across toilet paper, straw/container systems, and prior art, but its inferential strength differed by domain (Table 1). Dimensions, technical descriptions, and patent concepts were observable; controlled population estimates of toilet-paper width compensation and linked straw/container functional minima were not. Consequently, no design was declared behaviorally optimal from observed data.

The FGO framework (Figure 1) made this evidence boundary operational. Geometry can reduce supplied area, length, or mass, but the successful-service denominator introduces response, failure, and shifted burden. This distinction prevented nominal reduction from being reported as achieved cleaner-production benefit.

Prior art was extensive enough to reject product-invention novelty as a manuscript premise. Longitudinal division of rolled paper dates at least to US453003A, while later publications describe reduced-area pieces and partitionable full, half, or quarter sheets {cite:us453003,us20160345786,wo2003026472}. The defensible novelty is the cross-case, service-normalized, rebound- and logistics-aware framework and its reproducible falsification analysis.

### 3.2 Fixed-width toilet paper

For the illustrative {{num:baseline_width_mm}}-to-{{num:primary_candidate_width_mm}}-mm reference scenario, the physical width reduction and zero-compensation saving were {{pct:primary_width_zero_compensation_saving}} (Table 2). Exact break-even occurred when longitudinal consumption reached {{num:primary_width_break_even_longitudinal_ratio}} times baseline. Thus an increase of {{pct:primary_width_break_even_consumption_increase}} erased the nominal {{pct:primary_width_zero_compensation_saving}} width saving. The elasticity form produced the same boundary at \(\epsilon_{LW}=-1\). The scenario is not an estimated optimum or commercial recommendation.

Figure 2 shows that width alone does not determine sign. At any candidate width, saving is positive above the break-even elasticity and negative below it. Greater narrowing increases the zero-compensation ceiling but also reduces the absolute response margin before failure. The surface therefore supports selection of empirical experiments, not an unconditional recommendation for the narrowest design.

{{int:patent_contrast_count}} paired contrasts calculated from the patent table ranged from {{pct:patent_saving_min}} to {{pct:patent_saving_max}}, with {{int:patent_positive_contrasts}} positive and {{int:patent_negative_contrasts}} negative (Figure 3). The mixed signs directly contradict an assumption that narrowing always reduces use. Because the underlying observations were patent-reported focus-group data with limited design information, these contrasts were treated as weak evidence and were not used to fit the primary distribution.

[[FIGURE:3]]

### 3.3 Center perforation

In the transparent center-perforation mixtures, material saving before penalties was {{pct:center_low_task_mix_saving}}, {{pct:center_mid_task_mix_saving}}, and {{pct:center_high_task_mix_saving}} when 25%, 50%, and 75% of tasks, respectively, were suitable for half width and used 1.2 half-units (Table 3). These values were expected task-mixture outcomes, not empirical forecasts. They were lower than the frequently implied 50% because suitable tasks still consumed more than one half-unit on average and unsuitable tasks retained full width.

[[TABLE:3]]

Figure 3 shows how the benefit changes across the entire suitable-task fraction and alternative half-task multipliers. When suitable tasks consume two half-units, the line remains at zero: adding a selectable dimension provides no area saving. Values above two produce harm for that task class. Manufacturing loss and lower successful-event adequacy shift all curves downward.

The four-design comparison yielded a conceptual interaction. Fixed narrowing affected every task and was therefore exposed to global longitudinal compensation. Center perforation affected only tasks for which users selected half width. Their combination could reduce both continuous width and discrete mismatch, but it also combined two acceptance and manufacturing risks. Without measured task distributions and cross-tear performance, the combined design remained conditional.

### 3.4 Straw shortening and container burden

At fixed cross-section and zero shifted burden, shortening by {{pct:straw_10pct_length_reduction}}, {{pct:straw_20pct_length_reduction}}, and {{pct:straw_30pct_length_reduction}} produced equal nominal mass reductions (Table 4). Under the expected additional replacement-rate formulation, break-even values were {{pct:straw_10pct_expected_replacement_rate_break_even}}, {{pct:straw_20pct_expected_replacement_rate_break_even}}, and {{pct:straw_30pct_expected_replacement_rate_break_even}}, respectively. Under independent per-attempt failure, the corresponding boundaries were {{pct:straw_10pct_failure_probability_break_even}}, {{pct:straw_20pct_failure_probability_break_even}}, and {{pct:straw_30pct_failure_probability_break_even}}. The configured primary case was {{pct:straw_primary_length_reduction}}, with zero-shift boundaries of {{pct:straw_primary_expected_replacement_rate_break_even}} for expected additional replacement and {{pct:straw_primary_failure_probability_break_even}} for independent per-attempt failure. A 5% normalized per-successful-serving container burden reduced both tolerances. The distinction prevents the expected-rate boundary from being mislabeled as a failure probability.

[[TABLE:4]]

Figure 4 maps the complete length-reduction/expected-replacement-rate boundary; Table 4 and one-way sensitivity provide the independent-failure-probability comparison. Larger shortening creates more material headroom but is more likely to conflict with access, protrusion, stability, and ergonomics. No observed configuration was classified as excessive because the public data did not identify a common container geometry and functional threshold. The result is therefore a testable design boundary, not a recommended universal straw length.

[[FIGURE:4]]

Published straw comparisons did not support a universal material ranking. Their functional units, geographies, production systems, and end-of-life assumptions differed, and mechanical performance can alter replacement. Geometry optimization and substitution should therefore be modeled factorially: current geometry/current material, optimized geometry/current material, current geometry/substitute material, and optimized geometry/substitute material under a common service definition.

### 3.5 Logistics

The hypothetical integer-packing example increased capacity from {{int:logistics_baseline_units_per_carton}} units at {{num:logistics_baseline_length_mm}} mm to {{int:logistics_mid_units_per_carton}} at {{num:logistics_mid_length_mm}} mm and {{int:logistics_short_units_per_carton}} at {{num1:logistics_short_length_mm}} mm (Table 5). The {{pct:logistics_mid_length_reduction}} reduction from the baseline to the middle packed length therefore produced a {{pct:logistics_mid_capacity_increase}} carton-capacity increase in this geometry, not a proportional change. This discontinuity arose from floor divisions and orientation, not an environmental coefficient.

[[TABLE:5]]

The example also demonstrated the opposite boundary: if packaging remained unchanged, unit shortening generated no cube benefit. If vehicle payload rather than volume was binding, transport response depended on total item and packaging mass. Hence no transport-emission saving was inferred directly from item mass or length.

### 3.6 Scenario uncertainty and stress tests

Under the configured scenario distributions, the {{num:baseline_width_mm}}-to-{{num:primary_candidate_width_mm}}-mm width case had a median saving of {{pct:width_mc_median}}, a 95% simulation interval from {{pct:width_mc_p2_5}} to {{pct:width_mc_p97_5}}, and positive saving in {{pct:width_mc_probability_positive}} of draws (Table 6). The interval crossed zero, so the result was classified as conditional rather than robust.

The center-perforation case had a median saving of {{pct:perforation_mc_median}}, a 95% interval from {{pct:perforation_mc_p2_5}} to {{pct:perforation_mc_p97_5}}, and a positive result in {{pct:perforation_mc_probability_positive}} of configured draws. Despite the high scenario proportion, adverse boundaries remained: low suitable-task share, two or more half-units, low acceptance, or process penalty could eliminate benefit.

The {{pct:straw_primary_length_reduction}} straw-shortening expected-rate case had a median saving of {{pct:straw_mc_median}}, a 95% interval from {{pct:straw_mc_p2_5}} to {{pct:straw_mc_p97_5}}, and positive saving in {{pct:straw_mc_probability_positive}} of configured draws. Its interval also crossed zero, driven by expected additional replacement and shifted burden. Figure 5 displays all three scenario distributions and their no-benefit tails.

[[TABLE:6]]

[[FIGURE:5]]

Convergence diagnostics changed little between 100,000 and {{count:monte_carlo_iterations}} draws. One-way sensitivity recovered the analytical boundaries: width saving changed sign at elasticity −1; center-perforation saving approached zero as half-task multipliers approached two or suitable-task share approached zero; and {{pct:straw_primary_length_reduction}} straw shortening changed sign at an expected additional replacement rate of {{pct:straw_primary_expected_replacement_rate_break_even}} or an independent failure probability of {{pct:straw_primary_failure_probability_break_even}} when shifted burden was zero. These identities served as internal checks on the simulation.

### 3.7 Research-question synthesis

RQ1 was answered analytically but remains empirically unresolved: each case has an exact no-benefit boundary, while the decisive behavioral and engineering inputs are not population estimates. RQ2 showed that a second selectable dimension reduces mismatch only when half width is suitable and fewer than two half-units are consumed; otherwise the task-level area saving is zero or negative. RQ3 showed that logistics improvement requires package redesign and an integer threshold, as demonstrated by {{int:logistics_baseline_units_per_carton}}, {{int:logistics_mid_units_per_carton}}, and {{int:logistics_short_units_per_carton}} units per hypothetical carton; unchanged packaging gives zero cube benefit. RQ4 identified width compensation, task suitability and selection, straw access and failure, process yield, and measured packaging utilization as the highest-value validation measurements.

## 4. Discussion

### 4.1 Principal interpretation

The analysis supports a narrow but useful claim: removing geometry can reduce material per service, but only when function, response, process yield, and system handling remain within calculable boundaries. This is stronger than a nominal lightweighting statement because it specifies how the claim can fail. It is weaker than an empirical effectiveness claim because the decisive behavior and adequacy parameters have not yet been measured. In research-question terms, RQ1-RQ3 yield falsifiable conditional answers, while RQ4 supplies the empirical program needed to resolve them.

Across cases, the algebraic ceiling was substantial while the evidence-based conclusion remained conditional. Toilet-paper narrowing offered a {{pct:primary_width_zero_compensation_saving}} physical ceiling in the illustrative reference scenario, yet mixed patent-table contrasts and an exact {{pct:primary_width_break_even_consumption_increase}} compensation boundary prevented unconditional benefit. Center perforation offered larger modeled savings under favorable task mixtures, but its result depended on heterogeneous width requirements and selection behavior. Straw shortening was especially sensitive at modest reductions: a 10% reduction was erased by a {{pct:straw_10pct_expected_replacement_rate_break_even}} expected additional replacement rate or a {{pct:straw_10pct_failure_probability_break_even}} independent failure probability.

These findings make “redesign before substitution” a sequencing heuristic, not a claim that substitution is unnecessary. Before replacing a material, designers should ask whether the product supplies dimensions, shape, or dispensing units that do not contribute enough to service. That question can reduce the amount of either incumbent or substitute material. A paper straw that is longer than its functional geometry requires still carries avoidable paper production, and an unnecessarily large plastic product is not justified by the possibility of recycling. Conversely, substitution may be preferable when geometry cannot be reduced without loss of function, safety, or acceptance.

### 4.2 Relation to material efficiency and eco-design

FGO belongs within material efficiency, source reduction, and eco-design rather than outside them. Material-efficiency scholarship already recognizes lightweighting, reduced yield loss, longer life, and intensified use {cite:allwood2011,allwood2013}. Eco-design tools already treat geometry and material selection as interacting decisions {cite:bovea2012,ardente2014}. The present framework specializes these ideas for consumables by emphasizing selectable geometry, service-normalized throughput, response, and integer logistics.

The specialization matters because consumables differ from durable products. Their service is repeatedly purchased and depleted; a small mismatch recurs at high frequency; and the minimum selectable unit can be as important as product strength or lifetime. A roll's one-dimensional dispensing constrains width, while a pre-attached accessory inherits dimensions from a container. Geometry thus affects not only nominal mass but the resolution with which users can match material to task.

The framework also clarifies boundaries with adjacent strategies. Thinning changes cross-sectional material and may affect strength or barrier performance. Substitution changes material properties and supply systems. Reuse increases service cycles and introduces cleaning, return, and loss. Recycling changes feedstock and end-of-life flows. FGO changes spatial allocation or dispensing granularity at a stated performance threshold. These strategies can be combined; none should be treated as universally dominant.

### 4.3 Behavioral rebound as a design variable

The toilet-width model turns rebound from a qualitative warning into an exact design variable. For the {{num:primary_candidate_width_mm}}-mm candidate against {{num:baseline_width_mm}} mm, the relevant question is whether successful-event length rises by less than {{pct:primary_width_break_even_consumption_increase}}, not whether users notice the width. The elasticity boundary at −1 is independent of the absolute width and can guide study power and monitoring. Similar boundaries can be derived for basis mass, process yield, and adequacy.

Center perforation shows that response is not only “more use.” Users may fail to perceive the longitudinal line, accidentally tear across it, select two halves where one would suffice, or reject a narrow piece for a task requiring intact width. Conversely, users may exploit smaller units without changing the amount required for larger tasks. This heterogeneity is precisely why a single average saving assumption is inappropriate.

For straws, expected additional replacement is a compact summary of multiple failure pathways but should not be the only empirical outcome. A design may technically reach liquid yet produce awkward angle, insufficient protrusion, high residual volume, or buckling. These defects can reduce acceptance before they generate a recorded replacement. Future work should therefore measure attempt-level failure probability, additional units per successful serving, process outcomes, and subjective adequacy alongside mass.

Rebound reviews emphasize that direct, indirect, and economy-wide mechanisms require different methods {cite:castro2022,metic2022,lowe2024}. The present study addresses direct material rebound and selected system shifts. It does not model price-mediated demand growth or economy-wide rebound. A lower unit cost could increase consumption or alter product positioning; those mechanisms lie beyond the present boundary and should be added before making market-scale savings claims.

### 4.4 Logistics and packaging discontinuities

The integer-packing result demonstrates why product-level percentage reductions should not be translated directly into transport claims. Packaging and vehicles operate with discrete rows, layers, cartons, pallets, and legal constraints. A design can become smaller without changing package count, or cross a threshold that produces a much larger capacity change. Repacking can also require new protection, machinery, labels, or void management.

Mass- and cube-constrained systems must be separated. Toilet tissue is often low density, making cube and compression relevant, whereas dense products may be payload constrained. Straws can be bundled, attached, or packed separately, so shortening may alter neither shipping carton nor vehicle utilization. Reporting both kilograms and cubic metres per functional unit makes these mechanisms visible.

The illustrative carton was deliberately not calibrated to a commercial supply chain. Its role was to falsify proportional reasoning. A submission-ready industrial application would need measured package dimensions, orientation rules, damage rates, pallet patterns, vehicle mix, utilization, and backhaul assumptions. Until those inputs are available, the strongest claim is that logistics benefit is conditional and discontinuous.

### 4.5 Prior art, manufacturing, and implementation

Prior art changes the manuscript's novelty claim but strengthens its engineering realism. Longitudinal paper partition and reduced-area pieces have been proposed repeatedly. This means the question is not whether a perforation line can be imagined, but why a design has or has not produced acceptable performance at scale. Patent documents can identify mechanisms and testable parameters, yet they are advocacy documents and do not substitute for independent evidence.

Manufacturing penalties deserve symmetric treatment with behavioral rebound. A longitudinal perforation may change web tension, converting speed, roll integrity, dust, accidental cross-tear, or dispenser interaction. Narrower rolls may change machine utilization, packaging, and consumer compatibility. Shorter straws may require new applicators, insertion locations, or container tooling. Any attributable conversion loss belongs in material per successful event.

Implementation should proceed through bounded prototypes rather than declaring an optimum from the present model. Analytical boundaries identify the parameters worth measuring. A manufacturer can screen a candidate width by asking whether the observed upper confidence bound for compensation remains below inverse width ratio. A perforation prototype can be rejected if cross-tear or selection error consumes its task-mixture advantage. A straw candidate can be rejected if its measured expected additional replacement rate or independent failure probability plus the defined container burden crosses the corresponding length-specific boundary.

### 4.6 Substitution, life-cycle evidence, and PFAS

Straw life-cycle studies show why common service definitions and geography are essential. Studies differ in feedstock, electricity, transport, use count, disposal, and functional unit {cite:tetra2019,zanghelini2020,moy2021,chitaka2020}. Pooling their rankings would imply comparability that does not exist. A factorial comparator should hold the beverage service constant and report current versus optimized geometry for each material.

The present analysis reports material-flow reduction rather than environmental-impact reduction because it does not construct a complete inventory and impact assessment. ISO life-cycle principles require goal and scope, functional unit, system boundary, inventory, impact assessment, interpretation, and limitations {cite:iso14040,iso14044}. Material saving is relevant to prevention, but its environmental meaning can be reversed by high process losses, added container material, different energy, or failure.

PFAS evidence was retained as a secondary, evidence-specific issue. Studies have reported PFAS in samples of plant-based or commercially available straws, but results vary by market, year, material, analytical method, and target list {cite:timshina2021,boisacq2023}. It is not defensible to state that all paper straws contain PFAS. More importantly, PFAS is not necessary to the main FGO conclusion: geometry boundaries remain even if PFAS evidence is removed. Chemical safety must be assessed separately and can constrain material choice without converting a geometry study into a chemical-risk assessment.

### 4.7 Generalization and taxonomy

The same analytical lens can generate hypotheses for tissues, paper towels, napkins, wipes, cotton-swab stems, cutlery handles, stirrers, plastic-bag handles, food-packaging margins, and disposable liners. These are candidate applications, not findings that the products are oversized. Each requires its own task distribution, adequacy threshold, failure modes, and manufacturing constraints.

Nine mechanisms organize future tests: width excess, length excess, area excess, thickness excess, shape excess, excessive minimum dispensing unit, one-dimensional dispensing, unnecessary symmetry, and accessory–container mismatch. The mechanism identifies a decision variable but does not establish removable material. For example, apparently unused packaging margin may supply seal integrity, a symmetric handle may support ambidextrous use, and stem length may provide contamination control.

The taxonomy is valuable when it changes measurement. Width excess calls for compensation and intact-width outcomes. Length excess calls for reach, protrusion, and handling. Minimum-unit excess calls for task mixtures and selection errors. Accessory–container mismatch calls for joint geometry and shifted burden. A general term is justified only if it directs case-specific falsification rather than labeling ordinary lightweighting as novel.

### 4.8 Limitations

The most important limitation is lack of controlled empirical behavior. No robust population estimate of toilet-paper width–consumption elasticity was found, and task-level suitability for half width was not measured. The Monte Carlo distributions are scenarios chosen to span plausible mechanisms; their positive proportions cannot be interpreted as posterior probabilities or expected market performance.

The straw model lacks linked observations for container geometry, insertion point, liquid-access target, residual threshold, protrusion, and user acceptance. Consequently, it cannot estimate a universal minimum length. The packaging model is illustrative and omits measured carton, pallet, damage, and vehicle data. Environmental coefficients were not combined because source studies used incompatible systems.

Patent evidence has limited independence and external validity. Product pages can change and may omit technical tolerances. Some public-source retrievals failed or returned empty responses; these were preserved in the acquisition ledger. The literature search was targeted and therefore cannot support a claim of exhaustive novelty. Exact-phrase non-detection does not prove worldwide absence of terminology.

The functional units themselves require validation. “Successful toilet-paper event” involves sensitive, heterogeneous behavior and hygiene criteria. “Successfully consumed beverage serving” depends on beverage, container, context, accessibility, and user population. Any empirical program must protect privacy, minimize participant burden, and define adequacy before observing results.

### 4.9 Future validation

A toilet-paper study should use a randomized crossover design in which participants experience baseline and candidate geometries in balanced order. Roll-weight measurement or instrumented dispensing should capture total mass or length per event without relying only on recall. Prespecified outcomes should include successful-event material, pull length, number of sheets or units, folding strategy, repeat use, adequacy, leakage or hygiene failure, and acceptability. Analysis should estimate within-participant response and the upper bound relative to the exact break-even.

Center-perforation validation should cross width and dispensing granularity in a \(2\times2\) design. The protocol should record whether half width was available, noticed, selected, accidentally torn, combined with another half, or followed by a full sheet. Tasks should be classified prospectively by intact-width and area requirements rather than inferred from the amount used. Manufacturing trials should measure web breaks, line strength, conversion speed, waste, roll integrity, and dispenser compatibility.

A straw program should begin with a geometric bench rig. Container height, fill level, insertion point, straw angle, and target residual volume should be varied systematically. Outcomes should include accessible liquid fraction, residual mass, protrusion, insertion and handling force, buckling, leakage, detachment, and replacement. Candidate lengths that pass the bench boundary can proceed to randomized user evaluation with beverage viscosity and accessibility needs represented.

Both programs should preregister adequacy and exclusion rules, retain negative outcomes, and report material per successful service. Life-cycle comparison should be added only after geometry and performance are established, using a common functional unit and region-specific inventory. Industrial logistics validation should then measure actual packages, pallets, damage, and vehicle utilization. This staged sequence allocates empirical effort to the uncertainties most capable of changing the decision.

## 5. Conclusions

Functional geometry optimization is best understood as a study-defined, geometry-specific implementation of material efficiency and source reduction. Across toilet-paper width, center perforation, and straw–container co-design, nominal reduction created a calculable opportunity but not a guaranteed benefit. Exact break-even equations exposed how compensation, unsuitable tasks, failure, expected additional replacement, process loss, container burden, and unchanged packaging can eliminate savings.

The defensible cleaner-production message is therefore “redesign before substitution,” with *before* meaning “evaluate upstream geometric necessity,” not “reject material change.” Geometry and material should ultimately be optimized together against one successful service. The present reproducible model supplies boundaries and validation priorities; it does not supply population effectiveness or a universal optimum.

The strongest result is methodological: conditional and negative regions can be specified before a prototype or trial. That makes geometry proposals falsifiable and helps prevent nominal mass reductions from being mislabeled as achieved environmental gains. RQ1-RQ3 are answered as analytical and scenario-dependent boundaries rather than population effects; RQ4 remains a defined validation agenda. Future controlled measurement should focus on the response parameters that cross those boundaries.

## Declarations

**Funding:** [AUTHOR ACTION BEFORE SUBMISSION: confirm funding. If no specific funding applied, use the journal-recommended no-specific-grant statement; otherwise provide funder names, grant identifiers, and sponsor roles.]

**Competing interests:** [AUTHOR ACTION BEFORE SUBMISSION: complete the Elsevier declarations tool, upload its DOC/DOCX output, and insert the author-confirmed statement here.]

**Ethics:** This study analyzed public documents and hypothetical scenarios and did not enroll human participants or use identifiable personal data. The proposed future validation protocols would require appropriate ethics review before implementation.

**Data and code availability:** Publicly redistributable processed data, source registries, code, configuration, tests, figures, and tables are available at https://github.com/bougtoir/functional_geometry. Acquisition ledgers identify public raw-source snapshots and retrieval failures. Copyrighted or restricted source documents are not redistributed where terms do not permit it. [AUTHOR ACTION BEFORE SUBMISSION: insert the DOI or persistent release identifier for the exact submitted version.]

**CRediT authorship contribution statement:** [AUTHOR ACTION BEFORE SUBMISSION: confirm and insert the final CRediT role list for every author.]

**Declaration of generative AI and AI-assisted technologies in the manuscript preparation process:** During preparation, the author used Devin, an AI software-engineering assistant by Cognition AI, to support literature organization, code generation, reproducibility checks, and drafting. The author critically reviewed the sources, code, calculations, and text, edited the output, and takes full responsibility for the content.
