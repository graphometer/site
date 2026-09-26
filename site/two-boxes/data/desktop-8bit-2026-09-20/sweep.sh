#!/usr/bin/env bash
# DeepSeek V4 Flash: reading-speed sweep. The quality preset puts EVERY expert on the CPU (-cmoe) and
# uses only 17.8 GB of a 32.6 GB card; the two levers are the spare card space and the batch sizes
# (llama.cpp defaults, never tuned here).
#   usage: sweep.sh <tag> <preset> <ctx> <probe_tokens> [extra llama-server args...]
set -u
TAG="$1"; PRESET="$2"; CTX="$3"; PROBE="$4"; shift 4
D=<REDACTED_PATH>
LOG="$D/logs/$TAG.log"; OUT="$D/logs/$TAG.result"
CU=<REDACTED_PATH>/lib64
case "$PRESET" in
  quality) BIN=<REDACTED_PATH>/llama-server
           M=<REDACTED_PATH>/DeepSeek-V4-Flash-0731-UD-Q8_K_XL-00001-of-00005.gguf ;;
  fast)    BIN=<REDACTED_PATH>/llama-server
           M=<REDACTED_PATH>/DeepSeek-V4-Flash-0731-UD-IQ3_XXS-00001-of-00004.gguf ;;
  *) echo "bad preset"; exit 2 ;;
esac
export LD_LIBRARY_PATH="$(dirname "$BIN"):$CU"
pgrep -x llama-server >/dev/null && { echo "REFUSED: llama-server already running" | tee "$OUT"; exit 1; }
A=$(free -g | awk '/^Mem:/{print $7}'); [ "$A" -lt 100 ] && { echo "REFUSED: ${A}GB avail" | tee "$OUT"; exit 1; }

"$BIN" --model "$M" --host 127.0.0.1 --port <PORT> --alias <ALIAS> \
  --jinja --reasoning-format deepseek --ctx-size "$CTX" --parallel 1 \
  --threads 24 --threads-batch 24 --n-gpu-layers 999 --no-repack --flash-attn auto \
  --timeout 3600 --temp 1.0 --top-p 1.0 --top-k 0 --min-p 0.05 "$@" > "$LOG" 2>&1 &
PID=$!
UP=""
for i in $(seq 1 120); do sleep 5; kill -0 $PID 2>/dev/null || { echo "$TAG DIED on load — $(grep -iE 'error|out of memory' "$LOG"|tail -1|cut -c1-160)" | tee "$OUT"; exit 1; }
  grep -q "listening on http" "$LOG" && { UP=1; break; }; done
[ -z "$UP" ] && { echo "$TAG never came up" | tee "$OUT"; kill $PID; exit 1; }
V=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits|head -1)
echo "[load] $TAG preset=$PRESET ctx=$CTX vram=${V}MiB load=$((i*5))s args='$*'" | tee "$OUT"

python3 - "$PROBE" > <REDACTED_PATH>/_dsprobe.json <<'PY'
import sys, json, random, urllib.request
target=int(sys.argv[1]); rng=random.Random(20260920)
T=["drainage of the upper meadow","insulation of the pump house","seasoning of the oak planks",
   "repair of the east sluice","survey of the lower orchard","restocking of the grain loft"]
def line(i): return (f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve, who noted the "
                     f"reserve stood at {rng.randint(3,400)} units against {rng.randint(3,400)}.")
def body(n): return "\n".join(line(i) for i in range(1,n+1))
def ntok(t):
    r=urllib.request.Request("http://<LOCAL>/tokenize",data=json.dumps({"content":t}).encode(),
                             headers={"Content-Type":"application/json"})
    return len(json.load(urllib.request.urlopen(r,timeout=900))["tokens"])
per=ntok(body(200))/200; n=max(50,int(target/per))
for _ in range(3):
    t=ntok(body(n))
    if abs(t-target)/target < 0.02: break
    n=max(50,int(n*target/t))
json.dump({"messages":[{"role":"user","content":body(n)+"\n\nReply with the single word: ready"}],
           "max_tokens":8,"temperature":0.0,"stream":False}, open("<REDACTED_PATH>/_dsreq.json","w"))
print(json.dumps({"entries":n,"tokens":t}))
PY
cat <REDACTED_PATH>/_dsprobe.json | tee -a "$OUT"
curl -s -m 7200 http://<LOCAL>/v1/chat/completions -H 'Content-Type: application/json' \
  --data-binary @<REDACTED_PATH>/_dsreq.json > <REDACTED_PATH>/_dsresp.json
python3 -c "
import json;d=json.load(open('<REDACTED_PATH>/_dsresp.json'));t=d.get('timings',{})
print('[read] prompt_n=%d prefill=%.2f t/s (%.1f min) decode=%.2f t/s'%(
 t.get('prompt_n',0), t.get('prompt_per_second',0) or 0, (t.get('prompt_ms',0) or 0)/60000,
 t.get('predicted_per_second',0) or 0))" | tee -a "$OUT"
echo "[peak] $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)" | tee -a "$OUT"
kill $PID 2>/dev/null; sleep 6; pkill -x llama-server 2>/dev/null; sleep 4
