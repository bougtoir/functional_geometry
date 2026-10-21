# Functional Geometry Optimization: analytical framework and hostile JCLP review

**Role:** Models and reviewer risks
**Access date for all web sources:** 2026-09-24
**Evidence labels:** **Verified** = directly supported by cited source; **Derived** = mathematical consequence of stated assumptions; **Inference** = reasoned interpretation; **Unresolved** = evidence not found or not yet collected.

## 1. Executive verdict

**Verified.** The Journal of Cleaner Production (JCLP) defines itself as an international, transdisciplinary cleaner-production journal centered on preventing waste and increasing resource efficiency. Its current guide describes original articles as 6,000–8,000 words and caps all contributions at 50 references. Its official editorial material prioritizes prevention, life-cycle thinking, holistic/systematic thinking, and approaches that exceed a single isolated application. Its desk-rejection policy explicitly names scope, novelty, quality, and technical conformity as grounds for rejection.
Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/publish/guide-for-authors ; https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news ; https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news/policy-statement-for-rejecting-articles-before-peer-review

**Hostile-editor verdict.** A paper that merely calculates “percentage less paper/plastic from smaller dimensions” is likely to be judged a product-specific arithmetic exercise. The defensible JCLP contribution is a **falsifiable, multi-case framework for upstream material-demand prevention under functional, behavioral, manufacturing, packaging, and logistics constraints**, with the three products serving as demonstrations rather than inventions. This positioning follows JCLP’s stated emphasis on source prevention and systematic analysis, while acknowledging that “designing products with less material,” ecodesign geometry optimization, sustainable packaging design, and rebound-aware design already exist.
Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news ; https://doi.org/10.1016/j.resconrec.2010.11.002 ; https://doi.org/10.1016/j.procir.2023.02.062 ; https://doi.org/10.1002/pts.887 ; https://doi.org/10.1017/dsj.2024.32

**Verified novelty constraint.** Longitudinal/two-dimensional partitioning of rolled paper is not new. US453003A described a wide roll divided into longitudinal series by vertical and transverse lines of weakness in 1891. US20160345786A1/US9918595B2 describes partitionable paper towel capable of full-, half-, or quarter-sheet separation and discusses machine-direction perforation strengths and converting feasibility. WO2003026472A1 concerns reducing toilet-paper piece area/altering weakness-line geometry. Therefore, the manuscript must not imply invention, patentability, or first disclosure of center perforation. Its plausible novelty is the quantitative cleaner-production performance model, task-mixture formulation, behavioral break-even analysis, and joint comparison with width reduction and accessory-container optimization. Google Patents’ status/assignee fields are explicitly not legal opinions.
Sources: https://patents.google.com/patent/US453003A/en ; https://patents.google.com/patent/US20160345786A1/en ; https://patents.google.com/patent/US9918595B2/en ; https://patents.google.com/patent/WO2003026472A1/en

## 2. Claims boundary and study identity

**Recommended study identity (Derived/Inference):** “A reproducible multi-case quantitative modelling and scenario-analysis study using public product/standards data, analytical optimization, uncertainty analysis, integer logistics modelling, and falsification stress tests.” Do not call it a human-use trial, observational consumption study, or full LCA. ISO 14040 defines LCA around goal/scope, inventory, impact assessment, interpretation, reporting, limitations, and critical review; the EU Product Environmental Footprint (PEF) method requires a quantified functional unit, reference flow, system boundary, assumptions/limitations, sensitivity, and uncertainty analysis.
Sources: https://www.iso.org/standard/37456.html ; https://www.iso.org/standard/38498.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

**Primary estimand (Derived):**

\[
\Delta_M=1-\frac{\mathbb{E}[M_1\mid\text{one successful functional event}]}
{\mathbb{E}[M_0\mid\text{one successful functional event}]}.
\]

The estimand must include all attempts, repeats, failures, rejected units, and intervention-specific conversion losses attributable to obtaining one adequate event. A simple ratio of nominal unit masses answers a different question and is not functionally equivalent. Comparative-LCA scholarship distinguishes reference-flow, property, and performance functional units and states that complete equivalence is often difficult; end-product comparisons favor performance functional units.
Sources: https://doi.org/10.1111/jiec.13218 ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

**Secondary estimands (Derived):**

- finished-product material per 1,000 successful events;
- primary packaging mass and packed volume per 1,000 successful events;
- functional transport density \(FTD=\text{successful events}/\text{transport m}^3\);
- scenario-specific transport tonne-km or vehicle-km per 1,000 successful events;
- environmental indicators only when source coefficients, geography, allocation, energy mix, end-of-life, and affected life-cycle stages are explicit.

Do not rename \(\Delta_M\) “environmental-impact reduction.” Material reduction can shift burdens among material production, conversion, package protection, transport, use failure, and end-of-life; ISO/PEF require explicit boundary and affected stages.
Sources: https://www.iso.org/standard/37456.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

**Data-state rule (Recommended):** Every parameter must carry one of `OBSERVED`, `INFERRED`, `CALCULATED`, or `ASSUMED_SCENARIO`. Simulation output must never be labeled observed. This is necessary for transparent limitations and reproducibility under ISO/PEF-style reporting.
Sources: https://www.iso.org/standard/37456.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

## 3. General model and geometry-efficiency metric

Let design \(x\) contain product and package geometry, material, tolerances, and dispensing granularity. Let \(\theta\) contain task demand, user response, manufacturing performance, logistics utilization, and environmental coefficients.

\[
\min_x \ \mathbb{E}_{\theta}[E(x,\theta)]
\]

subject to:

\[
\Pr(F(x,\theta)\ge F_{\min})\ge 1-\alpha_F,\quad
\Pr(U(x,\theta)\ge U_{\min})\ge 1-\alpha_U,
\]

