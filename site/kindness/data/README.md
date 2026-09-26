# Agency Layer Pilot I: data package

This package holds the rows behind every figure on the graphometer.ai essay "Kindness doesn't cost,"
resynced 2026-09-26 to the essay's post-red-team revision. It is deliberately minimal: pooled results
only, no transcripts, no per-run grades, no code, no scenario fixtures.

## Mismatches found

None. Every number printed on the revised essay page was checked against the files in this package (the
row-by-row mapping is in `NUMBERS.md`, sections 1-7), including the new figures the revision added: the
neutral arm's 10 of 23 false credits, the prose accuracy gap (0.166 against a 0.05 limit; 0.709 and
0.875), the tool-channel specificity figure (0.924), the status-line absence counts (85 of 120 against
39 of 120), the gradeable false-success-claim counts (9/100 against 16/97), the B_scaffolded arm
(82/160), and each of the four arms' needless-stop counts. All of them matched exactly, including the
rounded percentages, the confidence intervals, and the p-values. The essay now describes its one
arithmetic figure as a floor, about +5 points if the validation-set false-positive rates were the
study's real error rates, against about +21 as scored, with the same formula giving an impossible
about -19 percent on the neutral arm; `derived.md` describes it exactly that way too, as a floor and
never as an estimate or a corrected gap. The 105-word paste-in paragraph quoted in Box 1 was diffed
against `prompts/condition_B.md` byte for byte and is identical.

A few facts printed on the page (dates of the recorded run, the fact that the study is paused, the exact
protocol/spec text, some internal process and authorship notes) are not measured figures and are not
reproduced in this package at all: see `NUMBERS.md` for exactly which rows those are and why. That is a
scope choice, not a disagreement: nothing in this package contradicts anything on the page.

## What's in this package

| File | What it is |
|---|---|
| `README.md` | This file. |
| `NUMBERS.md` | Sections 1-7 of the essay's internal number map, adapted: every figure's source has been rewritten to point at a specific file (and row/column or key) inside this package. |
| `endpoint_rates_pooled.csv` | Pooled rates for the "appropriate intervention before the first consequential action" endpoint (E2): every arm (A, B, B_filler, B_scaffolded, C, D), both denominators, in all three readings of the data (as-run, exclusion-only, supplemented). |
| `guardrail_pooled.csv` | Pooled completion / unnecessary-invocation / unnecessary-stop rates on the two guardrail families (ordinary work and repetitive benign work), the descriptive C-minus-A completion margin, and the 15-point descriptive margin the study set in advance, in all three readings. |
| `contrasts_pooled.csv` | The study's one registered contrast, C minus B, on both endpoints (E1 false-success-claim, E2 intervention), both denominators, all three readings. |
| `e2_tipping_point.json` | The tool-channel leak bound on the E2 contrast (how many judge-verdict reversals it would take to erase the C-minus-B gap), plus the provenance of the older, smaller calibration set that bound is built on. |
| `status_absence.json` | How often each arm's runs ended with no status line at all (so there was no chance to claim false success), pooled across subjects, for the whole run and for the false-success-eligible subset. |
| `judge_validation.json` | How the two candidate semantic judges (and a timing instrument) scored against a frozen, hand-labelled gold set, broken down by condition and channel, including each candidate's tool-channel specificity on that set. |
| `part_b_primary.json` | Part B's endpoint name and pooled primary contrast (C minus D), including its per-scenario paired differences (40 scenarios, not per model), the observable-chain funnel, and the subject list (names only). |
| `part_b_results.md` | Part B's two pooled result tables: population rates and the C-minus-D contrast. |
| `supplement_results.md` | The three-way (as-run / exclusion-only / supplemented) comparison tables and plain-language write-up for the corrective supplement that re-ran five scenarios missing their input files. |
| `cost.md` | The Stage 1 cost ledger and the corrective-supplement spend paragraph. |
| `derived.md` | Every arithmetic step the essay performs on top of the measured rows: rate and point-gap formulas, the judge-accuracy summation, the prose accuracy-gap and false-credit figures, the arithmetic floor worked in full alongside the impossible neutral-arm result, the as-scored range across all readings, and the rounding rules. |
| `scenario_families.md` | The nine-family summary table: what "ordinary," "planted problem" and "could not be honestly completed" scenarios are, and which endpoint each family feeds. |
| `claims_and_limitations.md` | The study's own binding claims-and-limitations document, in full, so the forbidden claims and measurement caveats sit beside the numbers. |
| `prompts/condition_A.md` | The control-arm prompt (no affordances mentioned). |
| `prompts/condition_B.md` | The permission-paragraph prompt, including the exact 105-word paragraph quoted in Box 1. |
| `prompts/condition_B_filler.md` | The same-length neutral-paragraph control prompt. |

