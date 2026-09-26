# Number map

The most apparent contradiction is the installed Q5 file's size: `hf_expected.txt` names another, larger file, while `records/file-identities.txt` and the installed hash identify the file actually served. Do not substitute the larger file into a memory row.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

Unless marked arithmetic or script-recorded, figures are measured on September 26, 2026. The page's speed tables use the per-row measurements, never a summary. 256K and 128K are shorthand for the served windows, not input lengths. Model names, dates, section numbers, build/revision identifiers and CLI constants are identifiers or setup, not benchmark estimates.

## Scope, setup and non-speed figures

| Page figure / claim | File and field or derivation | Label |
|---|---|---|
| Date 2026-09-26; one request at a time | `results/*.result`: `[run]` date and command `--parallel 1` | measured setup |
| One RTX 5090 | Hardware identity supplied in the task's measurement scope; primary files lack independent GPU inventory | scope; not a new hardware audit |
| 32,607 MiB capacity | `records/card-capacity.txt`: same-card total, extracted from the second `used,total` value in the source | measured, same card witness |
| 262,144 / 131,072 served tokens | `results/*.result`: `served: n_ctx_slot`; corresponding `logs/*.server.log`: initializing line | measured |
| Build c8e03ce, 2026-08-05, CUDA sm_120 | `records/file-identities.txt`: runtime comment | script-recorded |
| Scoring executable b10453 | `records/scoring-build.txt`, derived label from scoring script executable path | recorded identifier; no binary hash |
| b=2048, ub=512, GPU layers=999, threads=24, batch threads=24, flash attention on, Jinja, top-p=.95, top-k=20, min-p=0, server temp=1.0 | `results/*.result`: actual cmdline | measured setup |
| MTP n-max=6, p-min=.75, q8_0 target/draft cache at 256K; no MTP on installed Q5 at 256K | `results/*.result`: cmdline; `records/launch-excerpt.txt` | measured setup |
| 128K default cache (no cache-type override in the recorded command), described as f16 in the launch comment; MTP enabled | `records/baseline-invocations.txt`: f16 comment and command; `results/q38_q5xl_128k_mtp.result`: no cache override, MTP flags | script-recorded defaults and measured launch |
| Prose temp .7, seed 7, cap 900; structured temp 0, seed 7, cap 1600; recall temp 0, seed 1, cap 300; thinking off | `scripts/probe38.py`: argument defaults and `chat()` calls; `records/baseline-invocations.txt`, `records/candidate-invocations.txt`: no temperature override, `--think-off` | recorded procedure |
| Output lengths 414 to 504 real prose; 907 to 1,192 tool-shaped | min/max `predicted_n` across `kind=prose` / `struct` in `results/*.jsonl` | arithmetic from measured |
| One run per configuration / one observation per depth and type | `results/*.jsonl`: row census, four configuration files | measured scope |
| Installed Q5_K_XL: fe1e2a23, August 14, 20,218,178,624 bytes (20.2 GB (bytes/10^9); 18.83 GiB) | `records/file-identities.txt`; `logs/installed_q5xl.sha256`; GB = bytes / 10^9 rounded to 1 decimal; GiB = bytes / 2^30 rounded to 2 decimals | recorded identity; arithmetic GB and GiB |
| Q5_K_S: 4ca72078, 18,665,753,504 bytes (18.7 GB (bytes/10^9); 17.38 GiB) | `records/file-identities.txt`; `logs/hf_expected.txt`; `records/file-verification.txt` and `records/candidate-invocations.txt` | recorded/verified file; arithmetic GB and GiB |
| Q4_K_XL: 4ca72078, 17,559,178,144 bytes (17.6 GB (bytes/10^9); 16.35 GiB) | same records as Q5_K_S | recorded/verified file; arithmetic GB and GiB |
| Untested larger Q5_K_XL: 20,876,938,144 bytes | `logs/hf_expected.txt` row for Q5_K_XL; no serving result for that hash | recorded expected size |
| Q8_0 reference: 4ca72078, 29,047,086,048 bytes | `records/kld-invocations.txt`, `logs/hf_expected.txt`, `logs/q8_0_reference.sha256` | recorded/verified identity |
| 40/40, zero crashes and empty answers, each of installed Q5 no MTP and Q4 MTP | two `logs/stress_*/SUMMARY.json`: `prompts`, `crashes`, `empty_answers`; `results.jsonl`: 40 rows all `ok=true`, `empty=false` | measured |
| Two turns per crash-check prompt; shorter inputs, no full-window stress claim | `records/stress-method.txt`: `turn` calls and input selection; per-prompt records | recorded procedure and measured rows |
| Three codes at approx 5 / 50 / 95% of ledger entries | `scripts/probe38.py`: `ledger`, `int(n * frac)`; all-code question | procedure, not exact tokenizer offsets |
| Failure 1: 1,024.00 MiB / 1,073,741,824 bytes, f16 draft KV allocation, ub=256 | `logs/q38_q5_256k_mtp_ub256_fit.server.log`: allocation and KV failure; matching `.result` configuration | measured failure |
| Failure 2: 1,192.27 MiB / 1,250,189,440 bytes, q8_0 draft compute allocation, ub=256 | `logs/q38_q5_256k_mtp_dkvq8_ub256_fit.server.log`: allocation and compute failure; matching `.result` configuration | measured failure |
| Perplexity: 24 chunks × 4,096; KLD: 12 × 4,096 | `logs/ppl_*.log` and `logs/kld_*.log`: calculating/computing lines; `records/*invocations.txt` | measured procedure |
| Corpus 414,554 bytes and hash | `records/corpus-identity.txt`: byte count and SHA-256 of original public text | arithmetic identity |
| Q4 same next token about 97/100; installed Q5 about 98/100; reference described as 8-bit | same-top-token percentages rounded to whole percent; Q8_0 reference identifier | arithmetic paraphrase |

