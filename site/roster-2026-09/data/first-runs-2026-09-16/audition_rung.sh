#!/usr/bin/env bash
# audition_rung.sh — first-contact probe for a model that has never run here.
# Same skeleton as context256_rung.sh (pre-flight, direct launch, served-window check, deep
# three-code recall, clean teardown) plus the two things an audition needs and a window sweep does not:
#   * a TOOL round-trip — OpenAI tools in, a well-formed tool_call out (the thing that breaks first
#     on a new architecture or a fork branch)
#   * a THINKING-SWITCH check — the same question asked with the model's thinking knob off and on,
#     comparing reasoning output and first-word latency
#
#   audition_rung.sh <label> <host> <port> <kwargs-off|-> <kwargs-on|-> <load_timeout_s> <ldpath> <min_ram_gb> <target_tokens> -- <cmd...>
set -uo pipefail
D=<REDACTED_PATH>
TSV="$D/AUDITION_MEASUREMENTS.tsv"
L="$D/logs_audition"; mkdir -p "$L"

LABEL="$1"; HOST="$2"; PORT="$3"; KWOFF="$4"; KWON="$5"; TMO="$6"; LDP="$7"; MINRAM="$8"; TARGET="$9"; shift 9
[ "${1:-}" = "--" ] && shift
LOG="$L/${LABEL}.log"; : > "$LOG"
[ -f "$TSV" ] || printf 'label\tstatus\tload_s\tn_ctx\tvram_loaded_mib\tvram_peak_mib\tdecode_tps\tfirst_word_s\ttools\tthink_off_chars\tthink_on_chars\tdeep_prompt_tok\tdeep_prefill_tps\tcodes_hit\tnote\n' > "$TSV"
[ "$KWOFF" = "-" ] && KWOFF=""; [ "$KWON" = "-" ] && KWON=""

want_ctx=""; prev=""; for a in "$@"; do [ "$prev" = "--ctx-size" ] && want_ctx="$a"; prev="$a"; done
gpu() { nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -1; }
live_servers() { local n=0 p; for p in /proc/[0-9]*; do case "$(readlink -f "$p/exe" 2>/dev/null)" in *llama-server) n=$((n+1));; esac; done; echo "$n"; }
row() { printf '%s' "$LABEL" >> "$TSV"; for f in "$@"; do printf '\t%s' "$f" >> "$TSV"; done; printf '\n' >> "$TSV"; }

pre_gpu="$(gpu)"; avail="$(free -g | awk '/^Mem:/{print $7}')"
echo "[preflight] gpu=${pre_gpu}MiB ram=${avail}GB want_ctx=${want_ctx}" | tee -a "$LOG"
[ "$pre_gpu" -ge 2048 ] && { row PREFLIGHT_ABORT - - - - - - - - - - - - "gpu holds ${pre_gpu} MiB"; exit 3; }
[ "$(live_servers)" -gt 0 ] && { row PREFLIGHT_ABORT - - - - - - - - - - - - "a llama-server is already running"; exit 3; }
ss -tln | awk '{print $4}' | grep -qxF "${HOST}:${PORT}" && { row PREFLIGHT_ABORT - - - - - - - - - - - - "port busy"; exit 3; }
[ "$avail" -lt "$MINRAM" ] && { row PREFLIGHT_ABORT - - - - - - - - - - - - "ram ${avail} GB under the ${MINRAM} GB floor"; exit 3; }
echo "[cmd] $*" >> "$LOG"

t0=$(date +%s.%N)
LD_LIBRARY_PATH="$LDP" setsid nohup "$@" >>"$LOG" 2>&1 &
SPID=$!; sleep 1; PGID="$(ps -o pgid= -p "$SPID" 2>/dev/null | tr -d ' ')"
echo "[launch] pid=$SPID pgid=${PGID:-?}" | tee -a "$LOG"

