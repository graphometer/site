# NUMBERS: every figure on the page, with its file and field

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

**The one place a file will look like it contradicts the page:** `excerpts/glm-4.7-full-start-script-mtp.txt`
part C prints `5.51 t/s` for the rung `131072/92/q5_1` and `7.02 t/s` for `131072/93/q5_1` as trailing comments
in a shell `case` statement, and part B prints `5.23` and `6.54` at 32K. Those are figures written into the
script on 17 September by the session that measured them ("3 runs per arm", its header says); the logs were not
kept, so nothing in this package shows a run producing them. The page prints them as "the script's own dated
note", says no kept log compares the draft head on and off at one window and placement, and takes the 5.51 it
prints from the September roster's row 13 (2026-09-12, paragraph replies, better of two), whose scope it
states. One more comment figure ships without a log: line 77 of `excerpts/qwen3.6-27b-start-script-kvargs.txt`
(line 90 in its part B) says "262144 MEASURED 2026-09-17: 27,947 MiB VRAM, 71.8 t/s, healthy in 13 s" and that
an f16 cache "wants 16 GB"; those are the script's comment, no file in this package shows the run behind them,
and the page does not use them. Everything else on the page is either measured in a file named below or
arithmetic on such a file.

Paths are relative to `data/`. Figures owned by another page are mapped to that page's package, the way that
page's own `NUMBERS.md` maps them; those packages live at `/batch-size/data/`, `/context-256k/data/`,
`/roster-2026-09/data/`, `/field-notes-2026-09/data/`, `/qwen38-256k/data/` and, for item 13,
`/describing-pictures/data/` (publishing with this page).

## Eyebrow, title, subtitle, lead, section 01

