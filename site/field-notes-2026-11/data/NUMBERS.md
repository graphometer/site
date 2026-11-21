# NUMBERS: every figure on the page, mapped to its file

Paths are inside this package. "Arithmetic" rows show the sum or difference.

| Page figure | File | Field or derivation |
|---|---|---|
| 01: 102 stops; 710 to 1,642 MiB | `01-desktop-card/card-after-each-stop-2026-11-01.txt` | last line: count 102, min 710, max 1642 |
| 01: about 2 to 5 percent of 32,607 MiB | arithmetic | 710 / 32,607 = 2.2%; 1,642 / 32,607 = 5.0% |
| 01: `--n-cpu-moe 23`; 131,072 window; batch and micro-batch 2048 | `01-desktop-card/gpt-oss-120b-ship.cmd.txt` | `--n-cpu-moe 23`, `--ctx-size 131072`, `--batch-size 2048 --ubatch-size 2048`, `--parallel 1` |
| 01: `allocating 1315.93 MiB on device 0: cudaMalloc failed: out of memory` | `01-desktop-card/gpt-oss-120b-n-cpu-moe-23.server-errors.txt` | line 2 |
| 01: 24 blocks loaded, 30,627 MiB when ready | `01-desktop-card/gpt-oss-120b-ship24.cmd.txt`; `gpt-oss-120b-n-cpu-moe-24.run-lines.txt` | `--n-cpu-moe 24`; "ready after 86 s, card 30627 MiB" |
| 01: chat, tool call, two-token reply passed; 131,072 window | `01-desktop-card/deepseek-v4.1-flash-short-calls-2026-11-02.txt` | 14:05:26 `--ctx-size 131072`; 14:05:31 chat ok; 14:06:00 tool called; 14:06:01 `gen_n': 2` |
| 01: about 32,000 characters; 53.2 s; HTTP 502; 31,987 MiB | `01-desktop-card/deepseek-v4.1-flash-real-size-check-2026-11-02.log` | 14:25:32 "32000 characters"; 14:26:25 FAILED line; 14:26:26 "card peak 31987" |
| 01: batch 2560; 7,175, 7,175 and 26,781 prompt tokens; 30,771 MiB or less; 40-token cap | same file and its header (40-token reply cap) | b2560-first, -second, -long "prompt tokens" and peaks 30771, 30721, 30719 |
| 01: read the card every quarter second | same file, header | "samples the card every 0.25 s" |
| 02: v0.12.5; hybrid search; reranker; embedding model | `02-empty-search/settings-lines.txt` | image line, `ENABLE_RAG_HYBRID_SEARCH`, `RAG_RERANKING_MODEL`, `RAG_EMBEDDING_MODEL` |
| 02: 20 documents, 10 questions, all first | `02-empty-search/results-2026-11-02.log` | 14:25:42 "20 docs"; 14:26:19 "10 of 10 ... ranks [1, ...]" |
| 02: 10 direct searches failed with HTTP 400; 20 files failed | same file | 14:52:55 ten "query failed 400" lines; 14:53:06 "20 docs in 10.7 s, 20 failed" |
| 02: HTTP 200 in 8.7 s, no code | same file | 14:57:07 "HTTP 200 in 8.7 s; 4471 found: False" |
| 02: note that the forwarding service was stopped | same file | the line after 14:57:07 (a note written into the log) |
| 02: code with `[1]` in 5.8 s, after pointing at the laptop | same file | 14:57:17 switch line; 14:57:23 "HTTP 200 in 5.8 s; 4471 found: True" and its reply |
| 02: the desktop processor also found all 10 first | same file | 14:48:14 to 14:48:44 "searched with the RTX processor", "10 of 10 ... ranks [1, ...]" |
| 03: 32,768 window | `03-timeout/mistral-large-4-server-cancel-lines.txt` | `n_ctx_slot = 32768` |
| 03: `stream=False`; 1,800 s; 6,000-token cap; caching off | `03-timeout/ask_round_v1.py`; `03-timeout/round-invocation.txt` | `stream=False`, `cache_prompt=False`; `large4 6000 1800` |
| 03: questions 1, 2 and 6 at 1,800.1 s, no text; 3, 4, 5 finished | `03-timeout/mistral-large-4-round-2026-10-31.txt` | q1, q2, q6 `1800.1 s None 0 error 0`; q3, q4, q5 `stop` |
| 03: 4,328; 4,713; 906 tokens | `03-timeout/mistral-large-4-server-cancel-lines.txt` | `n_gen` on the last progress line at or just after each cancel |
| 03: about 90 minutes | arithmetic | 3 x 1,800.1 s = 5,400.3 s |
| 04: 501B-A23B, UD-Q2_K_XL, 131,072 window, batch 4096, micro-batch 2048 | `04-first-reply/beam-default.cmd.txt`, `beam-dio.cmd.txt` | model file name, `--ctx-size`, `--batch-size`, `--ubatch-size` |
| 04: 66-token prompt, 420 tokens | `04-first-reply/beam-1.0-two-loadings-2026-11-01.txt` | `read_n` 66, `gen_n` 420 on `prose1` and `prose2` |
| 04: default 289 s, 164 GiB; 1.95 t/s, 289.7 s, 44.7 GB; 8.37 t/s, 57.2 s | same file | default first line; `prose1` and `prose2` `gen_tps`, `wall_s`, `drive_GB` |
| 04: dio 135 s, 11 GiB; 8.38 t/s, 54.5 s, 0.1 GB; 8.29 t/s, 54.3 s | same file | dio first line; `prose1` and `prose2` |
| 04: a later dio start, first reply 3.62 t/s | `04-first-reply/beam-dio-later-start-2026-11-01.txt` | `--load-mode dio` in the command line; `eval time = ... / 420 tokens ... 3.62 tokens per second` |
| 05: 46 of 72 layers; 26 on the laptop | `05-laptop-worker/serve_split.sh`, `run_split2.txt` | `N_LAYERS=72`, `DESKTOP_LAYERS` 46; run label split-46-4 |
| 05: six answers of symbols, 1.67 to 4.82 t/s | `05-laptop-worker/answers/split-46-4-*.json` | `gen_tps`, `answer` |
| 05: sample of symbols | `05-laptop-worker/answers/split-46-4-short2.json` | start of `answer` |
| 05: no error line | `05-laptop-worker/server-log-error-check.txt` | "E lines 0" |
| 05: readable, 2.10 to 3.98 t/s; two of six with a final answer | `05-laptop-worker/answers/split-cpu-46-4-*.json` | `gen_tps`; `answer` non-empty in `after` and `read2k`, empty in the other four |
| 05: about 20 minutes | `05-laptop-worker/run_split2.txt` | sum of `wall_s`: 285.4 + 68.0 + 201.1 + 185.3 + 149.1 + 52.8 = 941.7 s, plus "ready after 256s" = 1,197.7 s |
| 06: 229,376 window | `06-xid/229k-draft.server-excerpt.txt` | `n_ctx_slot = 229376` |
| 06: 31,094 idle, 31,235 highest; 1,372 below 32,607 | `06-xid/SHAPES-2026-11-03.log`; arithmetic | 20:04:35 line; 32,607 less 31,235 |
| 06: 205,741 tokens at 1,185.6 t/s | `06-xid/229k-draft.probe.jsonl` | depth 205376 read row, `prompt_n` and `prefill_tps` |
| 06: 198,656 tokens, 97 percent; CUDA error | `06-xid/229k-draft.server-excerpt.txt` | last progress line (`progress = 0.97`) and the error line |
| 06: the four runs, highest readings and Xid counts; 20:14:16 | `06-xid/SHAPES-2026-11-03.log` | "peak" and "Xid lines since start" per run; 196k-draft-a stop and 196k-no-draft start both 20:14:16 |
| 07: huggingface_hub 1.3.4; the CAS error twice; 1 of 8 at 29:48 | `07-download/hf-tool-attempts-2026-10-30.txt` | version line; two RuntimeError lines; `1/8 [29:48<` |
| 07: 128 MiB, 16 workers | `07-download/download_attempt3.py` | `PIECE = 128 << 20`, `WORKERS = 16` |
| 07: 15:39:12 to 17:00:22; five files; 1,856 pieces | `07-download/piece-downloader-2026-10-30.log` | first and last lines; pieces 295 + 297 + 291 + 149 + 824 |
| 07: 23 errors: 16 timeouts, 4 resets, 3 short reads | same file | count of error lines by kind |
| 07: five files matched | same file; `07-download/expected-sha256.tsv` | five `OK` lines (written only after the hash matches) and `SHA_ALL_OK` |
| 07: about an hour | arithmetic | 14:37:41 (first hf start) to 15:39:12 (downloader start) = 61.5 minutes |
| 08: four a second, about 110 s | `08-network/ph_*.txt`, `w_*.txt` | timestamps 0.25 s apart; ping summary `time 109975ms` to `111990ms` |
| 08: two then three DNS servers | `08-network/` | `ph_g`, `ph_cf`; `w_g`, `w_cf`, `w_c` |
| 08: 6.1 to 8.9 percent over whole runs | same files | summary lines: 8.90, 8.68, 8.30, 6.05, 6.73 percent loss |
| 08: 3.8 to 19.3 percent quiet; 0 to 2.6 busy (estimate) | `08-network/loss_by_phase.output.txt` | rows `both` and `wired`: lowest 6/160, highest 17/88 quiet; 0 to 1/39 busy |
| 08: 22:36; 0 of 446 to three DNS servers; 0 of 438 to the gateway | `08-network/r_*.txt` | first timestamp of `r_g.txt` 1793414205 = 2026-10-30 22:36:45 local; summary lines |
| 08: 0 of 597 to each of two | `08-network/q_g.txt`, `q_cf.txt` | 597 transmitted, 597 received |
| 08: 21 of 597; 2,060.6 ms | `08-network/q_wifi.txt` | 576 received; rtt max 2060.602 |
| What we ran: 32,607 MiB | `01-desktop-card/deepseek-v4.1-flash-real-size-check-2026-11-02.log` | "of 32607" |
| What we ran: 188 GiB | `05-laptop-worker/run_split2.txt` | `Mem: 188` (free -g) |
| What we ran: builds | `builds.txt` | one line per run |
