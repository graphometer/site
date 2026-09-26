#!/usr/bin/env bash
# series_probe.sh: load ONE model through its own start_server.sh (optionally with a batch override)
# and send a SERIES of sealed-code reads of the given sizes against that single load. Used to
# re-verify a shipped config the way users hit it: several requests, small and large, one server.
# Same needle and body as models/batch_sweep.sh (seed 20260920, code AMBER-3172-WILLOW), but each
# request gets its own seed so the prompt prefix never matches the previous one (no cache reuse).
#
#   usage: series_probe.sh <tag> <dir-under-gguf> <PFX> <port> <ubatch|skip> <size> [<size> ...]
#   e.g.   series_probe.sh Ling-3.0-flash_shipped Ling-3.0-flash LING <port> skip 3000 3000 48000 200000
set -u
TAG="$1"; DIR="$2"; PFX="$3"; PORT="$4"; UB="$5"; shift 5
OUT="<OUTPUT_DIR>/logs"; mkdir -p "$OUT"
LOG="$OUT/$TAG.log"; RES="$OUT/$TAG.result"
SCRIPT="<MODEL_DIR>/$DIR/start_server.sh"
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is already running" | tee "$RES"; exit 1; }
A=$(free -g | awk '/^Mem:/{print $7}'); [ "$A" -lt 100 ] && { echo "REFUSED: only ${A} GB RAM available" | tee "$RES"; exit 1; }
if [ "$UB" != "skip" ]; then export ${PFX}_UBATCH="$UB"; export ${PFX}_BATCH="$(( UB < 4096 ? 4096 : UB ))"; fi
# [a block configuring a private companion process was removed from this copy; it does not touch the measurement]
echo "[series] $TAG $DIR ubatch=$UB sizes=$*" | tee "$RES"
bash "$SCRIPT" ${SCRIPT_ARGS:-} > "$LOG" 2>&1 &   # SCRIPT_ARGS: positional args for scripts that take them (Laguna: ctx)
PID=$!
UP=""
for i in $(seq 1 240); do
  sleep 5
  kill -0 $PID 2>/dev/null || { echo "  DIED on load: $(grep -iE 'error|out of memory|REFUSED' "$LOG" | tail -1 | cut -c1-160)" | tee -a "$RES"; exit 1; }
  for h in 127.0.0.1 <LOCAL>; do
    curl -s -m 4 "http://$h:${PORT}/health" 2>/dev/null | grep -q ok && { UP=$h; break 2; }
  done
done
[ -z "$UP" ] && { echo "  never became healthy in 20 min" | tee -a "$RES"; kill $PID; exit 1; }
echo "  healthy in $((i*5))s · $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · host=$UP" | tee -a "$RES"
grep -oE 'n_ctx_slot = [0-9]+|n_batch *= *[0-9]+|n_ubatch *= *[0-9]+' "$LOG" | sort -u | tr '\n' ' ' | sed 's/^/  served: /' | tee -a "$RES"; echo | tee -a "$RES"
VRAMLOG="$OUT/$TAG.vram"
( while kill -0 $PID 2>/dev/null; do nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits; sleep 2; done ) > "$VRAMLOG" 2>/dev/null &
SAMPLER=$!
k=0
for SIZE in "$@"; do
  k=$((k+1))
  if ! kill -0 $PID 2>/dev/null; then echo "  #$k size=$SIZE SKIPPED: server is dead" | tee -a "$RES"; continue; fi
  SIZE="$SIZE" SEED="${SEED_FIXED:-$((20260920 + k))}" BASE="http://$UP:$PORT" python3 - <<'PY' 2>&1 | sed "s/^/  #$k /" | tee -a "$RES"
import os, sys, json, random, urllib.request, time
target = int(os.environ["SIZE"]); BASE = os.environ["BASE"]
rng = random.Random(int(os.environ["SEED"])); CODE = "AMBER-3172-WILLOW"
T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]
def line(i):
    return (f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve; reserve "
            f"{rng.randint(3,400)} units against {rng.randint(3,400)}.")
def body(n):
    ls = [line(i) for i in range(1, n + 1)]
    ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls)
def ntok(t):
    r = urllib.request.Request(BASE + "/tokenize", data=json.dumps({"content": t}).encode(),
                               headers={"Content-Type": "application/json"})
    return len(json.load(urllib.request.urlopen(r, timeout=900))["tokens"])
per = ntok(body(200)) / 200
n = max(50, int(target / per))
for _ in range(3):
    t = ntok(body(n))
    if abs(t - target) / target < 0.02: break
    n = max(50, int(n * target / t))
q = body(n) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
req = {"messages": [{"role": "user", "content": q}], "max_tokens": 900, "temperature": 0.0, "stream": False}
r = urllib.request.Request(BASE + "/v1/chat/completions", data=json.dumps(req).encode(),
                           headers={"Content-Type": "application/json"})
t0 = time.time()
try:
    d = json.load(urllib.request.urlopen(r, timeout=7200))
except Exception as e:
    print(json.dumps({"size": target, "error": f"{type(e).__name__}: {e}", "wall_s": round(time.time()-t0,1)})); sys.exit(0)
m = d["choices"][0]["message"]; c = (m.get("content") or "").strip(); rsn = (m.get("reasoning_content") or "").strip()
ti = d.get("timings", {})
print(json.dumps({"size": target, "prompt_n": ti.get("prompt_n"), "prefill_tps": round(ti.get("prompt_per_second", 0) or 0, 1),
                  "decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2), "needle_in_answer": CODE in c,
                  "needle_found": CODE in (c + " " + rsn), "answer_head": c[:60], "wall_s": round(time.time()-t0,1)}))
PY
done
kill $SAMPLER 2>/dev/null
echo "  peak VRAM: $(sort -n "$VRAMLOG" 2>/dev/null | tail -1) MiB · server alive at end: $(kill -0 $PID 2>/dev/null && echo yes || echo NO)" | tee -a "$RES"
grep -E 'illegal memory|CUDA error|out of memory|GGML_ASSERT|Aborted' "$LOG" | head -3 | sed 's/^/  LOG: /' | tee -a "$RES"
kill $PID 2>/dev/null; sleep 6; pkill -x llama-server 2>/dev/null; sleep 4
echo "  stopped · $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)" | tee -a "$RES"
