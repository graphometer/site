#!/usr/bin/env bash
# z13_run2.sh  -  ONE model on the Z13 alone (Vulkan, llama.cpp d3146f2b5 = build 10919), bound to 127.0.0.1
# only, then sealed-code reads (same body/seeds as the desktop harness), peak GTT/RAM, stop.
# Run 2 (2026-09-21 ~19:50): same runner, but the probe is z13_probe.py (cold sealed-code read, then a warm
# follow-up on the same ledger) and its output is unbuffered.
# Refuses if any llama-server already runs here.
#   usage: z13_run2.sh <tag> <model.gguf> <ctx> <ubatch> <sizes "3000 48000"> [extra llama-server args...]
set -u
TAG="$1"; MODEL="$2"; CTX="$3"; UB="$4"; SIZES="$5"; shift 5
D="<REDACTED_PATH>/RUN_DIR"; mkdir -p "$D"
BIN="<REDACTED_PATH>/llama-server"
export LD_LIBRARY_PATH="$(dirname "$BIN")${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
LOG="$D/$TAG.server.log"; RES="$D/$TAG.result"; PORT=18200
for p in $(pgrep -x llama-server); do echo "REFUSED: llama-server pid $p already running" | tee "$RES"; exit 1; done
[ -f "$MODEL" ] || { echo "REFUSED: no model $MODEL" | tee "$RES"; exit 1; }
B=$(( UB < 2048 ? 2048 : UB ))
echo "[z13] $TAG ctx=$CTX -b $B -ub $UB extra: $*" | tee "$RES"
"$BIN" --model "$MODEL" --host 127.0.0.1 --port $PORT --jinja --ctx-size "$CTX" --parallel 1 \
  -ngl 999 -fa on -b "$B" -ub "$UB" -t 16 --timeout 3600 "$@" > "$LOG" 2>&1 &
PID=$!; echo $PID > "$D/$TAG.pid"
T0=$(date +%s)
until curl -sf -m 3 http://127.0.0.1:$PORT/health | grep -q '"ok"'; do
  kill -0 $PID 2>/dev/null || { echo "  DIED on load: $(grep -iE 'error|failed|out of' "$LOG" | tail -2 | tr '\n' ' ' | cut -c1-220)" | tee -a "$RES"; rm -f "$D/$TAG.pid"; exit 1; }
  [ $(( $(date +%s) - T0 )) -gt 1500 ] && { echo "  never healthy in 25 min" | tee -a "$RES"; kill $PID; exit 1; }
  sleep 5
done
G=/sys/class/drm/card1/device; [ -f $G/mem_info_gtt_used ] || G=$(dirname $(ls /sys/class/drm/card*/device/mem_info_gtt_used | head -1))
echo "  healthy in $(( $(date +%s) - T0 ))s · GTT $(( $(cat $G/mem_info_gtt_used)/1048576 )) MiB · RAM avail $(free -g | awk '/Mem:/{print $7}') GB · $(grep -oE 'n_ctx_slot = [0-9]+' "$LOG" | head -1)" | tee -a "$RES"
( while kill -0 $PID 2>/dev/null; do echo "$(( $(cat $G/mem_info_gtt_used)/1048576 )) $(free -m | awk '/Mem:/{print $3}')"; sleep 2; done ) > "$D/$TAG.mem" 2>/dev/null &
SAMP=$!
python3 -u "$D/z13_probe.py" http://127.0.0.1:$PORT 900 $SIZES 2>&1 | sed -u 's/^/  /' | tee -a "$RES"
kill $SAMP 2>/dev/null
echo "  peak GTT $(sort -n "$D/$TAG.mem" | tail -1 | cut -d' ' -f1) MiB · peak RAM used $(sort -k2 -n "$D/$TAG.mem" | tail -1 | cut -d' ' -f2) MiB · server alive: $(kill -0 $PID 2>/dev/null && echo yes || echo NO)" | tee -a "$RES"
grep -E 'CUDA error|vk::|ErrorOutOf|GGML_ASSERT|failed to allocate' "$LOG" | head -3 | sed 's/^/  LOG: /' | tee -a "$RES"
kill $PID 2>/dev/null; for i in $(seq 1 30); do kill -0 $PID 2>/dev/null || break; sleep 1; done; kill -9 $PID 2>/dev/null
rm -f "$D/$TAG.pid"; sleep 2
echo "  stopped · GTT $(( $(cat $G/mem_info_gtt_used)/1048576 )) MiB" | tee -a "$RES"
