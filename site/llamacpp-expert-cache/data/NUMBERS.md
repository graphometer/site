# NUMBERS: every figure on the page, with its file and field

> Note, 21 November 2026: the page this file belongs to was rewritten in plain language on this date and its sections were reordered. Section numbers in this file refer to the page as it stood before. The figures and the files are unchanged.

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

The one place a file will look like it contradicts the page: a screen file's `peak.avail_min_gib` is often higher than
the page's "lowest free RAM", because the page takes the lowest across every run of the same command (listed per model
in `tools/page_table.py`, `ROWS`, sixth and seventh fields).

`python3 tools/page_table.py` prints every table figure below from these files; its output is `derived_page_table.txt`.
All paths are under `runs/`.

## Column rules (sections 03, 04, 05, 06)

| Page column | File | Field |
|---|---|---|
| Writing, short; Second answer | `<run>.screen.json` | `steps[step=prose2].gen_tps` |
| First answer | `<run>.screen.json` | `steps[step=prose1].gen_tps`; its seconds: `.wall_s`; tokens: `.gen_n` |
| Writing at 20K | `<run>.screen.json` | `steps[step=next].gen_tps` |
| Read, 20K | `<run>.screen.json` | `steps[step=read].read_tps`; tokens: `.read_n`; code found: `code_ok` |
| Code | `<run>.screen.json` | `steps[step=code].gen_tps` |
| Start to ready, s (main table); cold load, s (section 04) | `logs/RUNS.log` or `logs/ready_and_trap_lines.txt` | `<run>: pid <PID> ready after S s` |
| Pinned at start, GiB | same ready line | `RssShmem`; mapped file pages: `RssFile` |
| Card peak, MiB (before and after) | `<run>.screen.json` and, for the after column, the extra files in `ROWS` | the largest `peak.gpu_mib` among those files (sampled every 2 s; other starts of the same command can differ) |
| Lowest free RAM, GiB | same files | the smallest `peak.avail_min_gib`, one decimal |
| Drive reads (Beam 1.0, 57.9 GB) | `r1/results/beam-1.0-ship.screen.json` | sum of `steps[].drive_GB` |
| Window, cache size, micro-batch, load mode, conversation cache | `logs/cmd/<run>.cmd` or `.cmdline` | `--ctx-size`, `--moe-cache-mib`, `--ubatch-size`, `--load-mode`, `--cache-type-k` (the last one given wins) |
| Build | `<run>.screen.json` | `props.build_info` |

## The runs behind each row (before, dio alone, after)

| Page row | Before | Dio alone | After |
|---|---|---|---|
| DeepSeek V4.1 Flash | `r1/.../deepseek-v4.1-flash-ship` | `deepseek-v4.1-flash-dio` | `final-deepseek-v4.1-flash` |
| GLM-5.3-Flash | `glm-5.3-flash-ship` | `glm-5.3-flash-dio` | `final-glm-5.3-flash` |
| DeepSeek V4 Flash 0731 | `deepseek-v4-flash-ship` | `deepseek-v4-flash-dio` | `final-deepseek-v4-flash` (+ `deepseek-v4-flash-proof` for card and RAM) |
| MiMo-V2.6-Flash | `mimo-v2.6-flash-ship` | `mimo-v2.6-flash-dio` | `final-mimo-v2.6-flash` |
| Qwen3.8-Flash-Next | `qwen3.8-flash-next-ship` | `qwen3.8-flash-next-dio` | `final-qwen3.8-flash-next` (+ proof) |
| Ornith-1.5-122B | `ornith-1.5-122b-ship` | `ornith-1.5-122b-dio` | `final-ornith-1.5-122b` (+ proof) |
| gpt-oss-120b | `gpt-oss-120b-ship24` | none | `final-gpt-oss-120b` (+ proof) |
| Ling-3.0-flash | `ling-3.0-flash-ship` | `ling-3.0-flash-dio` | `final-ling-3.0-flash` (+ proof) |
| Qwen3.5-397B-A17B | `qwen3.5-397b-ship` | none | `final-qwen3.5-397b` (+ proof) |
| Qwen3-Coder-Next | `qwen3-coder-next-ship` | `qwen3-coder-next-dio` | `final-qwen3-coder-next` (+ proof) |
| Nemotron 3.5 Bolt | `nemotron-3.5-bolt-ship` | `nemotron-3.5-bolt-dio` | `final-nemotron-3.5-bolt` (+ proof) |
| Beam 1.0 | `beam-1.0-ship` | `beam-1.0-dio` | `final-beam-1.0` (+ proof) |
| Muse Spark Open | `muse-spark-open-ship` | `muse-spark-open-dio` | `final-muse-spark-open` (+ proof) |
| Inkling-Small | `inkling-small-ship` | `inkling-small-dio` | `final-inkling-small` (+ proof) |
| Qwen3-235B-A22B | `qwen3-235b-ship` | `qwen3-235b-dio` | `final-qwen3-235b` |
| Qwen3.5-122B-A10B | `qwen3.5-122b-ship` | none | `final-qwen3.5-122b` |
| Qwen3.6-35B-A3B | `r2/.../qwen3.6-35b-a3b-screen-ship` (+ `-deep-ship`) | `qwen3.6-35b-a3b-screen-dio` | `final-qwen3.6-35b-a3b` (+ `-deep-c18u4`, `-proof-c18u4`) |
| Qwen3-30B-A3B, 262,144 | `qwen3-30b-a3b-screen-ship` (+ `-deep-ship`) | `qwen3-30b-a3b-screen-dio` | `final-qwen3-30b-a3b` (+ `-deep-q8c115u4`, `-proof-q8c115u4`) |
| Qwen3-30B-A3B, 131,072 | `qwen3-30b-a3b-deep-128ship` | none | `final-qwen3-30b-a3b-128` (+ `-proof-128c135u4`) |
| Ornith-1.5-35B | `r3/.../ornith-1.5-35b-ship` | `ornith-1.5-35b-dio` | `final-ornith-1.5-35b` (+ `ornith-1.5-35b-c18`) |

