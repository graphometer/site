# Data package: context-256k

## Where these files can appear to disagree

- The main TSV has eleven rows. The page’s main table uses ten configurations at their large served windows. The extra DeepSeek split row at 131,072 is retained for completeness, not included in the ten-row ranges.
- `decode_tps` is the best of two earlier short-prompt prose replies. The page’s at-depth rates are `deep_decode_tps` and the deep JSON’s `predicted_per_second`, for 25 to 33 token code answers. They are different workloads.
- The 15 September DeepSeek Q8 read and the 20 September (collection date) read are both preserved. The latter has explicit larger batch settings, a different prompt length and no recorded build identifier. The timing improvement is not a controlled single-variable result.
- Laguna’s 866.1 tokens/s is `prefill_tps`, not wall ÷ tokens; its 233.9 s `wall_s` is request wall time, whereas the main table uses prompt-processing time. Its peak is for a series of requests, and its retrieval check uses one planted string. DeepSeek’s later memory value is at load, not a request peak.
- Qwen3.5’s main-table launches retained MTP. The Ornith failures and GLM setup note do not justify a blanket claim that draft heads cannot coexist with a 262,144 window.
- GLM Full is a copied configuration-comment excerpt, not a raw run result. It is labelled as such on the page.
- The two 26 September Flash-Next rows (`flashnext-fullwindow/`) used another placement than the 15 September Flash-Next row: 40 expert layers requested on CPU instead of 99, and an 8-bit cache. Their 205.5 tokens/s at the default batch is not a re-measurement of the 165.70 row.
- The two 26 September Ornith-1.5-35B rows (`ornith35-fullwindow/`) ran without the MTP draft head that `failures/ornith35_262144.log` requested. They loaded an Ornith-1.5-35B Q6_K file of the same name from another directory (both paths are removed here; neither log records a hash or a file size), with the same window, 6 expert layers in RAM and default cache. They also wrote the batch out (2048 / 512, or 2048 / 2048), used a 7,200-second timeout and set no CORS flag, where the failed launch set no batch, a 3,600-second timeout and a localhost CORS flag; that log's first line is a preflight card reading of 1,113 MiB, and the 26 September results record no reading before launch. The 2048 / 512 row is the start-script copy's own setting at this window then; 2048 / 2048 was passed in (`ORNITH_35B_BATCH` and `ORNITH_35B_UBATCH` in its header) and is the installed script's setting since. So these rows show a file of that name serving this window without the draft head, not the failure's copy serving it with the head. That success does not contradict the failure record.
- The two 26 September Qwen3.5-122B-A10B rows (`qwen122-fullwindow/`) use the launch of its 15 September row, the batch values now written out, but a different probe: a fresh ledger at each depth, thinking off per request, and the deep read after three shorter ones on the same server. Their card figure is at load; the `.result` files also give each series' peak. The page's 822 MiB is arithmetic: the card's reported total, 32,607 MiB, published in the Qwen3.8-27B at 256K package (`/qwen38-256k/data/records/card-capacity.txt`), minus the 31,785 MiB peak of the 2048 / 1024 series. The installed script's comment, quoted in `qwen122-fullwindow/launch-notes.txt`, gives about 0.8 GB.
- The 26 September MiniMax M2.7 row (`minimax-m27-fullwindow/`) is at 196,608, the context length its model file declares, not 262,144, and it has no September 15 row. Unlike the other 26 September rows, thinking was left on (`reasoning_chars` 395, 438 and 480 on the reads). Its two prose requests after the shorter reads spent all 4,096 tokens reasoning and have empty answers; the page uses only the reads. Its card figure is at load; the `.result` also gives the series peak, 31,907 MiB.
- The 26 September GLM-5.3-Flash rows (`glm53-fullwindow/`) have no September 15 row. Its reasoning effort was set to none at launch (`--chat-template-kwargs {"reasoning_effort":"none"}`), yet every reply carries reasoning (`reasoning_chars` 362 to 617 on the reads at 262,144). The -ub 1024 row stops at 47,992 tokens; nothing longer was read at 1024. `glm53_256k_ub4096` is the load failure in section 05 (13,281.37 MiB refused); `glm53_128k_default`, at 131,072, is the comparison the page quotes in its paragraph, not a table row. The page's 656 MiB is arithmetic on the card total cited for Qwen3.5-122B-A10B above: 32,607 - 31,951.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

