# MiniMax M2.7 audition, 2026-09-13: the measurement tables

This note is an extract. The session write-up these tables came from is a working
document and does not ship; every measured row below is copied from it unchanged,
with the narrative, the machine's internal names and the session's own coordination
text left out. The raw artifacts the rows rest on ship beside this file:
`gguf_header.txt` (the header dump), `ling_gguf_header.txt`, `ling_chat_template.txt`,
`qwen36_upstream_header.txt`, `cpu_load_test.log`, `hf_config.json`, `hf_tree*.json`,
and the probe scripts `probe.py`, `recall_probe.py`, `gguf_header.py`.

Machine: one NVIDIA GeForce RTX 5090 (32,607 MiB by nvidia-smi), Intel Core Ultra 9
285K, 188 GiB of RAM. Server: llama.cpp `llama-server`, local build at upstream
commit `5f55650`, all 256 experts in system memory (`-cmoe`), one request at a time.

## 1. File and shard verification

| | |
|---|---|
| repository | `unsloth/MiniMax-M2.7-GGUF`, quantization **UD-IQ4_XS** |
| expected | **4 shards, 108,413,781,312 bytes** (108.41 GB, 100.97 GiB) |
| download | started 2026-09-13 00:45:28 local; failed once at 01:19:06 with shard 3 incomplete (a transient connection-token error after 42.4 GB of that shard's 49.6 GB); one retry, resumed from the partial file |
| verification | count and byte-for-byte size checked against the repository tree, not `du`: both exact |

## 2. GGUF header, read before any load

Read with `gguf_header.py`, a standalone reader: it reads the key-value block at the
head of shard 1 and never touches tensor data. Full dump in `gguf_header.txt`.

```
general.architecture              minimax-m2
general.name                      Minimax-M2.7
general.size_label                256x4.9B
general.quantized_by              Unsloth
minimax-m2.block_count            62
minimax-m2.attention.head_count   48
minimax-m2.attention.head_count_kv 8
minimax-m2.attention.key_length   128
minimax-m2.attention.value_length 128
minimax-m2.expert_count           256
minimax-m2.expert_used_count      8
minimax-m2.embedding_length       3072
minimax-m2.context_length         196608
minimax-m2.rope.freq_base         5000000.0
minimax-m2.rope.dimension_count   64
tokenizer.ggml.model              gpt2 (pre: minimax-m2), vocab 200,064
split.count                       4 (split.tensors.count 809)
```

Two notes from the dump: the GGUF declares a native context of **196,608** while the
upstream `config.json` declares 204,800, and llama.cpp honours the GGUF; and
`head_count_kv 8` with key and value length 128 over 62 blocks is plain grouped
attention, which is what makes the cache expensive (section 4).

## 3. Chat template read

`tokenizer.chat_template` is **6,594 characters**. Probed for a thinking switch:

| probe | present? |
|---|---|
| `enable_thinking` | no |
| `reasoning_effort` | no |
| `thinking` | yes, as prose and variable names, not a branch |
| `<think>` / `</think>` | yes |
| `tools` / `tool_call` | yes |

The generation prompt is unconditional:

```jinja
{%- if add_generation_prompt -%}{{- ']~b]ai' ~ '\n' ~ '<think>' ~ '\n' }}{%- endif -%}
```

The template has no thinking off-switch: the model is started inside a `<think>`
block on every turn, so a small output budget can be spent entirely inside it. The
only levers in this build are server-side: `--reasoning-format`, `--reasoning-budget`
and `-rea on|off|auto`.

The template renders tool calls as an XML dialect of its own, with the delimiters
`]~!b[`, `]~b]ai` and `[e~[`.

## 4. Cache-cost arithmetic, from the header, before any load

```
2 (K and V) x 8 key-value heads x 128 head dimensions x 2 bytes (f16) x 62 blocks
  = 253,952 B = 248 KiB per token
```

| context | cache at f16 | cache at q8_0 |
|---|---|---|
| 32,768 | 7.8 GiB | 3.9 GiB |
| 65,536 | 15.5 GiB | 7.8 GiB |
| 131,072 | 31.0 GiB | 15.5 GiB |
| 196,608 (the GGUF ceiling) | 46.5 GiB | 23.3 GiB |

31.0 GiB of cache does not fit a 31.8 GiB card alongside weights and compute buffers,
so the 131,072 rung exists only with an 8-bit cache.

## 5. The two served rungs, measured 2026-09-13, 01:42 to 01:58

| | 65,536 with an f16 cache | 131,072 with an 8-bit cache |
|---|---|---|
| load to `/health` | 36 s | 3 s (page cache warm) |
| card memory | **21,232 MiB** | **22,240 MiB** |
| card free after load | 10,843 MiB | 9,793 MiB |
| reading, ~20-token prompt | 20.7 t/s | 21.4 t/s |
| reading, ~4,000-token prompt | 45.6 t/s | 45.0 t/s |
| speaking | 9.9 to 10.2 t/s | 9.6 to 9.9 t/s |

The two readings differ by about 1 GB because both hold about 15.5 GiB of cache,
which is what the arithmetic in section 4 predicts.

## 6. Coherence probe

| attempt | output budget | result |
|---|---|---|
| first | 900 tokens | `finish=length`, **900 completion tokens, 0 characters of content, 4,034 characters of reasoning** |
| second | 4,096 tokens | `finish=stop`, 1,522 completion tokens: 5,481 characters of reasoning and 1,313 characters of answer |

Three sentences of the second attempt's answer (the page no longer quotes them;
they are kept here as the evidence for "answered coherently"):

