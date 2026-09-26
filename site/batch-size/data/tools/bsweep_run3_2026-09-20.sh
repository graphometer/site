#!/usr/bin/env bash
# Load-only at each model's REAL served window (262144), with the tuned batch. The sweep ran at
# 131072; the compute buffer and KV both grow with the window, so a value that fits at 128K can
# OOM at 256K: Qwen3.8-Flash-Next and Inkling-Small already proved they OOM at -ub 8192 at the SMALLER window.
D=<OUTPUT_DIR>
$D/bsweep_2026-09-20.sh Ling-3.0-flash_262k-confirm      Ling-3.0-flash      262144 3000 --batch-size 4096 --ubatch-size 4096
$D/bsweep_2026-09-20.sh Inkling-Small_262k-confirm   Inkling-Small   262144 3000 --batch-size 4096 --ubatch-size 2048
$D/bsweep_2026-09-20.sh Qwen3.8-Flash-Next_262k-confirm Qwen3.8-Flash-Next 262144 3000 --batch-size 4096 --ubatch-size 2048
echo "RUN3-COMPLETE"
