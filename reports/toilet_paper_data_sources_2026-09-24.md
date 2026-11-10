# Toilet-paper dimensional, compatibility, standards, and consumption sources

**Access date for all web sources:** 2026-09-24

**Scope:** public or persistently capturable sources relevant to toilet-paper width, sheet length, roll length/count, ply, basis weight/grammage, mass, package dimensions, dispenser compatibility, standards, aggregate consumption, and width-related compensation.

**Machine-readable registry:** `data/processed/source_registry.csv` (45 candidates; URLs, variables, observation units, grades, reuse notes, capture status, snapshot paths, sizes, and SHA-256 checksums).

**Raw acquisition ledger:** `data/raw/toilet_paper_sources/acquisition_ledger_2026-09-24.tsv`.

## Bottom line

1. Public manufacturer records provide strong **product-level** dimensional observations across the US, Ireland/UK, Australia, Japan, and continental Europe, but they are not probability samples and must not be represented as national market distributions. Representative primary records include Tork US 1102910, Tork Ireland 101408, Tork Australia 2170329, Elleair Japanese products, and Katrin 169505/104834 ([Tork US](https://www.torkglobal.com/us/en/product/toilet-paper/refills/mid-size-rolls/1102910); [Tork Ireland](https://www.torkglobal.com/ie/en/product/toilet-paper/refills/conventional-toilet-paper/101408); [Tork Australia](https://www.torkglobal.com/au/en/product/toilet-paper/refills/conventional-rolls/2170329); [Elleair](https://www.elleair.jp/product/detail/toilet_single.html); [Katrin 169505](https://www.metsagroup.com/katrin/products/toilet-paper/toilet-paper-roll/169505-katrin-toilet-paper-roll-250-sheets-2-ply/); [Katrin 104834](https://www.metsagroup.com/contentassets/c6bc3da19e63405682fe98dcbb8d174e/104834_katrin_en.pdf); accessed 2026-09-24).
2. Standards and procurement specifications establish test methods, minimums, allowed formats, or installation constraints; they do **not** establish one universal toilet-paper width. The clearest captured dimensional procurement source is US A-A-59594A, while the official Japanese and Chinese catalogs establish standard identity/status but not a globally representative product dimension ([A-A-59594A](https://quicksearch.dla.mil/WMX/Default.aspx?token=5710999); [JSA 2026 catalog](https://webdesk.jsa.or.jp/link/lib/jis2026/index/319176.pdf); [China National Digital Standards Library](https://www.ndls.org.cn/standard/detail/a459a2fe870c292f3ce60ec17c83398d); accessed 2026-09-24).
3. One captured source directly manipulated width: Table 2 of US Patent 6,458,450 B1 compared 4.5, 5.75, and 7.0 inch two-ply sheets within each of three total basis-weight groups. It is limited evidence because the outcome was the amount that two focus groups of eight women each **believed** necessary for post-urinary drying, not measured household consumption ([US6458450B1](https://patents.google.com/patent/US6458450B1/en), accessed 2026-09-24).
4. The patent contrasts do not support a universal “narrower always saves” claim. Reproducible calculations from the disclosed Table 2 produce material-saving fractions from **−20.0% to +18.4%** across the nine within-basis-weight pairwise contrasts; five contrasts cross the no-saving boundary and four retain positive calculated material savings. These are calculations from rounded patent table entries, not population estimates (`data/processed/pg_patent_table2_observed.csv`; `data/processed/pg_patent_table2_width_contrasts.csv`; source [US6458450B1](https://patents.google.com/patent/US6458450B1/en), accessed 2026-09-24).
5. No peer-reviewed controlled field estimate of real-world, width-only consumption elasticity \( \epsilon_{LW} \) was located in the captured set. The defensible conclusion is: **limited direct focus-group width evidence exists; a robust controlled real-world width-only elasticity estimate remains unresolved.**

## Evidence grading

- **A1:** primary official government/standards metadata or directly captured manufacturer specification with clear identity and usable variables.
- **A2:** primary official/manufacturer source with a material limitation: blocked local capture, survey/report limitations, relative rather than absolute dimensions, or metadata rather than full clauses.
- **B1:** peer-reviewed empirical or engineering study with identifiable methods and observation unit.
- **B2:** retailer or industry-association evidence with useful original data but weaker independence/method reporting.
- **C1:** patent empirical disclosure, retailer measurement, secondary standard rendering, consumer journalism, or supplier-hosted technical sheet; useful only with explicit limitations.
- **D:** failed, incomplete, or unverified lead that should not support a substantive claim.

Grades describe fitness for the stated variable and question, not overall institutional prestige. For example, ISO metadata are authoritative for the existence/scope of a test method but do not provide a product-width requirement.

## Representative dimensional and logistics observations

These are **observations for named products**, not national averages.

| Market/source | Verified variables and values | Observation unit | Grade |
|---|---|---|---|
| US, Tork 1102910 | 625 ft roll length; 3.94 in roll width; 5.40 in roll diameter; 1.70 in core inner diameter; 2,000 sheets; 3.75 in sheet length; 1 ply | one refill SKU | A1 ([source](https://www.torkglobal.com/us/en/product/toilet-paper/refills/mid-size-rolls/1102910), accessed 2026-09-24) |
| Ireland/EU, Tork 101408 | 19.55 m roll length; 10.10 cm roll width; 11 cm roll diameter; 5.10 cm core inner diameter; 11.50 cm sheet length; 3 ply | one refill SKU | A1 ([source](https://www.torkglobal.com/ie/en/product/toilet-paper/refills/conventional-toilet-paper/101408), accessed 2026-09-24) |
| Australia, Tork 2170329 | 85 m roll length; 10 cm width; 850 sheets; 10 cm sheet length; 1 ply | one refill SKU | A1 ([source](https://www.torkglobal.com/au/en/product/toilet-paper/refills/conventional-rolls/2170329), accessed 2026-09-24) |
| Japan, Elleair single | 114 mm width; 55 m roll length; 12-roll package 342 × 204 × 204 mm; 18-roll package 342 × 313 × 204 mm | named manufacturer product/package variants | A1 ([source](https://www.elleair.jp/product/detail/toilet_single.html), accessed 2026-09-24) |
| Japan, Elleair double | 114 mm width; 30 m two-ply roll length; 12-roll package 342 × 204 × 204 mm | named manufacturer product/package | A1 ([source](https://www.elleair.jp/product/detail/toilet_double.html), accessed 2026-09-24) |
| Japan, Nepia renewal | cited product changed from 114 mm to 109 mm width while retaining a two-ply, 50 m specification; manufacturer also reports a prior-user survey of 200 people | renewed product and pooled manufacturer survey | A2 ([source](https://www.nepia.co.jp/company/news_release/news20240326.pdf), accessed 2026-09-24) |
| Continental Europe, Katrin 169505 | 110 mm sheet length; 94.5 mm sheet width; 250 sheets; 27.5 m roll length; 105 mm roll diameter; 43 mm core; 2 ply; 94.5 × 195 × 400 mm consumer pack; 0.691 kg gross; 8 rolls/pack; GTIN 4004231169501 | one refill SKU and consumer pack | A1 ([source](https://www.metsagroup.com/katrin/products/toilet-paper/toilet-paper-roll/169505-katrin-toilet-paper-roll-250-sheets-2-ply/), accessed 2026-09-24) |
| Continental Europe, Katrin 104834 | 120 mm sheet length; 97 mm sheet width; 400 sheets; 48 m roll length; 118 mm roll diameter; 39.5 mm core; 2 ply; 194 mm package height; 0.933 kg gross; 6 rolls/pack | one refill SKU and consumer pack | A1 ([source](https://www.metsagroup.com/contentassets/c6bc3da19e63405682fe98dcbb8d174e/104834_katrin_en.pdf), accessed 2026-09-24) |
| Continental Europe, Serla P17148 | 153 sheets/roll; sheet 125 ± 2 mm × 101 ± 1 mm; 115 mm roll diameter; 46 mm core; 19.125 m roll length; 3 ply; 51.9 ± 3 g/m² all-layer grammage; 2.406 kg net-net, 2.538 kg net, 2.573 kg gross; package 430 × 220 × 303 mm | one product code and package | C1 because the captured file is supplier-hosted | ([source](https://easystar.ee/wp-content/uploads/2024/05/P17148.pdf), accessed 2026-09-24) |
| US, Charmin Forever Roll | 1,700 two-ply sheets/roll; 17.0 m² (185 ft²) total area/roll; sheet 9.9 × 10.1 cm; listed roll mass 2 lb; two-roll starter kit includes a dedicated freestanding holder | one special-format product/holder kit | A1 ([source](https://shop.charmin.com/forever-roll-starter-kit-holder-stand-included-2-roll/), accessed 2026-09-24) |

The Charmin page also displays a 12 in roll dimension. Because the same record separately gives sheet dimensions, this value must not be imported as tissue sheet width without checking the page’s dimension label ([source](https://shop.charmin.com/forever-roll-starter-kit-holder-stand-included-2-roll/), accessed 2026-09-24).

## Compatibility and dispenser constraints

- Tork refill records explicitly identify dispenser systems, so compatibility can be represented as a product–system relationship rather than inferred from width alone ([Tork US 1102910](https://www.torkglobal.com/us/en/product/toilet-paper/refills/mid-size-rolls/1102910); [Tork Ireland 101408](https://www.torkglobal.com/ie/en/product/toilet-paper/refills/conventional-toilet-paper/101408); accessed 2026-09-24).
- Tork GB dispenser 557000 supplies dispenser dimensions of 15.80 × 15.30 × 28.60 cm plus delivery/package specifications and weights; this supports explicit packaging and compatibility modelling for that system ([source](https://www.torkglobal.com/gb/en/product/toilet-paper/dispensers/conventional-roll-dispensers/557000), accessed 2026-09-24).
- Katrin 169505 lists compatible dispensers alongside refill dimensions; these links should be preserved when testing whether a width or diameter change remains compatible ([source](https://www.metsagroup.com/katrin/products/toilet-paper/toilet-paper-roll/169505-katrin-toilet-paper-roll-250-sheets-2-ply/), accessed 2026-09-24).
- Charmin Forever Roll is sold with a specialized holder, demonstrating that nonstandard roll geometry can shift burden into a new durable compatibility component; the holder must be inside the system boundary if that case is modelled ([source](https://shop.charmin.com/forever-roll-starter-kit-holder-stand-included-2-roll/), accessed 2026-09-24).
- The US Access Board’s 2010 ADA Standards section 604.7 regulates dispenser location and states that dispensers must allow continuous paper flow rather than controlling tissue width; it is an installation/dispensing constraint, not evidence for a minimum sheet width ([source](https://www.access-board.gov/ada/chapter/ch06/), accessed 2026-09-24).

## Standards, procurement, and environmental criteria

### United States

The captured A-A-59594A institutional procurement specification, dated 2011-06-01, permits roll one- or two-ply tissue and perforated or nonperforated classes. Listed perforated sheet formats include 4.0 × 4.0, 4.5 × 4.0, and 4.5 × 4.5 in; nonperforated formats include 750, 1,000, and 2,000 ft lengths at 3.5 in width. Minimum grammage is 14.7 g/m² for one ply and 27.7 g/m² for two ply. This is procurement evidence for institutional formats, not a universal US consumer standard ([official DLA QuickSearch record](https://quicksearch.dla.mil/WMX/Default.aspx?token=5710999), accessed 2026-09-24).

US EPA Comprehensive Procurement Guideline guidance provides recovered-fiber and postconsumer-fiber recommendations for bathroom tissue. It supports a recycled-content comparator but supplies no width-consumption response and should not be used as dimensional evidence ([source](https://www.epa.gov/smm/comprehensive-procurement-guideline-cpg-program), accessed 2026-09-24).

### Japan

The Japan Standards Association’s 2026 catalog lists JIS P 4501:1993 and Amendment 1:2006, confirming the identifier/version in the current catalog ([source](https://webdesk.jsa.or.jp/link/lib/jis2026/index/319176.pdf), accessed 2026-09-24). A secondary rendering exposes roll lengths 27.5, 32.5, 55, 65, 75, and 100 m and a maximum wound-roll diameter of 120 mm, but the dimensional table is incompletely rendered; those clauses remain provisional until checked against licensed official text ([secondary rendering](https://kikakurui.com/p/P4501-2006-01.html), accessed 2026-09-24). The standard is a product specification, not evidence of how much users consume at different widths.

### China

The official National Digital Standards Library identifies GB/T 20810-2018 and its English version as current, published 2018-06-07 and implemented 2019-07-01 ([source](https://www.ndls.org.cn/standard/detail/a459a2fe870c292f3ce60ec17c83398d), accessed 2026-09-24). The captured official page establishes identity and status, not all dimensional clauses. A commercial preview is retained only as secondary, nonredistributable clause-level support ([secondary preview](https://www.chinesestandard.net/PDF.aspx/GBT20810-2018), accessed 2026-09-24).

### India

The publicly downloadable mirror of IS 14661:1999 states 21 g/m² grammage, sheet width not less than 100 mm, and sheet area not less than 135 cm² ([source](https://law.resource.org/pub/in/bis/S02/is.14661.1999.pdf), accessed 2026-09-24). However, 2025 BIS-series records indicate restructuring/revision activity for IS 14661; therefore the 1999 text is classified as **legacy/provisional** and must not be called the current Indian requirement without official BIS confirmation.

### European Union

Commission Decision (EU) 2019/70 establishes EU Ecolabel criteria for tissue paper and tissue products; its criteria concern fiber sourcing, emissions, energy, hazardous substances, waste, and fitness for use, not a standard consumer roll width ([official text](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019D0070), accessed 2026-09-24). Commission Decision (EU) 2024/3179 extends the validity of the relevant criteria through 2028-12-31 ([official ELI record](https://eur-lex.europa.eu/eli/dec/2024/3179/oj/eng), accessed 2026-09-24). Direct automated captures of the EUR-Lex documents returned HTTP 202 with zero-byte bodies; the official URLs are verified, but complete local source bodies remain unresolved.

### International test methods

ISO 12625-4, -6, -8, and -12 concern tensile properties, grammage, water absorption, and perforated-line tensile strength/perforation efficiency respectively. They are appropriate measurement-method references but do not themselves establish one finished-product width or behavioral response ([ISO 12625-4](https://www.iso.org/standard/80328.html); [ISO 12625-6](https://www.iso.org/standard/66472.html); [ISO 12625-8](https://www.iso.org/standard/53425.html); [ISO 12625-12](https://www.iso.org/standard/83277.html); accessed 2026-09-24). ISO pages were blocked during local capture; only metadata and exact acquisition failures are retained.

## Consumption evidence that does not manipulate width

| Source | Observation and unit | Relevance and limitation |
|---|---|---|
| Fenner Hall audit | 507 students, seven-day collection; 21 g/day/resident, 7.4 kg/year/resident, and 3.7 tonnes/year for the community | Direct mass-throughput context, but no width variation and one residential setting ([DOI 10.22459/AURJ.05.2013.19](https://doi.org/10.22459/aurj.05.2013.19), accessed 2026-09-24) |
| Bangkok household study | survey of 300 families; approximately 9.75 rolls/month/household and approximately 2 rolls/month/person | Roll-count context; roll dimensions/quality and width were not experimentally controlled ([source](https://so04.tci-thaijo.org/index.php/kjss/article/view/243981), accessed 2026-09-24) |
| BMA bathroom diary | 48 UK residents, seven days, 404 toilet visits and 39 cleaning routines; women used toilet paper on 96% of visits and averaged 6.1 sheets/visit, while men used it on 64% and averaged 7.5 sheets/visit | Useful task-frequency/sheet-count context; association-sponsored, small sample, and no width manipulation ([source](https://bathroom-association.org.uk/wp-content/uploads/2024/05/BMA-Behind-the-Bathroom-Door-Research-Overview.pdf), accessed 2026-09-24) |
| Yuasa retailer measurement | approximately 200 employee observations and sex-specific reported lengths/use | Original measurements but retailer-origin, non-peer-reviewed, and no controlled width variation ([source](https://yuasakamiten.com/blogs/iseecolumn/toiletpaper-1roll-howmanydays), accessed 2026-09-24) |
| Hanyu et al. | 1,242 Japanese respondents; recycled-versus-virgin toilet-paper evaluations, purchasing, and recycling behavior | Relevant to acceptance/material preference, not consumption quantity under different widths ([DOI 10.1016/S0921-3449(00)00060-4](https://doi.org/10.1016/S0921-3449(00)00060-4), accessed 2026-09-24) |

None of these sources can identify \(d\ln L/d\ln W\). They should calibrate plausible use-event counts, identify heterogeneity, or motivate a validation design—not be converted into a width elasticity.

## Direct width-manipulation evidence

### US Patent 6,458,450 B1, Table 2

The patent reports two-ply samples at total basis weights of 28, 44, and 70 lb/3,000 ft² and widths of 4.5, 5.75, and 7.0 in. Within each basis-weight group, sheet length, softness, texture, and visual appearance were described as similar. Two groups of eight women pulled the quantity they believed necessary for post-urinary drying ([source](https://patents.google.com/patent/US6458450B1/en), accessed 2026-09-24).

Observed sheets/task:

| Total basis weight (lb/3,000 ft²) | 4.5 in | 5.75 in | 7.0 in |
|---:|---:|---:|---:|
| 28 | 3.1 | 2.6 | 1.8 |
| 44 | 2.6 | 2.0 | 1.6 |
| 70 | 1.9 | 1.8 | 1.5 |

The observation table is transcribed as `data/processed/pg_patent_table2_observed.csv`. `scripts/analyze_patent_width_compensation.py` computes all within-basis-weight pairwise contrasts in `data/processed/pg_patent_table2_width_contrasts.csv`.

Key reproducible implications:

- Longitudinal/sheet-count compensation is present in every disclosed narrow-versus-wide contrast, but its magnitude differs substantially by total basis weight ([source](https://patents.google.com/patent/US6458450B1/en), accessed 2026-09-24).
- Calculated finite \( \epsilon_{LW} \) spans approximately −1.87 to −0.22. The sign and magnitude cannot be treated as a population elasticity because the endpoint is perceived need, the sample is 16 focus-group participants, and no uncertainty estimates are reported.
- Calculated material-saving fractions span −20.0% to +18.4%; narrower sheets can therefore produce saving, near break-even, or increased supplied material in these disclosed contrasts.
- Because basis weight is held fixed only **within** each three-width block, the patent supports width contrasts conditional on each tested sheet construction; it does not establish a single width-only response transferable across products.

This patent is the strongest direct signal located, but grade C1 is appropriate. It should inform sensitivity bounds and falsification cases, not serve as a definitive prior distribution or causal field estimate.

### Related but non-identifying evidence

Nepia’s manufacturer release combines a width change with a product renewal and reports acceptance among 200 previous users. It does not report event-level sheet length, mass, or roll depletion under randomized widths, so it cannot identify compensation ([source](https://www.nepia.co.jp/company/news_release/news20240326.pdf), accessed 2026-09-24).

The BioResources perforation study tested eight commercial papers (two each at 2, 3, 4, and 5 ply), found a minimum service length of 125 mm in its setup, and reported perforation efficiency stabilizing above a 6 mm cut distance; its laboratory blade needed approximately 15% greater cut distance to match industrial perforation efficiency. This supports perforation engineering, not half-width user selection or consumption ([source](https://bioresources.cnr.ncsu.edu/wp-content/uploads/2021/11/BioRes_17_1_492_Vieira_VMCFC_Toilet_Paper_Perforation_Efficiency_19308.pdf), accessed 2026-09-24).

## Capture and reuse audit

- Registry candidates: **45**.
- Current local capture classifications after rebuilding the registry: 33 successful, 7 HTTP-403 failures, 3 zero-byte HTTP-202 captures, 1 HTTP-404 failed lead, and 1 successful nonempty Fenner file with a historical `200000` curl-status anomaly.
- The blocked records are Kimberly-Clark Scott, Tesco, the original DLA URL, and four ISO pages. The successful DLA QuickSearch source supersedes the blocked DLA acquisition for substantive use.
- The failed Quilton Double Length URL is retained as negative provenance and must not support a product claim; the successfully captured Quilton FAQ supports only its stated regular/double/triple categories, regular 180-sheet count, and pallet-packing explanation ([FAQ](https://www.quilton.com.au/pages/faqs), accessed 2026-09-24).
- Three EUR-Lex capture attempts are zero bytes and explicitly marked incomplete. Their official URLs may be cited, but the project must not claim the raw local corpus is complete.
- Manufacturer, retailer, supplier, association, ISO, JIS, and secondary-standard snapshots should not be redistributed publicly unless the applicable licence permits it. The registry records reusable citation facts separately from raw snapshots.

## Recommendations for the parent analysis

1. **Build dimensional scenarios from named product observations, not market-frequency claims.** Use the manufacturer records to define an observed range or deliberately stratified case set and label it nonrepresentative ([Tork](https://www.torkglobal.com/us/en/product/toilet-paper/refills/mid-size-rolls/1102910); [Elleair](https://www.elleair.jp/product/detail/toilet_single.html); [Katrin](https://www.metsagroup.com/katrin/products/toilet-paper/toilet-paper-roll/169505-katrin-toilet-paper-roll-250-sheets-2-ply/); accessed 2026-09-24).
2. **Keep standards as constraints.** A-A-59594A can parameterize institutional formats; JIS and GB/T establish jurisdiction-specific specifications/status; ISO standards define tests; none should be treated as observed household behavior ([DLA](https://quicksearch.dla.mil/WMX/Default.aspx?token=5710999); [JSA](https://webdesk.jsa.or.jp/link/lib/jis2026/index/319176.pdf); [GB/T catalog](https://www.ndls.org.cn/standard/detail/a459a2fe870c292f3ce60ec17c83398d); [ISO](https://www.iso.org/standard/83277.html); accessed 2026-09-24).
3. **Use the patent only as limited sensitivity-bound evidence.** Preserve each basis-weight block, the exact finite break-even calculation, and both benefit and harm contrasts; do not pool the nine rows into one empirical \( \epsilon_{LW} \) ([US6458450B1](https://patents.google.com/patent/US6458450B1/en), accessed 2026-09-24).
4. **Model compensation transparently as scenarios until stronger evidence exists.** The no-compensation case, the nine patent-conditional contrasts, exact break-even, and deliberately adverse compensation should all be shown. Label any distribution over compensation as `ASSUMED` unless directly derived from a validated study.
5. **Keep center-perforation behavior separate from perforation mechanics.** ISO 12625-12 and Vieira et al. support tear-line testing/engineering, but no captured source establishes the probability that a user selects one half-width or compensates with additional longitudinal length ([ISO 12625-12](https://www.iso.org/standard/83277.html); [Vieira et al.](https://bioresources.cnr.ncsu.edu/wp-content/uploads/2021/11/BioRes_17_1_492_Vieira_VMCFC_Toilet_Paper_Perforation_Efficiency_19308.pdf); accessed 2026-09-24).
6. **Model packaging and compatibility explicitly.** Use actual pack dimensions/weights and refill–dispenser relationships where available; compare unchanged packaging with re-optimized integer packing rather than multiplying material savings by an assumed transport factor ([Katrin 169505](https://www.metsagroup.com/katrin/products/toilet-paper/toilet-paper-roll/169505-katrin-toilet-paper-roll-250-sheets-2-ply/); [Tork 557000](https://www.torkglobal.com/gb/en/product/toilet-paper/dispensers/conventional-roll-dispensers/557000); accessed 2026-09-24).
7. **Do not convert material savings into environmental-impact savings without coefficients and boundaries.** EPA recovered-fiber guidance and EU Ecolabel criteria are relevant contextual comparators but do not supply a geometry-to-impact conversion ([US EPA](https://www.epa.gov/smm/comprehensive-procurement-guideline-cpg-program); [EU 2019/70](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019D0070); accessed 2026-09-24).
8. **Prioritize a randomized crossover validation study.** Measure roll mass/area depletion per adequately completed event, longitudinal length, sheets, folding, repeat/additional use, rejection, and acceptability under standard, narrow, and center-perforated variants. This is a recommended future protocol, not completed evidence.

## Unresolved items

- No robust controlled real-world width-only estimate of \( \epsilon_{LW} \) was located.
- No behavioral study of longitudinal center-perforation/half-width selection was located.
- The current official status and dimensional clauses of India’s restructured IS 14661:2025 series require direct BIS verification; the captured 1999 text is legacy evidence.
- Complete local bodies for the current EUR-Lex decisions and ISO pages remain unavailable from automated capture.
- Secondary JIS and GB/T renderings must not substitute for licensed official standard text when exact compliance clauses are material.
- Retailer/manufacturer pages may change; the acquisition ledger’s timestamped snapshots and SHA-256 values should be used for reproducibility, subject to nonredistribution constraints.
