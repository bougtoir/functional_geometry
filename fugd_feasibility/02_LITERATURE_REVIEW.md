# 02 Literature review (PHASE 2.1)

## Search method and access limits

* Sources queried: Crossref REST API and OpenAlex API (all HTTP 200), Semantic Scholar Graph API (search endpoint: 7 of 8 requests HTTP 429, i.e. **Semantic Scholar search was not completed**; two single-paper lookups succeeded but abstracts were elided by the publisher). Publisher landing pages were attempted for one paper (Springer: bot challenge, no content). Scopus, Web of Science and Google Scholar were not used.
* Every raw response is stored under `data/raw/literature_search/` with URL, UTC time, HTTP status, path, bytes and SHA-256 in `search_ledger.csv` (170 rows; all checksums re-verified). Script: `scripts/search_literature.py`.
* DOI verification: Crossref `/works/{doi}` (or OpenAlex DOI lookup where noted) → `data/processed/doi_verified_metadata.csv`. One candidate (`10.1016/0048-7333(93)00768-M`) returned 404 and is not cited.
* Content verification level is stated per study: **A** = abstract read (OpenAlex), **M** = Crossref/S2 metadata only (title, authors, venue, year). Nothing below is claimed from full text.

## Domain-by-domain findings (15 required domains)

