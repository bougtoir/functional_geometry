# 01 — Closest Prior Study Full-Text Audit

Gate 1 of the Function Before Form endpoint-feasibility gate. Builds on `../function_before_form_gate/` (PR #799), which is preserved unchanged.

Verification levels: **FT** = full text read (legitimate OA copy); **FT-P** = OA full text available and searched for specific passages, not read end-to-end; **AB+S** = abstract plus publisher-displayed section snippets; **AB** = abstract only; **MD** = metadata only.

## 1. Mandatory study — Collado-Ruiz & Ostad-Ahmad-Ghorabi (2010)

Collado-Ruiz, D., Ostad-Ahmad-Ghorabi, H. (2010). Influence of environmental information on creativity. *Design Studies* 31(5), 479–498. https://doi.org/10.1016/j.destud.2010.06.005

### PRIMARY CLOSEST PRIOR STUDY — FULL TEXT VERIFIED (user-provided copy)

**Update.** The first pass could not obtain the full text. The routes tried are kept for the record:
- Unpaywall, OpenAlex and Semantic Scholar: closed, no OA copy.
- CORE: HTTP 403.
- RiuNet: HTTP 404.
- ScienceDirect (anonymous): abstract and snippets only.

The user then supplied the publisher PDF (20 pp.) through institutional access. It is stored local-only as `data/raw/fulltext/10.1016_j.destud.2010.06.005_user_provided.pdf` (ledger row `user_provided`, SHA-256 recorded) and was **read in full**. Page numbers below are journal pages.

### 1.1 Observed methods

| Item | Observation | Page |
|---|---|---|
| Participants | 56 students of a "Creativity engineering" course, TU Vienna. Mixed disciplines; 8.9% PhD, 37.5% master, 39.3% undergraduate | 486 |
| Task | "coming up with design ideas which would reduce the environmental impact of an office chair". The brief was uniform: "Attention was paid to brief participants uniformly" | 486 |
| Manipulation | 5 groups: A no information; B newspaper item; C internal e-mail on the previous model's impact distribution ("no numerical data"); D two-page LCA of a competitor's chair; E two-page LCA of own previous model. Two axes: *level of detail* and *specificity* (Fig. 1) | 483, 487 (Table 1) |
| Allocation | "The subjects where then divided into five groups". **Random assignment is not stated.** ("Randomly distributed" on p. 487 describes the spread of prior LCA familiarity, not allocation.) | 486–487 |
| Time | 15 min briefing → 45 min ideation → 15 min to document each idea on a standardised form (name, description, sketch). Information documents of "similar length"; group A had no reading time | 486–487 |
| Problem framing | Held constant: "the strict definition of the problem is one of the controlled parameters" | 485 |
| Outcome | Creativity per idea = participant self-evaluation (stickers for surprising / feasible / exciting; Van der Lugt equation) × authors' 1–5 rating of each participant's best idea. The authors' rating was reached by "individual evaluation and further discussion to reach a consensus". **No inter-rater statistic is reported** | 488 (Eq. 1–2, Table 2) |
| Unit of analysis | All 262 ideas (Kruskal–Wallis, Mann–Whitney); plus the best idea per participant and fluency | 487, 489–491 |
| Results | Groups differ (p = 0.002). The LCA groups (D+E) have lower creativity than all other combinations. Soft information (B, C) is not different from no information (p = 0.267) | 489–490 |

### 1.2 Answers to the ten questions

| # | Question | Answer | Basis |
|---|---|---|---|
| 1 | Experimentally manipulated environmental information? | **Yes**, 5 groups. Randomisation is **not stated** | 486–487 |
| 2 | Compared levels of design abstraction? | **No.** It manipulated the level of detail and the specificity of the *information*; the problem definition was held constant | 483, 485 |
| 3 | Material substitution vs functional redesign? | **No.** Material change appears only as motivation ("changing materials or reducing the product's weight", described as perceived conservative strategies) | 480 |
| 4 | Fixation / originality? | **Yes**, creativity (originality + feasibility via self-evaluation × author rating), interpreted as fixation | 488, 492 |
| 5 | Functional adequacy? | **Only as self-rated "feasible" stickers.** No functional-equivalence check | 485, 488 |
| 6 | Objective environmental performance? | **No. Explicitly excluded:** "no conclusions can be driven whether more or less creative ideas will lead to more or less environmentally benign solutions" | 488 |
| 7 | LCA as outcome? | **No.** LCA was only the *manipulation* (groups D, E) | 487 |
| 8 | Final selected concepts? | **No.** All ideas were analysed; the "best idea" was chosen by the participant's own stickers and rated for creativity only | 488 |
| 9 | Time, information, task controlled? | **Mostly.** Same brief and time; documents of similar length; group A gained reading time (authors argue the effect is secondary) | 487, 490 |
| 10 | Already tested the E3 hypothesis? | **No.** The authors list it as future work: "it is also a necessity to assess the influence of the proposed ideas in regard to occurring environmental impacts in the final product" | 494 |

**Interpretation.** The study establishes the *mechanism*: detailed LCA information depresses rated creativity. It explicitly does **not** measure the environmental consequence, and it names that as an open question (p. 494). E3 does not replicate it. E3 is the extension the authors called for: it varies framing level instead of information detail, and measures functional-unit impact plus functional adequacy of the selected concept instead of creativity.

### 1.3 Companion and follow-up papers

- **Collado-Ruiz, Bastante-Ceca, Capuz-Rizo, Pacheco-Blanco & Viñoles-Cebolla (2012).** "Researching the influence of environmental information on the ideation process and results". XVI CIIP, Valencia. User-provided, FT.
  - A project-foundation paper. It announces "Experiment 1" (≈120 designers, 2012), whose final results "will be assessed as to their novelty, their technical and market feasibility, and their sustainability potential" (PDF p. 5, proceedings p. 1934), and a follow-up "Experiment 2" (50 participants).
  - It also lists, as a variable to consider, "whether the environmental aspects are included in the brief, or given as independent information" (p. 1936).
  - **No published results of Experiment 1/2 were found:** no hit in the OpenAlex author record A5036721753 (11 works since 2011) or in a Crossref author query (both saved with ledger rows). This is a **residual prior-art risk.** An unindexed thesis or Spanish-language report could exist, and Scopus/WoS were not searched.
- **Collado-Ruiz & Ostad-Ahmad-Ghorabi (2011)**, ICoRD'11, doi:10.1007/978-0-85729-224-7_11. Abstract only. Three expert raters on the same 56-student idea set (creativity, feasibility, originality); no environmental outcome in the abstract.

## 2. Other closest studies revisited (focused on E3 contribution)

| Study | Level | Manipulation | Environmental endpoint | Bearing on E3 |
|---|---|---|---|---|
| Faludi, Yiu & Agogino 2020, *Design Science* 6:e22, doi:10.1017/dsj.2020.17 | FT (prior gate) | Three sustainable design methods (TNS, WSM, Biomimicry) in 23 professional workshops | None. Value was self-reported because objectively assessing vague early-stage ideas "was deemed too subjective and too highly uncertain" (PDF p. 10) | Names the endpoint problem E3 must solve; it does not solve it |
| Faludi, Ali, Srour & Mecanna 2019, ICED, doi:10.1017/dsi.2019.342 | FT | Same three methods; 1,115 Post-it ideas from 23 workshops | Ideas qualitatively *categorised and counted* by sustainability strategy; coders not present at the workshops | Shows that method choice changes the *kinds* of ideas, measured by category counts, not by environmental magnitude |
| Linsey et al. 2010, *JMD* 132(4):041003, doi:10.1115/1.4001110 | FT-limited (prior gate) | Example exposure plus defixation instructions (three arms) | None (fixation/novelty) | The three-arm fixation template already exists; E3 cannot claim the manipulation design as new |
| Devanathan et al. 2010, *JMD* 132(8):081004, doi:10.1115/1.4001890 | AB (prior gate) | None (method paper: Function Impact Matrix) | Function-level semi-quantitative impact | Function-level environmental assessment at the concept stage already exists. It supports feasibility of an E3 endpoint and weakens any claim that the endpoint is novel |
| Bohm et al. 2010, *JMD* 132(9), doi:10.1115/1.4002152 | AB | None (method) | Streamlined LCA of repository-generated virtual concepts, benchmarked against analogous real products | Direct methodological precedent for screening LCA of early concepts and for benchmark validation (see 05/08) |
| Kota & Chakrabarti 2010, *JMD* 132(9), doi:10.1115/1.4002163 | MD/AB | None (method) | Uncertainty of LCA during design | Precedent for treating early-LCA uncertainty explicitly |
| Ross, Ferrero & DuPont 2022, *JMD* 144(3):032001, doi:10.1115/1.4052513 | FT (user-provided) | Exp. 1: 98 third-year ME students, control / Telenko guidelines / GREEn Quiz ("separated into each respective group"; randomisation not stated), toaster redesign, 30 min (032001-5). Exp. 2: 24 graduate students (12 teams), pre/post, 48 h | Counts of "sustainable design decisions" (any word related to sustainability or the tools); 3 expert judges rated sustainability, detail, originality and feasibility on 1–5, averaged; **no inter-judge agreement reported**; no LCA (032001-6) | Information-structure manipulation with a rated sustainability outcome. It does not quantify impact, has no FE gate and does not single out a final concept. It does not eliminate E3. It does state that LCA in conceptual design "leads to substantial uncertainty" (032001-1) |
| Collado-Ruiz & Ostad-Ahmad-Ghorabi 2012 (online; vol. 17(1), p. 31), *JIE*, doi:10.1111/j.1530-9290.2012.00510.x | MD | None (method) | Estimating environmental behaviour without a full LCA | Same authors; supports feasibility of an early-stage estimate. Not read |

Design-fixation experiments (Jansson & Smith 1991; Linsey et al. 2010; Zahner et al. 2010; and Crilly 2015, FT) were covered in the prior gate. They establish that problem representation and examples shape idea features. **They do not measure environmental performance.** E3 cannot claim novelty on "framing causes fixation". It can claim novelty only on *the environmental consequence of framing, measured on a functional-unit basis for the selected concept*.

New close studies found in Gate 2 are audited in `02` and `03`: Liao & MacDonald 2021; Greeley et al. 2025; Ruiz-Pastor et al. 2020; Ross et al. 2022 (full text, row above); She & MacDonald 2013; Hu et al. 2021; Wasserbaur & Sakao 2020; Cardin et al. 2013.
