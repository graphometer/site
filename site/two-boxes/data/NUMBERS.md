# Numbers: every figure on the page, and the file it came from

**Standing sentence: if a number on the page disagrees with a file in this package, the file is right and the page
is wrong.** Tell us and we will fix the page.

Revised 2026-09-26 for the cut version of the page. Tables and write-ups that left the page that day are in
`moved-from-the-page-2026-09-26.md`; the last part of this file maps them, and the page's sections are numbered as
they now stand (01 to 12).

## The places a file will look like it contradicts the page

1. **Two speaking figures for the same pair.** The page says the pair spoke DeepSeek V4 Flash's 3-bit file at
   **15.9 to 17.1** tokens a second on 13 September (section 04) and at **14.76** on 21 September. Open
   `logs/deepseek-3bit-8-10-25.log` and `same-file-2026-09-21/pair-ub512.result` and you will find both, for the
   same file, placement and build commit: the first at a 131,072-token window on a filler prompt, the second at
   262,144 on a ledger prompt. Two more nights sit between them (`moved-from-the-page-2026-09-26.md`, section 2).
2. **A reading time and a whole-request time for the same request.** The page prints both: at 48,024 tokens the
   desktop spent 69.5 seconds reading the prompt (the server's `prompt eval time`) inside a 75.2-second request (the
   probe's `wall_s`). The DeepSeek V4 Flash card prints the whole-request times; both pages use the same digits.
3. **The desktop's 150,103-token run says `ubatch=skip`.** The page labels it `-b/-ub 4096` and says why in the
   table note: `README.md`, contradiction 10.

Column key: **file** is the file in this package; **where** is the block, line marker or field. Rows marked
**not shipped** name the record they come from and why it cannot ship (`README.md` has the reasons).

## Title spots, hero, the two notes, section 01

| figure on the page | value | file | where |
|---|---|---|---|
| a 48,024-token request answered in 75.2 s alone, 416.4 s on the pair at `-b/-ub 2048` (its best completed setting) and 474.2 s at the kept `-b 2048 -ub 512` (subtitle, og and twitter descriptions, "What to set", summary 1 and 5) | `wall_s` 75.2, 416.4, 474.2 | `same-file-2026-09-21/desktop-ub4096.result` (`#2`), `pair-ub2048.result` and `pair-ub512.result` (`size 48000`) | the probe's wall clock from request to finished answer |
| of which reading: 69.5 s alone, 468.4 s at 512, 410.5 s at 2,048 | 69,512.49 ms; `read_s` 468.4; `read_s` 410.5 | `desktop-ub4096.log` (task 61 `prompt eval time`); `pair-ub512.result`; `pair-ub2048.result` | |
| 2,048 finished and was faster; 512 kept as a precaution after the 4,096 failure | `needle_in_answer` true at 2,048; the 4,096 failure below | `pair-ub2048.result`; `pair-ub4096.log` | |
| read a long prompt 12.3 times faster (meta description), each machine at its own setting | 632.1 against 51.4 | `desktop-ub4096-150k.result`, `pair-ub512-150k.result` | `prefill_tps` |
| ten models tried | eight 13 to 15 September, Mistral Medium 3.5 on 16 September, MiniMax M3 on 20 September | `logs/`, `mistral-medium-3.5-pair-2026-09-16/`, `minimax-m3-pair-2026-09-20/` | one run folder or log per model |
| 128 GB laptop, RTX 5090 | as in section 02 | see section 02 | |
| 283.03 GiB file larger than either machine's memory | `file size = 283.03 GiB` | `logs/model-headers.txt` | Kimi block |
| 14.76 against 12.65 on 2,998 tokens (about a sixth) | `decode_tps` 14.76 and 12.65 | `same-file-2026-09-21/pair-ub512.result`, `desktop-ub4096.result` | `size 3000` line; `#1` line |
| a quarter of llama.cpp's default micro-batch; at the default the desktop read faster on a shorter prompt, 3,658 tokens against the pair's 7,844 | `-ub 128`; 100.77 on 3,658; 70.4 on 7,844 | `other-models-desktop/minimax-m2.7-2026-09-13-launch-and-timings.txt`; `other-models-desktop/minimax-m2.7-2026-09-19/A_ub512_cmoe.json`; `logs/minimax-m2.7-pair.log` | the `-cmoe -ub 128` launch line; `sizes.4096.cold`; `[depth~8000]` |
| GLM-4.7 Full and the control not re-run after the batch change | no later run of either in this package | `logs/glm-4.7-full-pair.log`, `logs/control-glm-4.7-flash.log` | dated 2026-09-13 |
| the laptop's side failed 40,960 tokens into a 48,024-token read | last progress line `n_tokens = 40960`, then `Remote RPC server crashed or returned malformed response` | `same-file-2026-09-21/pair-ub4096.log`; `pair-ub4096.result` | the last `prompt processing` line and the next two lines |
| summary 1: 690.9 and 632.1 alone; 102.5 and 51.4 on the pair; whole requests 75.2 against 474.2 and 244.8 against 2,933.8; reading 237.5 s and 2,922.9 s (48.7 minutes) | `prefill_tps`; `wall_s`; `prompt eval time` 237,469.00 ms; `read_s` 2922.9 | `desktop-ub4096.result`, `desktop-ub4096-150k.result` (and its log), `pair-ub512.result`, `pair-ub512-150k.result` | |
| summary 2: 12.04 against 12.16 at 48,024; 7.66 against 11.79 at 150,103; 226.8 to 30.7 | `decode_tps`; stretch rates | the four result files; `same-file-2026-09-21/stretch_rates.txt` | the first and last rows |
| summary 3: 400.71 B and 1.03 T parameters; 283.03 GiB | header lines | `logs/model-headers.txt` | Maverick and Kimi blocks |
| summary 4: 5.54 on a 441-token prose reply; 1.97 on the desktop record | see section 05 | | |
| summary 5: 14 percent; 416.4 against 474.2 | 117.0 against 102.5; `wall_s` | `pair-ub2048.result`, `pair-ub512.result` | `size 48000` lines |
| summary 6: 63.80, 67.97, 63.86 on answers of 54, 10 and 8 tokens; 223.65 on replies of about 200 tokens | `eval time` lines of tasks 0, 55 and 66 | `logs/control-glm-4.7-flash.log`; the desktop figure **not shipped** (the 2026-09-12 sweep) | |
| 17 September: the same 3-bit file measured alone, 13.5 (section 04) | 13.5 | `placement-2026-09-17-extract.md` | the table; provenance stated there |

## Section 02, the bench

| figure | value | file | where |
|---|---|---|---|
| card | 32,086 MiB as llama.cpp reports it | `logs/control-glm-4.7-flash.log` | device probe line, `CUDA0` |
| card, second reading | 32,607 MiB as nvidia-smi reports it | `long-reads-2026-09-15/context-256k-deepseek-rows.tsv` is silent on it; the figure is the site's standing bench reading, printed on every page | **not shipped**: no run in this package produced it |
| threads | 16 of 24 in the control run; 24 in the others | `logs/control-glm-4.7-flash.log` (`system_info: n_threads = 16 ... / 24`); every other launch line (`--threads 24`) | |
| memory | 192,591 MiB, which is 188 GiB | `logs/control-glm-4.7-flash.log` | device probe line, `CPU` |
| CUDA | 12.8.93 | `logs/build-cuda-version.txt` | both lines |
| sm_120 | `ARCHS = 1200` | `logs/control-glm-4.7-flash.log` | `system_info` line |
| laptop's graphics device | Radeon 8060S, `uma: 1`, `fp16: 1`, `bf16: 0`, `fp4: 0` | `logs/deepseek-8bit-matched-worker.log` | `ggml_vulkan` device line |
| memory the laptop offered | 110,592 MiB total, 109,602 MiB free | `logs/control-glm-4.7-flash.log` | device probe line, `RPC0` |
| the laptop holds the attention cache of its layers | `llama_kv_cache: RPC0[<LAPTOP>] KV buffer size = ...` | `logs/deepseek-3bit-8-10-25.log`, `logs/minimax-m2.7-pair.log`, `logs/qwen3-235b-pair.log` | the `RPC0 KV buffer` lines in the placement block |
| 284 billion parameters, from the file's header | 284 billion, 256 experts, 6 used per token plus 1 shared | `placement_knobs.txt` | the identity line recorded when the file was installed |
| the maker's 304B | 304B | **not shipped**: the maker's repository page, read 2026-09-15 | the maker's card in `vendor/` at revision `7872f01b` states no parameter count |

## Section 03, what we ran

The link figures are printed on the page in one sentence; their table is in `moved-from-the-page-2026-09-26.md`, section 1.

| figure | value | file | where |
|---|---|---|---|
| build 10919, commit `d3146f2b5`, GNU 13.3.0 | as printed | `logs/control-glm-4.7-flash.log` | first line |
| worker binary 196,848 bytes, built 2026-09-13 21:08 | as printed | `logs/deepseek-8bit-matched-worker.log` | the build block |
| later pair runs and the 21 September desktop runs on the same commit; `5f55650a7` and `c8e03ce81` for the other desktop runs | full commit ids | `build-and-file-status-2026-09-26.txt` | "llama.cpp builds" |
| link: 0.157 / 0.667 / 0.820 ms, 0% loss, 30 packets | as printed | `link/ping.txt` | whole file |
| link: 2,092 to 2,120 MB/s (16.7 to 17.0 Gbit/s); 1,107 to 1,111 MB/s (8.9 Gbit/s); 1 MiB writes, 2 GB per run | as printed | `link/tcp_up_run*.txt`, `link/tcp_down_run*.txt`, `link/tcp_client.py`, `link/RUN_LOG.txt` | both lines of each; the write loop |
| windows: 131,072 on 13 to 14 September, 8,192 for the control, 262,144 on the 15 and 21 September rows | `n_ctx_slot` | `logs/control-glm-4.7-flash.log` (8192); the 13 September run headers ("128K"); `long-reads-2026-09-15/*.log` and `same-file-2026-09-21/*.result` (262144) | `n_ctx_slot` or the `served:` line |
| default batch sizes `-b 2048 -ub 512` on the pair until 21 September | the pair's launch lines carry no batch flag; the 21 September kept rung is `ubatch=512 batch=2048` | `long-reads-2026-09-15/pair-262k.log` (`[cmd]` line), `same-file-2026-09-21/pair-ub512.result` | first lines |
| probe shapes: 21 to 55-token short probe, up to 200 tokens, about 8,000 and 16,000 tokens of depth | as described | `probe_speed.py`, `probe_fresh_prefill.py`; `logs/*` `[short]` and `[depth~N]` lines | |
| the ledger probe; codes at 5, 50 and 95 percent on the long reads; identical 21 September prompts of 2,998, 48,024 and 150,103 tokens | as described | `same-file-2026-09-21/turn_probe.py`, `desktop_driver.sh` (its embedded probe), `long-reads-2026-09-15/deep_recall_probe.py`; the `prompt_n` fields | |
| a whole-request time is the probe's wall clock; a reading time is the server's prompt evaluation | `wall_s`; `prompt eval time` or `read_s` | `same-file-2026-09-21/desktop_driver.sh` and `turn_probe.py` | how `wall_s` is taken |
| dates | 13 to 21 September | each file's timestamps; `README.md` lists them per folder | |

## Section 04, the same file on one machine and on two (21 September)

| figure | value | file | where |
|---|---|---|---|
| 3-bit file 104.2 GB | shard byte counts | `logs/deepseek-3bit-8-10-25.log` | the four shard lines |
| experts of 36 of 43 layers in system memory alone; 8 / 10 / 25 on the pair | `--n-cpu-moe 36`; `card whole 0-7 · experts-in-RAM 8-17 · <LAPTOP> 18-42` | `placement-2026-09-17-extract.md` for the placement's meaning; `same-file-2026-09-21/pair-*.log` first line | |
| desktop `-b/-ub 4096`: 539.6 / 690.9 / 632.1 reading, 12.65 / 12.16 / 11.79 speaking | as printed | `desktop-ub4096.result` (`#1`, `#2`), `desktop-ub4096-150k.result` (`#1`) | `prefill_tps`, `decode_tps` |
| desktop `-b 4096 -ub 2048`: 208.1 / 426.5 / 403.8 (149,898 tokens), 12.62 / 12.29 / 11.80 | as printed | `desktop-ub2048.result` | `#1`, `#2`, `#3` |
| pair `-b 2048 -ub 512`: 161.8 / 102.5 / 51.4, 14.76 / 12.04 / 7.66 | as printed | `pair-ub512.result`, `pair-ub512-150k.result` | the JSON lines |
| pair `-b/-ub 2048`: 224.9 / 117.0, 14.61 / 11.70 | as printed | `pair-ub2048.result` | the JSON lines |
| pair `-b/-ub 4096`: 250.5, 14.39; the 48,024-token read failed after 40,960 tokens | as printed | `pair-ub4096.result`, `pair-ub4096.log` | the JSON lines; the last progress line |
| short answers of 59 to 86 generated tokens | 59, 67, 68, 69, 73, 82, 83, 86 | the `eval time` lines of the seven logs; `gen_n` in the pair results | |
| 400-token replies within 3 percent: 14.73, 12.05, 7.85 | `warm_decode_tps` | `pair-ub512.result`, `pair-ub512-150k.result` | `warm_*` fields |
| 3.3, 6.7, 12.3 times | 539.6/161.8, 690.9/102.5, 632.1/51.4 | derived from the rows above | arithmetic |
| time to the answer, reading: 69.5 s, 410.5 s, 468.4 s at 48,024; 237.5 s and 2,922.9 s (48.7 min, and 237.5 s is 4.0 min) at 150,103 | `prompt eval time` in ms, or `read_s` | `desktop-ub4096.log`, `pair-ub2048.result`, `pair-ub512.result`, `desktop-ub4096-150k.log`, `pair-ub512-150k.result` | task lines for 48,024 and 150,103 tokens; `read_s` |
| time to the answer, whole request: 75.2 s, 416.4 s, 474.2 s at 48,024; 244.8 s and 2,933.8 s at 150,103 | `wall_s` | `desktop-ub4096.result` (`#2`), `pair-ub2048.result`, `pair-ub512.result`, `desktop-ub4096-150k.result`, `pair-ub512-150k.result` | |
| the 150,103-token desktop run: `ubatch=skip`, the fast preset, card 28,570 MiB at load against 28,490 (the explicit 4,096 run) and 27,092 (2,048) | as printed | `desktop-ub4096-150k.result` and `.log` (first line `preset=fast`); `desktop-ub4096.result`; `desktop-ub2048.result` | `healthy` lines; `README.md` contradiction 10 |
| at the same micro-batch of 2,048: the pair slightly faster on 2,998 tokens (224.9 against 208.1) and 3.6 times slower at 48,024 (117.0 against 426.5) | 426.5/117.0 | `pair-ub2048.result`, `desktop-ub2048.result` | arithmetic; the desktop rung used `-b 4096`, the pair `-b 2048` (`desktop_driver.sh`, `pair_chain.sh`) |
| the stretch table, in tokens a second: 690.7, 673.7, 614.6, 573.7; 226.8, 75.2, 43.3, 30.7 | as printed; the last desktop stretch is 4,096 tokens over 223.46 minus 216.32 seconds, 573.67 | `same-file-2026-09-21/stretch_rates.txt`, recomputed by `stretch_rates.py` from the two 150,103-token logs | the four rows |
| about a sixth; level; faster | 14.76/12.65 = 1.17; 12.04 and 12.16; 11.79 and 7.66 | derived | |
| 39 and 14 percent from 512 to 2,048 | 224.9/161.8 and 117.0/102.5 | derived | |
| the worker serving again three minutes later | failure at 22:39:31 (log start 22:31:58 plus the server clock 7:33); next run's log starts 22:42:14 and reaches `listening` | `pair-ub4096.log`, `pair-ub512-150k.log` | first lines and the failure line |
| next turn: 238 tokens, 5.4 s; 228, 5.0 s; changed question: 533, 10.0 s; 2,065, 28.2 s | `next_*` and `warm_*` fields | `pair-ub512.result`, `pair-ub2048.result` | `size 48000` lines |
| at 150,103 deep: 239 tokens in 9.7 s; 533 in 20.7 s | as printed | `pair-ub512-150k.result` | `next_*`, `warm_*` |
| 13 September band 15.9 to 17.1 and 184.6 to 187.9 on about 8,000 tokens | as in `moved-from-the-page-2026-09-26.md`, section 2 | `logs/deepseek-3bit-8-10-25.log` | probe lines |
| 12 September check: 9.7 and 9.2 speaking; about 75.5 and 73.8 reading (the harness's estimate) on counted prompts of 52,931 and 102,481 tokens | `decode_tps`, `prefill_tps_approx`, `prompt_tokens` | `gate/desktop-8bit-2026-09-12.json` | `l64.A_recall`, `l128.A_recall` |
| 17 September: 13.5 | as printed | `placement-2026-09-17-extract.md` | the `--n-cpu-moe 36` row |
| the laptop alone read 48,024 tokens at 56.7 | as printed | `same-file-2026-09-21/laptop-alone-131k-ub512.result` | `size 48000` line |
| the laptop-side notes (driver reset, worker restart) | not a measurement | **not shipped**: our notes from the laptop's system log that night; the log itself was not kept | `README.md`, withheld list |

## Section 05, the other models

The page prints a shortened table; `moved-from-the-page-2026-09-26.md`, section 3, has every cell. Both are mapped here.

| model | figures on the page | file | where |
|---|---|---|---|
| GLM-4.7-Flash control | 29.94 B, 16.31 GiB; 8,192 window; 63.80 on 54 tokens, 67.97 on 10 and 63.86 on 8 speaking; 1,125.28 on 1,940 tokens; 63.49 on 22 tokens (prompt evaluation) | `logs/model-headers.txt`; `logs/control-glm-4.7-flash.log` | header block; `n_ctx_slot = 8192`; `slot print_timing` tasks 0, 55, 66 |
| GLM-4.7-Flash alone | 223.65 speaking (best of two ~200-token replies), 4,447.44 on 20,221 tokens at 131,072 | **not shipped**: the desktop-only sweep of 2026-09-12 | its table's header defines `decode_tps` as the best of two warm ~200-token replies |
| Qwen3-235B pair | 235.09 B, 132.39 GiB; 5.97 on 49 tokens, 5.54 on 10 tokens at depth, 97.6 on 7,844 tokens | `logs/model-headers.txt`; `logs/qwen3-235b-pair.log` | `[short]`, `[depth~8000]` |
| Qwen3-235B alone, 12 September | 6.93 (best of two ~200-token replies, 0.6B draft), 251.58 on 21,493 tokens | **not shipped**: the 2026-09-12 sweep | as above |
| Qwen3-235B alone, 21 September | 285.8 on 48,020 tokens at the defaults; 703.3 at `-b 4096 -ub 2048`; 944.2 at `-b/-ub 4096`, code found, 131,072 window | `other-models-desktop/qwen-2026-09-21/qwen3-235b-default.result`, `qwen3-235b-ub2048.result`, `qwen3-235b-ub4096.result` | the JSON line; the build is `c8e03ce81` (`build-and-file-status-2026-09-26.txt`) |
| a prompt a sixth as long | 7,844 against 48,020 | derived | |
| MiniMax M2.7 pair | 228.69 B, 100.96 GiB; 9.66 on 401 tokens; 8.98 on 128 tokens; 70.4 on 7,844 tokens | `logs/model-headers.txt`; `logs/minimax-m2.7-pair.log` | `[short]`, `[depth~8000]` |
| MiniMax M2.7 alone, 13 September | 9.8 to 10.2 across eight timings (9.80 to 10.19; replies of 64 to 900 tokens, the 900 all hidden reasoning cut off at the length limit); 45.6 on 6,776 tokens; `-ub 128`, 64K window, f16 cache | `other-models-desktop/minimax-m2.7-2026-09-13-launch-and-timings.txt` | the eight `eval time` lines; task 129's `prompt eval time`; the exec block; the banner line |
| MiniMax M2.7 alone, 19 September | 100.8 on 3,658 tokens at `-ub 512`; 656.5 on 43,909 tokens at `-ub 4096` (experts of 59 layers in RAM); q8_0 cache; build `10919/d3146f2b5` | `other-models-desktop/minimax-m2.7-2026-09-19/A_ub512_cmoe.json`, `one_ub4096_59_ctx131072.json` | `sizes.*.cold.prefill_tps`, `config` |
| GLM-4.7 Full | 358.34 B, 135.15 GiB; 5.66, 5.59, 51.1; alone 5.51 and 61.36 on 20,221 tokens with a q5_1 cache | `logs/model-headers.txt`; `logs/glm-4.7-full-pair.log`; alone **not shipped** (2026-09-12 sweep) | |
| Qwen3.5-397B pair | 402.94 B, 139.54 GiB; 5.18, 12.61 on 10 tokens, 15.31 on 108 tokens; 98.7 and 108.2 | `logs/model-headers.txt`; `logs/qwen3.5-397b-then-deepseek-4bit.log` | probe and fresh blocks |
| Qwen3.5-397B alone, 21 September | 224.5 on 48,029 tokens at the defaults; 932.2 at `-b/-ub 4096`; 16.39 on an 11-token answer | `other-models-desktop/qwen-2026-09-21/qwen3.5-397b-default.result`, `qwen3.5-397b-ub4096.result`; the `eval time` line in `qwen3.5-397b-default.log` | |
| six times longer | 48,029 against 7,651 and 8,222 | derived | |
| Llama 4 Maverick | 400.71 B, 167.21 GiB; 13.09, 12.02, 13.18; 147.4 and 148.5; deleted 2026-09-14 | `logs/model-headers.txt`; `logs/deepseek-draft-runs-and-maverick.log` `=== RUN12 ===` | the deletion date is our operator record, **not shipped** |
| Mistral Medium 3.5 on the pair, 16 September | 54.4 GB (7,875,456 + 49,892,371,008 + 4,466,692,064 bytes); 16 / 72 layers; q8 cache; draft model | `mistral-medium-3.5-pair-2026-09-16/shard-bytes.json`; `pair16-draft-simple.launch.json` | `bytes`; `--tensor-split 16,72`, `--cache-type-k q8_0`, `--spec-draft-model` |
| its prose speaking and reading | 5.54 on 441 tokens after 1,453 tokens (43.8 reading); 3.81 on 353 tokens with no draft at 8 / 80; 4.71 on 311 tokens after an 8,437-token request, 1,377 tokens of it cached (`cache_n`, `cached_tokens`) and 7,060 read (`prompt_n`); 2.82 on 331 tokens after 32,509 tokens read in 1,027.1 s at 31.65 | `pair16-draft-simple-smoke.result-final.json`, `pair8-none-smoke.result-final.json`, `pair16-draft-simple-prose8k.result-final.json`, `pair16-depth-draft-simple-32000.result-final.json` | `timings`, `usage`; the prose requests are synthetic observatory notes, as the replies show |
| its desktop record | 1.97 prose with the draft, 435 reading, UD-Q4_K_XL, 32K window, 2026-08-06 | **not shipped here**: published on the model's field card with its own data package | |
| MiniMax M3 on the pair, 20 September | 167.6 GiB (the launcher's line); 4 / 32 / 24; q8 cache; allocation failures at `-ub 4096` and 2048, 20,746,340,352 bytes asked of the card at 4096 at both splits; loaded at `-ub 1024`, 17.58 on 3,658 tokens; stopped during the first speaking probe | `minimax-m3-pair-2026-09-20/split-ladder.console.log`, `split-50-10.console.log`, `split-allocation-failures.txt`, `split_msa_128k_ub1024.prefill.json`, `split-36-24-ub1024.server.log`, `split-measure.console.log` | the ladder lines; the `failed to allocate` lines; `prefill_tps`; the server log's last lines (`cleaning up before exit`, `Received second interrupt`) |
| MiniMax M3 alone, 20 September | Q2_K_L, 142.6 GiB (153,086,988,768 bytes); 147.5 on 3,658 tokens at `-ub 2048`; 8.90 on an 82-token answer | `minimax-m3-pair-2026-09-20/msa_q2kl_128k_ub2048.prefill.json`, `.decode.json`; `build-and-file-status-2026-09-26.txt` | `prefill_tps`; `chat.rate`, `chat.n`; the shard listing |
| an eighth | 17.58 against 147.5 | derived | |
| M3 file since deleted | its folder absent; parent directory changed 2026-09-21 19:25 | `build-and-file-status-2026-09-26.txt` | "Files no longer present" |
| Kimi K2.7-Code | 1.03 T, 283.03 GiB; 0.67 cold; 5.17 and 26.10 warm; ready at 689 s; 552 s and 331 s | `logs/model-headers.txt`; `logs/kimi-k2.7-pair.log`; `logs/kimi-warm-timings.txt` | as before |
| its weights removed 2026-09-17 | no `.gguf` left; directory changed 2026-09-17 11:46 | `build-and-file-status-2026-09-26.txt` | "Files no longer present" |

## Section 06, the placement rule

| figure | value | file | where |
|---|---|---|---|
| 17 percent ahead, 35 percent behind | 14.76/12.65 and 7.66/11.79 | section 04 files | derived |
| 226.8 to 30.7 | first and last stretch | `same-file-2026-09-21/stretch_rates.txt` | |
| a cable of about two gigabytes a second | 2,092 to 2,120 MB/s one way | `link/tcp_up_run*.txt` | |
| 14 percent before the laptop's side failed | as in section 04 | | |

## Section 07, the draft model, the installed preset and the checks

The page prints the draft model's two gains and costs, the 4-bit preset's 19.55, 19.59 and 125.1, and the two long legs; the tables are in `moved-from-the-page-2026-09-26.md`, sections 4 and 5.

| figure | value | file | where |
|---|---|---|---|
| 16.15 to 18.12 (+12%), 184.6 to 148.8; 12.78 to 19.25 (+51%), 145.4 to 121.9 | depth probe lines | `logs/deepseek-3bit-8-10-25.log`, `logs/qwen3.5-397b-then-deepseek-4bit.log`, `logs/deepseek-draft-runs-and-maverick.log` | RUN5, RUN8, RUN11b, RUN10b blocks |
| acceptance 61 to 85 percent; runs of 2.8 to 3.8 tokens; three samples per file | 0.614 to 0.846; 2.82 to 3.75 | `logs/deepseek-draft-runs-and-maverick.log` | the six `draft acceptance` lines |
| placement moved 8 / 10 / 25 to 4 / 14 / 25, 5 / 14 / 24 to 2 / 13 / 28; draft length 8 | run headers | the same logs | `===` headers; "n-max 8" |

| figure | value | file | where |
|---|---|---|---|
| 19.55 and 19.59; 125.1 on 7,841 tokens; 16.5 on 21 tokens; 225 s; 27,430 MiB; 91 GB; 131,072 window | as printed | `installed-4bit-preset-run.txt` | the 14:28:03 to 14:35:17 block |
| the earlier attempt: 27,501 MiB, 93 GB | as printed | `installed-4bit-preset-run.txt` | the 14:05 to 14:09 block |
| check shape: 48,000 and 96,000-token legs, codes at 5 / 50 / 95 percent, window clamped to 118,000 of 131,072 | as described | `gate/q4-preset.json` (`fit_provision`); `gate/attempt2.json` (`l64`, `l128`) | |
| attempts 1 to 3 | fail, fail on one leg (HTTP 400), pass without long legs | `logs/check-attempt1.log`, `gate/attempt2.json`, `gate/attempt3.json` | `[VERDICT]`, `verdict`, `H1.error`, absence of `l64`/`l128` |
| 48,000-token leg: 52,928 tokens, 3 of 3, 543.65 s, 97.4, 11.7 | `l64.A_recall.*` | `gate/attempt2.json` | |
| 96,000-token leg: 102,478 tokens, 3 of 3, 1,537.75 s, 66.6, 10.0 | `l128.A_recall.*` | `gate/attempt2.json` | |
| nine and twenty-six minutes | 543.65 s and 1,537.75 s | derived | |
| the 4-bit preset's check: 5.8 s, 27,566 MiB, no long legs | `T0.latency_s`, `S.vram_after_mib` | `gate/q4-preset.json` | |

## Section 08, the traps

Traps 1 and 2 are on the page; the other two, A and B, are in `moved-from-the-page-2026-09-26.md`, section 6.

| figure | value | file | where |
|---|---|---|---|
| ready after 414 s, then HTTP 500 | as printed | `logs/deepseek-8bit-mismatched-worker.log` | `healthy after`, the traceback |
| `GGML_OP_COUNT` 101 to 102, RPC protocol 0 to 1; the device claims every operation | as printed | `build-mismatch-trap.txt` | Run 3 and Run 3b blocks |
| 100 gigabytes, a 50-second batch, 90 seconds, two kills on 2026-09-15 | as printed | `installed-4bit-preset-run.txt` | the 14:09:07 to 14:09:08 lines and the closing block |
| trap A: 9 refusals and 1 acceptance in 10 probes of a busy worker | as printed, attributed to the note | **not shipped**: the method note of the 2026-09-16 check, which records the ten probes; no separate probe log exists, and the moved write-up says so | |
| `ggml_vulkan: No devices found` | as printed | `installed-4bit-preset-run.txt` | the 14:28:03 line |
| trap 4 | 2,998, 40,960, 48,024 | `same-file-2026-09-21/pair-ub4096.log`, `.result` | as in section 04 |

## Section 09, what we got wrong

Each row pairs what our records said with a file in this package: the DeepSeek rows with section 04's and 05's
files; the MiniMax rows with `other-models-desktop/minimax-m2.7-2026-09-13-launch-and-timings.txt` and the
19 September JSON; the Qwen3.5-397B row with `other-models-desktop/qwen-2026-09-21/` (the 385 on a 2,617-token
prompt at a 64K window is the model's August record, **not shipped**; the page now calls it retired); the window row with
`logs/control-glm-4.7-flash.log`; the attention row with the `RPC0 KV buffer` lines; the speaking band row with
the section 05 table's files. The ledger table's log side is cited in sections 05, 06 and 09; the ledger itself
is withheld (`README.md`).

The first row's 75.2 and 474.2 are the whole-request times in section 04's rows above; the M2.7 row's 3,658 and 7,844 are in the hero rows. The ledger table left the page and is mapped in the last part of this file.

## Section 10, what this does not show

| figure | value | file | where |
|---|---|---|---|
| windows up to 262,144; longest prompts 230,835 on the pair, 150,475 alone | as printed | `long-reads-2026-09-15/pair-262k.deep.json`, `desktop-8bit-262k.deep.json` | `timings.prompt_n` |
| files no longer here, with dates | as printed | `build-and-file-status-2026-09-26.txt`; Maverick's date is our operator record, **not shipped** | |

## `moved-from-the-page-2026-09-26.md`

| section of that file | its figures come from |
|---|---|
| 1, the link | the link rows of section 03 above |
| 2, DeepSeek on the pair, 13 September; other nights; the 8-bit file at 16,000 tokens | the rows below, carried from the 16 September version of this file |
| 2, the comparison first made | `gate/desktop-8bit-2026-09-12.json` (the 12 September check, now shipped) and the 13 September row |
| 3, the other models, full cells | section 05 above |
| 4, the draft model | section 07 above |
| 5, the 4-bit preset and the checks | section 07 above |
| 6, traps A and B | section 08 above |
| 7, the ledger against the logs | the log side: sections 04, 05 and 07 above and this table; the ledger itself is withheld |

Every row: `=== probe ===` for the short and depth figures, the fresh-prompt block for the fresh figures,
`=== VRAM ===` for the card reading, `healthy after N s` for the load.

| row | speaking (short / 8K depth / fresh 8K) | reading (8K depth / fresh 8K) | card | file |
|---|---|---|---|---|
| 3-bit, 8 / 10 / 25 | 17.06 / 16.15 / 15.89 | 184.6 / 187.9 | 24,907 MiB, ready at 163 s | `logs/deepseek-3bit-8-10-25.log` |
| 3-bit, 8 / 5 / 30 | 17.69 / 16.15 / 16.01 | 160.0 / 159.9 | 24,005 MiB | `logs/deepseek-3bit-8-5-30.log` |
| 3-bit plus draft, 4 / 14 / 25 | 19.04 / 18.12 / 16.36 | 148.8 / 149.5 | 27,268 MiB | `logs/deepseek-draft-runs-and-maverick.log`, `=== RUN11b ===` |
| 4-bit, 5 / 14 / 24 | 10.59 / 12.78 / 13.02 | 145.4 / 173.0 | 26,461 MiB | `logs/qwen3.5-397b-then-deepseek-4bit.log`, the Q4_K_XL block |
| 4-bit plus draft, 2 / 13 / 28 | 16.99 / 19.25 / 15.96 | 121.9 / 119.9 | 27,991 MiB | `logs/deepseek-draft-runs-and-maverick.log`, `=== RUN10b ===` |

| other figure in section 05 | value | file | where |
|---|---|---|---|
| file sizes 104.2 GB and 155.1 GB | shard byte counts | `logs/deepseek-3bit-8-10-25.log`, `logs/qwen3.5-397b-then-deepseek-4bit.log` | shard lines |
| two missed recalls | `recall: MISSED` | `logs/deepseek-3bit-8-5-30.log`, `logs/qwen3.5-397b-then-deepseek-4bit.log` | fresh blocks |
| the short probe's 200 tokens all hidden reasoning | `decode 200 tok`, empty `reply:` | the five run blocks above | `[short]` lines |
| card baseline 793 to 987 MiB | the bare `NNN MiB` line before each header | every 13 to 15 September run and check log | |
| other nights: 14.95 and 15.10 (262,144, 15 September); 15.24 and 15.38 (131,072, 16 September), 208 tokens each, prompts of 30 then 4 tokens | `predicted_per_second`, `predicted_n`, `prompt_n` | `long-reads-2026-09-15/pair-262k.short.r1.json`, `.r2.json`, `pair-131k-120k.short.r1.json`, `.r2.json` | `timings` |
| 21 September: 14.76 on 67 tokens and 14.73 on 400 | `decode_tps`, `gen_n`; `warm_decode_tps`, `warm_gen_n` | `same-file-2026-09-21/pair-ub512.result` | `size 3000` line |
| the 8-bit row: 3.19 cold, 7.74 and 80.8 on 15,641 tokens, 26,300 MiB, ready at 183 s, file 150.8 GiB | as printed | `logs/deepseek-8bit-matched-worker.log`; `logs/model-headers.txt` | `[short]`, `[depth~16000]`, `=== VRAM ===`; 8-bit block |
| the same 8-bit file alone: 81.6 on 16,011 tokens at the defaults; 260.8 with `-b 4096 -ub 2048` | 81.64, 260.82 | `desktop-8bit-2026-09-20/ub512-16k.result`, `ub2048-16k.result` | `[read]` lines |
| BF16 and MXFP4 tensors; `bf16: 0`, `fp4: 0` | 555 BF16 and 129 MXFP4 tensors | `logs/deepseek-8bit-tensor-list.txt`; `logs/deepseek-8bit-matched-worker.log` | type column; device line |
| the first-runs comparison: 9.7 and 9.2 speaking; about 75.5 and 73.8 reading, the harness's estimate, on counted prompts of 52,931 and 102,481 tokens; 8-bit alone, 12 September | `decode_tps`, `prefill_tps_approx`, `prompt_tokens` | `gate/desktop-8bit-2026-09-12.json` (the per-model record of that check, shipped redacted on 26 September; the check's ledger, which carries private labels, stays withheld) | `l64.A_recall`, `l128.A_recall` |
| a day apart | 12 September and 13 September | as above; the 13 September logs | |
