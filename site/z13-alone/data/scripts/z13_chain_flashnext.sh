#!/usr/bin/env bash
# z13_chain_flashnext.sh  -  Qwen3.8-Flash-Next UD-Q3_K_XL on the Z13 alone at its served 256K window, q8_0 K/V
# and thinking at medium effort (the desktop unit's knob file: FN_CTX=262144, FN_KV default q8_0, FN_THINK=on,
# FN_EFFORT=medium). Same llama.cpp commit as the desktop (d3146f2b5). -ub 512 (default) then 2048 (desktop's value).
set -u
D="<REDACTED_PATH>/RUN_DIR"
M="<REDACTED_PATH>/Qwen3.8-Flash-Next-UD-Q3_K_XL-00001-of-00003.gguf"
for ub in 512 2048; do
  "$D/z13_run2.sh" "fn_ctx256k_ub${ub}" "$M" 262144 "$ub" "3000 48000" \
    -ctk q8_0 -ctv q8_0 --chat-template-kwargs '{"reasoning_effort": "medium"}'
done
echo CHAIN-DONE
