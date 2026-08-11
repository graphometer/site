#!/usr/bin/env bash
# Gate-ladder row driver — Operation Qwen WP-C, 2026-08-10.
# Invocations derived ONCE from plan §2.0's mapping table (PM pre-authorization P6),
# so no row is ever hand-composed. Usage: ladder_row.sh <open|sweep|close> <rownum>
set -o pipefail
export HUB=<VAULT>/work/qwen
export SWEEP="$HUB/instrument/mtpsweep"
export SRV="$HUB/runs/qwen397"
export OUT="$HUB/runs/qwen397/2026-08-10"
export URL=http://127.0.0.1:8197/v1
# row -> launcher_T  mtpsweep_treatment  gate_p_min  cycle   (from §2.0; cycle2 = exact reverse)
row_spec() { case "$1" in
  1) echo "none none - 1";;      2) echo "ungated ungated - 1";;  3) echo "gate050 gated 0.50 1";;
  4) echo "gate075 gated 0.75 1";; 5) echo "gate090 gated 0.90 1";; 6) echo "gate090 gated 0.90 2";;
  7) echo "gate075 gated 0.75 2";; 8) echo "gate050 gated 0.50 2";; 9) echo "ungated ungated - 2";;
 10) echo "none none - 2";; *) echo "BADROW"; return 1;; esac; }
read -r T TR GATE N <<<"$(row_spec "$2")" || exit 2
[ "$T" = BADROW ] && { echo "bad row $2"; exit 2; }

case "$1" in
open)
  echo "=== ROW $2: $T (treatment=$TR gate=$GATE cycle=$N) server start $(date '+%H:%M:%S') ==="
  bash "$SRV/serve_variant.sh" "$T" "$OUT" 2>&1 | tail -13; rc=${PIPESTATUS[0]}
  [ "$rc" -ne 0 ] && { echo "!! serve_variant exit=$rc — see 4.B"; exit 1; }
  tr '\0' ' ' < "/proc/$(cat "$OUT/server_$T.pid")/cmdline" > "$OUT/flags_$T.txt"
  echo -n "GATE argv: "; grep -o -- '--spec-draft-p-min [0-9.]*' "$OUT/flags_$T.txt" || echo "(none — correct only for row 1/10)"
  echo -n "GATE alias: "; curl -s http://127.0.0.1:8197/v1/models | python3 -c 'import sys,json;print([m["id"] for m in json.load(sys.stdin)["data"]])'
  ;;
sweep)
  ARGS=(--base-url "$URL" --model-id qwen3.5-397b --out "$OUT" --treatment "$TR")
  [ "$GATE" != "-" ] && ARGS+=(--gate-p-min "$GATE")
  ARGS+=(--cycle "$N" --ctx-size 65536 --subset both --seed 42 --max-tokens 256 --temperature 0
         --server-flags-file "$OUT/flags_$T.txt" --server-build c8e03ce
         --placement "n-cpu-moe 57, ctx 65536, no-mmap, flash-attn on, parallel 1"
         --note "WP-C gate ladder 2026-08-10, scratch port 8197, live qwen35-397b.service untouched")
  cd "$SWEEP" && ./mtpsweep run "${ARGS[@]}" 2>&1 | tee "$OUT/session_${T}_c${N}.log"
  echo "MTPSWEEP_EXIT=${PIPESTATUS[0]} at $(date '+%H:%M:%S')"
  ;;
close)
  echo "=== ROW $2 close: census ==="
  grep -l '"stream_options_fallback": true' "$OUT"/sessions/*.json 2>/dev/null && echo "!! FALLBACK — see 4.D" || echo "no fallback"
  grep -c 'HIDDEN-REASONING\|UNRECOGNISED-DELTA-FIELDS' "$OUT/session_${T}_c${N}.log" | xargs echo "abort markers in session log:"
  echo "=== stop ==="; bash "$SRV/stop_variant.sh" "$T" "$OUT" 2>&1 | tail -3
  # P7: cycle-tag IMMEDIATELY, before any verification reading
  for f in "server_$T.log" "load_$T.json" "flags_$T.txt"; do
    [ -e "$OUT/$f" ] && mv "$OUT/$f" "$OUT/${f%.*}_c${N}.${f##*.}"; done
  echo "archived: $(ls -1 "$OUT"/*_c${N}.* 2>/dev/null | grep -c "$T")"
  echo -n "VRAM: "; nvidia-smi --query-gpu=memory.used --format=csv,noheader
  free -g | awk '/^Mem:/{print "RAM available:",$7,"GB"}'
  ss -tln | awk '{print $4}' | grep -q '127.0.0.1:8197' && echo "!! 8197 STILL LISTENING" || echo "port 8197 clear"
  echo -n "draft acceptance: "; grep -o -i -E 'draft[a-z_ ]*accept[a-z_]*[ =:]+[0-9.]+' "$OUT/server_${T}_c${N}.log" 2>/dev/null | tail -2 | tr '\n' ' '; echo
  ;;
esac
