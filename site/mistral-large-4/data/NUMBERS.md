# Number map: Mistral Large 4 at home

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

**Where a file can look like it contradicts the page:** `quality/blind-map.json` gives Large 4 (four experts) speeds of 0.88 to 1.72 tokens a second on three questions and a total wall time of 100.6 minutes. Those three answers were written on 31 October on an earlier, slower setup; the other three on the final setup. The page makes no time comparison from these wall times.

**Every generation figure counts reasoning.** `gen_n` and `gen_tps` cover the model's reasoning and its visible answer together; `finish` `length` means the cap was reached.

Paths are relative to `data/`. `T/` = `trial-2026-10-31/`, `X/` = `twobox-2026-11-01/`. Fields: `gen_tps` writing, `read_tps`/`prompt_tps` reading, `drive_gb`/`drive_read_gb` drive reads, `major_faults` major page faults, `read_n`/`prompt_n` prompt tokens, `gen_n` generated tokens.

## Hero and sections 01 to 03

| Page figure | File and field, or derivation |
|---|---|
| 217 GiB; 233,009,564,322 bytes; six files | `T/logs/tree.json`, sum of `size` over the six `UD-IQ1_S` files; / 2^30 = 217.007 (arithmetic) |
| about 1.9 bits per weight | 233,009,564,322 × 8 / 10^12 = 1.86 (arithmetic, using the vendor's "~1T") |
| about 1 trillion total; 49 billion active per token, 52 billion with embeddings and output layers; 128 routed experts, 4 active, 1 shared; largest to date; 1M window | `vendor/mistral-large-4-model-card.md` (vendor) |
| Licence name, modified MIT, section 2 (Model as a Service), section 3 exceptions | `vendor/mistral-large-4-LICENSE.txt` (vendor) |
| SHA-256 checked | `T/logs/want.tsv` (hashes) and `T/logs/download.log` (six `OK` lines); the download script does not ship |
| 188 GiB RAM | `T/logs/run_split3.txt`, the `free -g` total line |
| 32 GB card | the product's nominal size; not measured here |
| "under 3" on the desktop alone | `T/results/` one-desktop files: max `gen_tps` 2.866 (`moe69-b.json`) |
| about 6.6; 6.58, 6.62, 6.67 in short tests | `X/results/l10-final.jsonl`, `gen_tps` 6.62, 6.58, 6.67; each `gen_n` 300 and `finish` `length` |
| 72.1 on 6,411 tokens | `X/results/l10-final.jsonl`, tag `read2k`, `read_tps` 72.1, `read_n` 6411 |
| first request after start-up as fast | `l10-final.jsonl` first line `w300a` 6.62 (no warm-up requests in this run) |
| 72 layers; 42 layers' experts in RAM, 30 on the laptop | `scripts/serve_ml4.sh` with `LAYOUT=expz Z=30 GPU_N=0` (`scripts/rounds/round10.sh`): CPU list 0 to 41, RPC list 42 to 71 |
| Flags in the schematic | `scripts/serve_ml4.sh`, `scripts/rounds/round10.sh`, `scripts/run_ml4.sh` (worker line, `GOMP_CPU_AFFINITY`) |
| Cores 0 to 15 = 8 performance + 8 efficiency (desktop) | the processor's core layout as the operating system lists it; not in this package |
| build strings `b330-6279535`, `b12057-629237e51` | `X/results/ml4-final.json` and `ml4-c5g-64k.json`, field `props.build_info` |
| "b12015" | the build name our scripts use (the binary folder in `scripts/serve_ml4.sh`, redacted); not printed by the server |
| pull request 31286 merged locally | `scripts/rounds/round12.sh` comment; the local build's merge record (not shipped) |
| Prompts 8 to 32 tokens; caps 150 to 800; 1,940 / 6,411 / 48,367 / 96,325 | `read_n` and `gen_n` in `X/results/*.jsonl`; `depth[].prompt_n` in `X/results/ml4-final.json` |
| Dates | `started` fields and log times in the files of each folder; the fault test file is dated 2 November |

## Section 04, the path table

| Row | File and fields |
|---|---|
| One desktop, first launch: 0.15; 0.17 to 0.48; reading 0.10 to 0.22 on 8 to 32 tokens | `T/logs/serve1.log`, `print_timing` lines: eval 0.15, 0.17, 0.39, 0.48, 0.43, 0.46; prompt eval 0.10, 0.12, 0.17, 0.22, 0.16, 0.18 on 26, 8, 21, 29, 21, 32 tokens. Model path in the log: the data drive |
| Best placement, three launches pooled: first 1.52 to 1.53; later 1.18 to 2.87; 3.54 on 1,940 (548 s) | `T/results/moe69-a.json` 1.525 (data drive, `serve2.log`), `fast-short1.json` 1.518 (NVMe, `serve3.log`); later: `moe69-b` 2.866, `moe69-c` 2.166, `fast-short2` 2.838, `fast-read2k` 1.179, `long-write1..3` 2.269, 1.490, 2.252 (`serve5.log`); read: `fast-read2k.json` `prompt_tps` 3.538; `T/logs/serve3.log` prompt eval 548,350 ms / 1,940 tokens |
| A read request cancelled after about 25 minutes on the data drive | `T/logs/serve2.log`: task 558 launched at 10:25.8, `cancel task` at 35:26.0 (log clock, minutes:seconds). Its prompt size is not logged |
| Read-ahead library: 2.01; 1.74 to 2.08; 7.24; mixed writing; 570.8 GB | `T/results/seq-short1.json` 2.013; `seq-short2` 2.075 (against `fast-short2` 2.838), `seq-read2k` 1.737 write (against `fast-read2k` 1.179), 7.240 read and `drive_read_gb` 570.8, `seq-after` 1.969 |
| 8,000 MiB cache, 31 Oct: 0.97; 1.11 to 1.43; 4.85; 17.7 to 362.2 GB | `T/results/cache8g-*.json`: `short1` 0.973, `short2` 1.110, `long2` 1.229, `read2k` 1.428 and read 4.847, `after` 1.407; `drive_read_gb` 232.0, 133.7, 320.4, 362.2, 17.7 |
| Six whole layers: 33,208 MiB allocation failed | `T/logs/run_split1.txt`, `split-46-6.log`: "allocating 33208.37 MiB on device 0: cudaMalloc failed". Run before the Vulkan run (log times) |
| Vulkan worker (device per our run notes; the laptop worker's log was not kept): 1.67; 3.75 to 4.82; 33.1; random symbols returned as normal responses | `T/results/split-46-4-*.json` `gen_tps` 1.673, 3.749, 4.141, 4.402, 3.863, 4.822; read 33.10; `answer` fields hold the symbols, with an ordinary `finish` value and no error field |
| Laptop CPU, 26 layers: 2.10; 3.20 to 3.98; 26.7 | `T/results/split-cpu-46-4-*.json`: 2.103; 3.635, 3.714, 3.823, 3.202, 3.982; read 26.73 |
| 30 layers, 64K: 0.63; 2.56 to 3.77; 24.1 | `T/results/split-cpu-42-3-64k-*.json`: 0.628; 2.560, 2.959, 3.562, 2.994, 3.767; read 24.06 |
| 1 Nov, 8 threads: 1.76; 3.22 to 3.96; 26.8; 87.1 GB | `X/results/l1-back26.jsonl`: `warm1` 1.76 and `drive_gb` 87.1; later 3.22, 3.70, 3.86, 3.24, 3.96; read 26.76 |
| First layers on the laptop: 1.40; 2.45 to 3.77; 24.4 | `X/results/l1-front26.jsonl` |
| 24 threads: 1.09; 1.45 to 3.20; 22.6 | `X/results/l2-back26-t24.jsonl`: 1.09; 1.45, 1.78, 2.30, 3.20, 3.08; read 22.6 |
| 16 threads: 1.82; 2.60 to 4.76; 25.8 | `X/results/l2-back26-t16.jsonl` |
| Experts only, 26 layers: 2.20; 3.35 to 6.67; 32.3 | `X/results/l3-expz26-t16.jsonl` (`scripts/rounds/round3.sh`, first line) |
| 20 threads, whole layers on the laptop: 1.76; 2.30 to 4.65; 26.6 | `X/results/l3-back26-t20.jsonl` (`round3.sh`, second line) |
| Experts only, 30 layers, 3 on card: 2.85; 3.85 to 6.69; 33.9; 74.0 GB | `X/results/l4-expz30-g3.jsonl` |
| Read once: 6.78; 6.76 to 6.87; 51.8; huge pages for the laptop worker; split not logged | `X/results/l5-expz-huge.jsonl` (`drive_gb` 0.0 on every line); `scripts/rounds/round5.sh` |
| Ordinary memory, huge pages on the desktop: 6.52; 6.83 to 6.89; 35.5 | `X/results/l6-expz-nohost.jsonl`; `X/logs/ml4_round6.out` "server 100.3 of 114.1 GiB" |
| 36 layers, 1 whole on the card: 6.53; 6.26 to 6.62; 45.5; 88 to 104 GiB | `X/results/l7-expz36-g1-128k.jsonl`; `scripts/rounds/round7.sh` (`HUGE=1`, `GPU_N=1`); `X/logs/ml4_round7.out` "Z13 104 GiB used" against 88 in rounds 4 to 6 |
| Micro-batch 2048, tuned worker: 3,092.56 MiB allocation failed | `X/logs/l8-expz30-g0-128k-ub2048.server.log`; `scripts/rounds/round8.sh` (`UB=2048`, worker `ZENV` with huge pages and `GOMP_SPINCOUNT`); `--batch-size 2048` in `scripts/serve_ml4.sh` |
| Final setup: first 6.62; later 6.58, 6.67; 72.1 on 6,411 | `X/results/l10-final.jsonl`; `scripts/rounds/round10.sh` (`UB=1024`, plain worker) |
| Long reads: 6.5 at 48,367; 6.3 at 96,325; reads 72.3 and 71.5; 1,347 s; 3 of 3; next turn 5.0 and 4.2 s at 6.5 | `X/results/ml4-final.json` `depth[]`: `gen_tps`, `read_tps`, `read_s` 1347.3, `codes`, `next_read_s` 5.03 and 4.19, `next_gen_tps` 6.5. The codes check is a substring match on three planted codes (`scripts/smoke.py`) |
| Three experts: 8.09 to 8.16 with caps 800, 300, 800; still reasoning at the caps; 82.6 on 1,940 | `X/results/l11-expert3.jsonl`: `gen_n` 800, 300, 800, every `finish` `length`, every `answer` empty; `read_n` 1940, `read_tps` 82.63 |
| Newer build, 5,500 MiB cache, 64K: 7.20 to 7.42; 81.1 on 1,940; plain 6.72 to 6.76 | `X/results/l14-c5g-64k.jsonl` (7.42, 7.20, 7.36; read 81.14) and `l14-plain.jsonl` (6.76, 6.73, 6.72); ratios 9.8%, 7.0%, 9.5%. Windows: 65,536 against 131,072 (`scripts/rounds/round14.sh`). The earlier run `l12-c5g-64k.jsonl` gave 7.00 to 7.32 |
| 8,000 MiB at 32K: first 7.44 (cap 500); 2.59 (cap 300), then 7.58 (cap 500); 77.6 on 6,411; 12,000 and 4,000 MiB did not load | `X/results/l13-c8g-32k.jsonl`; `X/logs/l12-c12g-32k.server.log` (11,969.44 MiB failed), `l12-c4g-128k.server.log` (3,982.78 MiB failed) |
| Load average about 25 during the slow reply, about 13 during the first request | `X/logs/l13-c8g-32k.cores.log`, third column (one-minute load average every 5 s): 4.93 at 11:29:55 rising to 25.60 at 11:31:40 during the slow reply's generation; up to 13.00 during the first request (11:27:20 to 11:28:25). Request boundaries are matched by `wall_s` and the busy-core columns |

## Section 05

| Page figure | Source |
|---|---|
| 114.1 GiB at start-up in the read-once run | `X/logs/ml4_round5.out` "server 0.4 of 114.1 GiB" (the second figure is the server's RSS; the first is the part in huge pages) |
| The before/after table: t/s, drive GB, major faults; 27-token and 8-token prompts | `X/results/l4-expz30-g3.jsonl` (mapped) and `l5-expz-huge.jsonl` (read once), tags `warm1`, `warm2`, `w300a`, `w300b`, `read2k`, `final`: `gen_tps`, `read_tps`, `drive_gb`, `major_faults`, `read_n`, `gen_n` |
| Card memory 29,915 / 29,686 / 26,116 MiB; RSS 114.1 GiB in a recorded 30-and-3 run | `X/logs/ml4_round5.out`, `ml4_round4.out`, `ml4_round3.out` "card ... MiB"; `ml4_round6.out` "of 114.1 GiB" with `scripts/rounds/round6.sh` `Z=30 GPU_N=3` |
| Mapped run pre-read 112.4 GiB in 18 s; read-once run skipped it | `X/logs/ml4_round4.out` "prefetch layers 3-41: 112.4 GiB in 18 s"; `scripts/rounds/round5.sh` `PREFETCH=0` |
| Huge pages: laptop worker on, desktop 0.4 GiB took | `scripts/rounds/round5.sh` (`ZENV`, `HUGE=1`); `X/logs/ml4_round5.out` "server 0.4 of 114.1 GiB, Z13 80.0 GiB" |
| Load 275 s and 251 s | `X/logs/ml4_round4.out` and `ml4_round5.out`, "ready after" |
| Tuned worker: 3.2%, 2.4%, 0.1% faster; reading 70.4 against 72.1 | `X/results/l9-expz30-g0-128k-ub1024.jsonl` (6.83, 6.74, 6.68; read 70.37) against `l10-final.jsonl` (6.62, 6.58, 6.67; read 72.1); worker settings in `scripts/rounds/round8.sh` (carried into round 9) and `round10.sh` |
| About 9% with the cache | as in section 04: three ratios 9.8%, 7.0%, 9.5% |

## Section 06

| Page figure | Source |
|---|---|
| 8.09 to 8.16; caps 800, 300, 800; 82.6 on 1,940 | `X/results/l11-expert3.jsonl` |
| 4 active per token by default | `vendor/mistral-large-4-model-card.md` (vendor) |
| 15 and 18 of 18 | `quality/judge-scores.json` joined with `quality/blind-map.json` |
| Statistics error | `quality/answers/large4-3experts-q4-statistics.json` (the answer text); score 2 in `judge-scores.json` |
| 15,405 against 7,640 tokens | `gen_n` in `quality/answers/large4-3experts-q2-probability.json` and `large4-q2-probability.json` (also in `blind-map.json`) |
| 28,051 and 22,115 tokens over six questions | sum of `gen_n` per setup over the six answer files (arithmetic) |

## Section 07

| Page figure | Source |
|---|---|
| Every score in the table | `quality/judge-scores.json` joined with `quality/blind-map.json` on question id and letter |
| Judge: OpenAI GPT-6 Astra, high reasoning effort | the judge run's log header (model `gpt-6-astra`, provider `openai`, reasoning effort `high`); not shipped |
| DeepSeek 16.66 to 16.77; Large 3 7.14 to 7.26; three experts 8.08 to 8.32 | `gen_tps` in each answer file under `quality/answers/` |
| Four-expert set: three answers from 31 October at 0.88 to 1.72 with a 6,000 cap; three timed out at 1,800 s and were rerun on 1 November with a 10,000 cap | `T/logs/round1.txt`; `scripts/run_round.sh` (cap 6000); `scripts/run_quality.sh` (cap 10000, `QIDS="q1-logic q2-probability q6-decision"`); `gen_tps` in `quality/answers/large4-q3-code.json` 1.72, `-q4-statistics.json` 1.37, `-q5-premise.json` 0.88 |
| Reruns: 4,000 to 12,000; 10,000 to 20,000 | `scripts/run_quality.sh` (Large 3 cap 4000) and `quality/answers-large3-cut-4000/` (`finish` `length`); `scripts/run_large3_more.sh` (12000); `scripts/run_e3_q2.sh` (20000); `quality/answers-large4-3experts-cut-10000/` |
| Treaty answers | `quality/answers/*-q5-premise.json` |
| Key slip, clues 5 and 6 | `quality/key.md` (corrected edition; the original line is quoted in `README.md`) |

## Section 08, Mistral Small 4

| Page figure | Source |
|---|---|
| 73,763,180,544 bytes, 68.7 GiB, on disk 21 November | `small4/shard-sizes.txt`, sum; / 2^30 = 68.70 (arithmetic) |
| 131,072 window | `small4/*.json` `props.default_generation_settings.n_ctx` |
| 8 threads, cores 0 to 7, experts of 26 layers in RAM | `scripts/run_variant.sh` |
| Prose and code pairs; every run at its cap | `small4/*.extra.json`, `speed[]` `runs[].gen_tps`, `gen_n`, `finish` |
| Prompts and caps (300 words on tides, 420; type hints on a supplied file, 1,400; temperature 0.15) | the Small 4 speed script `extra.py` (not shipped) |
| Next turn; long prompts 2,620, 48,624, 97,096 on the fastest row | `small4/*.json` `depth[].next_gen_tps`, `depth[].prompt_n` |
| Peak card MiB, RSS 70.8 GiB | `small4/*.json` `peak.gpu_mib`, `peak.rss_max_gib` |
| 3 of 3 codes, 5 of 5 tools, 4 of 5 quick checks, the checker miss | `small4/*.json` `depth[].codes`, `tools[].final_ok`, `quick[].ok` and `quick[].a`; the four questions, the coding task and its four assertions, and the pattern are in `scripts/smoke.py` |
| Reading 1,480 to 2,295 | `small4/*.json` `depth[].read_tps`, min 1,480.0 (`older-build-repeat`, 97K), max 2,295.1 (`new-dio-auto-ngram`, 48K) |
| Fastest row flags | `scripts/s4_round4.sh` (`new-dio-auto-ngram`, `b12015-dio-cache-ngram`), `scripts/s4_round1.sh` (`older-build-repeat`, `b12015-plain-2`), `scripts/run_variant.sh` |

## Section 09

| Page figure | Source |
|---|---|
| Laptop total RAM in use 88 GiB | `X/logs/ml4_round10.out` "Z13 88 GiB used" (`free -g` used column, whole machine) |
| Worker killed; desktop server aborted with a core dump; no server at 10 s; closed connection | `twobox-2026-11-02-fault-test.txt` |
| 31,168 MiB at start-up; 31,246 MiB highest sample | `X/logs/ml4_round10.out` |
| 126.0 GiB peak; available memory as low as 35.5 GiB | `X/logs/ml4_round10.out` "min available 35.5 GiB, RSS 126.0 GiB" (Linux `MemAvailable`) |
| 216 s in the test script, from 4 s after launch; 252 s through the start scripts | `X/logs/ml4_round10.out` "ready after 216 s" with `scripts/run_ml4.sh` (`sleep 4`, then a health poll); `twobox-2026-11-02-fault-test.txt` "healthy after 252.1 s" |
| 1,347 s for 96,325 tokens; next turn 4.2 and 5.0 s | `X/results/ml4-final.json` `read_s` 1347.3, `next_read_s` |
| Reasoning in every 1 November request | `reasoning` is non-empty on all 102 lines of `X/results/l*.jsonl` (count) |

## Section 10

| Page figure | Source |
|---|---|
| 2.2 to 2.8, about 4 | what our 31 October notes said (the lab's own summary; not in this package) |
| 1.18 to 2.87 after the first requests | as section 04, best-placement row |
| 1.11 to 1.43; 17.7 to 362.2 GB | `T/results/cache8g-*.json` |
| 7.20 to 7.42 against 6.72 to 6.76 | `X/results/l14-c5g-64k.jsonl`, `l14-plain.jsonl` |
| 1.45 to 3.20 against 3.22 to 3.96 | `X/results/l2-back26-t24.jsonl`, `l1-back26.jsonl` |
| Small 4: 19.37 and 13.29; 18.22 and 19.05; 33.51, 33.64; 34.73, 27.81 | `small4/b12015-plain.extra.json`, `older-build-baseline.extra.json`, `b12015-plain-2.extra.json`, `older-build-repeat.extra.json` |

## Section 11

| Page figure | Source |
|---|---|
| Greedy match: 48 of 48 on three prompts, 25 of 48 on the fourth | `X/results/l14-c5g-64k.logits.json` against `l14-plain.logits.json`: position-by-position token match over 4 prompts of 48 tokens (25, 48, 48, 48) |
| 96,325 deepest read; 131,072 window | `X/results/ml4-final.json`; `scripts/rounds/round10.sh` `CTX=131072` |
| 1M window | `vendor/mistral-large-4-model-card.md` (vendor) |
