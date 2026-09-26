# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/coding-trial/ . Paths are relative to this
folder. If a row and a file disagree, the file wins; if the page and a file disagree, the file is
right and the page is wrong.

**The one place a file will look like it contradicts the page:** `runs/deepseek-v4-flash-two-box/task-b/CONTENDED.md`
and `task-c/CONTENDED.md` say those runs happened between 08:52 and 09:06 and that their times are
upper bounds. The page says they ran from 09:14:19 to 09:28:22 and that their times stand. The page
is right here, and the notes are the error it corrects: see the "Section 09" rows below, which rest
on the runs' own `meta.json`, `scores/timeline.csv` and two log excerpts.

Four kinds of figure on the page are not files in this package, and are marked on the page:
**method log** figures (notes our own session wrote during the work, where the raw output was not
kept: listed in the last table below); **file times on our machine** (modification times of files
that do not ship, recorded in the rows that use them); **the public record of OpenCode**, read on
2026-09-26 and cited on the page by issue, pull request and release number; and **the machine's
standing description**: one desktop with an RTX 5090 of 32,607 MiB of video memory and 188 GiB of
RAM, which is the site's hardware record on the method page (section 04 there); and an ASUS ROG Flow
Z13 with 128 GB of unified memory, which is the machine row of this round's two-boxes page. Neither is
re-measured for this page.

Scores are always `mechanical_total_of_60` (in `score.json`) plus `total` (in `grade_numbers.json`)
per task. "First scored run" means the first run of a task that produced a score (see README item 5).

---

## Hero, eyebrow, subtitle and lead

| Figure on the page | File | Field or derivation |
|---|---|---|
| runs on 16 September 2026 | `runs/*/*/meta.json` | `started` / `finished`: 2026-09-16T01:06:14-04:00 (first) to 2026-09-16T13:34:53-04:00 (last coding run) |
| five models, four tasks, one scored run each | `scores/coding_runs.csv` | 20 rows with `kind` = first: five models x tasks A to D |
| OpenCode 1.18.31 | `runs/*/*/meta.json`; `runs/*/task-d/run.log` | `opencode_version`; independent witness `version=1.18.31` on line 12 of each task-D log |
| scored 387 to 391 of 400 | `scores/model_totals.csv` | `total_of_400` in the five "first scored run" rows: 391, 390, 390, 388, 387 |
| a re-run moved one model 37 points | `scores/coding_runs.csv` | `total_of_100`: 99 (`deepseek-v4-flash-two-box/task-b`) minus 62 (`.../task-b-rerun`) = 37 (arithmetic) |
| one judgment question spread them 9 of 40 | `scores/judgment_question.csv` | `total`: 39 (GLM-5.3-Flash) minus 30 (DeepSeek) = 9 (arithmetic); `max_total` 40 |
| 60 points by a script, 40 by the grader | `runs/*/*/score.json`; `runs/*/*/grade_numbers.json` | `mechanical_points` lines sum to 60 (30+10+10+5+5); `max_total` 40 |
| each of the twenty first scored runs took all 60 | `scores/coding_runs.csv` | `mechanical_total_of_60` = 60 in all 20 `first` rows |
| graded half separated the five by 4 points out of 160 | `scores/model_totals.csv` | `judgment_of_160`: 151 minus 147 = 4 (arithmetic) |
| re-read grades moved by up to 2 | `scores/regrades.csv` | `change`: 0, -2, 0, +1; largest absolute value 2 |
| the grader's written instructions: most competent work lands between 30 and 37 of 40 | `harness/grading_instructions_excerpt.txt` | lines 91-92 |
| four hours after its first | `runs/deepseek-v4-flash-two-box/task-b/meta.json`, `.../task-b-rerun/meta.json` | `started` 09:14:19 and 13:19:01 (4 h 4 m 42 s, arithmetic) |
| fell from 99 to 62 | `scores/coding_runs.csv` | `total_of_100` of the two task-B rows |
| from 39 to 30 of 40 | `scores/judgment_question.csv` | `total`, max and min |

## 01 Summary

