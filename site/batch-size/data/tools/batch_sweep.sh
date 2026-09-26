#!/usr/bin/env bash
# batch_sweep.sh: measure one roster model's READING speed at a given ubatch, through its own
# start script, and check the answer is still right.
#
# WHY THIS SHAPE. The 2026-09-20 sweep first replicated each model's llama-server flags by hand.
# That worked for four models and FAILED on Laguna, because the replication was wrong (its binary
# is Poolside's llama.cpp fork and it does not take --n-gpu-layers 999). Driving the model's OWN
# start_server.sh removes that whole class of mistake: the real binary, the real placement, the
# real guards, the real port.
#
# HOW THE OVERRIDE REACHES THE SCRIPT. Each start script sources its knob file near the top and
# then reads <PFX>_BATCH/<PFX>_UBATCH with ${VAR:-default} much further down. The knob files do
# NOT set those two, so a value exported here survives the sourcing and wins. Nothing on disk is
# edited. (If the script has no such knob yet, add it first: that is the change you are shipping
# anyway. Copy the shape from Ling-3.0-flash/start_server.sh.)
#
#   usage: batch_sweep.sh <dir-under-models/gguf> <PFX> <port> <ubatch|skip> <probe_tokens>
#   e.g.   batch_sweep.sh Ling-3.0-flash LING <port> 4096 48000
#          batch_sweep.sh Ling-3.0-flash LING <port> skip  48000     # baseline, no override
#
# Writes logs to <OUTPUT_DIR>/logs/. Stops the server at the end.
set -u
DIR="$1"; PFX="$2"; PORT="$3"; UB="$4"; PROBE="$5"
OUTDIR="<OUTPUT_DIR>"
mkdir -p "$OUTDIR/logs"
TAG="${DIR}_${UB}"
LOG="$OUTDIR/logs/$TAG.log"; RES="$OUTDIR/logs/$TAG.result"
SCRIPT="<MODEL_DIR>/$DIR/start_server.sh"

[ -x "$SCRIPT" ] || { echo "no start script: $SCRIPT" | tee "$RES"; exit 2; }
# ONE AT A TIME. The roster is a single exclusion group; the start script's own guards will also
# refuse, but failing here is cheaper and clearer.
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is already running" | tee "$RES"; exit 1; }
A=$(free -g | awk '/^Mem:/{print $7}')
[ "$A" -lt 100 ] && { echo "REFUSED: only ${A} GB RAM available" | tee "$RES"; exit 1; }

if [ "$UB" != "skip" ]; then
  export ${PFX}_UBATCH="$UB"
  # a batch below the ubatch is silently clamped; keep batch >= ubatch
  export ${PFX}_BATCH="$(( UB < 4096 ? 4096 : UB ))"
fi
# [a block configuring a private companion process was removed from this copy; it does not touch the measurement]
echo "[run] $DIR ubatch=${UB} $( [ "$UB" = skip ] && echo "(the script's own default)" )" | tee "$RES"

bash "$SCRIPT" > "$LOG" 2>&1 &
PID=$!
UP=""
for i in $(seq 1 240); do
  sleep 5
  kill -0 $PID 2>/dev/null || { echo "  DIED on load: $(grep -iE 'error|out of memory|REFUSED' "$LOG" | tail -1 | cut -c1-160)" | tee -a "$RES"; exit 1; }
  curl -s -m 4 "http://127.0.0.1:${PORT}/health" 2>/dev/null | grep -q ok && { UP=1; break; }
  curl -s -m 4 "http://<LOCAL>:${PORT}/health" 2>/dev/null | grep -q ok && { UP=1; break; }
done
[ -z "$UP" ] && { echo "  never became healthy in 20 min" | tee -a "$RES"; kill $PID; exit 1; }
HOSTBASE=$(curl -s -m 4 "http://127.0.0.1:${PORT}/health" 2>/dev/null | grep -q ok && echo 127.0.0.1 || echo <LOCAL>)
echo "  healthy in $((i*5))s · $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · host=$HOSTBASE" | tee -a "$RES"
# The window actually served, from the server's own log line: not what we think the knob file says.
grep -oE 'n_ctx_slot = [0-9]+|n_ctx *= *[0-9]+' "$LOG" | head -1 | sed 's/^/  served: /' | tee -a "$RES"
# Peak card memory DURING the read (2026-09-21): the compute buffer only fills while prefill runs,
# so the at-load reading understates what the card must hold.
VRAMLOG="$OUTDIR/logs/$TAG.vram"
( while kill -0 $PID 2>/dev/null; do nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits; sleep 2; done ) > "$VRAMLOG" 2>/dev/null &
SAMPLER=$!

PROBE="$PROBE" BASE="http://$HOSTBASE:$PORT" python3 - <<'PY' 2>&1 | tee -a "$RES"
import os, sys, json, random, urllib.request
target = int(os.environ["PROBE"]); BASE = os.environ["BASE"]
rng = random.Random(20260920); CODE = "AMBER-3172-WILLOW"
T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]
def line(i):
    return (f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve; reserve "
            f"{rng.randint(3,400)} units against {rng.randint(3,400)}.")
def body(n):
    ls = [line(i) for i in range(1, n + 1)]
    ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls)          # varied prose: repeated characters tokenize pathologically
def ntok(t):
    r = urllib.request.Request(BASE + "/tokenize", data=json.dumps({"content": t}).encode(),
                               headers={"Content-Type": "application/json"})
    return len(json.load(urllib.request.urlopen(r, timeout=900))["tokens"])
per = ntok(body(200)) / 200
n = max(50, int(target / per))
for _ in range(3):
    t = ntok(body(n))
    if abs(t - target) / target < 0.02:
        break
    n = max(50, int(n * target / t))
q = body(n) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
# max_tokens 900, NOT 64: several of these models think by default and a small budget is spent
# entirely on reasoning, returning an EMPTY answer that looks exactly like a corruption bug.
req = {"messages": [{"role": "user", "content": q}], "max_tokens": 900,
       "temperature": 0.0, "stream": False}
r = urllib.request.Request(BASE + "/v1/chat/completions", data=json.dumps(req).encode(),
                           headers={"Content-Type": "application/json"})
try:
    d = json.load(urllib.request.urlopen(r, timeout=7200))
except Exception as e:
    print(json.dumps({"error": f"{type(e).__name__}: {e}",
                      "note": "a dropped connection here usually means the server died mid-read "
                              ": the compute buffer did not fit. Try a smaller ubatch."}))
    sys.exit(0)
m = d["choices"][0]["message"]
c = (m.get("content") or "").strip()
rsn = (m.get("reasoning_content") or "").strip()
ti = d.get("timings", {})
print(json.dumps({"prompt_n": ti.get("prompt_n"),
                  "prefill_tps": round(ti.get("prompt_per_second", 0) or 0, 1),
                  "decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2),
                  "needle_found": CODE in (c + " " + rsn),
                  # 2026-09-21: the code in the ANSWER itself, and what the answer actually says :
                  # a corrupted reply can still quote the code inside its reasoning.
                  "needle_in_answer": CODE in c, "answer_head": c[:60],
                  "answer_len": len(c), "reasoning_len": len(rsn)}))
PY
kill $SAMPLER 2>/dev/null
echo "  peak VRAM during read: $(sort -n "$VRAMLOG" 2>/dev/null | tail -1) MiB" | tee -a "$RES"

kill $PID 2>/dev/null; sleep 6
pkill -x llama-server 2>/dev/null; sleep 4
echo "  stopped · $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)" | tee -a "$RES"
