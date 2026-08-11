#!/usr/bin/env bash
# Mistral Large 3 UD-IQ1_S tuning ladder — Grant's go 2026-08-05, ceiling: ≥6 GiB VRAM free
# (used ≤ ~26,400 MiB incl. desktop). Arch facts: deepseek2, 61 blocks (3 dense), 128 experts
# (4 routed + 1 shared), 1 KV head. Each rung: start → health → warmup → timed gen → VRAM → stop.
set -uo pipefail
D=<VAULT>/work/agent-staging/claude/2026-08-04_model-advisors
M=<VAULT>/models/gguf/Mistral-Large-3/UD-IQ1_S/Mistral-Large-3-675B-Instruct-2512-UD-IQ1_S-00001-of-00004.gguf
BIN=<VAULT>/models/llamacpp-kimi/build/bin/llama-server
export LD_LIBRARY_PATH=<VAULT>/models/cuda-12.8/lib64:${LD_LIBRARY_PATH:-}
URL=http://127.0.0.1:8104
TSV=$D/l3_ladder_results.tsv
echo -e "rung\tconfig\tvram_mib\tdecode_tps\tprefill_tps\tnotes" > "$TSV"
PID=""

stop_server() { [[ -n "$PID" ]] && kill "$PID" 2>/dev/null; for i in $(seq 1 30); do kill -0 "$PID" 2>/dev/null || break; sleep 2; done; kill -9 "$PID" 2>/dev/null; PID=""; sleep 3; }
trap stop_server EXIT

gen() { # max_tokens, prompt -> "decode_tps prefill_tps"
  curl -s -m 900 "$URL/v1/chat/completions" -H 'Content-Type: application/json' \
    -d "{\"messages\":[{\"role\":\"user\",\"content\":$2}],\"max_tokens\":$1}" |
  python3 -c "import json,sys; t=json.load(sys.stdin).get('timings',{}); print(f\"{t.get('predicted_per_second',0):.2f} {t.get('prompt_per_second',0):.1f}\")" 2>/dev/null || echo "0 0"
}

rung() { # name, extra-args...
  local name="$1"; shift
  echo "=== RUNG $name : $* ($(date -Is))"
  "$BIN" -m "$M" --host 127.0.0.1 --port 8104 --alias mistral-large-3 \
    -ngl 99 --no-repack --jinja --flash-attn on --no-warmup "$@" \
    > "$D/ladder_$name.log" 2>&1 &
  PID=$!
  local ok=0
  for i in $(seq 1 80); do
    curl -sf -m 3 "$URL/health" >/dev/null 2>&1 && { ok=1; break; }
    kill -0 "$PID" 2>/dev/null || break
    sleep 10
  done
  if [[ $ok -ne 1 ]]; then
    echo -e "$name\t$*\tLOAD_FAIL\t0\t0\tserver died or 13min timeout (see ladder_$name.log tail)" >> "$TSV"
    tail -3 "$D/ladder_$name.log" | head -3; stop_server; return 1
  fi
  gen 48 '"Warm up: describe a lighthouse in one sentence."' >/dev/null
  local r vram
  r=$(gen 120 '"In about 100 words, explain why running AI models on personal hardware matters."')
  vram=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits)
  echo -e "$name\t$*\t$vram\t${r% *}\t${r#* }\tok" >> "$TSV"
  echo "RESULT $name: vram=${vram} MiB decode=${r% *} t/s prefill=${r#* } t/s"
}

# R1/R2 — how many MoE layers' routed experts fit on GPU under the ceiling (58 MoE layers total)
rung R1_ncmoe58_c8k  -c 8192  -b 2048 -ub 512 --n-cpu-moe 58
R1_VRAM=$(awk -F'\t' '$1=="R1_ncmoe58_c8k"{print $3}' "$TSV"); stop_server
if [[ "$R1_VRAM" != "LOAD_FAIL" && "${R1_VRAM:-30000}" -le 24200 ]]; then
  rung R2_ncmoe57_c8k -c 8192 -b 2048 -ub 512 --n-cpu-moe 57; stop_server
fi

# pick winner N by best decode among fitting rungs (fallback 55)
WINN=$(awk -F'\t' 'NR>1 && $3!="LOAD_FAIL" && $3<=26400 {if($4+0>b){b=$4+0;w=$2}} END{print w}' "$TSV" | grep -o 'n-cpu-moe [0-9]*' | awk '{print $2}'); WINN=${WINN:-58}
echo "WINNER n-cpu-moe = $WINN"

# R3 — context 32768 at winner placement (KV should be cheap: 1 KV head / MLA)
rung R3_ncmoe${WINN}_c32k -c 32768 -b 2048 -ub 512 --n-cpu-moe "$WINN"; stop_server

# R4 — --no-mmap attempt, guarded by available RAM
AVAIL=$(awk '/MemAvailable/{print int($2/1048576)}' /proc/meminfo)
if [[ $AVAIL -ge 165 ]]; then
  rung R4_nommap_c32k -c 32768 -b 2048 -ub 512 --n-cpu-moe "$WINN" --no-mmap; stop_server
else
  echo -e "R4_nommap_c32k\tskipped\t-\t-\t-\tMemAvailable ${AVAIL} GiB < 165 guard" >> "$TSV"
fi

# R5 — prefill throughput with a long prompt (~2.4k tokens), -ub 512 vs -ub 2048
LONG=$(python3 -c "print('\"'+('The vault holds many services and models. '*300)+'Summarize the previous text in one sentence.\"')")
rung R5_ub512_c32k  -c 32768 -b 2048 -ub 512  --n-cpu-moe "$WINN"
r=$(gen 64 "$LONG"); echo -e "R5_longprompt_ub512\tlong-prompt prefill\t-\t${r% *}\t${r#* }\tprefill on ~2.4k-tok prompt" >> "$TSV"; stop_server
rung R6_ub2048_c32k -c 32768 -b 4096 -ub 2048 --n-cpu-moe "$WINN"
r=$(gen 64 "$LONG"); echo -e "R6_longprompt_ub2048\tlong-prompt prefill\t-\t${r% *}\t${r#* }\tprefill on ~2.4k-tok prompt" >> "$TSV"; stop_server

echo "=== LADDER COMPLETE $(date -Is)"
column -t -s$'\t' "$TSV"
nvidia-smi --query-gpu=memory.used --format=csv,noheader
