# Moved from the page on 26 September 2026

On 26 September the page "Two boxes, one model" was cut to put its practical answer on the first screen. The tables
and write-ups below left the page then. Nothing in them was dropped: each keeps its figures, its date and the files
in this package it comes from. Corrections made in the same pass are applied here as well as on the page.

If a number here disagrees with a file in this package, the file is right. All speeds are llama.cpp's own timings,
one request at a time, measured on these machines; "reading" is prompt tokens per second and "speaking" is
generated tokens per second, hidden reasoning included.

## 1. The link, measured (2026-09-15)

With no model server running and the graphics card idle: 30 pings, then a plain Python socket test, one TCP
stream, 1 MiB writes, 2 GB per run, two runs in each direction. `iperf3` is installed on neither machine, so these
are a lower bound on what the link carries, not a tuned benchmark.

| Link measurement, 2026-09-15 | Result | Label |
|---|---|---|
| Round trip, 30 packets, 0.2 s apart | 0.157 min / 0.667 avg / 0.820 max ms, 0% loss | measured |
| Desktop to laptop, one stream, 2 GB, two runs | 2,092 to 2,120 MB/s (16.7 to 17.0 Gbit/s) | measured |
| Laptop to desktop, one stream, 2 GB, two runs | 1,107 to 1,111 MB/s (8.9 Gbit/s) | measured |

Both connections were opened from the desktop. The direction is asymmetric by roughly a factor of two on this
cable, and we did not chase why. No figure for the card's or the system's own memory bandwidth was measured.

Files: `link/ping.txt`, `link/tcp_up_run1.txt`, `link/tcp_up_run2.txt`, `link/tcp_down_run1.txt`,
`link/tcp_down_run2.txt`, `link/tcp_client.py`, `link/tcp_server.py`, `link/RUN_LOG.txt`.

## 2. DeepSeek V4 Flash on the pair, 13 September

The first runs, kept as the dated record they are. Every row is one run on the pair at a 131,072-token window and
llama.cpp's default batch sizes. The three speaking columns are three different probes, not three repeats. File
sizes are the byte counts of each file's shards.

| File and extras | Placement | Speaking, short probe | Speaking, 8K depth probe | Speaking, fresh 8K probe | Reading, 8K depth probe | Reading, fresh 8K probe | Card MiB |
|---|---|---|---|---|---|---|---|
| UD-IQ3_XXS (3-bit), 104.2 GB, no draft; the configuration that passed the tool-and-recall check | 8 / 10 / 25 | 17.06 | 16.15 | 15.89 | 184.6 | 187.9 | 24,907 |
| UD-IQ3_XXS, no draft, laptop-heavy variant | 8 / 5 / 30 | 17.69 | 16.15 | 16.01 | 160.0 | 159.9 | 24,005 |
| UD-IQ3_XXS plus the maker's draft model | 4 / 14 / 25 | 19.04 | 18.12 | 16.36 | 148.8 | 149.5 | 27,268 |
| UD-Q4_K_XL (4-bit), 155.1 GB, no draft | 5 / 14 / 24 | 10.59 | 12.78 | 13.02 | 145.4 | 173.0 | 26,461 |
| UD-Q4_K_XL plus the maker's draft model | 2 / 13 / 28 | 16.99 | 19.25 | 15.96 | 121.9 | 119.9 | 27,991 |

Recall was found on every probe in this table except two: the laptop-heavy variant and the 4-bit file without the
draft model each missed the planted code on the fresh prompt. The short probe's 200 generated tokens were all
hidden reasoning on every row. Every card figure includes a desktop baseline, which the run logs record between
793 and 987 MiB just before each load. The 3-bit headline row, as a band: 15.9 to 17.1 speaking and 185 reading
(184.6 at depth, 187.9 fresh), ready to serve 163 seconds after launch.

Files: `logs/deepseek-3bit-8-10-25.log`, `logs/deepseek-3bit-8-5-30.log`, `logs/deepseek-draft-runs-and-maverick.log`
(`=== RUN11b ===`, `=== RUN10b ===`), `logs/qwen3.5-397b-then-deepseek-4bit.log` (the Q4_K_XL block).

### The pair's speaking speed on other nights

The 21 September 14.76 is below the 13 September band. The window changed between the nights, but it is not the
whole story: two nights at the same 131,072-token window disagree with each other.