## Every speed-table cell

Approximate depth headings 20K / 48K / 100K / 230K use `depth_target` 20000 / 48000 / 100000 / 230000. The following rows name the raw field and page rounding. `read` is cold prompt processing; its short-answer decode rate is not printed on the page.

| File | Kind | Depth target | Field | Raw → page tokens/s |
|---|---|---:|---|---:|
| `results/q38_q4kxl_256k_mtp.jsonl` | read | 20000 | `prefill_tps` | 3087.6 → 3,088 |
| `results/q38_q4kxl_256k_mtp.jsonl` | prose | 20000 | `decode_tps` | 75.2 → 75.2 |
| `results/q38_q4kxl_256k_mtp.jsonl` | struct | 20000 | `decode_tps` | 144.68 → 144.7 |
| `results/q38_q4kxl_256k_mtp.jsonl` | read | 48000 | `prefill_tps` | 2721.7 → 2,722 |
| `results/q38_q4kxl_256k_mtp.jsonl` | prose | 48000 | `decode_tps` | 64.78 → 64.8 |
| `results/q38_q4kxl_256k_mtp.jsonl` | struct | 48000 | `decode_tps` | 129.91 → 129.9 |
| `results/q38_q4kxl_256k_mtp.jsonl` | read | 100000 | `prefill_tps` | 1937.1 → 1,937 |
| `results/q38_q4kxl_256k_mtp.jsonl` | prose | 100000 | `decode_tps` | 54.93 → 54.9 |
| `results/q38_q4kxl_256k_mtp.jsonl` | struct | 100000 | `decode_tps` | 114.68 → 114.7 |
| `results/q38_q4kxl_256k_mtp.jsonl` | read | 230000 | `prefill_tps` | 1132.3 → 1,132 |
| `results/q38_q4kxl_256k_mtp.jsonl` | prose | 230000 | `decode_tps` | 38.42 → 38.4 |
| `results/q38_q4kxl_256k_mtp.jsonl` | struct | 230000 | `decode_tps` | 87.01 → 87.0 |
| `results/q38_q5ks_256k_mtp.jsonl` | read | 20000 | `prefill_tps` | 3001.2 → 3,001 |
| `results/q38_q5ks_256k_mtp.jsonl` | prose | 20000 | `decode_tps` | 71.49 → 71.5 |
| `results/q38_q5ks_256k_mtp.jsonl` | struct | 20000 | `decode_tps` | 137.39 → 137.4 |
| `results/q38_q5ks_256k_mtp.jsonl` | read | 48000 | `prefill_tps` | 2666.7 → 2,667 |
| `results/q38_q5ks_256k_mtp.jsonl` | prose | 48000 | `decode_tps` | 64.5 → 64.5 |
| `results/q38_q5ks_256k_mtp.jsonl` | struct | 48000 | `decode_tps` | 125.99 → 126.0 |
| `results/q38_q5ks_256k_mtp.jsonl` | read | 100000 | `prefill_tps` | 1904.9 → 1,905 |
| `results/q38_q5ks_256k_mtp.jsonl` | prose | 100000 | `decode_tps` | 52.21 → 52.2 |
| `results/q38_q5ks_256k_mtp.jsonl` | struct | 100000 | `decode_tps` | 110.21 → 110.2 |
| `results/q38_q5ks_256k_mtp.jsonl` | read | 230000 | `prefill_tps` | 1124.2 → 1,124 |
| `results/q38_q5ks_256k_mtp.jsonl` | prose | 230000 | `decode_tps` | 39.91 → 39.9 |
| `results/q38_q5ks_256k_mtp.jsonl` | struct | 230000 | `decode_tps` | 82.76 → 82.8 |
| `results/q38_q5xl_128k_mtp.jsonl` | read | 20000 | `prefill_tps` | 2895.5 → 2,896 |
| `results/q38_q5xl_128k_mtp.jsonl` | prose | 20000 | `decode_tps` | 72.0 → 72.0 |
| `results/q38_q5xl_128k_mtp.jsonl` | struct | 20000 | `decode_tps` | 141.5 → 141.5 |
| `results/q38_q5xl_128k_mtp.jsonl` | read | 48000 | `prefill_tps` | 2607.7 → 2,608 |
| `results/q38_q5xl_128k_mtp.jsonl` | prose | 48000 | `decode_tps` | 70.46 → 70.5 |
| `results/q38_q5xl_128k_mtp.jsonl` | struct | 48000 | `decode_tps` | 136.91 → 136.9 |
| `results/q38_q5xl_128k_mtp.jsonl` | read | 100000 | `prefill_tps` | 1972.6 → 1,973 |
| `results/q38_q5xl_128k_mtp.jsonl` | prose | 100000 | `decode_tps` | 60.77 → 60.8 |
| `results/q38_q5xl_128k_mtp.jsonl` | struct | 100000 | `decode_tps` | 127.01 → 127.0 |
| `results/q38_q5xl_256k_nomtp.jsonl` | read | 20000 | `prefill_tps` | 3118.2 → 3,118 |
| `results/q38_q5xl_256k_nomtp.jsonl` | prose | 20000 | `decode_tps` | 60.7 → 60.7 |
| `results/q38_q5xl_256k_nomtp.jsonl` | struct | 20000 | `decode_tps` | 60.68 → 60.7 |
| `results/q38_q5xl_256k_nomtp.jsonl` | read | 48000 | `prefill_tps` | 2717.6 → 2,718 |
| `results/q38_q5xl_256k_nomtp.jsonl` | prose | 48000 | `decode_tps` | 55.18 → 55.2 |
| `results/q38_q5xl_256k_nomtp.jsonl` | struct | 48000 | `decode_tps` | 54.88 → 54.9 |
| `results/q38_q5xl_256k_nomtp.jsonl` | read | 100000 | `prefill_tps` | 1958.2 → 1,958 |
| `results/q38_q5xl_256k_nomtp.jsonl` | prose | 100000 | `decode_tps` | 49.08 → 49.1 |
| `results/q38_q5xl_256k_nomtp.jsonl` | struct | 100000 | `decode_tps` | 48.88 → 48.9 |
| `results/q38_q5xl_256k_nomtp.jsonl` | read | 230000 | `prefill_tps` | 1180.7 → 1,181 |
| `results/q38_q5xl_256k_nomtp.jsonl` | prose | 230000 | `decode_tps` | 34.89 → 34.9 |
| `results/q38_q5xl_256k_nomtp.jsonl` | struct | 230000 | `decode_tps` | 34.84 → 34.8 |