| # | Domain | Key verified studies (level) | What they establish for FUGD |
|---|---|---|---|
| 1 | Modular product design | Gershenson et al. 2003 J Eng Des 14 (M) | Modularity defined as decomposition into interchangeable/independent units; partitioning a product into units is a standard design dimension |
| 2 | Configurable product design | Salvador & Forza 2004 IJPE 91 (M) | Configuration of variants from modules to meet customer needs |
| 3 | Product architecture | Ulrich 1995 Res Policy (OpenAlex record `10.1016/0048-7333(94)00775-3`, M) | Mapping function→physical chunks; granularity of chunks is an architecture choice |
| 4 | Product family design | Jiao, Simpson & Siddique 2007 J Intell Manuf 18 (M) | Platform/variant selection; covers choosing a set of variants for a heterogeneous demand |
| 5 | Mass customisation | Da Silveira et al. 2001 IJPE 72 (M) | Customer-selected variants; user-side selection of the unit is a customisation mode |
| 6 | Cutting stock / C&P | Gilmore & Gomory 1961 Oper Res 9 (M); Wäscher et al. 2007 EJOR 183 (M); Alem et al. 2008 Ann OR 179 (M); Zanarini 2017 LNCS (M); Chauhan et al. 2008 Comput OR 35 roll assortment in a paper mill (M) | Choosing stock/roll sizes and cut patterns under (stochastic) demand, including paper rolls |
| 7 | Assortment problem (size selection) | Pentico 1974 Manage Sci 21 (A); Pentico 1976 Oper Res 24 (A); Pentico 1988 Oper Res 36 (A); Pentico 2008 EJOR survey (M); Tryfos 1986 JORS 37 apparel sizing as p-median (A); Akchen & Caro 2025 MSOM size substitution (A) | Which discrete sizes to offer when a larger size substitutes for a smaller requirement at a scrap cost, in 1-D and 2-D, with probabilistic demand and choice-based substitution |
| 7b | Choice-based assortment | Talluri & van Ryzin 2004 Manage Sci 50 (M); Aouad, Farias & Levi 2021 Manage Sci 67 (M) | Assortment under general discrete-choice and consider-then-choose models |
| 8 | Dispensing / dose-unit optimisation | Hatswell & Porter 2018 AHEHP 17 (M); Matsuo et al. 2020 BMC HSR 20 (A); Bach et al. 2016 BMJ (A); Rajangom et al. 2025 Value Health 28 (M); Jacques & Alexandridis 2019 Appl Sci 9 tablet scoring (A) | The "whole units cover a stochastic requirement → leftover waste" problem, unit-size optimisation, and user-breakable score lines are established and empirically evaluated in pharmacy |
| 8b | Denomination design | van Hove & Heyndels 1996 EJOR 90 (M); Telser 1995 Econ Lett 49 (M); van Hove 2001 JMCB 33 (M); Shallit 2003 Math Intelligencer 25 (M) | Combinations of discrete units to reach an amount; least-effort vs denomination-count trade-off |
| 9 | Consumer choice under configuration | Green & Krieger 1985 Mark Sci 4 (M); Michalek et al. 2004 JPIM 22 (M); Wassenaar & Chen 2003 J Mech Des 125 (M) | Product-line selection with choice models; linking engineering design to discrete choice |
| 10 | Behavioural response to unit/package geometry | Wansink 1996 J Mark 60 (A); Geier et al. 2006 Psychol Sci 17 (A); Marchiori et al. 2011 J Am Diet Assoc 111 (M); Zlatevska et al. 2014 J Mark 78 meta-analysis (M); Hollands et al. 2015 Cochrane (M) | Unit/package size changes amount used (unit bias, portion-size effect), with meta-analytic evidence — in food, not tissue |
| 11 | Perforation / divisible consumables | Vieira et al. 2021 BioResources 17 (A); Vieira et al. 2022 BioResources 18 review of converting (A); de Assis et al. 2018 BioResources 13 (A); prior-project patent registry (selectable-size towels, half-sheet perforations) | Perforation efficiency and converting effects are measured; selectable-size perforation is patented prior art |
| 12 | Task-dependent material consumption | Koenigsberg et al. 2010 Manage Sci 56 (A); van Rooijen et al. 2024 Resour Conserv Recycl (A); Williams et al. 2012 JCLP 24 (M); Wikström et al. 2014 JCLP 73 (M); Wikström et al. 2019 JIE 23 (A) | Package/unit size vs heterogeneous use and waste, including mathematical programming with discrete package sizes |
| 13 | Robust product design | Chen et al. 1996 J Mech Des 118 (M); Beyer & Sendhoff 2007 CMAME 196 (M); Bertsimas & Mišić 2017 Oper Res 65 robust product line (A) | Robustness to uncertain choice models is an existing method class |
| 14 | Stochastic / bilevel design | Colson, Marcotte & Savard 2007 Ann OR 153 (M); Alem et al. 2008 (M) | Designer-anticipates-user (leader–follower) and stochastic-demand formulations exist |
| 15 | Design for resource efficiency | Allwood et al. 2011 RCR 55 (M); Shu et al. 2017 CIRP Ann 66 (M); Willskytt & Tillman 2019 RCR 144 (A); Willskytt 2021 Sustainability 13 (M); Hertwich 2005 JIE 9 rebound (M) | "Match the delivered unit to the need" and use-phase design are recognised resource-efficiency levers for consumables |

Curated set: 55 records whose DOI existence was confirmed (46 via Crossref `/works`, 9 via OpenAlex DOI lookup), 20 with abstracts read. Irrelevant search hits (e.g. a hub-location survey and a JORS editorial surfaced by keyword) were screened out and are not cited.

## Synthesis

1. The *core* of FUGD — choose discrete unit sizes so that users covering a stochastic continuous requirement with whole units waste as little as possible — is the assortment / vial-size / denomination problem, which has a 50-year OR literature and an empirical pharmacy literature with measured requirement distributions.
2. User-breakable partitions inside one manufactured unit (score lines, perforations, selectable-size sheets) are established in pharmaceutics and in tissue patents.
3. Behavioural effects of unit size (unit bias, package-size effect) are established and meta-analysed in food; nothing found measures them for tissue sheets or perforation granularity.
4. Manufacturing-side perforation performance is measured in the tissue-converting literature but not linked to granularity choice.

The gap that survives is **empirical** (no tissue task-requirement or selection data), not conceptual or mathematical. See 04 and 05.
