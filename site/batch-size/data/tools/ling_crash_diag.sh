#!/usr/bin/env bash
# ling_crash_diag.sh: DIAGNOSTIC ONLY (not a measurement of the shipped config). Runs the ling
# binary with the EXACT flags of <MODEL_DIR>/Ling-3.0-flash/start_server.sh's exec line (copied
# 2026-09-21; thinking on, MTP off) on a scratch port, with the window and batch
# given here, then sends the exact 2026-09-20 crash prompt (models/batch_sweep.sh body, seed
# 20260920, sized to ~3000 tokens = 3,007 tokens) and reports CRASH / OK.
# Positive control first: ctx 262144 + ub 4096 MUST crash, or this harness proves nothing.
#   usage: ling_crash_diag.sh <tag> <ctx> <ubatch> [<probe_tokens> [<seed>]]
set -u
TAG="$1"; CTX="$2"; UB="$3"; PROBE="${4:-3000}"; SEED="${5:-20260920}"
OUT=<OUTPUT_DIR>/logs; LOG="$OUT/diag_$TAG.log"
BIN=<llama.cpp build d3146f2b5>/llama-server
MODEL=<MODEL_DIR>/Ling-3.0-flash/Ling-3.0-flash-Q4_K_M/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is running"; exit 1; }
export LD_LIBRARY_PATH="<llama.cpp build d3146f2b5>:<CUDA 12.8 libraries>"
B=$(( UB < 4096 ? 4096 : UB ))
"$BIN" --model "$MODEL" --host 127.0.0.1 --port 8188 --alias ling-3.0-flash \
  --jinja --ctx-size "$CTX" --parallel 1 --batch-size "$B" --ubatch-size "$UB" \
  --n-gpu-layers 999 -cmoe --fit off --threads 24 --threads-batch 24 \
  --flash-attn auto --cors-origins localhost --timeout 3600 --top-p 0.95 --top-k 20 > "$LOG" 2>&1 &
PID=$!
for i in $(seq 1 120); do sleep 3; kill -0 $PID 2>/dev/null || { echo "$TAG DIED ON LOAD"; exit 1; }
  curl -s -m 3 http://127.0.0.1:8188/health | grep -q ok && break; done
R=$(PROBE="$PROBE" SEED="$SEED" python3 - <<'PY'
import os, json, random, urllib.request
target = int(os.environ["PROBE"]); BASE = "http://127.0.0.1:8188"
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
try:
    d = json.load(urllib.request.urlopen(r, timeout=3600))
    c = (d["choices"][0]["message"].get("content") or "").strip(); ti = d.get("timings", {})
    print(f"OK prompt_n={ti.get('prompt_n')} prefill={round(ti.get('prompt_per_second',0),1)} answer_ok={CODE in c}")
except Exception as e:
    print(f"NO-ANSWER {type(e).__name__}")
PY
)
if grep -q 'illegal memory access' "$LOG"; then V="CRASH (illegal memory access)"; else V="$R"; fi
echo "$TAG ctx=$CTX ub=$UB probe=$PROBE seed=$SEED -> $V"
kill $PID 2>/dev/null; sleep 5; pkill -x llama-server 2>/dev/null; sleep 3
