#!/usr/bin/env bash
# Large 4 round 5: experts in plain memory instead of a mapped file, huge pages on both machines. Same layout as the best so far, for a straight comparison.
D=<REDACTED_PATH>
Zpid=$(ssh <LAPTOP> "ss -ltnp | grep ':<PORT> ' | sed -E 's/.*pid=([0-9]+).*/\1/'")
[ -n "$Zpid" ] && { ssh <LAPTOP> "kill $Zpid"; sleep 4; }
ZENV="GLIBC_TUNABLES=glibc.malloc.hugetlb=1" HUGE=1 PREFETCH=0 WT=300 LAYOUT=expz Z=${Z5:-26} GPU_N=${G5:-2} CPUS=0-15 T=16 $D/run_ml4.sh l5-expz-huge --load-mode ${LM:-dio}
echo ROUND_DONE
