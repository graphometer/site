#!/usr/bin/env bash
# run_hard.sh - one config: start llama-server on the probe port, read a long ledger once, then ask
# three graded questions against the cached prefix, score them, and stop. Touches nothing on disk
# outside this directory and never starts the live :<PORT> unit.
#   usage: run_hard.sh <tag> <ctx> <target_tokens> <ncmoe> <ctk> <ctv> <rope_target|0>
set -u
TAG="$1"; CTX="$2"; TARGET="$3"; NCMOE="$4"; CTK="$5"; CTV="$6"; ROPE="$7"
DIR="<REDACTED_PATH>"
Q="$DIR/q/$TAG"; mkdir -p "$Q"
LOG="$DIR/logs/hard_${TAG}.log"; OUT="$DIR/logs/hard_${TAG}.result"
BIN="<REDACTED_PATH>"
M="<REDACTED_PATH>"/Qwen3.8-Flash-Next-UD-Q3_K_XL-00001-of-00003.gguf
S="http://127.0.0.1:<PORT>"
export LD_LIBRARY_PATH="<REDACTED_PATH>"

pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is already running" | tee "$OUT"; exit 1; }
AVAIL=$(free -g | awk '/^Mem:/{print $7}')
[ "$AVAIL" -lt 100 ] && { echo "REFUSED: only ${AVAIL} GB available (<100 GB floor)" | tee "$OUT"; exit 1; }

ROPEARGS=()
[ "$ROPE" != "0" ] && ROPEARGS=(--rope-scaling yarn --rope-scale 1.0001 --yarn-orig-ctx "$ROPE")

"$BIN" --model "$M" --host 127.0.0.1 --port <PORT> --alias <server-alias> \
  --jinja --ctx-size "$CTX" --parallel 1 \
  "${ROPEARGS[@]}" --cache-type-k "$CTK" --cache-type-v "$CTV" \
  --n-gpu-layers 99 --n-cpu-moe "$NCMOE" --fit off \
  --threads 24 --threads-batch 24 \
  --flash-attn auto --timeout 3600 > "$LOG" 2>&1 &
PID=$!
for i in $(seq 1 900); do sleep 1; kill -0 $PID 2>/dev/null || { echo "$TAG DIED during load" | tee "$OUT"; exit 1; }
  grep -q "listening on http" "$LOG" && break; done
GOT=$(grep -oE "n_ctx_slot = [0-9]+" "$LOG" | tail -1 | grep -oE "[0-9]+")
VLOAD=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -1)
echo "[load] tag=$TAG asked=$CTX got=$GOT vram=${VLOAD}MiB ncmoe=$NCMOE kv=$CTK" | tee "$OUT"

python3 "$DIR/hard_recall_probe.py" --server "$S" --target "$TARGET" --out-dir "$Q" \
  --kwargs '{"enable_thinking": false}' | tee -a "$OUT"

# warm short decode, so the deep figures have a same-session reference
curl -s -m 600 "$S/v1/chat/completions" -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","content":"Reply with the single word: ready"}],"max_tokens":16,"temperature":0.0,"stream":false,"chat_template_kwargs":{"enable_thinking":false}}' \
  > "$Q/warm.json"
python3 -c "
import json;d=json.load(open('$Q/warm.json'));t=d.get('timings',{})
print('[warm] decode=%.2f t/s'%t.get('predicted_per_second',0))" | tee -a "$OUT"

VPEAK=$VLOAD
for n in q1 q2 q3; do
  ( while :; do u=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits|head -1); echo $u; sleep 5; done ) > "$Q/$n.vram" &
  W=$!
  curl -s -m 20000 "$S/v1/chat/completions" -H 'Content-Type: application/json' \
    --data-binary @"$Q/$n.json" > "$Q/$n.out.json"
  kill $W 2>/dev/null
  P=$(sort -n "$Q/$n.vram" | tail -1); [ -n "$P" ] && [ "$P" -gt "$VPEAK" ] && VPEAK=$P
  python3 - "$Q" "$n" <<'PY' | tee -a "$OUT"
import json,sys,re
q,n=sys.argv[1],sys.argv[2]
d=json.load(open(f"{q}/{n}.out.json")); k=json.load(open(f"{q}/meta.json"))
t=d.get("timings",{}); c=(d["choices"][0]["message"].get("content") or "").strip()
pre="prompt_n=%d prefill=%.2f t/s (%.1f min) decode=%.2f t/s"%(
    t.get("prompt_n",0),t.get("prompt_per_second",0) or 0,(t.get("prompt_ms",0) or 0)/60000,t.get("predicted_per_second",0) or 0)
if n=="q1":
    hit=sum(1 for code in k["codes"] if code in c); print(f"[q1 RETRIEVE] {hit}/3  {pre}")
elif n=="q2":
    got=dict(re.findall(r"\b([A-H])\s*=\s*(\d{3,5})\b",c))
    hit=sum(1 for L,v in k["tallies"].items() if got.get(L)==str(v))
    print(f"[q2 MULTI-NEEDLE] {hit}/8  {pre}")
    if hit<8: print("        wanted",k["tallies"],"| got",got)
else:
    e=k["q3"]; L=e["letter"]==(re.search(r"\b([A-H])\s*=",c).group(1) if re.search(r"\b([A-H])\s*=",c) else "")
    T=str(e["tally"]) in c; K=(e["task"] or "~~").lower() in c.lower()
    print(f"[q3 INTEGRATE] letter={'Y' if L else 'N'} tally={'Y' if T else 'N'} task={'Y' if K else 'N'}  {pre}")
    if not(L and T and K): print("        wanted",e,"| got",repr(c[:220]))
PY
done
echo "[peak] vram=${VPEAK}MiB" | tee -a "$OUT"
kill $PID 2>/dev/null; sleep 5; pkill -x llama-server 2>/dev/null; sleep 3
echo "[done] $TAG" | tee -a "$OUT"
