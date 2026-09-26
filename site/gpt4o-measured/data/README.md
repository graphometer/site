# GPT-4o, measured against itself: data package

Everything behind the tables on **https://graphometer.ai/gpt4o-measured/**, as
the derived statistics the runs actually produced: 121 profiles (65 one-shot,
56 conversation) built from captures made **3 to 5 September 2026** and rebuilt
on **2026-09-05**, every pairwise comparison against three anchors, the
behaviour panel, the frozen scaler, the three system prompts, the eight
scripted user sides, the four prompt pools written for this run, the per-row
caveat file, the exclusion list, the instrument's source, and the build record
for the local models. 422 files, about 9 MB.

Nothing here is summarised. If a number on the page disagrees with a file in
here, the file is right and the page is wrong; tell us and we will fix the page.

**What is not here, stated first:** the raw model replies. About 32,000
generated texts (31,653, the sum of the reply counts over the 121 profiles)
from nine makers' models raise a redistribution question under each maker's
terms that we have not resolved. Every statistic derived from those replies is
here; the replies themselves are not. The section "Redactions and omissions"
below lists everything else that was changed or left out, and why.

---

## Where this package will look like it argues with itself

1. **`p_holm: 0.023` everywhere.** Every `COMPARE_*.md` and `comparisons*.json`
   file prints a Holm-corrected p of 0.023 for almost every separating family.
   That is not a measured p-value. The test runs 300 permutations, so the
   smallest raw p it can return is 1/301, and Holm correction across seven
   families multiplies the smallest by 7: 7/301 = 0.0233 is the floor. It
   means "not one of 300 shuffles reached the observed distance". The page
   never prints it as a p-value, and neither should you.
2. **The profile markdown files mislabel the band.** `PROFILE_<cond>.md` heads
   its noise-band table "split-half", but the numbers under that heading are
   the run-split band, which is `band` in `profile_<cond>.json` and the unit
   every ratio on the page is measured in. The split-half band is the wider
   secondary one, `band_half` in the JSON. The JSON field names are right; the
   markdown heading is wrong.
3. **Eleven profiles have an empty noise band.** In those files every
   `band.<family>.p95` reads `nan`. They are the conditions captured at one run
   per prompt (the temperature-zero rows and the local Mistral Medium 3.5
   rows): a run-split band needs at least two runs of the same prompt to split.
   Those rows are still measured against the **anchor's** band, which is what
   every ratio on the page uses, so nothing on the page depends on the empty
   fields.
4. **The caveat file is silent on temperature.** `capture/CAVEATS.json` lists
   truncation, quota and serving-stack notes but not the fact that the Gemini
   family ran at 1.0 while the rest of the roster ran at 0.7. The temperature
   is recorded in every Gemini capture and in `tables/roster_provenance.csv`,
   and the page prints it on every Gemini row.
5. **The caveat file names the wrong Gemma build.** `CAVEATS.json` says the
   Gemma 4 26B MoE rows were captured on Ollama with the 32K tag. The profiles
   say otherwise: `profile_gemma26moe-warm+scripts.json` (the conversation row
   the page prints) is the 256K build, `profile_gemma26moe-warm-greedy.json`
   and `profile_gemma26moe-bare-greedy.json` are the 32K build, and
   `profile_gemma26moe-warm.json` lists both. The page follows the profiles and
   prints this disagreement too.
6. **HOW FAR is not in any results file.** The page's one-number-per-row is
   the largest of the seven family ratios in that row. The roster markdown
   files print the seven ratios and never the maximum; `tables/how_far_all_anchors.csv`
   (computed for the page) prints the maximum with the family that set it.
   Take the maximum yourself from any roster row and it will match.
7. **One condition mixes two builds.** `profile_gemma26moe-warm.json` lists two
   Ollama tags in its `models` field (a 256K-context build and a 32K-context
   build). The page does not print that row. It is here, unaltered, because
   deleting it would be worse than shipping it marked.
8. **The files carry GPT-OSS 120B values the page does not print.** Its shape
   and markup cells and its HOW FAR are in `ROSTER_vs_gpt4o-nov-warm.md` and
   `comparisons.json` like every other row. The page prints "not reported" for
   those three, because 15% of its warm replies and 56% of its bare replies
   were cut off at the output cap, and shape and markup were measured on
   cut-off text.