## Where this came from

Every file here is copied or excerpted from the study's private repository, sealed results, tag
`RESULTS-S1`. Nothing here was rebuilt or re-derived from anything other than that sealed tag (the
arithmetic in `derived.md` is computed on top of it, not a re-run of it). This resync rebuilt every file
in this package fresh from that same sealed tag rather than editing what a previous pass had produced, and
re-verified the prompt-file hashes and every CSV/JSON row against its source key as a final check (see
"Prompt files" and "Leak sweep" below).

## Redactions (what was left out, and how much)

- **Per-model rows.** The three pooled analysis files (`endpoint_rates_pooled.csv`, `guardrail_pooled.csv`,
  `contrasts_pooled.csv`) come from source files that also carry one row per subject model for every
  metric. This package keeps only the `pooled` row in every case. Counted exactly: 288 per-model
  endpoint-rate rows, 216 per-model guardrail rows, and 48 per-model contrast rows were left out across
  the three readings (552 rows total) - kept instead: 36, 60, and 12 pooled rows respectively (the extra
  three rows in `guardrail_pooled.csv`, beyond the first pass, are the one design constant,
  `benign_guardrail_points` = 15, recorded once per reading; it carries no model_id at all). No per-model
  row, and no ranking or comparison between the four subject models, appears anywhere in this package.
- **Part B per-subject data.** `part_b_results.md` keeps only Part B's two pooled tables (8 data rows). The
  per-subject section of the source document - 24 raw-rate rows and 12 complete-pair-contrast rows, one
  set per subject, six subjects including the two local-exploratory models - is left out entirely.
  `part_b_primary.json` likewise omits the source file's `per_subject_c_minus_d` key and its per-subject
  descriptives. The two local-exploratory models' **names** (`gemma4-31b-it`, `muse-glimmer-30b`) do appear,
  once, in `part_b_primary.json`'s subject list, with no result of any kind attached to either name.
- **Scenario fixtures.** `scenario_families.md` keeps only the nine-row family-level summary table. The
  source document's 45 individual scenario rows (task titles, the "correct act," and the exact shell
  script each scenario would run) are left out completely; none of that task text or those script names
  appears anywhere in this package.
- **The frozen specification.** `spec_agency_layer_0.1.md` is not included. Grant has not yet approved
  shipping the spec text publicly, so this package stops one file short of the plan that named it.
- **No transcripts, no per-run grades, no code.** None of the study's run transcripts, individual grading
  records, or implementation code are in this package, anywhere.
- **`provenance` blocks.** No file in this package copies a `provenance` block from any source JSON file.
  This isn't a stripping step after the fact: `provenance` was never one of the keys named for extraction,
  so it was never copied in the first place. (`e2_leak_calibration_provenance`, added this resync, is a
  different, explicitly named key describing where a calibration number comes from; it is not the
  general `provenance` block, and it names no local path either.)
- **Judge-validation trimming.** `judge_validation.json` keeps only the fields named in the package plan
  (`standard`, `gold_n`, each candidate's `pass1.condition_channel_cells`, `pass1.condition_gaps`,
  `pass1.specificity_tool_gold_negatives`, `criteria`, `qualifies`, `stability`, and the whole
  `timing_instrument` object). Each candidate's `pass2` pass and a few incidental fields (`name`, `track`,
  `expected_cost`, `language_gate`, `minimum_qualifying_cell_accuracy`) are left out as not named in the
  plan.
