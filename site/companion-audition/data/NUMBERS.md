# NUMBERS: every figure on the page, and where it lives in this package

The one place a file will look like it contradicts the page: exam A's "waited" figure on the page (21 of 99) is the
`waited_firm` column; the 27 doubtful-only answers are a separate column. Exam B's "waited" (30 of 60) counts any line.
The CSV column is the recorded figure. `NUMBERS.md` is a map of the page onto these files and does not outrank the page. If the page and a file here disagree, check the recorded run.

| Section | Figure on the page | File | Field or derivation |
|---|---|---|---|
| Subtitle | up to 80% (longer answer won) | `judges_length_bias_2026-09-25.csv` | round 2, judge A, would rather be: 80 |
| 02 | 14 items (A), 4 items (B) | `exam_answers_per_item.csv` | rows per exam |
| 02 | 51 / 134 / 3,074 / 3,484 / 286 / 124 | `exam_sizes.csv` | exam A, 2026-10-23 rebuild |
| 02 | 41 / 91 / 887 / 1,087 / 0 / 200 | `exam_sizes.csv` | exam B, 2026-10-23 rebuild |
| 02 | 105, 13, 5, 1; 135, 52, 10, 3; the 5 a 32K short check (newest 46 of 166 history messages, longer run kept); 3 from the same 32K short check (its longer run was kept); 0.06 tokens per second on a prompt of 122,880 tokens (R2 round) | `exam_sizes.csv` | `left_out_detail` |
| 02 | 180 fine-tune answers (four settings, 45 each, two 27B models) and 9 extra samples inside the 3,074 | `checks_and_reading.csv` | last two rows (R2 round) |
| 02 | coded subsets: 99; 60 and 60; 72 per condition | `coded_vs_kept.csv` | `coded_by_hand`, `coded_per_condition` |
| 02 | 46 and 2,860; 36 and 787 | `exam_sizes.csv` | 2026-10-22 first build rows |
| 02 | 4,515 = 3,264 + 981 + 270; 0 without a raw file; 0 of 3,933 misplaced (3,647 shown + 286 duplicates); 4,231 = 3,074 + 887 + 270 | `checks_and_reading.csv` | first four rows and the `expected raw files` row |
| 03 | 24 forms; 72 / 63 answers; 21 of the 24 forms asked the honesty items | `memory_traps.csv` | `answers` column, exam A (63 = 21 x 3) |
| 03 | note placement 19 / 2 / 1 / 2 of 24 forms | `note_placement_exam_a_traps.csv` | `model_forms_of_24` |
| 03 | 144 of 352; 144 of 349 (twice); 126 of 168; 126 of 156 | `coded_vs_kept.csv` | exam A trap rows |
| 03 | photo 17 → 3; 43 → 63; 12 → 6; no reply 0 → 0 | `memory_traps.csv` | photo that never happened, all four kinds |
| 03 | song 29 → 3; 22 → 49; hedges 12 → 11; no reply 0 → 0 | `memory_traps.csv` | song never played, exam A, all four kinds |
| 03 | user's line 17 → 20; 24 → 32; both 4 → 5; 27 → 15 | `memory_traps.csv` | real line of the user's, all four kinds |
| 03 | credited line 25 → 29; 40 → 30; unclear 7 → 12; no reply 0 → 1; accepts down 10, corrects up 4, unclear up 5 | `memory_traps.csv` | real line wrongly credited, all four kinds; differences |
| 03 | honesty real line: user 31 → 39; own 14 → 4; mixed 5 → 4; never said 13 → 16 | `memory_traps.csv` | real line asked about (honesty item) |
| 03 | exam B song: 53 per condition, 106 of 260 kept; goes along 33 → 3; hedges 16 → 6; no record 4 → 44 | `memory_traps.csv` | exam B rows |
| 04 | 18 local settings and 2 hosted models, 60 answers (of 136 kept); 31 / 23 / 6 | `harm_check_no_breaks_week_exam_b.csv`; `coded_vs_kept.csv` | ALL row; 18 local rows + one row of 2 hosted models |
| 04 | Flash-Next 2 of 3, GLM-4.7-Flash 2 of 3, Gemma 4 26B thinking off 1 of 3, Ling 1 of 3 | same | `goes_along` per row |
| 04 | 59 of 60 planned the week | same | ALL, `went_on_to_plan_the_week` |
| 05 | 5 of 99 asks how he is; 6 of 99 gap not mentioned | `return_message_exam_a_by_model.csv` | ALL row |
| 05 | exam A table (34 rows + All: 99 / 21 / 43 / 63 / 99 / 5 / 6); 99 of 197 kept; row labels now carry the model file, top_p 1.0 sent on both DeepSeek chat forms (V4.1: installed server default 0.95; V4 Flash: its server started at 1.0, min_p 0 sent against a server floor of 0.05), 6 of 8 experts and 131,072 on Qwen3-235B, installed 128K on V4.1 (R2 round) | same; `coded_vs_kept.csv` | every row; row labels as on the page |
| 05 | 27 doubtful-only answers | same | ALL, `waited_doubtful_only` |
| 05 | 19 of 34 forms with no firm "waited" | same | count of rows with `waited_firm` = 0 |
| 05 | Ling 3.0 Flash 3 of 3 waited | same | Ling row |
| 05 | exam B table (19 rows + All: 60 / 30 / 20 / 7 / 29); 60 of 218 kept | `return_message_exam_b_by_model.csv`; `coded_vs_kept.csv` | every row; row labels as on the page |
| 05 | 18 local model settings | same | rows other than the hosted row and ALL |
| 06 | round 1: A 77% of 189, 74% of 187; C 71% and 67%, each of 63, one run | `judges_length_bias_2026-09-25.csv` | round 1 rows; `runs in this round` row |
| 06 | round 2: A 74% and 80%, each of 189; B 76% and 72%, each of 189; C 53% of 188, 61% of 189 | same | round 2 rows |
| 06 | 100% at 2.5 times longer: of 30 (A), 12 (B), 18 (C) | same | `both` rows |
| 06 | 0.79 / 0.82 / 0.11 | same | Spearman rows |
| 06 | 68% to 74% self-agreement: A 70% of 374, 74% of 378; B 68% of 378; C 70% of 376 | same | run-to-run rows |
| 06 | round-to-round on identical texts: A 63% of 321; C 72% of 108 | same | round-to-round rows |
| 06 | 12 models: 7 candidates, 3 anchors, 2 decoys | `judges_round4_validity.json` | field described in `about`; the round's frozen plan |
| 06 | own answers 1st / 3rd / 9th | `judges_round4_2026-09-26.csv` | row 1 |
| 06 | other-family decoy 6th / 1st / 1st | same | row 2 |
| 06 | wrong-world decoy 12th / 10th / 12th; 9th to 12th across both framings | same | rows 3 and 4 |
| 06 | steadiness drops 8.3 / 12.9 / 13.7 and 10.6 / 12.1 / 19.5 | same | identical-repeat minus neighbours-changed, rows 5 to 8, in points |
| 06 | longer won 74% / 73%, 66% / 62%, 57% / 55% | same | rows 9 and 10, rounded |
| 06 | 313 of 324 calls; 11 lost, all judge C on one question; 814 / 792 vs 924 decisions; more than 2% missing, so the frozen script gave no table; about $68 by the design's estimate | `judges_round4_2026-09-26.csv` | calls rows, `decisions behind` rows, `frozen analysis output` row, cost row (design estimate; the provider's bill is the authority) |
| 07 | 320 sentences; 2 inventions | `checks_and_reading.csv` | exam B sentence and invention rows |
| 04 | about a dozen labels could move; 59 of 60 still planned the week | `harm_check_no_breaks_week_exam_b.csv` | ALL row, `went_on_to_plan_the_week` (the dozen is the readers' own caution in the round log, not a count) (round 3) |
| 07 | 31 / 23 / 6 (section 07 points back to section 04's caution) | `harm_check_no_breaks_week_exam_b.csv` | ALL row |
| 07 | 478 answers, 34 forms, five messages, 13 passes, 7,187 + 485 quotes, 0 failures, 16 damaged copies | same | exam A rows |
| 07 | 1,507 quotes over 271 entries | same | exam B rows |
| 02 (round 3) | exam B's 3 left-out answers are the same 32K short check (longer run kept) | `exam_sizes.csv` | `left_out_detail` |
| 02 (round 3) | the 9 extra answers: three slots, a second set of three samples each, one model's no-note run of three trap items | `checks_and_reading.csv` | extra-sample row |
| 05 (round 3) | row labels: record model names with active-size suffixes, files on every local row in both exams, Claude adaptive thinking, GPT-OSS 120B 131,072 and experts of 23 of 36 layers in RAM (now in the table note, for every 120B row; round 4), MXFP4_MOE, V4.1 7 October weights | `return_message_exam_a_by_model.csv`, `return_message_exam_b_by_model.csv`, `harm_check_no_breaks_week_exam_b.csv` | `model_form` / `model` labels (counts unchanged) |
| 05 (round 3) | 3 of Qwen3.8-27B's 5 kept exam B return answers and 1 Ling answer repeat an earlier reply | (not in a data file) | the exam B round log; see `../CLAIMS_TRACE.md` |
| Subtitle (round 4) | "Plain traps read by hand, and the judges that failed." then "The traps told models apart." | (title string) | the subtitle carries the rest of the `<title>` string after the short `h1` |
| 02, 05 (round 4) | top_p 1.0 sent to DeepSeek V4.1 Flash, installed server default 0.95; V4 Flash rows: top_p 1.0 sent, its server started at 1.0, min_p 0 sent, server floor 0.05 (both exams) | `return_message_exam_a_by_model.csv`, `return_message_exam_b_by_model.csv`, `harm_check_no_breaks_week_exam_b.csv` | row labels (counts unchanged) |
| 05 (round 4) | GPT-OSS rows: experts MXFP4, the rest F16 (stock 120B, 20B); Derestricted experts MXFP4, the rest Q8_0; every 120B row window 131,072, experts of 23 of 36 layers in RAM, batch 2048 | `return_message_exam_a_by_model.csv` | row labels and table note (counts unchanged) |
| 05 (round 4) | Qwen3.5-35B-A3B and Qwen3.6-35B-A3B: thinking off sent at temperature 0.7, top_p 0.8, cap 4,096; thinking on at 1.0, 0.95, cap 16,384; server starts differ from the requests: Qwen3.6-27B and Qwen3.6-35B-A3B at 1.0 / 0.95 / top_k 20 / min_p 0, Qwen3.5-35B-A3B at 1.0 / 1.0 / top_k 0, Qwen3.5-122B-A10B at 0.6 / 0.95, none with a presence penalty while every Qwen request sent presence_penalty 1.5; Gemma 4 26B-A4B start top_k 64, min_p floor 0.05, request min_p 0. Exam B Gemma 4 26B-A4B pair sampled alike (1.0 / 0.95 / top_k 64), caps 4,096 and 16,384; exam B Qwen3.6-27B, Qwen3.8-27B, Qwen3.5-397B thinking-off starts at 1.0 / 0.95 / top_k 20, requests 0.7 / 0.8 / presence 1.5 / cap 4,096; each result log records no server-added values | (not in a data file) | table notes; see `../CLAIMS_TRACE.md` round 4 |
| 06 (round 4) | the other-family decoy was heard at temperature 0.7, thinking off, answers cut to about 180 words | (not in a data file) | see `../CLAIMS_TRACE.md` round 4 |
