#!/usr/bin/env bash
# ===========================================================================
# run_warm.sh - does a RESTORED slot actually get reused on MiniMax M2.7?
# ===========================================================================
# The last technical unknown, and independent of prefill speed. WARM_WAKE_PLAN
# Phase 0's rule: ordinary attention restores (Qwen3-235B 434 s -> 0.62 s);
# sliding-window / DeltaNet restores and then recomputes everything (DeepSeek
# V4 Flash restored 727 MB in 0.14 s, then re-read all 102,852 tokens).
# M2.7's GGUF has no attention.sliding_window key, so it should restore.
# "Should" is not "does". This measures it.
#
# Full cycle, unattended: start -> seed 96K -> save -> STOP -> start again
# -> restore -> identical request -> verdict. The restart is real, not simulated.
# Uses the winning Phase A/B config. Guards, PID-file waits and VOID handling
# are m27_sweep.sh's; this script only drives the two phases around a restart.
# ===========================================================================
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

STAGE="<REDACTED_PATH>"
MODEL="$STAGE/MiniMax-M2.7-UD-IQ4_XS-00001-of-00004.gguf"
BIN="<REDACTED_PATH>"
HOST=127.0.0.1; PORT="<PORT>"
UB=4096; NCMOE=59; CTX=131072
TOKENS="${M27_WARM_TOKENS:-96000}"
STATE="${M27_WARM_STATE:-<REDACTED_PATH>}"
LOG=results/WARM.server.log
mkdir -p "$STATE" results

# --- the same refusals the sweep uses; an idle card is not permission --------
for u in "<server-alias>"; do
  systemctl is-active --quiet "$u" 2>/dev/null && { echo "REFUSED: unit '$u' is active."; exit 1; }
done
for d in /proc/[0-9]*; do
  pid="${d#/proc/}"; [ "$pid" = "$$" ] && continue; [ -r "$d/cmdline" ] || continue
  cmd="$(tr '\0' ' ' < "$d/cmdline" 2>/dev/null || true)"
  case "$cmd" in */llama-server\ *|*/llama-server)
    echo "REFUSED: pid $pid is already running a llama-server."; exit 1;; esac
done

start_server() {  # $1 = a label for the log
  echo ">> starting server ($1) -- -ub $UB --n-cpu-moe $NCMOE --slot-save-path $STATE"
  LD_LIBRARY_PATH="<REDACTED_PATH>" \
  "$BIN" --model "$MODEL" --host "$HOST" --port "$PORT" --alias <server-alias> \
    --jinja --ctx-size "$CTX" --parallel 1 \
    --threads 24 --threads-batch 24 \
    --n-gpu-layers 999 --n-cpu-moe "$NCMOE" \
    -b 4096 -ub "$UB" --no-repack --flash-attn on \
    --cache-type-k q8_0 --cache-type-v q8_0 \
    --slot-save-path "$STATE" --slots --timeout 3600 \
    >> "$LOG" 2>&1 &
  echo $! > results/warm.pid
  local pid t0; pid=$(cat results/warm.pid); t0=$(date +%s)
  while :; do
    kill -0 "$pid" 2>/dev/null || { echo "   VOID -- server exited during load"; tail -5 "$LOG"; return 1; }
    curl -fsS -m 5 "http://${HOST}:${PORT}/health" >/dev/null 2>&1 && break
    [ $(( $(date +%s) - t0 )) -gt 1800 ] && { echo "   VOID -- no health in 1800s (harness stall)"; kill -9 "$pid"; return 1; }
    sleep 5
  done
  echo "   healthy in $(( $(date +%s) - t0 ))s"
}

stop_server() {
  local pid; pid=$(cat results/warm.pid 2>/dev/null) || return 0
  echo ">> stopping server (pid $pid)"
  kill -INT "$pid" 2>/dev/null || true
  local t0; t0=$(date +%s)
  while kill -0 "$pid" 2>/dev/null; do
    [ $(( $(date +%s) - t0 )) -gt 120 ] && { kill -9 "$pid" 2>/dev/null; break; }
    sleep 2
  done
  rm -f results/warm.pid; echo "   stopped"
}

echo "=== PHASE 1: seed ${TOKENS} tokens and save the slot ==="
start_server seed || exit 1
python3 m27_warm_prove.py seed --url "http://${HOST}:${PORT}" --state-dir "$STATE" --tokens "$TOKENS"
stop_server

echo
echo "=== PHASE 2: a REAL restart, then restore and test reuse ==="
start_server check || exit 1
python3 m27_warm_prove.py check --url "http://${HOST}:${PORT}" --state-dir "$STATE"
stop_server

echo
echo "slot file left in $STATE for inspection; remove it when done:"
du -sh "$STATE" 2>/dev/null
