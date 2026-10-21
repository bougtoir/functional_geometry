# Straw replacement-model audit

## Audit conclusion

The pre-audit implementation multiplied retained straw mass by \(1+r\). Computationally, \(r\) was therefore the **expected number of additional replacement straws per successful serving**, not a Bernoulli replacement probability. The implementation has been renamed accordingly. The primary Monte Carlo retains this expected-rate formulation and the same triangular values, so its numerical draws and primary straw outputs are unchanged apart from terminology.

A second formulation now represents a true independent per-attempt failure probability. It is used for analytical boundaries and one-way sensitivity, not for the primary Monte Carlo.

## Definitions

Let:

- \(s\): fractional straw-length reduction;
- \(r\): expected number of additional straws used per successful serving;
- \(p\): independent failure probability for each straw attempt;
- \(c\): container or package burden caused by the geometry change **per successful serving**, normalized to baseline straw material mass.

The definition of \(c\) is additive after replacement or repeated-attempt straw use because it is incurred once per successful serving. It is not a per-attempt container burden.

## Formulation A: expected additional replacement rate

The normalized material ratio is

\[
R_{S,\mathrm{rate}}=(1-s)(1+r)+c.
\]

At break-even, \(R_{S,\mathrm{rate}}=1\), hence

\[
r^*=\frac{1-c}{1-s}-1.
\]

At \(c=0\),

\[
r^*=\frac{s}{1-s}.
\]

For \(s=0.20\), \(r^*=0.25\). Thus a 20% shortening is erased by an expected 0.25 additional straws per successful serving. This is a rate and must not be described as a 25% failure probability.

## Formulation B: independent per-attempt failure probability

With independent failure probability \(p\), the number of attempts through the first success is geometric:

\[
E[N]=\frac{1}{1-p}.
\]

Under the stated per-successful-serving definition of \(c\),

\[
R_{S,\mathrm{prob}}=\frac{1-s}{1-p}+c.
\]

At break-even,

\[
p^*=1-\frac{1-s}{1-c}.
\]

At \(c=0\), this simplifies to

\[
p^*=s.
\]

For \(s=0.20\), the independent per-attempt failure-probability boundary is therefore 20%, not 25%.

If a future study instead defines shifted container burden per attempt, the model must be changed to \((1-s+c)/(1-p)\). That is not the definition used in this project.

## Verification

Tests evaluate \(s=0.10, 0.20, 0.30\) under both formulations at \(c=0\) and \(c=0.05\). In every case, substituting the analytical boundary into its material-ratio function returns 1.0. The zero-shift boundaries are:

| Length reduction \(s\) | Expected additional replacement-rate \(r^*\) | Independent failure probability \(p^*\) |
|---:|---:|---:|
| 0.10 | 0.111111 | 0.10 |
| 0.20 | 0.25 | 0.20 |
| 0.30 | 0.428571 | 0.30 |

The generated `table_4_straw_break_even.csv` reports both formulations with and without 5% shifted burden. The generated one-way sensitivity file reports separate `straw_expected_rate` and `straw_failure_probability` cases.

## Monte Carlo identification

The primary straw Monte Carlo uses:

```text
monte_carlo_replacement_formulation =
EXPECTED_ADDITIONAL_REPLACEMENT_RATE
```

and samples `expected_additional_replacement_rate_triangular = [0.0, 0.05, 0.35]`. These values were not reinterpreted as probabilities. The true-probability formulation is a distinct sensitivity analysis because changing the primary formulation would change the estimand and numerical output rather than merely correcting terminology.
