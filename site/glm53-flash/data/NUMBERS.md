# Number map

## Scope rules

The installed launcher falls back to micro-batch 1024 above a 131,072-token window. That setting was measured only through 47,992 prompt tokens. The 230,039-token read used micro-batch 2048, which is not the installed setting.

The audition's 20.5-second value is whole-request wall time. It is not first-token latency.

Each row below maps one quantitative figure printed in the page content. Repeated uses of the same figure share a row only when their scope and evidence are identical. Package fields that the page does not print are not listed as page figures.

## Model, files and machine

| Page figure | Scope | File and field |
|---|---|---|
| 4 shards | Tested GGUF file set | `gguf-header.txt`, recorded shard bytes 1 through 4 |
| 137.404 GiB | File-set size, arithmetic | `gguf-header.txt`, total bytes divided by 1,073,741,824 |
| 42 expert blocks | Installed launcher and 21 and 26 September CPU expert placement | `installed-profile.txt`, `n_cpu_moe` |
| 46 blocks | GGUF metadata | `gguf-header.txt`, `glm5next.block_count` |
| 288 experts | GGUF metadata | `gguf-header.txt`, `glm5next.expert_count` |
| 8 selected experts | GGUF metadata | `gguf-header.txt`, `glm5next.expert_used_count` |
| 1,048,576 tokens | Native context metadata, not a useful-context measurement | `gguf-header.txt`, `glm5next.context_length` |
| 147,535,921,955 bytes | Recorded shard-size sum | `gguf-header.txt`, `total` |
| file type 12 | GGUF header value | `gguf-header.txt`, `general.file_type` |
| 188 GiB | Recorded system memory | `machine.txt`, memory field |
| Intel Core Ultra 9 285K | Processor specification | `machine.txt`, processor field |
| 1 RTX 5090 | Card count and model | `machine.txt`, card field |
| 32,607 MiB | Reported card capacity | `card-capacity.txt` |

## Audition and launch profiles

| Page figure | Scope | File and field |
|---|---|---|
| 16 September 2026 | Audition date | `audition.tsv`, `date` |
| 131,072 tokens | Audition context allocation | `audition.tsv`, `n_ctx` |
| 999 GPU layers | Audition and later launch setting | `audition-profile.txt`, `n_gpu_layers`; `installed-profile.txt`, `n_gpu_layers` |
| 75.48 t/s | Audition deep-read prompt processing | `audition.tsv`, `deep_prefill_tps` |
| 9.58 t/s | Audition short-answer decode | `audition.tsv`, `decode_tps` |
| temperature 0 | Audition and long-window code requests | `request-settings.txt` |
| 400-token cap | Audition short-answer cap | `request-settings.txt` |
| 181 generated tokens | Audition short answer | `audition-short.json`, `timings.predicted_n` |
| 38 prompt tokens | Audition short request total | `audition-short.json`, `usage.prompt_tokens` |
| 29 evaluated tokens | Audition short prompt evaluation | `audition-short.json`, `timings.prompt_n` |
| 9 cached tokens | Audition short prompt cache | `audition-short.json`, `usage.prompt_tokens_details.cached_tokens` |
| 18.89 t/s | Audition short prompt processing, rounded | `audition-short.json`, `timings.prompt_per_second` |
| 20.5 s | Audition whole-request wall time | `audition.tsv`, `request_wall_s` |
| 120,979 evaluated tokens | Audition deep read | `audition.tsv`, `deep_prompt_tokens` |
| 58 generated tokens | Audition deep answer | `audition-deep.json`, `timings.predicted_n` |
| 8.71 t/s | Audition deep-answer decode, rounded | `audition-deep.json`, `timings.predicted_per_second` |
| 3 planted codes | Audition deep answer | `audition.tsv`, `codes_hit` |
| 21 September 2026 | Batch-sweep date and later-placement scope | `batch-sweep.txt`, recorded date |
| 26 September 2026 | Long-window date and later-placement scope | `full-window.jsonl`, `date` |
| 1 slot | Later server concurrency | `installed-profile.txt`, `parallel` |
| 1 request at a time | Measurement concurrency | `batch-sweep.txt`; `full-window-loads.txt` |
| 24 threads | Later server thread setting | `installed-profile.txt`, `threads` and `threads_batch` |
| 1 run per serving configuration | Repetition count | Recorded measurement design described by `batch-sweep.txt` and `full-window-loads.txt` |
| 1,024-token cap | Long-window code requests | `request-settings.txt` |
| seed 1 | Long-window code requests | `request-settings.txt` |
| temperature 0.7 | Long-window letter requests | `request-settings.txt` |
| seed 7 | Long-window letter requests | `request-settings.txt` |
| 1,200-token cap | Long-window letter requests | `request-settings.txt` |

