# 06 — Blind Assessment Protocol (draft)

## 1. Standardised concept description (SCD) template

Every final selected concept is transcribed into the same SCD before assessment. Transcription is done by a **research assistant who is not an assessor**, using only what the participant produced (sketch, text, worksheet).

| Field | Content | If participant did not specify |
|---|---|---|
| 1 Concept summary | ≤ 60 words, neutral wording, no framing vocabulary from any arm brief | — |
| 2 Sketch | Re-drawn or scanned; handwriting and arm-specific annotations removed | — |
| 3 Components and materials | List | "not specified" |
| 4 Mass / size class | Value or S/M/L | "not specified" |
| 5 Manufacturing route | Text | "not specified" |
| 6 Use pattern | Uses per unit, cleaning, who handles it | "not specified" |
| 7 Supporting system | Infrastructure, logistics, service | "none stated" |
| 8 End of life | Text | "not specified" |
| 9 Participant's own feasibility notes | Text | — |

Rules:
- The same worksheet with the same fields is given to **all arms**. No arm receives prompts for extra fields.
- The SCD transcriber follows a fixed wording guide. A second assistant checks a random 20% sample against the originals for added or omitted information. Discrepancies are logged.
- Arm-revealing words are masked with a fixed list derived from the three briefs (e.g. "substitute", "same shape", "function"), unless the participant's concept cannot be described without them; such cases are logged.
- SCDs receive random IDs. The arm key is held by a data manager who does not assess.

## 2. Assessors

- **Two independent assessors**, each with demonstrable LCA competence (e.g. ≥1 completed product LCA; criteria fixed in advance).
- Neither assessor is involved in designing the briefs or in recruiting participants.
- Assessors are blind to arm, participant expertise and hypotheses. They are told only that concepts come "from a design study".

## 3. Assessment instructions

1. Read the SCD and score the FE gate (F1–F8) **first**. Lock the FE scores in the scoring system; they cannot be edited afterwards.
2. Map each SCD field to the frozen archetype library (05 §5). Use defaults only for fields marked "not specified", and log every default.
3. Run the fixed calculation tool (same version for both assessors). Assessors choose inputs, not the model.
4. Record the median, 90% interval and data-quality score.
5. Lock the record. Locking is time-stamped; the record is read-only after that.

Permitted assumptions: only archetype defaults and the scenario options listed in 05. Assessors must not consult external sources about the concept.

## 4. Disagreement handling

- Reliability (07) is computed on the **locked independent scores, before adjudication**. Those scores are archived unchanged.
- Adjudication follows reliability: a third assessor reviews pairs whose FE status differs, or whose log-impact differs by more than a pre-specified threshold (set before the pilot). The adjudicated value is used for the main analysis.
- A sensitivity analysis uses the mean of the two independent assessments instead of the adjudicated value.

## 5. Information-parity safeguards

- Identical worksheet, time and materials across arms (09).
- Description length (word count) and the number of "not specified" fields are recorded per arm, as covariates and as a manipulation side-effect check.
- If one arm systematically produces less-specified concepts, the assessment uncertainty differs by arm. This is reported, not corrected away.

## 6. What is prohibited

- No manufactured or simulated assessor ratings.
- No assessor access to the arm key before the analysis dataset is locked.
- No re-assessment after unblinding.
