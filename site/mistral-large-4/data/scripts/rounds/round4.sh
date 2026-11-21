#!/usr/bin/env bash
# Large 4 round 4, experts-only on the Z13: one more layer on the card and four more on the Z13, then a 128K window with no experts on the card.
D=<REDACTED_PATH>
WT=300 LAYOUT=expz Z=30 GPU_N=3 CPUS=0-15 T=16 $D/run_ml4.sh l4-expz30-g3
WT=300 LAYOUT=expz Z=30 GPU_N=1 CPUS=0-15 T=16 CTX=131072 $D/run_ml4.sh l4-expz30-g1-128k
echo ROUND_DONE
