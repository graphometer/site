#!/usr/bin/env bash
# One Small 4 variant, shipping settings, on loopback :<PORT>.
# b12015 refuses --no-mmap: set LOADFLAG="--load-mode none" and pass --fit off. Core load goes to logs/LABEL.cores.log.
# usage: run_variant.sh LABEL RT_DIR [extra llama-server args...]
set -uo pipefail
L=$1; RT=$2; shift 2
D=<REDACTED_PATH>
M=<REDACTED_PATH>/Mistral-Small-4-119B-2603-UD-Q4_K_M-00001-of-00003.gguf
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is running"; exit 3; }
g=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits); [ "$g" -lt 3000 ] || { echo "REFUSED: card in use, $g MiB"; exit 3; }
a=$(free -g | awk '/^Mem:/{print $7}'); [ "$a" -ge 70 ] || { echo "REFUSED: $a GB available"; exit 3; }
python3 -I "$D/cores.py" "$D/logs/$L.cores.log" & C=$!; trap 'kill $C 2>/dev/null' EXIT
export LD_LIBRARY_PATH="$RT:<REDACTED_PATH>" GOMP_SPINCOUNT=10000000
taskset -c 0-7 "$RT/llama-server" --model "$M" --host 127.0.0.1 --port <PORT> --alias mistral-small-4 --jinja --ctx-size 131072 --parallel 1 \
  --batch-size 8192 --ubatch-size 8192 --n-gpu-layers 999 --n-cpu-moe 26 ${LOADFLAG:---no-mmap} --threads 8 --threads-batch 8 \
  --flash-attn auto --timeout 3600 --temp 0.15 --top-p 1.0 --top-k 0 "$@" > "$D/logs/$L.server.log" 2>&1 &
P=$!; echo "$P" > "$D/logs/$L.pid"; S=$(date +%s)
for i in $(seq 1 180); do
  curl -sf -m 2 http://127.0.0.1:<PORT>/health >/dev/null && break
  kill -0 $P 2>/dev/null || { echo "$L: server died"; tail -5 "$D/logs/$L.server.log"; exit 4; }
  sleep 2
done
echo "$L: ready after $(( $(date +%s)-S )) s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits) MiB"
cd "$D"
python3 -I smoke.py --url http://127.0.0.1:<PORT> --label "$L" --depths 2000,48000,97000 --max-tokens 800 --pid $P 2>&1 | tail -12
python3 -I extra.py http://127.0.0.1:<PORT> "$L" 2>&1 | tail -5 | cut -c1-300
kill $P; for i in $(seq 1 30); do kill -0 $P 2>/dev/null || break; sleep 1; done
kill -0 $P 2>/dev/null && { kill -9 $P; echo "$L: needed kill -9"; }
sleep 5; echo "$L: stopped, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits) MiB"
