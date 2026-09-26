# Inkling-Small, the probe tables from its first night on this machine (2026-09-14)

An extract, not a copy. The record it comes from continues into work that is not published, and
the sections after run 2 are not here. Program names, paths, ports and aliases are removed. The
probe tables and the header facts are as the record wrote them.

## Header facts, read from the model file and the runtime

- Maker: Thinking Machines. Parameter counts: 276B total, 12B active (the maker's figures).
- Licence: Apache 2.0.
- File: `unsloth` UD-Q3_K_XL, 4 shards, 119,554,379,840 bytes, verified byte for byte against the
  maker's published file listing.
- Header: architecture `inkling`, 42 blocks (2 dense + 40 mixture of experts), 256 experts,
  6 used per token plus 2 shared, 32 attention heads, 8 key/value heads, embedding 4096, a
  sliding window of 512 on 5 of every 6 blocks (the 7 global blocks carry the full cache, so a
  128K window costs about 3.7 GB at f16), 1,048,576 tokens of architecture context, vocabulary
  201,024, and a chat template of 22.7K characters carrying a `reasoning_effort` setting with six
  levels (none, minimal, low, medium, high, max; default high).
- Runtime: llama.cpp pull request #25731 (a draft branch; commit 946fc11d1, build 10897, based at
  df750f76b), CUDA 12.8.93.

## Run 1, this desktop alone, every expert in system memory, 128K window, f16 cache, 22:05

Healthy in 40 s. 12.4 GB of the card, of which about 3.7 GB is the attention cache, leaving about
19 GB of the card untouched.

| probe | prompt | prefill | decode | note |
|---|---|---|---|---|
| cold short, effort none | 32 tok | 29 t/s | 11.9 t/s | 444 characters of coherent prose |
| same again | 32 | 34 | 12.1 | |
| thinking on (medium) | 34 | 32 | 11.8 | 961 characters of reasoning in a separate channel, clean answer |
| tool call, effort none | 73 | 23 | 12.1 | well formed tool call |
| depth ~2K | 1,950 | 119 t/s | 11.7 | recall OK |
| depth ~8K | 7,641 | 158 t/s | 11.6 | recall OK |
| depth ~32K | 30,441 | 182 t/s | 11.6 | recall OK |

Decode is flat with depth (sliding-window attention); prefill rises with batch size. Reasoning
effort works per request.

## Run 1b, the same server, 22:14 to 22:24

| probe | prompt | prefill | decode | note |
|---|---|---|---|---|
| tool call, thinking on (medium) | 75 | 26 | 12.0 | 132 characters of thought, then a well formed tool call |
| tool call, thinking on (high, the template default) | 75 | 27 | 12.2 | the same |
| depth ~100K | 95,041 | 185.5 t/s (8.5 min) | 11.6 | recall OK at 100K; 12.5 GB of the card |

A cold 100K history reads in about 9 minutes; decode does not sag with depth.

## Run 2, five blocks' experts moved onto the card, 23:00

Healthy in 6 s (the page cache was warm). 26.9 GB of the card. Decode 13.0 to 13.6 t/s, about 12%
over run 1. Prefill 136 t/s at 2K and 176 t/s at 8K, recall OK, tool call OK.