## Provenance and scope

The main sweep was recorded on September 15, 2026. It used one desktop with an RTX 5090 and system RAM; the DeepSeek IQ3 split also used a laptop. The hardware capacities on the page are the study’s supplied bench specification, not a capacity measurement extracted from these files. Most configurations kept expert weights in system RAM; the 8,473 to 31,068 MiB range is sampled card use. Flash-Next requested 99 expert layers on CPU; the record does not establish that this means all expert layers. GLM-4.7-Flash requested and served 202,752; its launch notes call that its ceiling, but this package has no failed attempt above it. No hosted model output is included. The local outputs are synthetic-ledger retrieval and short water-pump prose responses.

The raw JSON timing fields, generated content, token usage, finish reasons and creation timestamps are retained. Builds are recorded separately as derived commit identifiers because request/provider identifier fields were removed. The Ornith failure logs and audition table have no calendar date. MiniMax’s September 2026 date is collection provenance, not an embedded calendar timestamp. Its three tested headers each place experts on CPU (`cmoe` in the test label). The later DeepSeek and Laguna records have September 20 (collection date) and September 21 (collection date), respectively; neither file contains a calendar timestamp.

## File map

| Files | Type and meaning |
|---|---|
| `CONTEXT_256K_MEASUREMENTS.tsv` | Primary sweep measurement table; includes load-time contention caveat and all eleven original rows |
| `logs256/*.deep.json` | Eleven primary deep retrieval responses, including the extra smaller-window split run |
| `logs256/*.short.r1.json`, `logs256/*.short.r2.json` | Twenty-two primary short-prompt prose responses explaining the TSV’s separate `decode_tps` column |
| `logs256/*.log` | Eleven primary server/probe logs; commands, served-window checks, timings, sampled card readings |
| `deep_recall_probe.py` | Primary synthetic-ledger generator and retrieval request builder |
| `context256_bodies.sh`, `context256_rung.sh` | Primary archived launch and measurement harnesses, with private context removed and placeholders for local setup |
| `failures/ornith35_262144.log`, `failures/ornith397_262144.log` | Primary allocation failures with requested configuration |
| `later/v_W_256k_ub8192.log`, `later/v_W_256k_ub8192.result` | Primary later DeepSeek Q8 reading time, batch settings and load memory |
| `later/Laguna_ctx262144_ub4096.result` | Primary later long-window result; two-request series and series peak |
| `later/MSA_256K.console.log` | Primary MiniMax sparse-attention failure ladder |
| `later/GLM-4.7-Full-config-excerpt.txt` | Source-comment excerpt only, recording the 128K MTP placement trade; not a raw response |
| `flashnext-fullwindow/shipped_b4096_ub2048.jsonl`, `flashnext-fullwindow/default_b2048_ub512.jsonl` | Primary 26 September Flash-Next reads at 262,144, one row per request: tokens, prompt milliseconds, rates, the model file's share in memory before and after, card use, codes |
| `flashnext-fullwindow/run.console.log` | Primary console record of the same run: the file's share in memory before each start, load time, card use at load, served window |
| `flashnext-fullwindow/launch-flags.txt` | Excerpt of the launch flags of the start-script copy used for both rows, paths omitted |
| `ornith35-fullwindow/orn_256k_b2048_ub512.result`, `ornith35-fullwindow/orn_256k_b2048_ub2048.result` | Primary 26 September Ornith-1.5-35B runs at 262,144: header (served window, card at load, launch command), one JSON row per request at four depths (tokens, prompt milliseconds, rates, codes), card peak over the series |
| `ornith35-fullwindow/*.server.log` | Primary server logs of the same two runs: served window, prompt-evaluation times |
| `ornith35-fullwindow/launch-notes.txt` | Derived notes: the two launches against the failure record's, the build, and the installed start script's comment on this window, verbatim |
| `qwen122-fullwindow/q122_256k_b2048_ub512.result`, `qwen122-fullwindow/q122_256k_b2048_ub1024.result` | Primary 26 September Qwen3.5-122B-A10B runs at 262,144: header, one JSON row per request at four depths, draft acceptance lines, card peak over the series |
| `qwen122-fullwindow/*.server.log` | Primary server logs of the same two runs |
| `qwen122-fullwindow/launch-notes.txt` | Derived notes: the two launches against the 15 September launch, the build, and the installed start script's comment on this window, verbatim |
| `minimax-m27-fullwindow/m27_192k_cmoe_ub1024.result` | Primary 26 September MiniMax M2.7 run at 196,608 through its installed start script: header (served window, card at load, launch command), one JSON row per request at three depths (tokens, prompt milliseconds, rates, codes, reasoning length), card peak over the series |
| `minimax-m27-fullwindow/m27_192k_cmoe_ub1024.server.log` | Primary server log of the same run: the start script's note on this window, served window, prompt-evaluation times |
| `minimax-m27-fullwindow/launch-notes.txt` | Derived notes: the window the model file declares, the launch, the build and the requests |
| `glm53-fullwindow/glm53_256k_ub2048.result`, `glm53-fullwindow/glm53_256k_ub1024.result`, `glm53-fullwindow/glm53_128k_default.result` | Primary 26 September GLM-5.3-Flash runs through a copy of its start script, at 262,144 with -ub 2048 and 1024 and at 131,072 with 4096: header (served window, card at load, launch command), one JSON row per request (tokens, prompt milliseconds, rates, codes, reasoning length), card peak over the series |
| `glm53-fullwindow/glm53_256k_ub4096.result` | Primary load failure at 262,144 with -ub 4096: its settings (the env lines) and the exit on load |
| `glm53-fullwindow/*.server.log` | Primary server logs of the same four runs, the failed one with its refused 13,281.37 MiB compute buffer |
| `glm53-fullwindow/launch-notes.txt` | Derived notes: the window, the launches, the build, the requests and the start script's setting at each window |
| `build-records.tsv` | Derived mapping from each original deep response build identifier to its commit |
| `CONFIGURATIONS.md` | Derived per-model command and build map from the archived primary files |
| `NUMBERS.md` | Derived figure-to-field map, rounding and arithmetic |

