# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/l3-threads/ . Paths are
relative to this folder. If a row and a file disagree, the file wins.

Three figure families on the page are verified reads or citations rather than
files in this package: the llama.cpp source-code reads of sections 07 and 10
(`cpu_count_math_cpus` / `common_cpu_get_num_math()` in `common/common.cpp` on
build `5f55650`, its two quoted comments, the `is_hybrid_cpu()` gate and the
non-hybrid fallback, and `llama-server --help` printing `(default: -1)`) — all
read directly on the build we ran, quoted on the page, checkable on any clone;
the project-history facts (PR #6414 merged 2024-04-16, its llamafile origin);
and the prior-art citations of section 09 (llama.cpp discussion #572, issue
#842, justine.lol/matmul, ramalama #934, the January 2026 MoE offload guide),
all named on the page with identifiers and dates. Hardware identity (Core
Ultra 9 285K, 8P+16E, no hyperthreading, 188 GiB RAM) is recorded in
`ab_run/RUN_LOG.md` and the dossier; the 41B-active figure is labelled "per
the release" on the page.

---

## Hero, 01 and 05: the A/B decode figures

| Figure on the page | File | Field |
|---|---|---|
| arm (a) warm decode 6.83 / 7.07 / 6.96 t/s | `ab_run/arm_a_probe2.json` .. `probe4.json` | `timings.predicted_per_second`: 6.834 / 7.072 / 6.958 (digest: `ab_run/arm_a_probes_summary.txt`) |
| arm (b) warm decode 5.82 / 6.96 / 7.09 t/s | `ab_run/arm_b_probe2.json` .. `probe4.json` | `timings.predicted_per_second`: 5.820 / 6.956 / 7.088 (digest: `ab_run/arm_b_probes_summary.txt`) |
| arm (c) warm decode 1.70 / 3.56 / 3.57 t/s | `ab_run/arm_c_probe2.json` .. `probe4.json` | `timings.predicted_per_second`: 1.704 / 3.559 / 3.574 (digest: `ab_run/arm_c_probes_summary.txt`) |
| arm (a) first generation 3.46 t/s, 897.0 s wall | `ab_run/arm_a_probe1.json`; `ab_run/arm_a_probes_summary.txt` | decode 3.461; `wall=897.0s`; server-side total 896,963.56 ms in `ab_run/arm_a_server.log` |
| arm (b) first generation 2.07 t/s, 969.8 s wall | `ab_run/arm_b_probe1.json`; `ab_run/arm_b_probes_summary.txt` | decode 2.066; `wall=969.8s` |
| arm (c) first generation 3.14 t/s, 130.5 s wall | `ab_run/arm_c_probe1.json`; `ab_run/arm_c_probes_summary.txt` | decode 3.137; `wall=130.5s`; prefill 8.35 t/s |
| loads to healthy 6 m 50.9 s / 2 m 06.1 s / 1 m 59.7 s | `ab_run/arm_{a,b,c}_server.log`; `ab_run/RUN_LOG.md` | "model loaded" timestamps 6.50.954 / 2.06.1xx / 1.59.7xx; per-arm log lines |
| the reproduced record: 3.56-3.57 against 3.58-3.61, "to within 0.05" | `ab_run/arm_c_probe3.json`/`probe4.json` vs `ladder/l3_ladder_results.tsv` | 3.559/3.574 vs the final (R7 winner) row's "3.58-3.61"; 3.61 − 3.56 = 0.05 (arithmetic) |
| the thread-count witness: 33 threads vs 53, difference 20 = 24 − 4 | `ab_run/RUN_LOG.md` (arm (c) load notes); `ab_run/arm_{a,b,c}_pid.txt` | "process nlwp = 33 vs 53 in arms (a)/(b)"; the PIDs the counts were read from |
| pre-registered bands "about 3.6" = 3.2-4.2, "about 6" = 5.5-6.7; two probes above the 6.7 edge | `ab_run/RUN_LOG.md` | VERDICT LOGIC block (written before any measurement); probes 7.072 / 7.088 vs the band edge |
| wall-clock corroboration: 200 tokens in ~28.5 s ≈ 7.0 t/s, ~56.3 s ≈ 3.56 | `ab_run/arm_{a,b}_probes_summary.txt`, `ab_run/arm_c_probes_summary.txt` | walls 28.4-29.5 s (arms a/b warm), 56.2-56.5 s (arm c probes 3-4); division (arithmetic) |
| the two transient dips (5.82 with a mid-run sag; 1.70) | `ab_run/arm_b_probe2.json`, `ab_run/arm_c_probe2.json`; sag detail in `ab_run/arm_b_server.log` and `ab_run/RUN_LOG.md` | decode 5.820 / 1.704; tg_3s sag lines |

## 01, 02 and 08: VRAM, corrected

| Figure | File | Field |
|---|---|---|
| 24,420 MiB used = 23.85 GiB; arms (a) and (b) identical | `ab_run/arm_a_nvidia_smi.txt`, `ab_run/arm_b_nvidia_smi.txt` | "24420, 32607" (raw MiB); 24,420/1024 = 23.85 |
| arm (c) 24,375 MiB | `ab_run/arm_c_nvidia_smi.txt` | "24375, 32607" |
| 8,187 MiB = 8.00 GiB free | derived | 32,607 − 24,420 = 8,187 (arithmetic; total from the same nvidia-smi lines) |
| card total 32,607 MiB | every `ab_run/arm_*_nvidia_smi.txt` | second field |
| "24.6 GiB" was 24,627 MiB = 24.05 GiB | `ladder/l3_ladder_results.tsv`; `REPORT_l3_claims_dossier.md` §1 | R7 winner row `vram_mib` 24627 |
| "27.6" was 27,624 MiB = 26.98 GiB | `ladder/l3_ladder_results.tsv`; dossier §1 | R3_ncmoe58 row `vram_mib` 27624 |
| "15.1" was 15,082 MiB = 14.73 GiB | `ladder/l3_probes.log`; dossier §1 | final line "15082 MiB" |
| desktop baseline ~830-900 MiB inside every reading | `ab_run/RUN_LOG.md` | pre-run GPU 902 MiB; per-arm pre-load 891/826/827 MiB; final 827 MiB |
| the ≥6 GiB-free ceiling holds with more margin (8.00 vs 7.79 GiB) | `FINDINGS_l3_warmup_ab.md`; dossier §1 | corrected-VRAM section; free-figures row |
| the slip family: raw MiB divided by 1000, caught before on three other models' records | `REPORT_l3_claims_dossier.md` | Units preamble ("the same slip family...") |

## 02 and 03: environment and the record before the test

| Figure | File | Field |
|---|---|---|
| 190.80 GB on disk = 177.7 GiB, 4 shards | `REPORT_l3_claims_dossier.md` §5 | "On-disk bytes sum to 190,801,132,352 = 190.80 GB", 4 shards vs the HF manifest |
| arch: `deepseek2`, 61 blocks (3 dense), 128 experts (4 routed + 1 shared), 1 KV head | dossier §4 | GGUF shard-1 header values, re-verified during the audit |
| build `5f55650` | `ab_run/arm_*_probe*.json` | `system_fingerprint`: "b1-5f55650" |
| canonical flags: `-c 32768 -b 4096 -ub 2048 --parallel 1 --threads 24 --threads-batch 24`, temp 0.15 pinned at launch, warmup default on | `ab_run/arm_exec_blocks.txt`; `ab_run/arm_scripts.diff` | arm (a)'s invocation = the canonical configuration (loopback host aside) |
| the canonical script was never edited; SHA-256 recorded before and after | `ab_run/arm_scripts.sha256`; `ab_run/RUN_LOG.md` | digest `eeff0e3f...`; FINAL RELEASE block ("unchanged") |
| probe: temp 0, max_tokens 200, one fixed prompt → 557-token prefill; 4 probes per arm, 3 warm | `ab_run/run_probes.sh`; `ab_run/arm_*_probes_summary.txt` | request body; `prompt_n=557` on every probe 1 |
| the ladder ran `--no-warmup`, no `--threads`, 4 slots | `ladder/l3_tuning_ladder.sh` (line 28); `ladder/ladder_R7_ncmoe59.log` | base args; "n_slots = 4, n_ctx_slot = 32768" |
| ladder winner decode 3.58-3.61 | `ladder/l3_ladder_results.tsv`; `ladder/ladder_R7_ncmoe59.log` | final row; per-generation eval lines 3.29 → 3.53 → 3.58 → 3.61 |
| smoke read 5.98-6.28, warmup on, threads 24, 1 slot | `ladder/l3_canonical_smoke.log` | eval lines 6.28 (36 tok) and 5.98 (260 tok); "n_slots = 1" |
| the smoke's first prefill: 547 tokens at 3.67 t/s = 149 s | `ladder/l3_canonical_smoke.log` | "prompt eval time = 149099.07 ms / 547 tokens ... 3.67" |
| A/B arms all `n_slots = 1` | `ab_run/arm_{a,b,c}_server.log` | "initializing, n_slots = 1" |

## 06: what warmup did in this run

| Figure | File | Field |
|---|---|---|
| major-faulting at ~67 MB/s in uninterruptible sleep; cumulative reads past 237 GB against the 190.80 GB file; RSS 169.6→161 GB | `ab_run/RUN_LOG.md` | arm (a) probe-1 notes (state D, `folio_wait_bit_common`, read_bytes) — process-state reads, labelled as such on the page; see the GB/GiB annotation inside the file |
| arm (b)'s fault cost reappearing in the first generation (7.4M+ majflt) | `ab_run/RUN_LOG.md` | arm (b) probe-1 notes |
| ~154 GiB of experts CPU-side (derived, labelled) | `REPORT_l3_claims_dossier.md` §4 | 177.7 GiB file minus ~24 GiB GPU-resident (arithmetic, not instrumented) |
| prefill 8.35 t/s on the third load's first answer | `ab_run/arm_c_probe1.json`; `ab_run/arm_c_probes_summary.txt` | `timings.prompt_per_second` 8.35 |

## 09 and 11: scope numbers

| Figure | File | Field |
|---|---|---|
| this week's warm band 5.8-7.1 vs the smoke's 5.98-6.28: compatible, not a finding | `ab_run/arm_{a,b}_probes_summary.txt` vs `ladder/l3_canonical_smoke.log` | warm decodes 5.820-7.088 vs 5.98/6.28 |
| the 897 s / 970 s / 130 s first answers (cache history, not an arm contrast) | `ab_run/arm_{a,b,c}_probes_summary.txt` | probe-1 walls |
| the thread axis's two measured points, 4 and 24 | `ab_run/arm_exec_blocks.txt` (24 pinned; line absent in arm (c)); `ab_run/RUN_LOG.md` (nlwp delta → 4) | |

## 12: the timeline

| Figure | File | Field |
|---|---|---|
| 2026-08-04/05 ladder and smoke | `ladder/l3_tuning_ladder.sh` output dates; `ladder/l3_probes.log` ("2026-08-05T00:19:42-04:00"); `ladder/l3_ladder_results.tsv` | |
| 2026-08-11 audit, then the A/B at 01:15-02:10 EDT | `REPORT_l3_claims_dossier.md` (header); `ab_run/RUN_LOG.md` (start/FINAL RELEASE stamps) | |
| GPU released clean (827 MiB ≤ the 902 MiB pre-run baseline) | `ab_run/RUN_LOG.md` | FINAL RELEASE block |

*If you find a figure on the page that is not in this table, that is a bug in
this table; tell us.*
