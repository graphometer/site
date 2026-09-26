#!/usr/bin/env bash
D=<OUTPUT_DIR>
for k in Ling-3.0-flash Inkling-Small Qwen3.8-Flash-Next; do
  $D/bsweep_2026-09-20.sh ${k}_base  $k 131072 48000
  $D/bsweep_2026-09-20.sh ${k}_ub8192 $k 131072 48000 --batch-size 8192 --ubatch-size 8192
done
$D/bsweep_2026-09-20.sh Laguna-S-2.1_handflags_base   Laguna-S-2.1 32768 24000 --batch-size 512 --ubatch-size 128
$D/bsweep_2026-09-20.sh Laguna-S-2.1_handflags_ub4096 Laguna-S-2.1 32768 24000 --batch-size 4096 --ubatch-size 4096
echo "BSWEEP-COMPLETE"
