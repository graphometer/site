# Data package: llama.cpp's batch settings on one RTX 5090 (19 to 21 September 2026)

This package holds the files the runs produced: result files, server logs, card-memory samples, stress
records, the harness scripts, and a few tables derived from them. If a number on the page disagrees with a
file in this package, the file is right and the page is wrong; tell us and we will fix the page.

## Read this first: where the package argues with itself

1. **"llama.cpp default 512" is sometimes a wrong label.** Runs with no override print
   `ubatch=skip (llama.cpp default 512)` in their `.result` header. That text is the harness's, and it is
   wrong in two files: `runs/2026-09-21_sweep/Laguna-S-2.1_skip.result` (and its copy
   `Laguna-S-2.1_baseline_ub128.result`), where the start script itself set `-b 512 -ub 128`, and
   `runs/2026-09-21_ling-crash/Ling-3.0-flash_ub4096_CRASHPROMPT.result`, where the script then set
   `-b 4096 -ub 4096`. The logs carry the truth: Laguna's prompt-processing progress lines step by 512
   (546, 1058, 1570...), which is its `-b 512`, and `derived/excerpts.md` quotes the script lines. On all
   other `skip` runs the label matches the script.
2. **"FIT" for two settings that did not fit.** `runs/2026-09-19_minimax-m2.7/192K.console.log` prints
   `^ FIT at -ub 4096` and `^ FIT at -ub 2048`, yet the same log shows `VOID: server exited during load`
   for both, and the server logs show the refused allocations. The harness wrapped each run in `|| true`, so
   its exit code was always 0. Only `-ub 1024` loaded at 196,608.
3. **One M2.7 figure lives only in a console log.** The 3,658-token read at `-ub 4096` (564.0 t/s, 24,359 MiB
   at load) was run under the label `one_ub4096_cmoe_ctx131072`, and the 43,909-token run that followed used
   the same label, so `one_ub4096_cmoe_ctx131072.json` now holds the 43,909-token run. The 564.0 figure's
   record is `CONFIRM.console.log`.
4. **Four or five scripts.** The header of `tools/bsweep_2026-09-20.sh` says "Only 4 of 25 start scripts set
   --batch-size/--ubatch-size". Our file-by-file recount (`derived/scripts_before_sweep.tsv`) finds five
   that set them by default, one of them on only two of its three window settings, plus one that sets them
   only when an optional setting is given. The page prints five.
5. **Two untuned DeepSeek readings at the same depth.** The 48,073-token read at llama.cpp's default measured
   72.32 t/s in `runs/2026-09-20_deepseek-v4-flash/v_A_base_48k.*` (a load of 3 min 55 s) and 83.33 t/s in
   `v_V_base.*` (a load of 3 s), same flags. The logs' clocks count from each process's start, so they do not
   date the gap between the two runs, and the page does not give one. The page uses 83.33.
6. **"needle_found: false" that is not a failed recall.** In `run_verify.out`, the first 48K pass on DeepSeek
   shows `needle_found: false` and `reply_len: 0` at every rung. That pass set `max_tokens` to 64; the logs
   show 64 of 64 tokens generated each time, all spent reasoning. That is the page's section 08. The same file
   then shows a broken edit of the harness (`peated: command not found`, a syntax error) and several
   `REFUSED: busy` lines; those produced no measurements. The corrected harness is
   `tools/deepseek_verify_2026-09-20.sh`; the 64-token version was not kept.
7. **An empty answer that passed.** `runs/2026-09-21_sweep/GLM-4.7-Flash_2048.result` has
   `needle_in_answer: false` and `answer_len: 0`: the model spent all 900 tokens reasoning, with the code in the
   reasoning. The pass rule accepts an empty answer on the reasoning alone; the chain file shows it.
8. **Card memory is measured two ways.** 20 September files record card memory once, after load (`vram=` in
   the `.result`); 21 September files record the peak during the read (`peak VRAM`, sampled into `.vram`). Do
   not subtract one kind from the other.