## Window settings and load boundaries

| Page figure | Scope | File and field |
|---|---|---|
| 131,072 tokens | Measured smaller allocation and launcher threshold | `full-window-loads.txt`; `installed-profile.txt` |
| batch 4096 | Explicit measured and installed batch setting | `full-window-loads.txt`; `installed-profile.txt` |
| micro-batch 4096 | Smaller-window setting | `batch-sweep.txt`; `full-window-loads.txt` |
| 48,168 tokens | Smaller-window long read | `batch-sweep.txt`, fourth request on batch 4096 and micro-batch 4096 |
| 425.1 t/s | Same smaller-window long read | `batch-sweep.txt`, `prefill_tps` |
| 29,872 MiB | Peak for batch 4096 and micro-batch 4096 load | `batch-sweep.txt`, `peak_mib` |
| micro-batch 8192 | Smaller-window failed load | `batch-sweep.txt`, failed configuration |
| 262,144 tokens | Measured larger allocation | `full-window-loads.txt`, `ctx` |
| micro-batch 1024 | Installed larger-window fallback and measured headroom setting | `installed-profile.txt`; `full-window-loads.txt` |
| 47,992 tokens | Deepest measured prompt on the larger-window micro-batch-1024 setting | `full-window.jsonl`, matching read row |
| 142.6 t/s | Same larger-window micro-batch-1024 read | `full-window.jsonl`, `prefill_tps` |
| 29,261 MiB | Same setting's peak | `full-window-loads.txt`, `peak_mib` |
| micro-batch 2048 | Separate larger-window deep-read setting | `full-window-loads.txt` |
| 230,039 tokens | Deepest measured prompt, micro-batch 2048 only | `full-window.jsonl`, matching read row |
| 211.9 t/s | Same deepest read | `full-window.jsonl`, `prefill_tps` |
| 3 of 3 codes | Same deepest read | `full-window.jsonl`, `codes3_hits` |
| 31,951 MiB | Same setting's peak | `full-window-loads.txt`, `peak_mib` |
| 13,281.37 MiB | Refused compute allocation at larger-window micro-batch 4096 | `full-window-loads.txt`, `failed_compute_allocation_mib` |

## Long-window request rows

Each letter reused the cached document from the paired read at that target depth. The paired reads evaluated 20,065, 47,992, 100,003, or 230,039 tokens. On a letter row, Prompt evaluated is only the uncached tail, and the prompt-processing rate is the rate for that tail.

