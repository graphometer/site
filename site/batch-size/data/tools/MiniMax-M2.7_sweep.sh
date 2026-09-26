#!/usr/bin/env bash
# ===========================================================================
# MiniMax-M2.7_sweep.sh: one-variable-at-a-time prefill sweep for MiniMax M2.7
# ===========================================================================
# WHY: [two sentences removed from this copy]
# DeepSeek V4 Flash: same box, same --threads 24, same all-experts-on-CPU
# placement, but llama.cpp's DEFAULT -ub 512: reads at 75 t/s.
#
# PHASE A is the -ub sweep. `-ub 128` is included FIRST and deliberately: it is
# the control. If it does not land near 27 t/s, the diagnosis is wrong or the
# build changed the baseline, and the rest of the grid means nothing.
#
# PHASE B is the placement sweep, run only after A picks a winner.
#
# SAFETY: this script refuses to start if anything else owns the card:
#   1. [a check on other model services, removed from this copy]
#   2. any llama-server process is alive (matched on /proc cmdline PREFIX,
#      never `pgrep -f`, which matches this script's own command line)
#   3. an Ollama model is resident
#   4. the port is already listening
#   5. available RAM is under the floor
# It never uses sudo, never installs anything, never touches a canonical path.
# Results are written per-config to results/: nothing is appended to a file
# while another process reads it, and this script is never rewritten while running.
#
# Usage:
#   bash MiniMax-M2.7_sweep.sh A            # the -ub sweep (the one that matters)
#   bash MiniMax-M2.7_sweep.sh B <ub>       # the placement sweep at the winning -ub
#   bash MiniMax-M2.7_sweep.sh one <ub> <ncmoe> [ctx] [sizes]   # a single config
# ===========================================================================
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESULTS="$HERE/results"
mkdir -p "$RESULTS"

# ---- fixed for the whole sweep ----------------------------------------------
STAGE=<MODEL_DIR>/MiniMax-M2.7/UD-IQ4_XS
MODEL="$STAGE/MiniMax-M2.7-UD-IQ4_XS-00001-of-00004.gguf"
# build 10919 / d3146f2b5: newest build carrying `minimax-m2`, and the SAME
# commit the laptop's RPC worker was built from, so a two-machine split later
# needs no rebuild. (The earlier test used the 5f55650 build.)
BIN=<llama.cpp build d3146f2b5, RPC enabled>/llama-server
HOST=127.0.0.1
PORT="${MINIMAX_M27_PORT:-8131}"
THREADS=24
RAM_FLOOR_GB="${MINIMAX_M27_RAM_FLOOR_GB:-125}"
LOAD_TIMEOUT="${MINIMAX_M27_LOAD_TIMEOUT:-1800}"   # 101 GB of weights; VOID past this
PROBE_TIMEOUT="${MINIMAX_M27_PROBE_TIMEOUT:-2400}"
SIZES_DEFAULT="${MINIMAX_M27_SIZES:-4096}"

PY=/usr/bin/python3
[ -x "$PY" ] || PY=$(command -v python3)

# ---- guards -----------------------------------------------------------------

