#!/usr/bin/env bash
# ladder.sh — Qwen3.8-27B placement/profile ladder.
# For each profile: start llama-server, time the load, record RAW nvidia-smi MiB (never /1000),
# record RSS, run warm prose+structured decode reps, stop, verify GPU released.
# Every raw response is kept by ladder_probe.py under raw/.
set -u
D="$(cd "$(dirname "$0")" && pwd)"
BIN=<VAULT>/models/llamacpp-qwen35/build/bin/llama-server
MODEL=<VAULT>/models/gguf/Qwen3.8-27B/Qwen3.8-27B-UD-Q5_K_XL.gguf
PORT=8198
TSV="$D/ladder.tsv"
export LD_LIBRARY_PATH="<VAULT>/models/cuda-12.8/lib64:${LD_LIBRARY_PATH:-}"

[ -f "$TSV" ] || printf "profile\tctx\tmtp\tload_s\tvram_used_MiB\tvram_total_MiB\tvram_free_MiB\tRSS_GiB\tprose_tps\tstruct_tps\tprefill_tps\taccept_pct\tnote\n" > "$TSV"

run_profile () {
  local name="$1" ctx="$2" mtp="$3" pmin="${4:-0.75}"
  echo "=========== $name  (ctx=$ctx mtp=$mtp) ==========="
  local base_vram; base_vram=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits)
  local extra=()
  if [ "$mtp" = "yes" ]; then
    extra=(--spec-type draft-mtp --spec-draft-n-max 6 --spec-draft-p-min "$pmin")
  fi
  local t0 t1
  t0=$(date +%s.%N)
  "$BIN" --model "$MODEL" --host 127.0.0.1 --port "$PORT" --alias qwen3.8-27b \
    --jinja --ctx-size "$ctx" --parallel 1 --n-gpu-layers 999 \
    --threads 24 --threads-batch 24 --flash-attn on --timeout 3600 \
    --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 ${extra[@]+"${extra[@]}"} \
    > "$D/ladder_${name}.log" 2>&1 &
  local pid=$!
  for i in $(seq 1 300); do
    curl -s -m 2 "http://127.0.0.1:$PORT/health" 2>/dev/null | grep -q '"ok"' && break
    kill -0 $pid 2>/dev/null || { echo "SERVER DIED — see ladder_${name}.log"; tail -20 "$D/ladder_${name}.log"; return 1; }
    sleep 1
  done
  t1=$(date +%s.%N)
  local load_s; load_s=$(echo "$t1 - $t0" | bc)
  sleep 2
  local vram total rss
  vram=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits)
  total=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits)
  local spid; spid=$(pgrep -f "^$BIN --model $MODEL" | head -1)
  rss=$(awk -v r="$(ps -o rss= -p "$spid" | tr -d ' ')" 'BEGIN{printf "%.2f", r/1048576}')
  echo "load ${load_s}s  VRAM ${vram}/${total} MiB (baseline was ${base_vram})  RSS ${rss} GiB"

  PROBE_BASE="http://127.0.0.1:$PORT/v1" PROBE_OUT="$D" PROFILE="$name" \
    python3 "$D/ladder_probe.py" > "$D/ladder_${name}_probe.json" 2>&1
  local prose struct prefill accept
  prose=$(python3 -c "import json;d=json.load(open('$D/ladder_${name}_probe.json'));print(d['prose_tps_median'])" 2>/dev/null || echo "NA")
  struct=$(python3 -c "import json;d=json.load(open('$D/ladder_${name}_probe.json'));print(d['struct_tps_median'])" 2>/dev/null || echo "NA")
  prefill=$(python3 -c "import json;d=json.load(open('$D/ladder_${name}_probe.json'));print(d['prefill_tps'])" 2>/dev/null || echo "NA")
  accept=$(grep -oE "draft acceptance rate = [0-9.]+" "$D/ladder_${name}.log" | tail -1 | grep -oE "[0-9.]+$" || echo "NA")

  printf "%s\t%s\t%s\t%.2f\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
    "$name" "$ctx" "$mtp" "$load_s" "$vram" "$total" "$((total-vram))" "$rss" \
    "$prose" "$struct" "$prefill" "$accept" "warm page cache" >> "$TSV"

  kill "$pid" 2>/dev/null; wait "$pid" 2>/dev/null
  for i in $(seq 1 60); do pgrep -f "^$BIN --model $MODEL" >/dev/null || break; sleep 1; done
  sleep 3
  echo "after stop: VRAM $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits) MiB"
  echo
}

for spec in "$@"; do
  IFS=: read -r n c m pm <<< "$spec"
  run_profile "$n" "$c" "$m" "${pm:-0.75}"
done
column -t -s $'\t' "$TSV"