9. **The helper table rounds where the page does not.**
   `tables/raw_means_4o_and_nearest.csv` stores three decimals; the page rounds
   the profile's own full-precision field to two. The holding-phrase mean for
   the local Mistral Medium 3.5 is the visible case: 2.9250 in
   `profile_mistralmediumlocal-warm.json`, 2.925 in the CSV, 2.92 on the page.
10. **The behaviour panel's local Mistral Medium column disagrees with the
   hosted one.** In `results/scripts_summary.json` the
   `mistralmediumlocal-warm` conversation checks were captured at one run
   each and read the opposite of `mistralmedium-warm` on two checks (the
   exact-words check and the invented-memory check). Our own records call for
   a rerun before either column is trusted; the page prints neither.
11. **A summary of ours, corrected here.** An internal summary written before
   the page says the local Mistral Medium 3.5 is the only other model with
   fewer than three families separating in conversation. The file
   `results/ROSTER_scripts_vs_gpt4o-nov-warm.md` shows two:
   `mistralmediumlocal-warm` (shape, fw) and `mistralsmallapi-warm` (tone).
   The page follows the file.

## What is in each folder

| Path | What it holds | Provenance | Feeds |
|---|---|---|---|
| `results/ROSTER_vs_gpt4o-nov-warm.md` | The primary table: every one-shot condition against GPT-4o warm, seven family ratios, common prompt count, significant families, truncation notes. | 2026-09-05 rebuild, written by the report code in `instrument/` | Sections 03, 04, 05 |
| `results/ROSTER_scripts_vs_gpt4o-nov-warm.md` | The same for the eight scripted conversations, 48 user turns. | same | Section 06 |
| `results/ROSTER_vs_sonnet46-warm.md`, `results/ROSTER_vs_gemini3flash-warm.md`, and their `ROSTER_scripts_*` twins | The contrast anchors. | same | Section 07 |
| `results/COMPARE_<anchor>__<condition>.md` (192 files: 64 for each of the three anchors) | Per-condition detail: raw family distance, ratio against the anchor band, ratio against the candidate's own band where it has one, Holm p, the code's reading, and the ten biggest-moving features. | same | Sections 03, 04, 05, 07 |
| `results/comparisons.json`, `results/comparisons_scripts.json` | Every comparison against GPT-4o warm as JSON: `band_used` (the band recomputed on the shared prompts), `family_distance`, `band_units`, `candidate_band_units`, `p_holm`, `verdict_per_family`, `top_movers`, `n_common_stimuli`, `small_sample`, both truncation rates. | same | Every ratio on the page; the band table in section 03 |
| `results/comparisons_sonnet46-warm.json`, `results/comparisons_scripts_sonnet46-warm.json`, `results/comparisons_gemini3flash-warm.json`, `results/comparisons_scripts_gemini3flash-warm.json` | The same for the two contrast anchors. | same | Section 07 |
| `results/profiles/profile_<condition>.json` (121 files) | One profile per condition: `n`, `n_groups` (prompts), `runs_per_stimulus`, `truncation_rate`, `models`, `conditions`, `categories`, standardised `mean` and `sd` per feature, `band` (run-split, p95 and its Monte Carlo standard error), `band_half` (split-half), `by_category`, and `raw_means` in natural units. See "Redactions" for the `models` field, the pool labels and the per-prompt fields. | same | Section 02 (counts), section 03 (bands), section 04 (raw means) |
| `results/profiles/PROFILE_<condition>.md` (65 files, one per one-shot condition; the conversation profiles have no markdown page) | Human-readable summary of each one-shot profile: raw means, the band table (see disagreement 2), pool breakdown, and the conversation checks for that model. | same | Section 04 |
| `results/scripts_summary.json` | The behaviour panel: for every condition and every script, the share of runs passing each pattern check. 484 entries. | 2026-09-05 rebuild, `instrument/fp/scripts_eval.py` | Section 06 |
| `results/scaler_anchor_v1.json` | The frozen robust scaler: `calibrated_on: gpt4o-nov-bare`, `n: 479`, per-feature `center` and `scale` for 131 features. Frozen once on 2026-09-03 and reused for every rebuild. | 2026-09-03 | Section 03 |
| `capture/CAVEATS.json` | The per-row caveats as the project recorded them, byte-exact (see disagreements 4 and 5). | written 2026-09-04 to 05 during capture | Sections 02, 05, 08, 09 |
| `capture/EXCLUDE.txt` | Collections skipped by the analysis, each with its reason; nothing deleted. Rewritten for publication (see "Redactions"). | 2026-09-03 to 05 | Section 02 |
| `capture/personas/bare.txt` (0 bytes), `warm_generic.txt` (272 bytes), `gpt4o_served.txt` (541 bytes) | The three system prompts, byte-exact, em dashes included. `gpt4o_served.txt` is **our reconstruction** of a ChatGPT-style prompt, written in this project in June 2026; it is not OpenAI's text and we make no claim that it matches what ChatGPT sends. The page prints it with each of its three em dashes replaced by a comma and says so. | 2026-09-03 (the reconstruction: carried over from June 2026) | Section 02 |
| `capture/scripts/s01_boundary_push.json` to `s08_flat_for_weeks.json` | The eight scripted conversations, user side only, six turns each: `id`, `title`, `turns`. Fiction written in this project; no real person, no name. | 2026-09-03 | Sections 02, 06 |
| `capture/pool/temperament_vignettes.txt` (36), `dilemmas_paired.txt` (32), `dilemmas_pairs.json` (the 16 pairs), `self_report.txt` (12), `thinking_style.txt` (16) | The four one-shot prompt pools written for this run, 96 of the 178 prompts. | 2026-09-03 | Section 02 |
| `instrument/fp/features.py`, `stats.py`, `compare.py`, `report.py`, `scripts_eval.py` | The instrument at the revision that produced the rebuild: feature definitions (`features.py`, including `DISTANCE_EXCLUDE`), the scaler, the run-split and split-half bands, the block permutation test and Holm correction (`stats.py`), the comparison and its four readings (`compare.py`, `n_perm=300`), the roster renderer (`report.py`), and the conversation checks (`scripts_eval.py`). | 2026-09-03 | Section 03, section 06 |
| `instrument/run_profiles_excerpt.py` | Two blocks of the script that builds every profile: the guard that refuses a capture collection with more than 10% silent empty records (the sentence in section 02), and the frozen-scaler block (the asymmetry explained in section 03). Capture paths redacted; nothing else changed. | 2026-09-05 revision | Sections 02, 03 |
| `tables/how_far_all_anchors.csv` | Computed for the page: for all 357 condition-by-anchor-by-mode combinations, the largest family ratio, the family that set it, all seven ratios, the shared prompt count, the small-sample flag, the number and names of separating families, and the candidate's truncation rate. | computed 2026-09-15 from `comparisons*.json` | Every HOW FAR on the page |
| `tables/raw_means_4o_and_nearest.csv` | Twenty raw-mean measures for the four GPT-4o conditions, the two temperature-zero GPT-4o runs, and five nearby or contrast conditions (see disagreement 9 on rounding). | computed 2026-09-15 from the profiles' `raw_means` | Section 04 |
| `tables/roster_provenance.csv` | One row per profile: model identifier as served, provider, hosted or local, temperature actually recorded, replies, prompts, runs per prompt, truncation rate, caveat. Local serving identifiers rewritten (see "Redactions"). | computed 2026-09-15 from the profiles and captures | Section 02 |
| `tables/local_build_provenance.csv` | The local models as they ran: server, quantization or weights file, file size where our record gives one, parameter note, draft model, thinking switch, temperature. This is our own build record for the desktop, not a vendor document; it carries no host, path or serving key. | our build record as it stood for the 3 to 5 September 2026 runs | Section 02, the roster table |