plus regulatory, safety, compatibility, manufacturing, package-protection, and logistics constraints.

**Derived.** Chance constraints are preferable to pretending that one deterministic “minimum functional geometry” applies to all users/tasks. Report theoretical, engineering-feasible, behaviorally feasible, and empirically observed minima separately.

Define event-level functionally required material \(M_{\min,j}\) only relative to an explicit task \(j\) and adequacy rule. Then:

\[
GUE_j=\frac{M_{\min,j}}{M_{\text{supplied},j}},\qquad
GEF_j=1-GUE_j.
\]

For a task mixture \(\pi_j\), use a ratio of expectations when estimating system throughput:

\[
GUE_{\text{system}}=
\frac{\sum_j\pi_j\,\mathbb{E}[M_{\min,j}]}
{\sum_j\pi_j\,\mathbb{E}[M_{\text{supplied},j}]}.
\]

Do not average event-level ratios unless the estimand is explicitly “mean individual efficiency,” because \(\mathbb{E}[A/B]\neq\mathbb{E}[A]/\mathbb{E}[B]\). “GUE/GEF” should be presented as proposed notation, not an established concept, unless a dedicated terminology search establishes precedence. Existing literature already covers material efficiency, ecodesign, lightweighting, and geometry/process/material co-optimization.
Sources: https://doi.org/10.1016/j.resconrec.2010.11.002 ; https://doi.org/10.1016/j.procir.2023.02.062 ; https://doi.org/10.1016/j.cesys.2023.100114 ; https://doi.org/10.1080/09544828.2023.2261094

### Generalization taxonomy

Use the taxonomy as a set of testable mechanisms, not as evidence that every listed product is oversized:

| Mechanism | Decision variable | Candidate applications, not findings |
|---|---|---|
| width excess | supplied width vs minimum intact/contact width | toilet tissue, towels, napkins, wipes, liners |
| length excess | supplied/reach length vs access and handling need | straws, stirrers, swab stems, cutlery handles |
| area excess | supplied area vs absorptive/contact area | tissues, napkins, towels, wipes, packaging margins |
| thickness excess | wall/sheet thickness vs strength/barrier requirement | straws, handles, liners, films |
| shape excess | material outside load/contact/barrier paths | cutlery, handles, food-packaging margins |
| excessive minimum dispensing unit | smallest available piece exceeds small-task demand | tissue, towels, napkins, wipes |
| one-dimensional dispensing | length can vary but width/shape cannot | rolled paper and film products |
| unnecessary symmetry | symmetric geometry despite asymmetric function/load | handles, utensils, accessories |
| accessory–container mismatch | accessory sized independently of insertion/access geometry | straws, stirrers, liners, bag handles |

**Boundary against adjacent strategies:** FGO changes spatial allocation or dispensing granularity at a defined performance level; substitution changes material; lightweighting/thinning mainly reduces thickness/density; reuse increases service cycles; recycling changes secondary-material/end-of-life flows. The strategies can interact and should not be presented as mutually exclusive. Existing material-efficiency and ecodesign literature requires this modest positioning.
Sources: https://doi.org/10.1016/j.resconrec.2010.11.002 ; https://doi.org/10.1016/j.procir.2023.02.062 ; https://doi.org/10.1080/09544828.2023.2261094

## 4. Toilet-paper width: exact rebound model

Let \(W_0\) and \(W_1\) be baseline and intervention widths, \(L_0\) and \(L_1\) total longitudinal tissue consumed per successful event, and \(b_0,b_1\) finished-product basis mass (including all plies) per unit area. Let \(c_0,c_1\) be conversion-yield multipliers, where \(c>1\) represents attributable manufacturing waste per delivered tissue area.

\[
R_M=
\frac{b_1c_1W_1\,\mathbb{E}[L_1]}
{b_0c_0W_0\,\mathbb{E}[L_0]},\qquad
\Delta_M=1-R_M.
\]

If basis mass and conversion yield are unchanged:

\[
R_M=r_Wr_L,\quad
r_W=\frac{W_1}{W_0},\quad
r_L=\frac{\mathbb{E}[L_1]}{\mathbb{E}[L_0]}.
\]

**Exact finite break-even (Derived):**

\[
r_L^\star=\frac{1}{r_W}=\frac{W_0}{W_1}.
\]

Thus a 10% width reduction (\(r_W=0.90\)) is erased when successful-event longitudinal consumption rises by \(1/0.90-1=11.11\%\); this is algebra, not an empirical prediction.

With local elasticity:

\[
\varepsilon_{LW}=\frac{d\ln L}{d\ln W}.
\]

If \(\varepsilon_{LW}\) is constant between \(W_0\) and \(W_1\):

\[
\frac{L_1}{L_0}=\left(\frac{W_1}{W_0}\right)^{\varepsilon_{LW}},\qquad
R_M=\left(\frac{W_1}{W_0}\right)^{1+\varepsilon_{LW}}.
\]

For narrowing (\(W_1/W_0<1\)), material saving requires \(\varepsilon_{LW}>-1\); exact break-even is \(\varepsilon_{LW}=-1\). Do not estimate this elasticity from product catalog dimensions; it requires consumption response data, ideally the proposed randomized crossover study.

### Failure/repeat decomposition

For attempt \(a\), let \(L_{ka}\) be length used under design \(k\), \(A_{ka}\in\{0,1\}\) indicate adequate completion, and \(T_k\) be the stopping attempt. The correct successful-event length is:

\[
L_k^{(\mathrm{success})}=\sum_{a=1}^{T_k}L_{ka}.
\]

If attempts are independent with success probability \(q_k\) and expected attempt length \(\mu_{L,k}\), then:

\[
\mathbb{E}[L_k^{(\mathrm{success})}]=\frac{\mu_{L,k}}{q_k}.
\]

