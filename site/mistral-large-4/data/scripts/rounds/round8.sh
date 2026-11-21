#!/usr/bin/env bash
# Large 4 round 8: no whole layers on the card and a bigger read batch, with the Z13 worker spinning between graphs as the desktop does.
D=<REDACTED_PATH>
Zpid=$(ssh <LAPTOP> "ss -ltnp | grep ':<PORT> ' | sed -E 's/.*pid=([0-9]+).*/\1/'")
[ -n "$Zpid" ] && { ssh <LAPTOP> "kill $Zpid"; sleep 4; }
export ZENV="GLIBC_TUNABLES=glibc.malloc.hugetlb=1 GOMP_SPINCOUNT=10000000" PREFETCH=0 WT=300 RK=30000 QUICK=1 LAYOUT=expz Z=30 CTX=131072 CPUS=0-15 T=16
GPU_N=0 UB=2048 $D/run_ml4.sh l8-expz30-g0-128k-ub2048 --load-mode dio
echo ROUND_DONE
