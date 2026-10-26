# Data package: "The roster, as of October 2026"

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where this package looks like it argues with itself

1. **Muse Spark's reading speed.** An earlier summary of ours said 191 t/s for a 106K read. The timing extract shows
   155.00 t/s for the 106,469-token read; 190.52 and 192.92 are two later reads of about 77,000 tokens.
2. **Qwen3.8-27B thinking-on "prose" rows hold no prose.** In `installed_229k.jsonl` and `E2_..._thinkON.jsonl` the
   `kind: prose` rows have `answer_words: 0`: all 3,500 tokens were reasoning. The page calls them reasoning.
3. **Hemmingway-1's `kind: prose` rows** in `measure.jsonl` are the same: 3,000 tokens of reasoning, no visible letter.
4. **MiniMax M2.7 in the P-core folder** is the one pair whose replies differ (381 against 421 tokens); its pinned run
   restored a saved cache (`prompt_n` 1) instead of reading the ledger again.
5. **GLM-5.3-Flash's 28,846 MiB** comes from a shorter run at the same setting
   (`glm-5.3-flash-new-256k-ub2048.peak_mib`), not from the 230,039-token run, which kept no peak file.
6. **Card memory in `.result` files and `.peak` files** can differ by a few MiB from `.vram` samples: they are separate
   samplers. The page prints the largest sample from the file it names.
7. **GLM-5.3-Flash has two copies of its first file.** `extracts/file-sizes-2026-10-25.tsv` lists the four files as
   downloaded (147,535,921,955 bytes in all) and a second, rewritten first file of 9,429,984 bytes beside links to the
   other three. The page prints the downloaded total.
8. **Qwen3-235B's runs differ in more than one setting.** `runs/qwen3-235b-2026-09-29/start-lines.txt` gives the window,
   cache and extra flags of each run. The 16-bit and 6-expert runs used a 118,784 window; the 8-bit, 4-bit and installed
   runs used 131,072; only the installed run sets `-ub 1024`.
9. **DeepSeek V4 Flash 0731's build comparison** uses the `long` request of each file. The two `short` requests differ
   more (10.64 against 13.33 t/s), and they wrote different amounts of reasoning (4,244 and 6,160 characters); the page
   does not use them.
10. **Qwen3.8-27B's draft and no-draft runs differ in micro-batch too.** The `A0_*` runs (no draft model) start with
    `--ubatch-size 512`; the `E2_*`, `F1_*` and `F3_*` draft runs with `--ubatch-size 256`. Threads match. At 262,144
    no pair holds the micro-batch fixed, so the page says the letter gains and the 262,144 reasoning speeds (189.26 and
    143.68) were measured with the draft model, the smaller micro-batch and a shorter request (`prompt_n` 314 against 570) all at once. `F2_*` is a draft run with `-ub 512`, at a 196,608
    window. Its 100,000-deep reasoning row (`prompt_n` 570, 3,500 tokens, no visible answer) ran at 133.92 t/s against
    47.3 on `A0_prod_256k_thinkON` at the same `-ub 512` and `prompt_n`; the window differs, so that pair does not
    isolate the draft model either, and no run here does. F2's 20,000-deep row (2,897 tokens, a 350-word answer) is not
    a match and is not used. `installed_229k.jsonl` has no command line, so the page does not say which `-ub` or cache
    type the installed server used, and gives its speeds no micro-batch. The new text after the long read also differs:
    `prompt_n` 570 on the `A0` letters and reasoning, 314 on the `E2` and installed rows.

## What is here

