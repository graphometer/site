# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/speculation-gate/ . Paths
are relative to this folder; `lowerarm/` rows belong to the follow-up run and
are never pooled with the main run's. If a row and a file disagree, the file
wins.

Two figure families on the page are citations rather than measurements of ours
and have no file here: the llama.cpp history and pull-request facts of sections
01, 02, 06 and 09 (commit hashes `d9d54e498`, `abd4d0bc4`, `d14ce3dab`; PRs
#10362, #11954, #23269; issues #26100, #25908; the koboldcpp, neoteric.no,
juejin and cmp-nct results of section 10), all named on the page with their
identifiers and dates, and the one third-party artifact we do preserve, under
`third-party/` (see section 10 below).

---

## Hero and section 01: the headline contrasts

| Figure on the page | File | Field |
|---|---|---|
| prose 19.8% slower under the shipped default [95% CI −24.7 to −17.9] | `analysis/analysis.md` | PROSE table, `ungated` row: −19.79% [−24.67%, −17.90%] |
| structured 22.5% faster in the same run [+7.6 to +41.9] | `analysis/analysis.md` | STRUCTURED table, `ungated` row: +22.53% [7.57%, 41.94%] |
| prose +18.6% / +21.9% / +22.8% at gates 0.50 / 0.75 / 0.90 | `analysis/analysis.md` | PROSE table: 18.58% / 21.87% / 22.78% |
| structured +38.4% / +47.0% / +47.7% at the same gates | `analysis/analysis.md` | STRUCTURED table: 38.41% / 47.02% / 47.72% |
| gates 0.10 and 0.25 were prose regressions in their own right: −32.0% [−38.6, −27.4] and −23.7% [−27.9, −20.1] | `lowerarm/analysis/analysis.md` | PROSE table: −32.04% [−38.58%, −27.37%] and −23.73% [−27.92%, −20.09%] |
| pooled −4.45% with a 95% interval of [−19.6, +19.6] | `analysis/analysis.md` | POOLED table, `ungated` row: −4.45% [−19.56%, 19.62%] |
| prose byte-identical to baseline 0 times out of 16 under every speculative setting | `analysis/analysis.md`, `lowerarm/analysis/analysis.md` | Output-equivalence tables: prose 0/16 for `ungated`, `gate_0.50`, `gate_0.75`, `gate_0.90`, `gate_0.10`, `gate_0.25` |
| the baseline reproduces itself 16/16 across restarts | `records/none_cycle1_4574baed.jsonl` vs `records/none_cycle2_8ac19fed.jsonl` | `output.sha256` per `prompt.id`: equal on all 16 |
| roughly 127 GB of weights resident in CPU RAM | `loads/load_ungated_c1.json` (and the other nine) | `server_rss_mb` 126,804 |
| 160 paired measurements, main run; 96, follow-up; zero excluded | `analysis/analysis.md`, `lowerarm/analysis/analysis.md` | headers ("160 eligible", "96 eligible") and exclusions tables (warmup and calibration roles only) |

## Section 02: environment

| Figure | File | Field |
|---|---|---|
| four GGUF shards, ~150 GB on disk | `RUN_LOG.md` | preflight table, shard bytes summing to 149,840,422,542 |
| build `c8e03ce`, verified two ways | `RUN_LOG.md` preflight (`version: 1 (c8e03ce)`); every record | `system_fingerprint` rides the streamed chunks; the record's `config.server_props_fingerprint` and the RUN_LOG identity caveat carry the rest |
| the 17.9 KB thin-launcher caveat | `RUN_LOG.md` | identity caveat block (17,920 bytes) |
| VRAM ~20.3 GB baseline, 24.0 to 24.1 GB with speculation | `loads/load_none_c1.json` (20,270 MiB), `loads/load_gate075_c1.json` (24,103 MiB), and the rest | `vram_mb_after_load` |
| placement and server flags, port 8197, one varied flag | `flags/` (all ten files) | full argv per load; only `--spec-type/--spec-draft-n-max/--spec-draft-p-min` differ between treatments |
| requests: temperature 0, seed 42, max_tokens 256, streaming usage | any record | `config` block and `request.body` |
| argv read back from `/proc/<pid>/cmdline` on every row | `flags/` (content), `RUN_LOG.md` (procedure); `lowerarm/RUN_LOG.md` shows the capture command inline | |
| the VRAM step as treatment witness | `loads/` | baseline ~20.3 GB vs speculative ~24.0 GB, both runs (`lowerarm/loads/`: 20,499 vs 24,298–24,360 MiB) |

