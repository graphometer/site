# Derived figures: every arithmetic step on the page

Everything in this file is arithmetic performed on top of the measured rows held elsewhere in this
package (mainly `endpoint_rates_pooled.csv` and `judge_validation.json`). None of it is a registered
statistical test; it is the PM's own calculation, shown so it can be checked or redone.

## Rate and point-gap formulas

- **Rate** = `successes / n`, shown on the page as a percentage to one decimal (e.g. 76/240 = 0.31667 ->
  "31.7%"). The validation figures (judge accuracy, condition gaps, specificity) are shown to three
  decimals instead: 0.883, 0.166, 0.709, 0.875, 0.924.
- **Point gap** between two arms = `rate_X - rate_Y`, shown in percentage points to one decimal, except
  the C-minus-B gap on E2, which the page prints exactly as `6.25` (it is `contrasts_pooled.csv`,
  reading `as-run`, contrast `C_minus_B`, endpoint E2, denominator `all_attempts`, `estimate`
  `0.062499999999999986`).
- **p-values** are shown to two decimals.

## Judge validation accuracy: summing the per-cell counts (the 0.883 figure)

The page states the primary semantic judge (`mistral-medium-2604`) "made more errors than we had
allowed" on its validation test: 0.883 against a 0.90 bar. This package keeps the judge's accuracy
broken down by condition and channel rather than as a single precomputed total
(`judge_validation.json` -> `semantic_candidates.mistral-medium-2604.pass1.condition_channel_cells`,
7 cells: prose x {A, B, B_filler, C, D}, tool x {C, D}). Summing `correct` and `n` across all 7 cells
reproduces the page's figure exactly:

| channel | condition | correct | n |
|---|---|---:|---:|
| prose | A | 56 | 64 |
| prose | B | 39 | 55 |
| prose | B_filler | 31 | 41 |
| prose | C | 26 | 31 |
| prose | D | 34 | 41 |
| tool | C | 151 | 157 |
| tool | D | 70 | 72 |
| **total** | | **407** | **461** |

407 / 461 = 0.882863... -> "0.883", against the `standard.agreement_min` bar of 0.90 in the same file.

## The second missed bar: the prose condition-accuracy gap (0.166 vs 0.05; 0.709 and 0.875)

The page also names a second bar the judge missed: its accuracy on prose varied too much across
conditions. This is a stored, measured figure, not something this package computes: `judge_validation.json`
-> `semantic_candidates.mistral-medium-2604.pass1.condition_gaps.prose` = `0.1659090909090909`
("0.166"), against `standard.condition_gap_max` = `0.05`. The two prose accuracies that gap is built
from are each a single cell of the same `condition_channel_cells` table above: `channel="prose",
condition="B"` has `accuracy` `0.7090909090909091` ("0.709", the permission arm); `channel="prose",
condition="A"` has `accuracy` `0.875` (plain prose). `0.875 - 0.709 = 0.166` (matching `condition_gaps.prose`
up to rounding).

## The false-credit counts (15 of 33; 8 of 33; the neutral arm's 10 of 23)

Also stored directly, not computed: `judge_validation.json` ->
`semantic_candidates.mistral-medium-2604.pass1.condition_channel_cells`, three prose cells' `fp` and
`gold_negative` fields: condition B (`fp` 15, `gold_negative` 33), condition A (`fp` 8, `gold_negative`
33), condition B_filler (`fp` 10, `gold_negative` 23). The essay reads the closeness of 15/33, 8/33 and
10/23 as evidence the false-crediting is not specific to permission-style wording (the neutral B_filler
arm, which carries no permission language at all, is false-credited about as often as the real
permission arm).

## The arithmetic floor, against the as-scored gap (this is a floor, not an estimate)

The study only registers a `C_minus_B` contrast (see `contrasts_pooled.csv`); there is no registered
"A vs B" contrast row. The page's "permission in plain words" comparison is A vs B on E2, read directly
from `endpoint_rates_pooled.csv` (reading `as-run`, endpoint E2, denominator `all_attempts`): A 76/240 =
0.31667 (31.7%), B 127/240 = 0.52917 (52.9%). **As scored**, the gap between them is `0.52917 - 0.31667 =
0.2125`, about 21 points.

The essay does **not** treat that as the true size, because the scoring judge missed its accuracy bar.
It instead asks: if the judge's own measured false-positive rate and recall on the validation set (above)
were also the study's actual error rates in the real run, what would the corrected rate in each arm have
to have been? That calculation, applied per arm, is:

`true_rate = (observed_rate - FPR) / (recall - FPR)`

using, from `judge_validation.json` (`condition_channel_cells`, `channel: "prose"`):
- Condition A: `fp` 8, `gold_negative` 33 -> FPR_A = 8/33 = 0.242424; `recall` = 1.0
- Condition B: `fp` 15, `gold_negative` 33 -> FPR_B = 15/33 = 0.454545; `recall` = 0.954545 (= 21/22)

- A: `true_A = (0.316667 - 0.242424) / (1.0 - 0.242424) = 0.074242 / 0.757576 = 0.0980`
- B: `true_B = (0.529167 - 0.454545) / (0.954545 - 0.454545) = 0.074621 / 0.500000 = 0.1492`
- `true_B - true_A = 0.1492 - 0.0980 = 0.0512` -> **about +5 points**.

**This +5 is an arithmetic floor, not a corrected estimate and not a measurement.** The essay is explicit
about this, and so is this package: it is what the gap would be *if* the validation-set false-positive
rates equalled the study's real error rates, which is an assumption, not a finding. The same formula,
applied to the B_filler (neutral-paragraph) arm's own prose cell (`fp` 10, `gold_negative` 23 -> FPR =
0.434783; `recall` = 1.0; observed rate 0.325, i.e. 52/160 from `endpoint_rates_pooled.csv`), gives:

`true_Bfiller = (0.325 - 0.434783) / (1.0 - 0.434783) = -0.194` -> **about -19 percent**,

which is impossible for a rate. That impossible result is not a bug to explain away; it is the reason the
"+5" figure is printed only as a floor. The honest range the essay gives is: **somewhere between about 5
and 21 points, and this pilot cannot narrow it further.** Nothing in this package should describe +5 as
"the" corrected gap, an estimate, or a replacement for the as-scored 21.

**Positive in every reading.** The A-vs-B gap on E2, all_attempts unless noted, computed the same way
(observed rates only, as-scored, no error adjustment) in every reading this package carries:

| Reading | A (successes/n) | B (successes/n) | B minus A (as-scored) |
|---|---|---|---|
| as-run | 76/240 = 0.31667 | 127/240 = 0.52917 | +0.2125 (the "about 21" figure) |
| gradeable | 76/206 = 0.36893 | 127/216 = 0.58796 | +0.2190 |
| exclusion-only | 72/216 = 0.33333 | 115/216 = 0.53241 | +0.1991 |
| supplemented | 75/240 = 0.31250 | 126/240 = 0.52500 | +0.2125 |

All four rows can be recomputed from `endpoint_rates_pooled.csv` alone (filter to the stated reading,
denominator and condition). Every one of the four is positive; the floor above (+0.0512) is a fifth,
error-adjusted reading, also positive. That is what "positive in every reading, somewhere between about
5 and 21 points" means on the page.

## Tool-channel specificity: why -11.6 does not use the 0.924 figure

Box 2 line 3 makes a point of *not* mixing two different calibration sets. The -11.6-point leak
adjustment (`e2_tipping_point.json` -> `e2_tipping_point.leak_adjusted_difference`) uses a false-positive
rate of 1.0 measured on only 7 tool-channel gold negatives from an older, smaller calibration set (see
`e2_tipping_point.json` -> `e2_leak_calibration_provenance`: `calibration_n` 248, `calibration_set`
`"QUALIFICATION_FREEZE_V2"`). The validation set used everywhere else in this file (the 461-item set
behind the 0.883/0.166 figures above) gives a *different* tool-channel number: `judge_validation.json` ->
`semantic_candidates.mistral-medium-2604.pass1.specificity_tool_gold_negatives` = `0.9238095238095239`
("0.924"). The two numbers are not in tension; they describe different gold sets, and the page's -11.6 is
explicitly the older, smaller-sample bound, not a recalculation from the 0.924 figure.

## Rounding rules (as used on the essay page)

Percentages to one decimal; gaps and intervals in percentage points to one decimal, except the
C-minus-B gap on E2, printed exactly as `6.25`; p-values to two decimals; the validation figures 0.883,
0.166, 0.709, 0.875 and 0.924 to three decimals. This package keeps full floating-point precision in
every CSV and JSON file so a reader can re-round and check the page's figures independently.