| Path | What it is | Provenance |
|---|---|---|
| `runs/ornith-1.5-122b-2026-10-23/` | probe results at 20K and 240K for three placements, card peaks, the health lines | direct probe, 2026-10-23 |
| `runs/hemmingway-aura-spark-2026-10-22/` | probe results for Hemmingway-1 (two windows), Aura 4o Rebirth (three windows), Muse Spark at 262,144; peaks; health and start lines; `spark256-settings.txt`, that run's window, pin and cache setting | direct probe, 2026-10-22 |
| `runs/gpt-oss-2026-10-15/` | depth probe results and card samples for GPT-OSS 20B and 120B; `command-lines.txt`, both server command lines | direct probe, 2026-10-15 |
| `runs/beam-nemotron-2026-10-17/` | probe results for Beam (two windows), Nemotron 3.5 Bolt (2-bit with draft, Q4, laptop); perplexity result lines; `beam-q2kxl-256k.window-lines.txt`, the start and load lines that set Beam's 262,144 window (paths removed) | direct probe, 2026-10-17 |
| `runs/deepseek-v4.1-1017-2026-10-18/` | speed and depth probe results, card peak, the layout comparison against the first V4.1 file; `deepseek-v4.1-1017-server-lines.txt`, the server's page-locked RAM line and its drive-read counters around the 110,052-token read | direct probe, 2026-10-18 |
| `runs/qwen-installs-2026-10-03-to-04/` | the installed-shape probe and card samples for Qwen3.6-35B-A3B, Qwen3-30B-A3B-2507, Qwen3.5-27B | install tuning runs |
| `runs/qwen3.8-27b-2026-10-19/` | same-day runs without and with the draft model, thinking off and on, and the installed 229,376 shape; run records with card peaks | direct probe, 2026-10-19 |
| `runs/build-tests-2026-10-11/` | old build against mainline b11552 for GLM-5.3-Flash, DeepSeek V4 Flash 0731 and Qwen3.8-Flash-Next; GLM at 262,144 deep; the refused -ub 4096 allocation | direct probe, 2026-10-11 |
| `runs/pcore-pin-2026-09-29/` | 16 pairs of runs, 24 threads against 8 pinned P-cores; `thread-placement.txt`, the cores and spin setting each server ran with, and the launcher line for each setting | direct probe, 2026-09-29 |
| `runs/qwen3-235b-2026-09-29/` | the three cache types, the 6-expert run (`d5_f16_6exp`) and the installed shape on the Q3 file; `start-lines.txt`, each run's start line and the file it loaded | direct probe, 2026-09-29 |
| `extracts/timing-only/` | only the server's timing lines (prompt time, generation time, draft acceptance, window) from runs whose prompts are not published | derived: lines filtered from server logs, unchanged |
| `extracts/file-sizes-2026-10-25.tsv` | every model file named on the page with its byte count | listing taken 2026-10-25 |
| `extracts/served-windows-2026-10-25.tsv` | the default window each start script serves | read from the start scripts and their settings files, 2026-10-25 |
| `extracts/mimo-v2.6-flash-start-script-note.txt` | the reasoning-cap note and default from the MiMo start script, with one phrase removed | quoted 2026-10-25 |
| `extracts/glm-5.3-flash-template-effort-line.txt` | the reasoning-effort line from the chat template inside the GLM-5.3-Flash file | read from the file header, 2026-10-25 |
| `NUMBERS.md` | every figure on the page, mapped to a file and field | |

No reply text ships. Every reply-text field (`tail`, `answer_tail`, `reply_head`, `long_answer_head`) was deleted from
every probe file, including the copies inside `.result` files, and so were the arguments of tool calls. What is left
is counts, timings and pass or fail flags. No hosted-API output is in this package.

## Redactions

Counts are for this package and the October field notes' package together; both were built in one pass.

- Absolute paths: replaced in full with `<REDACTED_PATH>/` plus the file name (33 replacements).
- Bridge addresses and bind hosts: `<LOCAL>` (7 and 7); ports passed on a command line: `<PORT>` (7).
- Host names: `<DESKTOP>` (14). Process ids: `<PID>` (5).
- Our internal short names for each model, in file names and inside files: replaced with the public model name
  (252 replacements). Run tags such as `hem229` or `o262n38` are kept; they name a run, not a service.
- Reply text, round 2 (2026-10-25): every reply-text field deleted from every JSON line in this package: 396 fields
  (`tail` 197, `answer_tail` 142 counting the copies inside `.result` files, `reply_head` 51, `long_answer_head` 6),
  plus 6 tool-call argument fields. One of them, in the DeepSeek V4.1-Flash-1017 depth file
  (tag `tool:result`), held the model's report of a tool result; that text is gone with the rest of the reply text. The speeds and
  counts are untouched.
- Added in round 2, each with its address, port and path removed: the GPT-OSS command lines, the Spark start line and
  setting, the DeepSeek V4.1-Flash-1017 server lines, the P-core run placement lines, the Qwen3-235B start lines.
- The DeepSeek card-peak line: the name of the second drive was changed to "second drive".
- The DeepSeek layout comparison: the old chat template text removed; its line now reads `tokenizer.chat_template: old='<template text removed>' new='None'`.
- Not shipped at all: the runs' text logs that name an agent framework's internal tools; the server logs of runs whose
  prompts are not published (only their timing lines ship, above); the start scripts and their settings files (the one
  quoted MiMo note excepted).

Before publishing, this whole `data/` tree was searched again on 2026-10-25 for reply text, tool results, local file
paths, private network addresses, host and account names, disk device names, internal service and tool names, places
and personal details. What that search found is listed above and was removed.