Where a ready line appears twice (the r2 end-to-end runs ran twice, in `final.out` and later in `round6.out`), the
screen file is the later run's, so the page prints the later load: 42, 46 and 47 seconds. The earlier starts took 43,
46 and 46.

## Derived figures (arithmetic on the fields above)

| Page figure | Derivation |
|---|---|
| Writing 1.44 to 2.88 times (11 large cached models) | after / before `prose2.gen_tps`: Bolt 81.14 / 56.18; Ling 114.34 / 39.77 |
| At 20K, 1.42 to 2.76 times | after / before `next.gen_tps`: Bolt 78.83 / 55.42; Ling 106.08 / 38.48 |
| 1.25, 1.34, 3.38, 4.99 times | Ornith-1.5-35B 173.23 / 138.1; Qwen3.6-35B-A3B 175.3 / 131.06; Qwen3-30B-A3B 171.26 / 50.72 and 147.98 / 29.67 |
| dio-only rows within 5 percent | largest: Muse Spark Open at 20K, 6.35 / 6.05 = 1.0496 |
| Read 1.60 to 3.13 times (14 mapped), 1.96 to 3.13 (12 large) | dio / before `read.read_tps`: Ornith-1.5-35B 7070.4 / 4408.5; Qwen3.8-Flash-Next 1373.9 / 439.0; GLM-5.3-Flash 1239.4 / 633.6 |
| Cold load 29 to 63 percent | dio / before load: Qwen3.6-35B-A3B 14 / 48 = 29.2%; Qwen3-Coder-Next 15 / 24 = 62.5% |
| Writing with dio, minus 3.4 to plus 2.1 percent | dio / before `prose2.gen_tps`: Ornith-1.5-35B 133.35 / 138.1; Qwen3-235B-A22B 11.73 / 11.49 |
| 2.0 to 3.1 times (subtitle) | the 12 large mapped models: read 1.96 to 3.13 times, rounded to one decimal |
| Cache rows 1.4 to 2.9 (subtitle) | 1.44 and 2.88 above, rounded to one decimal |
| 8 of 12 cached models read slower than dio alone | `read.read_tps`, after against dio alone: slower on GLM-5.3-Flash, DeepSeek V4 Flash, MiMo-V2.6-Flash, Qwen3.8-Flash-Next (1021.2 against 1373.9), Ornith-1.5-122B, Qwen3-Coder-Next, Nemotron 3.5 Bolt, Ornith-1.5-35B; faster on DeepSeek V4.1 Flash, Ling-3.0-flash, Qwen3.6-35B-A3B, Qwen3-30B-A3B 256K |
| Placement changed on 13 of 15 cached rows; build on 7 rows (6 models) | `--cpu-moe` against `--n-cpu-moe N` or `--fit on` in each row's before and after `logs/cmd/` files (DeepSeek V4 Flash and Ling-3.0-flash use `-cmoe` on both sides); `props.build_info` before and after |
| Card use rose on 9 of 15 cached rows, fell on 6 | before and after `card` in `derived_page_table.txt`: fell on gpt-oss-120b, Qwen3-Coder-Next, Nemotron 3.5 Bolt, Qwen3.6-35B-A3B, Qwen3-30B-A3B 256K, Ornith-1.5-35B |
| Qwen3-30B-A3B depth gain 2.8 and 1.36 times | `r2/results/qwen3-30b-a3b-deep-q8c115u4.json` / `-deep-ship.json`, `depth[].next_gen_tps`: 76.6 / 27.5; 28.9 / 21.3 |
| Start script checks, 20 to 28 s | ready lines: `nemotron-3.5-bolt-inst-c17` 33 and `final-nemotron-3.5-bolt` 53; `glm-5.3-flash-b15-c11` 87 and `final-glm-5.3-flash` 110; `ornith-1.5-122b-inst-c18` 47 and `final-ornith-1.5-122b` 70; `ornith-1.5-35b-c18` 20 and `final-ornith-1.5-35b` 48 |
| PR build within 3.2 percent on four | `prose2.gen_tps` new / release: 19.65 / 19.97, 78.53 / 81.11, 110.89 / 110.74, 62.82 / 61.5 |

