#!/usr/bin/env bash
# Two-machine launcher for DeepSeek V4 Flash 0731. Heavily redacted: every path,
# address, port and machine label is replaced, and the refusal list of other local
# services is reduced to one line. The placement, window, threading, chat-format,
# draft and sampling flags are unchanged, and they are the flags the card describes.
# 
# split-launch.sh , DeepSeek V4 Flash 0731 (UD-Q8_K_XL, 150.8 GiB, 43 layers) split across the
# desktop and the Z13 over llama.cpp RPC. Two-box experiment, 2026-09-13. HAND-RUN ONLY, not a unit.
# Placement (defaults): layers 0..GPU_FULL-1 whole on the 5090 · layers GPU_FULL..HOST_LAYERS-1 attention
# on the 5090 + experts in desktop RAM · layers HOST_LAYERS..42 whole on the Z13 (Vulkan, unified memory).
# Refuses while any member of the bigmodel exclusion group is active , this IS a DeepSeek instance.
# STOP ORDER: stop this server first (Ctrl-C / kill), wait for it to exit, THEN stop the Z13 worker , the reverse
# order aborts the server on exit (dry run 2026-09-13: 'Remote RPC server crashed', harmless but ugly).
set -euo pipefail
S=<REDACTED_PATH>
BIN=$S/llama.cpp/build-cuda-rpc/bin/llama-server
MODEL="${MODEL:-<REDACTED_PATH>/DeepSeek-V4-Flash-0731-UD-Q8_K_XL-00001-of-00005.gguf}"   # override with MODEL=/path to test another quant of the same family
Z13="${Z13:-<LAPTOP>}"        # the Z13 worker; Ethernet fallback: Z13=<LAPTOP>
HOST_LAYERS="${HOST_LAYERS:-20}"      # layers 0..HOST_LAYERS-1 stay on the desktop; the rest go to the Z13
GPU_FULL="${GPU_FULL:-4}"               # of those, the first GPU_FULL keep their experts on the card
CTX="${CTX:-131072}"
HOST="${HOST:-127.0.0.1}"; PORT="${PORT:-8199}"   # bind address and port
N_LAYERS="${N_LAYERS:-43}"
LOG="${LOG:-$S/logs/split-$(date +%Y%m%d-%H%M%S).log}"; mkdir -p "$(dirname "$LOG")"

UNITS="<REDACTED: the list of this machine's other model services>"
for u in $UNITS; do :; done   # one model runs at a time
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is already running"; exit 3; }
avail_gb=$(awk '/MemAvailable/ {printf "%d", $2/1048576}' /proc/meminfo)
[ "$avail_gb" -ge 100 ] || { echo "REFUSED: only ${avail_gb} GiB RAM available (want >= 100)"; exit 3; }
timeout 3 bash -c "echo > /dev/tcp/${Z13%:*}/${Z13#*:}" 2>/dev/null || { echo "REFUSED: no RPC worker answering at $Z13 (start the worker script on the Z13)"; exit 4; }

# experts of the desktop's non-GPU-full layers -> host CPU (bounded regex: never touches the Z13's layers)
cpu_layers=""; for ((i=GPU_FULL; i<HOST_LAYERS; i++)); do cpu_layers+="${cpu_layers:+|}$i"; done
OT="blk\.(${cpu_layers})\.ffn_(up|down|gate)_exps=CPU,output\.weight=CUDA0"
Z13_LAYERS=$((N_LAYERS - HOST_LAYERS))
echo "split: desktop layers 0-$((HOST_LAYERS-1)) (GPU-full 0-$((GPU_FULL-1)), CPU experts ${GPU_FULL}-$((HOST_LAYERS-1)))  |  Z13 layers ${HOST_LAYERS}-$((N_LAYERS-1)) (${Z13_LAYERS})  |  ctx $CTX  |  log $LOG"
export LD_LIBRARY_PATH="<REDACTED_PATH>:${LD_LIBRARY_PATH:-}"
exec "$BIN" \
  --model "$MODEL" --alias "${ALIAS:-<MODEL_ALIAS>}" \
  --rpc "$Z13" --device "CUDA0,RPC0" --tensor-split "${HOST_LAYERS},${Z13_LAYERS}" \
  --n-gpu-layers 999 --override-tensor "$OT" --no-repack --flash-attn auto \
  --host "$HOST" --port "$PORT" --ctx-size "$CTX" --parallel 1 ${SLOT_SAVE_PATH:+--slot-save-path "$SLOT_SAVE_PATH"} \
  --jinja --reasoning-format deepseek --threads 24 --threads-batch 24 --timeout 3600 -lv 4 \
  ${DRAFT:+--spec-type draft-dspark --spec-draft-model "$DRAFT" --spec-draft-device CUDA0 --spec-draft-ngl 99 --spec-draft-n-max "${DRAFT_N:-6}" --spec-draft-p-min "${DRAFT_P:-0.5}"} \
  --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 \
  2>&1 | tee "$LOG"
