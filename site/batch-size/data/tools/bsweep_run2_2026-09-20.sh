#!/usr/bin/env bash
D=<OUTPUT_DIR>
$D/bsweep_2026-09-20.sh Ling-3.0-flash_base       Ling-3.0-flash    131072 48000
$D/bsweep_2026-09-20.sh Ling-3.0-flash_ub4096     Ling-3.0-flash    131072 48000 --batch-size 4096 --ubatch-size 4096
$D/bsweep_2026-09-20.sh Inkling-Small_ub2048  Inkling-Small 131072 48000 --batch-size 4096 --ubatch-size 2048
$D/bsweep_2026-09-20.sh Qwen3.8-Flash-Next_ub2048 Qwen3.8-Flash-Next 131072 48000 --batch-size 4096 --ubatch-size 2048
$D/bsweep_2026-09-20.sh Laguna-S-2.1_handflags_base     Laguna-S-2.1  32768 24000 --batch-size 512 --ubatch-size 128
$D/bsweep_2026-09-20.sh Laguna-S-2.1_handflags_ub2048   Laguna-S-2.1  32768 24000 --batch-size 4096 --ubatch-size 2048
echo "RUN2-COMPLETE"
