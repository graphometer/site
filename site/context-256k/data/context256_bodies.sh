#!/usr/bin/env bash
# context256_bodies.sh : one entry per body for the 2026-09-15 256K sweep. Flags are copied from each
# canonical start script's exec line (read 2026-09-15); only --ctx-size changes.
# Usage: bash context256_bodies.sh <body>
set -uo pipefail
D=<REDACTED_PATH>
R="$D/context256_rung.sh"
G=<REDACTED_PATH>
CU=<REDACTED_PATH>
FN=<REDACTED_PATH>
Q35=<REDACTED_PATH>
KIMI=<REDACTED_PATH>
INK=<REDACTED_PATH>
RPC=<REDACTED_PATH>
C=262144
T=230000
NOTHINK='{"enable_thinking": false}'
COMMON=(--parallel 1 --threads 24 --threads-batch 24 --cors-origins localhost --timeout 3600)

case "${1:-}" in

gemma26)      # Gemma-4-26B-A4B :<LOCAL> : all on the card
  bash "$R" gemma26_262144 <LOCAL> <LOCAL> "$NOTHINK" 600 "$FN:$CU" 20 "$T" -- \
    "$FN/llama-server" --model "$G/Gemma-4-26B-A4B/gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf" \
    --host <LOCAL> --port <LOCAL> --alias Gemma-4-26B-A4B --jinja --ctx-size "$C" \
    --n-gpu-layers 99 --flash-attn auto "${COMMON[@]}" ;;

glm47flash)   # GLM-4.7-Flash :<LOCAL> : native ceiling 202,752
  bash "$R" glm47flash_202752 <LOCAL> <LOCAL> "$NOTHINK" 600 "$FN:$CU" 20 190000 -- \
    "$FN/llama-server" --model "$G/GLM-4.7-Flash/GLM-4.7-Flash-UD-Q4_K_XL.gguf" \
    --host <LOCAL> --port <LOCAL> --alias GLM-4.7-Flash --jinja --ctx-size 202752 \
    --n-gpu-layers 99 --flash-attn auto "${COMMON[@]}" ;;

flashnext)    # Qwen3.8-Flash-Next :<LOCAL> : experts CPU-side, never --no-mmap, --fit off required
  bash "$R" flashnext_262144 <LOCAL> <LOCAL> "$NOTHINK" 900 "$FN:$CU" 100 "$T" -- \
    "$FN/llama-server" --model "$G/Qwen3.8-Flash-Next/Qwen3.8-Flash-Next-UD-Q3_K_XL-00001-of-00003.gguf" \
    --host <LOCAL> --port <LOCAL> --alias Qwen3.8-Flash-Next --jinja --ctx-size "$C" \
    --n-gpu-layers 99 --n-cpu-moe 99 --fit off --flash-attn auto \
    --temp 0.7 --top-p 0.8 --top-k 20 "${COMMON[@]}" ;;

ling)         # Ling-3.0-flash :<LOCAL> : experts CPU-side (-cmoe), --fit off required, MTP off (the gated default)
  bash "$R" ling_262144 <LOCAL> <LOCAL> "$NOTHINK" 900 "$FN:$CU" 100 "$T" -- \
    "$FN/llama-server" --model "$G/Ling-3.0-flash/Ling-3.0-flash-Q4_K_M/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf" \
    --host <LOCAL> --port <LOCAL> --alias Ling-3.0-flash --jinja --ctx-size "$C" \
    --n-gpu-layers 999 -cmoe --fit off --flash-attn auto \
    --top-p 0.95 --top-k 20 "${COMMON[@]}" ;;

mistral4)     # Mistral Small 4 :<LOCAL> : the 128K knob profile NCMOE 26, --no-mmap; no reasoning unless asked
  bash "$R" mistral4_262144 <LOCAL> <LOCAL> - 900 "$CU" 70 "$T" -- \
    "$KIMI/llama-server" --model "$G/Mistral-Small-4/UD-Q4_K_M/Mistral-Small-4-119B-2603-UD-Q4_K_M-00001-of-00003.gguf" \
    --host <LOCAL> --port <LOCAL> --alias Mistral-Small-4 --jinja --ctx-size "$C" \
    --n-gpu-layers 999 --n-cpu-moe 26 --no-mmap --flash-attn auto \
    --temp 0.15 --top-p 1.0 --top-k 0 "${COMMON[@]}" ;;

