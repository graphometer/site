#!/usr/bin/env bash
# sweep_chain.sh: run models/batch_sweep.sh over ascending ubatch rungs for ONE model and stop at
# the first rung that dies, errors, loses the sealed code, or reads SLOWER than the rung before it
# (the handoff's rule: "stop at the first that OOMs or regresses"). One model at a time; each rung
# is a full load -> read -> stop through the model's own start_server.sh.
#
#   usage: sweep_chain.sh <dir-under-gguf> <PFX> <port> <probe_tokens> <ub> [<ub> ...]
#   e.g.   sweep_chain.sh Laguna-S-2.1 LAGUNA 8100 24000 2048 4096 8192
#
# Writes a one-line verdict per rung to logs/<dir>_chain.txt and exits 0 when the chain ends.
set -u
DIR="$1"; PFX="$2"; PORT="$3"; PROBE="$4"; shift 4
OUT="<OUTPUT_DIR>/logs"
mkdir -p "$OUT"
CHAIN="$OUT/${DIR}_chain.txt"
echo $$ > "$OUT/${DIR}_chain.pid"
prev=0
for ub in "$@"; do
  <TOOLS>/batch_sweep.sh "$DIR" "$PFX" "$PORT" "$ub" "$PROBE" > /dev/null 2>&1
  RES="$OUT/${DIR}_${ub}.result"
  js=$(grep -E '^\{' "$RES" | tail -1)
  if [ -z "$js" ] || echo "$js" | grep -q '"error"'; then
    echo "ub=$ub STOP: no answer ($(grep -E 'DIED|never|REFUSED|error' "$RES" | tail -1 | cut -c1-140))" | tee -a "$CHAIN"; break
  fi
  tps=$(echo "$js" | python3 -c 'import sys,json; print(json.load(sys.stdin)["prefill_tps"])')
  # A non-empty answer must itself carry the code; an EMPTY answer (thinking ate the budget) passes
  # on the reasoning alone: the handoff's max_tokens trap: and is visible in the logged JSON.
  ok=$(echo "$js" | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d["needle_found"] and (d["answer_len"] == 0 or d.get("needle_in_answer", True)))')
  echo "ub=$ub prefill=$tps needle_ok=$ok  $js" | tee -a "$CHAIN"
  [ "$ok" != "True" ] && { echo "ub=$ub STOP: sealed code not in the answer" | tee -a "$CHAIN"; break; }
  python3 -c "import sys; sys.exit(0 if $tps > $prev else 1)" || { echo "ub=$ub STOP: regressed ($tps <= $prev)" | tee -a "$CHAIN"; break; }
  prev=$tps
done
echo "=== chain done ===" | tee -a "$CHAIN"
rm -f "$OUT/${DIR}_chain.pid"
