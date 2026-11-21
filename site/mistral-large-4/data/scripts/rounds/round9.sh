#!/usr/bin/env bash
# Large 4 round 9: 128K window, no whole layers on the card, read batch 1024 (2048 ran the card out of memory). Z13 worker keeps spinning between graphs.
D=<REDACTED_PATH>
export PREFETCH=0 WT=300 RK=30000 QUICK=1 LAYOUT=expz Z=30 CTX=131072 CPUS=0-15 T=16
GPU_N=0 UB=1024 $D/run_ml4.sh l9-expz30-g0-128k-ub1024 --load-mode dio
echo ROUND_DONE
