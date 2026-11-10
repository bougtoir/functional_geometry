# 12 — Collado-Ruiz & Ostad-Ahmad-Ghorabi (2010): Full-Text Critical Audit

**Source.** Collado-Ruiz, D., Ostad-Ahmad-Ghorabi, H. (2010). Influence of environmental information on creativity. *Design Studies* 31(5), 479–498. doi:10.1016/j.destud.2010.06.005.

**Copy audited.** The publisher PDF supplied by the user (20 PDF pages).
- Session attachment: `/home/ubuntu/attachments/a13674ab-88af-4195-8c68-58dca73e8580/Influence_of_environmental_information_on_creativity.pdf`
- Local-only copy: `data/raw/fulltext/10.1016_j.destud.2010.06.005_user_provided.pdf`
- SHA-256 `83321ec60cd3731bf8aa02dbb79e998530887afee3a962909eb74942a95df336`; the two copies are identical.
- **Read in full.** Page numbers are journal pages (479–498). Quotations are kept brief.

## 1. Verification of the prompt's checkpoints

| Checkpoint | Verified? | Evidence |
|---|---|---|
| 56 participants | **Yes** | "a sample group of 56 students of the Vienna University of Technology" (486) |
| Five environmental-information groups | **Yes** | Table 1: A none; B newspaper item; C internal e-mail, no numerical data; D two-page LCA of competitor; E two-page LCA of own previous model (487) |
| Office-chair redesign | **Yes** | "design ideas which would reduce the environmental impact of an office chair" (486) |
| 262 generated ideas | **Yes** | "A total of 262 ideas were recorded" (487). See the discrepancy in §4: Table 3 sums to 261 |
| Detailed LCA information associated with lower creativity | **Yes, as rated creativity** | Groups D+E have lower mean ranks in every comparison of Table 3 (490); conclusion at 492 |
| Did not establish whether creative ideas have lower impact | **Yes** | "no conclusions can be driven whether more or less creative ideas will lead to more or less environmentally benign solutions" (488); "The study is not able to conclude whether more creative ideas will lead to more sustainable solutions" (494) |

## 2. Answers to the eight questions

1. **Conditions and allocation.**
   - Conditions are A–E as above. After a uniform 15-minute briefing, participants had 45 minutes of ideation and 15 minutes of documentation on a standard form (486–487).
   - Allocation: "The subjects where then divided into five groups" (486). **The method is not reported.** The phrase "Randomly distributed" (487) describes the spread of prior environmental or LCA knowledge, not assignment.
   - **Group sizes in participants are not reported.** Only idea counts per group are given (Table 3).
2. **What is manipulated.** Only environmental **information**, along two axes: *level of detail* (soft vs LCA) and *specificity* (own vs competitor product) (Fig. 1, 483).
   - Not design framing: "the strict definition of the problem is one of the controlled parameters" (485).
   - Not the permissible solution space: all groups had the same task.
3. **Material-first vs function-first briefs.** **No.** Material change is mentioned only as an example of strategies "perceived as conservative incremental approaches (like changing materials or reducing the product's weight)" (480).
4. **What is measured.**
   - **Creativity** per idea (Eq. 2, 488) = participant self-evaluation score (stickers for surprising / feasible / exciting; Eq. 1, 485) × the authors' 1–5 rating of that participant's best idea (Table 2, 488).
   - Fluency (number of ideas) and the best-idea score are also analysed (491).
   - Fixation is inferred from lower creativity; it is not measured directly.
   - Functional adequacy appears only as self-awarded "feasible" stickers.
   - **Environmental performance is not measured.**
5. **Quantitative environmental outcome.** **None.** LCA appears only as the treatment (groups D, E).
6. **Final selected concept.** **Not evaluated separately for the environmental question.**
   - All 262 ideas enter the idea-level tests.
   - A participant-level "best idea" score exists. The best idea is chosen through the participant's own sticker allocation, and it is rated only for creativity (491).
7. **Unresolved questions stated by the authors.**
   - Other intermediate levels of information detail (492).
   - Group vs individual ideation (493).
   - Differences between disciplines (494).
   - "the bi-directionality of conclusions", i.e. whether creative ideas lead to more sustainable solutions (494).
   - The need "to assess the influence of the proposed ideas in regard to occurring environmental impacts in the final product", via longitudinal tracking (494).
8. **Relation to Function Before Form.** Not a replication.
   - **Incremental extension in mechanism:** information or brief cues → fixation.
   - **Potentially distinct in endpoint:** functional-unit impact and functional adequacy of the selected concept, which the authors explicitly left open.
   - The manipulation differs. Collado-Ruiz varies *information detail*; E3/O2 varies *brief emphasis* with identical information.

## 3. Statistical inference audit

| Issue | Observation | Consequence |
|---|---|---|
| Unit of analysis | Kruskal–Wallis and Mann–Whitney tests are applied to **ideas** (N = 43, 68, 43 and 107 in Table 3). Ideas are nested in 56 participants, about 4.7 ideas per participant | **Pseudoreplication.** The independence assumption is violated, so p-values are anti-conservative. There is no clustering or participant-level aggregation |
| Score construction induces within-participant dependence | Eq. 2 multiplies each idea's self-score by the *same* best-idea rating for that participant (488) | Ideas from one participant share a multiplier, which strengthens the clustering |
| Participant-level evidence | Fluency differs across 5 groups (p = 0.048), but neither axis is significant (0.113, 0.054). The best-idea score: 5 groups p = 0.015; level of detail p = 0.002; specificity p = 0.210 (491) | The participant-level tests are the defensible inferences. They support a level-of-detail effect on the *authors' rating of the best idea* only |
| Rater blinding and reliability | The best-idea rating is the authors' own consensus after "individual evaluation and further discussion" (488). Blinding to group is not reported, and no inter-rater statistic is given | Possible assessor bias. Reliability is unknown |
| Multiple testing | One omnibus test, at least 6 combined-group tests (Table 3 plus text) and 10 pairwise tests (Table 4) | **No correction reported.** Several pairwise p-values (0.029, 0.046, 0.050) would not survive a family-wise correction |
| Textual inconsistencies (source-reported, not repaired) | (a) "pairwise comparison between the two first groups was significant (p = 0.046 > 0.05)" (490): the inequality sign contradicts the claim. (b) "differences of this group always have a p-value of p > 0.05" (490), although Table 3 shows p ≤ 0.05 throughout; presumably "<" was intended. (c) Table 3 idea counts sum to 261, but the text reports 262 ideas (487) | Recorded as discrepancies. The direction of the main finding is unaffected; its precision is uncertain |
| Time confound | Group A had no reading time. The authors argue the effect is secondary because A also had higher fluency (491) | This argument cannot separate time from information. It is a minor confound |
| Sample | Mixed-discipline students in one course | Limited external validity |

**Conclusion.** The paper supports a *qualitative* claim: detailed LCA information was associated with lower rated creativity of ideas. Its idea-level p-values overstate precision. **It provides no evidence about environmental performance, and it says so itself.**

## 4. Implications for E3

- **The mechanism is established** (information → conventional ideas). E3 cannot claim it.
- **The environmental consequence is explicitly open.** E3's endpoint targets exactly this gap.
- **Lessons:**
  - analyse at the participant level (one selected concept per participant);
  - blind independent assessors and report agreement;
  - pre-specify the multiplicity correction;
  - equalise time across arms (E3/O2 uses length-matched framing paragraphs).