## Section 03: the experiment

| Figure | File | Field |
|---|---|---|
| ten server loads, five treatments × two cycles, cycle 2 reversed | `RUN_LOG.md` | the ten invocation blocks and the row-by-row table (ordinals 1–10) |
| sixteen prompts per session plus warmup and calibration | `sessions/session_none_c1.log` (and the other nine) | 19 numbered lines: warmup, calibration_pre, 16 measurements, calibration_post |
| six loads, 96 measurements, follow-up | `lowerarm/RUN_LOG.md` | six invocation blocks and its row table |
| pre-registration written before row 1 | `RUN_LOG.md` ("written 2026-08-10 18:15, BEFORE row 1"), `lowerarm/RUN_LOG.md` ("written 2026-08-11 00:08 EDT, BEFORE row 1") | the two pre-registration blocks, endpoints, contrasts, knee rule, tiebreak |
| the decode-rate estimator and its N/(N−1) bias | any record | `endpoint.rate_definitions`, both definitions embedded verbatim |
| primary vs interval-basis never diverged by more than 0.02 pp | `analysis_interval_basis/analysis.md` vs `analysis/analysis.md`; `lowerarm/analysis_interval_basis/analysis.md` | headline cells; the RUN_LOG final-state blocks record the 0.02 pp maxima |
| bootstrap: 95% cluster, 2,000 resamples, percentile, no BCa | every `analysis.md` | CI caveat lines under each table |
| #26100 cleared on four grounds | `flags/` (no `--cache-prompt` in any argv), `loads/` (ten distinct PIDs), `records/` (no prompt repeated within a session), `analysis/measurements.csv` | fastest observation: max `decode_rate_tps_primary` 19.17 t/s vs baseline ~9.8–10.7, about 1.9× |

## Section 04: the headline tables

| Figure | File | Field |
|---|---|---|
| every cell of both vs-none tables (medians, % changes, CIs) | `analysis/analysis.md` | PROSE and STRUCTURED tables, verbatim; per-pair detail in `analysis/pairs.csv`, per-observation in `analysis/measurements.csv` |
| every cell of the gates-vs-default table | `analysis_vs_ungated/analysis.md` | PROSE (+49.82 / +53.12 / +52.65) and STRUCTURED (+15.07 / +18.03 / +21.92) tables with CIs |
| the structured 0.50-vs-default interval contains zero | `analysis_vs_ungated/analysis.md` | STRUCTURED `gate_0.50` row: [−0.75%, 26.36%] |

## Section 05: pooled

| Figure | File | Field |
|---|---|---|
| pooled −4.45% [−19.56, +19.62]; components −19.8% and +22.5% | `analysis/analysis.md` | POOLED and subset tables |
| the previous evening's pooled −6.5% (different prompt set) | **not in this package** | a project record of the 2026-08-09 exploratory run, quoted on the page as a mild reproducibility note only |

## Section 06: acceptance

All acceptance figures are `server_diagnostic.timings.draft_n_accepted /
draft_n` per measurement observation, computable from every record; n = 16 per
treatment × subset.

