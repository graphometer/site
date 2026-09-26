#!/usr/bin/env bash
# z13_chain_ling.sh  -  Ling-3.0-flash Q4_K_M on the Z13 alone at its served 256K window, thinking on (the desktop
# unit's knob file: LING_CTX=262144, LING_THINK=on, LING_MTP=off; default f16 K/V). Same llama.cpp commit as
# the desktop (d3146f2b5). -ub 512 (default), then 2048 (the desktop's shipped value), then 2048 with the built-in
# MTP draft on  -  the desktop card measured only +4% from it because its experts sit in CPU RAM; here every
# weight is resident, which is the case its start script says "should matter much more".
set -u
D="<REDACTED_PATH>/RUN_DIR"
M="<REDACTED_PATH>/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf"
"$D/z13_run2.sh" ling_ctx256k_ub512      "$M" 262144 512  "3000 48000"
"$D/z13_run2.sh" ling_ctx256k_ub2048     "$M" 262144 2048 "3000 48000"
"$D/z13_run2.sh" ling_ctx256k_ub2048_mtp "$M" 262144 2048 "3000 48000" --spec-type draft-mtp
echo CHAIN-DONE
