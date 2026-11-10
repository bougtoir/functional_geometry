# 27 — Inventory and Licence Audit

| Source | Type | Access verified in this gate | Licence / redistribution (verified?) |
|---|---|---|---|
| USLCI (Federal LCA Commons), `FLCAC-admin/uslci-content` | Public inventory | Repository reachable; LICENSE file retrieved | **MIT licence, verified** from the raw LICENSE file. US geography |
| Agribalyse (ADEME) | Public (food/agri) | Documentation page retrieved | "free of charge and can be adapted for use in LCA software" (verified text). The full version depends on ecoinvent; the core version is not recommended by ADEME (verified text). Limited relevance (food, not packaging) |
| ecoinvent | **Licensed** database | Licence and EULA pages returned HTTP 404 to automated requests | **Not verified.** It is commercial or academic-licensed, and redistribution of unit-process data is generally restricted; the terms must be checked. **No access is claimed** |
| EU Environmental Footprint datasets (EPLCA / LCDN) | Public / conditional | Page is JavaScript-only; content not retrievable | **Not verified** |
| ELCD | Archived public | HTTP 404 | **Not verified** |
| openLCA Nexus | Mixed free/paid | Page is JavaScript-only | **Not verified** |
| Idemat | Free tables (conditions apply) | Page retrieved; terms not parsed | **Not verified** |
| Published benchmark LCAs (26) | Published estimates | OA copies exist | Usable as benchmark *results*. Copying their inventories requires checking each article's licence (many are CC BY; to be confirmed per paper) |

**Coverage per life-cycle element:**
- materials and manufacturing: USLCI (partial), ecoinvent (licensed), benchmark papers;
- transport: USLCI / ecoinvent;
- use phase, cleaning, dishwashing: benchmark papers and ecoinvent;
- reuse, return and failure rates: benchmark papers and scenario assumptions only, **no measured database**;
- end of life: regional scenario datasets (ecoinvent / EF; not verified);
- infrastructure: ecoinvent (licensed) or explicit exclusion.

**Usable inventory exists only partially.** The public, licence-verified source is USLCI (MIT), which is US-only and has gaps for packaging and foodservice. A licensed database (likely ecoinvent) is needed for consistent coverage. **Its licence and the author's institutional access must be confirmed.** Reuse, return and failure parameters have no database source and must be scenario ranges derived from the benchmarks.