Exact file inventory follows below. Original request captures and model warmup responses are not included. The generator preserves the synthetic prompt construction. Other tasks from the source collection are outside this package. No internal summaries, session narratives or working manifest are included.

## Redactions

Paths are replaced in full, with a model or shipped-script basename retained where useful. All fixed bound addresses and port values become `<LOCAL>`, including loopback. Process identifiers become `<REDACTED>`. Serving aliases become public model names; in the 26 September Ornith-1.5-35B, Qwen3.5-122B-A10B, MiniMax M2.7 and GLM-5.3-Flash copies, so do the harness's script-copy and settings-variable names (for example `Ornith-1.5-35B_start-script-copy.sh`, `ORNITH_35B_CTX`, `MINIMAX_M27_CTX` and `GLM_5_3_FLASH_CTX`). One start-script banner line naming a private helper process, which plays no part in these measurements, was deleted from the MiniMax M2.7 server log. JSON `id` and `system_fingerprint` fields are removed; the latter’s commit component is separately documented as build provenance. The complete private-context comment block was deleted, not rephrased. Scripts with placeholders are archival evidence, not ready-to-run files.

Counts below are substitutions or deleted fields/lines in the primary copied files. Derived documents reuse the already-redacted material and are not counted again. Original timing values and relative-clock log prefixes were preserved.

| Redaction | Count |
|---|---|
| internal storage label removed | 1 |
| internal paths replaced | 108 |
| addresses replaced | 75 |
| port arguments replaced | 31 |
| comment ports replaced | 10 |
| positional ports replaced | 10 |
| process identifiers replaced | 60 |
| serving aliases replaced | 31 |
| harness script-copy and settings-variable names replaced | 59 |
| punctuation normalized | 18 |
| synthetic punctuation escaped (same generated text) | 3 |
| private-context comment lines deleted | 4 |
| log line naming a private helper process deleted | 1 |
| JSON model aliases replaced | 33 |
| JSON identifier fields removed | 66 |
| Comment fragment closed after paragraph deletion | 1 |

Synthetic string punctuation was written as Unicode escapes in the probe source; it generates the same text. Other em-dash punctuation in logs and comments was normalized to a colon. Response JSON uses Unicode escapes to retain the exact original generated text.

The package brief’s complete case-insensitive leak-sweep pattern was run over index.html and data/ on 2026-09-26. Standard output: empty. Standard error: empty. Exit status: 1 (no matches). The literal command is retained in the non-public SELF_CHECK.md to avoid embedding the forbidden search terms in this public package.


