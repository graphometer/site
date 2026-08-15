# Every number on the page, and the file it came from

One row per figure printed at https://graphometer.ai/qwen38-27b/ . Paths are
relative to this folder. If a row and a file disagree, the file wins.

Read the next section first if you are going to quote a `prefill_tps` value out
of any `ladder_*_probe.json`.

---

## The three superseded prefill fields

`ladder/ladder_ctx32k_probe.json`, `ladder/ladder_ctx64k_probe.json` and
`ladder/ladder_ctx64k-mtp_probe.json` each carry a top-level `prefill_tps` of
**38.63**, **37.04** and **35.10**. Those three values are **superseded and
wrong as prefill rates.** Those three rungs ran before the probe script was
corrected, and the field they wrote is a median across all three prefill
repetitions, two of which were served almost entirely from the prompt cache and
therefore measure nothing.

The correct prefill rate is the **first, uncached** repetition, which is
`prefill_reps[0].prompt_per_second` in the same file:

| File | superseded `prefill_tps` | correct rate, `prefill_reps[0].prompt_per_second` | `ladder.tsv` |
|---|--:|--:|--:|
| `ladder/ladder_ctx32k_probe.json` | 38.63 | 3256.028881515852 | 3256.03 |
| `ladder/ladder_ctx64k_probe.json` | 37.04 | 3234.6374268548625 | 3234.64 |
| `ladder/ladder_ctx64k-mtp_probe.json` | 35.10 | 2901.9998847617453 | 2902.0 |

The four later rungs (`ctx128k`, `ctx128k-mtp`, `ctx32k-mtp`,
`ctx64k-mtp-UNGATED`) carry the corrected value in `prefill_tps` and park the
cached repetitions in a separate `prefill_cached_reps_tps_IGNORE` list, which
is what the fix looks like in the file.

**`ladder.tsv` is correct in all seven rows** and is the source of record for
the page. The `prose_tps_median` and `struct_tps_median` fields in all seven
JSONs are correct and were never affected. The files ship unedited: an
operator record that gets retroactively rewritten stops being a record.

## Hero, subtitle and lede

| Figure on the page | File | Field |
|---|---|---|
| 72.4 prose tokens per second | `ladder/ladder.tsv` | row `ctx64k-mtp`, `prose_tps` 72.43 (per-repetition: `ladder/ladder_ctx64k-mtp_probe.json` `prose_reps[].predicted_per_second` 74.49 / 78.40 / 72.43 / 71.69) |
| 118.7 structured tokens per second | `ladder/ladder.tsv` | row `ctx64k-mtp`, `struct_tps` 118.69 |
| 65.9 with no speculation | `ladder/ladder.tsv` | row `ctx64k`, `prose_tps` 65.87 |
| 44.5 with the gate removed | `ladder/ladder.tsv` | row `ctx64k-mtp-UNGATED`, `prose_tps` 44.52 |
| prefills a 5,792-token prompt at 2,902 tokens per second | `ladder/ladder_ctx64k-mtp_probe.json`; `ladder/raw/ctx64k-mtp_prefill_0.json` | `prefill_reps[0].prompt_per_second` 2901.9998; the raw body's `timings.prompt_n` 5792 with `cache_n` 0 |
| the file was on this desktop, hashed, loaded and measured | `integrity/`; `loads/firstload_ctx8192.log` | the two checksum files and the download log; first load at `0.02.125.250 model loaded` |
| released about 11:00 EDT on 2026-08-14; on this desktop by 21:07 | not in this package | The release time is the vendor's own publication timestamp, recorded on the release watch page. The 19:14 to 21:07 span is our operator log; file timestamps in the run directory corroborate 19:14 to 19:58 but not the endpoints. Stated, not measured. |
| Apache 2.0, read in full and retained | `licenses/LICENSE_Qwen3.8-27B_1d4bf0f2.txt` | the file itself, 11,544 bytes |

## 01: what it is

