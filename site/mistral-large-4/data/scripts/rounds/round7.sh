#!/usr/bin/env bash
# Large 4 round 7: six more layers' experts on the Z13, 128K window, CUDA host memory back on the desktop, then the real use test with room for visible answers.
D=<REDACTED_PATH>
POST='python3 -I $D/usable_ml4.py $U $N 900' HUGE=1 PREFETCH=0 WT=300 LAYOUT=expz Z=36 GPU_N=1 CTX=131072 CPUS=0-15 T=16 $D/run_ml4.sh l7-expz36-g1-128k --load-mode dio
echo ROUND_DONE