cleanup() {
  [ -n "${PGID:-}" ] && kill -TERM -- "-$PGID" 2>/dev/null
  kill -TERM "$SPID" 2>/dev/null
  for i in $(seq 1 60); do kill -0 "$SPID" 2>/dev/null || break; sleep 0.5; done
  kill -0 "$SPID" 2>/dev/null && { [ -n "${PGID:-}" ] && kill -KILL -- "-$PGID" 2>/dev/null; kill -KILL "$SPID" 2>/dev/null; sleep 2; }
  for sig in TERM KILL; do
    hits=0
    for p in /proc/[0-9]*; do
      case "$(readlink -f "$p/exe" 2>/dev/null)" in *llama-server) kill -"$sig" "${p#/proc/}" 2>/dev/null; hits=1;; esac
    done
    [ "$hits" = 0 ] && break; sleep 3
  done
  for i in $(seq 1 60); do [ "$(gpu)" -lt 2048 ] && break; sleep 1; done
  echo "[cleanup] gpu_after=$(gpu) MiB live_servers=$(live_servers)" | tee -a "$LOG"
}

health=FAIL; load=""
for i in $(seq 1 "$TMO"); do
  kill -0 "$SPID" 2>/dev/null || { echo "[health] exited before healthy (t=${i}s)" | tee -a "$LOG"; break; }
  case "$(curl -s -m 3 "http://${HOST}:${PORT}/health" 2>/dev/null)" in *'"ok"'*) health=ok; load="$(echo "$(date +%s.%N) - $t0" | bc)"; break ;; esac
  sleep 1
done
if [ "$health" != "ok" ]; then
  v="$(gpu)"; err="$(grep -iE 'error|failed|out of memory|cudaMalloc|unknown model|unsupported|terminate|what\(\)' "$LOG" | tail -3 | tr '\n\t' '  ' | cut -c1-300)"
  cleanup; row FAIL - - "$v" - - - - - - - - - "${err:-no health in ${TMO}s}"; exit 1
fi
n_ctx="$(curl -s -m 10 "http://${HOST}:${PORT}/props" | python3 -c "import sys,json;d=json.load(sys.stdin);print((d.get('default_generation_settings') or {}).get('n_ctx') or d.get('n_ctx') or 'NA')" 2>/dev/null)"
vram="$(gpu)"; note=""
[ -n "$want_ctx" ] && [ "$n_ctx" != "$want_ctx" ] && note="SERVED ${n_ctx} != asked ${want_ctx}; "
echo "[result] healthy in ${load}s n_ctx=${n_ctx} vram=${vram} MiB" | tee -a "$LOG"

ask() { # $1 text, $2 max_tokens, $3 kwargs-json, $4 out-file  → prints "<first_word_s> <decode_tps> <content_chars> <reasoning_chars>"
  python3 - "$1" "$2" "$3" "$4" "http://${HOST}:${PORT}/v1/chat/completions" <<'PY'
import json,sys,time,urllib.request
text,maxt,kw,out,url = sys.argv[1],int(sys.argv[2]),sys.argv[3],sys.argv[4],sys.argv[5]
req={"messages":[{"role":"user","content":text}],"max_tokens":maxt,"temperature":0.0,"stream":False}
if kw: req["chat_template_kwargs"]=json.loads(kw)
t0=time.time()
try:
    r=urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(req).encode(),headers={"Content-Type":"application/json"}),timeout=3600)
    d=json.load(r)
except Exception as e:
    open(out,'w').write(json.dumps({"error":str(e)})); print("NA NA 0 0"); sys.exit()
open(out,'w').write(json.dumps(d))
el=time.time()-t0
m=(d.get("choices") or [{}])[0].get("message") or {}
t=d.get("timings") or {}
print(f"{el:.1f} {t.get('predicted_per_second',0):.2f} {len(m.get('content') or '')} {len(m.get('reasoning_content') or '')}")
PY
}

read -r _ _ _ _ <<<"$(ask 'Say the single word: ready.' 24 "$KWOFF" "$L/${LABEL}.warm.json")"
read -r FW DEC CCHARS RCHARS <<<"$(ask 'In exactly one paragraph of about 150 words, describe how a mechanical water pump moves water uphill. Plain prose, no lists.' 400 "$KWOFF" "$L/${LABEL}.short.json")"
echo "[short] first_word=${FW}s decode=${DEC} t/s content=${CCHARS} reasoning=${RCHARS}" | tee -a "$LOG"
THINK_ON_R=0
if [ -n "$KWON" ]; then
  read -r _ _ _ THINK_ON_R <<<"$(ask 'A bat and a ball cost 1.10 in total. The bat costs 1.00 more than the ball. How much does the ball cost?' 1200 "$KWON" "$L/${LABEL}.thinkon.json")"
  echo "[think-on] reasoning chars=${THINK_ON_R}" | tee -a "$LOG"
