#!/usr/bin/env bash
# DeepSeek V4.1 launcher for the community port. Heavily redacted: every path, address,
# port and machine label is replaced, and the refusal list of other local services is
# reduced to one line. The streaming, context, sampling and draft flags are unchanged.
# 
# v41-launch.sh , DeepSeek V4.1 Flash on the desktop alone via a community port of llama.cpp: routed
# experts streamed from the home-drive NVMe through a VRAM cache and a pinned host tier; engram tables mmap'd.
# HAND-RUN experiment (2026-09-14). Knobs via env: CACHE (GiB VRAM expert cache, author 18), L2 (GiB pinned host
# tier, author 72 , we have 188 GiB), IOT (io threads, auto), CTX (author verified 4096), HOST/PORT, DRAFT=1 for
# the DSpark head. Refuses if any model unit / llama-server is up or RAM is short. Logs to logs/.
set -euo pipefail
Q=<REDACTED_PATH>
BIN=$Q/llama.cpp/build/bin/llama-server
D=<REDACTED_PATH>
MODEL=$D/main/DeepSeek-V4.1-Flash-MXFP4-engram-00001-of-00011.gguf
DRAFTF=$D/dspark/DeepSeek-V4.1-Flash-DSpark.gguf
CACHE="${CACHE:-18}"; L2="${L2:-72}"; IOT="${IOT:-}"; CTX="${CTX:-4096}"
HOST="${HOST:-127.0.0.1}"; PORT="${PORT:-8199}"; NGL="${NGL:-40}"
LOG="${LOG:-$Q/logs/server-$(date +%H%M%S)-c${CACHE}-l2${L2}-ctx${CTX}.log}"
[ -x "$BIN" ] || { echo "ERROR: build not finished ($BIN)"; exit 2; }
for i in $(seq -w 1 11); do f=$D/main/DeepSeek-V4.1-Flash-MXFP4-engram-000${i}-of-00011.gguf; [ -f "$f" ] || { echo "ERROR: shard $i missing , download incomplete"; exit 2; }; done
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is running"; exit 3; }
for u in <REDACTED: the list of this machine's other model services>; do :; done   # one model runs at a time
avail=$(awk '/MemAvailable/ {printf "%d", $2/1048576}' /proc/meminfo); need=$((L2 + 30))
[ "$avail" -ge "$need" ] || { echo "REFUSED: $avail GiB available, need >= $need (L2 $L2 + 30 for the engram page cache)"; exit 3; }
export LD_LIBRARY_PATH="$(dirname "$BIN"):<REDACTED_PATH>:${LD_LIBRARY_PATH:-}"
BATCHARGS=(); [ -n "${UB:-}" ] && BATCHARGS=(-ub "$UB" -b "${BATCH:-$UB}")
THINKARGS=(); [ "${THINK_OFF:-0}" = "1" ] && THINKARGS=(--chat-template-kwargs '{"enable_thinking": false}')
DRAFTARGS=(); [ "${DRAFT:-0}" = "1" ] && DRAFTARGS=(--spec-type draft-dspark --spec-draft-model "$DRAFTF" --spec-draft-n-max "${DRAFT_N:-2}" --spec-draft-device CUDA0 --spec-draft-ngl 99)
echo "V4.1 port: VRAM cache ${CACHE} GiB · host tier ${L2} GiB · io-threads ${IOT:-auto} · ctx $CTX · ngl $NGL · draft ${DRAFT:-0} · log $LOG"
exec "$BIN" --model "$MODEL" --alias <MODEL_ALIAS> \
  --moe-stream --moe-stream-cache "$CACHE" --moe-stream-l2 "$L2" ${IOT:+--moe-stream-io-threads "$IOT"} \
  -ngl "$NGL" --ctx-size "$CTX" --parallel 1 --host "$HOST" --port "$PORT" \
  --jinja --reasoning-format deepseek --threads 24 --threads-batch 24 --timeout 7200 \
  --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 -lv 3 "${BATCHARGS[@]}" "${THINKARGS[@]}" "${DRAFTARGS[@]}" 2>&1 | tee "$LOG"