| Page figure | Scope | File and field |
|---|---|---|
| 47,992 evaluated tokens | 131,072, micro-batch 4096, code at 48,000 target depth | `full-window.jsonl`, row 3 `prompt_n` |
| 404.9 t/s | Same code request | `full-window.jsonl`, row 3 `prefill_tps` |
| 98 generated tokens | Same code request | `full-window.jsonl`, row 3 `predicted_n` |
| 9.84 t/s | Same code request | `full-window.jsonl`, row 3 `decode_tps` |
| 1 visible word | Same code request | `full-window.jsonl`, row 3 `answer_words` |
| 20,000 target depth | Cached-document letter runs across the three successful serving settings | `full-window.jsonl`, rows 2, 8 and 12 `depth_target` |
| 20,065 evaluated tokens | Paired reads for cached 20,000-token documents | `full-window.jsonl`, rows 1, 7 and 11 `prompt_n` |
| 4,148 evaluated tokens | Uncached tail for each 131,072 letter request | `full-window.jsonl`, rows 2, 4 and 6 `prompt_n` |
| 312.1 t/s | Uncached-tail prompt processing for first 131,072 letter | `full-window.jsonl`, row 2 `prefill_tps` |
| 1,200 generated tokens | Each displayed 131,072 cached-document letter request | `full-window.jsonl`, rows 2, 4 and 6 `predicted_n` |
| 10.09 t/s | First 131,072 letter decode | `full-window.jsonl`, row 2 `decode_tps` |
| 0 visible words | Each of the three 131,072 letters | `full-window.jsonl`, rows 2, 4 and 6 `answer_words` |
| 48,000 target depth | Cached-document letter runs across the three successful serving settings | `full-window.jsonl`, rows 4, 10 and 14 `depth_target` |
| 47,992 evaluated tokens | Paired reads for cached 48,000-token documents | `full-window.jsonl`, rows 3, 9 and 13 `prompt_n` |
| 294.8 t/s | Uncached-tail prompt processing for second 131,072 letter | `full-window.jsonl`, row 4 `prefill_tps` |
| 9.85 t/s | Second 131,072 letter decode | `full-window.jsonl`, row 4 `decode_tps` |
| 100,000 target depth | Third 131,072 cached-document letter run and omitted micro-batch-2048 letter | `full-window.jsonl`, rows 6 and 16 `depth_target` |
| 100,003 evaluated tokens | Paired reads for cached 100,000-token documents | `full-window.jsonl`, rows 5 and 15 `prompt_n` |
| 260.9 t/s | Uncached-tail prompt processing for third 131,072 letter | `full-window.jsonl`, row 6 `prefill_tps` |
| 9.51 t/s | Third 131,072 letter decode | `full-window.jsonl`, row 6 `decode_tps` |
| 125 generated tokens | 262,144, micro-batch 1024, code at 48,000 target depth | `full-window.jsonl`, row 9 `predicted_n` |
| 10.02 t/s | Same code request | `full-window.jsonl`, row 9 `decode_tps` |
| 1 visible word | Same code request | `full-window.jsonl`, row 9 `answer_words` |
| 1,080 evaluated tokens | Uncached tail for both micro-batch-1024 letter requests | `full-window.jsonl`, rows 8 and 10 `prompt_n` |
| 97.0 t/s | Uncached-tail rate for micro-batch-1024 letter on cached 20,000-token document | `full-window.jsonl`, row 8 `prefill_tps` |
| 10.22 t/s | Same letter decode | `full-window.jsonl`, row 8 `decode_tps` |
| 0 visible words | Same letter result | `full-window.jsonl`, row 8 `answer_words` |
| 95.3 t/s | Uncached-tail rate for micro-batch-1024 letter on cached 48,000-token document | `full-window.jsonl`, row 10 `prefill_tps` |
| 729 generated tokens | Same successful letter | `full-window.jsonl`, row 10 `predicted_n` |
| 9.98 t/s | Same successful letter decode | `full-window.jsonl`, row 10 `decode_tps` |
| 351 visible words | Same successful letter | `full-window.jsonl`, row 10 `answer_words` |
| 102 visible words | Omitted micro-batch-2048 letter on cached 20,000-token document; reached the 1,200-token cap | `full-window.jsonl`, row 12 `answer_words` and `predicted_n` |
| 119 visible words | Omitted micro-batch-2048 letter on cached 48,000-token document; reached the 1,200-token cap | `full-window.jsonl`, row 14 `answer_words` and `predicted_n` |
| 337 visible words | Omitted finished micro-batch-2048 letter on cached 100,000-token document | `full-window.jsonl`, row 16 `answer_words` and `predicted_n` |
| 230,000 target depth | Deepest micro-batch-2048 code and letter pair | `full-window.jsonl`, rows 17 and 18 `depth_target` |
| 230,039 evaluated tokens | Paired read for the cached 230,000-token document | `full-window.jsonl`, row 17 `prompt_n` |
| 231 generated tokens | Deepest code read | `full-window.jsonl`, row 17 `predicted_n` |
| 8.88 t/s | Deepest code-read decode | `full-window.jsonl`, row 17 `decode_tps` |
| 3 visible words | Deepest code read | `full-window.jsonl`, row 17 `answer_words` |
| 1,085.744 s | Deepest code prompt processing | `full-window.jsonl`, row 17 `prompt_ms` divided by 1,000 |
| 1,112.9 s | Deepest code whole-request wall time | `full-window.jsonl`, row 17 `wall_s` |
| 617 reasoning characters | Deepest code read | `full-window.jsonl`, row 17 `reasoning_chars` |
| 2,088 evaluated tokens | Uncached tail for letter on cached 230,000-token document | `full-window.jsonl`, row 18 `prompt_n` |
| 131.6 t/s | Same letter's uncached-tail prompt processing | `full-window.jsonl`, row 18 `prefill_tps` |
| 1,200 generated tokens | Same letter | `full-window.jsonl`, row 18 `predicted_n` |
| 9.04 t/s | Same letter decode | `full-window.jsonl`, row 18 `decode_tps` |
| 0 visible words | Same letter result | `full-window.jsonl`, row 18 `answer_words` |
| about 10 t/s | Description of successful 26 September decode rates | `full-window.jsonl`, successful decode rows spanning 8.88 to 10.23 t/s |
| 40 prompts | Separate shipped-setting check | `shipped-profile-stress.json`, `prompts` |
| 36 empty answers | Same shipped-setting check | `shipped-profile-stress.json`, `empty_answers` |
| 0 crashes | Same shipped-setting check | `shipped-profile-stress.json`, `crashes` |

## Batch sweep request order