fi

TOOLS="$(python3 - "http://${HOST}:${PORT}/v1/chat/completions" "$KWOFF" "$L/${LABEL}.tool.json" <<'PY'
import json,sys,urllib.request
url,kw,out=sys.argv[1],sys.argv[2],sys.argv[3]
req={"messages":[{"role":"user","content":"What is the weather in Lisbon? Call the tool; do not answer from memory."}],
     "tools":[{"type":"function","function":{"name":"get_weather","description":"Current weather for a city",
      "parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}],
     "tool_choice":"auto","max_tokens":700,"temperature":0.0,"stream":False}
if kw: req["chat_template_kwargs"]=json.loads(kw)
try:
    d=json.load(urllib.request.urlopen(urllib.request.Request(url,data=json.dumps(req).encode(),headers={"Content-Type":"application/json"}),timeout=1800))
except Exception as e:
    open(out,'w').write(json.dumps({"error":str(e)})); print("FAIL:no-response"); sys.exit()
open(out,'w').write(json.dumps(d))
ch=(d.get("choices") or [{}])[0]; m=ch.get("message") or {}; tc=m.get("tool_calls") or []
if not tc: print("FAIL:no-tool-call"); sys.exit()
try:
    args=json.loads(tc[0]["function"]["arguments"])
    print("OK" if str(args.get("city","")).lower().startswith("lisbo") else f"WEAK:{str(args)[:30]}")
except Exception:
    print("FAIL:unparsable-arguments")
PY
)"
echo "[tools] $TOOLS" | tee -a "$LOG"

meta="$(python3 "$D/deep_recall_probe.py" --server "http://${HOST}:${PORT}" --target "$TARGET" --out "$L/${LABEL}.deep.req" --kwargs "${KWOFF:--}" 2>>"$LOG")"
echo "[deep] $meta" | tee -a "$LOG"
curl -s -m 14400 -H 'Content-Type: application/json' --data @"$L/${LABEL}.deep.req" "http://${HOST}:${PORT}/v1/chat/completions" > "$L/${LABEL}.deep.json" 2>>"$LOG" &
CPID=$!; peak="$vram"
while kill -0 "$CPID" 2>/dev/null; do g="$(gpu)"; [ "$g" -gt "$peak" ] && peak="$g"; sleep 5; done
read -r PN PPS HITS <<EOF
$(python3 - "$L/${LABEL}.deep.json" <<'PY'
import json,sys
codes=["AMBER-3172-WILLOW","COBALT-5821-FERN","ONYX-9044-HAZEL"]
try: d=json.load(open(sys.argv[1]))
except Exception: print("NA NA 0/3:no-response"); sys.exit()
if "error" in d: print("NA NA 0/3:error"); sys.exit()
t=d.get("timings") or {}; m=(d.get("choices") or [{}])[0].get("message") or {}
txt=m.get("content") or ""
hit=sum(c in txt for c in codes)
print(t.get("prompt_n","NA"), ("%.2f"%t["prompt_per_second"]) if t.get("prompt_per_second") else "NA",
      f"{hit}/3" + ("" if txt.strip() else ":empty-content"))
PY
)
EOF
echo "[deep] prompt=${PN} prefill=${PPS} codes=${HITS} vram_peak=${peak}" | tee -a "$LOG"

cleanup
row OK "$load" "$n_ctx" "$vram" "$peak" "$DEC" "$FW" "$TOOLS" "$RCHARS" "$THINK_ON_R" "$PN" "$PPS" "$HITS" "${note%; }"
echo "=== $LABEL DONE: n_ctx=${n_ctx} vram=${vram}/${peak} decode=${DEC} first_word=${FW}s tools=${TOOLS} codes=${HITS} ==="
