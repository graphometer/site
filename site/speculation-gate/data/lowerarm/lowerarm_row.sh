#!/usr/bin/env bash
# Lower-arm row driver — Operation Qwen WP-C downward extension, 2026-08-11.
# Derived from 2026-08-10/ladder_row.sh (P6: invocations composed ONCE, never by hand).
# Two deliberate changes from the 08-10 driver:
#   1. flags are captured DIRECTLY into flags_<T>_c<N>.txt (no overwrite window at all);
#   2. the defective close-step acceptance grep is REMOVED — per-observation counters in
#      the records are the authoritative mechanism numbers (known defect, mission brief).
# Usage: lowerarm_row.sh <open|sweep|close> <rownum 1-6>
set -o pipefail
export HUB=<VAULT>/work/qwen
export SWEEP="$HUB/instrument/mtpsweep"
export SRV="$HUB/runs/qwen397"
export OUT="$HUB/runs/qwen397/2026-08-11_lowerarm"
export URL=http://127.0.0.1:8197/v1
# row -> launcher_T  mtpsweep_treatment  gate_p_min  cycle  (cycle 2 = exact reverse)
row_spec() { case "$1" in
  1) echo "none none - 1";;      2) echo "gate010 gated 0.10 1";;  3) echo "gate025 gated 0.25 1";;
  4) echo "gate025 gated 0.25 2";; 5) echo "gate010 gated 0.10 2";; 6) echo "none none - 2";;
  *) echo "BADROW"; return 1;; esac; }
read -r T TR GATE N <<<"$(row_spec "$2")" || exit 2
[ "$T" = BADROW ] && { echo "bad row $2"; exit 2; }

case "$1" in
open)
  echo "=== ROW $2: $T (treatment=$TR gate=$GATE cycle=$N) server start $(date '+%H:%M:%S') ==="
  bash "$OUT/serve_variant_lowerarm.sh" "$T" "$OUT" 2>&1 | tail -13; rc=${PIPESTATUS[0]}
  [ "$rc" -ne 0 ] && { echo "!! serve_variant exit=$rc — see plan 4.B"; exit 1; }
  tr '\0' ' ' < "/proc/$(cat "$OUT/server_$T.pid")/cmdline" > "$OUT/flags_${T}_c${N}.txt"
  echo -n "GATE argv: "; grep -o -- '--spec-draft-p-min [0-9.]*' "$OUT/flags_${T}_c${N}.txt" || echo "(none — correct only for rows 1/6)"
  echo -n "GATE alias: "; curl -s http://127.0.0.1:8197/v1/models | python3 -c 'import sys,json;print([m["id"] for m in json.load(sys.stdin)["data"]])'
  ;;
sweep)
  ARGS=(--base-url "$URL" --model-id qwen3.5-397b --out "$OUT" --treatment "$TR")
  [ "$GATE" != "-" ] && ARGS+=(--gate-p-min "$GATE")
  ARGS+=(--cycle "$N" --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0
         --server-flags-file "$OUT/flags_${T}_c${N}.txt" --server-build c8e03ce
         --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1"
         --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched")
  cd "$SWEEP" && ./mtpsweep run "${ARGS[@]}" 2>&1 | tee "$OUT/session_${T}_c${N}.log"
  echo "MTPSWEEP_EXIT=${PIPESTATUS[0]} at $(date '+%H:%M:%S')"
  ;;
close)
  echo "=== ROW $2 close: census ==="
  grep -l '"stream_options_fallback": true' "$OUT"/sessions/*.json 2>/dev/null && echo "!! FALLBACK — see plan 4.D" || echo "no fallback"
  grep -c 'HIDDEN-REASONING\|UNRECOGNISED-DELTA-FIELDS' "$OUT/session_${T}_c${N}.log" | xargs echo "abort markers in session log:"
  # P6 assertion: newest session's treatment.key + cycle vs this row's expectation
  python3 - "$TR" "$GATE" "$N" <<'PY'
import glob, json, os, sys
tr, gate, cyc = sys.argv[1], sys.argv[2], sys.argv[3]
exp = "none" if tr == "none" else ("ungated" if tr == "ungated" else f"gate_{float(gate):.2f}")
p = max(glob.glob(os.path.join(os.environ["OUT"], "sessions", "*.json")), key=os.path.getmtime)
s = json.load(open(p))
k = s.get("treatment", {}).get("key"); c = s.get("cycle"); su = s.get("summary", {})
print(f"latest session {os.path.basename(p)}: key={k} cycle={c} "
      f"meas={su.get('measurements')} ok={su.get('measurements_ok')} "
      f"usable={su.get('measurements_usable')} fail={su.get('failures')} "
      f"fallback={su.get('stream_options_fallback')}")
print("P6 KEY " + ("OK" if (k == exp and str(c) == cyc) else "MISMATCH — STOP THE LADDER"))
PY
  echo "=== stop ==="; bash "$SRV/stop_variant.sh" "$T" "$OUT" 2>&1 | tail -3
  # P7: cycle-tag IMMEDIATELY (flags file is already cycle-tagged at capture)
  for f in "server_$T.log" "load_$T.json"; do
    [ -e "$OUT/$f" ] && mv "$OUT/$f" "$OUT/${f%.*}_c${N}.${f##*.}"; done
  echo "archived: $(ls -1 "$OUT"/*_c${N}.* 2>/dev/null | grep -c "$T")"
  echo -n "VRAM: "; nvidia-smi --query-gpu=memory.used --format=csv,noheader
  free -g | awk '/^Mem:/{print "RAM available:",$7,"GB"}'
  ss -tln | awk '{print $4}' | grep -q '127.0.0.1:8197' && echo "!! 8197 STILL LISTENING" || echo "port 8197 clear"
  pgrep -f 'llama-server --model' || echo "no llama-server running"
  ;;
esac
