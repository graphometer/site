# NUMBERS: every figure on the page, and where it lives in this package

Where the page gives two times for one review (Gemma 4 31B: 83 seconds measured, 1 minute in the log's minute field;
Laguna S 2.1: 88 seconds in the strategy note, 2 minutes in the log and in `review_uses.csv`; DeepSeek V4.1 Flash: 56
minutes in the minute field, 54 minutes in the same entry's prose), both are recorded and `review_uses.csv` carries them
in `minutes` and `time_note`.

| Section | Figure on the page | File | Field or derivation |
|---|---|---|---|
| Title sentence (title, subtitle, og, twitter, image alt, cards, feed), 03 | best agent 74.0; 100.0 | `trim_job_scores.csv` | Flash-Next default row; row "+ no-model fixer" after the Qwen3.6-35B-A3B writer (outcome `scored`) |
| Lead, descriptions | 52.0 alone; 81.0 with one wrong archive, two open items lost, and one invented row when the file is scored again with the same scorer | same | Qwen3.6-35B-A3B writer row; Flash-Next pipeline fixer row, `wrong_archives` 1, `open_items_untraceable` 2, `invented_rows` 1 |
| 01 | 45 rows; 300 characters; one row done | `trim_job_scores.csv` | rows_kept + rows_archived = 45; `scoring_rules.csv` |
| 01 | 15 / 5 / 3 / 2 / 1.5 / 1 / 0.5 | `scoring_rules.csv` | points |
| 01 | planted draft 13 defects, 61.0; 2 wrong archives, 2 invented rows, 2 lost links counted; 5 dropped open items not scored | `trim_job_scores.csv` | control row (`open_items_untraceable` 0); the 13 and the 5 are the planter's counts |
| 01 | one ambiguous row cost several drafts 15 points | `trim_job_scores.csv` | the single wrong archive in the 85.0, 84.5, 84.0, 83.0 and 74.0 rows is the same row (its id is removed) |
| 02 | cloud 99.5 / 98.5 / 98.0 / 96.5 / 85.0 / 83.0 / 84.5 / 84.0 (1,261 s) / 47.0 (151 s); Grok's first effort-high run no file | `trim_job_scores.csv` | cloud rows |
| 02 | the 83.0 retry's wrong archive is the ambiguous row (the job note names it); the 85.0, 84.5 and 84.0 runs each have one wrong archive; 83.0 also has 1 lost link and 1 untraceable open item, 84.5 has 1 untraceable, 84.0 has 2 | same | `wrong_archives`, `links_lost`, `open_items_untraceable` on the hosted rows |
| 02 | every local agent row: seconds, score, and every non-zero penalty class | `trim_job_scores.csv` | matching rows |
| 02 | 74.0 then 60.0; a 14-point pair | same | Flash-Next rows |
| 02 | no-file rows: 590 s; 230 s; 1,091 s invalid; 408 s then 1,461 s; 2,102 s | same | outcome column |
| 03 | 52.0 / 52.0 / 92.5 / 100.0; 43.5 (12 of 45 rows fell back; 3 wrong archives, 2 invented rows, 3 lost links, 2 untraceable open items) / 73.5 (1 wrong archive, 2 invented rows, 3 lost links, 2 untraceable open items) / 81.0 (1 wrong archive, 1 invented row, 2 open items untraceable) | same | one-row-per-call rows; the fallback count is in the 43.5 row's `outcome` |
| 03 | voided fixer runs 95.5 and 100.0 | same | rows with outcome `void` |
| 03 | about 29 minutes | same | seconds 1,740 (approximate in the record) |
| 03 | 44 kept, 1 archived, 0 lost links, 0 over length; 240.3 characters in the job log, 240 in the job's summary table | same | 100.0 row, `avg_kept_row_chars` 240.3 |
| 03 | -51.5 as an agent | same | "Qwen3.6-35B-A3B, default" |
| 04 | every review row; union of two frontier reviews that disagree on severity; partial matches | `review_uses.csv` | matching rows; `reference` column |
| 04 | Gemma 4 31B: 83 seconds, minute field 1 | `review_uses.csv` | `minutes`, `time_note` |
| 04 | Laguna: 3 of 7 reference defects; 4 true and 2 false; 88 seconds; minute field 2 | `review_uses.csv` | `found`, `minutes`, `time_note` |
| 04 | DeepSeek V4.1: 56 (minute field), 54 (prose) | `review_uses.csv` | `minutes`, `time_note` |
| 05 | 32,000-token step; 590 s; three runs (two coder runs plus the trim-job run, 590.4 s) | `trim_job_scores.csv` (the trim-job run); the coder test's record (the two coder runs) | a lab record, not part of this package |
| 05 | temperature 0.7, top_p 0.8, top_k 20; the note of that test says 20 minutes (102 steps, 34 edits), the second round's note 24 minutes; no separate run timer is recorded; 53 of 53; five findings; 70 of 70 | (not in a data file) | the coder test record |
| 05 | over 10 minutes vs 6 to 30 seconds (checker) | (not in a data file) | the job's progress log |
| 05 | 24,000 tokens; 14,000-token cap; 7 of 7 | `review_uses.csv` | MiMo row; the cap is in the setting column |
| 05 | HTTP 500; 2 turns; 39 seconds | (not in a data file) | the shim probe record |
| 05 | Gemma 4 31B: three of three first answer with thinking on; without, two of three eventually, one of three first answer | `fix_test.csv` | Gemma 4 31B rows, `attempt_that_passed` |
| 05 | 2,000 characters; 9 of 45 rows; 214 tool calls; 1,500 characters | (not in a data file) | the job's progress log |
| 05 | 8,192 cap; raised to 32,768, still unfinished at the 32,000 harness maximum; the other writers needed about 14,000 output tokens | `trim_job_scores.csv` (the caps and outcomes); the job's progress log, line 217 (the 14,000) | Laguna rows |
| 06 | fix table: solved, retries, time ranges; thinking on, 64,000 tokens, no sampling fields | `fix_test.csv` | per model; ranges are min to max of `seconds`; `setting` |
| 09 | file sizes and quantizations, model list as of 2026-10-25, not per-run file names; GPT-OSS copy deleted 11 Oct, restored 15 Oct | (not in a data file) | the lab's model roster as of 2026-10-25 |
| 09 | OpenCode 1.18.35; Claude Code 2.1.296 | (not in a data file) | the job's progress log; drivers note |
| 02 | Flash-Next repeat named in the opener; Vibe retry 83.0 at 60 turns and $3, 254 s; both Codex scores at effort high (84.5, 47.0); the 83.0 retry's wrong archive is the ambiguous row; 74.0's wrong archive is that row | `trim_job_scores.csv` | Vibe retry row (254, 83.0); Codex rows; `wrong_archives` 1 on 85.0 / 84.5 / 84.0 / 83.0 / 74.0 (row id removed; the job note names it for the 83.0 retry) |
| 02 | GPT-OSS 120B ran twice: high effort −45.5, seconds blank; 416 s and 136 s from a note at the end of those runs | `trim_job_scores.csv` | high-effort row (seconds blank) and the "medium effort (its default)" no-file row (seconds blank); the 416 and 136 are not in a data file, a lab record, not part of this package |
| 03 | 52.0 rows: 3 wrong archives, 1 mangled row (100 − 45 − 3) | `trim_job_scores.csv` | Qwen3.6-35B-A3B writer and same-model rows |
| 03 | 81.0: job note's breakdown sums to 84 (100 − 15 − 1); the score file also has one invented row (−3). The job note does not name that class | `trim_job_scores.csv` | Flash-Next fixer row: `wrong_archives` 1, `invented_rows` 1, `open_items_untraceable` 2 |
| 04 | security GLM one false pass; 76 KB GLM one miss; DeepSeek 76 KB counter 1 miss; M2.7 counter 3 misses | `review_uses.csv` | `false_passes`, `misses` |
| 04 | one confident all-clear (MiniMax M2.7) | `review_uses.csv` | `false_all_clears` 1 on that row only |
| 04 | three omitted 10 October reviews: 1 / 1 / 1 in 8 min; 1 false pass, 0 misses, 39 s (minute field 1); 1 miss, 1 false alarm, 32 min | `README.md` | file table, `review_uses.csv` row (counts only; the reviews are not in a data file) |
| 05 | 20 minutes (102 steps, 34 edits); 24 minutes for the second round | (not in a data file) | the note of that test |
| 05 | Gemma 4 26B-A4B with thinking off solved one of three | `fix_test.csv` | 26B-A4B "no thinking switch sent" rows |
| 05 | 8,192 then 32,768 in the OpenCode config; harness maximum 32,000, answer still unfinished; the other writers needed about 14,000 output tokens | `trim_job_scores.csv` (the caps and outcomes); the job's progress log, line 217 (the 14,000) | Laguna rows |
| 06 | three tasks in two files; the third edits two functions; Sonnet effort high, no tools | `fix_test.csv` | Sonnet `setting`; task scope not in a data file, a lab record, not part of this package |
| 09 | GLM-5.3-Flash build split: 10 October and 01:01 reviews on the previous build; 06:51 on 11 October first on the later one | (not in a data file) | the testing log |
| 01 | 13 planted: 5 dropped open items, 3 invented facts, 3 lost links, 2 wrong archives; one planted invented fact and one planted lost link left no penalty | `trim_job_scores.csv` | control row (`invented_rows` 2, `links_lost` 2); the planted counts are the planter's |
| 02 | Opus at effort medium; both Sonnet runs at effort high | `trim_job_scores.csv` | cloud rows, `model_and_setting` |
| 03 | 92.5: 1 invented row, 1 mangled row, 1 lost link; 100.0 average 240.3 in the job log, 240 in the job's summary table | `trim_job_scores.csv` | `invented_rows`, `mangled_rows`, `links_lost` on the 92.5 row; `avg_kept_row_chars` 240.3 on the 100.0 row |
| 04 | Qwen3.8-27B security review: two false passes | `review_uses.csv` | `false_passes` 2 |
| 04 | DeepSeek V4.1: 56 (minute field), 54 minutes (prose) | `review_uses.csv` | `minutes`, `time_note` |
| 09 | the note kept with the GPT-OSS run names an F16 file; 65.4 GB is the model list's later size | (not in a data file) | a lab record, not part of this package |
| 03 (round 4) | 43.5 and 73.5 classes: wrong archives from each run's result file (3 and 1); invented 2, lost links 3, untraceable 2 from the score table; the job note does not name those classes | `trim_job_scores.csv` | Flash-Next writer and same-model rows: `wrong_archives`, `invented_rows`, `links_lost`, `open_items_untraceable` |
| 03 (round 4) | Qwen3.6-35B-A3B looking again: 52.0 stays 52.0; Qwen3.8-Flash-Next looking again: 43.5 to 73.5 | `trim_job_scores.csv` | the two "+ same model looks again" rows |
| 02 (round 4) | Inkling-Small, reasoning effort set to none | `trim_job_scores.csv` | Inkling row, `model_and_setting` |
