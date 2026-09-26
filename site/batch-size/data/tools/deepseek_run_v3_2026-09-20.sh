#!/usr/bin/env bash
D=<OUTPUT_DIR>
$D/deepseek_verify_2026-09-20.sh V_base    quality 48000 -cmoe
$D/deepseek_verify_2026-09-20.sh V_ub4096  quality 48000 -cmoe --batch-size 4096 --ubatch-size 4096
$D/deepseek_verify_2026-09-20.sh V_ub8192  quality 48000 -cmoe --batch-size 8192 --ubatch-size 8192
echo "V3-COMPLETE"