| Night | Window | Prompt | Answer | Speaking |
|---|---|---|---|---|
| 13 September | 131,072 | 21 tokens | 200 tokens, all hidden reasoning | 17.06 |
| 13 September | 131,072 | 7,841 tokens | 42 tokens | 16.15 |
| 15 September | 262,144 | 30, then 4 tokens | 208 tokens, twice | 14.95, 15.10 |
| 16 September | 131,072 | 30, then 4 tokens | 208 tokens, twice | 15.24, 15.38 |
| 21 September | 262,144 | 2,998 tokens | 67 tokens; then 400 | 14.76; 14.73 |

Same file, same placement, same build commit on every night. The prompts, the answers and the laptop's state
varied, and we did not isolate which of them moved the speed.

Files: `long-reads-2026-09-15/pair-262k.short.r1.json`, `.r2.json`, `pair-131k-120k.short.r1.json`, `.r2.json`;
`same-file-2026-09-21/pair-ub512.result`.

### The 8-bit file, at 16,000 tokens of depth

The maker's 8-bit file was the first thing tried on the pair. Its probe was taken at about 16,000 tokens of depth,
so it does not belong in the 8,000-token table above.

| File | Placement | Speaking, cold short probe | Speaking, 16K depth probe | Reading, 16K depth probe | Card MiB |
|---|---|---|---|---|---|
| Q8_K_XL, 150.8 GiB, with BF16 and MXFP4 tensors inside | 4 / 16 / 23 | 3.19 | 7.74 | 80.8 | 26,300 |

Measured 2026-09-13 on 15,641 tokens, ready to serve in 183 seconds, recall found. The same 8-bit file alone on the
desktop read a 16,011-token prompt at 81.6 on 20 September at the same default batch sizes, level with the pair,
and at 260.8 with `-b 4096 -ub 2048`; the prompts and the builds differ. The laptop's Vulkan device reports
`bf16: 0` and `fp4: 0`, and this file's tensors are in exactly those two formats; we read that as the likely
reason it speaks slowly on the pair, without having instrumented the conversion cost.

Files: `logs/deepseek-8bit-matched-worker.log`, `logs/deepseek-8bit-tensor-list.txt`, `logs/model-headers.txt`;
`desktop-8bit-2026-09-20/ub512-16k.result`, `ub2048-16k.result`.

### The comparison these runs were first read against

