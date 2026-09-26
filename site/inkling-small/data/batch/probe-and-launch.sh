#   usage: bsweep.sh <tag> <public-model-name> <ctx> <probe_tokens> [extra args...]
set -u
TAG="$1"; MODEL_NAME="$2"; CTX="$3"; PROBE="$4"; shift 4
D=<REDACTED_PATH>
LOG="$D/logs/$TAG.log"; OUT="$D/logs/$TAG.result"
CU=<REDACTED_PATH>; G=<REDACTED_PATH>
case "$MODEL_NAME" in
  Inkling-Small)   BIN=<REDACTED_PATH>
             M=<REDACTED_PATH>
             PLACE=(-ngl 999 --n-cpu-moe 42 --flash-attn on -ctk f16 -ctv f16) ;;
  *) echo "unknown model"; exit 2 ;;
esac
export LD_LIBRARY_PATH="$(dirname "$BIN"):$CU"
pgrep -x llama-server >/dev/null && { echo "REFUSED: busy" | tee "$OUT"; exit 1; }
[ -f "$M" ] || { echo "REFUSED: model missing $M" | tee "$OUT"; exit 1; }
"$BIN" --model "$M" --host 127.0.0.1 --port <LOCAL_PORT> --alias Inkling-Small \
  --jinja --ctx-size "$CTX" --parallel 1 "${PLACE[@]}" \
  --threads 24 --threads-batch 24 --timeout 3600 "$@" > "$LOG" 2>&1 &
PID=$!
for i in $(seq 1 150); do sleep 5; kill -0 $PID 2>/dev/null || { echo "$TAG DIED: $(grep -iE 'error|out of memory' "$LOG"|tail -1|cut -c1-140)" | tee "$OUT"; exit 1; }
  grep -q "listening on http" "$LOG" && break; done
echo "[load] $TAG model=Inkling-Small ctx=$CTX vram=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader) load=$((i*5))s args='$*'" | tee "$OUT"
python3 - "$PROBE" <<'PY' 2>&1 | tee -a "$OUT"
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
req={"messages":[{"role":"user","content":q}],"max_tokens":900,"temperature":0.0,"stream":False}
r=urllib.request.Request("http://<LOCAL>/v1/chat/completions",data=json.dumps(req).encode(),
                         headers={"Content-Type":"application/json"})
d=json.load(urllib.request.urlopen(r,timeout=7200))
m=d["choices"][0]["message"]; c=(m.get("content") or "").strip()
rsn=(m.get("reasoning_content") or "").strip(); ti=d.get("timings",{})
print(json.dumps({"prompt_n":ti.get("prompt_n"),"prefill_tps":round(ti.get("prompt_per_second",0),1),
 "decode_tps":round(ti.get("predicted_per_second",0),2),"needle_found":CODE in (c+" "+rsn),
 "answer_len":len(c),"reasoning_len":len(rsn)}))
PY
kill $PID 2>/dev/null; sleep 6; pkill -x llama-server 2>/dev/null; sleep 4
