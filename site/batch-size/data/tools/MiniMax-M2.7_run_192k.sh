#!/usr/bin/env bash
# Can M2.7 serve its FULL native window (196,608) on one card?
# Arithmetic: 62 layers x 8 KV heads x 128 x 2 = 126,976 elem/token.
# At q8_0 (~1.0625 B/elem) 192K of KV = ~24.7 GiB, leaving ~7 GiB for the
# resident weights and the compute buffer. The compute buffer scales with -ub,
# so descend -ub until it fits.
# An OOM here is a MEASUREMENT, not a failure: run_one records it VOID.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
for ub in 4096 2048 1024; do
  echo "### 192K feasibility at -ub ${ub}"
  bash MiniMax-M2.7_sweep.sh one "$ub" cmoe 196608 4096 && echo "   ^ FIT at -ub ${ub}" || echo "   ^ did not fit at -ub ${ub}"
done