> "Keeping a promise across many years requires a quiet, stubborn devotion that goes
> beyond fleeting intention."

> "It means weaving the promise into ordinary habits, turning it from a grand
> declaration into a small, repeatable act that survives the erosion of time."

> "Trust, once given, becomes a living contract that demands regular renegotiation
> with oneself, asking for honesty about lapses and a willingness to correct course
> without self-condemnation."

## 7. Thinking-switch attempts: four variants, run at both rungs

Every one of the eight calls produced a `reasoning_content` block.

| variant | completion tokens (64K / 128K) | reasoning characters (64K / 128K) | thinking suppressed? |
|---|---|---|---|
| A, default, no switch | 177 / 310 | 601 / 1,368 | no |
| B, `chat_template_kwargs {"enable_thinking": false}` | 145 / 384 | 455 / 1,824 | no |
| C, `chat_template_kwargs {"thinking": false}` | 240 / 184 | 950 / 704 | no |
| D, `reasoning_effort: "low"` | 327 / 311 | 1,414 / 1,324 | no |

The spread is sampling noise at temperature 1.0, not a switch taking effect: B
produced fewer tokens than A at 65,536 and more at 131,072. Across all twelve chat
calls of the audition, thought text never once appeared in `message.content`: the
server routed it to `message.reasoning_content`. The thinking is separable, not
suppressible.

## 8. Tool call

Both rungs returned `finish_reason: tool_calls` with a correctly shaped array and
valid JSON arguments, in 64 tokens and 14.7 s, with `content` empty and the reasoning
in its own field. The generic handler produced a correct call from this template's XML
dialect, against the template read's prediction that it would not.

## 9. Thinking-budget test, measured 2026-09-15

MiniMax M2.7 alone at 131,072 with an 8-bit cache, the server's `--reasoning-budget`
control set to 0 and then to 256. The probe's own log is `budget/budget_probe_log.txt`
and the probe is `budget/probe_budget.py`. Card memory: 22,090 MiB at budget 0,
22,024 MiB at budget 256.

| setting | prompt tokens | decode | speaking | wall | reasoning characters | first answer token (estimated) | finish |
|---|---|---|---|---|---|---|---|
| budget 0, short | 59 | 467 tok | 10.73 t/s | 47.6 s | 1,734 | ~36 s | stop |
| budget 0, question | 27 | 600 tok | 10.71 t/s | 57.0 s | 3,003 | ~57 s | **length, reply 0 characters** |
| budget 0, tool | 174 | 57 tok | 10.53 t/s | 12.9 s | 129 | ~13 s | tool_calls |
| budget 0, depth ~8K | **7,850** | 164 tok | 10.24 t/s | **244.9 s** | 665 | ~245 s | stop, recall OK |
| budget 256, short | 59 | 311 tok | 10.79 t/s | 32.8 s | 1,217 | ~27 s | stop |
| budget 256, question | 27 | 338 tok | 10.90 t/s | 31.9 s | 1,272 | ~23 s | stop |
| budget 256, tool | 174 | 52 tok | 10.53 t/s | 12.5 s | 115 | ~13 s | tool_calls |
| budget 256, depth ~8K | **7,850** | 167 tok | 10.44 t/s | **246.9 s** | 647 | ~247 s | stop, recall OK |