preflight() {
  [ -x "$BIN" ] || { echo "REFUSED: runtime missing: $BIN" >&2; exit 3; }
  for n in 1 2 3 4; do
    s="$STAGE/MiniMax-M2.7-UD-IQ4_XS-0000${n}-of-00004.gguf"
    [ -f "$s" ] || { echo "REFUSED: shard $n of 4 missing: $s" >&2; exit 3; }
  done

  # [a check that no other model service was active was removed from this copy]

  # any llama-server at all, by /proc cmdline prefix. Self-safe: this script's
  # own argv contains the binary path as an ARGUMENT, never as argv[0].
  for d in /proc/[0-9]*; do
    pid="${d#/proc/}"; [ "$pid" = "$$" ] && continue
    [ -r "$d/cmdline" ] || continue
    cmd="$(tr '\0' ' ' < "$d/cmdline" 2>/dev/null || true)"
    case "$cmd" in
      */llama-server\ *|*/llama-server)
        echo "REFUSED: pid $pid is already running a llama-server:" >&2
        echo "  ${cmd:0:160}" >&2
        echo "Stop it first (kill by PID). An idle GPU does not release the hold." >&2
        exit 1 ;;
    esac
  done

  if command -v ollama >/dev/null 2>&1; then
    if ollama ps 2>/dev/null | tail -n +2 | grep -q .; then
      echo "REFUSED: an Ollama model is resident (ollama ps is not empty). Free the card first." >&2
      exit 1
    fi
  fi

  if ss -tln | awk '{print $4}' | grep -qxF "${HOST}:${PORT}"; then
    echo "REFUSED: ${HOST}:${PORT} is already listening." >&2
    exit 1
  fi

  avail=$(awk '/MemAvailable/ {printf "%d", $2/1048576}' /proc/meminfo)
  if [ "$avail" -lt "$RAM_FLOOR_GB" ]; then
    echo "REFUSED: only ${avail} GB RAM available (floor ${RAM_FLOOR_GB} GB). 101 GB of weights page in" >&2
    echo "through the cache under -cmoe; below the floor the model thrashes instead of serving." >&2
    echo "Override deliberately with MINIMAX_M27_RAM_FLOOR_GB=<n> if you know why." >&2
    exit 1
  fi
  echo "preflight OK: card free, ${avail} GB RAM available, port ${PORT} free"
}

# ---- one configuration -------------------------------------------------------
# run_one <ub> <ncmoe|cmoe> <ctx> <kv> <sizes> <tag>
run_one() {
  local ub="$1" place="$2" ctx="$3" kv="$4" sizes="$5" tag="$6"
  local log="$RESULTS/${tag}.server.log"
  local out="$RESULTS/${tag}.json"
  local pidf="$RESULTS/${tag}.pid"

  local PLACE=()
  if [ "$place" = "cmoe" ]; then PLACE=(-cmoe); else PLACE=(--n-cpu-moe "$place"); fi

  echo
  echo "=== $tag :: -ub $ub · place $place · ctx $ctx · KV $kv ==="

  LD_LIBRARY_PATH=<CUDA 12.8 libraries> \
  "$BIN" \
    --model "$MODEL" \
    --host "$HOST" --port "$PORT" --alias minimax-m2.7 \
    --jinja --ctx-size "$ctx" --parallel 1 \
    --threads "$THREADS" --threads-batch "$THREADS" \
    --n-gpu-layers 999 "${PLACE[@]}" \
    -b 4096 -ub "$ub" \
    --no-repack --flash-attn on \
    --cache-type-k "$kv" --cache-type-v "$kv" \
    --timeout 3600 \
    > "$log" 2>&1 &
  echo $! > "$pidf"
  local pid; pid=$(cat "$pidf")

  # --- wait for health by PID + HTTP, never by name ---
  local t0; t0=$(date +%s); local up=0
  while :; do
    if ! kill -0 "$pid" 2>/dev/null; then
      echo "  VOID: server exited during load. Tail:" ; tail -5 "$log" | sed 's/^/    /'
      rm -f "$pidf"; return 1
    fi
    if curl -fsS -m 5 "http://${HOST}:${PORT}/health" >/dev/null 2>&1; then up=1; break; fi
    local now; now=$(date +%s)
    if [ $((now - t0)) -gt "$LOAD_TIMEOUT" ]; then
      echo "  VOID: no health inside ${LOAD_TIMEOUT}s (harness stall, not a model verdict)"
      kill -INT "$pid" 2>/dev/null || true; sleep 5; kill -9 "$pid" 2>/dev/null || true
      rm -f "$pidf"; return 1
    fi
    sleep 5
  done
  local load_s=$(( $(date +%s) - t0 ))
  local vram; vram=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -1)
  echo "  healthy in ${load_s}s · VRAM ${vram} MiB"

  "$PY" "$HERE/MiniMax-M2.7_probe.py" --url "http://${HOST}:${PORT}" \
      --sizes "$sizes" --timeout "$PROBE_TIMEOUT" \
      --label "$tag" --out "$out" || echo "  probe returned non-zero"

  # annotate with the config, load time and VRAM
  "$PY" - "$out" "$ub" "$place" "$ctx" "$kv" "$load_s" "$vram" <<'PYEOF'
