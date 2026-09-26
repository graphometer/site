#!/usr/bin/env bash
# queue_runner.sh: for each model given as DIR:PFX:PORT:PROBE, run the baseline (the script's own
# defaults, "skip") and then the ascending ubatch chain, one model at a time. Each step goes through
# the model's own start_server.sh via models/batch_sweep.sh; sweep_chain.sh stops a model's chain at
# its first death / missing code / regression. A marker line per step goes to logs/QUEUE.txt.
#
#   usage: queue_runner.sh "<model-dir>:<PFX>:<port>:48000" ...
#   rungs: RUNGS env (default "2048 4096 8192")
set -u
D=<OUTPUT_DIR>
Q="$D/logs/QUEUE.txt"
echo $$ > "$D/logs/QUEUE.pid"
for spec in "$@"; do
  IFS=: read -r DIR PFX PORT PROBE <<< "$spec"
  echo "$(date +%T) BEGIN $DIR ($PFX :$PORT, probe $PROBE)" >> "$Q"
  <TOOLS>/batch_sweep.sh "$DIR" "$PFX" "$PORT" skip "$PROBE" > /dev/null 2>&1
  echo "$(date +%T)   baseline: $(grep -E '^\{|DIED|never|REFUSED' "$D/logs/${DIR}_skip.result" | tail -1 | cut -c1-220)" >> "$Q"
  "$D/sweep_chain.sh" "$DIR" "$PFX" "$PORT" "$PROBE" ${RUNGS:-2048 4096 8192} > /dev/null 2>&1
  sed 's/^/           /' "$D/logs/${DIR}_chain.txt" | cut -c1-230 >> "$Q"
  echo "$(date +%T) END $DIR · card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)" >> "$Q"
done
echo "$(date +%T) === QUEUE DONE ===" >> "$Q"
rm -f "$D/logs/QUEUE.pid"