| Page figure | Scope | File and field |
|---|---|---|
| 2,048 batch | llama.cpp default batch size in recorded load | `batch-sweep.txt`, default setting |
| 512 micro-batch | llama.cpp default micro-batch size in recorded load | `batch-sweep.txt`, default setting |
| first request | Default-load comparison request | `batch-sweep.txt`, `request_order` |
| 24,008 prompt tokens | Default-load first request | `batch-sweep.txt`, `prompt_n` |
| 80.7 t/s | Default-load first request | `batch-sweep.txt`, `prefill_tps` |
| 62 generated tokens | Default-load first request | `batch-sweep.txt`, `predicted_n` |
| 9.22 t/s | Default-load first request decode | `batch-sweep.txt`, `decode_tps` |
| 24,352 MiB | Default-load peak | `batch-sweep.txt`, `peak_mib` |
| 2,048 micro-batch | Intermediate tuned load | `batch-sweep.txt`, setting |
| 48,168 prompt tokens | Intermediate tuned long read | `batch-sweep.txt`, `prompt_n` |
| 252.0 t/s | Intermediate tuned long read | `batch-sweep.txt`, `prefill_tps` |
| 9.21 t/s | Intermediate tuned decode | `batch-sweep.txt`, `decode_tps` |
| 26,763 MiB | Intermediate tuned peak | `batch-sweep.txt`, `peak_mib` |
| third request | Published tuned comparison request | `batch-sweep.txt`, `request_order` |
| 20,333 prompt tokens | Tuned third request | `batch-sweep.txt`, `prompt_n` |
| 446.0 t/s | Tuned third request | `batch-sweep.txt`, `prefill_tps` |
| 60 generated tokens | Tuned third request | `batch-sweep.txt`, `predicted_n` |
| 9.35 t/s | Tuned third request decode | `batch-sweep.txt`, `decode_tps` |
| fourth request | Longer request on same tuned load | `batch-sweep.txt`, `request_order` |
| 310 generated tokens | Tuned fourth request | `batch-sweep.txt`, `predicted_n` |
| 9.12 t/s | Tuned fourth request decode | `batch-sweep.txt`, `decode_tps` |
| 5.5 times | 446.0 divided by 80.7, rounded to one decimal place | Arithmetic from `batch-sweep.txt` |
| batch and micro-batch 8192 | Failed load | `batch-sweep.txt`, failed configuration |

## Output boundary and launcher

| Page figure | Scope | File and field |
|---|---|---|
| 17 September 2026 | Diagnostic and isolated guard date | `diagnostic-failure-result.json`; guard result records |
| 3-sentence answer | Correct answer before visible leakage | `diagnostic-failure-result.json`, visible output |
| 689 generated tokens | Diagnostic failure | `diagnostic-failure-result.json`, generation count |
| second assistant token | Raw generation boundary | `diagnostic-failure.json`, control-token check |
| 4 stop strings | Isolated guard request configuration | `combined-guard-comparison.json`, `profile.request_stop` |
| 254 characters | Clean guard-smoke visible output | `combined-guard-comparison.json`, smoke `visible_chars` |
| 1 isolated fixture | Qualification scope | `combined-guard-comparison.json`, `production_qualified` false |
| 3-part guard test | Smoke, tool call and tool-result legs | `combined-guard-gate.json` |
| 26 September 2026 | Installed launcher inspection date | `installed-profile.txt` |
| temperature 1.0 | Installed fallback | `installed-profile.txt`, `temperature` |
| top-p 0.95 | Installed fallback | `installed-profile.txt`, `top_p` |
| 150 GB | Launcher availability check, recorded as inferred from another deployment and not measured for this model | `installed-profile.txt`, `availability_floor_gb` and `availability_floor_status` |

## Coding snapshot

| Page figure | Scope | File and field |
|---|---|---|
| 4 tasks | Coding-trial run count | `coding-totals.csv`, task rows A through D |
| 387 of 400 | Coding-trial total | `coding-totals.csv`, total row |
| 6,058 seconds | Coding-trial sum of task wall times | `coding-totals.csv`, total row `wall_seconds` |
| 60 of 60 | Mechanical score on each task | `coding-totals.csv`, task rows |
| 34 of 40 | Task A blind judgment | `coding-totals.csv`, task A |
| 39 of 40 | Task B blind judgment | `coding-totals.csv`, task B |
| 37 of 40 | Task C blind judgment | `coding-totals.csv`, task C |
| 37 of 40 | Task D blind judgment | `coding-totals.csv`, task D |
| 1 question | Separate judgment probe | `coding-totals.csv`, probe row |
| 39 of 40 | Separate judgment probe score | `coding-totals.csv`, probe row |
| 423 seconds | Separate judgment probe time from question to answer | `coding-totals.csv`, probe row `wall_seconds` |
