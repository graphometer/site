#!/usr/bin/env bash
# Large 4 round 11: three experts per token instead of four, same shape. Speed and a look at the answers; a quality trade, not a free one.
D=<REDACTED_PATH>
export PREFETCH=0 WT=800 RK=9000 QUICK=1 LAYOUT=expz Z=30 CTX=131072 CPUS=0-15 T=16 GPU_N=0 UB=1024
$D/run_ml4.sh l11-expert3 --load-mode dio --override-kv mistral-large4.expert_used_count=int:3
echo ROUND_DONE
