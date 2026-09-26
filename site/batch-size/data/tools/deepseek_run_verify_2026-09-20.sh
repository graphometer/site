#!/usr/bin/env bash
D=<OUTPUT_DIR>
$D/deepseek_verify_2026-09-20.sh A_base_48k     quality 48000 -cmoe
$D/deepseek_verify_2026-09-20.sh B_ub2048_48k   quality 48000 -cmoe --batch-size 4096 --ubatch-size 2048
$D/deepseek_verify_2026-09-20.sh F_ub4096_48k   quality 48000 -cmoe --batch-size 4096 --ubatch-size 4096
$D/deepseek_verify_2026-09-20.sh G_fast_ub2048  fast    48000 --n-cpu-moe 36 --batch-size 4096 --ubatch-size 2048
echo "=== VERIFY SUMMARY ==="; cat $D/logs/v_*.result
