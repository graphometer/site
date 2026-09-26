#!/usr/bin/env bash
# Speed means nothing if the answer is garbage. Three open llama.cpp bugs hit THIS model on THIS
# card: #26509 (5090 + deepseek4 + flash-attn: a prompt spanning more than one forward pass emits
# only repeated '<'), #25382/#26423 (quantised K cache -> confident gibberish), #25582 (experts on
# CUDA -> garbled, proportional to how many). The sweep measured t/s and never read a reply.
# This plants a code at 50% depth of a multi-pass prompt and checks it comes back.
#   usage: verify.sh <tag> <preset> <probe_tokens> [extra args...]
set -u
TAG="$1"; PRESET="$2"; PROBE="$3"; shift 3
D=<REDACTED_PATH>
LOG="$D/logs/v_$TAG.log"; OUT="$D/logs/v_$TAG.result"
CU=<REDACTED_PATH>
case "$PRESET" in
  quality) BIN=<REDACTED_PATH>
           M=<REDACTED_PATH> ;;
  fast)    BIN=<REDACTED_PATH>
           M=<REDACTED_PATH> ;;
esac
export LD_LIBRARY_PATH="$(dirname "$BIN"):$CU"
pgrep -x llama-server >/dev/null && { echo "REFUSED: busy" | tee "$OUT"; exit 1; }
"$BIN" --model "$M" --host 127.0.0.1 --port <LOCAL_PORT> --alias DeepSeek-V4-Flash-0731 \
  --jinja --reasoning-format deepseek --ctx-size ${VCTX:-131072} --parallel 1 \
  --threads 24 --threads-batch 24 --n-gpu-layers 999 --no-repack --flash-attn auto \
  --timeout 3600 --temp 0 --top-p 1.0 --top-k 0 --min-p 0.05 "$@" > "$LOG" 2>&1 &
PID=$!
for i in $(seq 1 120); do sleep 5; kill -0 $PID 2>/dev/null || { echo "$TAG DIED" | tee "$OUT"; exit 1; }
  grep -q "listening on http" "$LOG" && break; done
echo "[load] $TAG vram=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader) args='$*'" | tee "$OUT"
python3 - "$PROBE" <<'PY'
import sys, json, random, urllib.request
target=int(sys.argv[1]); rng=random.Random(20260920); CODE="AMBER-3172-WILLOW"
T=["drainage of the upper meadow","insulation of the pump house","seasoning of the oak planks"]
def line(i): return (f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve; reserve "
                     f"{rng.randint(3,400)} units against {rng.randint(3,400)}.")
def body(n):
    ls=[line(i) for i in range(1,n+1)]
    ls[n//2]=f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls)
def ntok(t):
    r=urllib.request.Request("http://<LOCAL>/tokenize",data=json.dumps({"content":t}).encode(),
                             headers={"Content-Type":"application/json"})
    return len(json.load(urllib.request.urlopen(r,timeout=900))["tokens"])
per=ntok(body(200))/200; n=max(50,int(target/per))
for _ in range(3):
    t=ntok(body(n))
    if abs(t-target)/target<0.02: break
    n=max(50,int(n*target/t))
q=body(n)+"\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
# DeepSeek V4 Flash THINKS by default. A small budget is spent entirely on reasoning and the
# visible answer comes back EMPTY : measured here at max_tokens 64, on the baseline too, so it
# is the budget and not a corruption signature. 900 leaves room to reason AND answer.
req={"messages":[{"role":"user","content":q}],"max_tokens":900,"temperature":0.0,"stream":False}
r=urllib.request.Request("http://<LOCAL>/v1/chat/completions",data=json.dumps(req).encode(),
                         headers={"Content-Type":"application/json"})
d=json.load(urllib.request.urlopen(r,timeout=7200))
m=d["choices"][0]["message"]; c=(m.get("content") or "").strip()
rsn=(m.get("reasoning_content") or "").strip(); ti=d.get("timings",{})
both=c+" "+rsn
ok = CODE in both
# the #26509 signature is a reply made of repeated '<'
probe_txt = c or rsn
corrupt = (len(set(probe_txt.replace(" ","")))<=2 and len(probe_txt)>4) or probe_txt.count("<")>max(1,len(probe_txt))*0.5
print(json.dumps({"prompt_n":ti.get("prompt_n"),"prefill_tps":round(ti.get("prompt_per_second",0),1),
 "decode_tps":round(ti.get("predicted_per_second",0),2),"needle_found":ok,
 "looks_corrupt":bool(corrupt),"answer_len":len(c),"reasoning_len":len(rsn),"sample":(probe_txt[:70] if probe_txt else "<EMPTY>")}))
PY
kill $PID 2>/dev/null; sleep 6; pkill -x llama-server 2>/dev/null; sleep 4
