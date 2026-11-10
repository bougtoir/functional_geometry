# 01 — Conceptual Prior Art (Gate A)

Project: *Function Before Form* research gate. Proposition under test (not an established finding): "The function is the requirement. The form is a hypothesis. The material is a choice."

## 1. Search scope and evidence levels

| Item | Status |
|---|---|
| Databases | Crossref + OpenAlex (51 queries over three passes: 21 domain, 15 gap, 15 targeted second pass, 15 third pass; all HTTP 200); DOI verification Crossref/OpenAlex (71 DOIs, 3 returned 404 and were dropped); Unpaywall (26 lookups); Semantic Scholar batch abstract lookup (1 call, 200, but almost no abstracts returned for closed papers) |
| Not searched | Scopus, Web of Science, Google Scholar, patent databases, grey literature (UNEP reports) |
| Full text actually read | 8 works (legal OA copies: institutional repositories or gold OA). Elsevier publisher URLs returned 403 and are not counted. |
| Curated set | 42 works in `evidence/CURATED_SOURCES.csv` with verification level FT (full text, 8), AB (abstract, 18), MD (metadata only, 15), NV (not retrieved, 1) |
| Raw evidence | `data/raw/` with ledger `data/raw/literature_search/search_ledger.csv` (330 rows; existence, byte size and SHA-256 re-verified, 0 mismatches — `data/processed/ledger_verification.csv`) |

Rule followed: findings are stated only at the level actually accessed. MD entries are used only for the existence and stated topic of a work, never for its findings.

## 2. Does the literature already address the combined argument?

The combined argument has four parts. Each part is already in the literature; the *combination tested against environmental outcomes* was not found.

| Component of the proposal | Existing literature | Evidence level |
|---|---|---|
| (a) Separate function from form; describe the requirement form-independently | Functional basis: "Functional models represent a form independent blueprint of a product" (Stone & Wood 2000, S02); FBS separates function, behaviour, structure (Gero & Kannengiesser 2004, S04); systematic design abstraction before embodiment (Pahl et al., S01) | AB / MD |
| (b) Decide function before material | Same design-methodology canon; LCA requires comparison on a function-defined unit (Cooper 2003, S32); Function Impact Matrix attaches LCA to functions in early design (Devanathan et al. 2010, S26) | AB / MD |
| (c) Ecodesign should go beyond product/material improvement to function and system | Ceschin & Gaziulusoy 2016 (S17, full text): early green design "primarily focused on lowering environmental impact through redesigning individual qualities of individual products … replacing virgin materials with recycled materials, replacing hazardous/toxic materials with non-hazardous ones"; argues "to move from a focus on product improvements-alone, towards a wider approach"; PSS are "value propositions oriented to satisfy users through the delivery of functions instead of products". Also PSS (Mont 2002; Tukker 2004), circular strategies (Bocken et al. 2016, full text), sufficiency (Bocken & Short 2016). The Brezet & van Hemel (1997) levels are widely attributed (product improvement / redesign / function innovation / system innovation) but the source was **not accessed**; only its citation in S17 is verified. | FT / AB / NV |
| (d) Familiar forms persist because of bounded cognition and inherited solutions | Design fixation (Jansson & Smith 1991; Purcell & Gero 1996; Smith et al. 1993; Chrysikou & Weisberg 2005; Linsey et al. 2010; Leahy et al. 2020); reused prior work "carries assumptions about physical properties, materials, manufacturing processes and context of use" (Crilly 2015, full text, citing Eckert et al. 2005); lock-in/path dependence (Arthur 1989; Unruh 2000) | FT / AB / MD |
| (e) Material substitution can shift burdens; material intuitions mislead | Kakadellis & Harris 2020 (full text): bioplastic benefits "often negated by the agricultural inputs", food-protection function must be in the LCA; Gallego-Schmid et al. 2019: EPS single-use lowest impact, reusable PP better only after 3–39 reuses; Stefanini et al. 2021; Zimmerman & Anastas 2015 (regrettable substitution); consumers judge greenness by material type (Boesen et al. 2019; Sokolova et al. 2023, N = 4,103) | FT / AB |

## 3. Answers A1–A10

| Q | Question (abridged) | Answer | Basis |
|---|---|---|---|
| A1 | Is separation of function and form established? | **Yes — established theory.** | S02, S04, S01 |
| A2 | Is "function before material" established? | **Yes, as normative design method and as LCA practice** (functional unit). Not established as an empirically demonstrated cause of better environmental outcomes. | S01, S26, S32 |
| A3 | Does ecodesign already question product form / product existence? | **Yes.** DfS evolution, PSS, sufficiency and circular strategies explicitly move beyond the product. | S17 (FT), S20–S25 |
| A4 | Is there a named hierarchy from material change to function/system innovation? | **Very likely yes** (Brezet levels; S17's four innovation levels verified). The Brezet source itself was not verified here. | S17 FT; S18 NV |
| A5 | Is form fixation (retaining familiar features) established? | **Yes, robustly**, but measured as feature repetition/novelty, not environmental quality. | S05–S12, S14 |
| A6 | Has *material-first framing* been experimentally shown to produce form fixation? | **Not found.** No screened study manipulated a material-substitution brief versus a functional brief. | gap queries s05, s08, s11, t09, t11 |
| A7 | Have framing strategies been compared on environmental outcomes of the resulting designs? | **Not found.** Closest: Faludi et al. 2020 (FT) compared three sustainable design methods with >172 professionals but measured *self-reported* value because objective assessment of early ideas was "deemed too subjective and too highly uncertain". Collado-Ruiz & Ostad-Ahmad-Ghorabi 2010 (title: environmental information and creativity) could not be read and is an **unresolved risk**. | S28 FT; S16 MD |
| A8 | Does abstraction/function-first framing reliably improve outcomes? | **Not established.** It increases originality and out-of-domain search (S10, S11) but Zahner et al. report "not all the added ideas fit the problem constraints". | S10, S11 AB |
| A9 | Is substitution bias in professional design practice empirically demonstrated? | **Not established.** Material-type heuristics are demonstrated for consumers (S38, S39), not for designers or firms. See Gate C. | S38, S39 AB |
| A10 | Does the literature already warn that like-for-like substitution can worsen outcomes? | **Yes.** | S34, S35, S36, S37 |

## 4. Gate A conclusion

- The **principle** ("function is the requirement, form is a hypothesis, material is a choice") is a restatement of established design methodology plus ecodesign's innovation-level argument. Conceptual originality: **very low**.
- What was *not found* in the screened literature is narrower: **a controlled test of whether the framing level of a brief changes the environmental performance (per functional unit, with functional equivalence checked) of the designs people actually select under a bounded effort budget.** This is the only candidate gap carried forward.
- Search limitations (no Scopus/WoS/Google Scholar, Collado-Ruiz 2010 unread, Brezet 1997 unread) mean the gap is "not found", not "proven absent".
