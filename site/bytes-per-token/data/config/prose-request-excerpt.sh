reqjson() {  # $1 = user text, $2 = max_tokens
  python3 - "$1" "$2" "$KW" <<'PY'
import json,sys
r={"messages":[{"role":"user","content":sys.argv[1]}],"max_tokens":int(sys.argv[2]),"temperature":0.0,"stream":False}
if sys.argv[3]: r["chat_template_kwargs"]=json.loads(sys.argv[3])
print(json.dumps(r))
PY
}

# ---------- WARM-UP + SHORT DECODE (two water-pump replies, best kept; neither Inkling-Small reply cached prompt tokens) ----------
reqjson "Say the single word: ready." 24 > "$L/${LABEL}.warm.req"
curl -s -m 1800 -H 'Content-Type: application/json' --data @"$L/${LABEL}.warm.req" "http://${HOST}:${PORT}/v1/chat/completions" > "$L/${LABEL}.warm.json" 2>>"$LOG"
reqjson "In exactly one paragraph of about 150 words, describe how a mechanical water pump moves water uphill. Plain prose, no lists." 320 > "$L/${LABEL}.short.req"
best=0
for rep in 1 2; do
  curl -s -m 1800 -H 'Content-Type: application/json' --data @"$L/${LABEL}.short.req" "http://${HOST}:${PORT}/v1/chat/completions" > "$L/${LABEL}.short.r${rep}.json" 2>>"$LOG"
  d="$(python3 -c "import json,sys;print((json.load(open(sys.argv[1])).get('timings') or {}).get('predicted_per_second') or 0)" "$L/${LABEL}.short.r${rep}.json" 2>/dev/null || echo 0)"
  echo "[short rep$rep] decode=$d t/s" | tee -a "$LOG"
  best="$(python3 -c "print(max(float('$best'), float('$d')))")"
done

