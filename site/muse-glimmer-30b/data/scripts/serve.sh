#!/usr/bin/env bash
# serve.sh <armname> [extra llama-server args...]
# Starts a FRESH llama-server for one study arm on :8195 and waits for health.
# Kills any prior server by PID from a pidfile (never pkill -f: the pattern
# matches this script's own command line and kills the caller).
set -u
ARM="$1"; shift
D=<VAULT>/work/agent-staging/fable/2026-08-16_muse-glimmer/runs/study
PIDF=$D/server.pid
mkdir -p "$D"

if [ -f "$PIDF" ]; then
  OLD=$(cat "$PIDF")
  if kill -0 "$OLD" 2>/dev/null; then kill "$OLD"; fi
  for _ in $(seq 30); do kill -0 "$OLD" 2>/dev/null || break; sleep 1; done
  rm -f "$PIDF"
fi

export LD_LIBRARY_PATH=<VAULT>/models/cuda-12.8/lib64:${LD_LIBRARY_PATH:-}
nohup <VAULT>/models/llamacpp-b10453/build/bin/llama-server \
  --model <VAULT>/models/gguf/Muse-Glimmer-30B/Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf \
  --host 127.0.0.1 --port 8195 --alias muse-glimmer-30b \
  --jinja --ctx-size 8192 --parallel 1 --n-gpu-layers 99 \
  --threads 24 --threads-batch 24 --flash-attn on --timeout 3600 \
  "$@" > "$D/${ARM}.log" 2>&1 &
echo $! > "$PIDF"
echo "started ${ARM} pid=$(cat $PIDF)"

for i in $(seq 90); do
  if curl -s --max-time 3 http://127.0.0.1:8195/health 2>/dev/null | grep -q '"ok"'; then
    echo "healthy after ${i}s"
    nvidia-smi --query-gpu=memory.used --format=csv,noheader
    exit 0
  fi
  sleep 1
done
echo "TIMEOUT waiting for health"; tail -20 "$D/${ARM}.log"; exit 1
