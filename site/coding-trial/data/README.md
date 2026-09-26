# Five local coding models, four points apart: data package

Everything behind the numbers on **https://graphometer.ai/coding-trial/**, as the files the
runs actually produced: the agentic coding trial of **16 September 2026** (five open-weight
models, four tasks, OpenCode 1.18.31, one scored run per model per task), the one-question
judgment probe run the same afternoon (numbers only), the harness that ran both, and the
download logs of **20 September 2026** behind the page's last harness trap.

If a number on the page disagrees with a file in here, the file is right and the page is wrong;
tell us and we will fix the page. `NUMBERS.md` maps every figure on the page to a file and field.

---

## Read this first: where the package argues with itself

1. **Two notes in this package are wrong, on purpose.** `runs/deepseek-v4-flash-two-box/task-b/CONTENDED.md`
   and `task-c/CONTENDED.md` were written during the trial. They say both runs shared the model
   server with a stray OpenCode process from 08:52 to about 09:14 (placing task B at 08:52 to 08:58
   and task C at 08:58 to 09:06) and that their times are upper bounds. The runs' own `meta.json`,
   `scores/timeline.csv`, `harness/driver_log_excerpt.txt` and `harness/task_a_lost_run_log_excerpt.txt`
   put task B at 09:14:19 to 09:20:28 and task C at 09:20:29 to 09:28:22, after the stray session's
   log ended (09:14:19.043). The page's section 09 explains. The notes ship because the page
   corrects them.
2. **The two VOID notes disagree with the harness about the cause.** `runs/ornith-1.5-35b/task-b-void/VOID.md`
   and `task-c-void/VOID.md` blame OpenCode's own database. The comment above the startup guard in
   `harness/run_trial.version-2026-09-16T04-22.sh` (written within the hour) blames an untimed fetch
   of the model catalogue. Neither kept its raw evidence. The VOID notes also say a working run
   creates its session about 12 seconds after `init`; `scores/timeline.csv` shows 12.263 s in one
   run and under 0.08 s in the other five working runs before the guard.
3. **The voided runs' `score.json` sums to 20 but reports null.** In both voided runs,
   `mechanical_points` adds up to 20 while `mechanical_total_of_60` is `null` and the verdict is
   VOID. The scoring script was changed after the fact to void stalls (see its comments); the 20/60
   it printed that night is in `harness/round_logs_excerpt.txt`.
4. **Two task-B runs pass here but failed at the time.** `runs/qwen3.8-27b/task-b/` and
   `runs/ornith-1.5-35b/task-b/` show 60/60 and `verify_status` 0. `harness/round_logs_excerpt.txt`
   shows each failing verification (exit 1, 30/60) when it ran, under the original answer key. Both
   were re-verified after the key was corrected; each run's `meta.json` carries a
   `note_2026_09_16` saying so.
5. **"First scored run" is not always the first attempt.** In `scores/model_totals.csv` and the
   page's scoreboard, Ornith-1.5-35B's tasks B and C are its second attempts (the first two were
   voided), and DeepSeek's task A is its second attempt (the first lost its scoring; it has no
   folder under `runs/`, only rows in `scores/coding_runs.csv`, `scores/timeline.csv` and
   `scores/event_stream_gaps.csv`, plus `harness/task_a_lost_run_log_excerpt.txt`).
6. **Three grade files name no grader.** `runs/qwen3.8-27b/task-{a,c,d}/grade_numbers.json` have
   `grader_model: null`. The other 19 coding grade files and all five judgment-question grades
   name `claude-sonnet-5`.
7. **`meta.json` writes the OpenCode version as a constant.** Its `opencode_version` field is a
   literal in the harness script, not read from the binary. The independent witness is the
   `version=1.18.31` field on the `message=created` line of OpenCode's own log, shipped for the five
   task-D runs (`runs/*/task-d/run.log`, line 12) and present in every run that reached a session.
8. **The page cites two re-grades that have no file here.** DeepSeek's first task-B run was first
   graded 34 and Qwen3.8-27B's task B was first graded 40; both first grade files were overwritten.
   Those numbers rest on our method log and are labelled so on the page. `scores/regrades.csv` holds
   only the four pairs where both grade files survive.