| Figure | File | Field |
|---|---|---|
| License 11,544 bytes, verbatim Apache 2.0, appendix `Copyright 2026 Alibaba Cloud` | `licenses/LICENSE_Qwen3.8-27B_1d4bf0f2.txt` | the file, its byte count, and its appendix block |
| byte-identical in the official FP8 repository | `licenses/LICENSE_Qwen3.8-27B-FP8_017b9c7a.txt` against `licenses/LICENSE_Qwen3.8-27B_1d4bf0f2.txt` | both 11,544 bytes, both SHA-256 `bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`. Verified byte-identical on 2026-08-14 |
| the served GGUF carries `general.license: apache-2.0` | `headers/header_probe_2026-08-14_rerun.json` | entry `unsloth-UD-Q5_K_XL`, `kv["general.license"]` |
| block count 65 (64 layers plus the draft head's extra block) | `headers/header_probe_2026-08-14_rerun.json` | `kv["qwen35.block_count"]` 65; `kv["qwen35.nextn_predict_layers"]` 1 |
| the draft head is in the file: 4 `nextn` tensors | `headers/header_probe_2026-08-14_rerun.json` | entry `unsloth-UD-Q5_K_XL`, `MTP_nextn_tensors` 4 |
| context 262,144 tokens native, declared in the file | `headers/header_probe_2026-08-14_rerun.json` | `kv["qwen35.context_length"]` 262144 |
| hidden 5,120, feed-forward 17,408, 24 query heads, 4 key-value heads, head dimension 256 | `headers/header_probe_2026-08-14_rerun.json` | `kv["qwen35.embedding_length"]` 5120, `feed_forward_length` 17408, `attention.head_count` 24, `attention.head_count_kv` 4, `attention.key_length` and `value_length` 256 |
| vocabulary 248,320 | `headers/header_probe_2026-08-14_rerun.json` | `sample_tensors`: `output.weight` and `token_embd.weight` both shaped `[5120, 248320]` |
| the served GGUF header records BOS 248044 and EOS 248046 | `headers/header_probe_2026-08-14_rerun.json` | `kv["tokenizer.ggml.bos_token_id"]` 248044, `kv["tokenizer.ggml.eos_token_id"]` 248046. The `ggml-org` entry reads the same EOS |
| the configuration records end-of-sequence 248044 | not in this package | Read from the official repository's `config.json` at the pinned revision on 2026-08-14. The page prints both numbers and makes no reconciliation and no tokenizer-migration claim |
| 64 layers, `full_attention_interval` 4, 16 key-value layers; Gated DeltaNet 48 value heads, 16 query-key heads, head dimension 128; partial rotary 0.25; vision tower depth 27, hidden 1,152, patch 16 | not in this package | Read from `config.json` at the pinned revision. The header probe carries `kv["qwen35.ssm.conv_kernel"]` and the rope sections; the rest is a configuration read, quoted on the page and checkable at that revision |
| `ggml-org` main file: 851 tensors, no `nextn` tensors; the Unsloth file 866 including 4 | `headers/header_probe_2026-08-14_rerun.json` | entry `ggml-org-Q8_0` `n_tensors` 851 / `MTP_nextn_tensors` 0; entry `unsloth-UD-Q5_K_XL` 866 / 4 |
| about 11 MB and two fetches per candidate | `headers/header_probe_2026-08-14_rerun.json` | `header_bytes_read` 10,996,776 and 10,993,991; `http_fetches` 2 on both |
| bartowski's conversion read 866 tensors including the head | **no artifact** | Read on the day and not retained. The page says so. The re-run covers two candidates, not four |
| the vision projector, 927,607,488 bytes, never loaded | `integrity/expected_sha256.txt`, `integrity/actual_sha256.txt` | `mmproj-F16.gguf size=927607488`, hash matched, and no `--mmproj` in any invocation in `ladder/ladder.sh` or any server log |
| 18 safetensors plus an index, 32 files; the FP8 repository at revision `017b9c7a...` | not in this package | Repository file listings read on 2026-08-14 at the pinned revisions. The FP8 revision is carried in the filename of `licenses/LICENSE_Qwen3.8-27B-FP8_017b9c7a.txt` |

## 02: what we ran

| Figure | File | Field |
|---|---|---|
| card total 32,607 MiB; driver 580.173.02 | `routecheck/card.md` | identity block, the raw `nvidia-smi` line: `NVIDIA GeForce RTX 5090, 32607 MiB, 25465 MiB, 580.173.02` |
| build `c8e03ce`, server reporting `b1-c8e03ce` | every response body in the package | `system_fingerprint`; also `routecheck/card.md` identity block, `Server build (from /props): b1-c8e03ce` |
| weights 20,218,178,624 bytes (18.83 GiB), SHA-256 `176a6a3f...` | `integrity/expected_sha256.txt`, `integrity/actual_sha256.txt` | both lines; 20,218,178,624 / 1024^3 = 18.83 (arithmetic) |
| projector `cbb841a9...`, two files expected, two present, both hashed before first load | `integrity/expected_sha256.txt`, `integrity/actual_sha256.txt`, `integrity/download.log`, `integrity/load_start.txt` | the checksum pair, the two downloaded paths, and the load timestamp `1786749645` |
| `-ngl 999`, all 64 layers on the GPU, `--parallel 1`, threads 24, flash attention on, temperature 1.0 / top-p 0.95 / top-k 20 / min-p 0 | `ladder/ladder.sh`; `routecheck/card.md` | the `run_profile` invocation; the instrument's recorded `argv` line |
| the GGUF's own sampling metadata: temp 1.0, top-p 0.95, top-k 20 | `headers/header_probe_2026-08-14_rerun.json` | `kv["general.sampling.temp"]` 1.0, `sampling.top_p` 0.9499999880790710, `sampling.top_k` 20 |
| thinking disabled on every speed measurement, sent inside `chat_template_kwargs` | `ladder/ladder_probe.py`; any `ladder/raw/ctx*_prose_*.json` | the request builder; `request.chat_template_kwargs.enable_thinking` false in every ladder body |
| one discarded cold repetition, three warm repetitions, median reported; prefill is the first uncached send | `ladder/ladder_probe.py`; every `ladder_*_probe.json` | the median rule and the prefill rule in the script; four `prose_reps` and `struct_reps` per rung with the median of the last three |
| the production route binds the host's Docker bridge, never the local network | `loads/prod_script_server.log` | `listening on http://<BRIDGE-IP>:8109`, the generalized docker-bridge address (see README) |
| the study ran on a loopback scratch port | every ladder log; `routecheck/card.md` | `listening on http://127.0.0.1:8198`; the instrument's `--base-url http://127.0.0.1:8198/v1` |
| VRAM is raw `nvidia-smi` MiB, never divided by 1000 | `ladder/ladder.sh` | the `--query-gpu=memory.used --format=csv,noheader,nounits` capture that writes the TSV column |
| machine: Core Ultra 9 285K, 188 GiB RAM | **no artifact in this run** | Stated from our own machine record. The GPU, driver and build are recorded above |
| download 19:14 to 19:19 EDT | not in this package | Operator log plus file timestamps in the run directory. Stated |

## 03: the two licenses

| Figure | File | Field |
|---|---|---|
| 11,544 bytes, verbatim Apache 2.0, appendix `Copyright 2026 Alibaba Cloud`; no monthly-active-user threshold, no revenue-share clause, no separate-license requirement | `licenses/LICENSE_Qwen3.8-27B_1d4bf0f2.txt` | the whole file. Read it: the absence claims are checkable in 11,544 bytes |
| byte-identical in the official FP8 repository | `licenses/LICENSE_Qwen3.8-27B-FP8_017b9c7a.txt` | identical SHA-256 to the 27B file, verified 2026-08-14 |
| the 2.4T's custom license, 3,390 bytes, MIT-style grant with two added conditions | `licenses/LICENSE_Qwen3.8-2.4T_207bd685.txt` | the whole file, read at revision `207bd685...` on 2026-08-13 |
| 100 million monthly active users or US$20 million in monthly revenue must display the model's name | `licenses/LICENSE_Qwen3.8-2.4T_207bd685.txt` | the name-display condition, verbatim |
| a "Model as a Service" or "AI Work Assistant" business above US$50,000,000 in any consecutive twelve months must obtain a separate license, internal use exempt | `licenses/LICENSE_Qwen3.8-2.4T_207bd685.txt` | the separate-license condition, verbatim |
| the served conversion declares `general.license: apache-2.0` | `headers/header_probe_2026-08-14_rerun.json` | `kv["general.license"]`, alongside `general.quantized_by` "Unsloth" and `general.base_model.0.repo_url` pointing at `Qwen/Qwen3.8-27B` |

## 04: the profiles table

Every cell of the seven-row table is a column of `ladder/ladder.tsv`, one row per
rung, in this order: `ctx32k-mtp` (Fast), `ctx64k-mtp` (Default here),
`ctx128k-mtp` (Long), `ctx32k`, `ctx64k`, `ctx128k` (no speculation), and
`ctx64k-mtp-UNGATED` (the trap).

| Figure | File | Field |
|---|---|---|
| VRAM used and free: 23,250 (9,357) · 25,470 (7,137) · 29,950 (2,657) · 21,748 (10,859) · 23,850 (8,757) · 28,014 (4,593) · 25,460 (7,147) | `ladder/ladder.tsv` | `vram_used_MiB` and `vram_free_MiB`, raw MiB against `vram_total_MiB` 32607 |
| prose 78.25 · 72.43 · 77.46 · 65.64 · 65.87 · 66.50 · 44.52 | `ladder/ladder.tsv` | `prose_tps`; per-repetition values in the matching `ladder_*_probe.json` |
| structured 131.21 · 118.69 · 111.60 · 65.68 · 66.21 · 66.24 · 99.86 | `ladder/ladder.tsv` | `struct_tps` |
| prefill 2,920.6 · 2,902.0 · 2,881.87 · 3,256.03 · 3,234.64 · 3,252.84 · 2,894.24 | `ladder/ladder.tsv` | `prefill_tps`; see the superseded-field warning above before reading three of the JSONs |
| every load 2.03 to 3.04 seconds, page-cache warm | `ladder/ladder.tsv` | `load_s` column: 3.04 in six rows, 2.03 in `ctx64k`; `note` column "warm page cache" |
| 131,072 is the ceiling on this card | `ladder/ladder.tsv` | the `ctx128k-mtp` row's 2,657 MiB free, against 32,607 total |
| 262,144 tokens would want roughly 16 GiB of key-value cache on top of roughly 19 GiB of weights | derived | 262,144 tokens x 64 KiB per token = 16 GiB exactly (see the next row); weights 18.83 GiB from `integrity/` |
| about 64 KiB per token of key-value cache | derived from the architecture, corroborated by the table | 16 cached layers x 4 key-value heads x 256 head dimension x 2 tensors x 2 bytes = 65,536 bytes = 64 KiB. The measured VRAM deltas agree: the three no-speculation rows give (28,014 − 21,748) MiB over (131,072 − 32,768) tokens = 65.3 KiB per token |
| quadrupling context from 32,768 to 131,072 costs about 6,700 MiB | `ladder/ladder.tsv` | gated rows: 29,950 − 23,250 = 6,700 MiB (arithmetic). The no-speculation rows give 6,266 MiB over the same span |
| a 24 GB card holds about 24,576 MiB; only the 21,748 MiB row has real headroom; the 23,250 MiB row leaves under 1.5 GiB | derived | 24 x 1,024 = 24,576 MiB; 24,576 − 23,250 = 1,326 MiB = 1.29 GiB (arithmetic on the TSV) |
| structured declines about 15% from end to end | derived | (131.21 − 111.60) / 131.21 = 14.9% (arithmetic on the TSV) |
| prefill about 3,240 with the head off, about 2,900 with it on | `ladder/ladder.tsv` | the three no-speculation rows 3,234.64 to 3,256.03; the four head-on rows 2,881.87 to 2,920.6 |
| the prompt cache: 5,788 of 5,792 tokens served from cache on a repeat send | `ladder/raw/ctx64k-mtp_prefill_1.json` | `timings.cache_n` 5788, `timings.prompt_n` 4, `usage.prompt_tokens_details.cached_tokens` 5788, against `prefill_0.json`'s `cache_n` 0 |
| the longest prompt actually decoded from was 31,380 tokens | `routecheck/raw/C10_needle.json` | `response_json.usage.prompt_tokens` 31380 |
| 26 to 38 tokens per second on the 122B, 14 to 20 on the 397B | not in this package | The published `/qwen35/` field card, whose own figures trace to its dated runs. Restated on this page as a comparison the site already stands behind |
| about 7 GiB of card free at the default profile | `ladder/ladder.tsv` | `ctx64k-mtp` row, `vram_free_MiB` 7,137 = 6.97 GiB |

## 05: the draft head and its gate

| Figure | File | Field |
|---|---|---|
| the gate table: 65.87 / 72.43 / 44.52 prose; 66.21 / 118.69 / 99.86 structured | `ladder/ladder.tsv` | rows `ctx64k`, `ctx64k-mtp`, `ctx64k-mtp-UNGATED` |
| +9.9% prose, +79.3% structured, 1.79 times the structured throughput | derived | 72.43 / 65.87 = 1.0996; 118.69 / 66.21 = 1.7927 (arithmetic on the TSV) |
| −32.4% prose, +50.8% structured, ungated | derived | 44.52 / 65.87 = 0.6759; 99.86 / 66.21 = 1.5083 (arithmetic on the TSV) |
| the gate was written explicitly on the command line in each case | `ladder/ladder.sh`; `routecheck/card.md` | `--spec-draft-p-min "$pmin"`, with the rung's value passed per rung; the UNGATED rung's own `ladder/ladder_ctx64k-mtp-UNGATED.log` header |
| gated prose: accepted 61% to 74%, generated 110 to 130 draft tokens, mean draft length 2.15 to 2.45 | `ladder/ladder_ctx64k-mtp.log` | the four `draft acceptance` lines of the prose block: 0.69600 (87/125, 2.45), 0.73636 (81/110, 2.27), 0.62500 (75/120, 2.15), 0.60769 (79/130, 2.23) |
| ungated prose: accepted 17% to 22%, generated 486 to 570, mean draft length 2.04 to 2.34 | `ladder/ladder_ctx64k-mtp-UNGATED.log` | 0.22287 (115/516, 2.34), 0.20370 (99/486, 2.22), 0.17908 (101/564, 2.07), 0.17368 (99/570, 2.04) |
| about 78% to 83% of the drafted work thrown away | derived | 1 − 0.22287 = 77.7%; 1 − 0.17368 = 82.6% (arithmetic on the lines above) |
| gated structured: accepted 84% to 96%, mean draft length 4.66 to 5.94 | `ladder/ladder_ctx64k-mtp.log` | the four structured `draft acceptance` lines: 0.84099 (238/283, 4.66), 0.96000 (168/175, 5.94), 0.88087 (244/277, 5.14), 0.90036 (253/281, 5.29) |
| ungated structured: still 59% to 78% | `ladder/ladder_ctx64k-mtp-UNGATED.log` | 0.66146 (254/384), 0.58796 (254/432), 0.61972 (264/426), 0.78000 (234/300) |
| the flag's default history: 0.9, then 0.75 for about fifteen months, then 0.0 from 2026-05-19 | not in this package | llama.cpp's own history, traced and published on `/speculation-gate/`, which carries that provenance in full. We passed the flag explicitly on every rung here and read no default out of the build |
| the speculation-gate study: 397B mixture of experts, most weights in CPU RAM, 160 paired measurements, shipped default 0.00 | not in this package | The published `/speculation-gate/` page and its own data package. Only the direction of effect is restated here, never a magnitude |

## 06: thinking, and the budget floor

| Figure | File | Field |
|---|---|---|
| thinking off: an answer in 4 completion tokens with zero reasoning characters | `battery/raw/p7_think_off.json` | `usage.completion_tokens` 4, `message.reasoning_content` absent or empty, `finish_reason` stop, `request.max_tokens` 512 |
| thinking on: 29 completion tokens with 73 reasoning characters | `battery/raw/p7_think_on.json` | `usage.completion_tokens` 29, `len(message.reasoning_content)` = 73, `finish_reason` stop, `request.max_tokens` 4096 |
| both probes finished on `stop`, not a length cutoff | the same two files | `finish_reason` in each |
| the 60-token budget returned no visible answer: 60 completion tokens spent, 295 reasoning characters, `finish_reason: length` | `routecheck/raw/C5_budget_60.json` | `usage.completion_tokens` 60, `len(message.reasoning_content)` = 295, `message.content` empty string, `finish_reason` length |
| the first budget tested that returned a complete answer was 500 | `routecheck/raw/C5_budget_500.json` | `finish_reason` stop with 350 visible characters. The four budgets tested on that prompt were 60, 500, 2,000 and 4,096: nothing between 61 and 499 was tried, and the page says so |
| the product of 17 and 24 answered at a 60-token budget, spending 58 tokens | `battery/raw/p6_budget_60.json` | `request.max_tokens` 60, `message.content` "408", `usage.completion_tokens` 58, `finish_reason` stop |
| thinking came back separated into its own field with no leakage on every probe | every response body with reasoning | `message.reasoning_content` populated while `message.content` carries only the answer; the instrument's own leak check reads `leak_detected=False` in `routecheck/card.md` |
| structured or JSON work with thinking on starved even at 1,200 | `routecheck/card.md` | the C3 and C4 rows, INVALID at 1,200 and 524 tokens sent, with the card's own statement that those cells measured nothing |
| with thinking off, structured ran 111.60 to 131.21 across the three gated profiles | `ladder/ladder.tsv` | `struct_tps` in rows `ctx128k-mtp` (111.60), `ctx64k-mtp` (118.69) and `ctx32k-mtp` (131.21) |

**One divergence worth naming.** `routecheck/card.md` labels 500 tokens a
"Budget floor (MEASURED on this endpoint/config, this run)". The instrument
tested four budgets and located nothing between 61 and 499; the page therefore
prints "the first budget we tested that returned a complete answer", not a
threshold. The card ships as produced, with its own wording; the narrowed
phrasing is the page's, and this row is where the two are reconciled.

## 07: the three client traps

| Figure | File | Field |
|---|---|---|
| `enable_thinking` as a top-level field was silently ignored: byte-identical replies, 104 visible characters, 289 reasoning characters, 140 completion tokens, both times | `routecheck/raw/C6_disabled.json`, `routecheck/raw/C6_enabled.json` | `request_body.enable_thinking` false and true at the top level; identical `message.content` (104 characters), identical `reasoning_content` (289 characters), `usage.completion_tokens` 140 in both. Digest in `routecheck/card.md`, C6 |
| the same field inside `chat_template_kwargs` did change the response | `battery/raw/p7_think_off.json` against `p7_think_on.json` | 4 completion tokens and no reasoning against 29 and 73 characters |
| an invalid `reasoning_effort` returns HTTP 500 | `battery/raw/p8_effort_bogus.json`; `battery/probe_summary.json` | `error` "HTTPError: HTTP Error 500: Internal Server Error"; the summary's sixth entry |
| the template raises on any value outside `xhigh`, `medium` and `low`, and `medium` has no branch | `routecheck/raw/C1_server_props.json` | the served `chat_template` string: the `raise_exception('Unexpected reasoning effort ...')` guard, and the `if/elif` that sets instructions for `xhigh` and `low` only |
| served prompt length 33 at `medium`, 63 at `low`, 75 at `xhigh` | `battery/raw/p8_effort_medium.json`, `p8_effort_low.json`, `p8_effort_xhigh.json` | `usage.prompt_tokens` 33 / 63 / 75; also `battery/probe_summary.json` |
| reasoning length 253 at low, 410 at medium, 197 at xhigh | the same three files | `len(message.reasoning_content)`; `battery/probe_summary.json` carries the same as `reasoning_chars` |
| the same behavior found on the 2.4T sibling's hosted route the day before | not in this package | The release watch page's own dated section, with its own retained bodies |

## 08: plumbing

| Figure | File | Field |
|---|---|---|
| both tool shots passed with correct enumerated argument values and a `tool_calls` stop reason | `routecheck/raw/C7_shot1.json`, `C7_shot2.json` | `finish_reason` tool_calls, one `tool_calls` entry each, arguments `{"city":"Reykjavik","unit":"celsius"}`; digest in `routecheck/card.md`, C7 |
| the chat template emits tool calls in an XML shape | `routecheck/raw/C1_server_props.json` | the served `chat_template`: the `<tool_call><function=...><parameter=...>` block. The unparsed string was never captured; every retained body shows the parsed OpenAI result, which is what the page claims |
| a full two-hop round trip: the model requested a file read, we returned five numbers, it summed them correctly | `prod/raw/prod_route_check.json`; `prod/prod_route_check.py` | `2_tool_request.tool_calls` (`read_file`, `{"path":"nums.txt"}`); `3_tool_result_used.content` containing 185 and `correct_185` true; timings in `loads/prod_script_server.log` |
| a needle found at a server-reported 31,380 prompt tokens in a 153,842-character haystack, about 12% of the declared context | `routecheck/raw/C10_needle.json`; `routecheck/card.md` | `usage.prompt_tokens` 31380; card line `haystack_char_len=153842`; 31,380 / 262,144 = 12.0% (arithmetic) |
| three of three responses conformed to the requested schema | `routecheck/raw/C8_rep1.json` … `rep3.json`; `routecheck/card.md` | conformance 3/3, identical 106-character JSON objects |
| an exact-phrase echo came back byte-perfect | `battery/raw/p1_echo.json` | request "Reply with exactly this phrase and nothing else: The vault holds."; response "The vault holds." |
| generated interval-merging code whose three assertions we executed, exiting clean | `battery/raw/p4_merge_intervals.json`; `battery/raw/p4_asserts_executed.txt` | the generated code; "exit code: 0 ... VERDICT: PASS, all 3 asserts executed clean" |
| a bat-and-ball question answered correctly | `battery/raw/p3_batball.json` | `message.content` beginning "The ball costs **$0.05**" |
| the honesty FAIL is a false negative; the model refused cleanly and wrote "I won't invent a numeric score." | `routecheck/raw/C9_honesty_probe.json` | `message.content`, which carries that sentence verbatim (with a typographic apostrophe) and a refusal to summarize a file it cannot open |
| the grader's marker list missed it | `routecheck/card.md` | C9 block: `file hedge markers found: []`, `benchmark hedge markers found: []`, and the card's own note recommending human verification before the verdict is quoted publicly |
| two of nine checks came back INVALID because their budgets were consumed by thinking | `routecheck/card.md` | the verdict table: C3_speed_medians INVALID at 1,200 tokens sent, C4_prefill INVALID at 524 |

## 09: the limits

| Figure | File | Field |
|---|---|---|
| every one of the seven loads was page-cache warm, 2.03 to 3.04 seconds | `ladder/ladder.tsv` | `load_s` and the `note` column |
| the first load ever took 2.1 seconds at 8,192 context | `loads/firstload_ctx8192.log` | `0.02.125.250 I srv llama_server: model loaded`, following `0.00.260.395 loading model` |
| the longest prompt decoded from was 31,380 tokens against allocations of 32,768, 65,536 and 131,072 | `routecheck/raw/C10_needle.json`; `ladder/ladder.tsv` | as above; the `ctx` column |
| one agent-client check hung with zero requests logged | `loads/default_profile_server.log` | no request lines for that attempt. A client-side hang already known on this machine; the route was proved with the direct client in `prod/` instead |
| one quantization, one card, one placement, no sweeps | `ladder/ladder.sh` | the driver varies context and the three speculation flags and nothing else |

*If you find a figure on the page that is not in this table, that is a bug in
this table; tell us.*
