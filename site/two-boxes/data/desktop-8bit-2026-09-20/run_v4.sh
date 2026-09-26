#!/usr/bin/env bash
D=<REDACTED_PATH>
# the shipping question: does -ub 8192 still fit AND stay correct at the full served window,
# read deep? The Arc report said large -ub can collapse long-prompt throughput.
VCTX=262144 $D/verify.sh W_256k_ub8192 quality 150000 -cmoe --batch-size 8192 --ubatch-size 8192
echo "V4-COMPLETE"
