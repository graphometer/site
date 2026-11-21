#!/usr/bin/env bash
# Small 4 on the new build (master + PR 31286), and pinned memory. The docs say -lm dio can pin the experts, which should speed cache uploads; the first variant tests that on the installed b12015, so it would need no new build.
cd <REDACTED_PATH>
OLD=<REDACTED_PATH>; NEW=<REDACTED_PATH>
LOADFLAG="--load-mode dio" ./run_variant.sh b12015-dio-cache-ngram $OLD --fit off --cpu-moe --moe-cache-mib 19000 --spec-type ngram-mod
LOADFLAG="--load-mode none" ./run_variant.sh new-auto-ngram $NEW --fit off --cpu-moe --moe-cache-mib 19000 --moe-cache-cpu-share auto --spec-type ngram-mod
LOADFLAG="--load-mode dio" ./run_variant.sh new-dio-auto-ngram $NEW --fit off --cpu-moe --moe-cache-mib 19000 --moe-cache-cpu-share auto --spec-type ngram-mod
echo S4_DONE
