#!/usr/bin/env bash
# Large 4 round 13: how far the cache can take full quality. A 32K window leaves the most card memory: the budget is 32,088 MiB less about 1,920 unaccounted, 17,133 model, 2,620 KV, 1,894 compute at -ub 1024.
S=<REDACTED_PATH>; D=$S/ml4
export B=$S/llama.cpp-src/build/bin ZB=<REDACTED_PATH> PREFETCH=0 WT=500 RK=30000 QUICK=1 LAYOUT=expz Z=30 CPUS=0-15 T=16 GPU_N=0
CTX=32768 UB=1024 $D/run_ml4.sh l13-c8g-32k --load-mode dio -lv 4 --moe-cache-mib 8000 --moe-cache-cpu-share auto
echo ROUND_DONE
