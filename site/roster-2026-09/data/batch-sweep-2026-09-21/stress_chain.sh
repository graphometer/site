#!/usr/bin/env bash
# stress_chain.sh — crash-check SHIPPED batch values, one model at a time, through their own scripts:
#   (1) a fresh load whose FIRST request is the exact harness prompt that crashed Ling-3.0-flash
#       (batch_sweep.sh body, seed 20260920, 3,000 tokens), then
#   (2) stress_model.py: N prompts of real code/prose sized around one and two ubatches.
# One summary line per step in logs/STRESS.txt.
#   usage: stress_chain.sh <n_prompts> "DIR:PFX:PORT:SEED" ...
set -u
D=<REDACTED_PATH>/$(date +%F)_batch-sweep; S="$D/logs/STRESS.txt"; N="$1"; shift
for spec in "$@"; do
  IFS=: read -r DIR PFX PORT SEED <<< "$spec"
  echo "$(date +%T) BEGIN $DIR" >> "$S"
  SEED_FIXED=20260920 "$D/series_probe.sh" "${DIR}_replay3000" "$DIR" "$PFX" "$PORT" skip 3000 > /dev/null 2>&1
  echo "$(date +%T)   replay3000: $(grep -E '#1 |DIED|SKIPPED|LOG:' "$D/logs/${DIR}_replay3000.result" | tr '\n' ' ' | cut -c1-260)" >> "$S"
  python3 "$D/stress_model.py" "$DIR" "$PFX" "$PORT" skip "$N" "$SEED" > "$D/logs/stress_${DIR}.out" 2>&1
  echo "$(date +%T)   stress: $(grep -E 'SUMMARY|CRASH|REFUSED|died|never' "$D/logs/stress_${DIR}.out" | tr '\n' ' ' | cut -c1-300)" >> "$S"
done
echo "$(date +%T) === STRESS CHAIN DONE ===" >> "$S"