The "first answer token" column is an estimate, not a recorded timing: the probe takes
the wall time and subtracts the answer's own decode time, with the answer's token count
estimated from its character count (`probe_budget.py`, function `rep`). Wall time,
prompt tokens, decode counts and speaking rates are measured.

The write-up's verdict paragraph states a reading rate of about 40 t/s for the 8,000
token prompt. It does not derive from the rows above, and it is not published.

---

# Ling-3.0-flash, same night

| | |
|---|---|
| file | `Ling-3.0-flash-Q4_K_M`, **2 shards, 77,804,990,144 bytes**, both exact, verified on the first try |
| architecture | `bailingmoe3` |
| layout | 43 blocks, 512 experts with 8 used and 1 shared |
| attention | only **8 of the 43 blocks hold a cache**, and those 8 are compressed (`kv_lora_rank` 512 plus 64 rotary dimensions); the other 35 run a linear path with a fixed-size state |
| cache cost | **9 KiB per token**: 0.56 GiB at 65,536, 1.13 GiB at 131,072, **2.25 GiB at its native 262,144** |
| against MiniMax M2.7 | 9 KiB against 248 KiB per token, **27 times cheaper**, both computed the same way from the two files' headers |
| thinking off-switch | three of them: `enable_thinking: false`, `thinking_option: "off"`, or the literal phrase "detailed thinking off" in a system message. Off emits a closed, empty thought block, not a truncation |
| draft layer | the multi-token prediction layer ships inside the quantization (`nextn_predict_layers 1`) |

Header dump: `ling_gguf_header.txt`. Chat template: `ling_chat_template.txt`. The same
fields read with the sweep's own reader are in
`../256k-sweep/header-reads/ling-3.0-flash.txt`.

---

# Qwen3-32B, measured 2026-09-13, 01:58 to 02:01

Wiring facts from the file's header: architecture `qwen3`, dense, `Q4_K_M`, 18.81 GiB,
declared context ceiling **40,960** (so the served rung is 32,768, and a larger ask is
not offered), cache **256 KiB per token** at f16. Header read:
`../256k-sweep/header-reads/qwen3-32b.txt`.

| | |
|---|---|
| load to `/health` | about 2 s |
| card memory at 32,768 context | **28,520 MiB** measured, against 28,518 MiB predicted (18.81 GiB of weights, 8.00 GiB of cache, 1.04 GiB of compute buffers) |
| reading | 107.6 t/s short, **3,332 t/s at 4,000 tokens of depth** |
| speaking | **69.5 and 60.5 t/s** on two probes |
| thinking switch | works in both directions: baked off gives 0 characters of reasoning in 42 completion tokens; `{"enable_thinking": true}` per request gives 1,227 characters of reasoning in 281 tokens |
| tool call | well formed, `finish=tool_calls`, valid JSON arguments, 22 tokens in 1.2 s |
| coherence | pass, 1,124 characters of clean prose |

---

# Qwen3.6-27B: two distributions, one trailing zero

The file distributed through Ollama's model library declares three rope sections and
is refused by every llama.cpp build on this machine, in under a second, before any
memory is touched:

```
error loading model hyperparameters:
key qwen35.rope.dimension_sections has wrong array length; expected 4, got 3
```

| | |
|---|---|
| the refused file | rope sections `[11, 11, 10]`, three elements |
| the upstream file | `unsloth/Qwen3.6-27B-GGUF` UD-Q4_K_XL, 17,612,564,704 bytes, verified; rope sections `[11, 11, 10, 0]`, four elements (dump: `qwen36_upstream_header.txt`) |
| loader requirement | four elements, on all three builds on this machine that carry the `qwen35` architecture |
| the upstream file loaded | processor-only test with graphics initialisation deliberately disabled: `model loaded` at **6.39 s**, zero graphics memory allocated (log: `cpu_load_test.log`) |

This is an interaction between a file variant and a loader's array-length requirement.
It is not a claim about either project.
