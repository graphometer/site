#!/usr/bin/env bash
D=<REDACTED_PATH>
$D/sweep.sh A_baseline      quality 131072 16000 -cmoe
$D/sweep.sh B_ubatch2048    quality 131072 16000 -cmoe --batch-size 4096 --ubatch-size 2048
$D/sweep.sh C_ncmoe_q8      quality 131072 16000 --n-cpu-moe 50 --cache-type-k q8_0 --cache-type-v q8_0
$D/sweep.sh D_both          quality 131072 16000 --n-cpu-moe 50 --cache-type-k q8_0 --cache-type-v q8_0 --batch-size 4096 --ubatch-size 2048
$D/sweep.sh E_fast_preset   fast    131072 16000 --n-cpu-moe 36
echo "=== SUMMARY ==="; cat $D/logs/*.result