| DeepSeek V4 Flash 0731 | Where | File | Speaking | Reading |
|---|---|---|---|---|
| 2026-09-12 framework check, legs named for 48,000 and 96,000 tokens of seeded history; counted prompts 52,931 and 102,481 tokens | Desktop alone, default batch sizes | 8-bit | 9.7 and 9.2 | about 75.5 and 73.8 (the harness's estimate, `prefill_tps_approx`, not a prompt-evaluation rate) |
| 2026-09-13 probes, short / 8K depth / fresh 8K | The pair, 8 / 10 / 25 | 3-bit | 15.9 to 17.1 | 184.6 to 187.9 |

Different files, different prompt depths, a day apart, different methods, and llama.cpp's default batch sizes on
both. This is the comparison our records first called a speed-up for the pair. The page's section 04 replaces it
with the same file on both sides.

Files: `gate/desktop-8bit-2026-09-12.json` (`l64.A_recall` and `l128.A_recall`: `prompt_tokens`, `decode_tps`,
`prefill_tps_approx`); the 13 September row as in the table above.

## 3. The other models, full cells

The page's section 05 carries a shortened version of this table. One row per model, on the pair at llama.cpp's
default batch sizes, one request at a time. The parameter count and file size in each first cell are read from
that file's own header, as the loader printed them.

| Model and file | Placement | On the pair | On the desktop alone | What we take from it |
|---|---|---|---|---|
| GLM-4.7-Flash, UD-Q4_K_XL, the control run. Header: 29.94 B parameters, 16.31 GiB | Half the layers each side, 8,192-token window | Speaking 63.80, 67.97 and 63.86 on answers of 54, 10 and 8 tokens; reading 1,125.28 on a 1,940-token prompt. A fourth timing, 63.49, is prompt evaluation on a 22-token prompt, not speaking | Speaking 223.65 (best of two replies of about 200 tokens), reading 4,447.44 at a 131,072 window on a 20,221-token prompt (2026-09-12) | Proof that the path works. The two speaking figures are different reply lengths, and the two reading figures different prompt lengths and windows, so neither pair is a measured cost of the cable. Not re-run after the batch change |
| Qwen3-235B-A22B 2507, Q4_K_M. Header: 235.09 B parameters, 132.39 GiB | 6 / 36 / 52 | Speaking 5.97 on a 49-token answer, 5.54 on a 10-token answer at 8K depth; reading 97.6 on 7,844 tokens | 2026-09-12: speaking 6.93 (best of two replies of about 200 tokens, with a 0.6B draft model), reading 251.58 on 21,493 tokens. 2026-09-21, its own build, 48,020 tokens: reading 285.8 at the default batch sizes, 703.3 at `-b 4096 -ub 2048` (the setting it serves), 944.2 at `-b/-ub 4096` | Slower to read on the pair: 97.6 against 285.8 at the same default micro-batch, on a prompt a sixth as long. The speaking gap is soft: the desktop figure had a draft model and the pair's answers were 10 and 49 tokens |
| MiniMax M2.7, UD-IQ4_XS. Header: 228.69 B parameters, 100.96 GiB | 6 / 16 / 40 | Speaking 9.66 on a 401-token answer, 8.98 on 128 tokens at 8K depth; reading 70.4 on 7,844 tokens | 2026-09-13: speaking 9.8 to 10.2 across eight replies of 64 to 900 tokens (the 900 all hidden reasoning), reading 45.6 on 6,776 tokens, at `-ub 128`, a 64K window and an f16 cache. 2026-09-19, the pair's build, 131,072 window: reading 100.8 on 3,658 tokens at the default `-ub 512`; 656.5 on 43,909 tokens at `-ub 4096`; q8_0 cache | Same speaking speed. The faster reading on the pair was an artifact: the desktop run it was compared with used `-ub 128`, a quarter of the default, inherited from another model's launcher. At the default the desktop read faster, on a shorter prompt: 3,658 tokens against 7,844 |
| GLM-4.7 Full, IQ3_XXS. Header: 358.34 B parameters, 135.15 GiB | 4 / 34 / 55, q8 cache, thinking off | Speaking 5.66 short, 5.59 at 8K depth; reading 51.1 at depth | Speaking 5.51, reading 61.36 at a 131,072 window on 20,221 tokens with a q5_1 cache (2026-09-12) | Unchanged speaking within these probes, slower reading on the pair. The cache precision differs between the two, a second uncontrolled variable. Not re-run after the batch change |
| Qwen3.5-397B-A17B, UD-IQ3_XXS. Header: 402.94 B parameters, 139.54 GiB | 6 / 25 / 30, thinking off | Speaking 5.18 short, 12.61 on a 10-token answer at 8K depth, 15.31 on a 108-token fresh answer; reading 98.7 and 108.2 | 2026-09-21, same file, its own build, 131,072 window: reading 224.5 on 48,029 tokens at the default batch sizes, 932.2 at `-b/-ub 4096`; speaking 16.39 on an 11-token answer | Slower to read on the pair even against the desktop's default setting on a prompt six times longer. Speaking about level, on answers of very different lengths |
| Llama 4 Maverick, UD-Q3_K_XL. Header: 400.71 B parameters, 167.21 GiB | 4 / 20 / 24, q8 cache | Speaking 13.09 short, 12.02 at 8K depth, 13.18 fresh; reading 147.4 and 148.5 | Never served from one machine here | A capacity demonstration and nothing more: 167.21 GiB of weights loaded across the pair and answered. Dropped the next day, 2026-09-14, and its files deleted |
| Mistral Medium 3.5, a dense model, Q3_K_S, 54.4 GB by shard byte counts, with a 3B draft model patched to its vocabulary; 2026-09-16 | 16 layers on the card, 72 on the laptop; q8 cache | Prose speaking 5.54 on a 441-token reply to a 1,453-token prompt (3.81 with no draft at 8 / 80 layers); 4.71 on a 311-token reply to an 8,437-token request, 1,377 of its tokens already cached and 7,060 read; 2.82 after a 32,509-token read that took 1,027.1 seconds at 31.65. Reading 43.8 on the 1,453-token prompt | Its field card, 2026-08-06, a different and larger file (UD-Q4_K_XL) at a 32K window: prose 1.97 with the draft, reading 435 | The one model here that spoke clearly faster on the pair, across different files and months. On the desktop alone much of a dense model this size sits in system memory; on the pair it sits in the laptop's graphics memory. Reading fell about ten times |
| MiniMax M3, IQ3_XXS with its sparse-attention tensors, 167.6 GiB as its launcher reports; 2026-09-20 | 4 / 32 / 24, q8 cache | At `-ub 4096` and 2048 it could not allocate its compute buffers at either of two layer splits; at 4096 the card was asked for 20,746,340,352 bytes both times. At `-ub 1024` it loaded and read a 3,658-token prompt at 17.58. Speaking not measured: the run was stopped during the first speaking probe | A smaller file with the same attention (Q2_K_L, 142.6 GiB) read the same 3,658 tokens at 147.5 with `-ub 2048` and spoke 8.90 on an 82-token answer (2026-09-20) | The compute buffer grew with the micro-batch, not with the layer split: moving layers only moved which machine ran out. At the one setting that fit, the pair read at an eighth of the desktop's speed, on a larger file. The file has since been deleted |
| Kimi K2.7-Code, IQ1_M. Header: 1.03 T parameters, 283.03 GiB | 1 / 39 / 21 | Cold first turn 0.67 speaking; warm 8K turn 5.17 speaking and 26.10 reading | Not measured alone in this campaign | The second capacity demonstration. Ready to serve 689 seconds after launch; the first 8,000-token turn took 552 seconds end to end, a later warm turn of the same shape 331. Its weights were removed from the desktop on 2026-09-17 |

Files: as `NUMBERS.md` lists them under the page's section 05.

## 4. The draft model, and what it costs (13 September)

DeepSeek ships a draft model that guesses several tokens ahead for the main model to check. On the pair, the
draft on the card, maximum draft length 8.

| File | Speaking at 8K depth, no draft | Speaking at 8K depth, with draft | Change | Reading at 8K depth, no draft | Reading at 8K depth, with draft |
|---|---|---|---|---|---|
| UD-IQ3_XXS (3-bit) | 16.15 | 18.12 | +12% | 184.6 | 148.8 |
| UD-Q4_K_XL (4-bit) | 12.78 | 19.25 | +51% | 145.4 | 121.9 |

One comparison per file; both gains are quoted rather than an average. Placement also moved, because the draft
model takes card space: the 3-bit arm went from 8 / 10 / 25 to 4 / 14 / 25, the 4-bit arm from 5 / 14 / 24 to
2 / 13 / 28. llama.cpp reported the guesses accepted between 61 and 85 percent of the time across three samples per
file, with accepted runs of 2.8 to 3.8 tokens; three samples is too few to call that a rate. The draft bought
speaking speed on both files and cost reading speed on both. It was not re-measured at the 262,144-token window or
with a larger micro-batch.

Files: `logs/deepseek-3bit-8-10-25.log`, `logs/qwen3.5-397b-then-deepseek-4bit.log`,
`logs/deepseek-draft-runs-and-maverick.log` (the six `draft acceptance` lines).

## 5. The 4-bit preset on the installed service, and the checks

The last configuration tested in the first campaign, measured on 2026-09-15 on the installed service rather than in
a scratch script, at a 131,072-token window. The record shows a completed run of this preset on that service; it
does not show that the preset stayed selected afterwards.

| | |
|---|---|
| File and placement | UD-Q4_K_XL, 155.1 GB, plus the maker's draft model, at 2 / 13 / 28 |
| Speaking | 19.55 on the short probe and 19.59 at 8,000 tokens of depth (measured) |
| Reading | 125.1 on a 7,841-token prompt; 16.5 on the 21-token short prompt, which measures a tiny prompt's overhead rather than reading speed (measured) |
| Load | Ready to serve 225 seconds after launch; 27,430 MiB of the card, 91 GB of the laptop's memory. An earlier attempt the same afternoon (27,501 MiB, 93 GB) was killed by our own watchdog (trap A below) |

A separate check runs through an agent framework: a direct tool-schema call, three conversation turns, a file
written and read back, then legs named for 48,000 and 96,000 tokens of seeded history, three codes planted at 5, 50
and 95 percent depth and a tool call required at depth, the agent's window clamped to 118,000 of the served
131,072. The 3-bit split was checked three times on 2026-09-14. Attempt 1 failed (0 of 3 codes on both long legs,
no tool call, no clean first reply); attempt 2 passed both long legs and failed on an HTTP 400 in a leg unrelated
to the model; attempt 3 passed, and covers the short legs only. No single recorded attempt contains both long legs
and a passing verdict.

| Leg (3-bit split, 8 / 10 / 25, attempt 2) | Prompt tokens | Codes found | First word | Reading (the harness's estimate) | Speaking |
|---|---|---|---|---|---|
| 48,000-token leg | 52,928 | 3 of 3 | 543.65 s | 97.4 | 11.7 |
| 96,000-token leg | 102,478 | 3 of 3 | 1,537.75 s | 66.6 | 10.0 |

A leg is named for the seeded history the runner builds; the prompt column is what the model was sent. A tool call
at depth succeeded on both legs: the model wrote a file and the framework confirmed the bytes on disk. The 4-bit
preset's own check on 2026-09-15 covered a direct tool-schema call answered in 5.8 seconds, three conversation
turns, and a file written and read back, at 27,566 MiB on the card; the long legs were not re-run for it.

Files: `installed-4bit-preset-run.txt`; `logs/check-attempt1.log`, `gate/attempt2.json`, `gate/attempt3.json`,
`gate/q4-preset.json`.

## 6. Two more traps from the first nights

### A. Do not poke a busy worker's port

A watchdog of ours checked the worker by opening its port and stopped the server if the port did not answer for 90
seconds. While the worker loads 100 gigabytes of weights, or runs a 50-second reading batch, its port usually does
not answer. The watchdog killed a healthy server twice on 2026-09-15, once during a load and once during a reading
batch (both in `installed-4bit-preset-run.txt`). The method note of a later check, 2026-09-16, records that a busy
worker's port refused 9 of 10 probes and accepted 1; that count comes from the note, not from a shipped probe log,
because no separate probe log was kept. Either way, a refused probe proves nothing. Check that the machine is
reachable, and read the worker's health from the server: its health check and its timing lines.

### B. A worker that starts before the graphics driver binds the processor

On 2026-09-15, after a morning reboot, the laptop's worker had been running since boot with
`ggml_vulkan: No devices found` in its log: it had bound the processor instead of the graphics chip and served that
way, silently, for hours. Restarted after the driver was up, it took the graphics device and the expected speeds
came back (`installed-4bit-preset-run.txt`, the 14:28:03 line). Start the worker after the graphics driver is up,
pin the device explicitly, and read the worker's first log lines.

## 7. The ledger against the logs, 13 to 15 September

Our internal ledger of the first runs rounded several numbers or quoted the best probe without saying so. Where it
and the logs disagree, the log is printed. The ledger itself is withheld.

| Our ledger said | The log says |
|---|---|
| DeepSeek 3-bit on the pair: "17 t/s" | 15.89, 16.15 and 17.06 across the three probes of one run |
| DeepSeek 3-bit reading: "185 t/s" | 184.6 at depth, 187.9 on the fresh prompt |
| DeepSeek 4-bit without draft: placement "5 / 10 / 28", speaking "13 to 14 t/s" | Placement 5 / 14 / 24; speaking 10.59, 12.78, 13.02. The 14 appears in no raw file |
| DeepSeek 4-bit plus draft: "16 to 19 t/s" | 16.99 short, 19.25 at depth, 15.96 fresh |
| The 8-bit file: "7.7 / 81" with the other 8,000-token rows | 7.74 and 80.8, at about 16,000 tokens of depth |
| The tool check "passed, on the second morning" | Attempt 1 fail, attempt 2 fail on one leg, attempt 3 pass; the long legs are in attempt 2, the verdict in attempt 3 |
| Kimi K2.7 on the pair: "5.2 / 26", no mention of the first turn | 0.67 speaking on the cold first turn and a 552-second first turn; 5.17 and 26.10 on a warm 8,000-token turn |
| The link: "0.67 ms, at least 830 MB/s" | No artifact existed for either figure until the 2026-09-15 measurement |
| The second machine delivers "about 45 GB/s effective" for expert reads | No benchmark artifact exists for that figure; it is not printed |

The installed 4-bit preset's "19.6 and 125" survived unchanged: the log reads 19.55 and 19.59 speaking and 125.1
reading.