## Other figures

| Page figure | File | Field or line |
|---|---|---|
| GLM-5.3-Flash 123.7 GiB mapped, 117.5 GiB shared | `r1/logs/RUNS.log` | ready lines of `glm-5.3-flash-ship` (`RssFile`) and `glm-5.3-flash-dio` (`RssShmem`) |
| Already pinned: 93.0, 31.1, 49.4 GiB; 0.1 or 0.2 mapped | ready lines of `qwen3-235b-ship`, `r2` `qwen3-30b-a3b-screen-ship`, `qwen3.5-122b-ship` | `RssShmem`, `RssFile` |
| Desktop's own card use 710 to 1,642 MiB | `r1/logs/RUNS.log` | the lowest and highest of `<run>: stopped, card N MiB` |
| DeepSeek V4 Flash first answer 9.87 against 13.31 | `r1/results/deepseek-v4-flash-dio.screen.json` | `prose1.gen_tps`, `prose2.gen_tps` |
| Beam 1.0 first 420 tokens at 1.95 | `r1/results/beam-1.0-ship.screen.json` | `prose1.gen_n`, `prose1.gen_tps` |
| Beam 1.0 stall: 53.8 to 61.9 s, 7.62 to 8.38 t/s; 122.5 s, 3.62 t/s | `beam-1.0-dio`, `final-beam-1.0-again1`, `final-beam-1.0-again2`; `final-beam-1.0` `.screen.json` | `prose1.wall_s`, `prose1.gen_tps` |
| Qwen3.5-122B-A10B 12,000 MiB: 41.49, 40.54, 498.2 | `r1/results/qwen3.5-122b-b15-c12.screen.json` | `prose2`, `code`, `read` |
| Qwen3-235B-A22B before card 31,801 MiB | `r1/results/qwen3-235b-ship.screen.json` | `peak.gpu_mib` |
| Muse Spark Open 64K, 7,000 MiB: 11.47 and 8.43 | `r1/results/muse-spark-open-b15-64k-c7.screen.json` | `prose2`, `next`; window in `logs/cmd/muse-spark-open-b15-64k-c7.cmd` (65536) |
| DeepSeek V4.1 Flash 11,000 and 13,000 MiB: 44.95, 47.88 | `deepseek-v4.1-flash-b15-c11`, `-b15-c13` `.screen.json` | `prose2.gen_tps` |
| Nemotron 3.5 Bolt 12,000 and 17,000 MiB: 69.33, 78.84 | `nemotron-3.5-bolt-inst-c12`, `-inst-c17` `.screen.json` | `prose2.gen_tps` |
| Qwen3-30B-A3B 10,000 and 13,000 MiB: 130.8, 160.76; 2,000 MiB with the 16-bit conversation cache: 23.68; Qwen3.6-35B-A3B 18,000, 20,000, 20,500 MiB: 176.32, 175.51, 176.24 | `r2/results/qwen3-30b-a3b-screen-q8c10`, `-q8c13`, `-f16c2`, `qwen3.6-35b-a3b-screen-c18`, `-c20`, `-c205` `.screen.json` | `prose2.gen_tps` |
| Five scripts 1,000 MiB below a size that ran; peaks 31,174 to 31,735 MiB | `qwen3-coder-next-inst-c19.screen.json` (31,174), `gpt-oss-120b-b15-c20.screen.json` (31,463), `glm-5.3-flash-proof.json` (31,552), `deepseek-v4.1-flash-proof.json` (31,581), `mimo-v2.6-flash-proof.json` (31,735) | `peak.gpu_mib`; sizes in their `logs/cmd/` files |
| Hit rates 1.51, 33.26, 46.07 percent (batches of 8 or fewer); 1.65 and 0.11 for larger batches | `r1/logs/server_log_excerpts.txt` | `llama_moe_cache: ubatch <= 8 ... hit rate` (and the `ubatch  > 8` line under it) for `deepseek-v4-flash-b15-c45`, `-inst-c45`, `-b15-u4096-c7` |
| 11.75, 17.15, 20.13; 13.31 | `deepseek-v4-flash-b15-c45`, `-inst-c45`, `-b15-u4096-c7`, `-dio` `.screen.json` | `prose2.gen_tps` |
| Depth table (section 06) | `r2/results/qwen3.6-35b-a3b-deep-ship.json`, `-deep-c18u4.json`, `qwen3-30b-a3b-deep-ship.json`, `-deep-q8c115u4.json`, `-deep-128ship.json`, `-proof-128c135u4.json`; `r3/results/ornith-1.5-35b-ship.json`, `-c18.json` | `depth[].next_gen_tps`, `depth[].read_tps`, `depth[].prompt_n`, `depth[].codes` |
| Ling 9,764 MiB before | `r1/results/ling-3.0-flash-ship.screen.json` | `peak.gpu_mib` |
| Cached card peaks 29,629 to 31,289 MiB | after rows of the main table | Ling-3.0-flash (with proof) and DeepSeek V4 Flash (with proof) |
| Before free RAM 156 to 162 GiB | before rows of the 12 large mapped models | `peak.avail_min_gib`: GLM-5.3-Flash 156.3, Qwen3-Coder-Next 162.2 |
| Warm restart 4 s twice; 20 or 21 s on eight starts | `r3/logs/RUNS.log` | ready lines of `ornith-1.5-35b-ship2`, `-deep-ship` (4 s); `-c18`, `-c18np`, `-c12`, `-c15`, `-ngram`, `-c18-128`, `-mtp15`, `-deep-cache` (20 or 21 s) |
| GLM-5.3-Flash dio starts 84 to 103 s | `r1/logs/RUNS.log`, `ready_and_trap_lines.txt` | `glm-5.3-flash-dio` 103, `-new-dio` 100, `-new-c11` 86, `-b15-c11` 87, `-b15-c12` 84, `-b15-u4096-c14` 92, `glm-5.3-flash-proof` 86 |
| gpt-oss-120b 23 layers: 1,315.93 MiB refused | `r1/logs/server_log_excerpts.txt` | `gpt-oss-120b-ship.server.log` lines; 23 in `logs/cmd/gpt-oss-120b-ship.cmd` (`--n-cpu-moe 23`) |
| Out of memory at load or warm-up (11 cache setups) and the gpt-oss-120b before command | `r1/logs/server_log_excerpts.txt`, `r3/logs/server_log_excerpts.txt` | `qwen3-coder-next-inst-c21`, `-new-c21`, `qwen3.5-122b-b15-c17`, `-new-c17`, `qwen3-235b-b15-q8-c12`, `qwen3.5-397b-b15-c12`, `-new-c12`, `glm-5.3-flash-new-c14`, `deepseek-v4-flash-b15-128k-c11`, `qwen3.8-flash-next-inst-c17` (after the warm-up line), `ornith-1.5-35b-mtp` |
| MiMo-V2.6-Flash crash on the PR build | `r1/logs/server_log_excerpts.txt` | `mimo-v2.6-flash-new-c14.server.log`: cache size line, then `ggml-impl.h:330: fatal error` |
| PR build table (section 08) | `*-b15-c11`, `*-new-c11`, `*-b15-c20`, `*-new-c20`, `*-inst-c18`, `*-b15-c18`, `*-new-c18`, `*-inst-c45`, `*-b15-c45`, `*-new-c45`, `*-inst-c15`, `*-new-c15` `.screen.json` | `prose2`, `code`, `next`; build in `props.build_info`; `--moe-cache-cpu-share auto` in `logs/cmd/*-new-*.cmd` |
| Sealed codes 3 of 3 at depth (14 models; 16 at 48K) | `r1/results/*-proof.json`, `final-*.json` | `depth[].codes`, `depth[].depth` |
| Quick checks 5 of 5, Inkling-Small 4 of 5, tools 5 of 5 | `*-proof.json`, `r2/results/*-proof-*.json`, `r3/results/ornith-1.5-35b-c18.json` | `quick[].ok`; `tools[]` with `called`, `args_ok`, `final_ok`; Inkling's miss in `quick[].a` |
| Boundary reads 24 of 24 on 15 cached setups | `final-*.stress.json` (the 15 cached after setups; `tools/stress.py` sizes and pass rule) | count of `ok` true, `err` null |
| Ling crash prompt: 2,999 and 3,007 tokens; 40 of 40 | `r1/logs/RUNS.log`, `ready_and_trap_lines.txt` | `TRAP ling-3.0-flash-proof`, `TRAP final-ling-3.0-flash` |
| Turns that hit the cap | `final-ling-3.0-flash`, `final-mimo-v2.6-flash` (turn1), `final-ornith-1.5-122b`, `r2/results/final-qwen3.6-35b-a3b` (turn2) `.usable.jsonl`; `ling-3.0-flash-proof.usable.jsonl` (turn1, turn2) | `finish` length, `gen_n` 2500 |
| Output table (section 09) | the `*.logits.json` pairs in `tools/page_table.py`, `LOGIT` | computed as in `tools/logit_compare.py` |
| Muse Spark Open 72 of 192 | `muse-spark-open-shiplogit.logits.json` against `muse-spark-open-ship3.logits.json` | same computation |
| Qwen3-30B-A3B right or wrong: 106, 107, 105 of 128; 1 unread; jug 22, 23, 21 of 24 at 97K | `r2/logs/quality.out` | the line beginning `all`; the `97K jug` line |
| Ornith-1.5-35B thinking off: 74 and 77 of 128, 17 and 20 unread | `r3/results/ornith-1.5-35b-ship.qoff.json`, `ornith-1.5-35b-c18.qoff.json` | `python3 tools/ornith-1.5-35b_quality_off.py --compare ornith-1.5-35b-ship ornith-1.5-35b-c18`, line beginning `all` |
| Ornith-1.5-35B control, 192 of 192 | `r3/results/ornith-1.5-35b-ship.logits.json` against `ornith-1.5-35b-ship2.logits.json` | same computation as the output table |
| 2 of 15 cached comparisons match at every position | output table: Nemotron 3.5 Bolt 150 of 150, Qwen3.5-397B-A17B 145 of 145 | |
| Qwen3.5-122B-A10B before code 42.79 | `r1/results/qwen3.5-122b-ship.screen.json` | `steps[step=code].gen_tps` |
| Ornith-1.5-122B code 38.52 against 39.00, reply after read 42.83 against 42.62 | `ornith-1.5-122b-new-c18`, `-b15-c18` `.screen.json` | `code`, `next` |
| Prompt 22 to 162 tokens; caps 420, 700, 300; seed 42 | every main-table `.screen.json`, `steps[step=prose2].read_n`; `tools/screen.py` (`max_tokens`, `seed`) | |
| Beam 1.0 repeat peaks 31,402 and 31,409 MiB | `r1/results/final-beam-1.0-again1`, `-again2` `.screen.json` | `peak.gpu_mib` |
| Hand against start-script loads | ready lines named in "Start script checks" above; flags in their `logs/cmd/` files (hand starts add `-lv 4`; `ornith-1.5-35b-c18` adds `--no-reasoning-preserve`) | |
| MiMo-V2.6-Flash reasoning budget 14,000 | `logs/cmd/mimo-v2.6-flash-ship.cmd`, `final-mimo-v2.6-flash.cmdline` | `--reasoning-budget` |
| Draft head and presence penalty 1.5 | `logs/cmd/qwen3.5-397b-ship.cmd`, `final-qwen3.5-397b.cmdline`, `qwen3.5-122b-ship.cmd`, `final-qwen3.5-122b.cmdline` (`--spec-type draft-mtp`), `ornith-1.5-122b-*` (`--presence-penalty 1.5`) | |