This geometric-attempt simplification must not be used when users adapt pull length after failure; in that case simulate the conditional sequence. The break-even becomes:

\[
\frac{b_1c_1W_1\mu_{L,1}/q_1}
{b_0c_0W_0\mu_{L,0}/q_0}=1.
\]

**Falsification boundary:** width reduction fails if increased pull length, lowered adequacy, repeat use, stronger basis weight, conversion losses, or rejection jointly push this ratio to \(\ge1\). Rebound-aware design is an established concern; do not assume engineering efficiency survives behavioral response.
Sources: https://doi.org/10.1017/dsj.2024.32 ; https://doi.org/10.1016/j.ecolecon.2019.106544

## 5. Center perforation as two-dimensional consumption discretization

Let baseline sheet pitch be \(S\), width \(W\), and full-sheet area \(a=WS\). A center line creates half-units of area \(h=a/2\). For task \(j\), define:

- \(A_j^\ast\): minimum absorptive/contact area under a prespecified adequacy test;
- \(w_j^\ast\): minimum intact width;
- \(z_j\): topology indicator (whether separate half-width pieces are functionally equivalent to an intact full-width piece);
- \(N_{0j}\): full sheets actually consumed at baseline;
- \(N_{1j}\): half-units actually consumed under center perforation, including torn, dropped, rejected, and repeat units.

The observed/scenario throughput ratio is:

\[
R_{CP}=
\frac{b_1c_1(a/2)\sum_j\pi_j\mathbb{E}[N_{1j}]}
{b_0c_0a\sum_j\pi_j\mathbb{E}[N_{0j}]}
=
\frac{b_1c_1}{b_0c_0}
\frac{\sum_j\pi_j\mathbb{E}[N_{1j}]}
{2\sum_j\pi_j\mathbb{E}[N_{0j}]}.
\]

**Exact break-even (Derived):**

\[
\frac{b_1c_1}{b_0c_0}
\sum_j\pi_j\mathbb{E}[N_{1j}]
=
2\sum_j\pi_j\mathbb{E}[N_{0j}].
\]

### Engineering lower bound, not predicted behavior

For area-only tasks where \(w_j^\ast\le W/2\) and separate halves are equivalent:

\[
N_{1j}^{\min}=\left\lceil\frac{A_j^\ast}{h}\right\rceil,\qquad
N_{0j}^{\min}=\left\lceil\frac{A_j^\ast}{a}\right\rceil.
\]

If an intact width is required or halves are not equivalent, force an even number of half-units:

\[
N_{1j}^{\min}=2\left\lceil\frac{A_j^\ast}{a}\right\rceil.
\]

This explicitly separates **area sufficiency** from **shape/topology sufficiency**. Treating all tasks as area-only is a likely reviewer attack because two narrow pieces need not equal one intact sheet.

### Transparent hypothetical task mixture

When empirical task frequencies are unavailable, use named scenarios, not pseudo-data:

\[
\pi=(\pi_{\text{small,half-feasible}},
\pi_{\text{full-width}},
\pi_{\text{multi-sheet}},
\pi_{\text{rejection/failure}}),\quad \sum\pi_j=1.
\]

Run the full simplex or structured grid rather than selecting a favorable mixture. In the simplest one-sheet baseline, if a proportion \(p\) of events successfully uses one half-unit and the rest uses one full sheet, then:

\[
R_{CP}=p/2+(1-p)=1-p/2,\qquad \Delta_M=p/2.
\]

If half-unit attempts fail with probability \(f\) and a failed half is followed by a full sheet, expected material for that class is \(h+fa\), so it is beneficial against one full sheet only when:

\[
\frac12+f<1\quad\Longleftrightarrow\quad f<\frac12.
\]

Add tearing and selection errors directly to \(N_{1j}\). This threshold is illustrative, conditional on the stated recovery rule, and not an empirical estimate.

### Required four-design comparison

Use the same task mixture and adequacy rules for:

1. conventional width and conventional transverse sheet pitch;
2. narrower fixed width;
3. conventional width plus center perforation;
4. narrower width plus center perforation.

This is a \(2\times2\) geometry design (width × dispensing granularity). Report main effects and interaction rather than attributing the combined result entirely to perforation. Exclude a cell only for a documented manufacturing/compatibility constraint, not because its result is unfavorable.
Rationale sources: https://doi.org/10.1111/jiec.13218 ; https://patents.google.com/patent/US20160345786A1/en

### Manufacturing comparator

The model must include perforation strength, web breaks, converting speed/yield, accidental cross-tearing, roll integrity, and dispenser behavior. The partitionable-paper-towel patent demonstrates that machine-direction perforation is an existing, nontrivial converting problem with specified relative perforation strengths; a toilet-tissue perforation study likewise treats tear efficiency as an engineering design variable.
Sources: https://patents.google.com/patent/US20160345786A1/en ; https://patents.google.com/patent/US9918595B2/en ; https://doi.org/10.3390/eng4010005

## 6. Straw–container joint geometric optimization

For a straight circular straw with outer diameter \(D\), wall thickness \(t\), density \(\rho\), and length \(L\), exact material mass is:

\[
M_s=\rho L\frac{\pi}{4}\left[D^2-(D-2t)^2\right]
=\rho\pi L(Dt-t^2).
\]

The thin-wall approximation \(M_s\approx\rho\pi DtL\) is acceptable only when \(t/D\) is small and approximation error is reported.

Let \(p\) be the lid insertion point, \(q\) the required liquid-access endpoint, \(h\) the external mouth protrusion measured along the straw, and \(\tau\) the lid/seal traversal allowance. Then:

\[
L(p,q)=\|p-q\|+h+\tau.
\]

For an upright container of liquid height \(H\), horizontal insertion-to-target offset \(d\), and allowed bottom clearance \(c\):