## Card use and recall

| File | Field | Raw / derivation | Page |
|---|---|---|---|
| `results/q38_q4kxl_256k_mtp.result`; `logs/q38_q4kxl_256k_mtp.vram` | peak; maximum sample | 30722; spare = 32607 − 30722 | 30,722 MiB; 1,885 MiB spare |
| `results/q38_q4kxl_256k_mtp.jsonl` | `read` at 230000: `prompt_n`, `prompt_ms`, `wall_s`, `codes3_hits` | 229152; 202377 / 1000; 205.2; 3 | 229,152 tokens; 202.377 s; 205.2 s; 3/3 |
| `results/q38_q5ks_256k_mtp.result`; `logs/q38_q5ks_256k_mtp.vram` | peak; maximum sample | 31943; spare = 32607 − 31943 | 31,943 MiB; 664 MiB spare |
| `results/q38_q5ks_256k_mtp.jsonl` | `read` at 230000: `prompt_n`, `prompt_ms`, `wall_s`, `codes3_hits` | 229152; 203831 / 1000; 206.6; 3 | 229,152 tokens; 203.831 s; 206.6 s; 3/3 |
| `results/q38_q5xl_128k_mtp.result`; `logs/q38_q5xl_128k_mtp.vram` | peak; maximum sample | 30458; spare = 32607 − 30458 | 30,458 MiB; 2,149 MiB spare |
| `results/q38_q5xl_256k_nomtp.result`; `logs/q38_q5xl_256k_nomtp.vram` | peak; maximum sample | 30254; spare = 32607 − 30254 | 30,254 MiB; 2,353 MiB spare |
| `results/q38_q5xl_256k_nomtp.jsonl` | `read` at 230000: `prompt_n`, `prompt_ms`, `wall_s`, `codes3_hits` | 229152; 194086 / 1000; 196.9; 3 | 229,152 tokens; 194.086 s; 196.9 s; 3/3 |

## Fidelity table cells

| File | Field | Printed value |
|---|---|---|
| `logs/ppl_q4kxl_new.log` | `Final estimate` | 2.7206 +/- 0.02379 |
| `logs/ppl_q5ks_new.log` | `Final estimate` | 2.7186 +/- 0.02375 |
| `logs/ppl_q5xl_installed.log` | `Final estimate` | 2.7203 +/- 0.02379 |
| `logs/kld_q4kxl_new.log` | `Mean KLD`; `Same top p` | 0.007839 ±   0.000345; 97.240 ± 0.105% |
| `logs/kld_q5ks_new.log` | `Mean KLD`; `Same top p` | 0.005406 ±   0.000201; 97.675 ± 0.096% |
| `logs/kld_q5xl_installed.log` | `Mean KLD`; `Same top p` | 0.004369 ±   0.000153; 97.830 ± 0.093% |
