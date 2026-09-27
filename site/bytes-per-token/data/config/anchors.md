# Recorded anchor configurations

## Qwen3.5-397B-A17B: UD-IQ3_XXS

Window: 262144; llama.cpp commit: `c8e03ce`.

```text
<REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Qwen3.5-397B-A17B-UD-IQ3_XXS-00001-of-00004.gguf --host <LOCAL> --port <LOCAL> --alias Qwen3.5-397B-A17B --jinja --ctx-size 262144 --chat-template-kwargs {"enable_thinking": false} --n-gpu-layers 999 --n-cpu-moe 57 --no-mmap --spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.75 --flash-attn on --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 --parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600
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
