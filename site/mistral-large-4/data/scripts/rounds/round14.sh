#!/usr/bin/env bash
# Large 4 round 14: the recommended shape proved the way the final shape was: sealed codes at depth, a tool round-trip, a conversation. Then the plain shape on the same build, to compare top probabilities token by token.
S=<REDACTED_PATH>; D=$S/ml4
export B=$S/llama.cpp-src/build/bin ZB=<REDACTED_PATH> PREFETCH=0 WT=300 RK=9000 QUICK=1 LAYOUT=expz Z=30 CPUS=0-15 T=16 GPU_N=0
export POST='cd <REDACTED_PATH>; python3 -I smoke.py --url $U --label ml4-c5g-64k --depths 48000 --max-tokens 500 --skip-quick --pid $P 2>&1 | tail -4 | cut -c1-240; python3 -I $D/usable_ml4.py $U l14-c5g-64k 900 2>&1 | cut -c1-240; python3 -I $D/logit_check.py $U l14-c5g-64k'
CTX=65536 UB=1024 $D/run_ml4.sh l14-c5g-64k --load-mode dio -lv 4 --moe-cache-mib 5500 --moe-cache-cpu-share auto
export POST='python3 -I $D/logit_check.py $U l14-plain'
CTX=131072 UB=1024 $D/run_ml4.sh l14-plain --load-mode dio
echo ROUND_DONE