9. **Replay reads are slower than sweep reads.** The `_replay3000` files in `runs/2026-09-21_stress/` are the
   first request after a fresh load, run to check for a crash and for the code. Some read much slower than the
   sweep's reads of similar size (MiniMax M2.7: 192.6 t/s on 3,042 tokens, against 564.0 on 3,658 tokens on 19
   September). The page quotes two of them, and only as what they are: the 21 September replays of
   Qwen3.8-Flash-Next (112.3 t/s on 2,999 tokens) and Inkling-Small (187.9 on 3,033), because they and the 20
   September `*_262k-confirm` reads were the only speeds for those two models at the 262,144 window they serve
   (point 14), until Qwen3.8-Flash-Next was re-measured there on 26 September (point 15).
10. **Cross-pass ratios.** Ling's 238.2 comes from the 20 September pass (hand-copied flags, 131,072 window) and
    its 727.7 from 21 September (its own script, 262,144); each keeps its own card and decode figures on the
    page (7,233 MiB after load and 27.46 t/s on 77 tokens; 8,824 MiB peak over the series and 23.25 t/s on 77
    tokens), and a second line gives the one-pass, one-window pair (3,007 tokens: 201.5 and 444.0 t/s, peaks
    8,037 and 8,871 MiB, decode 24.41 and 23.0). The 2048 file's `decode_tps` 23.0 is the log's 23.00.
    GLM-5.3-Flash's default was read at 24,008 tokens (the load's first request, task 0); the page's tuned
    figure is the 20,333-token read (446.0 t/s, task 106, the series' third request), and the 48,168-token read
    (425.1, task 172) is in the note. The series file records one peak (29,872 MiB) for all four reads.
11. **The 15 September response lost its build field.** `runs/2026-09-15_deepseek-v4-flash-depth/DeepSeek-V4-Flash-Q8_262144.deep.json`
    had its `id`, `system_fingerprint` and `created` fields removed (our package rules strip response
    identifiers). The `system_fingerprint` read `b1-5f55650`: build 5f55650, the same binary the 20 September
    DeepSeek runs used (unchanged since 31 July).
12. **Two field names mean different things in different harnesses.** In the two-machine `.result` files,
    `warm_*` is the second request (the same document with a different last question) and `next_*` is the
    third (a real next turn). In the M2.7 JSON files, `warm` is the identical request sent a second time, a
    prompt-cache check.
13. **One digit of rounding between a log and its result file.** The page prints reading speeds as the result
    files give them (one decimal, rounded from the server's unrounded figure). The server log prints the same
    figure to two decimals, and rounding that twice can move the last digit: Gemma 4 26B-A4B's default read is
    8,972.35 in its log and 8,972.3 in its result file, GLM-4.7-Flash's 2,594.65 and 2,594.6.
    `derived/reads.tsv` carries the log's two-decimal values.
14. **"Confirmed" at the served window, on one short read.** The `*_262k-confirm` files in
    `runs/2026-09-20_first-pass/` hold one 3,000-token read each. Inkling-Small's ran at 263.6 t/s and
    Qwen3.8-Flash-Next's at 45.4 (3,041 tokens, 67.0 s, of which the first 989 tokens took 57.1 s by the log's
    progress lines). The start-script comments quoted in `derived/excerpts.md` section 3 cite only their card
    figures. The 48,000-token speeds in the page's main table are 131,072-window reads. For Inkling-Small no
    long read at 262,144 after the change is in the package or in our records; for Qwen3.8-Flash-Next the 26
    September run supplies them (point 15).
15. **The 26 September run: two starts, one of them from an empty page cache.** In
    `runs/2026-09-26_qwen3.8-flash-next-served-window/` the shipped setting ran first, on a server started with
    none of the model's 89.99 GB in the page cache (`run.console.log`: 0.0 GB before the start, 43.54 GB after
    the load). Its read 1 began at 43.54 GB and ended at 57.66 GB, and is the slow read (87.7 t/s, then 517.6 for
    read 2). llama.cpp's default ran second, on a server started with 60.05 GB already resident, and its read 1
    ran at 253.7 t/s, in line with its read 2 (255.7): the slowdown belongs to that one start, not to first
    requests in general. The six later reads began with 57.66 to 60.06 GB resident; the file never became fully
    resident. Only the 229,981-token reads planted three codes (`codes3_hits`); the others planted one
    (`code_ok`). `resident_gb_before` and `resident_gb_after` are decimal GB of the three model shards held
    in the page cache (the kernel's `mincore`, read by `tools/resident.py`); the model never became fully
    resident (about 60 of 90 GB). `vram_mib_after` is the card after each read, not a peak. The server logs do
    not print the batch settings; the progress lines show them, as restore points (983 = 3,035 - 4 - 2,048 on
    the shipped rung, 2,519 = 3,035 - 4 - 512 on the default) and as logical steps of 4,096 and 2,048. These
    reads ran with thinking off, the 20 September reads with it on.

## What is where

Every `.result` file is the harness's summary of one load; the `.log` beside it is that server's own log; the
`.vram` file is the card-memory samples (MiB) taken during the read. `_skip` means no override (the script's
own setting at that moment). Series files (`_ub2048`, `_shipped_*`, `_confirm`) hold several reads on one load,
one JSON line per read.

- `runs/2026-09-15_deepseek-v4-flash-depth/`: DeepSeek V4 Flash Q8 at its full 262,144 window at llama.cpp's
  default batch, 150,475 tokens, three planted codes (from a separate study; the depth baseline on the page).
  The log's first lines are the launch command.
- `runs/2026-09-19_minimax-m2.7/`: MiniMax M2.7's micro-batch ladder (`A_ub*`, 3,658 tokens), placement ladder
  at 4096 (`one_ub4096_{cmoe,61,60,59,58}_ctx131072`, 43,909 tokens), the 2048 depth read, the 196,608-window
  attempts (`*_ctx196608.server.log`), and the console logs. Prompt: a repeated paragraph; no answer check.
- `runs/2026-09-20_first-pass/`: the hand-copied-flags pass: Ling-3.0-flash, Inkling-Small and
  Qwen3.8-Flash-Next at the default, a candidate and (two of them) 8192; the 262,144-window confirmations
  (`*_262k-confirm`, including Ling's crash); the failed Laguna attempts (`Laguna-S-2.1_handflags_*`); the
  run outputs (`run*.out`).
- `runs/2026-09-20_deepseek-v4-flash/`: the 16,011-token comparisons (`A` default, `B` 2048, `C` q8_0 cache,
  `D` both, `E` the IQ3 file); the 64-token pass (`v_A_*`, `v_B_*`, `v_F_*`); the 900-token 48K reads
  (`v_V_*`); the 150,324-token read at 262,144 (`v_W_256k_ub8192`).
- `runs/2026-09-20_minimax-m3-two-machine/`: three refused working buffers on MiniMax M3 split across the
  desktop and the laptop (`vl36`/`vl50` = 36 or 50 of its 60 layers on the desktop; see `derived/excerpts.md`).
- `runs/2026-09-21_sweep/`: the sweep through each model's own start script: every rung's `.result`, `.log`
  and `.vram`, the chain verdicts (`*_chain.txt`), the queue log (`QUEUE.txt`), GLM-5.3-Flash's four-size
  series, Ornith-1.5-35B at 8192, and Laguna S 2.1 at larger windows (`Laguna_ctx*`) and through its shipped
  script (`Laguna_shipped_confirm`).
- `runs/2026-09-21_ling-crash/`: the Ling ladder on the crash prompt (`Ling-3.0-flash_{512,1024,2048,skip}`),
  the crash itself (`_ub4096_CRASHPROMPT`), the five-read series at 4096 (`_shipped_262k_A`), the shipped 2048
  confirmation (`_ub2048_confirm`); `diagnostic/` (the window and length tests, one server log each; the
  window and micro-batch are in each file name); `stress_ub{4096,2048}_s777/` (60 real-text prompts each);
  `ledger_ub{4096,2048}_s4242/` (50 ledgers each); `lenprobe_ub4096/` (eight raw-token lengths).
- `runs/2026-09-21_stress/`: `STRESS.txt` (the chain log), one folder per stress run
  (`stress_<model>_skip_s<seed>/`: `SUMMARY.json`, `results.jsonl`, `server.log`), and
  `replay-of-crash-prompt/` (a fresh load of each shipped setting of the eleven other models with experts in
  RAM, DeepSeek's Q8 and IQ3 files separately, answering the 3,007-token Ling prompt). The six models that fit
  on the card were not stress-checked. The GLM-5.3-Flash stress log does not print the micro-batch; its 4096 is
  its start script's setting (`derived/excerpts.md` section 3).
- `runs/2026-09-21_deepseek-v4-flash-iq3/`: the IQ3 file on the desktop alone at 262,144, `-ub` 2048 and 4096,
  its shipped 150K read, and the Q8 re-confirmation after the script was changed.
- `runs/2026-09-21_two-machine/`: DeepSeek V4 Flash IQ3 split across the desktop and the laptop, `-ub` 512,
  2048 and 4096, and the 150K read at 512. Each JSON line holds the cold read and the two follow-up requests.
  `Z13 GTT` is the laptop's graphics memory in use (MiB).
- `runs/2026-09-21_minimax-m2.7-installed/needle48k.json`: three codes planted in a 43,679-token document,
  all returned, through the installed start script.
- `runs/2026-09-26_qwen3.8-flash-next-served-window/`: Qwen3.8-Flash-Next at the 262,144 window it serves,
  through a copy of its start script: `-b 4096 -ub 2048` (the shipped setting) on a server started with an
  empty page cache, then `-b 2048 -ub 512` on one started with 60.05 GB of the file resident; one JSON row per read (`*.jsonl`: tokens, milliseconds, t/s, decode, page-cache residency
  before and after, card after, the code check), each load's server log, and the driver's console output
  (`run.console.log`: residency before each start, load time and card memory at load). Point 15.
- `runs/2026-09-26_ornith-1.5-35b-served-window/` and `runs/2026-09-26_qwen3.5-122b-a10b-served-window/`: Ornith-1.5-35B and Qwen3.5-122B-A10B at 262,144 through copies of their start
  scripts on 26 September, two batch settings each (Ornith 2048 / 512 and 2048 / 2048; the 122B 2048 / 512 and
  2048 / 1024). Each `.result` holds the header (served window, card at load, the launch command), one JSON row per
  request at depths of about 20,000, 48,000, 100,000 and 230,000 tokens (three codes in the deepest; thinking off per
  request), and the card peak over the series; the `.server.log` beside it is that server's log. The page's section
  04 note quotes the deepest reads. Its 822 MiB is arithmetic: the card's reported total, 32,607 MiB, published
  in the Qwen3.8-27B at 256K package (`/qwen38-256k/data/records/card-capacity.txt`), minus the 2048 / 1024
  series peak, 31,785 MiB.
- `runs/2026-09-26_minimax-m2.7-served-window/`: MiniMax M2.7 at 196,608, the context length its model file
  declares, through its installed start script on 26 September, which at that window sets `-b 4096 -ub 1024` with
  every expert layer in RAM (the one shape that loaded on 19 September). The `.result` holds the header, one JSON
  row per request at depths of about 20,000, 48,000 and 190,000 tokens (three codes in the deepest; thinking on,
  so `reasoning_chars` is above 0 in every row) and the card peak; the `.server.log` beside it is that server's
  log. The two prose requests after the shorter reads spent all 4,096 tokens reasoning and have empty answers; the
  page uses only the reads. `stress_MiniMax-M2.7_192k_s20260926/`: the 40-prompt stress check at the same window
  and shape (`SUMMARY.json`, one JSON row per prompt in `results.jsonl`, the server log). Each prompt asked for a
  reply of up to 160 tokens and a follow-up of up to 80, at temperature 0.7; every reply ran to its limit, and all
  40 rows are flagged `empty` (set when either reply is empty), so the check shows the server staying up, not the
  answers. The page's section 04 note quotes the three reads and the check.
- `runs/2026-09-26_glm-5.3-flash-served-window/`: GLM-5.3-Flash through a copy of its start script on 26 September:
  at 262,144, `-b 4096 -ub 4096` (did not load: the `.result` has the settings, its server log the refused 13,281.37 MiB
  compute buffer), `-ub 2048` (reads of about 20,000, 48,000, 100,000 and 230,000 tokens, three codes in the deepest)
  and `-ub 1024` (reads of about 20,000 and 48,000 only); at 131,072, `-ub 4096` (about 20,000, 48,000 and 100,000).
  Reasoning effort none at launch, yet `reasoning_chars` is above 0 on every read. `stress_GLM-5.3-Flash_256k_ub1024_s20260926/`:
  40 prompts at 262,144, the same request shapes as the MiniMax M2.7 check above; no crash, and 36 rows flagged
  `empty`. Its server log does not print the micro-batch; its first prompt's last progress line before the end sits
  1,028 tokens from it, as in the `-ub 1024` run's first read (2,052 at 2048, 4,096 at 4096). The page's section 04
  note quotes these runs.
- `tools/`: the harnesses that produced these files, with private paths removed (placeholders in angle
  brackets name what stood there, for example `<llama.cpp build d3146f2b5>/llama-server`):
  `batch_sweep.sh` (21 September driver), `sweep_chain.sh`, `queue_runner.sh`, `series_probe.sh`,
  `series_probe2.sh`, `two-machine_chain.sh`, `turn_probe.py`, `stress_chain.sh`, `stress_model.py`,
  `ling_crash_diag.sh`, `ling_stress.py`, `ling_ledger_stress.py`, `ling_len_probe.py`, `add_batch_knob.py`
  (it gave each start script that had no batch setting one whose default is llama.cpp's own), `repro_ling_crash.py`
  (the standalone reproducer; it rebuilds the 3,007-token request against any running server),
  `bsweep_2026-09-20.sh` and its three run files, the DeepSeek `deepseek_*_2026-09-20.sh` files, and the M2.7
  `MiniMax-M2.7_*` files, and for the 26 September run `Qwen3.8-Flash-Next_reads.py` (the four reads and their
  code checks) and `resident.py` (page-cache residency, read-only). They call our start scripts, which are not
  in the package; the settings that matter
  are in `derived/model_files.tsv`, `derived/builds.tsv` and the logs.
- `derived/reads.tsv`: every read the page quotes from a llama-server log in the sweeps and the 26 September
  run (card memory there is "after read"), one row each, parsed
  from the logs (tokens, seconds, t/s, tokens generated, decode t/s, code checks, card MiB and which kind).
  MiniMax M2.7's readings and the two-machine runs keep theirs in their own JSON and result files.
- `derived/model_files.tsv`: each model file's size and header fields (layers, experts), read from the GGUF
  headers without loading a model, and the placement during the sweep.
- `derived/builds.tsv`: the llama.cpp commit behind each binary, from each build's own build-info record.
- `derived/scripts_before_sweep.tsv`: what each of the 25 start scripts set before 20 September.
- `derived/excerpts.md`: the llama.cpp source lines, script lines, header fields and upstream report states the
  page cites.

## Provenance

- Machine: one desktop, one NVIDIA GeForce RTX 5090 (32 GB), 188 GiB of RAM; for the two-machine runs, an ASUS
  ROG Flow Z13 laptop over Thunderbolt using llama.cpp's RPC backend.
- Dates: 15 September (one depth read), 19 September (M2.7), 20 September (first pass, DeepSeek, M3 split
  buffers, just after midnight), 21 September (everything else), 26 September (Qwen3.8-Flash-Next at its served
  window, then Ornith-1.5-35B and Qwen3.5-122B-A10B at 262,144, MiniMax M2.7 at 196,608 and GLM-5.3-Flash at
  262,144 and 131,072). File times in the logs are the machine's local time.
- Temperature 0 on every sweep request; `max_tokens` 900 on sealed-code reads, 32 on stress prompts, 8 on the
  16,011-token DeepSeek comparisons, 32 on the M2.7 harness, 400 on the follow-up requests, 120 with thinking off
  on the 26 September Qwen3.8-Flash-Next reads, 300 with thinking off on the Ornith-1.5-35B and Qwen3.5-122B-A10B
  reads, 4,096 on MiniMax M2.7's, with thinking on, and 1,024 on GLM-5.3-Flash's, with its reasoning effort none;
  the 26 September stress checks asked for 160 and then 80 tokens at temperature 0.7.
- Every model output shipped here comes from a model running locally on this machine. No hosted model's output
  is in the package.

## Redactions, stated plainly

Nothing was changed in any file except the items below. Counts are over the whole package.

- **Paths:** 449 absolute paths in run files became `<REDACTED_PATH>/` plus the file's own name (a model file
  name, a source file name, or a script name; a settings file's name is not kept, it reads
  `<REDACTED_PATH>/<settings file>`). In the tools, 44 paths became named placeholders such as
  `<MODEL_DIR>`, `<OUTPUT_DIR>`, `<CUDA 12.8 libraries>` or `<llama.cpp build d3146f2b5>`.
- **Addresses and ports:** 179 occurrences of the desktop's bridge address in run files and 6 in the tools became
  `<LOCAL>` (with the port, where one followed); nine command-line ports next to it became `<PORT>`; 5 laptop link
  addresses became `<LAPTOP>`, and one laptop host alias in a tool became `<LAPTOP>`. Loopback addresses
  (`127.0.0.1`) and their ports are left as they were.
- **Process ids:** 47 became `<PID>`.
- **Private lines:** 253 log lines were deleted: 251 written by, or naming, a private helper process that runs
  beside some of our servers and plays no part in these measurements, and 2 notices naming a private system. No
  measurement line was deleted.
- **Internal names:** 74 run files and 14 tools were renamed from internal short names to public model names,
  and 74 occurrences of those short names inside files were changed the same way; 11 queue-log entries lost an
  internal prefix and a service port. For the 26 September run, 5 run files and 1 tool were renamed to carry
  the public model name, and the tool's 2 mentions of its old name changed with it. For the Ornith-1.5-35B and
  Qwen3.5-122B-A10B runs at 262,144, 8 run files were renamed to carry the public model name, and 84 occurrences
  of their run tags, settings-knob prefixes and script-copy names inside them, plus 4 serving aliases, changed the
  same way. For the MiniMax M2.7 run at 196,608, 2 run files and the stress check's folder were renamed the same
  way, and 16 occurrences of its run tags and settings-knob prefixes inside them, plus 1 serving alias, changed
  with them. For the GLM-5.3-Flash runs of 26 September, 8 run files and the stress check's folder were renamed the
  same way, and 45 occurrences of their run tags, settings-knob prefixes and script-copy names inside them, plus 3
  serving aliases, changed with them.
- **Tools, by hand:** 84 edits deleted sentences and blocks that named private systems or internal studies, or configured the helper
  process (each deletion is marked in place, for example `[one sentence removed from this copy]`), removed a list
  of internal service names, and reworded one comment whose English verb tripped our own leak check.
- **Response identifiers:** 3 fields (`id`, `system_fingerprint`, `created`) removed from one response.
- **Punctuation:** 68 em dashes in our own harness text (15 in console logs and one result note, 2 in a start
  script's note at the top of two 26 September server logs, 51 in script comments, messages and docstrings)
  became colons, two of them commas where a colon would not read, following the site's copy rule. None was in
  model output or in llama.cpp's own log lines. The package holds no en dash.
- **Not shipped:** our start scripts and their settings files (for the 26 September run: its copy of the start
  script, its driver script and its settings file), internal notes and working papers, the private reasoning
  recorded beside some results, two small test logs about the helper process, the 26 September run's
  process-id files, and, for the MiniMax M2.7 run at 196,608, its probe and stress drivers, card-memory samples and
  process-id files; the same for the GLM-5.3-Flash runs, and their copy of the start script.

Leak check: the sweep our packaging rules require (internal paths, staging-folder names, the hostname and
network names, the bridge and link addresses, the laptop's host names, operator keys, service names, and the
private system's vocabulary) was run over this whole tree after the last edit on 26 September 2026, both
case-sensitive and case-insensitive: no matches. A second sweep for the internal short names, non-loopback
ports and the helper process: no matches outside loopback addresses and the harmless word "warm" in cache
field names (point 12 above). An em dash sweep over the tree: no matches.

