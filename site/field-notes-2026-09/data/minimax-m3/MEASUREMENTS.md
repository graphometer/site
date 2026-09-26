# MiniMax-M3 - measurement note (2026-09-19/20)

Extracted measurements only. Companion result files ship alongside this note.

## 1. The inherited file runs the wrong attention

The inherited unsloth UD-IQ3_XXS conversion predates llama.cpp's MSA (MiniMax
Sparse Attention) support:

- Tensor inventory: **zero `indexer` tensors across all 948 tensors**
  (positive control: `ffn_down_exps` found).
- llama.cpp builds before sparse-attention support therefore load it as a
  **dense fallback**, a mode the model was never trained for.
- Build 10919 (`d3146f2b5`) refuses the file outright:
  `error loading model hyperparameters: key not found in model: minimax-m3.attention.indexer.head_count`
  (all four sweep rungs below were run on the older build 9869 / `00f95bd2d`,
  which loads it).

Every number in section 2 was measured on the model running in dense fallback.
They are real measurements of the wrong thing; treat them as provisional.

## 2. Micro-batch sweep on the inherited file (dense fallback)

Fixed `-b 4096`, `-cmoe`, ctx 131072, q8_0 KV cache, 3,658-token prompts, one
cold run per rung. ub128 is the control (the inherited setting).

| `-ub` | prefill t/s | VRAM MiB |
|---|---:|---:|
| 128 (control) | 22.5615 | 20,320 |
| 512 | 67.6735 | 20,478 |
| 1024 | 123.1158 | 20,692 |
| 2048 | 221.3094 | 21,135 |
| 4096 | 393.7783 | 22,037 |

Decode on the same file at 128K / `-ub 4096` (two independent methods, chat and
forced): 8.8463 / 8.8482 t/s.

NOTE: the `A_*.json` result files carry a probe artifact `"decode_tps":
1000000.0`. The probe divided by a zero-length generation (the model answered
with a single stop token); decode was not measured in those runs. Prefill
figures are unaffected.

## 3. The MSA-correct file (bartowski `MiniMax-M3-Q2_K_L`)

4 shards, 153,086,988,768 bytes, exact-byte VERIFY PASS 2026-09-20; all five
indexer keys present; MSA confirmed engaged (the dense-fallback warning strings
were checked against the build's source, and neither fired).

ctx 131072, `-ub 2048`, q8_0 KV:

| measurement | value |
|---|---:|
| 4K prefill, cold (3,658 tokens) | 147.5406 t/s |
| 58K read (58,307 prompt tokens, 300.2 s wall) | 194.2 t/s |
| decode (two methods) | 8.8995 / 8.9733 t/s |
| recall, 3 needles at 5/50/95% of a 64,000-token document (58,307 prompt tokens) | 3/3 |

The 300.2 s wall includes 165 generated tokens, so 194.2 t/s slightly
understates pure prefill.

192K window (ctx 196608, `-ub 512`):

| measurement | value |
|---|---:|
| 4K prefill, cold | 72.6 t/s |
| 58K read (58,307 tokens in 856.3 s) | 68.1 t/s |
| decode | 9.2 t/s |
| recall, same document | 3/3 |

(The shipped `msa_192k_ub512_4k.json` also carries an incidental 32-token
decode of 8.99 t/s from its cold run; the 9.2 figure is the session's decode
measurement.)

The model gets faster with depth (147.5 -> 194 t/s); the dense-fallback build
did the opposite.

## 4. The 262,144 ladder with correct attention

The compute buffer scales with both `-ub` and the window: at ctx 262144 it asks
for **19,619.15 MiB (20,572,169,216 bytes)** at `-ub 2048`, and cudaMalloc fails
beside the q8_0 cache. (Corrected 2026-09-26: this note first called it "the
indexer's" compute buffer. The server log names only a compute buffer, so the
attribution is withdrawn; the sizes are unchanged.)

| `-ub` | outcome |
|---|---|
| 2048 | VOID - cudaMalloc out of memory (20,572,169,216 B) |
| 1024 | VOID - cudaMalloc out of memory (10,286,650,368 B) |
| 512 | VOID - cudaMalloc out of memory (5,143,890,944 B) |
| 256 | VOID - cudaMalloc out of memory (2,572,511,232 B) |
| 128 | loads - 31,525 MiB on card, reads at 24.2 t/s (4K prefill) |

256K is off the table with correct attention on this card.

## 5. Two-machine split (bartowski `MiniMax-M3-IQ3_XXS`)

The MSA-correct IQ3_XXS file (5 shards, 180,011,108,960 bytes = 167.6 GiB)
does not fit one box, so it was tried split over RPC, layer split 36/24, ctx
131072, `-fa on`, `--parallel 1`, MSA confirmed engaged:

| layer split | `-ub` | outcome |
|---|---|---|
| 36/24 | 4096 | FAIL - compute buffer request does not fit |
| 36/24 | 2048 | FAIL - compute buffer request does not fit |
| 36/24 | 1024 | LOADED - prefill 17.5804 t/s cold over 3,658 tokens (208.11 s) |

Decode was never measured: the run was stopped during the first speaking probe.
The server log, `split_ctx131072_vl36_ub1024.server.log`, ends with the server
cleaning up after an interrupt ("Received second interrupt, terminating
immediately") while that probe's request was open, and the probe's own record,
`split_msa_128k_ub1024.decode.json`, shows the dropped connection
(`RemoteDisconnected: Remote end closed connection without response`). (Corrected
2026-09-26: this note first said the server died mid-request; the server log shows
it was stopped.) The file itself, 5 shards and 180,011,108,960 bytes, is verified in
`DOWNLOAD_STATUS.txt`; the split ran early on 2026-09-20, after that verification
and before the Q2_K_L download.

The compute buffer is sized by `-ub` alone, not by the layer split, so moving
layers only changes which machine runs out; and at the one rung that loads,
17.6 t/s against 393.8 t/s single-box means the pair buys capacity, not
latency. Conclusion recorded: two-box is closed for M3.