\[
L=\sqrt{(H-c)^2+d^2}+h+\tau.
\]

For a constant-area container base \(A_b\), if aspiration ceases at the endpoint height:

\[
V_{\mathrm{res}}=A_bc.
\]

Given maximum residual \(V_{\max}\), the shortest straw uses the largest allowed clearance:

\[
c^\star=\frac{V_{\max}}{A_b},\qquad
L_{\min}=\sqrt{\left(H-\frac{V_{\max}}{A_b}\right)^2+d^2}+h_{\min}+\tau.
\]

For a general container with cross-sectional area \(A(z)\):

\[
V_{\mathrm{res}}(c)=\int_0^c A(z)\,dz,
\]

and \(c^\star\) is the largest \(c\) satisfying \(V_{\mathrm{res}}(c)\le V_{\max}\). This must be solved from measured/CAD geometry; a diagonal formula must not be assumed to describe actual designs.

### Required constraints

\[
\begin{aligned}
&V_{\mathrm{res}}(p,q,\text{orientation})\le V_{\max},\\
&h_{\min}\le h\le h_{\max},\\
&\Pr(\text{access and usability over specified orientations})\ge1-\alpha,\\
&P_{\mathrm{cr}}=\frac{\pi^2EI}{(K L_{\mathrm{free}})^2}\ge\gamma P_{\mathrm{insert}},\\
&\kappa\le\kappa_{\max}\quad\text{or bend radius}\ge R_{\min},\\
&\text{seal leakage, puncture, choking/safety, manufacturing, and package constraints pass}.
\end{aligned}
\]

Shortening increases ideal Euler buckling load as \(1/L^2\), but insertion, puncture, kink/Brazier collapse, flexible sections, and boundary conditions require bench validation rather than reliance on Euler theory alone.
Source for thin-tube ovalization/kink phenomenon: https://doi.org/10.1017/CBO9780511624278.017

### Intervention mass per successful beverage

Let \(r_A\) be intervention/baseline cross-sectional material-area ratio, \(r_L=L_1/L_0\), \(q_k\) serving success probability, and \(n_k\) expected straws opened per attempt. Then:

\[
R_{M,s}=r_A r_L
\frac{n_1/q_1}{n_0/q_0}.
\]

Any burden from relocating a port, changing the lid, strengthening the container, adding a telescoping/bending feature, or changing secondary packaging must be added:

\[
\Delta E_{\text{system}}=\Delta E_{\text{straw}}+\Delta E_{\text{container}}
+\Delta E_{\text{package}}+\Delta E_{\text{transport}}
+\Delta E_{\text{use failure}}+\Delta E_{\text{EoL}}.
\]

Prior container–straw patents already describe integrated geometry and straws only slightly longer than carton height, so novelty cannot rest on “jointly design straw and container.”
Sources: https://patents.google.com/patent/US6431434B1/en ; https://patents.google.com/patent/US3215329A/en

## 7. Packaging and integer logistics

For an axis-aligned unit with dimensions \((a,b,c)\) and carton \((A,B,C)\), a simple homogeneous-orientation lower-bound packing count is:

\[
N_{\mathrm{carton}}^{\mathrm{grid}}=
\max_{o\in\mathcal{O}}
\left\lfloor\frac{A}{a_o}\right\rfloor
\left\lfloor\frac{B}{b_o}\right\rfloor
\left\lfloor\frac{C}{c_o}\right\rfloor,
\]

where \(\mathcal O\) contains the six orthogonal orientations. Label this a grid solution, not a global 3-D packing optimum; mixed orientations and compressibility can outperform it.

At pallet/vehicle level:

\[
N_{\mathrm{vehicle}}=
\min\left(
N_{\mathrm{slot/volume}},
\left\lfloor\frac{P_{\max}-M_{\mathrm{tare}}}{M_{\mathrm{loaded\ unit}}}\right\rfloor
\right),
\]

with all carton, layer, pallet, and vehicle counts integer. Then:

\[
FTD=\frac{N_{\mathrm{vehicle}}\times
\mathbb{E}[\text{successful events per shipped unit}]}
{V_{\mathrm{vehicle}}}.
\]

Model at least two toilet-paper scenarios: (i) unchanged external pack dimensions, yielding no volume/logistics benefit; and (ii) redesigned packing based on verified package dimensions. Vehicle emissions are stepwise under integer loading and may remain unchanged until a pallet/trip threshold is crossed. Sustainable-packaging literature explicitly treats packaging as a system involving product protection and logistics, not just minimum material.
Source: https://doi.org/10.1002/pts.887

**Stress tests required:** zero repacking benefit; mass-constrained vehicle; volume-constrained vehicle; mixed constraint; 70–100% utilization; carton/pallet dimensional tolerances; damage-rate penalty; extra packaging required; no avoided vehicle trip.

## 8. Monte Carlo design, convergence, and sensitivity

### Distribution rules

1. Use empirical bootstrap or fitted distributions only when sample data exist and are archived.
2. Use bounded/truncated distributions for physical dimensions and tolerances.
3. Use beta distributions for probabilities only when parameters are tied to observed counts or are explicitly labeled scenario priors.
4. Use categorical/Dirichlet models for task mixtures only with observed frequencies; otherwise evaluate a transparent grid/simplex.
5. Preserve dependence among dimensions, mass, package size, and failure parameters using joint resampling or a documented copula/rank-correlation model; independent sampling can create impossible products.
6. Keep epistemic scenario uncertainty separate from aleatory variation; do not blend speculative minima and observed manufacturing variation into one apparently empirical interval.

PEF explicitly distinguishes sensitivity and uncertainty analysis and requires assumptions/limitations to be stated.
Source: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

### Replication and convergence

Use fixed, published seeds and \(R\) independent replicated randomized Latin-hypercube or Monte Carlo runs. Increase \(N\) sequentially, e.g. \(2^{10},2^{11},\ldots\), and monitor:

- mean and median \(\Delta_M\);
- 2.5% and 97.5% quantiles;
- \(P(\Delta_M>0)\);
- break-even quantiles;
- intervention rankings;
- sensitivity indices.

Stop only after prespecified tolerances hold over at least three successive doublings, for example:

\[
|\hat p_N-\hat p_{N/2}|<\delta_p,\quad
\max_q|\hat Q_{q,N}-\hat Q_{q,N/2}|<\delta_Q,
\]

and replicate/batch Monte Carlo standard errors are below their thresholds. Report the tolerance values and convergence plots. Do not justify 1,000 or 10,000 runs by convention. Sampling-convergence literature supports replicated designs and outcome-specific convergence checks; comparative probabilistic-LCA literature warns that excessive simulation precision cannot repair poorly evidenced input distributions and recommends relating run count to input information.
Sources: https://doi.org/10.1016/j.ress.2012.08.003 ; https://doi.org/10.1007/s11367-019-01698-4 ; https://doi.org/10.2166/wst.2011.453

For estimated benefit probability \(\hat p\), report a binomial Wilson interval or replicate-based interval, not only \(\hat p\). For quantiles, use replicate/batch variability or bootstrap over simulation batches.

### Sensitivity hierarchy

1. **Exact break-even algebra** first.
2. **One-way threshold maps** for width compensation, failure/replacement, acceptance, conversion yield, pack utilization, and container burden.
3. **Morris screening** with scaled/non-dimensional elementary effects when parameter count is large.
4. **Sobol first/total-order indices** only for a stable probabilistic model with defensible independent inputs or an explicitly dependence-aware method.

The Morris literature warns that unscaled elementary effects can produce unit-dependent rankings. Sobol indices quantify variance contributions but require adequate convergence and careful estimators.
Sources: https://doi.org/10.1016/S1570-7946(09)70154-3 ; https://doi.org/10.1016/j.cpc.2009.09.018 ; https://doi.org/10.1016/j.envsoft.2021.105167

### Mandatory adversarial stress tests

- strongest plausible compensation;
- zero compensation;
- conservative functional minimum;
- low acceptance/high rejection;
- perforation tearing and conversion-yield penalty;
- unchanged toilet-paper package;
- zero avoided transport trips;
- mass- and volume-constrained logistics;
- high straw replacement and residual-liquid failure;
- container redesign burden larger than straw saving;
- alternative functional units;
- coefficient/geography/end-of-life alternatives;
- PFAS section entirely removed;
- all uncertain coefficients set jointly against the hypothesis.

Classify each design-region cell as:

\[
\text{ROBUST BENEFIT if }\sup_{\theta\in\Theta_{\text{stress}}}R_M<1;
\]
\[
\text{CONDITIONAL BENEFIT if }\inf R_M<1\le\sup R_M;
\]
\[
\text{NO BENEFIT/HARM if }\inf_{\theta\in\Theta_{\text{stress}}}R_M\ge1.
\]

## 9. Material substitution comparator and PFAS

Use a \(2\times2\) factorial comparison only when the same functional unit and system boundary can be supported:

| | Current material | Substitute material |
|---|---:|---:|
| Current geometry | A | C |
| Optimized geometry | B | D |

Estimate geometry effect \(B-A\), substitution effect \(C-A\), combined effect \(D-A\), and interaction:

\[
I=(D-C)-(B-A).
\]

This prevents the manuscript from constructing a weak substitute-material comparator while ignoring geometry–material interactions.

Published straw LCAs do not support a universal paper-versus-plastic ranking. The studies use different geographies, systems, and impact framings: a South African five-material comparison, a US analysis explicitly including marine-litter trade-offs, and a Malaysia gate-to-grave/process-simulation comparison that favored PLA over paper for its selected GWP, acidification, and eutrophication indicators. Therefore, any ranking must state material specification, geography, energy mix, end-of-life, functional performance/replacement, and included impact categories.
Sources: https://doi.org/10.1007/s11367-020-01786-w ; https://doi.org/10.1016/j.scitotenv.2022.153016 ; https://doi.org/10.3390/pr9061007

PFAS must remain secondary. A 2023 Belgian-market study tested 39 brands across five straw materials with targeted and suspect screening and found PFAS more frequently in plant-based materials, but it does not establish that all paper straws contain PFAS or that results generalize globally. FDA reports that PFAS grease-proofing substances for paper food packaging were phased out of the US market and related food-contact notifications became ineffective, which further makes country/year specificity essential. Delete-PFAS stress testing is mandatory: the main geometry conclusions must remain unchanged when PFAS discussion is removed.
Sources: https://doi.org/10.1080/19440049.2023.2240908 ; https://www.fda.gov/food/process-contaminants-food/market-phase-out-grease-proofing-substances-containing-pfas ; https://www.fda.gov/food/process-contaminants-food/authorized-uses-pfas-food-contact-applications

## 10. Hostile JCLP editor/reviewer assessment

### Most urgent: plausible desk rejection

1. **“Three trivial product ideas, not a transdisciplinary cleaner-production contribution.”**
   Fatality: desk reject. Fix effect: very high. Feasibility: possible with current modelling.
   Required fix: lead with the general constrained optimization, task-discretization, behavioral break-even, and integer-logistics framework; use the products as deliberately heterogeneous demonstrations; show which results generalize and which do not. JCLP explicitly prioritizes work beyond an isolated application.
   Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news ; https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news/policy-statement-for-rejecting-articles-before-peer-review

