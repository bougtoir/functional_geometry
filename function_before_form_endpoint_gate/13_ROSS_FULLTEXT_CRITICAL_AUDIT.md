# 13 — Ross, Ferrero & DuPont: Full-Text Critical Audit

**Source.** Ross, D., Ferrero, V., DuPont, B. Exploring the Effectiveness of Providing Structured Design-for-the-Environment Strategies During Conceptual Design. *Journal of Mechanical Design* 144(3), 032001. Published online 2021-10-21; issue March 2022. doi:10.1115/1.4052513.
- Author list verified against the PDF and Crossref. OpenAlex lists the third author incorrectly as "Bastien Dupont".

**Copy audited.** ASME PDF supplied by the user (10 PDF pages).
- Session attachment: `/home/ubuntu/attachments/73b0d4ba-f74a-48bf-8bb4-503f3ea229dc/Exploring_the_Effectiveness_of_Providing_Structured_Design-forthe-Environment_Strategies_During_Conceptual_Design.pdf`
- Local-only copy: `data/raw/fulltext/10.1115_1.4052513_user_provided.pdf`
- SHA-256 `6c8368cb142e374851f3d74bff007a0079b83f84edc98f2efb4e64e6d45a0742`; the two copies are identical.
- **Read in full**, including Figs 5–15 and Tables 1–4. Page numbers use the article pagination 032001-*n*.

## 1. Design

| Item | Experiment 1 (toaster) | Experiment 2 (established concepts) |
|---|---|---|
| Participants | Third-year ME students. **98 results included: 35 control, 31 guidelines, 32 GREEn Quiz** (-5). Voluntary; students chose whether their results were included | 24 graduate students in a Sustainable Product Design course (-6) |
| Allocation | "respondents were separated into each respective group" (-5). **Method not reported** | Within-team pre/post. No control group |
| Conditions | Control (no tool); Telenko guidelines printout (5 min of reading, then 30 min); GREEn Quiz (complete the quiz, then 30 min) (-5) | GREEn Quiz used between "before" and "after" versions of a concept; 48 h (-6) |
| Unit | Per participant: number of concepts. **Per concept**: design decisions, sustainable decisions, quality scores | "12 teams" (the text describes four teams of six split into three pairs each, i.e. 12 pairs); 11 analysed (-6, -8) |

## 2. What the intervention changes

- It changes **environmental design guidance**: none, versus a list, versus a tailored question tree plus strategies.
- It also changes **time on task**: the guidelines group had 5 extra minutes, and the quiz group spent extra quiz time before the 30 minutes.
- It changes **effective constraints**: the authors note that the tools "possibly behave as constraints during concept generation" (-9).
- It does **not** manipulate design framing level, and it does not change the formally permitted solution space.
- The treatment is therefore a **package** of information content, structure and time.

## 3. Outcome definitions

- **Sustainable design decision:** "any word or description related to sustainability or specifically from the two DfE tools was counted as such" (-6).
  - This is a lexical count. It rewards tool vocabulary and is mechanically favourable to the treatment groups.
- **Novel design decision:** the status-quo toaster features were filtered out (-6). The text says "six" status-quo decisions but lists seven, a discrepancy.
- **Solution quality:**
  - self-assessed, 1–5;
  - judged: three judges, "sustainable product design experts", each scored sustainability, level of detail, originality and feasibility on 1–5, and the four scores were **averaged** (-6).
  - Expert ratings therefore include an environmental component, mixed with three non-environmental components.
- **Environmental impact per functional unit: not measured.** No LCA or quantitative environmental model was applied to the concepts.
- **Environmental intention versus performance:** not distinguished. The discussion concludes that the tool "enabled them to produce concepts that are more likely to be environmentally sustainable" (-9). This is inferred from decision counts and ratings, not from measured impact.

## 4. Verification of the reported Experiment 1 values

