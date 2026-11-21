#!/usr/bin/env bash
# Large 4 round 10: the final shape with a plain Z13 worker (no huge pages, no spin), then speed and recall deep in the 128K window.
D=<REDACTED_PATH>
Zpid=$(ssh <LAPTOP> "ss -ltnp | grep ':<PORT> ' | sed -E 's/.*pid=([0-9]+).*/\1/'")
[ -n "$Zpid" ] && { ssh <LAPTOP> "kill $Zpid"; sleep 4; }
export PREFETCH=0 WT=300 RK=30000 QUICK=1 LAYOUT=expz Z=30 CTX=131072 CPUS=0-15 T=16 GPU_N=0 UB=1024
export POST='cd <REDACTED_PATH>; python3 -I smoke.py --url $U --label ml4-final --depths 48000,97000 --max-tokens 500 --skip-quick --pid $P 2>&1 | tail -12 | cut -c1-260'
$D/run_ml4.sh l10-final --load-mode dio
echo ROUND_DONE