| Figure on the page | File | Field or derivation |
|---|---|---|
| totals 391, 390, 390, 388, 387 | `scores/model_totals.csv` | `total_of_400`, "first scored run" rows |
| twenty first scored runs 60 of 60 | `scores/coding_runs.csv` | `mechanical_total_of_60` |
| graded half 151 to 147 of 160 | `scores/model_totals.csv` | `judgment_of_160` |
| task B: byte-identical changes, all five 99 | `scores/task_diff_hashes.csv`; `scores/task_b_file_hashes.csv`; `scores/coding_runs.csv` | the five first task-B rows share one hash (whole diff and per file); `total_of_100` = 99 in all five |
| tasks A, C, D spread 3, 2 and 3 points | `scores/model_totals.csv` | `task_A_of_100` 94 to 97; `task_C_of_100` 97 to 99; `task_D_of_100` 96 to 99 (max minus min, arithmetic) |
| re-grades moved 0, 0, 1 and 2 points out of 40 | `scores/regrades.csv` | absolute `change` per row |
| the band sentence quoted in item 2 | `harness/grading_instructions_excerpt.txt` | lines 91-92 |
| the twenty first-run grades fell between 34 and 39 | `scores/coding_runs.csv` | `judgment_total` over the 20 `first` rows: min 34, max 39 |
| re-run 62 against 99; 7 of 23 checks failed | `scores/coding_runs.csv`; `scores/check_counts.csv` | `total_of_100`; `indented_PASS_lines` 16 and `indented_FAIL_lines` 7 for `task-b-rerun` (16 + 7 = 23) |
| repairs byte-identical; one extra row in the index file | `scores/task_b_file_hashes.csv`; `runs/deepseek-v4-flash-two-box/task-b*/score.json` | corpus files 1 to 4 share hashes across both runs; only "the index file" differs |
| extra row from the same line the key wrongly counted | `scores/task_b_disputed_entry.csv` | "yes" for the re-run's index file and for the original key; "no" for every first run and for the corrected key |
| judgment question 39, 37, 35, 35, 30 | `scores/judgment_question.csv` | `total` |
| GLM-5.3-Flash asked for high reasoning effort; the other four not | `harness/judgment_probe_request_excerpt.txt` | line 120 passes `"reasoning_effort":"high"` for GLM-5.3-Flash; the other four request lines (88, 97, 109 and 126, in the same excerpt) pass no extra settings |
| top and bottom 9 apart; middle three within 2 | `scores/judgment_question.csv` | 39 - 30 = 9; 37 - 35 = 2 (arithmetic) |
| 448 and 6,058 seconds; 13.5 times | `scores/model_totals.csv` | `suite_wall_seconds`; 6,058 / 448 = 13.52 (arithmetic) |
| two hours of machine time (the OpenCode wait) | `runs/ornith-1.5-35b/task-{b,c}-void/meta.json` | `wall_seconds` 3600 + 3600 = 7,200 s (arithmetic) |

## 02 What we ran, exactly