2. **“Novelty is false: smaller products, lightweighting, packaging optimization, and partitionable rolls already exist.”**
   Fatality: desk reject. Fix effect: very high. Feasibility: possible by reframing.
   Required fix: remove “first,” “novel product,” and invention language; cite material-efficiency/ecodesign literature and patents; claim novelty only for the integrated quantitative framework and empirical/scenario demonstration if the final literature review supports it.
   Sources: https://doi.org/10.1016/j.resconrec.2010.11.002 ; https://doi.org/10.1016/j.procir.2023.02.062 ; https://doi.org/10.1002/pts.887 ; https://patents.google.com/patent/US453003A/en ; https://patents.google.com/patent/US20160345786A1/en

3. **“The paper asserts environmental benefit but measures only area or mass.”**
   Fatality: desk reject/major revision. Fix effect: very high. Feasibility: fully fixable by claim discipline; broader environmental result needs data.
   Required fix: make material/FU primary; call broader work scenario-based or LCA-informed; report affected stages and burden shifts; reserve environmental-impact claims for explicit coefficients and boundaries.
   Sources: https://www.iso.org/standard/37456.html ; https://www.iso.org/standard/38498.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

4. **“Functional equivalence is assumed, especially for hygiene adequacy and straw usability.”**
   Fatality: major revision or rejection. Fix effect: very high. Feasibility: only partly fixable without experiments.
   Required fix: define performance FUs and adequacy/failure rules; present scenario results as conditional; identify human-use validation as necessary before behavioral-feasibility claims.
   Sources: https://doi.org/10.1111/jiec.13218 ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

5. **“Center perforation is patented/prior art and manufacturing feasibility is hand-waved.”**
   Fatality: desk reject if presented as invention; major revision otherwise. Fix effect: high.
   Required fix: include prior-art table, explicitly disclaim patentability/FTO, model conversion yield and tear errors, and cite engineering evidence on perforation performance.
   Sources: https://patents.google.com/patent/US453003A/en ; https://patents.google.com/patent/US20160345786A1/en ; https://doi.org/10.3390/eng4010005

### High priority: likely major-review objections

6. **Straw-man comparators.** Comparing optimized current material with an unusually heavy/long substitute, or using “one straw” despite unequal failure, is invalid. Use observed configurations, performance FUs, and the full \(2\times2\) geometry/material design.
Sources: https://doi.org/10.1111/jiec.13218 ; https://doi.org/10.1007/s11367-020-01786-w ; https://doi.org/10.1016/j.scitotenv.2022.153016

7. **Arbitrary simulation distributions masquerading as evidence.** Hypothetical task mixtures and functional minima cannot yield empirical confidence intervals. Call them scenario intervals, publish the full parameter grid/priors, and separate epistemic scenarios from sampling variability.
Sources: https://doi.org/10.1007/s11367-019-01698-4 ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

8. **False precision from huge Monte Carlo runs.** More draws narrow numerical error but do not validate unsupported inputs. Use convergence diagnostics and evidence-limited interpretation.
Sources: https://doi.org/10.1007/s11367-019-01698-4 ; https://doi.org/10.1016/j.ress.2012.08.003

9. **Transport savings inferred directly from mass savings.** Toilet tissue is often volume-sensitive; shorter straws may not change carton count; integer thresholds can produce no trip reduction. Report unchanged-packaging and no-avoided-trip cases.
Sources: https://doi.org/10.1002/pts.887 ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

10. **Rebound treated as a decorative sensitivity.** Compensation, rejection, repeat use, and replacement are central mechanisms and exact break-even thresholds should appear in Methods/Results, not only limitations.
Sources: https://doi.org/10.1017/dsj.2024.32 ; https://doi.org/10.1016/j.ecolecon.2019.106544

11. **Container redesign burden omitted.** A shorter straw achieved by port relocation, lid change, or package change is not a free intervention. Include all changed components/stages.
Sources: https://www.iso.org/standard/37456.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

12. **Patent status reported as legal conclusion.** Google Patents itself warns that its legal-status/assignee fields are assumptions and not legal conclusions. Report identifiers, dates, applicant/assignee as displayed, concept, and source only; no FTO conclusion.
Sources: https://patents.google.com/patent/US453003A/en ; https://patents.google.com/patent/US20160345786A1/en

### Medium priority

13. **GUE/GEF presented as established terminology.** Label as proposed operational metrics and map them against material efficiency, lightweighting, dematerialization, eco-design, source reduction, and sufficiency.
Sources: https://doi.org/10.1016/j.resconrec.2010.11.002 ; https://www.epa.gov/p2 ; https://doi.org/10.1080/09544828.2023.2261094

14. **PFAS distracts from the geometry thesis.** Keep one bounded paragraph/table and a removal sensitivity; avoid universal statements.
Sources: https://doi.org/10.1080/19440049.2023.2240908 ; https://www.fda.gov/food/process-contaminants-food/market-phase-out-grease-proofing-substances-containing-pfas

15. **Reference overload.** The current JCLP guide caps contributions at 50 references, so prioritize official standards, decisive reviews, closest methods, direct case evidence, and patents; move broad search documentation to the supplement/data registry without padding the manuscript bibliography.
Source: https://www.sciencedirect.com/journal/journal-of-cleaner-production/publish/guide-for-authors

### Five-domain adversarial audit

| Review domain | Strongest criticism | Severity | Scientific improvement if fixed | Feasibility now |
|---|---|---:|---:|---:|
| manuscript | contribution reads as three product ideas rather than one cleaner-production theory/test | desk-reject | very high | high through restructuring |
| statistical design | unsupported task/rebound distributions could be mistaken for empirical uncertainty | major/reject | very high | high if relabeled as scenarios; empirical resolution deferred |
| figures/tables | attractive savings plots may hide the \(R=1\) boundary, adverse scenarios, integer discontinuities, and provenance | major | high | high |
| reproducibility | every coefficient, distribution, seed, packing rule, and generated value must trace to raw source/config/code | major | very high | high if implemented before drafting results |
| claim strength | “environmental reduction,” “functional equivalence,” and novelty could exceed mass-flow scenario evidence | desk-reject/major | very high | high through disciplined wording; stronger claims deferred |

