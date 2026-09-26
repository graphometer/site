#!/usr/bin/env bash
# context256_rung.sh : prove ONE body at a long window by invoking llama-server DIRECTLY with its
# canonical start_server.sh flags (only --ctx-size and the knobs named per body vary). Adapted from
# the 2026-09-12 context sweep's rung.sh. Adds three things that sweep did not need:
#   * a served-window check: /props n_ctx must equal the --ctx-size asked for (catches silent shrinking)
#   * a RAM floor per body, because direct invocation skips each start script's own floor
#   * a DEEP recall probe: three sealed codes at ~5/50/95 % of a prompt fitted to <target_tokens>
#     with the server's own tokenizer (deep_recall_probe.py), plus the VRAM peak while it is read
#
#   context256_rung.sh <label> <host> <port> <kwargs-json|-> <load_timeout_s> <ldpath> <min_ram_gb> <target_tokens> -- <cmd...>
set -uo pipefail
D=<REDACTED_PATH>
TSV="$D/CONTEXT_256K_MEASUREMENTS.tsv"
L="$D/logs256"; mkdir -p "$L"

LABEL="$1"; HOST="$2"; PORT="$3"; KW="$4"; TMO="$5"; LDP="$6"; MINRAM="$7"; TARGET="$8"; shift 8
[ "${1:-}" = "--" ] && shift
LOG="$L/${LABEL}.log"; : > "$LOG"
[ -f "$TSV" ] || printf 'label\tstatus\tload_s\tn_ctx\tvram_loaded_mib\tvram_peak_mib\tdecode_tps\tdeep_prompt_tok\tdeep_prefill_tps\tdeep_decode_tps\tcodes_hit\tnote\n' > "$TSV"
[ "$KW" = "-" ] && KW=""

want_ctx=""; prev=""; for a in "$@"; do [ "$prev" = "--ctx-size" ] && want_ctx="$a"; prev="$a"; done
gpu() { nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -1; }
live_servers() { local n=0 p; for p in /proc/[0-9]*; do case "$(readlink -f "$p/exe" 2>/dev/null)" in *llama-server) n=$((n+1));; esac; done; echo "$n"; }
row() { printf '%s' "$LABEL" >> "$TSV"; for f in "$@"; do printf '\t%s' "$f" >> "$TSV"; done; printf '\n' >> "$TSV"; }

# ---------- PRE-FLIGHT ----------
pre_gpu="$(gpu)"; avail="$(free -g | awk '/^Mem:/{print $7}')"
echo "[preflight] gpu_used=${pre_gpu}MiB ram_avail=${avail}GB want_ctx=${want_ctx} target=${TARGET}" | tee -a "$LOG"
[ "$pre_gpu" -ge 2048 ] && { row PREFLIGHT_ABORT - - - - - - - - - "gpu holds ${pre_gpu} MiB"; exit 3; }
[ "$(live_servers)" -gt 0 ] && { row PREFLIGHT_ABORT - - - - - - - - - "a llama-server is already running"; exit 3; }
ss -tln | awk '{print $4}' | grep -qxF "${HOST}:${PORT}" && { row PREFLIGHT_ABORT - - - - - - - - - "port busy"; exit 3; }
[ "$avail" -lt "$MINRAM" ] && { row PREFLIGHT_ABORT - - - - - - - - - "ram ${avail} GB under the ${MINRAM} GB floor"; exit 3; }
echo "[cmd] $*" >> "$LOG"

# ---------- LAUNCH (own process group so the whole tree dies together) ----------
t0=$(date +%s.%N)
LD_LIBRARY_PATH="$LDP" setsid nohup "$@" >>"$LOG" 2>&1 &
SPID=$!
sleep 1
PGID="$(ps -o pgid= -p "$SPID" 2>/dev/null | tr -d ' ')"
echo "[launch] pid=$SPID pgid=${PGID:-?}" | tee -a "$LOG"

cleanup() {
  echo "[cleanup] killing tree pgid=${PGID:-?} pid=$SPID" | tee -a "$LOG"
  [ -n "${PGID:-}" ] && kill -TERM -- "-$PGID" 2>/dev/null
  kill -TERM "$SPID" 2>/dev/null
  for i in $(seq 1 60); do kill -0 "$SPID" 2>/dev/null || break; sleep 0.5; done
  if kill -0 "$SPID" 2>/dev/null; then
    echo "[cleanup] SIGTERM did not land : SIGKILL" | tee -a "$LOG"
    [ -n "${PGID:-}" ] && kill -KILL -- "-$PGID" 2>/dev/null
    kill -KILL "$SPID" 2>/dev/null
    sleep 2
  fi
  # never pkill -f on a cmdline pattern (it matches this script); resolve real exes instead
  for sig in TERM KILL; do
    hits=0
    for p in /proc/[0-9]*; do
      case "$(readlink -f "$p/exe" 2>/dev/null)" in
        *llama-server) pid="${p#/proc/}"; echo "[cleanup] stray llama-server pid=$pid -> SIG$sig" | tee -a "$LOG"; kill -"$sig" "$pid" 2>/dev/null; hits=1 ;;
      esac
    done
    [ "$hits" = 0 ] && break
    sleep 3
  done
  for i in $(seq 1 30); do ss -tln | awk '{print $4}' | grep -qxF "${HOST}:${PORT}" || break; sleep 1; done
  for i in $(seq 1 60); do g="$(gpu)"; [ "$g" -lt 2048 ] && break; sleep 1; done
  echo "[cleanup] gpu_after=$(gpu) MiB live_servers=$(live_servers)" | tee -a "$LOG"
}

