# Data package: context-256k

## Where these files can appear to disagree

- The main TSV has eleven rows. The page’s main table uses ten configurations at their large served windows. The extra DeepSeek split row at 131,072 is retained for completeness, not included in the ten-row ranges.
- `decode_tps` is the best of two earlier short-prompt prose replies. The page’s at-depth rates are `deep_decode_tps` and the deep JSON’s `predicted_per_second`, for 25 to 33 token code answers. They are different workloads.
- The 15 September DeepSeek Q8 read and the 20 September (collection date) read are both preserved. The latter has explicit larger batch settings, a different prompt length and no recorded build identifier. The timing improvement is not a controlled single-variable result.
- Laguna’s 866.1 tokens/s is `prefill_tps`, not wall ÷ tokens; its 233.9 s `wall_s` is request wall time, whereas the main table uses prompt-processing time. Its peak is for a series of requests, and its retrieval check uses one planted string. DeepSeek’s later memory value is at load, not a request peak.
- Qwen3.5’s main-table launches retained MTP. The Ornith failures and GLM setup note do not justify a blanket claim that draft heads cannot coexist with a 262,144 window.
- GLM Full is a copied configuration-comment excerpt, not a raw run result. It is labelled as such on the page.
- The two 26 September Flash-Next rows (`flashnext-fullwindow/`) used another placement than the 15 September Flash-Next row: 40 expert layers requested on CPU instead of 99, and an 8-bit cache. Their 205.5 tokens/s at the default batch is not a re-measurement of the 165.70 row.

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
| `build-records.tsv` | Derived mapping from each original deep response build identifier to its commit |
| `CONFIGURATIONS.md` | Derived per-model command and build map from the archived primary files |
| `NUMBERS.md` | Derived figure-to-field map, rounding and arithmetic |

Exact file inventory follows below. Original request captures and model warmup responses are not included. The generator preserves the synthetic prompt construction. Other tasks from the source collection are outside this package. No internal summaries, session narratives or working manifest are included.

## Redactions

Paths are replaced in full, with a model or shipped-script basename retained where useful. All fixed bound addresses and port values become `<LOCAL>`, including loopback. Process identifiers become `<REDACTED>`. Serving aliases become public model names. JSON `id` and `system_fingerprint` fields are removed; the latter’s commit component is separately documented as build provenance. The complete private-context comment block was deleted, not rephrased. Scripts with placeholders are archival evidence, not ready-to-run files.

Counts below are substitutions or deleted fields/lines in the primary copied files. Derived documents reuse the already-redacted material and are not counted again. Original timing values and relative-clock log prefixes were preserved.

| Redaction | Count |
|---|---|
| internal storage label removed | 1 |
| internal paths replaced | 56 |
| addresses replaced | 51 |
| port arguments replaced | 23 |
| comment ports replaced | 10 |
| positional ports replaced | 10 |
| process identifiers replaced | 48 |
| serving aliases replaced | 23 |
| punctuation normalized | 17 |
| synthetic punctuation escaped (same generated text) | 3 |
| private-context comment lines deleted | 4 |
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