| figure | file and field |
|---|---|
| twelve items | the twelve item sections, 02 to 13 |
| 12 to 26 September 2026 | the earliest record is GLM-4.7 Full's 5.51 t/s, dated 2026-09-12 in the September roster (row 13); the latest are the 26 September starts and reads (items 02, 04, 06, 09) |
| RTX 5090, 32,607 MiB as nvidia-smi reports it | `/qwen38-256k/data/records/card-capacity.txt` (`same-card total 32607 MiB`) |
| 188 GiB of RAM, 24-core Core Ultra 9 285K | the site's standing machine description (the `/l3-threads/` environment table); not re-measured here |
| a 3,658-token read that took 17.5 times longer once one flag changed | **arithmetic**: 564.0 / 32.3 = 17.46 (item 05's M2.7 pair; the rates are mapped under item 05) |
| a card with 8,311 MiB of its 32,607 unused | `records/minimax-m2.7-placement-2026-09-19/placement.tsv`, row `cmoe`, `spare_below_32607_mib` (**arithmetic** in that file: 32,607 minus `card_after_load_mib` 24,296) |
| three items carry notes | items 10, 11 and 12 |

## 02 The window you pass is not the window you serve

| figure | file and field |
|---|---|
| 22 endpoints, all at 128K, on 15 September; ten rows serving more than 131,072 by default on 26 September | `/roster-2026-09/` section 05, its correction table row "The 15 September list: 22 endpoints, all at 128K"; the roster's own `NUMBERS.md` maps the ten rows |
| four starts with nothing passed, 21:06 to 21:13, served 262,144, 262,144, 196,608 and 262,144 | `/roster-2026-09/data/installed-starts-2026-09-26.txt`: `started` and `served n_ctx (GET /props)` for Ornith-1.5-35B-A3B (21:06:33, 262144), Qwen3.5-122B-A10B (21:07:29, 262144), MiniMax M2.7 (21:09:33, 196608), GLM-5.3-Flash (21:10:34, 262144; stopped 21:13:45) |

## 03 A window past the file's training length is capped

| figure | file and field |
|---|---|
| 524,288 asked, 262,144 served, no rope flags | `/field-notes-2026-09/data/flashnext-context/e_512k_norope.log` line 11 (the capping line) and line 12 (`n_ctx_slot = 262144`) |
| 23,816 MiB at peak; the capped server up in 2 seconds | `e_512k_norope.vram` (`result=UP`, `peak_vram_MiB=23816`, `elapsed=2s`) |
| 23,814 for a genuine 524,288 window with the flags | `/field-notes-2026-09/data/flashnext-context/b_512k_unlock.vram` (`peak_vram_MiB=23814`) |
| 15,394 on a plain 262,144 load, whose probe logged a 600-second timeout | `/field-notes-2026-09/data/flashnext-context/a_256k_base.vram` (`result=TIMEOUT`, `peak_vram_MiB=15394`, `elapsed=600s`); `a_256k_base.log` (the server loaded, `n_ctx_slot = 262144`) |
| 8,422 MiB more | **arithmetic**: 23,816 minus 15,394 |

## 04 A micro-batch that loads at one window fails at another

| figure | file and field |
|---|---|
| M2.7: 43,909 tokens at `-ub 4096` at 131,072; at 196,608 a 2,916.16 MiB buffer refused, 2048 failed, 1024 loaded at 31,560 MiB | `/batch-size/data/` as its `NUMBERS.md` section 04 row maps them: `one_ub4096_cmoe_ctx131072.json`; `one_ub4096_cmoe_ctx196608.server.log` (`allocating 2916.16 MiB`); `one_ub2048_cmoe_ctx196608.server.log` (`CUDA error: out of memory`); `one_ub1024_cmoe_ctx196608.json` (`config.vram_mib` 31560). The 43,909-token file is also `records/minimax-m2.7-placement-2026-09-19/one_ub4096_cmoe_ctx131072.json` here (`sizes.49152.cold.prompt_n`) |
| GLM-5.3-Flash at 262,144: 4096 refused, a 13,281.37 MiB compute buffer; 2048 read 230,039 tokens, peak 31,951 MiB, 656 below the total; ships 1024 | `/batch-size/data/runs/2026-09-26_glm-5.3-flash-served-window/GLM-5.3-Flash_256k_ub4096.result` and `_ub2048.result`, as the batch-size `NUMBERS.md` section 04 rows map them; 656 is that page's arithmetic against 32,607 |
| four other scripts returned to the default above 131,072 until 26 September; that day two were measured at 262,144: Ornith-1.5-35B's script now sets `-b 2048 -ub 2048` there, Qwen3.5-122B's keeps 512; Qwen3.5-397B and Mistral Small 4 still return to the default, unmeasured | `/batch-size/` section 04, the two "Update, 26 September" paragraphs, and its `derived/excerpts.md` |

## 05 An inherited micro-batch

| figure | file and field |
|---|---|
| 17.5 times on a 3,658-token read; 19.9 times on a 24,071-token read | **arithmetic**: 564.0 / 32.3 = 17.46 and 1,434.0 / 72.2 = 19.86 on the rates below; the batch-size page's `NUMBERS.md` computes the same ratios as 17.47 and 19.85 from the unrounded rates (564.0 / 32.278; 1434.01 / 72.23) |
| the server logs we kept do not print the batch sizes at load | two logs read for this page: the M2.7 `A_ub128_cmoe.server.log` (29 lines, `verbosity = 3`) and the 21 September `Laguna-S-2.1_skip.log` (`verbosity = 3`), neither containing `n_batch` or `n_ubatch`; both ship in the batch-size package |
| 512, the build's default | `/batch-size/data/derived/excerpts.md` section 1 (`common/common.h`: `n_ubatch = 512`) |
| Laguna S 2.1: `--batch-size 512 --ubatch-size 128` from July to 21 September; 32,768 window; 24,071 tokens; 333.2 s at 72.2 t/s; 16.8 s at 1,434.0 t/s with `-b 8192 -ub 8192`; the code correct at both; decode 18.40 to 16.50 on the 12-token answer | `/batch-size/data/runs/2026-09-21_sweep/Laguna-S-2.1_skip.result` and log (`n_ctx_slot = 32768`; prompt eval 333,246.19 ms / 24,071 tokens), `Laguna-S-2.1_8192.result` and log (16,785.77 ms; 12 tokens at 16.50), as the batch-size `NUMBERS.md` section 03 row (24,071; 72.2; 1,434.0; 18.40 and 16.50 (12)) and section 06 row map them; the July script lines in its `derived/excerpts.md` |
| M2.7 first judged at `-cmoe -ub 128`, the M3 script's pair; `-b 4096` held, every expert layer in RAM, 131,072; 3,658 tokens at 32.3 t/s at `-ub 128` and 564.0 at `-ub 4096` | `/batch-size/data/runs/2026-09-19_minimax-m2.7/A_ub128_cmoe.json` (`config`: `ctx` 131072, `place` cmoe, `kv` q8_0, `ub` 128; `sizes.4096.cold.prefill_tps` 32.278) and `CONFIRM.console.log` (564.0), as its `NUMBERS.md` maps them; `-b 4096` throughout per `/field-notes-2026-09/` section 03 and the harness `MiniMax-M2.7_sweep.sh` in the batch-size package; the M3 script's `-cmoe -b 4096 -ub "$UB"` line is `excerpts/minimax-m3-msa-fallback.txt` line 142 here |
| the 96,000-token check scored "l128 recall 0/3" when the turn ended at 1,800.4 seconds; timed out against `-ub 128` | the 1,800.4 seconds and the `-ub 128` cause: `/field-notes-2026-09/` section 03; the score string: that page's section 15 ("written down as "l128 recall 0/3"") and its `data/wave2/CORRECTION.md` (the per-leg fields `latency_s` 1800.4, `hits` 0, and the score string), as the field notes' `NUMBERS.md` row 30 maps it |

## 06 The first read after a start pages the file in

| figure | file and field |
|---|---|
| 90 GB file; none in memory at start, 43.5 GB after the load; first request 3,035 tokens at 87.7 t/s while the share grew to 57.7 GB; next 3,019 tokens at 517.6 | `/batch-size/data/runs/2026-09-26_qwen3.8-flash-next-served-window/` (`resident_gb` before and after; the two reads), as the batch-size `NUMBERS.md` section 04 rows map them; the same figures on `/context-256k/` section 04 |
| the default's server: 60.05 GB in memory; 253.7 then 255.7 | same folder, `run.console.log` (`resident_gb` 60.05) and the two reads |

## 07 Every expert in system memory leaves the card idle

All from `records/minimax-m2.7-placement-2026-09-19/`; `placement.tsv` carries every value with its file.

| figure | file and field |
|---|---|
| UD-IQ4_XS; build 10919; 131,072 window; 8-bit cache; `-ub 4096`; 43,909-token prompt; 32-token answer; one run per placement | each file's `config.quant`, `config.build` (`10919/d3146f2b5`), `config.ctx`, `config.kv` (`q8_0`), `config.ub`; `sizes.49152.cold.prompt_n` (43909) and `predicted_n` (32); one `cold` and one `warm` block per file |
| every expert layer in RAM (`-cmoe`): 24,296 MiB after load; 9.04 t/s decode; 640.2 t/s reading; repeat 8.95 | `one_ub4096_cmoe_ctx131072.json`: `config.vram_mib`, `sizes.49152.cold.decode_tps` (9.0436), `cold.prefill_tps` (640.205), `warm.decode_tps` (8.9530) |
| 8,311 below 32,607; the spare column | **arithmetic**: 32,607 minus 24,296 (and the other rows the same way); the card total from `/qwen38-256k/data/records/card-capacity.txt` |
| 61 of 62: 25,884 MiB; 8.97 t/s; 636.2 t/s; repeat 9.08 | `one_ub4096_61_ctx131072.json`: the same fields (8.9718; 636.204; 9.0847) |
| 60 of 62: 27,483 MiB; 9.27 t/s; 644.9 t/s; repeat 9.48; "gained 0.23" | `one_ub4096_60_ctx131072.json` (9.2728; 644.857; 9.4784); **arithmetic**: 9.27 minus 9.04 |
| 59 of 62: 29,094 MiB; 9.83 t/s; 656.5 t/s; repeat 9.77 | `one_ub4096_59_ctx131072.json` (9.8343; 656.476; 9.7705) |
| 58 of 62: 30,695 MiB; 10.02 t/s; 666.1 t/s; repeat 9.68 | `one_ub4096_58_ctx131072.json` (10.0184; 666.148; 9.6837) |
| the repeat moved by up to 0.34 t/s (58 layers: 10.02, then 9.68); the 0.19 step from 59 to 58; the whole gain under one token a second | **arithmetic**: 10.02 minus 9.68; 10.02 minus 9.83; 10.02 minus 9.04 = 0.98 |
| the script's default at 131,072 is 59; at 196,608 it forces every expert into RAM with `-ub 1024`; 196,608 the default since 26 September; 62 layers | `excerpts/minimax-m2.7-window-and-placement.txt`: line 82 (`NCMOE` default 59), line 96 (196608 "default since 2026-09-26"), lines 112 to 119 (the branch that sets `NCMOE=cmoe` and the micro-batch to 1024), lines 263 to 264 (`-cmoe` and "all 62") |
| a start with no window passed on 26 September held 31,512 MiB at load | `/roster-2026-09/data/installed-starts-2026-09-26.txt`, MiniMax M2.7: `served n_ctx (GET /props): 196608`, `card at load: 31512 MiB, 32607 MiB` |
| a 17 September pass kept no per-arm logs | the placement-sweep summary named in `SOURCES.md` (not shipped); nothing in this package |

## 08 Sparse attention that runs dense

| figure | file and field |
|---|---|
| runs dense unless flash attention is on and one sequence per stream (one slot, or a cache that is not unified); one warning line | `excerpts/minimax-m3-msa-fallback.txt`, source lines 228 to 244 (`fa_on`, `streams_ok`, `msa_enabled`, the two `LLAMA_LOG_WARN` strings) |
| commit d3146f2b5, build 10919 | same file, the `build-info.cpp` lines |
| checked against the upstream file at that commit on 26 September | same file's heading; the check is described in `SELF_CHECK.md` |
| the harness greps for those strings; the script sets `--flash-attn on --parallel 1` | same file, harness lines 85 to 89 and script lines 140 and 143 |
| zero indexer tensors among 948; every M3 number before the correct file arrived on 20 September a dense fallback | `/field-notes-2026-09/data/minimax-m3/MEASUREMENTS.md` section 1, as the field notes' `NUMBERS.md` row 82 maps it; the correct file's date from that page's section 04 |

## 09 A cache the script promised and never set

| figure | file and field |
|---|---|
| the comment's promise; `KVARGS` expanded at the launch line; no assignment | `excerpts/qwen3.6-27b-start-script-kvargs.txt` part A: lines 77 to 79 (the comment), 196 (the expansion), and the history block (`lines assigning KVARGS: none` for every copy before the 26 September edit) |
| 17 September 16:10 to 26 September | same file: the file time of the copy `bak-20260921-141932-m27` (2026-09-17 16:10, the first copy with the promise and the expansion) and the file time of the edited script (2026-09-26) |
| "deliberately not offered" two lines below the check | same file, part A line 82 |
| the assignment added on 26 September; the copy dated 2026-09-26 22:28 says "started with an f16 cache that cannot fit" | same file, part B lines 188 to 193 (the copy's file time is in the part B heading) |
| bash 5.2, `set -u` on, no error; an unassigned array expands to nothing | `excerpts/kvargs-expansion-check.txt` (bash 5.2.21; the first two commands print `[x]` `[y]` with exit code 0) |

## 10 A settings file wins over your environment

| figure | file and field |
|---|---|
| nineteen of the 26 start scripts source their settings file before any `${VAR:-default}` read; the twentieth, MiniMax M2.7, reads only the file's own location first; six have no settings file | `excerpts/settings-file-order.txt`: the table (26 rows) and its count line (20 name and source a file; 19 source it before the first read; MiniMax-M2.7 sourced at line 80 after a read at line 76; six `never`) |
| the transcript: exported 8199, script binds 8116 | same file, the last block (`exported FOO_PORT=8199 ... binds 8116`, exit code 0) |
| two verification runs misread as failures, 17 September | the session note named in `SOURCES.md` (a note; not shipped; the page says so) |

## 11 A header that said the draft head did not work

| figure | file and field |
|---|---|
| the old header's claim; the new header | `excerpts/glm-4.7-full-start-script-mtp.txt` parts A and B |
| `graph_mtp` 252 times in the library's strings; 444-line and 284-line `glm4-moe.cpp`; identical md5 of the library in both places | same file, part E |
| from 12 September, serving at 131,072, to 17 September | `/roster-2026-09/` row 13 ("131,072 with a 5-bit cache, as served on 2026-09-12"); the file time of the first copy holding the new header (2026-09-17 13:42, in the excerpt's heading) and the header's own date |
| 5.51 t/s on paragraph replies, better of two, 2026-09-12, 131,072, 5-bit cache, llama.cpp's default batch, before the head | `/roster-2026-09/` row 13, its speaking cell and window cell ("llama.cpp's defaults") |
| that figure at the rung `131072/92/q5_1`, the experts of 92 layers in RAM | `excerpts/glm-4.7-full-start-script-mtp.txt` part C line 104 (`5.51 t/s   the pre-MTP default; no draft-mtp at this rung`) (a script note) |
| 7.02 for `131072/93/q5_1` with the draft head; at 92 with the head, "failed to create MTP context" | same file, part B lines 45 to 46 and part C line 103 (a script note; logs not kept) |
| 7.41 at 65,536, `--n-cpu-moe 92`, head on | same file, part B line 44 and part C line 106 (a script note) |
| the matched pair at 32,768 and `--n-cpu-moe 92`: 5.23 without the head, 6.54 with it, three runs per arm | same file, part B lines 41 to 43 (a script note) |

## 12 A flag in --help the build cannot load

| figure | file and field |
|---|---|
| `draft-dspark` listed in `--help`; the loader message | `excerpts/deepseek-draft-flag.txt`: the type table (older build's `speculative.cpp` lines 31 to 42, and the helper that joins it for the help text), the loader message (`llama-model-loader.cpp` line 281), and the script note's quoted words |
| commit 5f55650 (older build); d3146f2b5 (newer) | same file, the build identities |
| the pattern key required whenever a window is set: `dflash.cpp` lines 25 to 27 | same file (`ml.get_key_or_arr(LLM_KV_ATTENTION_SLIDING_WINDOW_PATTERN, ...)` with no optional argument, inside `if (ml.get_key(LLM_KV_ATTENTION_SLIDING_WINDOW, hparams.n_swa, false) && hparams.n_swa > 0)`) |
| the newer build's DSpark branch reads the window and not the pattern | same file, newer build's `dflash.cpp` lines 38 to 42 (entered on `hparams.dsv4_hc_mult > 0`) |
| the draft's header: `dflash.attention.sliding_window = 128`; no pattern key; `hyper_connection.count = 4` | `records/deepseek-draft-header-keys.txt` |

## 13 Ollama's default thread count on the CPU

All timings from `records/ollama-threads-2026-09-20.tsv`; the default row from `records/qwen3vl30b_cpu.log`; the
thread count and the version from the server log excerpt the sibling page ships.

| figure | file and field |
|---|---|
| Qwen3-VL 30B-A3B, Ollama, CPU, first picture (a 4K nebula), cold with the load included | columns `model`, `device`, `picture` (`01_nebula_large.jpg`), `cold`, `load_s` |
| Ollama 0.30.10, the version the serving process logged when it started on 19 September | `/describing-pictures/data/service-log/ollama_2026-09-20_excerpt.txt` line 9 (`Listening on ... (version 0.30.10)`, 2026-09-19); the sibling page's "Server" row says the same |
| the card all but empty: 1,040 MiB in use | `records/qwen3vl30b_cpu.log` line 3 (`GPU MiB: 1040`) |
| with no thread count set, `n_threads = 4 (n_threads_batch = 4) / 24` | `/describing-pictures/data/service-log/ollama_2026-09-20_excerpt.txt` line 42 (the `system_info` line of the server launched at 08:20:56 with no thread flag); the sibling page's section 04 "Where the 4 comes from" |
| default: 273.17 s wall; 4,154 tokens in 242.93 s | `qwen3vl30b_cpu.log` line 2 (`wall=273.17s`, `img+prompt=4154tok/242.93s`); the same read in the server log excerpt, line 52 (`prompt eval time = 242931.43 ms / 4154 tokens`) |
| 8 threads: 157.31 wall, 123.53 processing; 16: 111.01, 87.77; 24: 107.88, 76.57 | rows `qwen3vl30b_cpu_t8.json`, `_t16.json`, `_t24.json`: `wall_s`, `prompt_s` |
| 16 threads, 1,536-pixel cap: 1,370 tokens in 18.17 s, 38.52 s wall | row `qwen3vl30b_cpu_t16_px1536.json`: `prompt_tokens`, `prompt_s`, `wall_s` |
| answers of 174 to 303 tokens | column `out_tokens` (174, 303, 193, 208, 207) |

## 14 to 18

No new figures. Section 16's counts: three items with a prior correction on a published page (02: roster
section 05; 05: batch-size section 13 and field notes section 03; 08: field notes section 04), three traps
measured and printed before without a wrong record (03: field notes section 09; 04 and 06: batch-size section
04), five corrected here first (07, 09, 10, 11, 12), and item 13 on the page publishing with this one. The dates
table in section 18 repeats dates mapped above.
