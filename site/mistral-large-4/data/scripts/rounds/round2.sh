#!/usr/bin/env bash
# Large 4 round 2 on the installed b12015: last night's shape with the E-cores joining, now that paging is out of the way.
D=<REDACTED_PATH>
WT=300 LAYOUT=back Z=26 GPU_N=4 CPUS=0-23 T=24 $D/run_ml4.sh l2-back26-t24
WT=300 LAYOUT=back Z=26 GPU_N=4 CPUS=0-15 T=16 $D/run_ml4.sh l2-back26-t16
echo ROUND_DONE