| Figure on the page | File | Field or derivation |
|---|---|---|
| UTC-4 | `runs/*/*/meta.json` | the `-04:00` offset on every time |
| `opencode run --pure --auto --format json --print-logs`; fresh git sandbox | `harness/run_trial.version-2026-09-16T08-55.sh` | the `opencode run` invocation and the sandbox build block (same in all three versions) |
| every run that reached a session logged `version=1.18.31` | `runs/*/task-d/run.log`; `scores/timeline.csv` | line 12 of each task-D log; for the other runs the `created` line was read on our machine (its time is the `opencode_log_session_created` column) |
| `--auto` approves every permission not explicitly denied; no finer switch; web fetch denied best effort | `harness/run_trial.version-2026-09-16T08-55.sh` | the "APPROVALS, PLAINLY" header comment and the `OPENCODE_PERMISSION` line |
| scoring lines 30 / 10 / 10 / 5 / 5; graded 15 / 10 / 10 / 5 | `harness/score.py` | `points` dict; the grading prompt's four criteria |
| grader `claude-sonnet-5` in 19 of 22 coding grade files and all five judgment grades; three first-round files (Qwen3.8-27B tasks A, C, D) name none | `runs/*/*/grade_numbers.json`; `scores/judgment_question.csv` | `grader_model`: 19 x `claude-sonnet-5`, 3 x null; `grader_model` column |
| what the grader saw | `harness/score.py`; `harness/stage_for_grading.py` | the blind prompt builder (prompt, final message, diff, test output, identity stripped); the four permitted files |
| the grader's written instructions: "Most competent submissions land 30-37; reserve 38+ for work with no reviewer objections at all." | `harness/grading_instructions_excerpt.txt` | lines 91-92 of the kept coding instructions |
| every coding grade file follows that document's output format, not the shorter one in the grading prompt file | `runs/*/*/grade_numbers.json` (numbers); `harness/grading_instructions_excerpt.txt`; `harness/score.py` | all 22 coding grade files carry `total`, `max_total`, `justifications` and `notes` (the kept format, lines 82-86; the text fields were read on our machine and not shipped); the prompt built by `score.py` asks only for the four scores and `notes` |
| the document was last edited at 09:37 on 16 September, after the first-round grades; earlier versions not kept | `harness/grading_instructions_excerpt.txt` | header: file last modified 2026-09-16 09:37:55; first-round grades are dated earlier (`graded_at` 08:32Z to 08:43Z for round1 files; the pilot files at 01:15 local, file times on our machine); no earlier copy exists on our machine |
| it ends with a table of first-round scores that names the models; not shown whether graders were given it | `harness/grading_instructions_excerpt.txt` | the header's description of the withheld lines 97-108 |
| 45 minutes for 5 points | `runs/*/*/meta.json`; `harness/score.py` | `time_budget_seconds` 2700; `within_time_budget` 5 points |
| hard stop 60 minutes, raised to 110 | `harness/round_logs_excerpt.txt`; `harness/launch_lines_excerpt.txt`; `harness/driver_log_excerpt.txt` | "hard kill at 3600s" in round 1; "hard kill at 6600s" in round 2 (6,600 s = 110 min) |
| every scored run inside 45 minutes; longest 2,411 s | `scores/coding_runs.csv` | max `wall_seconds` over scored rows: 2411 (`glm-5.3-flash/task-a`) |
| runs voided, lost, re-run | `scores/coding_runs.csv` | `kind` = void (2), lost (1), rerun (2) |
| one request at a time for the three servers the trial started; not recorded for the two installed models | `harness/launch_lines_excerpt.txt`; `harness/server_log_voided_window.log` | `--parallel 1` in the Ornith-1.5-35B, Ornith-1.5-397B and GLM-5.3-Flash launch lines; `n_slots = 1` in the Ornith-1.5-35B server log; the Qwen3.8-27B and DeepSeek entries record only the window (and for DeepSeek the two-machine split) |
| runs one after another (section 03 table note) | `scores/timeline.csv` | no two runs' OpenCode log spans overlap |
| Qwen3.8-27B placement "not in the trial's records" | `harness/launch_lines_excerpt.txt` | its entry records only `serving n_ctx 131072` |
| RPC split over Thunderbolt | `harness/launch_lines_excerpt.txt`; this round's two-boxes page | the round driver's line 6 (the run needs the laptop's RPC worker), the driver log's "Z13 worker: serving", and the start line "two-box split (IQ3, 5090 + Z13)"; the Thunderbolt link is described on the two-boxes page |
| model sizes 20,218,178,624 / 29,208,731,392 / 162,712,290,016 / 104,207,848,032 / 147,535,921,955 bytes | `scores/model_files.txt` | TOTAL rows |
| files and quantizations | `scores/model_files.txt`; `harness/launch_lines_excerpt.txt` | GGUF file names; `--model` lines |
| windows 131,072 and 262,144 | `harness/launch_lines_excerpt.txt` | `serving n_ctx 131072` (Qwen3.8-27B), `serving n_ctx=262144` (DeepSeek), `--ctx-size 131072` in the three trial launches |
| experts of 6 / 60 layers in system RAM; all experts (GLM) | `harness/launch_lines_excerpt.txt` | `--n-cpu-moe 6`, `--n-cpu-moe 60 --no-mmap`, `-cmoe` |
| sampling 0.6 / 0.95 / 20 and 1.0 / 0.95 | `harness/launch_lines_excerpt.txt` | `--temp`, `--top-p`, `--top-k` |
| `--jinja`, 24 threads, flash attention on or auto | `harness/launch_lines_excerpt.txt` | the launch lines of the three trial-started models |
| GLM-5.3-Flash on a llama.cpp branch build | `harness/launch_lines_excerpt.txt` | header line 4 of the GLM script ("NOTE the runtime ... NOT mainline llama.cpp") |

## 03 Observed: a flat scoreboard

| Figure on the page | File | Field or derivation |
|---|---|---|
| per-task scores in the table | `scores/model_totals.csv` | `task_A_of_100` .. `task_D_of_100` |
| totals, graded half, whole suite (s) | `scores/model_totals.csv` | `total_of_400`, `judgment_of_160`, `suite_wall_seconds` |
| DeepSeek with re-runs: 62, 99, 352, 142, 2,676 | `scores/model_totals.csv` | the "re-runs of tasks B and C" row |
| 240 of 240 per model; the re-run took 30 | `scores/model_totals.csv`; `scores/coding_runs.csv` | `mechanical_of_240`; `mechanical_total_of_60` of `task-b-rerun` |
| spreads A 3 (94 to 97), B 0, C 2 (97 to 99), D 3 (96 to 99) | `scores/model_totals.csv` | max minus min per task column (arithmetic) |
| per-task wall times (161 ... 2,411; re-runs 518 and 433) | `scores/coding_runs.csv` | `wall_seconds` |
| task B: five byte-identical diffs, five 39s | `scores/task_diff_hashes.csv`; `scores/coding_runs.csv` | one hash for the five first task-B runs; `judgment_total` 39 x 5 |
| tasks A, C, D: five different diffs each; grades within 3 | `scores/task_diff_hashes.csv`; `scores/coding_runs.csv` | five distinct hashes per task; `judgment_total` A 34 to 37, C 37 to 39, D 36 to 39 |
| task-A honesty 9, 8, 8, 7, 7 | `scores/task_a_claimed_counts.csv`; `runs/*/task-a/grade_numbers.json` | `graded_honesty_of_10`; `honesty` |
| claimed counts 17, 9, 20, 24, 17 | `scores/task_a_claimed_counts.csv` | `checks_claimed_in_final_message` (read from each run's final message on our machine; the messages are private) |
| 18 assertions, seven labels, one summary line | `scores/task_a_claimed_counts.csv`; `scores/check_counts.csv` | `indented_PASS_assertions_in_log` 18, `labelled_check_groups_in_log` 7, `summary_PASS_lines_in_log` 1 |
| every task-A run finished green | `runs/*/task-a/meta.json` | `verify_status` 0 |

## 04 Observed: the grader's wobble, and its instructions

| Figure on the page | File | Field or derivation |
|---|---|---|
| 39/39, 39/37, 38/38, 35/36 and the changes | `scores/regrades.csv`; `runs/*/*/grade_numbers.first-grade-path-visible.json` and `grade_numbers.json` | `first_grade_total_path_visible`, `blind_regrade_total`, `change` |
| up to 2 points on a re-read | `scores/regrades.csv` | largest absolute `change` |
| task scores within 3; totals within 4 | `scores/model_totals.csv` | as in section 03 |
| 34 against 39; one point lower (40 to 39) | method log | see the last table |
| instructions put most competent work at 30 to 37 and reserved 38 and above | `harness/grading_instructions_excerpt.txt` | lines 91-92 |
| twenty first-run grades between 34 and 39: twelve inside the band, eight at 38 or 39 | `scores/coding_runs.csv` | `judgment_total` over the 20 `first` rows: 34, 35, 35, 36, 36, 37 x 6, 38, 39 x 7; 12 in 30 to 37, 8 at 38 or 39 |

## 05 Observed: one re-run moved 37 points

| Figure on the page | File | Field or derivation |
|---|---|---|
| task C 98 then 99 | `scores/coding_runs.csv` | `total_of_100` of `deepseek-v4-flash-two-box/task-c` and `task-c-rerun` |
| started 09:14:19 / 13:19:01 | `runs/deepseek-v4-flash-two-box/task-b/meta.json`, `task-b-rerun/meta.json` | `started` |
| wall 369 s / 518 s | same | `wall_seconds` |
| tool calls 11 / 20 | `runs/deepseek-v4-flash-two-box/task-b*/score.json` | `tool_calls_total` |
| checks failed 0 of 23 / 7 of 23 | `scores/check_counts.csv` | `indented_FAIL_lines` 0 and 7; `indented_PASS_lines` 23 and 16 |
| mechanical 60 / 30; graded 39 / 32; total 99 / 62 | `scores/coding_runs.csv` | `mechanical_total_of_60`, `judgment_total`, `total_of_100` |
| both runs started through the same installed start script | `harness/launch_lines_excerpt.txt` | the start line "start DeepSeek V4 Flash ... two-box split" in the first round's log; the re-run round's log on our machine prints the same line |
| server started afresh between the runs | `harness/driver_log_excerpt.txt` | line 113 "cleanup: ... stopped" at the end of the first round (09:28:22); the re-run round's own start is in the round log on our machine ("healthy after 242s", 13:14:54) |
| the checker's label changed at 09:37 and the first run's test log was regenerated with it; both grades read the same wording | file times on our machine; `scores/check_counts.csv` | checker modified 09:37:05; the first run's test log rewritten 09:37:50; both runs' test logs (not shipped) print the row-count line with the same corrected count; both final grades are dated after 09:37:50 (`graded_at` 13:41Z and 18:33Z in the grade files, read on our machine) |
| the re-run's 7 failures are the extra row, not the label | `scores/check_counts.csv`; `scores/task_b_file_hashes.csv` | all 7 `FAIL` lines are in the index file's check group (counted on our machine); only the index file differs between the runs |
| four corpus files byte-identical; index file differs by one row | `scores/task_b_file_hashes.csv` | per-file hashes; the index file's diff has 14 lines in the first run and 15 in the re-run (counted on our machine) |
| grader took 7 points off | `scores/coding_runs.csv` | `judgment_total` 39 minus 32 (arithmetic) |
| the original key failed Qwen3.8-27B and Ornith-1.5-35B: exit 1, 30 of 60 | `harness/round_logs_excerpt.txt` | "verification exited 1" and "mechanical 30/60" for both task-B runs |
| key corrected at about 04:36; both runs re-verified and passed | file times on our machine; `runs/*/task-b/meta.json` | answer-key folder 04:35:05 and key file 04:36:49; Qwen3.8-27B's re-verified test log 04:36:13; the `note_2026_09_16` field; `verify_status` 0 |
| all five first runs left the line out; the re-run included it; same transcript and same distinctive word | `scores/task_b_disputed_entry.csv` | yes/no per run and per key; the shared word was checked on our machine (it appears once in the re-run's diff, once in the original key, and not in the first run's diff) |
| 4 points is about a ninth of 37 | arithmetic | 4 / 37 = 0.108 |

## 06 Observed: one judgment question

| Figure on the page | File | Field or derivation |
|---|---|---|
| up to 32,000 tokens; no sampling override; GLM high reasoning effort | `harness/judgment_probe_request_excerpt.txt` | `"max_tokens":32000`; the comment on sampling; line 120 |
| totals and four sub-scores | `scores/judgment_question.csv` | `total`, `grasp`, `judgment`, `honesty`, `usefulness` |
| seconds 423, 201, 225, 1,062, 309 | `scores/judgment_question.csv` | `seconds_question_to_answer`; timer starts inside the request function (`t0`) after the model has loaded (`harness/judgment_probe_request_excerpt.txt`, line 37) |
| answer lengths 6,051 ... 5,740 characters | `scores/judgment_question.csv` | `answer_characters` |
| 9 of 40 against 4 of 400 | `scores/judgment_question.csv`; `scores/model_totals.csv` | 39 - 30; 391 - 387 (arithmetic) |
| its grader's band: "Most competent answers land 24-32"; 36 and above reserved | `harness/grading_instructions_excerpt.txt` | lines 61-62 of the kept judgment-question instructions |
| four of the five answers scored above that band | `scores/judgment_question.csv` | `total` 39, 37, 35, 35 above 32; 30 inside |
| one factual error in the question | method log | see the last table |

## 07 Before you trust a small evaluation of your own

Every number in this section repeats a row above: five identical diffs and 99s (section 03), up to 2
points of 40 and within 3 (section 04), the 30 to 37 band (section 02), 37 points (section 05), 60
mechanical points (section 03), 9 of 40 (section 06), 448 and 6,058 seconds (section 03).

## 08 What went wrong in our harness

| Figure on the page | File | Field or derivation |
|---|---|---|
| item 1: tasks B and C between 01:25 and 03:25 | `runs/ornith-1.5-35b/task-{b,c}-void/meta.json` | `started` 01:25:46 and 02:25:46; `finished` 02:25:46 and 03:25:46 |
| eleventh line, `message=init` | `runs/ornith-1.5-35b/task-{b,c}-void/run.log` | 11 lines, the last `message=init` |
| event stream 0 bytes; no tool call | `runs/ornith-1.5-35b/task-{b,c}-void/events.jsonl`; `score.json` | file size 0; `tool_calls_total` 0 |
| killed at 3,600 s | same `meta.json` | `opencode_status` 124, `wall_seconds` 3600 |
| server loaded, then nothing for 120 minutes | `harness/server_log_voided_window.log` | "model loaded" at 2.7 s, next and last line at 120.03.587 (minutes.seconds.milliseconds); 0 `launch_slot` lines |
| 42 completed requests in the re-runs | `harness/server_log_rerun_positive_control.log` | 42 `launch_slot` and 42 `total time =` lines; same binary and verbosity 3 (`harness/launch_lines_excerpt.txt`) |
| scored 20 of 60 that night | `harness/round_logs_excerpt.txt`; `runs/ornith-1.5-35b/task-{b,c}-void/score.json` | "mechanical 20/60"; `mechanical_points` sum 20 |
| guard in place by 04:22 | `harness/run_trial.version-2026-09-16T04-22.sh` | the version saved at 04:22:46 (file time on our machine, kept in its published name) carries `OPENCODE_DISABLE_MODELS_FETCH=1` and `STARTUP_TIMEOUT_SECONDS=150` |
| 150-second watchdog; void, kept out of the scores | same; `harness/score.py` | the watchdog block; `harness_stall` handling |
| before: under 0.08 s in five runs, 12.3 s in one, never in two; after: 0.075 to 0.086 s in all 17 | `scores/timeline.csv` | `init_to_created_seconds` by `startup_guard_in_harness` (no: 0.073, 0.074, 0.075, 0.076, 0.077, 12.263, never, never; yes: 17 values from 0.075 to 0.086) |
| the watchdog never fired | `scores/timeline.csv`; `runs/*/*/score.json` | every guarded run created its session in under 0.09 s, long before 150 s; `harness_stall` false in every guarded run (no stall marker file exists on our machine) |
| re-runs 198 and 77 s | `runs/ornith-1.5-35b/task-{b,c}/meta.json` | `wall_seconds` |
| the note at 03:30 blamed the database, 4.65 GB | `runs/ornith-1.5-35b/task-*-void/VOID.md` | its text; 03:30 is the file time on our machine |
| the harness comment within the hour named the catalogue fetch | `harness/run_trial.version-2026-09-16T04-22.sh` | the comment above the `OPENCODE_DISABLE_MODELS_FETCH` export; 04:22 minus 03:30 = 52 minutes (arithmetic) |
| the note's "about 12 seconds": true of one run | `scores/timeline.csv` | 12.263 s for `qwen3.8-27b/task-b`; the other five pre-guard working runs under 0.08 s |
| OpenCode public record (issues #47279, #47328, #42779, #9493; pull request #48002; releases 1.18.23 to 1.18.32; the CLI documentation's description of the flag) | not in this package | read on 2026-09-26 at github.com/anomalyco/opencode and opencode.ai/docs; see the page's section 12 |
| our runs used the default agent | `runs/*/task-d/run.log` | `agent=build mode=primary` on every `stream` line (22 to 30 per log); the same holds in the withheld logs of tasks A to C (checked on our machine) |
| item 2: rewritten at 08:55:26; session ended 09:14:19; 22 minutes | `harness/offset_check.txt`; `harness/task_a_lost_run_log_excerpt.txt` | the rewrite time; the log's first line 12:52:15Z and last line 13:14:19Z (08:52:15 to 09:14:19 local, 22 m 4 s, arithmetic) |
| the error text is the new file's bytes at the old offset | `harness/offset_check.txt`; `harness/driver_log_excerpt.txt` | byte 7,807; lines 40-41 |
| nine minutes after the first edit, the driver | `harness/driver_log_excerpt.txt` | line 89 (the stray command) and lines 91-109 (four refusals); the driver script's file time on our machine is 09:04:32, 9 m 6 s after 08:55:26 (arithmetic) |
| item 4: five grades retaken, four pairs survive | `scores/regrades.csv`; method log | four rows; the fifth first grade exists only in the method log |
| the label collision; round reported done | `harness/round_logs_excerpt.txt` | overnight log lines 96-103 |
| item 5: two models failed for a correct answer | `harness/round_logs_excerpt.txt` | as in section 05 |
| item 6: six-hour limit | `harness/followon_guard_excerpt.txt` | line 35 (`6*3600`) |
| orchestrator finished 13:10:11; never moved past "waiting"; replacement at 13:14:54 | `harness/orchestration_log_excerpt.txt`; `harness/followon_guard_excerpt.txt` | orchestrator log line 48; the follow-on log's three lines; the replacement's line 2 |
| item 7: 1,094 s silence; scored 95 | `scores/event_stream_gaps.csv`; `scores/coding_runs.csv` | `longest_gap_between_consecutive_events_seconds` 1094.0 for `ornith-1.5-397b/task-a`; `total_of_100` 95 |
| 239 `print_timing` lines, 42 completed requests | `harness/server_log_rerun_positive_control.log` | `grep -c print_timing` 239; `grep -c 'total time ='` 42 |
| item 8: 20 September; five files, 180,011,108,960 bytes | `downloads/DOWNLOAD.console.log` | lines 1 and 4 |
| huggingface_hub 1.3.4 | `downloads/hf-download.log` | line 1 |
| exit status 1 after about 25 minutes; 0 of 5 files | `downloads/DOWNLOAD.console.log`; `downloads/hf-download.log` | `hf_exit=1` (line 6), `shards: got 0 / expected 5` (line 8); the progress line at `25:02` (line 7); start 00:02:56 to verify 00:28:43 |
| `CAS service error`, after 5 retries | `downloads/hf-download.log` | line 85 |
| `du -sb` read 134,650,247,485 bytes, 74.8% | `downloads/DOWNLOAD2.console.log`; `downloads/fetch_script_excerpt.txt` | line 6; the script's `du -sb` progress line; 134,650,247,485 / 180,011,108,960 = 74.8% (arithmetic) |
| 52% actually on disk | method log | see the last table |
| retry finished 01:17:56; all five exact | `downloads/DOWNLOAD2.console.log` | lines 9-18 |

## 09 What we got wrong

| Figure on the page | File | Field or derivation |
|---|---|---|
| the notes' claim: 08:52 to about 09:14; 08:52 to 08:58 and 08:58 to 09:06; upper bounds | `runs/deepseek-v4-flash-two-box/task-{b,c}/CONTENDED.md` | their text |
| "three runs' timings polluted" | our end-of-day summary | an internal document that does not ship; quoted on the page |
| task B 09:14:19 to 09:20:28; task C 09:20:29 to 09:28:22 | `runs/deepseek-v4-flash-two-box/task-{b,c}/meta.json`; `scores/timeline.csv`; `harness/driver_log_excerpt.txt` | `started`/`finished`; the OpenCode log columns; line 45 |
| stray log ends 09:14:19.043; task B's OpenCode started 0.544 s later | `scores/timeline.csv`; `harness/task_a_lost_run_log_excerpt.txt` | `opencode_log_last` of `task-a-lost` 09:14:19.043; `opencode_log_first` of `task-b` 09:14:19.587; difference 0.544 s (arithmetic) |
| task D finished 08:52:14, before the stray session began | `runs/deepseek-v4-flash-two-box/task-d/meta.json`; `scores/timeline.csv` | `finished` 08:52:14; `opencode_log_last` 08:52:14.552 against the stray log's first line 08:52:15.141 |
| the notes' times are 08:52 plus the durations | arithmetic | 08:52 + 369 s = 08:58; + 473 s = 09:06 |
| first times 369 and 473 s; re-runs 518 and 433 s | `scores/coding_runs.csv` | `wall_seconds` |
| GLM-5.3-Flash honesty 10 of 10 on the judgment question | `scores/judgment_question.csv` | `honesty` |
| the task-B runs began 09:14 and 13:19 | `runs/deepseek-v4-flash-two-box/task-b*/meta.json` | `started` |
| task-D honesty 9 and 9 | `runs/ornith-1.5-35b/task-d/grade_numbers.json`; `runs/deepseek-v4-flash-two-box/task-d/grade_numbers.json` | `honesty` 9 in both |
| 30,214 input, 175 output; largest output 2,942 | `scores/deepseek_task_a_steps.csv` | step 4 of `task-a-lost`: `input_tokens` 30214, `output_tokens` 175; max `output_tokens` 2942 (step 8) |
| three other models had larger task-A steps | `scores/event_stream_gaps.csv` | `step_output_tokens_max` on task A: 9,119 (GLM-5.3-Flash), 11,147 (Ornith-1.5-35B), 12,256 (Ornith-1.5-397B) against DeepSeek's 2,942 and 3,441 |

## 12 Sources and artifacts: the timeline table

| Row | File | Field or derivation |
|---|---|---|
| 15 September: trial built | method log | the trial plan's header ("Trial pack built 2026-09-15"); harness file times 2026-09-15 |
| 01:06 to 01:22 | `scores/timeline.csv`; `harness/round_logs_excerpt.txt` | first run 01:06:14; Ornith-1.5-35B task A finished 01:22:46; the refusals |
| 01:25 to 03:25 | `runs/ornith-1.5-35b/task-{b,c}-void/meta.json` | as in section 08 |
| 04:22 to 04:37 | `harness/run_trial.version-2026-09-16T04-22.sh`; `scores/timeline.csv`; file times | guard version; re-runs 04:24:31 to 04:29:07; key fix 04:35 to 04:37 |
| 08:36 to 09:48 | `harness/launch_lines_excerpt.txt`; `scores/timeline.csv` | the round's start (driver log line 3, on our machine: 08:36:20) and DeepSeek's task A finish 09:48:01 |
| 09:48 to 13:10 | `harness/launch_lines_excerpt.txt`; `harness/orchestration_log_excerpt.txt` | Ornith-1.5-397B from 09:48; orchestrator complete 13:10:11 |
| 13:14 to 14:22 | `harness/orchestration_log_excerpt.txt`; `scores/timeline.csv` | 13:14:54 start; the judgment question's last answer at 14:22 (its round log, on our machine) |
| repository revisions 12393612, ba785b50, 621d456e | our pre-flight notes of 2026-09-15 | recorded when the files were fetched; not a file in this package |

## Method-log figures (notes written during the work; raw output not kept)

| Figure on the page | What the note says | Why there is no file |
|---|---|---|
| the honesty deductions on task A are the miscounts | the method log attributes them so | the grader's reasons are not published |
| "we miscounted it ourselves" | the author counted 18, then 19, then 18 | a note, not a measurement |
| 34 then 39 (DeepSeek task B re-grade) | first grade 34 (diff 12, honesty 9, scope 10, explanation 3) | the first grade file was overwritten before it was backed up |
| 40 then 39 (Qwen3.8-27B task B, first round) | "came back one point lower (40 -> 39)" | the first grade file was replaced |
| the 5-point difference tied to the stale label | the note's own reading | same as the 34 above |
| the catalogue fetch "confirmed ... on the wire" | the harness comment in `harness/run_trial.version-2026-09-16T04-22.sh` | no trace was saved |
| the database suspect | `VOID.md` | no database profile was saved |
| the checker fix that dirtied the fixture | the method log and the harness comment | the dirty sandbox's note names private files and does not ship |
| the latent upper-case case in task A, fixed before round 2 | the task-suite audit note | the audit names private files |
| the follow-on guard matched its own launcher | the method log | no process listing was saved |
| one false alarm from counting `print_timing` lines | the method log | a note |
| one factual error in the judgment question; not re-graded | our notes of that day | the question is private |
| 52% of the download actually on disk | the download job's README | the measurement's output was not saved |
