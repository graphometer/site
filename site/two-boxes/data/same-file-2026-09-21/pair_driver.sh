#!/usr/bin/env bash
# series_probe2.sh — series_probe.sh for scripts other than start_server.sh (the two-box DeepSeek), with
# turn_probe.py (cold read + warm follow-up + next chat turn per size) and, for RPC runs, the <LAPTOP>'s GTT.
#   usage: series_probe2.sh <tag> <start-script> <PFX> <port> <ubatch|skip> <batch> <size> [<size> ...]
#   SCRIPT_ARGS: positional args for the script (split: "<ctx> <port>")
set -u
TAG="$1"; SCRIPT="$2"; PFX="$3"; PORT="$4"; UB="$5"; BATCH="$6"; shift 6
OUT="<REDACTED_PATH>/logs"; mkdir -p "$OUT"
LOG="$OUT/$TAG.log"; RES="$OUT/$TAG.result"
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is already running" | tee "$RES"; exit 1; }
A=$(free -g | awk '/^Mem:/{print $7}'); [ "$A" -lt 60 ] && { echo "REFUSED: only ${A} GB RAM available" | tee "$RES"; exit 1; }
if [ "$UB" != "skip" ]; then export ${PFX}_UBATCH="$UB"; export ${PFX}_BATCH="$BATCH"; fi
laptop_gtt() { ssh -o BatchMode=yes -o ConnectTimeout=5 <LAPTOP> 'echo $(( $(cat /sys/class/drm/card1/device/mem_info_gtt_used)/1048576 ))' 2>/dev/null || echo "?"; }
echo "[series2] $TAG $(basename "$SCRIPT") ubatch=$UB batch=$BATCH sizes=$* · <LAPTOP> GTT before $(laptop_gtt) MiB" | tee "$RES"
setsid bash "$SCRIPT" ${SCRIPT_ARGS:-} > "$LOG" 2>&1 &
PID=$!
UP=""
for i in $(seq 1 480); do
  sleep 5
  kill -0 $PID 2>/dev/null || { echo "  DIED on load: $(grep -iE 'error|out of memory|REFUSED' "$LOG" | tail -2 | tr '\n' ' ' | cut -c1-240)" | tee -a "$RES"; exit 1; }
  for h in 127.0.0.1 <LOCAL>; do
    curl -s -m 4 "http://$h:${PORT}/health" 2>/dev/null | grep -q ok && { UP=$h; break 2; }
  done
done
[ -z "$UP" ] && { echo "  never became healthy in 40 min" | tee -a "$RES"; kill -- -$PID 2>/dev/null; exit 1; }
echo "  healthy in $((i*5))s · card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · <LAPTOP> GTT $(laptop_gtt) MiB · host=$UP" | tee -a "$RES"
grep -oE 'n_ctx_slot = [0-9]+|n_batch *= *[0-9]+|n_ubatch *= *[0-9]+' "$LOG" | sort -u | tr '\n' ' ' | sed 's/^/  served: /' | tee -a "$RES"; echo | tee -a "$RES"
VRAMLOG="$OUT/$TAG.vram"
( while kill -0 $PID 2>/dev/null; do echo "$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits) $(laptop_gtt)"; sleep 5; done ) > "$VRAMLOG" 2>/dev/null &
SAMPLER=$!
python3 -u "$(dirname "$OUT")/turn_probe.py" "http://$UP:$PORT" 900 "$@" 2>&1 | sed -u 's/^/  /' | tee -a "$RES"
kill $SAMPLER 2>/dev/null
echo "  peak card $(sort -n -k1 "$VRAMLOG" | tail -1 | cut -d' ' -f1) MiB · peak <LAPTOP> GTT $(awk '$2 ~ /^[0-9]+$/' "$VRAMLOG" | sort -n -k2 | tail -1 | cut -d' ' -f2) MiB · server alive at end: $(kill -0 $PID 2>/dev/null && echo yes || echo NO)" | tee -a "$RES"
grep -E 'illegal memory|CUDA error|out of memory|GGML_ASSERT|Aborted|ErrorOutOf|WATCHDOG' "$LOG" | head -3 | sed 's/^/  LOG: /' | tee -a "$RES"
kill -- -$PID 2>/dev/null; for s in $(seq 1 40); do pgrep -x llama-server >/dev/null || break; sleep 1; done
pgrep -x llama-server >/dev/null && { kill -9 -- -$PID 2>/dev/null; sleep 3; }
sleep 3
echo "  stopped · card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · <LAPTOP> GTT $(laptop_gtt) MiB · llama-server left: $(pgrep -x llama-server | wc -l)" | tee -a "$RES"