## Exact primary-file inventory

- [CONTEXT_256K_MEASUREMENTS.tsv](CONTEXT_256K_MEASUREMENTS.tsv)
- [deep_recall_probe.py](deep_recall_probe.py)
- [context256_bodies.sh](context256_bodies.sh)
- [context256_rung.sh](context256_rung.sh)
- [logs256/dsv4q8_262144.deep.json](logs256/dsv4q8_262144.deep.json)
- [logs256/dsv4split_131072_120k.deep.json](logs256/dsv4split_131072_120k.deep.json)
- [logs256/dsv4split_262144.deep.json](logs256/dsv4split_262144.deep.json)
- [logs256/flashnext_262144.deep.json](logs256/flashnext_262144.deep.json)
- [logs256/gemma26_262144.deep.json](logs256/gemma26_262144.deep.json)
- [logs256/glm47flash_202752.deep.json](logs256/glm47flash_202752.deep.json)
- [logs256/inkling_262144.deep.json](logs256/inkling_262144.deep.json)
- [logs256/ling_262144.deep.json](logs256/ling_262144.deep.json)
- [logs256/mistral4_262144.deep.json](logs256/mistral4_262144.deep.json)
- [logs256/qwen122_262144.deep.json](logs256/qwen122_262144.deep.json)
- [logs256/qwen397_262144.deep.json](logs256/qwen397_262144.deep.json)
- [logs256/dsv4q8_262144.short.r1.json](logs256/dsv4q8_262144.short.r1.json)
- [logs256/dsv4q8_262144.short.r2.json](logs256/dsv4q8_262144.short.r2.json)
- [logs256/dsv4split_131072_120k.short.r1.json](logs256/dsv4split_131072_120k.short.r1.json)
- [logs256/dsv4split_131072_120k.short.r2.json](logs256/dsv4split_131072_120k.short.r2.json)
- [logs256/dsv4split_262144.short.r1.json](logs256/dsv4split_262144.short.r1.json)
- [logs256/dsv4split_262144.short.r2.json](logs256/dsv4split_262144.short.r2.json)
- [logs256/flashnext_262144.short.r1.json](logs256/flashnext_262144.short.r1.json)
- [logs256/flashnext_262144.short.r2.json](logs256/flashnext_262144.short.r2.json)
- [logs256/gemma26_262144.short.r1.json](logs256/gemma26_262144.short.r1.json)
- [logs256/gemma26_262144.short.r2.json](logs256/gemma26_262144.short.r2.json)
- [logs256/glm47flash_202752.short.r1.json](logs256/glm47flash_202752.short.r1.json)
- [logs256/glm47flash_202752.short.r2.json](logs256/glm47flash_202752.short.r2.json)
- [logs256/inkling_262144.short.r1.json](logs256/inkling_262144.short.r1.json)
- [logs256/inkling_262144.short.r2.json](logs256/inkling_262144.short.r2.json)
- [logs256/ling_262144.short.r1.json](logs256/ling_262144.short.r1.json)
- [logs256/ling_262144.short.r2.json](logs256/ling_262144.short.r2.json)
- [logs256/mistral4_262144.short.r1.json](logs256/mistral4_262144.short.r1.json)
- [logs256/mistral4_262144.short.r2.json](logs256/mistral4_262144.short.r2.json)
- [logs256/qwen122_262144.short.r1.json](logs256/qwen122_262144.short.r1.json)
- [logs256/qwen122_262144.short.r2.json](logs256/qwen122_262144.short.r2.json)
- [logs256/qwen397_262144.short.r1.json](logs256/qwen397_262144.short.r1.json)
- [logs256/qwen397_262144.short.r2.json](logs256/qwen397_262144.short.r2.json)
- [logs256/dsv4q8_262144.log](logs256/dsv4q8_262144.log)
- [logs256/dsv4split_131072_120k.log](logs256/dsv4split_131072_120k.log)
- [logs256/dsv4split_262144.log](logs256/dsv4split_262144.log)
- [logs256/flashnext_262144.log](logs256/flashnext_262144.log)
- [logs256/gemma26_262144.log](logs256/gemma26_262144.log)
- [logs256/glm47flash_202752.log](logs256/glm47flash_202752.log)
- [logs256/inkling_262144.log](logs256/inkling_262144.log)
- [logs256/ling_262144.log](logs256/ling_262144.log)
- [logs256/mistral4_262144.log](logs256/mistral4_262144.log)
- [logs256/qwen122_262144.log](logs256/qwen122_262144.log)
- [logs256/qwen397_262144.log](logs256/qwen397_262144.log)
- [failures/ornith35_262144.log](failures/ornith35_262144.log)
- [failures/ornith397_262144.log](failures/ornith397_262144.log)
- [later/v_W_256k_ub8192.log](later/v_W_256k_ub8192.log)
- [later/v_W_256k_ub8192.result](later/v_W_256k_ub8192.result)
- [later/Laguna_ctx262144_ub4096.result](later/Laguna_ctx262144_ub4096.result)
- [later/MSA_256K.console.log](later/MSA_256K.console.log)
- [later/GLM-4.7-Full-config-excerpt.txt](later/GLM-4.7-Full-config-excerpt.txt)
- [flashnext-fullwindow/shipped_b4096_ub2048.jsonl](flashnext-fullwindow/shipped_b4096_ub2048.jsonl)
- [flashnext-fullwindow/default_b2048_ub512.jsonl](flashnext-fullwindow/default_b2048_ub512.jsonl)
- [flashnext-fullwindow/run.console.log](flashnext-fullwindow/run.console.log)
- [flashnext-fullwindow/launch-flags.txt](flashnext-fullwindow/launch-flags.txt)
- [ornith35-fullwindow/orn_256k_b2048_ub512.result](ornith35-fullwindow/orn_256k_b2048_ub512.result)
- [ornith35-fullwindow/orn_256k_b2048_ub512.server.log](ornith35-fullwindow/orn_256k_b2048_ub512.server.log)
- [ornith35-fullwindow/orn_256k_b2048_ub2048.result](ornith35-fullwindow/orn_256k_b2048_ub2048.result)
- [ornith35-fullwindow/orn_256k_b2048_ub2048.server.log](ornith35-fullwindow/orn_256k_b2048_ub2048.server.log)
- [ornith35-fullwindow/launch-notes.txt](ornith35-fullwindow/launch-notes.txt)
- [qwen122-fullwindow/q122_256k_b2048_ub512.result](qwen122-fullwindow/q122_256k_b2048_ub512.result)
- [qwen122-fullwindow/q122_256k_b2048_ub512.server.log](qwen122-fullwindow/q122_256k_b2048_ub512.server.log)
- [qwen122-fullwindow/q122_256k_b2048_ub1024.result](qwen122-fullwindow/q122_256k_b2048_ub1024.result)
- [qwen122-fullwindow/q122_256k_b2048_ub1024.server.log](qwen122-fullwindow/q122_256k_b2048_ub1024.server.log)
- [qwen122-fullwindow/launch-notes.txt](qwen122-fullwindow/launch-notes.txt)
- [minimax-m27-fullwindow/m27_192k_cmoe_ub1024.result](minimax-m27-fullwindow/m27_192k_cmoe_ub1024.result)
- [minimax-m27-fullwindow/m27_192k_cmoe_ub1024.server.log](minimax-m27-fullwindow/m27_192k_cmoe_ub1024.server.log)
- [minimax-m27-fullwindow/launch-notes.txt](minimax-m27-fullwindow/launch-notes.txt)
- [glm53-fullwindow/glm53_256k_ub4096.result](glm53-fullwindow/glm53_256k_ub4096.result)
- [glm53-fullwindow/glm53_256k_ub4096.server.log](glm53-fullwindow/glm53_256k_ub4096.server.log)
- [glm53-fullwindow/glm53_256k_ub2048.result](glm53-fullwindow/glm53_256k_ub2048.result)
- [glm53-fullwindow/glm53_256k_ub2048.server.log](glm53-fullwindow/glm53_256k_ub2048.server.log)
- [glm53-fullwindow/glm53_256k_ub1024.result](glm53-fullwindow/glm53_256k_ub1024.result)
- [glm53-fullwindow/glm53_256k_ub1024.server.log](glm53-fullwindow/glm53_256k_ub1024.server.log)
- [glm53-fullwindow/glm53_128k_default.result](glm53-fullwindow/glm53_128k_default.result)
- [glm53-fullwindow/glm53_128k_default.server.log](glm53-fullwindow/glm53_128k_default.server.log)
- [glm53-fullwindow/launch-notes.txt](glm53-fullwindow/launch-notes.txt)