| Quantity | Reported value | Denominator | Location |
|---|---|---|---|
| Mean concepts per participant | **2.2 / 1.7 / 1.3** (control / guidelines / GREEn) | Participants (35 / 31 / 32). ANOVA F = 5.43, p = 0.0058, Fcrit = 3.09 | -7 text, Fig. 5–6 |
| Share of decisions that are "sustainable" | **≈30% / ≈52% / ≈58%** | Group-total design decisions (Fig. 7). Group totals are shown only graphically | -7 text |
| Mean judged quality | **2.72 / 3.01 / 3.17** | Concepts (averaged over 3 judges × 4 criteria) | Fig. 10, -8 (verified from the figure image) |
| Mean self-assessed quality | 2.95 / 3.10 / 3.35 | Concepts | Fig. 9, -8 |

Implied concept counts are about 77 / 53 / 42 (participants × mean). The Fig. 8 control histogram sums to roughly 78 concepts, consistent with that.

## 5. Statistical audit (source-reported discrepancies; not repaired)

| # | Issue | Evidence | Consequence |
|---|---|---|---|
| R1 | **Concept-level tests with participant clustering ignored** | The t-test dfs in Table 3 (112, 103, 93) and Table 4 (127, 118, 93) match concept counts (e.g. 77 + 53 − 2 ≈ 128), not participant counts | Pseudoreplication. Control participants contribute more concepts, so each control participant carries more weight |
| R2 | Inconsistent dfs across tables for the same concepts | Table 2 dfs are 97, 88 and 63, but Tables 3–4 use the same comparisons with different dfs | The denominators are unclear |
| R3 | Inverted decision rule | "if tobs < tcrit, then we reject this null hypothesis" (-6). The correct rule ("If tcrit > tobs, then we accept the null") is stated later (-7) | A textual error. The tables appear to follow the correct rule |
| R4 | Self-assessed ANOVA described as significant | "showed statistically significant differences ... F = 1.88 ... p-value is 0.15" with Fcrit = 3.05 (-7) | Contradiction. The self-assessed scores do **not** differ significantly |
| R5 | Judged-score ANOVA statistics appear swapped | "Fcrit = 11.08 at α = 0.05, F = 3.05 and the p-value is 3 × 10⁻⁵" (-8) | As written, F < Fcrit contradicts p = 3 × 10⁻⁵. The values were presumably transposed. Not verifiable |
| R6 | Table-number mismatch | Text says "shown in Tables 1 and 2"; the results are in Tables 2 and 3 (-7) | Minor |
| R7 | Identical guideline-vs-quiz row in Tables 3 and 4 | tobs 1.45, df 93 in both | Possible copy error |
| R8 | No multiplicity correction | At least 4 ANOVAs and 9 t-tests at α = 0.05 | Anti-conservative |
| R9 | No inter-judge agreement | The three judges' scores were averaged; no ICC, κ or α reported. One "notable inconsistency" (concept 30) is mentioned (-8) | Reliability unknown |
| R10 | Experiment 2 has no control and is confounded by time and course progression | Pre/post over 48 h, with a paired t-test on 11 units (-8/-9) | Cannot attribute the change to the tool |
| R11 | Allocation not described; a self-selected inclusion option | (-5) | Possible selection bias |
| R12 | Overinterpretation | More "sustainable decisions" and higher averaged ratings are read as "more environmentally sustainable products" (-9) | Environmental benefit is not established |

## 6. Implications for E3

- Ross shows a pattern: structured DfE information changes the *content* of concepts (more sustainability vocabulary, fewer concepts), and rated quality rises modestly.
- It does **not** show lower environmental impact. Its counting endpoint would reward a framing arm that echoes its own brief vocabulary. That is exactly the bias E3's blinded functional-unit endpoint is meant to remove.
- **Lessons for E3:**
  - analyse one selected concept per participant;
  - keep the time budget identical across arms;
  - do not use lexical counts of environmental vocabulary as an outcome;
  - report agreement among independent assessors.