# ---------- WAIT FOR HEALTH ----------
health=FAIL; load=""
for i in $(seq 1 "$TMO"); do
  if ! kill -0 "$SPID" 2>/dev/null; then echo "[health] process exited before healthy (t=${i}s)" | tee -a "$LOG"; break; fi
  case "$(curl -s -m 3 "http://${HOST}:${PORT}/health" 2>/dev/null)" in *'"ok"'*) health=ok; load="$(echo "$(date +%s.%N) - $t0" | bc)"; break ;; esac
  sleep 1
done
if [ "$health" != "ok" ]; then
  vfail="$(gpu)"
  err="$(grep -iE 'error|failed|out of memory|cudaMalloc|unable to allocate|terminate|what\(\)' "$LOG" | tail -3 | tr '\n\t' '  ' | cut -c1-300)"
  cleanup
  row FAIL - - "$vfail" - - - - - - "${err:-no health in ${TMO}s}"
  exit 1
fi

n_ctx="$(curl -s -m 10 "http://${HOST}:${PORT}/props" | python3 -c "import sys,json;d=json.load(sys.stdin);print((d.get('default_generation_settings') or {}).get('n_ctx') or d.get('n_ctx') or 'NA')" 2>/dev/null)"
vram="$(gpu)"
note=""
[ -n "$want_ctx" ] && [ "$n_ctx" != "$want_ctx" ] && note="SERVED WINDOW ${n_ctx} != asked ${want_ctx}; "
echo "[result] healthy in ${load}s  n_ctx=${n_ctx}  vram=${vram} MiB" | tee -a "$LOG"

reqjson() {  # $1 = user text, $2 = max_tokens
  python3 - "$1" "$2" "$KW" <<'PY'
import json,sys
r={"messages":[{"role":"user","content":sys.argv[1]}],"max_tokens":int(sys.argv[2]),"temperature":0.0,"stream":False}
if sys.argv[3]: r["chat_template_kwargs"]=json.loads(sys.argv[3])
print(json.dumps(r))
PY
}

# ---------- WARM-UP + SHORT DECODE (2 warm reps, best kept) ----------
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

# ---------- DEEP RECALL ----------
meta="$(python3 "$D/deep_recall_probe.py" --server "http://${HOST}:${PORT}" --target "$TARGET" --out "$L/${LABEL}.deep.req" --kwargs "${KW:--}" 2>>"$LOG")"
echo "[deep] $meta" | tee -a "$LOG"
curl -s -m 14400 -H 'Content-Type: application/json' --data @"$L/${LABEL}.deep.req" "http://${HOST}:${PORT}/v1/chat/completions" > "$L/${LABEL}.deep.json" 2>>"$LOG" &
CPID=$!
peak="$vram"
while kill -0 "$CPID" 2>/dev/null; do g="$(gpu)"; [ "$g" -gt "$peak" ] && peak="$g"; sleep 5; done

read -r PN PPS DDEC HITS <<EOF
$(python3 - "$L/${LABEL}.deep.json" <<'PY'
import json,sys
codes=["AMBER-3172-WILLOW","COBALT-5821-FERN","ONYX-9044-HAZEL"]
try: d=json.load(open(sys.argv[1]))
except Exception: print("NA NA NA 0/3:no-response"); sys.exit()
if "error" in d: print("NA NA NA 0/3:error"); sys.exit()
t=d.get("timings") or {}; m=(d.get("choices") or [{}])[0].get("message") or {}
txt=m.get("content") or ""; rc=m.get("reasoning_content") or ""
hit=sum(c in txt for c in codes)
tag=f"{hit}/3" + ("" if txt.strip() else ":empty-content") + (":reasoned" if rc else "")
f=lambda v: ("%.2f"%v) if isinstance(v,(int,float)) else "NA"
print(t.get("prompt_n","NA"), f(t.get("prompt_per_second")), f(t.get("predicted_per_second")), tag)
PY
)
EOF
echo "[deep] prompt_n=${PN} prefill=${PPS} t/s decode=${DDEC} t/s codes=${HITS} vram_peak=${peak} MiB" | tee -a "$LOG"

cleanup
row OK "$load" "$n_ctx" "$vram" "$peak" "$best" "$PN" "$PPS" "$DDEC" "$HITS" "${note%; }"
echo "=== $LABEL DONE: n_ctx=${n_ctx} vram=${vram}/${peak} MiB decode=${best} deep=${PN} tok @ ${PPS} t/s codes=${HITS} ==="
