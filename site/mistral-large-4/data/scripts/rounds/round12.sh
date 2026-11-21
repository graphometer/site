#!/usr/bin/env bash
# Large 4 round 12: the new build (master + PR 31286) with the Z13 on Performance. First the final shape unchanged, then the hot-expert cache with CPU misses.
# The cache can hold only the experts in the desktop's RAM, and it needs card memory, so a smaller window or -ub pays for it. Largest cache first: that is the most this can give.
S=<REDACTED_PATH>; D=$S/ml4
bash $S/run_e3_q2.sh
pgrep -x llama-server > /dev/null && { echo "REFUSED: a llama-server is running"; echo ROUND_DONE; exit 3; }
Z=$(ssh <LAPTOP> "ss -ltnp | grep ':<PORT> ' | grep -o 'pid=[0-9]*' | head -1 | cut -d= -f2")
[ -n "$Z" ] && { ssh <LAPTOP> "kill $Z"; sleep 3; echo "stopped the b12015 worker, pid $Z"; }
export B=$S/llama.cpp-src/build/bin ZB=<REDACTED_PATH> PREFETCH=0 WT=500 RK=30000 QUICK=1 LAYOUT=expz Z=30 CPUS=0-15 T=16 GPU_N=0
CTX=131072 UB=1024 $D/run_ml4.sh l12-base --load-mode dio -lv 4
CTX=32768 UB=512 $D/run_ml4.sh l12-c12g-32k --load-mode dio -lv 4 --moe-cache-mib 12000 --moe-cache-cpu-share auto
CTX=65536 UB=1024 $D/run_ml4.sh l12-c5g-64k --load-mode dio -lv 4 --moe-cache-mib 5500 --moe-cache-cpu-share auto
CTX=131072 UB=512 $D/run_ml4.sh l12-c4g-128k --load-mode dio -lv 4 --moe-cache-mib 4000 --moe-cache-cpu-share auto
echo ROUND_DONE