import json,sys
p,ub,place,ctx,kv,load_s,vram = sys.argv[1:8]
try: d=json.load(open(p))
except Exception: d={}
d["config"]={"ub":int(ub),"place":place,"ctx":int(ctx),"kv":kv,
             "load_s":int(load_s),"vram_mib":int(vram),
             "build":"10919/d3146f2b5","quant":"unsloth UD-IQ4_XS"}
json.dump(d,open(p,"w"),indent=1)
PYEOF

  # --- stop by PID, wait for exit ---
  kill -INT "$pid" 2>/dev/null || true
  local t1; t1=$(date +%s)
  while kill -0 "$pid" 2>/dev/null; do
    if [ $(( $(date +%s) - t1 )) -gt 120 ]; then kill -9 "$pid" 2>/dev/null || true; break; fi
    sleep 2
  done
  rm -f "$pidf"
  echo "  stopped."
}

summarise() {
  "$PY" - "$RESULTS" <<'PYEOF'
import json,os,sys,glob
r=sys.argv[1]; rows=[]
for p in sorted(glob.glob(os.path.join(r,"*.json"))):
    try: d=json.load(open(p))
    except Exception: continue
    c=d.get("config",{})
    for size,legs in (d.get("sizes") or {}).items():
        cold=legs.get("cold",{}); warm=legs.get("warm",{})
        rows.append((d.get("label",""),c.get("ub"),c.get("place"),size,
                     cold.get("prefill_tps"),cold.get("decode_tps"),
                     warm.get("wall_s"),c.get("load_s"),c.get("vram_mib")))
if not rows: print("(no results yet)"); sys.exit()
print(f"\n{'config':<22}{'ub':>6}{'place':>8}{'tokens':>8}{'prefill t/s':>13}{'decode t/s':>12}{'warm s':>9}{'load s':>8}{'VRAM':>8}")
print("-"*96)
for x in rows:
    f=lambda v,n=1: ("%.*f"%(n,v)) if isinstance(v,(int,float)) else "-"
    print(f"{str(x[0]):<22}{str(x[1]):>6}{str(x[2]):>8}{str(x[3]):>8}{f(x[4]):>13}{f(x[5]):>12}{f(x[6],2):>9}{str(x[7]):>8}{str(x[8]):>8}")
print("\nBaseline to beat: the 2026-09-13 gate read 26.7 t/s at 3,685 tokens (-cmoe -ub 128).")
PYEOF
}

# ---- phases -----------------------------------------------------------------
mode="${1:-A}"
case "$mode" in
  A)
    preflight
    echo "PHASE A: the -ub sweep. 128 runs FIRST as the control."
    for ub in 128 512 1024 2048; do
      run_one "$ub" cmoe 131072 q8_0 "$SIZES_DEFAULT" "A_ub${ub}_cmoe" || true
    done
    summarise
    ;;
  B)
    ub="${2:?usage: MiniMax-M2.7_sweep.sh B <winning-ub>}"
    preflight
    echo "PHASE B: placement at -ub ${ub}. M2.7 has 62 blocks; -cmoe == all 62 on CPU."
    for nc in 62 56 52 48; do
      run_one "$ub" "$nc" 131072 q8_0 "$SIZES_DEFAULT" "B_ub${ub}_ncmoe${nc}" || true
    done
    summarise
    ;;
  one)
    ub="${2:?usage: MiniMax-M2.7_sweep.sh one <ub> <ncmoe|cmoe> [ctx] [sizes]}"
    place="${3:?}"; ctx="${4:-131072}"; sizes="${5:-$SIZES_DEFAULT}"
    preflight
    run_one "$ub" "$place" "$ctx" q8_0 "$sizes" "one_ub${ub}_${place}_ctx${ctx}" || true
    summarise
    ;;
  summary) summarise ;;
  *) echo "usage: MiniMax-M2.7_sweep.sh {A|B <ub>|one <ub> <place> [ctx] [sizes]|summary}" >&2; exit 2 ;;
esac
