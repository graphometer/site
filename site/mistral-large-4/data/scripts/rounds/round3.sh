#!/usr/bin/env bash
# Large 4 round 3: T=16 kept. Routed experts only on the Z13, attention stays on the card; then T=20.
D=<REDACTED_PATH>
WT=300 LAYOUT=expz Z=26 GPU_N=2 CPUS=0-15 T=16 $D/run_ml4.sh l3-expz26-t16
WT=300 LAYOUT=back Z=26 GPU_N=4 CPUS=0-19 T=20 $D/run_ml4.sh l3-back26-t20
echo ROUND_DONE