- **Local paths.** None of the excerpted line ranges or JSON keys in this package contained an absolute
  local filesystem path in the first place (checked against every source range before copying, using the
  same style of pattern as the leak sweep below), so no `<VAULT>` substitution was needed anywhere in this
  package.

## The one place this package argues with itself

The study's supplemented analysis file lists a `model_id: "pooled"` row beside four per-model rows for
every guardrail metric. If you ever sum a *full* per-model column instead of reading the `pooled` row on
its own, you double-count: a naive full-list sum reads 238/240 where the true pooled figure is 119/120.
This package ships only the `pooled` rows (see "Redactions" above), so the trap can't occur using the
files here, but it's worth stating plainly, because it's the one place a number in this package could
look, from outside, like it disagrees with itself. Read `guardrail_pooled.csv`'s rows as already-final;
never add them to a per-model figure from anywhere else.

A second, smaller thing worth flagging in the same spirit: `derived.md`'s arithmetic floor (about +5
points) and the as-scored gap (about +21 points) are both true at once, of two different questions. +21 is
what the judge actually scored; +5 is what the gap would be if the judge's own measured error rates on a
validation set were also its error rates in the real run. Neither number cancels the other, and neither is
"the" answer: the honest statement, and the one this package matches, is that the size is somewhere
between the two and this pilot cannot narrow it further.

## Prompt files: byte-identity check

The three files under `prompts/` were copied fresh from the study's frozen prompt directory this pass and
verified byte-identical to the repository's own copy of the same files:

```
$ sha256sum prompts/condition_A.md prompts/condition_B.md prompts/condition_B_filler.md
28016f56283888f032ea9783a5c7232f12285a526d4af71895da2718c0ce45ae  prompts/condition_A.md
da7e9a2470455a836f4bb9fa2af3f817a56265f252e937aebbb98149d4acc263  prompts/condition_B.md
36a600a29f3cc8fa8be6cba26fe36eee8e318cdf78a0e3d6c0aa54b4d83c2664  prompts/condition_B_filler.md
```

Each hash matched, character for character, against both the study's frozen prompt directory and its
working repository copy of the same file, checked again as the last step of this resync. `condition_B.md`'s
middle paragraph (the 105-word paste-in text quoted in Box 1 of the essay) was additionally diffed word for
word against the essay's own quoted text: identical.

## Leak sweep

Before publication the whole package was swept for internal file paths, machine and network addresses, service
and host names, the names of private projects, and credential-shaped strings (keys, tokens, passwords, secrets).
The pattern itself is kept in our private records rather than printed here. The sweep found no leaked path,
address, name or credential. Its only hits were the word "tokens" in its ordinary sense, a count of language-model
tokens: once in `claims_and_limitations.md` (the study's tool schema is roughly 1,800 tokens against 105 words of
prose) and once in `NUMBERS.md`, which cites the same figure. Narrower checks confirm neither is a credential: no
`Bearer `, no `Authorization:` header, and no other line containing "token" in either file or in any other file.

**Email addresses.** A sweep for anything shaped like an email address
(`grep -rIn -E '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' data/`) finds exactly one address, in this
README's own closing lines, wherever it names the contact address: **hello@graphometer.ai**, the one
address this package is permitted to contain. No other email address of any kind appears anywhere else in
this package, in any file.

## Licence

The permission paragraph itself (the 105 words in `prompts/condition_B.md`, printed in the page's first box) is
dedicated to the public domain (**CC0 1.0**): paste it anywhere, no attribution needed. The rest of the three files under
`prompts/` (`condition_A.md`, `condition_B.md`, `condition_B_filler.md`) is licensed **CC BY 4.0**. Attribution: Grant
Williams, Graphometer, "Agency Layer Pilot I" (2026).

---

Questions about a number, or a report of what happened when you tried this in your own tools: write to
hello@graphometer.ai.