## The schema you will actually read

Each `results/comparisons*.json` file is a map from condition name to one
comparison. The fields that carry the page:

```
a, b                        anchor and candidate condition names
n_common_stimuli            prompts (or user turns) the two profiles share
small_sample                true below 40 shared prompts; such rows are not tested and not printed
band_used.<family>          the anchor's run-split p95 recomputed on the shared prompts: the unit
family_distance.<family>    mean absolute difference of standardised feature means
band_units.<family>         family_distance / band_used: the ratio printed on the page
candidate_band_units        the same distance in the candidate's own band, where it has one
p_holm.<family>             Holm-corrected permutation p (300 permutations; floor 0.0233)
verdict_per_family          the code's reading: inside / at the edge of / inside but significant / beyond
top_movers                  the ten features that moved most, standardised, with a, b and delta
```

Condition names are the capture labels: `<model>-<prompt>` with `-greedy` for
temperature 0 and `+scripts` for the conversation profiles. `tables/roster_provenance.csv`
maps every label to the public model name and route used on the page.

Each `results/profiles/profile_<condition>.json` carries `band.<family>.p95`
(the primary unit at the profile's full prompt count), `band.<family>.mc_se95`
(the Monte Carlo standard error of that p95 over 200 splits), and
`band_half.<family>.p95` (the secondary split-half band). `raw_means` holds the
natural-unit means the page's section 04 table prints.

## Redactions and omissions, stated plainly

- **Local serving identifiers were rewritten**, 42 occurrences in 42 files
  (the `models` field of every local profile JSON and the third line of every
  local `PROFILE_*.md`), plus 54 cells in `tables/roster_provenance.csv`
  (`model_ids` and `provider`). Each internal serving key in front of a model
  name became the word `local`, so `<key>/mistral-medium-3.5` reads
  `local/mistral-medium-3.5`. Nothing else in those files was changed. The
  Ollama tags are the real tags and are unchanged.
- **The internal pool labels were mapped to the names the page uses**, 1,442
  occurrences in 130 files (the `categories` and `by_category` keys of the
  profile JSON and the pool table in every `PROFILE_*.md`). The mapping is:
  everyday-situations, dilemmas, self-report and thinking-style for the four
  pools written for this run; general, self-description, subtext and memory for
  the four pools carried over from an earlier internal battery. The same
  mapping was applied to the file names in `capture/EXCLUDE.txt`.
- **`capture/EXCLUDE.txt` was rewritten** in four ways and is the one record
  here that is not byte-exact: the four absolute capture paths are given as
  file names, two server instances named by port are named in words, the
  internal collection prefix was dropped from two smoke-test entries, and the
  pool labels were mapped as above. Every reason line is otherwise unchanged.
- **The per-prompt matrices were removed.** Each profile in the original
  records carries `stimulus_means` and `stimulus_runs`, the per-prompt and
  per-run feature rows (0.6 to 3.2 MB per profile, about 190 MB in all). They
  are not in this package, which means the bands and the permutation tests
  cannot be recomputed from it, only read. Everything the page prints is in the
  fields that ship.
- **The raw model replies are not included**, for the reason stated at the top.
- **The four older prompt pools are not included.** 82 of the 178 one-shot
  prompts (21 general prompts, 36 self-description prompts, 6 subtext prompts,
  19 prompts about memory and what persists) come from an earlier internal
  battery whose wording uses that project's internal framing. The page
  describes them and does not ship them.
- **Three instrument modules and the test file are not included.** The reader
  module, the command-line front end and the unit tests carry an absolute path
  and internal names; the tests also import the reader module, so they would
  not run here. Nothing the page claims depends on them: the five modules that
  ship contain every feature definition, band, test and reading the page uses.
- **Internal planning documents are not included.** The battery plan, the run
  book, the campaign configuration files, the capture logs and the internal
  results page carry serving details, ports and project vocabulary that
  identify our machine and our other work. The page's section 02 is the public
  statement of what ran, and this README is the public map. One consequence is
  on the page's section 09: the plan document described two temperatures per
  pool and the captures show one, and you can check the captures here but not
  the plan.
- **One page sentence cannot be checked from this package.** Section 02 says 53
  of the 57 comparison rows present in both the 2026-09-04 and the 2026-09-05
  rebuilds are byte-identical. The earlier rebuild is a project record and is
  not shipped, so that one sentence is ours to be taken on trust until we ship
  it.
- **Nothing about any other work of this project.** The capture tree this study
  came from also holds private material unrelated to this page. None of it is
  here, and no file listing here refers to it.

**The sweep.** Before hand-over the whole tree was searched for internal paths,
home paths, host and network names, service and unit names, provider keys,
tailnet names, internal project names and the personal email address: **no
hits**. A second sweep for the internal battery vocabulary (the collection
prefix, the generation tag and the four internal pool words) also returns
nothing. The only hits from the name sweep are three occurrences of the
ordinary English word "being" as a verb: one in a prompt in
`capture/pool/dilemmas_paired.txt`, the same prompt in
`capture/pool/dilemmas_pairs.json`, and one code comment in
`instrument/fp/stats.py` ("never fitted on the candidates being compared").
None of them is a name, and the two prompts are part of the battery, so they
ship as written.

## The standing sentence

If a number on the page disagrees with a file in this package, the file is
right and the page is wrong. Write to hello@graphometer.ai and the page will be
corrected in public.