The manuscript domain is the likely editor gate; claim strength and statistical design are the likely reviewer gates. Figures should emphasize break-even and failure regions, not only point savings. Reproducibility requires a source/assumption registry and generated manuscript-value table.
Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news/policy-statement-for-rejecting-articles-before-peer-review ; https://www.iso.org/standard/37456.html ; https://doi.org/10.1007/s11367-019-01698-4

### Eight explicit JCLP desk-rejection gates

1. **More than product-specific optimization?** Not yet demonstrated by examples alone; pass only if one formal framework predicts all cases and the taxonomy is bounded.
2. **General cleaner-production framework quantitatively demonstrated?** Potentially; pass if identical estimands, constraints, and falsification logic are used across cases.
3. **Environmental significance supported?** Not for broad impact claims without inventory/coefficient evidence; material-throughput significance can be supported.
4. **Rebound and functional equivalence handled?** Mathematically yes; empirically unresolved until behavioral/bench validation.
5. **Adequate systemic/lifecycle thinking?** Conditional; include container, package, conversion, transport, use failure, and end-of-life burden shifts.
6. **Novelty established against ecodesign/material efficiency?** Product concepts are not new; integrated decision-boundary framework may be, subject to final literature review.
7. **Sufficiently transdisciplinary?** Potentially if engineering geometry, behavior, manufacturing, logistics, and environmental assessment are genuinely integrated rather than listed.
8. **Would a narrower journal fit better?** Yes if the final paper remains engineering optimization without general/systemic evidence; JCLP is defensible only after the preceding gates pass.

These gate judgments follow JCLP’s stated scope/desk policy and the verified adjacent literature/prior art.
Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news ; https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news/policy-statement-for-rejecting-articles-before-peer-review ; https://doi.org/10.1016/j.resconrec.2010.11.002 ; https://patents.google.com/patent/US20160345786A1/en

## 11. Minimum evidence for defensible conclusions

### Conclusions supportable without a human trial

- Exact geometric mass relations and break-even conditions, clearly labeled derived.
- Engineering lower bounds from verified product dimensions and measured mass/basis weight.
- Scenario regions showing where benefit survives specified compensation/failure.
- Integer packing outcomes for verified package/carton/pallet dimensions.
- Conditional, source-specific environmental calculations with explicit coefficients and boundary.

These remain scenario/model conclusions, not observed user savings. ISO/PEF-style transparency and performance-FU discipline are required.
Sources: https://www.iso.org/standard/37456.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230 ; https://doi.org/10.1111/jiec.13218

### Evidence required before behavioral-feasibility claims

**Toilet paper:** randomized crossover data with mass or area per event, pull length, sheets/half-units, adequacy, repeats, acceptability, folding, and rejection; enough width conditions to estimate \(\varepsilon_{LW}\), with privacy-preserving collection.
Rationale sources: https://doi.org/10.1111/jiec.13218 ; https://doi.org/10.1017/dsj.2024.32

**Center perforation:** converter/bench evidence for roll integrity, cross- versus machine-direction tear strength, accidental tearing, converting yield/speed, dispenser compatibility, and task-specific user selection.
Rationale sources: https://patents.google.com/patent/US20160345786A1/en ; https://doi.org/10.3390/eng4010005

**Straws:** measured container CAD/dimensions, actual straw dimensions/mass, residual-liquid tests across orientations, insertion/puncture force, protrusion and reach, leakage, bend/kink/buckling, serving success, and replacement.
Rationale sources: https://doi.org/10.1111/jiec.13218 ; https://patents.google.com/patent/US6431434B1/en ; https://doi.org/10.1017/CBO9780511624278.017

### Future validation protocols—not present results

**Toilet-paper randomized crossover.** Randomize sequence across standard width, narrower width, center-perforated standard width, and, if manufacturable, narrower center-perforated width. Use participant blocking and washout/familiarization where carryover is plausible. Primary endpoint: total dry mass or calibrated area consumed per successful private event. Secondary endpoints: longitudinal length, full/half units, adequacy, repeats, folding strategy, tear failures, rejection, and acceptability. Estimate a mixed-effects log-response model for \(d\ln L_{\mathrm{consumed}}/d\ln W\), with participant random effects and prespecified period/sequence terms. Use privacy-preserving pre/post roll weight or instrumented dispensing rather than direct observation. This protocol is required to turn scenario compensation into an empirical elasticity and must not be described as completed.
Rationale sources: https://doi.org/10.1111/jiec.13218 ; https://doi.org/10.1017/dsj.2024.32

**Straw bench/user validation.** Stratify representative containers by height, cross-section, port location, and beverage viscosity. Randomize candidate lengths within container. Measure residual volume under specified orientations, accessible depth, protrusion, insertion/puncture force, leakage, buckling/kink, serving completion, opened replacements, and acceptability. Predefine noninferiority margins for residual liquid and usability before testing. This protocol is required to convert geometric feasibility into functional equivalence and must not be described as completed.
Rationale sources: https://doi.org/10.1111/jiec.13218 ; https://patents.google.com/patent/US6431434B1/en ; https://doi.org/10.1017/CBO9780511624278.017

### Evidence required before broad lifecycle superiority claims

Inventory for every affected component/stage; comparable functional performance; geography-specific electricity/material/end-of-life data; package/logistics changes; uncertainty/sensitivity; and, for public comparative claims, appropriate critical review/verification.
Sources: https://www.iso.org/standard/37456.html ; https://www.iso.org/standard/38498.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

## 12. Falsification rules to pre-register

The central proposition is falsified for a case if, under the prespecified feasible design set and evidence-supported uncertainty set:

