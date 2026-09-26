#!/usr/bin/env bash
# z13_chain_ling104k.sh  -  the recommended Z13 body at a user depth: Ling-3.0-flash, 256K window, -ub 512,
# no MTP; one cold sealed-code read at ~104K (the deployment gate's deep rung for M2.7) + the warm follow-up.
set -u
D="<REDACTED_PATH>/RUN_DIR"
M="<REDACTED_PATH>/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf"
"$D/z13_run2.sh" ling_ctx256k_ub512_104k "$M" 262144 512 "104000"
echo CHAIN-DONE
