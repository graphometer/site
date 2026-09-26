# Recorded configurations

Derived from each server log’s `[cmd]` line and original response build identifier. These are archival commands with placeholders, not ready-to-run launch scripts. Model basenames identify the first shard for sharded files.

## Gemma-4-26B-A4B: UD-Q4_K_XL

Window: 262144; llama.cpp commit: `d3146f2b5`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf --host <LOCAL> --port <LOCAL> --alias Gemma-4-26B-A4B --jinja --ctx-size 262144 --n-gpu-layers 99 --flash-attn auto --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## GLM-4.7-Flash: UD-Q4_K_XL

Window: 202752; llama.cpp commit: `d3146f2b5`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/GLM-4.7-Flash-UD-Q4_K_XL.gguf --host <LOCAL> --port <LOCAL> --alias GLM-4.7-Flash --jinja --ctx-size 202752 --n-gpu-layers 99 --flash-attn auto --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## Qwen3.5-122B-A10B: UD-Q4_K_S

Window: 262144; llama.cpp commit: `c8e03ce`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Qwen3.5-122B-A10B-UD-Q4_K_S-00001-of-00003.gguf --host <LOCAL> --port <LOCAL> --alias Qwen3.5-122B-A10B --jinja --ctx-size 262144 --n-gpu-layers 999 --n-cpu-moe 38 --no-mmap --spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.75 --flash-attn on --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.0 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## Mistral Small 4: UD-Q4_K_M

Window: 262144; llama.cpp commit: `5f55650`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Mistral-Small-4-119B-2603-UD-Q4_K_M-00001-of-00003.gguf --host <LOCAL> --port <LOCAL> --alias Mistral-Small-4 --jinja --ctx-size 262144 --n-gpu-layers 999 --n-cpu-moe 26 --no-mmap --flash-attn auto --temp 0.15 --top-p 1.0 --top-k 0 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## Ling-3.0-flash: Q4_K_M

Window: 262144; llama.cpp commit: `d3146f2b5`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf --host <LOCAL> --port <LOCAL> --alias Ling-3.0-flash --jinja --ctx-size 262144 --n-gpu-layers 999 -cmoe --fit off --flash-attn auto --top-p 0.95 --top-k 20 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## Qwen3.5-397B-A17B: UD-IQ3_XXS

Window: 262144; llama.cpp commit: `c8e03ce`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Qwen3.5-397B-A17B-UD-IQ3_XXS-00001-of-00004.gguf --host <LOCAL> --port <LOCAL> --alias Qwen3.5-397B-A17B --jinja --ctx-size 262144 --chat-template-kwargs {"enable_thinking": false} --n-gpu-layers 999 --n-cpu-moe 57 --no-mmap --spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.75 --flash-attn on --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## Qwen3.8-Flash-Next: UD-Q3_K_XL

Window: 262144; llama.cpp commit: `d3146f2b5`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Qwen3.8-Flash-Next-UD-Q3_K_XL-00001-of-00003.gguf --host <LOCAL> --port <LOCAL> --alias Qwen3.8-Flash-Next --jinja --ctx-size 262144 --n-gpu-layers 99 --n-cpu-moe 99 --fit off --flash-attn auto --temp 0.7 --top-p 0.8 --top-k 20 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## Inkling-Small: UD-Q3_K_XL

Window: 262144; llama.cpp commit: `946fc11d1`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Inkling-Small-UD-Q3_K_XL-00001-of-00004.gguf --host <LOCAL> --port <LOCAL> --alias Inkling-Small -ngl 999 --n-cpu-moe 42 --flash-attn on -ctk f16 -ctv f16 --jinja --reasoning-format auto --ctx-size 262144 --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## DeepSeek V4 Flash, desktop: UD-Q8_K_XL

Window: 262144; llama.cpp commit: `5f55650`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/DeepSeek-V4-Flash-0731-UD-Q8_K_XL-00001-of-00005.gguf --host <LOCAL> --port <LOCAL> --alias DeepSeek-V4-Flash --jinja --reasoning-format deepseek --ctx-size 262144 --n-gpu-layers 999 -cmoe --no-repack --flash-attn auto --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```

## DeepSeek V4 Flash, desktop + laptop: UD-IQ3_XXS

Window: 262144; llama.cpp commit: `d3146f2b5`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/DeepSeek-V4-Flash-0731-UD-IQ3_XXS-00001-of-00004.gguf --host <LOCAL> --port <LOCAL> --alias DeepSeek-V4-Flash --rpc <LOCAL> --device CUDA0,RPC0 --tensor-split 18,25 --n-gpu-layers 999 --override-tensor blk\.(8|9|10|11|12|13|14|15|16|17)\.ffn_(up|down|gate)_exps=CPU,output\.weight=CUDA0 --no-repack --flash-attn auto --jinja --reasoning-format deepseek --ctx-size 262144 --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
```