qwen122)      # Qwen3.5-122B-A10B :<LOCAL> : NCMOE 38, --no-mmap, gated MTP
  bash "$R" qwen122_262144 <LOCAL> <LOCAL> "$NOTHINK" 900 "$CU" 70 "$T" -- \
    "$Q35/llama-server" --model "$G/Qwen3.5-122B-A10B/UD-Q4_K_S/Qwen3.5-122B-A10B-UD-Q4_K_S-00001-of-00003.gguf" \
    --host <LOCAL> --port <LOCAL> --alias Qwen3.5-122B-A10B --jinja --ctx-size "$C" \
    --n-gpu-layers 999 --n-cpu-moe 38 --no-mmap \
    --spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.75 --flash-attn on \
    --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.0 "${COMMON[@]}" ;;

inkling)      # Inkling-Small :<LOCAL> : every expert in RAM (NCMOE 42), f16 KV, PR #25731 build
  bash "$R" inkling_262144 <LOCAL> <LOCAL> '{"reasoning_effort": "none"}' 900 "$INK:$CU" 130 "$T" -- \
    "$INK/llama-server" --model <REDACTED_PATH>/Inkling-Small-UD-Q3_K_XL-00001-of-00004.gguf \
    --host <LOCAL> --port <LOCAL> --alias Inkling-Small \
    -ngl 999 --n-cpu-moe 42 --flash-attn on -ctk f16 -ctv f16 \
    --jinja --reasoning-format auto --ctx-size "$C" \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.0 "${COMMON[@]}" ;;

dsv4split)    # DeepSeek V4 Flash two-box :<LOCAL> : card 0-7, RAM experts 8-17, Z13 18-42 (the gated default, IQ3, no draft)
  ping -c 1 -W 2 <LOCAL> >/dev/null || { echo "Z13 worker unreachable : skipping dsv4split"; exit 1; }
  bash "$R" dsv4split_262144 <LOCAL> <LOCAL> "$NOTHINK" 1800 "$RPC:$CU" 40 "$T" -- \
    "$RPC/llama-server" --model "$G/DeepSeek-V4-Flash/UD-IQ3_XXS/DeepSeek-V4-Flash-0731-UD-IQ3_XXS-00001-of-00004.gguf" \
    --host <LOCAL> --port <LOCAL> --alias DeepSeek-V4-Flash \
    --rpc <LOCAL> --device CUDA0,RPC0 --tensor-split 18,25 \
    --n-gpu-layers 999 --override-tensor 'blk\.(8|9|10|11|12|13|14|15|16|17)\.ffn_(up|down|gate)_exps=CPU,output\.weight=CUDA0' \
    --no-repack --flash-attn auto --jinja --reasoning-format deepseek --ctx-size "$C" \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 "${COMMON[@]}" ;;

qwen397)      # Qwen3.5-397B-A17B :<LOCAL> : NCMOE 57, --no-mmap, gated MTP, served non-thinking (Q397_THINK=off)
  bash "$R" qwen397_262144 <LOCAL> <LOCAL> "$NOTHINK" 1200 "$CU" 155 "$T" -- \
    "$Q35/llama-server" --model "$G/Qwen3.5-397B-A17B/UD-IQ3_XXS/Qwen3.5-397B-A17B-UD-IQ3_XXS-00001-of-00004.gguf" \
    --host <LOCAL> --port <LOCAL> --alias Qwen3.5-397B-A17B --jinja --ctx-size "$C" \
    --chat-template-kwargs '{"enable_thinking": false}' \
    --n-gpu-layers 999 --n-cpu-moe 57 --no-mmap \
    --spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min 0.75 --flash-attn on \
    --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 "${COMMON[@]}" ;;

dsv4q8)       # DeepSeek V4 Flash Q8 :<LOCAL> : all experts CPU-side; prefill ~75 t/s, so a 150K-token probe (still past 128K)
  bash "$R" dsv4q8_262144 <LOCAL> <LOCAL> "$NOTHINK" 1800 "$CU" 150 150000 -- \
    "$KIMI/llama-server" --model "$G/DeepSeek-V4-Flash/UD-Q8_K_XL/DeepSeek-V4-Flash-0731-UD-Q8_K_XL-00001-of-00005.gguf" \
    --host <LOCAL> --port <LOCAL> --alias DeepSeek-V4-Flash \
    --jinja --reasoning-format deepseek --ctx-size "$C" \
    --n-gpu-layers 999 -cmoe --no-repack --flash-attn auto \
    --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 "${COMMON[@]}" ;;

*) echo "unknown body: ${1:-<none>}" >&2; exit 2 ;;
esac
