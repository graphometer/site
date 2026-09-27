# Number map

One row per printed figure and meaning. Repeated appearances of the same figure share a row; rounded variants and individual range endpoints have separate rows. Product-name numerals, quantization names, commit identifiers and section labels identify things rather than measured quantities. The build commits are recorded in `config/anchor-build-records.tsv` and `source/inkling-build-info.cpp`.

DeepSeek reply 1 is retained but excluded from the selected operating envelope. Inkling rates use (completed tokens minus one) / eval seconds; Qwen and DeepSeek use the completed count itself. The prediction retains these conventions. The target prose samples differ between placements. Server-reported desktop and pair ranges are the minima and maxima of the individually indexed rates below, not convention-independent speed bounds. Code-word recall is not code generation.

If a number on the page disagrees with a file in its package, the file is right and the page is wrong.

| Printed figure | Page location and meaning | Label | Source or derivation |
|---|---|---|---|
| 26 September 2026 | Hero; sections 02 and 05; footer | publication and header-read date | Edition date; header census provenance in `README.md`. |
| 15 September (2026 in section 03; 15 Sep in section 04) | Hero and sections 03 to 04, desktop local calendar; section 05, run ledger local calendar | recorded local run date | Archive chronology documented in `README.md`; `runs/*-prose-r*.json`, `created`, spans two UTC dates as indexed below. The original local timezone is not established by the shipped records. Target logs show elapsed time, not calendar date. |
| 15 September 23:52 UTC | Section 03, earliest anchor creation time, to the minute | recorded timestamp converted to UTC | `runs/inkling-small-prose-r1.json`, `created` = 1789516341, converted to UTC: 2026-09-15 23:52:21. |
| 16 September 02:52 UTC | Section 03, latest anchor creation time, to the minute | recorded timestamp converted to UTC | `runs/deepseek-prose-r2.json`, `created` = 1789527173, converted to UTC: 2026-09-16 02:52:53. |
| 1,000,000,000 | Section 02, bytes per decimal GB | unit conversion | Decimal GB definition; `tools/calculate.py`. |
| 119.55 GB | Section 02, inkling-small file size | arithmetic | `files.csv`, sum `file_size_bytes` for inkling-small, divided by 1e9. |
| 6 of 256 | Section 02, inkling-small routed selection | measured header | `inkling-small-headers.json`, architecture `expert_used_count` / `expert_count`. |
| 2.655 GB/token | Section 02, inkling-small RAM expert budget | arithmetic | `arithmetic.json`, `models.inkling-small.expert_RAM_bytes_per_token` / 1e9. |
| 149.84 GB | Section 02, qwen397 file size | arithmetic | `files.csv`, sum `file_size_bytes` for qwen397, divided by 1e9. |
| 10 of 512 | Section 02, qwen397 routed selection | measured header | `qwen397-headers.json`, architecture `expert_used_count` / `expert_count`. |
| 2.563 GB/token | Section 02, qwen397 RAM expert budget | arithmetic | `arithmetic.json`, `models.qwen397.expert_RAM_bytes_per_token` / 1e9. |
| 161.87 GB | Section 02, deepseek file size | arithmetic | `files.csv`, sum `file_size_bytes` for deepseek, divided by 1e9. |
| 6 of 256 | Section 02, deepseek routed selection | measured header | `deepseek-headers.json`, architecture `expert_used_count` / `expert_count`. |
| 3.449 GB/token | Section 02, deepseek RAM expert budget | arithmetic | `arithmetic.json`, `models.deepseek.expert_RAM_bytes_per_token` / 1e9. |
| 270.16 GB | Section 02, inkling-975b file size | arithmetic | `files.csv`, sum `file_size_bytes` for inkling-975b, divided by 1e9. |
| 6 of 256 | Section 02, inkling-975b routed selection | measured header | `inkling-975b-headers.json`, architecture `expert_used_count` / `expert_count`. |
| 6.006 GB/token | Section 02, inkling-975b RAM expert budget | arithmetic | `arithmetic.json`, `models.inkling-975b.expert_RAM_bytes_per_token` / 1e9. |
| 6.01 GB/token | Hero and share descriptions, target budget | arithmetic | `arithmetic.json`, `models.inkling-975b.expert_RAM_bytes_per_token` / 1e9, rounded to two decimals. |
| 6,006,472,704 bytes/token | Sections 02 and 05, target budget | arithmetic | `arithmetic.json`, `models.inkling-975b.expert_RAM_bytes_per_token`. |
| 256,276,168,704 bytes | Section 02, target routed banks | header arithmetic | `inkling-975b-headers.json`; `arithmetic.json`, target `category_stored_bytes.routed experts`; `source/inkling-architecture-excerpts.cpp`. |
| 66 blocks | Section 02, target total blocks | header arithmetic | `inkling-975b-headers.json`; `arithmetic.json`, target `blocks`; `source/inkling-architecture-excerpts.cpp`. |
| 2 dense blocks | Section 02, target first two blocks | header arithmetic | `inkling-975b-headers.json`; `arithmetic.json`, target `header: inkling.dense_block_count`; `source/inkling-architecture-excerpts.cpp`. |
| 2 to 65 | Section 02, target routed block indices | header arithmetic | `inkling-975b-headers.json`; `arithmetic.json`, target `tensor names`; `source/inkling-architecture-excerpts.cpp`. |
| 2 shared experts | Section 02, target both shared experts | header arithmetic | `inkling-975b-headers.json`; `arithmetic.json`, target `header: inkling.expert_shared_count`; `source/inkling-architecture-excerpts.cpp`. |
| 6 / 256 | Section 02, target active fraction | header ratio | `inkling-975b-headers.json`, `inkling.expert_used_count` / `inkling.expert_count`. |
| 0 to 56 | Section 02, Qwen RAM blocks | configured placement | `config/anchors.md`, `--n-cpu-moe 57`; `tools/calculate.py` excludes the draft block. |
| 5,322,866,688 bytes | Section 02, target shared experts and shared gate | header arithmetic | `arithmetic.json`, `models.inkling-975b.category_stored_bytes.shared experts and shared gate`; contributing rows in `tensors.csv`. |
| 6,091,720,704 bytes | Section 02, target attention and recurrent state weights | header arithmetic | `arithmetic.json`, `models.inkling-975b.category_stored_bytes.attention and recurrent state weights`; contributing rows in `tensors.csv`. |
| 662,962,176 bytes | Section 02, target dense feed-forward | header arithmetic | `arithmetic.json`, `models.inkling-975b.category_stored_bytes.dense feed-forward`; contributing rows in `tensors.csv`. |
| 407,511,304 bytes | Section 02, target routing, norms and other weights | header arithmetic | `arithmetic.json`, `models.inkling-975b.category_stored_bytes.routing, norms and other weights`; contributing rows in `tensors.csv`. |
| 694,763,520 bytes | Section 02, target output head and output norms | header arithmetic | `arithmetic.json`, `models.inkling-975b.category_stored_bytes.output head and output norms`; contributing rows in `tensors.csv`. |
| 694,738,944 bytes | Section 02, target input embedding | header arithmetic | `arithmetic.json`, `models.inkling-975b.category_stored_bytes.input embedding`; contributing rows in `tensors.csv`. |
| 3,456 bytes | Section 02, input embedding row | arithmetic | `arithmetic.json`, `models.inkling-975b.input_embedding_row_bytes`; tensor stored bytes divided by vocabulary rows. |
| 262,144 tokens | Section 03, anchor served window | recorded configuration | `config/anchors.md`, --ctx-size. |
| 320 tokens | Section 03, anchor output cap | recorded configuration | `config/prose-request-excerpt.sh`, water-pump request. |
| 1.0 | Section 03, anchor server temperature | recorded configuration | `config/anchors.md`, --temp. |
| 0 | Section 03, water-pump request temperature | recorded configuration | `config/prose-request-excerpt.sh`, temperature. |
| 1 request | Section 03, anchor concurrency | recorded configuration | `config/anchors.md`, --parallel 1. |
| 24 compute threads | Section 03, anchors | recorded configuration | `config/anchors.md`, --threads. |
| 24 batch threads | Section 03, anchors | recorded configuration | `config/anchors.md`, --threads-batch. |
| 42 | Section 03, Inkling-Small CPU block setting | recorded configuration | `config/anchors.md`, --n-cpu-moe. |
| 57 | Section 03, Qwen CPU block setting | recorded configuration | `config/anchors.md`, --n-cpu-moe. |
| 6 | Section 03, Qwen draft maximum | recorded configuration | `config/anchors.md`, --spec-draft-n-max. |
| 0.75 | Section 03, Qwen draft gate | recorded configuration | `config/anchors.md`, --spec-draft-p-min. |
| 131,072 tokens | Section 03, target served window | recorded configuration | `runs/975b-*.log`, n_ctx_slot. |
| 1 slot | Section 03, target concurrency | recorded configuration | `runs/975b-*.log`, n_slots. |
| 24 threads | Section 03, target desktop | recorded configuration | `runs/975b-*.log`, n_threads. |
| 66 | Section 03, target Run A CPU block setting | recorded configuration | `config/975b-launch.txt`, --n-cpu-moe. |
| 42 | Section 03, target Run B CPU block setting | recorded configuration | `config/975b-launch.txt`, --n-cpu-moe. |
| 42 to 65 | Section 03, target remote blocks | recorded configuration | `config/975b-launch.txt`, remote override. |
| 8 threads | Section 03, requested worker threads | recorded configuration | `config/975b-launch.txt`, worker -t. |
| 1.0 | Section 03, target request temperature | recorded configuration | `tools/probe_975b.py`, chat request. |
| 10897 | Section 03, target build number | recorded configuration | `source/inkling-build-info.cpp`. |
| 2048 | Section 03, default -b | recorded configuration | `source/offload-and-batch-excerpts.txt`. |
| 512 | Section 03, default -ub | recorded configuration | `source/offload-and-batch-excerpts.txt`. |
| 1 token subtracted | Sections 04 and 05, Inkling rate numerator | server timing convention | `runs/inkling-small-prose-r*.json`, (predicted_n - 1) / (predicted_ms / 1000); same convention in completed eval lines of `runs/975b-*.log`. Qwen and DeepSeek use predicted_n itself. |
| 11.77 t/s | Section 04, inkling-small reply 1 | server-reported | `runs/inkling-small-prose-r1.json`, `timings.predicted_per_second`; Inkling uses n - 1, Qwen and DeepSeek use n. |
| 31.26 GB/s | Section 04, inkling-small reply 1 | arithmetic | `arithmetic.json`, matching anchor `effective_expert_GB_s`, from unrounded server rate times RAM expert bytes / 1e9. |
| 11.69 t/s | Section 04, inkling-small reply 2 | server-reported | `runs/inkling-small-prose-r2.json`, `timings.predicted_per_second`; Inkling uses n - 1, Qwen and DeepSeek use n. |
| 31.04 GB/s | Section 04, inkling-small reply 2 | arithmetic | `arithmetic.json`, matching anchor `effective_expert_GB_s`, from unrounded server rate times RAM expert bytes / 1e9. |
| 202 tokens | Section 04, inkling-small, each reply | recorded output | `runs/inkling-small-prose-r*.json`, `timings.predicted_n`. |
| 174 words | Section 04, inkling-small paragraph | whitespace word count | `runs/inkling-small-prose-r*.json`, split `choices[0].message.content` on whitespace; `arithmetic.json`, visible_words. |
| 12.76 t/s | Section 04, qwen397 reply 1 | server-reported | `runs/qwen397-prose-r1.json`, `timings.predicted_per_second`; Inkling uses n - 1, Qwen and DeepSeek use n. |
| 32.70 GB/s | Section 04, qwen397 reply 1 | arithmetic | `arithmetic.json`, matching anchor `effective_expert_GB_s`, from unrounded server rate times RAM expert bytes / 1e9. |
| 12.84 t/s | Section 04, qwen397 reply 2 | server-reported | `runs/qwen397-prose-r2.json`, `timings.predicted_per_second`; Inkling uses n - 1, Qwen and DeepSeek use n. |
| 32.92 GB/s | Section 04, qwen397 reply 2 | arithmetic | `arithmetic.json`, matching anchor `effective_expert_GB_s`, from unrounded server rate times RAM expert bytes / 1e9. |
| 184 tokens | Section 04, qwen397, each reply | recorded output | `runs/qwen397-prose-r*.json`, `timings.predicted_n`. |
| 161 words | Section 04, qwen397 paragraph | whitespace word count | `runs/qwen397-prose-r*.json`, split `choices[0].message.content` on whitespace; `arithmetic.json`, visible_words. |
| 2.07 t/s | Section 04, deepseek reply 1 | server-reported | `runs/deepseek-prose-r1.json`, `timings.predicted_per_second`; Inkling uses n - 1, Qwen and DeepSeek use n. |
| 9.93 t/s | Section 04, deepseek reply 2 | server-reported | `runs/deepseek-prose-r2.json`, `timings.predicted_per_second`; Inkling uses n - 1, Qwen and DeepSeek use n. |
| 34.26 GB/s | Section 04, deepseek reply 2 | arithmetic | `arithmetic.json`, matching anchor `effective_expert_GB_s`, from unrounded server rate times RAM expert bytes / 1e9. |
| 209 tokens | Section 04, deepseek, each reply | recorded output | `runs/deepseek-prose-r*.json`, `timings.predicted_n`. |
| 166 words | Section 04, deepseek paragraph | whitespace word count | `runs/deepseek-prose-r*.json`, split `choices[0].message.content` on whitespace; `arithmetic.json`, visible_words. |
| 90 tokens | Section 04, Qwen draft counters | recorded output | `runs/qwen397-prose-r*.json`, `timings.draft_n_accepted`. |
| 106 tokens | Section 04, Qwen draft counters | recorded output | `runs/qwen397-prose-r*.json`, `timings.draft_n`. |
| 16.41 t/s | Section 04, Qwen batch code-word answer | recorded output | `runs/qwen397-batch4096.result`, decode_tps; excluded from anchors. |
| 17 characters | Section 04, Qwen batch code-word answer | recorded output | `runs/qwen397-batch4096.result`, answer_len; excluded from anchors. |
| 21 September | Section 04, batch pass date | provenance | Batch pass chronology in `README.md`; `runs/qwen397-batch4096.result`. |
| 31.0 GB/s | Section 04, the three description tags, and the feed summary, lower endpoint | arithmetic | `arithmetic.json`, `effective_expert_GB_s_range[0]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 34.3 GB/s | Section 04, the three description tags, and the feed summary, upper endpoint | arithmetic | `arithmetic.json`, `effective_expert_GB_s_range[1]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 31.044 GB/s | Section 05 only, lower endpoint | arithmetic | `arithmetic.json`, `effective_expert_GB_s_range[0]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 34.263 GB/s | Section 05 only, upper endpoint | arithmetic | `arithmetic.json`, `effective_expert_GB_s_range[1]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 5.2 tokens/s | Hero, title/share text and section 05, lower endpoint | arithmetic | `arithmetic.json`, `inkling975_prediction_tokens_s[0]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 5.7 tokens/s | Hero, title/share text and section 05, upper endpoint | arithmetic | `arithmetic.json`, `inkling975_prediction_tokens_s[1]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 5.168 tokens/s | Section 05 only, lower endpoint | arithmetic | `arithmetic.json`, `inkling975_prediction_tokens_s[0]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 5.704 tokens/s | Section 05 only, upper endpoint | arithmetic | `arithmetic.json`, `inkling975_prediction_tokens_s[1]`, rounded as printed. Prediction divides selected effective throughput by target budget; original server conventions retained. |
| 71 tokens | Section 05, desktop short prose | recorded completed count | `runs/975b-desktop.log`, completed eval line for short prose; `runs/975b-probe-stdout.txt`, matching output type. |
| 3.43 t/s | Sections 03 and 05, desktop short prose in the paging placement; hero/title/share prose figure | server-reported | `runs/975b-desktop.log`, completed eval line for short prose; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 20424.35 ms | Section 05, desktop short prose | recorded raw eval time | `runs/975b-desktop.log`, completed eval line for short prose; `runs/975b-probe-stdout.txt`, matching output type. |
| 18 tokens | Section 05, desktop weather tool call | recorded completed count | `runs/975b-desktop.log`, completed eval line for weather tool call; `runs/975b-probe-stdout.txt`, matching output type. |
| 4.98 t/s | Section 05, desktop weather tool call | server-reported | `runs/975b-desktop.log`, completed eval line for weather tool call; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 3414.75 ms | Section 05, desktop weather tool call | recorded raw eval time | `runs/975b-desktop.log`, completed eval line for weather tool call; `runs/975b-probe-stdout.txt`, matching output type. |
| 12 tokens | Section 05, desktop planted code word, 1,950-token prompt | recorded completed count | `runs/975b-desktop.log`, completed eval line for planted code word, 1,950-token prompt; `runs/975b-probe-stdout.txt`, matching output type. |
| 4.65 t/s | Section 05, desktop planted code word, 1,950-token prompt | server-reported | `runs/975b-desktop.log`, completed eval line for planted code word, 1,950-token prompt; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 2367.23 ms | Section 05, desktop planted code word, 1,950-token prompt | recorded raw eval time | `runs/975b-desktop.log`, completed eval line for planted code word, 1,950-token prompt; `runs/975b-probe-stdout.txt`, matching output type. |
| 80 tokens | Section 05, pair different short-prose sample | recorded completed count | `runs/975b-pair.log`, completed eval line for different short-prose sample; `runs/975b-probe-stdout.txt`, matching output type. |
| 3.13 t/s | Section 05, pair different short-prose sample | server-reported | `runs/975b-pair.log`, completed eval line for different short-prose sample; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 25201.99 ms | Section 05, pair different short-prose sample | recorded raw eval time | `runs/975b-pair.log`, completed eval line for different short-prose sample; `runs/975b-probe-stdout.txt`, matching output type. |
| 18 tokens | Section 05, pair weather tool call | recorded completed count | `runs/975b-pair.log`, completed eval line for weather tool call; `runs/975b-probe-stdout.txt`, matching output type. |
| 3.26 t/s | Section 05, pair weather tool call | server-reported | `runs/975b-pair.log`, completed eval line for weather tool call; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 5222.13 ms | Section 05, pair weather tool call | recorded raw eval time | `runs/975b-pair.log`, completed eval line for weather tool call; `runs/975b-probe-stdout.txt`, matching output type. |
| 12 tokens | Section 05, pair planted code word, 1,950-token prompt | recorded completed count | `runs/975b-pair.log`, completed eval line for planted code word, 1,950-token prompt; `runs/975b-probe-stdout.txt`, matching output type. |
| 3.34 t/s | Section 05, pair planted code word, 1,950-token prompt | server-reported | `runs/975b-pair.log`, completed eval line for planted code word, 1,950-token prompt; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 3293.87 ms | Section 05, pair planted code word, 1,950-token prompt | recorded raw eval time | `runs/975b-pair.log`, completed eval line for planted code word, 1,950-token prompt; `runs/975b-probe-stdout.txt`, matching output type. |
| 12 tokens | Section 05, pair planted code word, 7,641-token prompt | recorded completed count | `runs/975b-pair.log`, completed eval line for planted code word, 7,641-token prompt; `runs/975b-probe-stdout.txt`, matching output type. |
| 3.35 t/s | Section 05, pair planted code word, 7,641-token prompt | server-reported | `runs/975b-pair.log`, completed eval line for planted code word, 7,641-token prompt; `runs/975b-probe-stdout.txt`, matching output type. Rate = (completed tokens - 1) / eval seconds; prose samples differ between arms. |
| 3279.71 ms | Section 05, pair planted code word, 7,641-token prompt | recorded raw eval time | `runs/975b-pair.log`, completed eval line for planted code word, 7,641-token prompt; `runs/975b-probe-stdout.txt`, matching output type. |
| 1,950 tokens | Section 05, recall prompt on both arms | recorded setup/output | `runs/975b-desktop.log` and `runs/975b-pair.log`, completed prompt eval lines. |
| 7,641 tokens | Section 05, recall prompt on pair | recorded setup/output | `runs/975b-pair.log`, final completed prompt eval line. |
| 120 tokens | Section 05, prose output cap | recorded setup/output | `tools/probe_975b.py`, first chat call. |
| 80 tokens | Section 05, tool output cap | recorded setup/output | `tools/probe_975b.py`, tool chat call. |
| 40 tokens | Section 05, recall output cap | recorded setup/output | `tools/probe_975b.py`, recall chat call. |
| 3,647,766,528 bytes/token | Section 06, desktop | arithmetic | `arithmetic.json`, `models.inkling-975b.pair_local_expert_bytes_per_token`; split at block 42, sum equals full target budget. |
| 2,358,706,176 bytes/token | Section 06, laptop | arithmetic | `arithmetic.json`, `models.inkling-975b.pair_remote_expert_bytes_per_token`; split at block 42, sum equals full target budget. |
