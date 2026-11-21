#!/usr/bin/env bash
# Large 4 round 1 on the installed b12015: last night's shape on a quiet box, then the Z13 at the front of the model (no shared-KV crossing).
D=<REDACTED_PATH>
LAYOUT=back Z=26 GPU_N=4 $D/run_ml4.sh l1-back26
LAYOUT=front Z=26 GPU_N=4 $D/run_ml4.sh l1-front26
echo ROUND_DONE
