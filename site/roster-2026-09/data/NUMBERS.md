# Every figure on the page, and the file and field it came from

Revised 2026-09-26 for the snapshot "The roster, as of 26 September 2026", and again in the fix pass that day. The 15 September version of this file
mapped the first list; its mappings for the figures this page still prints are carried below, and
`ROSTER_22.csv` keeps the first list as it was.

**If a number on the page disagrees with a file in this package, the file is right and the page is wrong.**

Model names here are the public names the page uses; file names in this package use the same names. Folder names
below are relative to this `data/` folder. "Result" means a run's `.result` file, whose lines hold the harness's own
JSON (`prompt_n`, `prefill_tps`, `decode_tps`); "log" means the server's own log, whose `print_timing` lines hold the
server's count of tokens read and generated. Where both exist they agree; the answer lengths quoted on the page
("an 11-token answer") are the log's `eval time = ... / N tokens`.

## Where a file will look like it contradicts the page

1. **Qwen3-235B's 8.18 in `batch-sweep-2026-09-21/Qwen3-235B-A22B-Instruct-2507_2048.result`** is a speaking rate on
   an 11-token answer (the log's `eval time ... / 11 tokens`). The page prints the letters of 26 September instead
   (5.51, 4.68, 4.22) and says why in section 05. Both files are here.
2. **MiniMax M2.7's 9.80 in `minimax-m2.7/2026-09-13_ctx65536_f16.server.log`** (task 261, 900 tokens) is a reply
   made entirely of hidden reasoning, cut off at the length limit before any answer (`finish=length`,
   `content_chars=0` in `minimax-m2.7/2026-09-13_extract.txt`, section 3). The page prints the same request's
   finished reply from the 131,072-window run: 9.73 over 1,522 tokens.
3. **Inkling-Small's 337.9 and Qwen3.8-Flash-Next's 511.7** were read at a 131,072 window (the `ctx=131072` in each
   result's `[load]` line); both models serve 262,144. The page prints them as 131,072 figures and leads each row with
   what exists at the served window: the deep reads at the old batch setting, and 3,000-token reads at the new one.
4. **MiniMax M3's 194**, which our records carried, is not in any file as a rate. It is 58,307 tokens divided by
   the 300.2-second wall time of the whole request (`minimax-m3/2026-09-20_q2kl_needle_58k.json`, `wall_s`,
   `prompt_tokens`). The server's own reading figure for the same request is 208.11 (the server log, task 216).
5. **The Qwen3.8-Flash-Next records hold a failed question the page never mentions.** Each
   `qwen3.8-flash-next-2026-09-20/*.result` ends with `[q3 INTEGRATE] letter=N tally=N task=N`: a question that needs
   facts combined from across the ledger, answered wrongly at every length including the 5,986-token control. The
   page prints only the reading and speaking rates and the three-code retrieval (`[q1 RETRIEVE] 3/3`), and makes no
   claim about reasoning across a window.
6. **Short reads right after a start.** Every 3,000-token read in the batch-size folders was the first completion
   request after the server started (the drivers `bsweep.sh` and `series_probe.sh` send nothing before it). The page
   says so where it prints one as the only figure at a window.
7. **The framework's `t1` speaking column** in `tool-recall-wave1-2026-09-12.tsv` is still not printed, for the
   reason the 15 September version gave: it is a short first turn whose token count leaves out a thinking model's
   reasoning.

## Section 01, the machine and what changed

| page says | file | field |
|---|---|---|
| RTX 5090, 32,607 MiB | `context-sweep-2026-09-12.tsv` | header line 1 |
| Intel Core Ultra 9 285K, 188 GiB of RAM | `install-runs-qwen3.8-flash-next-2026-09-12.tsv` for the RAM figure; the processor is the machine's own specification, stated on the site's method page | |
| Laptop, 128 GB unified memory, direct Thunderbolt cable | `two-box-deepseek-probes-2026-09-13-to-15.txt` | run headings |
| Every start script refuses while another model is up; seven guards each refused | `refusal-guards-2026-09-12.txt` | tests G1 to G7 |
| Twenty-three endpoints | `ROSTER_23.csv` | 23 rows |
| Ornith-1.5-35B-A3B and GLM-5.3-Flash installed on 16 September, MiniMax M2.7 on 21 September; Kimi K3 retired 15 September | our operator records, labelled on the page as such; not measurements. The first runs of the two 16 September models are in `first-runs-2026-09-16/` and M2.7's framework check of 21 September is `gate-records/minimax-m2.7-2026-09-21.json` | |
| Kimi K2.7-Code's weights removed on 17 September | `file-listing-2026-09-26.txt` | section B: 0 model files; the folder last changed 2026-09-17 11:46 |
| MiniMax M3 serves a different file since 21 September | `file-listing-2026-09-26.txt` section A row 19 (the Q2_K_L shards) and section C (its start script); the date is our operator record | |
| Laguna S 2.1 serves 262,144 since 21 September | `file-listing-2026-09-26.txt` section C (`CTX="${1:-262144}"`); `batch-sweep-2026-09-21/Laguna-S-2.1_ctx262144_4096_series.result`, `served: n_ctx_slot = 262144` | |
| Qwen3.6-27B serves a different file since 26 September; our records give it 262,144 from that day, and the runs here passed that window explicitly | `file-listing-2026-09-26.txt`, section A row 10 and section C (`case "${Q36_FILE:-mtp-q5}"`, the cache block dated by the script's own comment); the window itself is set in a settings file that is not published, so the date and the window are our operator record | |

## Section 02, method

| page says | file | field |
|---|---|---|
| 21 September: each model started through its own start script | `batch-sweep-2026-09-21/batch_sweep.sh`, `series_probe.sh`, `series_probe2.sh` | each drives the model's own start script |
| 19 and 20 September: the server started by hand with the same flags | `minimax-m2.7/2026-09-19_*.json`, `config` (micro-batch, placement, window, cache, build) with the probe `m27_probe.py`; the header line of each `minimax-m3/*launch-check.log`; `batch-sweep-2026-09-20/bsweep.sh`; the `[load]` lines in `batch-sweep-2026-09-20/*.result` | |
| temperature 0, a code planted halfway that the answer had to quote exactly | `batch_sweep.sh` (the request: `"temperature": 0.0`, `max_tokens` 900; the ledger with `SEALED REFERENCE` at `n//2`) | |
| llama.cpp's defaults are `-b 2048 -ub 512` | `batch_sweep.sh`, the result line `ubatch=skip (the script's own default)`, and the 20 September `bsweep.sh` header | |
| Paragraph replies: 150 words on 15 September, about 200 tokens on 12 September, better of two warm replies | `long-reads-2026-09-15/CONTEXT_256K_MEASUREMENTS.tsv` header (`decode_tps = best of 2 warm ~200-token replies`) and the request text inside `first-runs-2026-09-16/audition_rung.sh` ("In exactly one paragraph of about 150 words ..."); `context-sweep-2026-09-12.tsv` header (`best of 2 WARM reps on a ~200-token prose generation`) | |
| First runs: thinking switch off, a tool call, about 120,000 tokens with three codes, default batch settings | `first-runs-2026-09-16/first-runs-2026-09-16.tsv` (`tools`, `deep_prompt_tok`, `codes_hit`); the `[cmd]` line of each `first-runs-2026-09-16/*.log` carries no batch flag | |
| Letters: 20,000, 60,000 and 100,000 (Qwen3-235B) or 20,000, 100,000 and 230,000 (Qwen3.6-27B); letters of about 350 to 400 words | `letters-2026-09-26/*.jsonl`, `depth_target` and `answer_words` (366, 333, 331; 398, 430, 429); the request is `PROSE_Q` in `letters-2026-09-26/prose_probe.py` | |
| Long reads: 150,000 to 231,000 tokens, three codes, 262,144 (202,752 for GLM-4.7-Flash) | `long-reads-2026-09-15/CONTEXT_256K_MEASUREMENTS.tsv`, `n_ctx`, `deep_prompt_tok` (150,475 to 231,065 at 262,144 and 189,931 at 202,752; the table's one row at 131,072 is not used on this page), `codes_hit` | |
| Framework: 48,000 and 96,000 seeded tokens, three codes, a tool call; the true size printed; short answers of 30 to 1,004 tokens; reading is the harness's estimate | `gate-records/*.json`: `l64` and `l128`, `seed_tokens_est`, `A_recall.prompt_tokens`, `A_recall.completion_tokens` (30 to 1,004), `A_recall.prefill_tps_approx` | |
| Gemma-4-26B: 8,972.3 direct at 47,983 against about 6,726.8 through the framework at 53,209 | `batch-sweep-2026-09-21/Gemma-4-26B-A4B_skip.result`; `gate-records/gemma-4-26b-a4b.json`, `l64.A_recall` | |
| Qwen3-235B: 9.3 on a 62-token framework answer at 53,458; 5.51 on a 478-token letter at 20,063 | `gate-records/qwen3-235b-a22b-2507.json`, `l64.A_recall`; `letters-2026-09-26/Qwen3-235B_2048.jsonl`, the first `prose` line | |

## Section 03, the twenty-three rows

Byte counts and shard counts for every row are in `file-listing-2026-09-26.txt`, section A (read 2026-09-26).
Every framework figure is the `l64.A_recall` (48K leg) or `l128.A_recall` (96K leg) block of the model's file in
`gate-records/`: `prompt_tokens`, `prefill_tps_approx`, `decode_tps`, `completion_tokens` and `hits`; the dates are
each record's `started_utc` in local time (UTC minus four hours).

| row | figure on the page | file and field |
|---|---|---|
| 1 | window: 131,072 by the script's fallback; 262,144 loaded on 15 and 21 September | `file-listing-2026-09-26.txt` section C (the split script's `CTX` line); `installed-windows-2026-09-21.txt` section C; the 21 September runs passed 262144 (`batch-sweep-2026-09-21/DeepSeek-V4-Flash-pair_chain.sh`, `SCRIPT_ARGS`), served `n_ctx_slot = 262144` in `DeepSeek-V4-Flash-pair_512_series.result`; the 15 September long-read run passed `--ctx-size 262144` (`long-reads-2026-09-15/CONTEXT_256K_MEASUREMENTS.tsv`, METHOD line and the `DeepSeek-V4-Flash-pair_262144` row); the 14 September framework records show 131,072 served and carry no launch arguments (`gate-records/deepseek-v4-flash-0731-two-machines.json` and `-attempt3.json`, `S.n_ctx`) |
| 1 | 14.73, 12.05, 7.85 on replies of about 400 tokens | same file, `warm_decode_tps` and `warm_gen_n` (400, 394) at 2,998 and 48,024; `..._512_150k.result`, 7.85 on 380 |
| 1 | 161.8 on 2,998, 102.5 on 48,024, 51.4 on 150,103 | the same two results, `prompt_n`, `prefill_tps`; the setting is the header's `ubatch=512 batch=2048` |
| 1 | framework, 2026-09-14 | `gate-records/deepseek-v4-flash-0731-two-machines.json` |
| 1 and 3 | 6.7 and 12.3 times | arithmetic: 690.9 / 102.5 and 632.1 / 51.4 |
| 1 | 19.55 speaking with the 4-bit preset on the pair | `two-box-deepseek-probes-2026-09-13-to-15.txt`, the 2026-09-15 block, `decode 19.55` |
| 2 | 11.77 on a 202-token paragraph | `long-reads-2026-09-15/CONTEXT_256K_MEASUREMENTS.tsv` `decode_tps` 11.772 (best of two); the token count is `timings.predicted_n` of the faster of `Inkling-Small_ctx262144.short.r1.json` and `.r2.json` |
| 2 | 8.78 on 27 tokens and 115.07 on 230,827 | `long-reads-2026-09-15/Inkling-Small_ctx262144.deep.json`, `timings` |
| 2 | 263.6 on 3,033 (2026-09-20) | `batch-sweep-2026-09-20/Inkling-Small_2048_ctx262144_3k.result`; its `[load]` line has `ctx=262144` and `--batch-size 4096 --ubatch-size 2048` |
| 2 | 187.9 on 3,033 (2026-09-21) | `batch-sweep-2026-09-21/Inkling-Small_ctx262144_3k.result`, `served: n_ctx_slot = 262144`; the setting is the start script's default (`file-listing-2026-09-26.txt`, section C) |
| 2 | 337.9 on 48,115 at 131,072 | `batch-sweep-2026-09-20/Inkling-Small_2048.result`, `ctx=131072` in its `[load]` line |
| 2 | framework, 2026-09-14 | `gate-records/inkling-small.json` |
| 2 | the 14 September probes served 131,072; a run that passed no window was served 262,144 on 21 September | `inkling-probes-2026-09-14.md` (run 1, "128K window"), `gate-records/inkling-small.json` (`S.n_ctx` 131072); `installed-windows-2026-09-21.txt` section A |
| 3 | 8-bit: 9.93 on a 209-token reply | `CONTEXT_256K_MEASUREMENTS.tsv` row `DeepSeek-V4-Flash-8bit-desktop_262144`, `decode_tps`; tokens from the faster short reply JSON |
| 3 | 8-bit: 480.0 on 150,324 at 262,144; 9.37 on 106 tokens | `batch-sweep-2026-09-20/DeepSeek-V4-Flash-8bit-desktop_verify-150k.out`; the log `..._8192_150k_ctx262144.log` (`n_ctx_slot = 262144`, `eval time ... / 106 tokens`) |
| 3 | 8-bit: 607.1 on 48,073 at 131,072 | `..._verify-48k.out`, third line; `..._8192_48k.log`, `n_ctx_slot = 131072` |
| 3 | 3-bit: 12.65 on 59 tokens at 2,998; 690.9 on 48,024 | `batch-sweep-2026-09-21/DeepSeek-V4-Flash-3bit-desktop_4096_series.result` and its log (59 tokens) |
| 3 | 3-bit: 632.1 on 150,103; 11.79 on 86 tokens | `..._3bit-desktop_4096_150k.result` and its log |
| 3 | experts of 36 of 43 layers; the 8-bit file is the default preset | `file-listing-2026-09-26.txt`, section C (the `fast` preset's `PLACE=(--n-cpu-moe 36)`, the default `PRESET="${DS_PRESET:-quality}"`); `model-file-headers.md` (`n_layer = 43`) |
| 3 | framework, 2026-09-12 | `gate-records/deepseek-v4-flash-0731-one-machine.json`; `tool-recall-wave1-2026-09-12.tsv` |
| 4 | 16.41 on 11 tokens after 48,029; 932.2 | `batch-sweep-2026-09-21/Qwen3.5-397B-A17B_4096.result` and its log |
| 4 | 224.5 at the defaults | `Qwen3.5-397B-A17B_skip.result` |
| 4 | 12.84 on a 184-token paragraph at 262,144 | `CONTEXT_256K_MEASUREMENTS.tsv` row `Qwen3.5-397B-A17B_262144`; the short reply JSONs |
| 4 | framework, 96K leg, 2026-09-13 | `gate-records/qwen3.5-397b-a17b.json` |
| 5 | 5.51, 4.68, 4.22 on 478, 426, 426 tokens; 741.8, 652.0, 542.1 | `letters-2026-09-26/Qwen3-235B_2048.jsonl`, the `read` and `prose` lines (`prefill_tps`, `decode_tps`, `predicted_n`) |
| 5 | `-b 4096 -ub 2048` | the `cmdline:` line of `letters-2026-09-26/Qwen3-235B_2048.result` |
| 5 | 703.3 on 48,020 (2026-09-21) | `batch-sweep-2026-09-21/Qwen3-235B-A22B-Instruct-2507_2048.result` |
| 5 | with `-ub 4096`: 1,069.0 on 20,063; 5.82 on letters | `letters-2026-09-26/Qwen3-235B_4096.jsonl`; the `env:` lines of its `.result` |
| 5 | framework, 2026-09-12 | `gate-records/qwen3-235b-a22b-2507.json` |
| 6 | 32.72 on a 716-token answer after 48,027; 2,101.7 | `batch-sweep-2026-09-21/Qwen3.5-122B-A10B_4096.result` and its log; `reasoning_len` 2,212 characters shows the answer is mostly reasoning |
| 6 | 520.2 at the defaults | `Qwen3.5-122B-A10B_skip.result` |
| 6 | 22.39 on a 188-token paragraph at 262,144 | `CONTEXT_256K_MEASUREMENTS.tsv` and the short reply JSONs |
| 6 | framework, 48K leg, 2026-09-12 | `gate-records/qwen3.5-122b-a10b.json` |
| 7 | 86.01 on paragraph replies (2026-09-12) | `context-sweep-2026-09-12.tsv`, Qwen3.8-27B `long-128K`, `decode_tps` |
| 7 | 99.26 on 106 tokens; 2,634.8 on 48,069 at the defaults | `batch-sweep-2026-09-21/Qwen3.8-27B_skip.result` and its log |
| 7 | `-ub 4096` would not load: 1,568.13 MiB | `batch-sweep-2026-09-21/Qwen3.8-27B_4096.log` |
| 7 | framework, 2026-09-13 | `gate-records/qwen3.8-27b.json` |
| 8 | 89.72 on a 198-token paragraph, thinking off | `first-runs-2026-09-16/first-runs-2026-09-16.tsv` `decode_tps`; `Ornith-1.5-35B_ctx131072.short.json`, `timings.predicted_n` |
| 8 | 73.2 on 83 tokens; 6,283.3 on 48,027 | `batch-sweep-2026-09-21/Ornith-1.5-35B_4096.result` and its log |
| 8 | 1,649.22 on 120,334, 3 of 3 | `first-runs-2026-09-16/Ornith-1.5-35B_ctx131072.deep.json` (`timings`, the three codes in the answer); `first-runs-2026-09-16.tsv`, `codes_hit` |
| 9 | 9.58 on a 181-token paragraph | `first-runs-2026-09-16.tsv`; `GLM-5.3-Flash_ctx131072.short.json` |
| 9 | 9.12 on 310 tokens; 425.1 on 48,168 | `batch-sweep-2026-09-21/GLM-5.3-Flash_4096_series.result`, fourth read, and its log |
| 9 | 75.48 on 120,979, 3 of 3 | `GLM-5.3-Flash_ctx131072.deep.json`; `first-runs-2026-09-16.tsv` |
| 10 | 60.85, 46.66, 34.61 on 481, 527, 526 tokens; 3,162.8, 1,971.1, 1,165.6 at 20,067, 99,934, 229,564 | `letters-2026-09-26/Qwen3.6-27B_ctx262144_draft-off.jsonl`, `read` and `prose` lines |
| 10 | `-b 2048 -ub 512`, 262,144 | the `cmdline:` line of `Qwen3.6-27B_ctx262144_draft-off.result` |
| 10 | draft head on at 262,144: "failed to create MTP context" | `letters-2026-09-26/Qwen3.6-27B_ctx262144_draft-on.result` |
| 10 | the cache setting referenced but never defined before 26 September | `file-listing-2026-09-26.txt`, section C, both Qwen3.6-27B blocks |
| 10 | framework, the earlier file, 2026-09-13 | `gate-records/qwen3.6-27b.json` |
| 11 | 23.50 on 32 tokens after 5,986; 236.50 on 5,986 | `qwen3.8-flash-next-2026-09-20/q8cache_short_control.result`, `[q1 RETRIEVE]` line, and its log |
| 11 | 13.08 on 32 tokens and 197.14 on 229,982 | `q8cache_ctx262144_deep.result`, `[q1 RETRIEVE]`, and its log |
| 11 | both at the defaults, 8-bit cache, 262,144 | the `[load]` lines (`asked=262144 got=262144 ... kv=q8_0`); `run_hard.sh` passes no batch flag |
| 11 | 45.4 on 3,041 (2026-09-20) | `batch-sweep-2026-09-20/Qwen3.8-Flash-Next_2048_ctx262144_3k.result`, `ctx=262144`, `--batch-size 4096 --ubatch-size 2048` |
| 11 | 112.3 on 2,999 (2026-09-21) | `batch-sweep-2026-09-21/Qwen3.8-Flash-Next_ctx262144_3k.result`, `served: n_ctx_slot = 262144`; the setting is the start script's default (`file-listing-2026-09-26.txt`, section C) |
| 11 | 511.7 on 48,069 at 131,072 | `batch-sweep-2026-09-20/Qwen3.8-Flash-Next_2048.result`, `ctx=131072` |
| 11 | 393,216 and 524,288 on request, same setting in the script; the reads at those windows at the defaults, before the change | `file-listing-2026-09-26.txt`, section C (the accepted windows, line 84; the batch line 235 has no window condition); `q8cache_ctx393216_deep.result` and `q8cache_ctx524288_deep.result` (344,981 and 459,911 tokens, 3/3; `run_hard.sh` passes no batch flag) |
| 11 | framework, 96K leg, 2026-09-12 | `gate-records/qwen3.8-flash-next-125b.json` |
| 12 | 227.43 on a 160-token paragraph at 202,752 | `CONTEXT_256K_MEASUREMENTS.tsv` row `GLM-4.7-Flash_202752`; the short reply JSONs |
| 12 | 129.6 on 429 tokens; 2,594.6 on 47,986 | `batch-sweep-2026-09-21/GLM-4.7-Flash_skip.result` (`reasoning_len` 1,388) and its log |
| 12 | framework, 96K leg, 2026-09-12 | `gate-records/glm-4.7-flash-31b.json` |
| 13 | 5.51 and 61.36 on 20,221 (2026-09-12) | `context-sweep-2026-09-12.tsv`, GLM-4.7 Full `long-128K` |
| 13 | the check failed at the 96K tool call | `gate-records/glm-4.7-full-358b.json`, `verdict` FAIL, `fails` |
| 14 | 202.64 on a 163-token paragraph; 3,799.69 on 230,855 | `CONTEXT_256K_MEASUREMENTS.tsv` row `Gemma-4-26B-A4B_262144`; the short and deep JSONs |
| 14 | 163.68 on 11 tokens; 8,972.3 on 47,983 | `batch-sweep-2026-09-21/Gemma-4-26B-A4B_skip.result` and its log |
| 14 | framework, 2026-09-12 | `gate-records/gemma-4-26b-a4b.json` |
| 15 | 73.68 on paragraph replies (2026-09-12) | `context-sweep-2026-09-12.tsv`, Gemma-4-31B IT QAT `long-128K` |
| 15 | 56.45 on 11 tokens; 2,687.5 on 47,983 | `batch-sweep-2026-09-21/gemma-4-31b-it-qat_skip.result` and its log |
| 15 | framework, 2026-09-12 | `gate-records/gemma-4-31b-it-qat.json` |
| 16 | 29.57 on a 172-token paragraph | `CONTEXT_256K_MEASUREMENTS.tsv` row `Ling-3.0-flash_262144`; the short reply JSONs |
| 16 | 23.25 on 77 tokens and 727.7 on 47,986; 22.6 on 135 and 694.6 on 149,711 | `batch-sweep-2026-09-21/Ling-3.0-flash_2048_series.result`, reads 2 and 3, and its log |
| 16 | framework, 2026-09-13 | `gate-records/ling-3.0-flash.json` |
| 17 | 29.55 on a 249-token paragraph (29.548) | `CONTEXT_256K_MEASUREMENTS.tsv` row `Mistral-Small-4_262144`; the short reply JSONs |
| 17 | 20.97 on 11 tokens; 2,192.3 on 48,697 at 8192; 481.3 at the defaults | `batch-sweep-2026-09-21/Mistral-Small-4_8192.result` and log; `Mistral-Small-4_skip.result` |
| 17 | framework, 2026-09-12 | `gate-records/mistral-small-4-119b.json` |
| 18 | 9.73 on a prose reply of 1,313 characters, 1,522 tokens, after a 70-token prompt | `minimax-m2.7/2026-09-13_ctx131072_q8_0.server.log`, task 261 (`70 tokens`, `1522 tokens`, `9.73 tokens per second`); `2026-09-13_extract.txt` section 3 (`content_chars=1313`, `finish=stop`) and section 1 (`-cmoe`, every expert in system memory) |
| 18 | 9.83 on 32 tokens after 43,909; 656.5 | `minimax-m2.7/2026-09-19_one_ub4096_59_ctx131072.json`, `sizes.49152.cold` (`prompt_n`, `prefill_tps` 656.48, `decode_tps` 9.834, `predicted_n`) |
| 18 | experts of 59 of 62 layers | the same JSON, `config.place` "59"; the layer count in `2026-09-13_extract.txt` section 4 (`n_layer = 62`) |
| 18 | 196,608 on request | `file-listing-2026-09-26.txt`, section C; `minimax-m2.7/2026-09-19_one_ub1024_cmoe_ctx196608.json` (`config.ctx` 196608, 3,658 tokens at 188.77) |
| 18 | row note: 45.6 on 6,776 at `-ub 128` (13 September) | `minimax-m2.7/2026-09-13_ctx65536_f16.server.log`, task 129 (`6776 tokens`, `45.58`); the flag in `2026-09-13_extract.txt` section 1 |
| 18 | row note: 100.8 on 3,658 at the default | `minimax-m2.7/2026-09-19_A_ub512_cmoe.json`, `sizes.4096.cold` |
| 18 | row note: with a 900-token limit the request returned no answer | `2026-09-13_extract.txt` section 3 (`finish=length`, `completion_tokens=900`, `content_chars=0`) |
| 18 | row note: `-ub 128` "copied from another model's launcher" | our session notes; stated, not a measurement |
| 18 | framework, 2026-09-21, 3 of 3 and the tool call, PASS | `gate-records/minimax-m2.7-2026-09-21.json`, `l64`, `l128`, `verdict`, `fails` |
| 19 | 8.90 on 82 tokens at 3,680 | `minimax-m3/2026-09-20_q2kl_ctx131072_ub2048.server.log`, task 4 |
| 19 | 208.11 on 58,307; 8.29 on 165 tokens; 3 of 3 | the same log, task 216; `2026-09-20_q2kl_needle_58k.json`, `score` |
| 19 | 186.8 on 3,009 through the model manager (2026-09-21) | `batch-sweep-2026-09-21/MiniMax-M3_model-manager_3k.result` |
| 19 | the file it serves carries the sparse-attention index; the launch check reports it engaged | `file-listing-2026-09-26.txt` (the Q2_K_L shards); `minimax-m3/2026-09-20_q2kl_ctx131072_ub2048.launch-check.log` (`MSA ENGAGED`) |
| 19 | the earlier file lacked the tensors | our session notes; stated, not a measurement |
| 19 | at 262,144 no micro-batch from 512 to 2048 could allocate | `minimax-m3/2026-09-20_q2kl_ctx262144_attempts.log` (buffers of 20,572,169,216, 10,286,650,368 and 5,143,890,944 bytes) |
| 19 | 196,608 loads only at `-ub 512`; 58,307 tokens at 70.16, 3 of 3 | `minimax-m3/2026-09-20_q2kl_ctx196608_attempts-and-launch-check.log` (2048 and 1024 fail); `2026-09-20_q2kl_ctx196608_ub512.server.log`, task 271; `2026-09-20_q2kl_ctx196608_needle_58k.json` |
| 20 | 15.74 and 14.69; 898.8 on 24,013 and 911.6 on 150,158 through the model manager | `batch-sweep-2026-09-21/Laguna-S-2.1_ctx262144_model-manager.result` |
| 20 | 12.73 on 35 tokens and 866.1 on 200,098, `-ub 4096` | `Laguna-S-2.1_ctx262144_4096_series.result`, read 2, and its log |
| 20 | row note: 72.2 at `-ub 128` and 1,434.0 at 8192, on 24,071 at 32,768 | `Laguna-S-2.1_baseline_ub128.result`; `Laguna-S-2.1_8192.result` (`served: n_ctx_slot = 32768`) |
| 21 | 193.65 on 139 tokens; 2,737.7 on 48,090 | `batch-sweep-2026-09-21/Muse-Glimmer-30B_skip.result` (`reasoning_len` 448) and its log |
| 22 | did not answer within the check's timeout, 2026-09-12 | `tool-recall-wave1-2026-09-12.tsv`, its `fails` cell; `gate-records/mistral-medium-3.5-128b.json` |
| 22, 23 | 32,768 | `file-listing-2026-09-26.txt`, section C |

Windows as served (fix pass, 26 September). Every window cell now says what shows it.
`installed-windows-2026-09-21.txt` lists, for each endpoint that has one, a run on 21 September that started the model through
its own start script **without passing a window**, and the window the server then reported: the crash check
(`batch-sweep-2026-09-21/stress_chain.sh`, `stress_model.py`, summary `STRESS.txt`) for rows 2 (262,144), 3 (262,144
on both presets), 4, 5, 6, 8, 9, 17 and 18 (131,072) and 11 (262,144); the batch sweep's `_skip` runs
(`batch_sweep.sh` passes no argument; each `_skip.result` and `_skip.log` is in `batch-sweep-2026-09-21/`) for rows 7, 15 and 21 (131,072), 12 (202,752), 14 and 16 (262,144). Row 20's
262,144 is its start script's own fallback, `CTX="${1:-262144}"`, and that script reads no settings file
(`file-listing-2026-09-26.txt` section C); row 19's 131,072 likewise, `CTX="${1:-131072}"`. Rows 1 and 10: every run that loaded 262,144 passed it explicitly, so the cell gives the
script's fallback (131,072) and the dates 262,144 was loaded (`installed-windows-2026-09-21.txt` section C). Row
13's 131,072 with a 5-bit cache is its 12 September framework record's `S.n_ctx` and the 12 September sweep's
`long-128K` row (`kv` q5_1). Rows 22 and 23: the start scripts' default profile and accepted windows (listing
section C). The batch setting printed with each window is the start script's setting at that window (listing
section C); `batch_sweep.sh` records that the settings files do not set the batch sizes.

### Section 03 rows and notes changed in the fix pass (26 September)

| row | figure on the page | file and field |
|---|---|---|
| 1 | 14.76, 12.04 and 7.66 on the short code answers of 67, 69 and 83 tokens | `DeepSeek-V4-Flash-pair_512_series.result` and `..._512_150k.result`: `decode_tps`, `gen_n` |
| 1 | the framework record's verdict is FAIL, on a separate leg | `gate-records/deepseek-v4-flash-0731-two-machines.json`: `verdict`, `fails` |
| 1 and 3 | 6.7 and 12.3 times, each machine at its own setting | 690.9 / 102.5 and 632.1 / 51.4 (arithmetic) |
| 1 and 3 | at `-ub 2048`: the pair 224.9 on 2,998 and 117.0 on 48,024; the desktop (`-b 4096`) 208.1 and 426.5; 3.6 times | `DeepSeek-V4-Flash-pair_2048_series.result`, `DeepSeek-V4-Flash-3bit-desktop_2048_series.result`; the `-b` values in `DeepSeek-V4-Flash-pair_chain.sh` and `series_probe.sh` |
| 1 and 3 | whole requests at 48,024 tokens: 75.2 s alone, 474.2 s on the pair kept, 416.4 s at `-b/-ub 2048` | `wall_s` in `DeepSeek-V4-Flash-3bit-desktop_4096_series.result` (`#2`), `DeepSeek-V4-Flash-pair_512_series.result` and `DeepSeek-V4-Flash-pair_2048_series.result` (`size 48000`) |
| 5 and 10 | the quote-the-code read passed at every depth; the edit-and-reread request, capped at 40 tokens of reply, did not return the code at any depth | `letters-2026-09-26/Qwen3-235B_2048.jsonl` and `Qwen3.6-27B_ctx262144_draft-off.jsonl`: `kind` `read` (`code_in_answer` true) and `edit_reread` (`code_in_answer` false, `predicted_n` 40); the cap is `max_tokens` 40 in `prose_probe.py` |
| 20 | the old script set `-b 512 -ub 128`; it now uses `-b 8192 -ub 4096` above 32,768 | `file-listing-2026-09-26.txt` section C (the saved copy's lines 54 and 55; the current script's lines 68 and 69) |
| hero | Laguna: 72.2 at `-b 512 -ub 128` and 1,434.0 at `-b/-ub 8192` at 32,768; 898.8 on 24,013 at 262,144 and `-b 8192 -ub 4096` | `batch-sweep-2026-09-21/Laguna-S-2.1_baseline_ub128.result` and `Laguna-S-2.1_8192.result` (`n_ctx_slot = 32768`); `Laguna-S-2.1_ctx262144_model-manager.result` (898.8 on 24,013; the series run at `-ub 4096`, `Laguna-S-2.1_ctx262144_4096_series.result`, read 901.9 on the same prompt); the batch lines as row 20 |


## Section 04, what a batch setting did

| page says | file |
|---|---|
| the six rows of the table | `batch-sweep-2026-09-21/<model>_skip.result` and `<model>_<setting>.result` for Qwen3.5-397B-A17B (4096), Qwen3.5-122B-A10B (4096), Mistral-Small-4 (8192), Ornith-1.5-35B (4096), Qwen3-235B-A22B-Instruct-2507 (2048); GLM-5.3-Flash `_skip` (24,008 tokens) and `_4096_series` (read 4, 48,168) |
| every setting that loaded quoted the code | the same results, `needle_in_answer` true |
| speaking moved by 6.2 percent at most, 30.81 to 32.72 | the same results, `decode_tps` (arithmetic: 32.72 / 30.81 = 1.062) |
| at 262,144 the scripts of the Qwen3.5 pair, Mistral Small 4 and Ornith keep `-b 2048 -ub 512` because the larger buffer does not fit | `file-listing-2026-09-26.txt` section C, rows 4, 6, 8 and 17 (the `if [ "$CTX" -gt 131072 ]` lines and the comments above them) |
| the models kept at the defaults: on each one's best rung, from a 0.6 percent loss (Muse Glimmer, 2,721.3 against 2,737.7 at 1024) to a 34.5 percent gain (Gemma-4-26B-A4B at 2048, 12,063.4 against 8,972.3, speaking 153.82 against 163.68, 6 percent slower); Qwen3.6-27B's rungs are the earlier Q4 file at 131,072; GLM-4.7-Flash at 2048 returned an empty answer (`needle_in_answer` false, `answer_len` 0, `needle_found` true) | `batch-sweep-2026-09-21/{Qwen3.8-27B,Qwen3.6-27B,GLM-4.7-Flash,Gemma-4-26B-A4B,gemma-4-31b-it-qat,Muse-Glimmer-30B}_{1024,2048,4096}.result` against each `_skip.result`: Gemma-4-26B-A4B at 2048 read 12,063.4 against 8,972.3 (+34 percent) and spoke 153.82 against 163.68; Muse Glimmer's best rung read 2,721.3 against 2,737.7 |

## Section 05, what changed since 15 September

`summary-table-corrections-2026-09-26.csv` carries the table with, for each line, where the old figure stood and
the package files that correct it. The old figures sat in our operator records and session results, which are not
published; the 15 September list's own figures are in `ROSTER_22.csv`.

| line | the correcting file and field |
|---|---|
| Qwen3-235B 8.2 | `Qwen3-235B-A22B-Instruct-2507_2048.result` (8.18) and its log (11 tokens); the letters |
| Qwen3.5-397B 385 | the 385's prompt size and window come from the model's spec card as quoted in our records (August); stated. The September figures are in the row 4 files; 215.5 against 195.2 are `l128.A_recall.prefill_tps_approx` in the two framework records |
| GLM-4.7 Full passed | `gate-records/glm-4.7-full-358b.json`, `verdict` |
| MiniMax M3 194 | see point 4 at the top |
| MiniMax M2.7 45.6 on "4,000" | `minimax-m2.7/2026-09-13_extract.txt` section 2: the probe line `("long(~4k tok)", longp)` and the recorded `(6776 tok)` |
| Laguna 72 (old window, `-b 512 -ub 128`) and 1,434.0 (`-b/-ub 8192`); 898.8 on 24,013 at 262,144 now | `Laguna-S-2.1_baseline_ub128.result` and `Laguna-S-2.1_8192.result` (`n_ctx_slot = 32768`); the old script's batch lines (`file-listing-2026-09-26.txt` section C); `Laguna-S-2.1_ctx262144_model-manager.result` |
| the pair at 262,144 on 21 September: 14.73 and 12.05 on replies of about 400 tokens; 14.76 and 12.04 on the short code answers | `DeepSeek-V4-Flash-pair_512_series.result`: `warm_decode_tps`, `warm_gen_n`; `decode_tps`, `gen_n` (67, 69) |
| the pair's 15.9 to 17.1 | `ROSTER_22.csv` row 1 and `two-box-deepseek-probes-2026-09-13-to-15.txt` run 5 (13 September, 131,072); the 21 September figures in row 1's files |
| 22 endpoints; seven rows now serving 202,752 or 262,144 by default, two more that loaded 262,144 when it was passed | `ROSTER_22.csv`; `ROSTER_23.csv`, `window_and_batch_setting` (rows 2, 3, 11, 12, 14, 16, 20; and rows 1, 10); `installed-windows-2026-09-21.txt` |
| every read that asked for a planted code returned it in its answer, except GLM-4.7-Flash at `-ub 2048`; the letter runs' edit-and-reread requests did not return it at any depth | every file named in section 03 with `needle_in_answer`, `needle_found`, `hits`, `score`, `codes_hit` or `code_in_answer`; the exception is `batch-sweep-2026-09-21/GLM-4.7-Flash_2048.result`; the `edit_reread` lines of `letters-2026-09-26/*.jsonl` (`code_in_answer` false, `predicted_n` 40, the reply cap `prose_probe.py` sets for that request) |

## Section 06, on request

| page says | file |
|---|---|
| the Qwen3.5 pair and Mistral Small 4 read about 231,000 tokens at 262,144 (15 September, at `-b 2048 -ub 512`, which their scripts keep there) | `CONTEXT_256K_MEASUREMENTS.tsv`, rows `Qwen3.5-397B-A17B_262144`, `Qwen3.5-122B-A10B_262144`, `Mistral-Small-4_262144` (230,803, 230,803, 231,065; 3/3) |
| Qwen3.8-Flash-Next read 344,981 and 459,911 at its two larger windows, at llama.cpp's default batch sizes, before its batch change | `qwen3.8-flash-next-2026-09-20/q8cache_ctx393216_deep.result`, `q8cache_ctx524288_deep.result`; `run_hard.sh` passes no batch flag |
| MiniMax M3 58,307 at 196,608 (`-ub 512`); MiniMax M2.7 only 3,658 at 196,608 (`-ub 1024`) | see rows 19 and 18 above |
| Qwen3.8-27B and Ornith-1.5-35B scripts offer 262,144 on a 17 September run whose logs were not kept | `file-listing-2026-09-26.txt`, section C (the `262144 MEASURED 2026-09-17` comments); no run record exists |

## What has no file in this package, stated plainly

1. The installation and retirement dates in section 01, and Qwen3.6-27B's served window: our operator records.
2. That MiniMax M2.7's `-ub 128` was copied from another model's launcher, and that MiniMax M3's earlier file lacked
   the sparse-attention tensors: our session notes.
3. The 385 for Qwen3.5-397B and its prompt size, and the other old figures in section 05: our own records as they
   stood, which are not published; each correcting figure is in the package.
4. The processor model: the machine's specification, stated on the site's method page.
5. Every framework reading figure is the harness's estimate, not a server timing; the page says so.
