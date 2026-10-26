# NUMBERS.md: every figure on "October field notes"

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

The one place a file will look like it contradicts the page: the Xid table names "a desktop app" and "the desktop's
compositor" where `xid/kernel-xid-lines-2026-10-12-to-25.txt` prints the process names. They are the same events; the
page describes the programs instead of naming them.

| Entry | Page figure | File | Field / derivation |
|---|---|---|---|
| 01 | five Xid 8 lines, times 19:19:30, 19:23:42, 18:05:18, 18:12:00, 21:21:37; "GPU is probably locked! Notify Timeout Seconds: 7" | `xid/kernel-xid-lines-2026-10-12-to-25.txt` | the boot -5 and boot -2 blocks; each time is the Xid line (the 18:05 fault's watchdog line is at 18:05:17, its Xid line at 18:05:18) |
| 01 | zero in six boots on 580.173.02 from 12 October to 18 October 11:47 | same | per-boot counts -13 to -8 and the boot list; driver load lines |
| 01 | 595.104.02 loaded 11:48:03 on 18 October | same | boot -7 load line |
| 01 | faults in two of the eight boots since; none after 21 October 21:21 | same | counts for boots -7 to 0 |
| 01 | UD-Q5_K_XL, 196,608, 8-bit cache, draft model plus n-gram, -ub 512, thinking on; peak 29,977 MiB; stop 19:19:30 (card 685 MiB after) | `xid/F2_q5_192k_ub512_dflash_ngram_thinkON.result` | `cmd:` line (`--model`, `--ctx-size`, `--cache-type-k/v q8_0`, `--spec-type draft-dflash,ngram-mod`, `--ubatch-size`); "served: n_ctx_slot"; "peak VRAM"; "stopped"; thinking on = the run's name (`thinkON`); about 29.3 GiB is 29,977 / 1,024 (arithmetic) |
| 01 | same setup, 229,376, -ub 256; peak 30,647 MiB; stop 19:23:44 | `xid/F3_q5_224k_dflash_ngram_thinkON.result` | the same fields |
| 01 | boot ended 19:41:05, next began 19:41:44 (the cost line's "a restart at 19:41"); the screen froze at the compositor fault; the restart was forced | `xid/kernel-xid-lines-...txt`; our 19 October operator note (not shipped) | boot list for the times; the freeze and the forced restart are the operator note's words, and the table cell and the cost line attribute them to it |
| 01 | last request before the fault 114,792; "launch timed out" | `xid/artemis-31b-b10453-2026-10-21-1805.server-excerpt.txt` | last "stop processing: n_tokens" before the CUDA error (an earlier line reaches 115,381) |
| 01 | last request before the fault 115,805 | `xid/artemis-31b-b11712-2026-10-21-1812.server-excerpt.txt` | last "stop processing" line (116,157 just before it) |
| 01 | last request before the fault 113,568 | `xid/aura-4o-rebirth-2026-10-21-2121.server-excerpt.txt` | last "stop processing" line (113,854 just before it; an earlier line reaches 114,419) |
| 01 | two later starts: prompts of 80,062 and 113,205, plus later prompts, the longest of those 7,419 tokens (44 prompt-eval lines in all, one per prompt read: 20 and 24), with no CUDA line in those files | `xid/aura-4o-rebirth-rerun-2026-10-22-0311.timing-only.txt`, `-0318.timing-only.txt` | first prompt-eval line of each; the other prompt-eval lines (largest 7,419 in the 03:11 file); 20 + 24 lines; no CUDA error line |
| 01 | journal's last line 25 October 02:03 | `xid/kernel-xid-lines-2026-10-12-to-25.txt` | boot 0 "last entry" |
| 01 | 239,533 tokens on Ornith-1.5-122B, 206,883 on Hemmingway-1 | the October roster's package: `runs/ornith-1.5-122b-2026-10-23/measure.jsonl`, `runs/hemmingway-aura-spark-2026-10-22/measure.jsonl` | read rows |
| 02 | four knowledge bases, three instances, 768 vs 1,024 (bge-m3), 384 vs 768 (nomic-embed-text) | `knowledge-base/vector-sizes-2026-10-18.txt` | the four lines |
| 02 | meaning search failed with no error; keyword matches remained except where hybrid search was off; Open WebUI 0.12.3; rebuilt 20 October through the re-index endpoint | our 20 October re-index session note (not shipped: it names the instances) | its "What was wrong" paragraph and its version and method lines |
| 03 | part 3 of 5, UD-IQ2_M, published hash begins 7478bfa7, HF_HUB_DISABLE_XET=1 | `download/fetch_beam_iq2m_part3.sh` | lines 2 to 11 |
| 03 | "twice", "hung at the end" | `download/fetch_beam_iq2m_part3.sh` | the script's own comment, line 2; no log of those two attempts ships |
| 03 | Beam now on UD-Q2_K_XL | the October roster, section 03 (unsloth UD-Q2_K_XL, 5 files, 186,877,720,196 bytes) | that page's file-size table |
| 04 | the temporary server fault that ended the tool | `download/hf-download-error-line-2026-09-19.txt` | "CAS service error : ... Request failed after 5 retries" |
| 04 | sparse partials; du -sb counts holes, du -sB1 counts blocks; staged 19 and 20 September | our 19 to 20 September download session note (not shipped) | its "Two download traps" section and its date line; its percentages are left off the page |
| 05 | gate and up 5,120 x 2,304 x 384; down 2,304 x 5,120 x 384 | `converter/convert_try1_stopped.log` | the 10 "repacked routed experts to MXFP4, shape" lines (7 gate or up, 3 down) |
| 05 | about 2.4 GB per array | arithmetic | 5,120 x 2,304 x 384 weights x 4.25 bits / 8 = 2,406,481,920 bytes |
| 05 | 120 arrays; about 289 GB (268.9 GiB) | `converter/repacked-tensor-count.txt`; arithmetic | 120 x 2,406,481,920 = 288,777,830,400 bytes = 268.9 GiB |
| 05 | 188 GiB of RAM | the published GLM-5.3-Flash field card's machine row ("188 GiB RAM") | not re-measured |
| 05 | 90 seconds, 10 of 120, exit code 143 | `converter/convert_try1_stopped.log` | start 00:38:14, CONVERT-FAILED rc=143 00:39:44, 10 repack lines |
| 05 | stopped by hand before the machine ran out of memory | our 18 October operator note (not shipped) | the note's words: the attempt was stopped by hand at 00:40, before it ran out. Not a log line; the page attributes it to the note. The note counts 9 arrays; the log's 10 repack lines are what the page prints. The 289 GB is a projection (arithmetic below), not a measured peak |
| 05 | nothing had been written | `converter/convert_try1_stopped.listing-note.txt` | "output directory listing after the failure contained only . and .." (the listing itself is removed: it named the Unix account) |
| 05 | 00:41:36 to 03:29:07, 2 h 47 min; inside a systemd scope | `converter/convert_final.head-and-tail.log` | CONVERT-START, "Running as unit ... scope", CONVERT-DONE |
| 05 | MemoryMax=64G, MemorySwapMax=0 | `converter/wrapper-line.txt` | the systemd-run line |
| 05 | 11 files, 1,012 tensors, 501.80 GB, same layout; two metadata keys differ: the name became Source, the chat template's new value is None | `converter/layout_compare.txt` | old/new lines; "different shape/type/size: 0"; "metadata keys that differ: 2"; the general.name line; the tokenizer.chat_template line (old template text removed); SAME-LAYOUT |
| 06 | low / high, anything else max | `reasoning/glm-5.3-flash-template-effort-line.txt` | the template line |
| 06 | 24,000 tokens at 12.28 t/s, 32.6 minutes | `reasoning/mimo-v2.6-flash.timing-only.txt` | eval time 1,953,986.87 ms / 24000 tokens (32.6 min, arithmetic) |
| 06 | no answer without a cap; cap 14,000 | `reasoning/mimo-v2.6-flash-start-script-note.txt` | the script's note and its `THINK` default |
| 06 | 36 empty answers out of 40 on the 262,144, -ub 1024 setting | the published GLM-5.3-Flash field card, "What this does not show" | published |
| 07 | 48,396 tokens in 0.93 s; inconsistent sequence positions, then the draft decode failed at position 48,110, then "failed to process speculative batch" | `slot-restore/glm-4.7-full.pcores-restore-failed.jsonl`, `.errors.txt` | slot_restore `n_restored`, `restore_ms` 927.08; errors lines 1 ("inconsistent sequence positions"), 4 ("llama_decode(ctx_dft) head=0 failed rc=-1 (pos=48110)"), 5 ("failed to process speculative batch") |
| 07 | 100,264 tokens, carried on | `slot-restore/minimax-m2.7.pcores.jsonl` | `n_restored`; the following t0_prose row |
| 08 | UD-Q3_K_XL; 109,712 deep; 5.71 (16-bit, window 118,784) / 4.24 (8-bit, 131,072) / 2.86 (4-bit, 131,072); 640 to 649 | `kv-cache/d1b_f16.jsonl`, `d1a_q80.jsonl`, `d1c_q40.jsonl`; the October roster's package, `runs/qwen3-235b-2026-09-29/start-lines.txt` | prose `decode_tps`; fill_read `prefill_tps` 640.15, 648.64, 643.61; windows and file from the START lines and the file line |
| 08 | about a quarter slower, on these single replies | arithmetic | 4.24 / 5.71 = 0.74 |
| 08 | 8-bit until 29 September; switched to 16-bit that day | our 29 September session results note (not shipped), its production-cache row and its install line; the model's settings file now sets a 16-bit cache | session record |
| 09 | DeepSeek V3-0324 108,315 / 56.9 / 1,902.6 s; window 114,688 | `cold-reads/deepseek-v3-0324-iq1s-2026-10-23.timing-only.txt` | first prompt eval line; first line `n_ctx_slot = 114688` |
| 09 | DeepSeek R1-0528 108,315 / 100.9 / 1,073.7 s; window 114,688 | `cold-reads/deepseek-r1-0528-tq1-2026-10-23.timing-only.txt` | first prompt eval line; first line `n_ctx_slot = 114688` |
| 09 | DeepSeek V4.1-Flash-1017 110,052 / 153.5 / 716.9 s; window 131,072 | the October roster's package, `runs/deepseek-v4.1-1017-2026-10-18/N1-1017.depth.jsonl`; `cold-reads/deepseek-v4.1-1017-server-lines.txt` | read:375000; line 11 `n_ctx_slot = 131072` |
| 09 | it also read expert weights from the drive | `cold-reads/deepseek-v4.1-1017-server-lines.txt` | the cumulative "slabs from the drive" counter rose from 691.6 GiB (line 154) to 3,680.3 GiB (line 206, just after the read) |
| 09 | Muse Spark 106,469 / 155.0 / 686.9 s; window 131,072 | the October roster's package, `extracts/timing-only/muse-spark-open-131072-2026-10-21.txt` | first prompt eval line; first line `n_ctx_slot = 131072` |
| 09 | Mistral Large Instruct 2411, Q4_K_M; 122,880 / 222.8 / 551.5 s to finish the read; window 131,072 | `cold-reads/mistral-large-2411-2026-10-21.timing-only.txt`; the server log's load filename Mistral-Large-Instruct-2411-Q4_K_M-00001-of-00002.gguf (log not shipped) | the line "n_tokens = 122880, progress = 1.00, t = 551.49 s / 222.82 tokens per second"; no eval line; first line `n_ctx_slot = 131072` |
| 09 | the client timed out at 5,400.1 s with no finished reply | `cold-reads/mistral-large-2411-2026-10-21.client-note.txt` | a hand-written note; not a server timing line. 5,400.1 s is the client's timeout for the request, not a second wait after the read |
| 09 | minutes | arithmetic | seconds / 60 |
| 09 | a September turn ended at 1,800.4 seconds with no answer | the September field notes and their package | published |