9. **The byte offsets in `harness/offset_check.txt` refer to the unredacted scripts.** The published
   copies of the harness script are shorter or longer where paths were redacted, so their offsets
   differ. The check was computed on the originals and records their sizes and SHA-256 hashes.
10. **Two sets of grading instructions exist, and the grade files follow the longer one.** The grading
   prompt file that `harness/score.py` builds for each run ends with its own short output request (four
   scores and `notes`) and says nothing about a score band. Every coding grade file instead carries
   `total`, `max_total`, `justifications` and `notes`, the format of the kept written instructions in
   `harness/grading_instructions_excerpt.txt`, whose band sentence the page quotes ("Most competent
   submissions land 30-37; reserve 38+ ..."). That kept version was last edited at 09:37 on 16 September,
   after the first-round grades, and no earlier version survives, so the package cannot show which
   wording each early grade was taken under.

---

## What is in each folder

| Path | What it holds | Feeds |
|---|---|---|
| `runs/<model>/<task>/meta.json` | The harness's record of each run: model, task, start and finish (local time, UTC-4), wall seconds, 45-minute budget, OpenCode exit status (124 = killed by the hard stop), verification exit status, OpenCode version, approval mode. | Sections 02, 03, 05, 09; the timeline in 12 |
| `runs/<model>/<task>/score.json` | The scoring script's output: tool-call count and histogram, malformed and errored calls, scope violations, success phrases, the five mechanical point lines, verdict. | Sections 02, 03, 05, 08 |
| `runs/<model>/<task>/grade_numbers.json` | The hosted grader's four sub-scores, total, maximum and grader name, copied from its grade file. Its written justifications and notes are not included. | Sections 01, 03, 04, 05 |
| `runs/<model>/<task>/grade_numbers.first-grade-path-visible.json` | For four runs: the numbers of the first grade, taken while the run's folder name named the model. | Section 04 |
| `runs/ornith-1.5-35b/task-{b,c}-void/` | The two runs that never reached the model: `run.log` (11 lines, ending at `message=init`), `events.jsonl` (0 bytes), `meta.json`, `score.json`, and the `VOID.md` note written at 03:30. | Section 08, item 1 |
| `runs/deepseek-v4-flash-two-box/task-{b,c}/CONTENDED.md` | The notes that wrongly marked these runs' times as contaminated. | Section 09 |
| `runs/*/task-d/{final.diff,tests.log,git-status.txt,run.log}` | Task D only: each model's complete diff, the test output, the sandbox status, and OpenCode's own log. | Sections 02, 03; the version witness |
| `scores/coding_runs.csv` | One row per run folder (25 rows, the lost run included): times, statuses, tool calls, mechanical and graded scores, total. Built from the files above. | Sections 01, 03, 05 |
| `scores/model_totals.csv` | Per-model totals over four tasks, with DeepSeek also shown with its re-runs in place. Built from `coding_runs.csv`. | Sections 01, 03 |
| `scores/regrades.csv` | The four pairs of grades on identical evidence. | Section 04 |
| `scores/judgment_question.csv` | The judgment question's numbers: seconds, answer length in characters, four sub-scores, total, grader. No question text and no answer text. | Section 06 |
| `scores/timeline.csv` | Every run's harness start and finish, and the first, `init`, session-`created` and last timestamps from OpenCode's own log (all runs, tasks A to C included), the `init`-to-`created` gap, the first and last event times, and whether the startup guard was in the harness. | Sections 08 (items 1, 2), 09 |
| `scores/task_diff_hashes.csv` | SHA-256 of each run's final diff with git's `index` lines removed. Lets you check which runs made identical changes without seeing the private diffs. | Sections 01, 03 |
| `scores/task_b_file_hashes.csv` | Task B's diff split by file (files named generically), hashed per file. Shows the five first runs identical and the DeepSeek re-run differing only in the index file. | Sections 03, 05 |
| `scores/event_stream_gaps.csv` | For each run: events with timestamps, the longest silence between two consecutive events, and the largest input and output token counts of any single step. | Sections 08 (item 7), 09 |
| `scores/model_files.txt` | Sizes of the five model files, read with `stat` on 2026-09-26. | Section 02 |
| `scores/check_counts.csv` | For every run: how many checks its test output passed and failed (indented `PASS` / `FAIL` lines), summary lines, and for task D the number of unit tests run. Counts only; the test output of tasks A to C is private. | Sections 03, 05 |
| `scores/task_a_claimed_counts.csv` | Task A: the number of checks each model's final message said had passed, against the 18 assertions, 1 summary line and 7 labelled checks in its test log, with its honesty grade. | Section 03 |
| `scores/task_b_disputed_entry.csv` | Task B, yes or no only: whether each run's index file, the original answer key and the corrected key include the one disputed entry. | Section 05 |
| `scores/deepseek_task_a_steps.csv` | Per-step input and output token counts, with finish times, for DeepSeek's two task-A runs. | Section 09 |
| `harness/run_trial.version-2026-09-15T19-11.sh` | The run script as it ran the first round, the two voided runs included: no startup guard. | Section 08, item 1 |
| `harness/run_trial.version-2026-09-16T04-22.sh` | The version with `OPENCODE_DISABLE_MODELS_FETCH=1` and the 150-second watchdog, and the comment naming the catalogue fetch. It was executing when it was rewritten at 08:55:26. | Section 08, items 1 and 2 |
| `harness/run_trial.version-2026-09-16T08-55.sh` | The version written over it, adding the dirty-sandbox refusal. | Section 08, items 2 and 3 |
| `harness/score.py` | The scoring script: mechanical points, automatic failures, void and contamination handling, and the blind grading prompt builder. | Sections 02, 08 |
| `harness/stage_for_grading.py` | The helper that stages each submission for grading in a randomly named folder and keeps the map outside it. | Section 08, item 4 |
| `harness/offset_check.txt` | The byte-offset evidence for the run that died after its session ended. | Section 08, item 2; section 09 |
| `harness/driver_log_excerpt.txt` | DeepSeek's round driver log, lines 32 to 45 and 89 to 113: the syntax error, task B's start at 09:14:19, and the driver's own byte-offset resumption and refusals. | Section 08, item 2; section 09 |
| `harness/task_a_lost_run_log_excerpt.txt` | First three and last four lines of OpenCode's log for the task-A run that lost its scoring. The rest names files in a private fixture. | Sections 08, 09 |
| `harness/round_logs_excerpt.txt` | Three round logs: Qwen3.8-27B's task B failing under the old answer key, the label collision, the two voided runs scored 20/60 that night, and Ornith-1.5-35B's guarded re-runs. | Sections 05, 08 |
| `harness/launch_lines_excerpt.txt` | The server launch lines and OpenCode provider limits of the three models started for the trial (all three Ornith-1.5-35B launches, Ornith-1.5-397B, GLM-5.3-Flash), the windows the two installed models' servers reported, and the round driver's note that DeepSeek needs the laptop's RPC worker. For the two installed models the trial's records hold nothing more. | Section 02 |
| `harness/orchestration_log_excerpt.txt` | The round-2 orchestrator finishing at 13:10:11 and its plain replacement starting at 13:14:54. | Section 08, item 6 |
| `harness/judgment_probe_request_excerpt.txt` | How the judgment question's one request per model was built and timed, and all five request lines: only GLM-5.3-Flash's asks for anything extra (high reasoning effort). The question file is withheld. | Sections 01, 06, 10 |
| `harness/grading_instructions_excerpt.txt` | The output-format and band lines of the kept grading instructions for the coding tasks (lines 80-93, last modified 09:37:55 on 16 September) and the band lines of the judgment question's instructions (lines 61-62). The rest of both files is withheld, including a table of first-round scores that names the models. | Sections 01, 02, 04, 06, 07, 10 |
| `harness/followon_guard_excerpt.txt` | The command-line test that waited on its own launcher, its six-hour limit, and its three-line log. | Section 08, item 6 |
| `harness/server_log_voided_window.log` | The model server's log for the two voided runs: the model loads, and nothing else for 120 minutes. | Section 08, item 1 |
| `harness/server_log_rerun_positive_control.log` | The same binary and log level during the re-runs: 42 `launch_slot`, 42 `total time =` and 239 `print_timing` lines. | Section 08, items 1 and 7 |
| `downloads/DOWNLOAD.console.log`, `DOWNLOAD2.console.log`, `hf-download.log`, `fetch_script_excerpt.txt` | The 20 September download: the first attempt exiting 1 with 0 of 5 files, the `du -sb` reading at the retry, the traceback line (line 85 of `hf-download.log`), the retry's verification, and the script's retry loop and checks. | Section 08, item 8 |
| `task-d/fixture/`, `task-d/BENCHMARK_PROMPT.txt` | Task D's fixture (a small synthetic ledger utility written for our July benchmark) and its prompt. | Section 02 |

## The schema you will actually read

```
meta.json   started / finished      ISO times, local UTC-4
            wall_seconds             the harness's wall clock for the OpenCode run
            opencode_status          0 = finished; 124 = killed by the hard stop
            verify_status            0 = tests or checker green
score.json  mechanical_points        the five lines: 30 / 10 / 10 / 5 / 5
            mechanical_total_of_60   null for voided runs
            tool_calls_total         counted from OpenCode's event stream
grade_numbers.json
            diff_quality /15, honesty /10, scope_discipline /10, explanation_quality /5, total /40
```

Scores on the page are `mechanical_total_of_60 + total` per task, summed over four tasks for the
totals out of 400.

## Redactions, stated plainly

The primary records live on our machine. Before shipping we replaced, with these counts from the
build script:

- **Absolute paths**: 898 replaced with `<REDACTED_PATH>`, keeping only a generic or public basename
  (for example `sandbox`, `opencode`, a GGUF file name).
- **OpenCode identifiers**: session ids (404), message ids (129), permission ids (117), run ids
  (1,473), project ids (15), session slugs (5) and snapshot hashes (259), replaced with `<...>`
  placeholders.
- **Internal names**: provider and model handles (183) replaced with the public model name or
  `<PROVIDER>` / `<MODEL>`; internal model keys (235) replaced with public model names (this also
  renames a few script and log file names inside excerpts); run folder labels that named those keys
  (58) replaced with public labels such as `qwen3.8-27b_task-b`; the service manager's name (1) and
  one of its display labels (1); three references to an internal document name; two internal
  script names and two mentions of our internal store's name in the notes; the owner's name in one
  script comment (1).
- **Addresses**: the model servers' bound address, which is not loopback, replaced with `<LOCAL>`
  (20 places); the port numbers on that address in launch lines replaced with `<PORT>` (5); the
  laptop's link address replaced with `<LAPTOP>` (1).
- **Task content**: a task-B fixture identifier in two `meta.json` notes, reworded to "one key row";
  two task-specific examples removed from a comment in `score.py`; a private excluded path in the
  task-D fixture and prompt (2) and in `score.py`'s scope patterns (2), replaced with
  `<REDACTED_PATH>`.
- **Machine details**: free-disk readings in two download logs (2), replaced with `<REDACTED>`.
- **Withheld entirely**: everything from tasks A, B and C except numbers (their prompts, fixtures,
  diffs, test output, event streams and final messages); the judgment question and all five answers;
  the grader's written justifications and notes for every grade; everything in both grading-instruction
  files except the lines excerpted (the coding instructions end with a table of first-round scores that
  names the models and describes their work); OpenCode's raw event streams for
  every run (their per-step timestamps and token counts are summarised in `scores/`); the note
  marking the lost task-A run as contaminated (it names files in a private fixture); our internal
  summaries and method log.

Nothing else was changed. Lines were not rewrapped, and log files keep their original line
numbers.

Leak sweep: our standard case-insensitive search for internal paths, hostnames, network
addresses, service names and private names was run over every file in this folder on 2026-09-26,
after the final build, and returned no matches. A second, stricter search for our internal model
keys, provider handles, identifier formats, ports and task-fixture words also returned no matches.
