#!/usr/bin/env bash
D=<REDACTED_PATH>
$D/verify.sh V_base    quality 48000 -cmoe
$D/verify.sh V_ub4096  quality 48000 -cmoe --batch-size 4096 --ubatch-size 4096
$D/verify.sh V_ub8192  quality 48000 -cmoe --batch-size 8192 --ubatch-size 8192
echo "V3-COMPLETE"
