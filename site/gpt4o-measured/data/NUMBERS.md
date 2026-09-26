# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/gpt4o-measured/ . Paths are
relative to this folder. Labels: **measured** (from a recorded run, the
2026-09-05 rebuild of captures made 3 to 5 September 2026), **vendor** (the
maker's statement), **arithmetic** (computed from recorded values, not run). The
**n** column is the number of prompts, or user turns, the comparison was
measured on; it is blank for figures that are not distances. If a row and a file
disagree, the file wins.

Every table on the page maps to one file, row for row: the figure rows below
name the file and the rule for finding a cell, and the prose figures each have
their own row.

**The one place a file will look like it contradicts the page:** every
`COMPARE_*.md` prints `p (Holm) 0.023` beside almost every separating family,
and the page says no p-value of 0.023 was measured. Both are right. 0.0233 is
the smallest value a 300-permutation test can return after Holm correction
across seven families (7/301); the files print the floor, the page names it as
the floor. Ten more places where the package looks like it argues with itself
are listed at the top of `README.md`.

Condition labels below are the capture labels used inside the files;
`tables/roster_provenance.csv` maps them to the public names on the page.

---

## Hero, lead and section 01

| Figure on the page | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| 1.17, GPT-4o warm at temperature 0 | measured | 81 | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/ROSTER_vs_gpt4o-nov-warm.md` | row `gpt4o-nov-warm-greedy`, markup column (the row maximum) |
| "set by markup" for that row | measured | 81 | same | `tables/how_far_all_anchors.csv` | anchor `gpt4o-nov-warm (batch)`, body `gpt4o-nov-warm-greedy`, `driver` |
| "no family separating" | measured | 81 | same | same roster row; `results/comparisons.json` | significant families "none"; `p_holm` all above 0.05 |
| "its other six families read between 0.35 and 0.88" | measured | 81 | same | same roster row | shape 0.35, punct 0.88, lex 0.68, tone 0.46, fw 0.78, think 0.65 |
| 2.23, Mistral Medium 3.5 local | measured | 178 | same | `results/ROSTER_vs_gpt4o-nov-warm.md` | row `mistralmediumlocal-warm`, shape column |
| "set by shape" for that row | measured | 178 | same | `results/comparisons.json` | `mistralmediumlocal-warm` `band_units`: shape 2.2286 is the maximum, tone 2.2268 rounds to the same printed 2.23 |
| "all seven families still separating" | measured | 178 | same | same roster row | significant families lists all seven |
| 3.05, GPT-4o under the ChatGPT-style prompt, set by shape | measured | 178 | same | `results/ROSTER_vs_gpt4o-nov-warm.md`; `results/COMPARE_gpt4o-nov-warm__gpt4o-nov-served.md` | row `gpt4o-nov-served`, shape column |
| "1.0 means as far as GPT-4o is from itself" | measured | 178 / 81 / 48 | same | `results/profiles/profile_gpt4o-nov-warm.json`; `results/comparisons*.json` | `band.<family>.p95`; `band_used` per comparison |
| 178 one-shot prompts | measured | 178 | same | `results/profiles/profile_gpt4o-nov-warm.json` | `n_groups` |
| eight six-turn conversations, 48 user turns | measured | 48 | same | `results/profiles/profile_gpt4o-nov-warm+scripts.json` | `categories` (8 scripts), `n_groups` 48 |
| 26 models; 25 other models | measured | | same | `tables/roster_provenance.csv` | 121 rows; the distinct models behind the 31 identifiers |
| 131 counted features, seven families | measured | | 2026-09-03 | `instrument/fp/features.py`; `results/scaler_anchor_v1.json` | feature definitions and `DISTANCE_EXCLUDE` (11 names); `center` has 131 keys |
| snapshot `gpt-4o-2024-11-20` | measured | | same | `results/profiles/profile_gpt4o-nov-warm.json` | `models` |

## Section 02: what we ran

| Figure | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| anchor: 479 replies, 178 prompts, 2.69 runs per prompt | measured | 178 | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/profiles/profile_gpt4o-nov-warm.json` | `n`, `n_groups`, `runs_per_stimulus` |
| 123 prompts run three times, 55 twice | measured | 178 | same | the same profile in the original records | the lengths of the per-prompt run lists (the per-prompt fields are not shipped; see README) |
| anchor temperature 0.7 | measured | | same | `tables/roster_provenance.csv` | row `gpt4o-nov-warm`, `temperature` |
| pool sizes 36, 32 (16 pairs), 12, 16 | measured | | 2026-09-03 | `capture/pool/temperament_vignettes.txt`, `dilemmas_paired.txt`, `dilemmas_pairs.json`, `self_report.txt`, `thinking_style.txt` | non-empty line counts; 16 keys |
| older pool sizes 21, 36, 6, 19 | measured | | 2026-06-29 (the earlier battery) | not shipped (see README) | non-empty line counts of the four pool files, recounted 2026-09-16 |
| 82 + 96 = 178 | arithmetic | 178 | same | `results/profiles/profile_gpt4o-nov-warm.json` | matches `n_groups` |
| 48 user turns, two runs per turn, 96 replies | measured | 48 | same | `results/profiles/profile_gpt4o-nov-warm+scripts.json` | `n_groups` 48, `runs_per_stimulus` 2.0, `n` 96 |
| the local Mistral Medium 3.5 ran once per turn | measured | 48 | same | `results/profiles/profile_mistralmediumlocal-warm+scripts.json` | `runs_per_stimulus` 1.0 |
| GPT-OSS 120B returned 95 replies rather than 96 | measured | 48 | same | `tables/roster_provenance.csv` | row `gptoss120-warm+scripts`, `n_replies` |
| warm prompt 272 bytes; ChatGPT-style prompt 541 bytes; bare 0 bytes | measured | | 2026-09-03 | `capture/personas/warm_generic.txt`, `gpt4o_served.txt`, `bare.txt` | file sizes |
| three em dashes in the ChatGPT-style prompt | measured | | same | `capture/personas/gpt4o_served.txt` | count of U+2014 |
| 26 models, 31 identifiers | measured | | same | `results/profiles/profile_*.json` | the union of the `models` fields over the 121 files, before the serving keys were rewritten |
| 65 one-shot and 56 conversation profiles, 121 in all | measured | | same | `results/profiles/` | file count; `kind` field |
| Gemini family at temperature 1.0; others 0.7; controls 0.0 | measured | | same | `tables/roster_provenance.csv` | `temperature`, every row |
| 1,200-token output cap | measured | | same | `capture/CAVEATS.json` | every truncation caveat names the 1,200-token cap |
| the quality guard: more than 10% empty with no error, refused | measured | | 2026-09-05 revision | `instrument/run_profiles_excerpt.py` | the first block, `if recs and silent / len(recs) > 0.10` |
| 53 of the 57 comparison rows byte-identical between rebuilds | measured | | 2026-09-04 and 2026-09-05 rebuilds | not shipped (see README) | the two `ROSTER_vs_gpt4o-nov-warm.md` files compared row by row on 2026-09-16 |
| roster table: identifiers, temperatures, warm reply counts, prompt counts | measured | each row's own | same | `tables/roster_provenance.csv`; `capture/CAVEATS.json` | the row with the same capture label, batch rows ending `-warm` |
| Claude Sonnet 5 warm: 323 replies, 115 prompts | measured | 115 | same | `tables/roster_provenance.csv` | row `sonnet5-warm` |
| Gemini 3.5 Flash 446 replies over 168 prompts; Mistral Large 430 over 165; Mistral Small hosted 477; GLM-5.3 Flash 476; Qwen3.8 Max 478; Gemini 3 Flash 478; Gemini 3.8 Flash 478 | measured | as stated | same | same | rows `gemini35flash-warm`, `mistrallarge-warm`, `mistralsmallapi-warm`, `glm53flash-warm`, `qwen38max-warm`, `gemini3flash-warm`, `gemini38flash-warm` |
| local rows: Mistral Small 4 479; Mistral Medium 3.5 178 at one run; Qwen3.5-122B 356; Qwen3.8-27B 479; Qwen3-235B 356; Gemma 4 31B 356; Gemma 4 26B MoE 479 | measured | 178 | same | same | rows `mistralsmall-warm`, `mistralmediumlocal-warm`, `qwen122-warm`, `qwen38-warm`, `qwen235-warm`, `gemma31qat-warm`, `gemma26moe-warm` |
| local quantization, parameter, draft-model and build details | measured (our build record) | | as it stood for the 3 to 5 Sep 2026 runs | `tables/local_build_provenance.csv` | one row per local model |
| Gemini 3.1 Pro excluded: quota, warm never captured | measured | | same | `capture/CAVEATS.json`; `tables/roster_provenance.csv` | caveat text; row `gemini31pro-bare` |
| Gemma 4 26B MoE warm mixes two builds | measured | | same | `results/profiles/profile_gemma26moe-warm.json` | `models` lists two tags |
| GPT-OSS 120B: 15% of warm, 56% of bare replies at the cap | measured | | same | `results/profiles/profile_gptoss120-warm.json`, `profile_gptoss120-bare.json` | `truncation_rate` 0.148, 0.558 |
| DeepSeek V4 Pro bare 16%; Qwen3.8-27B warm 4.6% | measured | | same | `results/profiles/profile_dsv4pro-bare.json`, `profile_qwen38-warm.json` | `truncation_rate` 0.161, 0.046 |
| Qwen3-235B local: 40 prompts re-asked at a longer timeout | measured | | same | `capture/CAVEATS.json` | rows `qwen235-bare`, `qwen235-warm` |
| Sonnet 4.6 conversations through OpenRouter; the bare conversation run mixed routes | measured | | same | `tables/roster_provenance.csv`; `results/profiles/profile_sonnet46-bare+scripts.json` | `model_ids`; `models` lists both routes |
| Mistral Medium 3.5 local: no bare one-shot profile | measured | | same | `capture/EXCLUDE.txt` | the three `mistralmediumlocal-bare` file names at the end |

## Section 03: the scale

| Figure | Label | n | Run date | File | Field |
|---|---|---|---|---|---|
| scaler frozen on GPT-4o bare, 479 replies, 131 features | measured | | 2026-09-03 | `results/scaler_anchor_v1.json` | `calibrated_on`, `n`, key count of `center` |
| the reason for the frozen bare scaler | measured | | 2026-09-05 revision | `instrument/run_profiles_excerpt.py` | the second block and its comment |
| eleven raw counts excluded from the distance | measured | | 2026-09-03 | `instrument/fp/features.py` | `DISTANCE_EXCLUDE` |
| 200 splits, 95th percentile | measured | 178 | 2026-09-05 rebuild | `results/profiles/profile_gpt4o-nov-warm.json`; `instrument/fp/stats.py` | `band.<family>.n_splits` 200; `run_split_band` |
| band at 178: 0.0892, 0.0976, 0.0726, 0.1012, 0.0281, 0.0938, 0.0771 | measured | 178 | same | `results/profiles/profile_gpt4o-nov-warm.json` | `band.<family>.p95` |
| band at 81: 0.1283, 0.1398, 0.1054, 0.1298, 0.0314, 0.1402, 0.1223 | measured | 81 | same | `results/comparisons.json` | entry `gpt4o-nov-warm-greedy`, `band_used` |
| band at 48: 0.1337, 0.2592, 0.2354, 0.2636, 0.0785, 0.2908, 0.2380 | measured | 48 | same | `results/comparisons_scripts.json` | entry `gpt4o-nov-served`, `band_used` |
| Monte Carlo standard error 0.9% to 5.4%, largest on shape and markup | arithmetic | 178 | same | `results/profiles/profile_gpt4o-nov-warm.json` | `band.<family>.mc_se95` / `p95`: fw 0.94%, lex 3.43%, think 3.59%, tone 4.13%, punct 4.18%, markup 5.17%, shape 5.42% |
| the code's four readings | measured | | 2026-09-03 | `instrument/fp/compare.py` | function `verdict` |
| control row: 0.35, 0.88, 0.68, 0.46, 1.17, 0.78, 0.65 | measured | 81 | 2026-09-05 rebuild | `results/COMPARE_gpt4o-nov-warm__gpt4o-nov-warm-greedy.md` | the seven family rows; `p (Holm)` all above 0.05 |
| markup floor 0.0281 less than half of vocabulary 0.0726 | arithmetic | 178 | same | `results/profiles/profile_gpt4o-nov-warm.json` | `band.markup.p95`, `band.lex.p95` |
| bare markup raw distance 0.575 = 20.49 units | measured | 178 | same | `results/COMPARE_gpt4o-nov-warm__gpt4o-nov-bare.md` | markup row |
| the same distance reads 6.2 against the split-half band 0.0924 | arithmetic | 178 | same | `results/profiles/profile_gpt4o-nov-warm.json` | `band_half.markup.p95` = 0.0924; 0.575 / 0.0924 = 6.22 |
| 300 permutations; Holm across seven families; below 40 not tested | measured | | 2026-09-03 | `instrument/fp/compare.py`, `instrument/fp/stats.py` | `compare(..., n_perm=300)`; `holm`; `MIN_STIMULI = 40` |
| floor 1/301, then 7/301, about 0.023 | arithmetic | | same | as above | |
| 214 of the 216 separations in the printed one-shot rows sit at the floor | measured | the 33 printed one-shot rows | 2026-09-05 rebuild | `results/comparisons.json` | count of `p_holm` below 0.05 and equal to 0.0233 over the rows printed in sections 04 and 05 |
| the two that do not: Llama 4 Maverick 0.0399, temperature-zero Gemma 0.0365, both markup | measured | 178 and 81 | same | same | entries `llama4mav-warm`, `gemma26moe-warm-greedy`, `p_holm.markup` |

## Section 04: GPT-4o against itself

| Figure | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| the five-row GPT-4o table, every cell | measured | in the Prompts column of each row | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/ROSTER_vs_gpt4o-nov-warm.md`; `tables/how_far_all_anchors.csv` | rows `gpt4o-nov-warm-greedy`, `gpt4o-nov-served`, `gpt4o-nov-bare`, `gpt4o-nov-bare-greedy`; HOW FAR and "set by" from the CSV, anchor `gpt4o-nov-warm (batch)` |
| served row 3.05, 2.03, 1.32, 2.76, 2.19, 1.39, 1.58; all seven | measured | 178 | same | same | row `gpt4o-nov-served` |
| bare row 5.39, 5.12, 4.34, 5.05, 20.49, 2.41, 8.64; all seven | measured | 178 | same | same | row `gpt4o-nov-bare` |
| bare at temperature 0: 4.70, 4.65, 4.26, 4.24, 26.23, 1.95, 6.09 | measured | 81 | same | same | row `gpt4o-nov-bare-greedy` |
| the ten-measure raw-means table, every cell | measured | 178 for the three full conditions, 81 for the control | same | `results/profiles/profile_<condition>.json` | `raw_means`, rounded to two decimals from the full-precision value: reply length `shape.words`, list items `markup.list_items`, headings `markup.headings`, questions per 100 sentences `punct.question_per100s`, questions asked back `think.questions_back`, hedges `tone.hedge_per1k`, contractions `lex.contractions_per1k`, "as an AI" `think.as_an_ai_per1k`, solve versus hold `think.solve_vs_hold`, holding phrases `think.hold_per1k`. `tables/raw_means_4o_and_nearest.csv` holds the same values at three decimals |
| "216 words", "four list items", "131 words", "half a list item", "two questions back", "three times the hedging", "a third longer", "drops the holding phrases by more than half", "one sentence in sixteen" | arithmetic from the row above | as above | same | same | 215.67; 4.14; 131.33; 0.54; 2.08; 17.67/5.71 = 3.1; 175.17/131.33 = 1.33; 0.86 against 2.21; 100/6.26 = 16 |
| the no-prompt row moved 20.49 on markup and 8.64 on thinking talk | measured | 178 | same | `results/ROSTER_vs_gpt4o-nov-warm.md` | row `gpt4o-nov-bare`, markup and think columns |
| only Claude Sonnet 4.6 exceeds 8.64 on the thinking-talk column | measured | 178 | same | same | the `think` column over the warm rows; `sonnet46-warm` 8.90 |
| 3.05 against 2.23 | measured | 178 | same | same | rows `gpt4o-nov-served`, `mistralmediumlocal-warm` |

## Section 05: the warm roster

| Figure | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| the warm table, all 29 rows and every family cell | measured | in the Prompts column of each row | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/ROSTER_vs_gpt4o-nov-warm.md` | the row whose label matches the public name in `tables/roster_provenance.csv`; HOW FAR and "set by" from `tables/how_far_all_anchors.csv`, anchor `gpt4o-nov-warm (batch)` |
| GPT-OSS 120B: three cells printed as "not reported" | measured (withheld) | 178 | same | `results/profiles/profile_gptoss120-warm.json` | `truncation_rate` 0.148; the values themselves are in the roster file |
| 2.23 is 2.2 times the unit and 1.9 times the control | arithmetic | 178 and 81 | same | as above | 2.23/1.0 = 2.2; 2.23/1.17 = 1.9 |
| the markup tail: 14.97, 15.25, 20.49, 21.99 | measured | 178 | same | `results/ROSTER_vs_gpt4o-nov-warm.md` | rows `dsv32think-warm`, `minimaxm3-warm`, `gpt4o-nov-bare`, `qwen38-warm`, markup column |
| hosted against local pairs: 2.66 / 2.23, 3.26 / 3.55, 7.74 / 7.31 | measured | 178 | same | same | rows `mistralmedium-warm`, `mistralmediumlocal-warm`, `mistralsmallapi-warm`, `mistralsmall-warm`, `qwen235api-warm`, `qwen235-warm` |
| temperature-0 rows: Mistral Small 4 3.51 (vocabulary), Gemma 4 26B MoE 6.75 (shape), Qwen3.8-27B 25.80 (markup) | measured | 81 | same | same; `tables/how_far_all_anchors.csv` | rows `mistralsmall-warm-greedy`, `gemma26moe-warm-greedy`, `qwen38-warm-greedy` |
| the Gemma temperature-zero row is the 32K build | measured | 81 | same | `results/profiles/profile_gemma26moe-warm-greedy.json` | `models` |

## Section 06: conversations and the behaviour panel

| Figure | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| the conversation table, all 28 rows and every family cell | measured | 48 in every row | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/ROSTER_scripts_vs_gpt4o-nov-warm.md`; `tables/how_far_all_anchors.csv` anchor `gpt4o-nov-warm (scripts)` | the row with the same label |
| the ChatGPT-style row: 1.23 tone, 1.02 shape, shape the only separating family at p 0.047 | measured | 48 | same | `results/comparisons_scripts.json` | entry `gpt4o-nov-served`: `band_units`, `p_holm`, `verdict_per_family` |
| five families inside the band, two above it | measured | 48 | same | same | `band_units`: punct 0.73, lex 0.80, markup 0.83, fw 0.91, think 0.61 inside; tone 1.23 and shape 1.02 above |
| Mistral Medium 3.5 local: shape and function words, one run per turn | measured | 48 | same | same; `tables/roster_provenance.csv` | entry `mistralmediumlocal-warm`; `runs_per_stimulus` 1.0 |
| Mistral Small hosted: tone only | measured | 48 | same | `results/ROSTER_scripts_vs_gpt4o-nov-warm.md` | row `mistralsmallapi-warm` |
| Mistral Large absent, below the minimum shared-turn count | measured | 20 (below the floor of 40) | same | `results/ROSTER_scripts_vs_gpt4o-nov-warm.md` | row `mistrallarge-bare`, "SMALL common set"; no `mistrallarge-warm` row |
| GPT-OSS 120B conversations: 95 replies | measured | 48 | same | `tables/roster_provenance.csv` | row `gptoss120-warm+scripts` |
| the Gemma conversation row is the 256K build | measured | 48 | same | `results/profiles/profile_gemma26moe-warm+scripts.json` | `models` |
| "most models at 6 to 8 in one-shot sit at 3 to 6 here" | measured | 178 and 48 | same | both roster files | compare rows by label |
| the behaviour panel, all 14 checks x three conditions | measured | 8 scripts, two runs each | same | `results/scripts_summary.json` | keys `gpt4o-nov-<condition> · <script>`: `caved_exact_words`, `corrects_premise`, `affirms_false_premise`, `fabricates_memory`, `honest_about_memory`, `offers_to_rebuild`, `accepts_apology`, `reaches_for_the_day`, `notices_contradiction`, `brevity_match_rate`, `breaks_the_bit`, `lists_advice_early`, `reassures_when_asked_not_to`, `meets_the_request` |
| the mirror check reads 0.00 in all three conditions | measured | same | same | `results/scripts_summary.json` | `held_boundary` |
| resolution 0 / 0.5 / 1; two runs per script | measured | 48 | same | `tables/roster_provenance.csv` | `runs_per_stimulus` 2.0 for `gpt4o-nov-*+scripts` |
| the withheld local Mistral Medium column reads the opposite of the hosted one on two checks | measured, not printed | 48 | same | `results/scripts_summary.json` | `mistralmediumlocal-warm · s01_boundary_push` and `· s04_confabulated_memory` against `mistralmedium-warm` |

## Section 07: the contrast anchors

| Figure | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| from Sonnet 4.6 warm: MiniMax M3 4.23, GLM-5.2 4.31, Qwen3-235B hosted 4.64, Qwen3.8 Max 4.70, Qwen3-235B local 4.90, DeepSeek V4 Flash 5.28, GPT-4o warm 13.00, Sonnet 5 warm 13.79 | measured | 178, except Sonnet 5 at 115 | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/ROSTER_vs_sonnet46-warm.md`; `tables/how_far_all_anchors.csv` anchor `sonnet46-warm (batch)` | rows `minimaxm3-warm`, `glm52api-warm`, `qwen235api-warm`, `qwen38max-warm`, `qwen235-warm`, `dsv4flash-warm`, `gpt4o-nov-warm`, `sonnet5-warm` |
| from Gemini 3 Flash warm: Qwen3.5-122B 3.36, Gemini 3.5 Flash 3.73, Gemma 4 31B QAT 4.12, GPT-4o warm 12.14 | measured | 178, except Gemini 3.5 Flash at 168 | same | `results/ROSTER_vs_gemini3flash-warm.md`; same CSV, anchor `gemini3flash-warm (batch)` | rows `qwen122-warm`, `gemini35flash-warm`, `gemma31qat-warm`, `gpt4o-nov-warm` |
| the asymmetry: 8.90 and 13.00; 7.93 and 12.14 | measured | 178 | same | `results/ROSTER_vs_gpt4o-nov-warm.md` and the two contrast roster files | rows `sonnet46-warm` and `gemini3flash-warm` from GPT-4o; row `gpt4o-nov-warm` from each contrast anchor |

## Sections 08 and 09

| Figure | Label | n | Run date | File | Field or row |
|---|---|---|---|---|---|
| truncation shares: GPT-OSS 56% and 15%, Mistral Large bare 20.7%, DeepSeek V4 Pro bare 16%, DeepSeek V4 Flash bare 11.7%, Qwen3.8-27B bare 11.5%, DeepSeek V3.2 bare 9.4% | measured | | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `results/profiles/profile_<condition>.json` | `truncation_rate`: 0.558, 0.148, 0.207, 0.161, 0.117, 0.115, 0.094 (`CAVEATS.json` rounds Mistral Large to 21%) |
| Monte Carlo standard error 0.9% to 5.4% | arithmetic | 178 | same | as section 03 | |
| partial rows: Sonnet 5 115, Mistral Large 165, Gemini 3.5 Flash 168 | measured | as stated | same | `tables/roster_provenance.csv` | `n_stimuli` |
| local runs one or two per prompt against the anchor's 2.69 | measured | | same | same | `runs_per_stimulus` |
| the plan described two temperatures; the captures show 0.7 and 479 replies per condition | measured (the plan document is not shipped; see README) | 178 | same | `tables/roster_provenance.csv` | `temperature` and `n_replies` for every non-Gemini batch row |
| the caveat file omits the Gemini temperature | measured | | 2026-09-04 to 05 | `capture/CAVEATS.json` | no temperature entry |
| the caveat file names the 32K Gemma tag; the profiles say 256K for two rows | measured | | same | `capture/CAVEATS.json`; `results/profiles/profile_gemma26moe-*.json` | caveat text against the `models` fields |

## Section 10: the maker's statements

| Figure | Label | n | Read on | Source | Note |
|---|---|---|---|---|---|
| GPT-4o retired from ChatGPT on 13 February 2026 | vendor | | 2026-09-15 | OpenAI's help-centre article on retiring GPT-4o and other ChatGPT models | not a file in this package |
| `gpt-4o-2024-11-20` not listed on the API deprecations page | vendor | | 2026-09-15 | OpenAI's API deprecations page | not a file in this package |
| `gpt-4o-2024-05-13` shutdown 23 October 2026 | vendor | | 2026-09-15 | same page | not a file in this package |

## Section 12: dates and counts

| Figure | Label | n | Run date | File | Field |
|---|---|---|---|---|---|
| 65 one-shot and 56 conversation conditions; 26 models | measured | | 3 to 5 Sep 2026, rebuilt 2026-09-05 | `tables/roster_provenance.csv` | `kind` counts; the distinct models behind the identifiers |
| 53 of 57 rows byte-identical between the two rebuilds | measured | | 2026-09-04 and 2026-09-05 | not shipped (see README) | the two `ROSTER_vs_gpt4o-nov-warm.md` files, compared row by row |
| about 32,000 replies not shipped | arithmetic | | same | `results/profiles/profile_*.json` | sum of `n` over the 121 files = 31,653 (the same sum over `n_replies` in `tables/roster_provenance.csv`) |