| Figure | File | Field |
|---|---|---|
| main-run ranges: default 0.21–0.33 prose / 0.37–0.89 structured; 0.50: 0.52–0.72 / 0.51–1.00; 0.75: 0.82–0.92 / 0.71–1.00; 0.90: 0.89–0.98 / 0.72–1.00 | `records/*.jsonl` | recomputed for this package: ungated prose min 0.207 max 0.327; 0.50 prose 0.517–0.724; 0.75 prose 0.824–0.916; 0.90 prose 0.889–0.976; structured mins 0.367 / 0.513 / 0.711 / 0.724, maxima 0.889 / 1.000 / 1.000 / 1.000 |
| follow-up min / median / max: 0.10 prose 0.207 / 0.254 / 0.327, structured 0.367 / 0.481 / 0.889; 0.25 prose 0.273 / 0.299 / 0.399, structured 0.430 / 0.519 / 0.889 | `lowerarm/records/*.jsonl` | same fields, exposed on all 32 observations in each gated arm (`speculative_counters.exposed`) |
| the maintainer's stated tradeoff | no file here | PR #23269 comment, cited on the page with its date |

## Section 07: the ladder and the follow-up

| Figure | File | Field |
|---|---|---|
| clause 1: gate 0.50 vs none, prose +18.58% [+12.55, +26.45] | `analysis/analysis.md` | PROSE table |
| clause 2: 0.75 vs 0.50, prose +2.17% [−1.31, +5.58] | `analysis_vs_gate_0.50/analysis.md` | PROSE table, `gate_0.75` row |
| 0.90 vs 0.75, prose +0.51% [−2.40, +3.03] | `analysis_vs_gate_0.75/analysis.md` | PROSE table, `gate_0.90` row |
| structured adjacent contrasts +4.64% [−3.42, +12.25] and +6.19% [−2.27, +8.65] | `analysis_vs_gate_0.50/analysis.md`, `analysis_vs_gate_0.75/analysis.md` | STRUCTURED tables |
| follow-up prose: 0.10 → 7.56 t/s, −32.04% [−38.58, −27.37]; 0.25 → 8.47, −23.73% [−27.92, −20.09]; baseline median 11.04 | `lowerarm/analysis/analysis.md` | PROSE table |
| follow-up structured: 0.10 → 11.63, +1.22% [−9.84, +24.71]; 0.25 → 12.41, +5.61% [−4.43, +25.03]; baseline median 11.40 | `lowerarm/analysis/analysis.md` | STRUCTURED table |
| 0.25 against 0.10 on prose: +13.67% [+7.74, +21.40] | `lowerarm/analysis_vs_gate_0.10/analysis.md` | PROSE table, `gate_0.25` row |
| the follow-up baseline decoded roughly 5–10% faster than the main run's | `analysis/analysis.md` vs `lowerarm/analysis/analysis.md` | baseline medians 10.20 / 10.25 (main) against 11.04 / 11.40 (follow-up); the run-log characterization is the follow-up findings memo's, and the per-session observed band ~9.8–10.7 t/s is in `RUN_LOG.md` row 1 |
| run identity of the follow-up (times, six loads, witnesses) | `lowerarm/RUN_LOG.md` | preflight, invocations, row table, final state |

## Section 08: output equivalence

