#!/usr/bin/env bash
# Small 4, one variant at a time, on the installed builds. Baseline first on a quiet box, then b12015 plain, then the expert cache, then ngram-mod.
cd <REDACTED_PATH>
K=<REDACTED_PATH>; B=<REDACTED_PATH>
./run_variant.sh older-build-repeat $K
LOADFLAG="--load-mode none" ./run_variant.sh b12015-plain-2 $B --fit off
LOADFLAG="--load-mode none" ./run_variant.sh b12015-cache19g $B --fit off --cpu-moe --moe-cache-mib 19000
LOADFLAG="--load-mode none" ./run_variant.sh b12015-ngram $B --fit off --spec-type ngram-mod
echo ROUND_DONE
