#!/usr/bin/env bash
# Large 4 round 6: experts in ordinary process memory on the desktop too, so huge pages take on both machines, with a batch-size timing and a real use at the end.
D=<REDACTED_PATH>
POST='python3 -I $D/batch_scan.py $U $N; python3 -I $D/usable_ml4.py $U $N 700' HUGE=1 PREFETCH=0 WT=300 LAYOUT=expz Z=30 GPU_N=3 CPUS=0-15 T=16 $D/run_ml4.sh l6-expz-nohost --load-mode dio --no-host
echo ROUND_DONE