| Figure | File | Field |
|---|---|---|
| prose 0/16 byte-identical, all four main-run speculative treatments; structured 10 / 10 / 14 / 14 of 16 | `analysis/analysis.md` | Output-equivalence table |
| the restart control: two baseline sessions 16/16 byte-identical | `records/none_cycle1_4574baed.jsonl`, `records/none_cycle2_8ac19fed.jsonl` | `output.sha256` per prompt, equal on all 16; sessions about 85 minutes apart per `observed_utc` |
| truncation census, main run: 12 of 160, named prompts per treatment | `analysis/analysis.md` (Data-quality table, finish=length: none 4, ungated 4, 0.50 2, 0.90 2, 0.75 0), `analysis/measurements.csv` | `finish_reason` per observation names the prompts (baseline `prose_05`+`prose_07` both cycles; ungated `prose_01`+`prose_07` both cycles; 0.50 `prose_03`+`prose_07` cycle 2; 0.90 `prose_03` both cycles) |
| pairs with a truncated member: 6 / 5 / 4 / 6 of 16; both-complete pairs 10 / 11 / 12 / 10, every one still differing | arithmetic on the two rows above | a pair is truncated if either member finished `length` |
| all 160 structured outputs passed the strict validator, zero fenced | `analysis/analysis.md` | Structured-validator table, 16/16 every treatment |
| no truncated row shows the empty-answer signature; healthy prose band 4.68–6.05 chars/token | `RUN_LOG.md` | row-1 shakedown block (prose_05 4.84, prose_07 5.17 chars/token, 0 hidden events); `hidden_delta_events` is 0 on every record |
| follow-up: prose 0/16 at both low gates; its own baseline control 16/16 | `lowerarm/analysis/analysis.md` (equivalence table); `lowerarm/records/none_cycle1_49265197.jsonl` vs `none_cycle2_68bc387f.jsonl` | `output.sha256` equal on all 16 |
| follow-up truncation: 9 of 96, all prose; gated arms truncate `prose_01`, baseline truncates `prose_05`/`prose_07` | `lowerarm/analysis/analysis.md` (finish=length 4 / 1 / 4), `lowerarm/RUN_LOG.md` row table | per-row length lists with prompt names |
| gate 0.25 reproduced its own prose across two fresh processes on 1 of 8 prompts; 0.10, baseline, and every structured cell 8/8 | `lowerarm/records/gate_0.25_cycle1_f6da0450.jsonl` vs `gate_0.25_cycle2_a4f212d0.jsonl` (and the 0.10 and none pairs) | `output.sha256` per prompt: 9/16 equal, prose 1/8, structured 8/8 |

## Section 09: provenance of 0.75

No measurement of ours. The commit hashes, dates, PR bodies and the in-tree
residue are external record, verified against a local clone of llama.cpp and
the GitHub API on the dates the page states; the Unsloth negative result
(zero `p_min` occurrences in three MTP GGUF READMEs and the MTP documentation
page) is dated 2026-08-11 on the page. None of that is reproduced here.

## Section 10: the public record

| Figure | File | Field |
|---|---|---|
| the pastebin sweep: 0.5 best across 2k/15k/64k at 6 drafts, 119/122/118 t/s vs a 106–126 range; model `Qwen3.6-27B-MTP-Q6_K`; draft max 10 | `third-party/pastebin_P57Uk6rz_fetched-2026-08-10.txt` | the inline comment on the `--spec-draft-p-min` line, and the surrounding config |
| the RTX 5090 / build `86b9470` attribution to a secondary newsletter | no file here | smol.ai 2026-07-02, named on the page as secondary |
| neoteric.no, juejin, koboldcpp #2271, cmp-nct on PR #23269, llama.cpp #25908 | no files here | external citations with dates and identifiers on the page |

## Section 13: dates

| Figure | File | Field |
|---|---|---|
| main run 18:16–19:43 EDT, ten loads, zero failures, GPU released clean | `RUN_LOG.md` (row table, final state), `release_log.jsonl` | per-stop VRAM (to 721–752 MiB), port clear |
| follow-up 00:09–01:05 EDT, six loads, released clean | `lowerarm/RUN_LOG.md`, `lowerarm/release_log.jsonl` | same fields |
| the 2026-08-11 recompute reproducing every figure | the `analysis*/` folders **are** the recorded analysis outputs the page reads from | the recompute-agreement statements are the RUN_LOG final-state and findings-memo record; every figure they confirm is checkable directly against the files above |

## Section 11: limitations with numbers in them

| Figure | File | Field |
|---|---|---|
| calibration drift, largest +9.98% (ungated cycle 2); baseline +6.35% cycle 1 | `analysis/analysis.md` | Calibration-drift table |
| follow-up drift −2.70% to +6.23% | `lowerarm/analysis/analysis.md` | Calibration-drift table |
| permitted adjacent gains ~5.6% and ~3.0% | `analysis_vs_gate_0.50/analysis.md`, `analysis_vs_gate_0.75/analysis.md` | upper CI bounds +5.58% and +3.03% |
| 12 of 160 observations at the cap | `analysis/analysis.md` | Data-quality table, finish=length column |

*Graphometer · measured 2026-08-10 and 2026-08-11 · figures cross-checked
against the packaged files at assembly, 2026-08-11 · English is the canonical
record.*