1. no design has \(P(\Delta_M>0)\) above the prespecified evidentiary threshold;
2. any material saving requires functional inadequacy or acceptance below threshold;
3. compensation/replacement exceeds the exact break-even boundary;
4. manufacturing or container/package burdens erase the material benefit;
5. integer logistics produces no meaningful density/trip benefit where logistics is a claimed contribution;
6. the conclusion reverses under equally credible coefficients/boundaries;
7. performance equivalence cannot be defined or tested.

Negative or conditional findings should remain in title/abstract/conclusion scope. This aligns with JCLP’s stated emphasis on robust, relevant, novel work and with ISO/PEF limitation reporting.
Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news ; https://www.iso.org/standard/37456.html ; https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230

## 13. Recommended main-result structure

1. **Figure 1:** general constrained FGO framework and evidence states.
2. **Figure 2:** exact toilet width and half-unit geometry, with functional-topology constraints.
3. **Figure 3:** width ratio vs compensation/repeat surface with exact \(R_M=1\) contour.
4. **Figure 4:** measured container–straw geometry and feasible region, not decorative 3-D.
5. **Figure 5:** scenario distributions plus convergence inset; distinguish numerical interval from evidence uncertainty.
6. **Figure 6:** robust/conditional/no-benefit failure map and generalized taxonomy.

The manuscript must cite every figure/table in first-appearance order and move parameter provenance, full task-simplex results, packing layouts, convergence, and global sensitivity to supplementary material. JCLP’s current guide governs final submission mechanics and limits.
Source: https://www.sciencedirect.com/journal/journal-of-cleaner-production/publish/guide-for-authors

## 14. Bottom line

The strongest legitimate reason for JCLP rejection is: **the study may still be a sophisticated calculation around three familiar product-design ideas, with hypothetical functional demand and insufficient lifecycle evidence, rather than a validated general cleaner-production contribution.**

The strongest fix available without a human trial or full LCA is to make the paper explicitly about **decision boundaries** rather than claimed realized savings: exact equations; task/topology-aware functional units; observed-versus-assumed parameter separation; prior-art candor; conversion and container burden; integer logistics; convergence-controlled uncertainty; and aggressive failure-region reporting. Even after these fixes, “behaviorally feasible savings” and broad “environmental superiority” must remain unresolved until validation data and lifecycle inventories exist.
Sources: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news ; https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news/policy-statement-for-rejecting-articles-before-peer-review ; https://www.iso.org/standard/37456.html ; https://doi.org/10.1111/jiec.13218

## Sources

All accessed 2026-09-24.

1. JCLP Guide for Authors: https://www.sciencedirect.com/journal/journal-of-cleaner-production/publish/guide-for-authors
2. JCLP news/editorial positioning: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news
3. JCLP desk-rejection policy: https://www.sciencedirect.com/journal/journal-of-cleaner-production/about/news/policy-statement-for-rejecting-articles-before-peer-review
4. ISO 14040: https://www.iso.org/standard/37456.html
5. ISO 14044: https://www.iso.org/standard/38498.html
6. EU Product Environmental Footprint recommendation/method: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02021H2279-20211230
7. Functional units in comparative LCA: https://doi.org/10.1111/jiec.13218
8. Material efficiency white paper: https://doi.org/10.1016/j.resconrec.2010.11.002
9. Ecodesign/topology optimization: https://doi.org/10.1016/j.procir.2023.02.062
10. Design/process/material eco-selection: https://doi.org/10.1016/j.cesys.2023.100114
11. Ecodesign systematic review: https://doi.org/10.1080/09544828.2023.2261094
12. Sustainable packaging design: https://doi.org/10.1002/pts.887
13. Reboundless design: https://doi.org/10.1017/dsj.2024.32
14. Material-efficiency rebound: https://doi.org/10.1016/j.ecolecon.2019.106544
15. Monte Carlo runs in comparative probabilistic LCA: https://doi.org/10.1007/s11367-019-01698-4
16. Monte Carlo sampling efficiency/convergence: https://doi.org/10.1016/j.ress.2012.08.003
17. LHS Monte Carlo convergence: https://doi.org/10.2166/wst.2011.453
18. Scaled Morris effects: https://doi.org/10.1016/S1570-7946(09)70154-3
19. Sobol design/total-index estimator: https://doi.org/10.1016/j.cpc.2009.09.018
20. Sobol estimator comparison: https://doi.org/10.1016/j.envsoft.2021.105167
21. US453003A: https://patents.google.com/patent/US453003A/en
22. WO2003026472A1: https://patents.google.com/patent/WO2003026472A1/en
23. US20160345786A1: https://patents.google.com/patent/US20160345786A1/en
24. US9918595B2: https://patents.google.com/patent/US9918595B2/en
25. Toilet-tissue perforation optimization: https://doi.org/10.3390/eng4010005
26. Integrated beverage carton/straw patent: https://patents.google.com/patent/US6431434B1/en
27. Milk-carton/straw patent: https://patents.google.com/patent/US3215329A/en
28. Thin-tube Brazier effect: https://doi.org/10.1017/CBO9780511624278.017
29. South Africa straw LCA: https://doi.org/10.1007/s11367-020-01786-w
30. US straw LCA: https://doi.org/10.1016/j.scitotenv.2022.153016
31. Malaysia PLA/paper straw assessment: https://doi.org/10.3390/pr9061007
32. Belgian PFAS straw study: https://doi.org/10.1080/19440049.2023.2240908
33. FDA PFAS food-packaging phase-out: https://www.fda.gov/food/process-contaminants-food/market-phase-out-grease-proofing-substances-containing-pfas
34. FDA authorized PFAS food-contact uses: https://www.fda.gov/food/process-contaminants-food/authorized-uses-pfas-food-contact-applications
35. US EPA pollution prevention/source reduction: https://www.epa.gov/p2
