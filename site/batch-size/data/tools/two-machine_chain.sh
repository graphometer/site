#!/usr/bin/env bash
# two-machine_chain.sh: batch sweep of the two-machine DeepSeek (IQ3, its served 262144 window, placement 8/10/25 from
# its settings file) through its own start script on a probe port (8188). -ub 512 = the current default, then 2048, 4096.
# Stops at the first rung that fails to load. Each rung: cold 3K + 48K reads, warm follow-up, next chat turn.
set -u
D=<OUTPUT_DIR>
S=<MODEL_DIR>/DeepSeek-V4-Flash/start_server_split.sh
for ub in 512 2048 4096; do
  b=$(( ub < 2048 ? 2048 : ub ))
  SCRIPT_ARGS="262144 8188" "$D/series_probe2.sh" "DeepSeek-V4-Flash-two-machine_ub${ub}" "$S" <PFX> 8188 "$ub" "$b" 3000 48000
  grep -q "DIED on load\|never became healthy\|REFUSED" "$D/logs/DeepSeek-V4-Flash-two-machine_ub${ub}.result" && { echo "STOP at ub $ub"; break; }
done
echo CHAIN-DONE
