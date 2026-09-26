#!/usr/bin/env bash
# run_fn.sh — Flash-Next at its served 262,144 window through a staged copy of its start script: the shipped batch
# (-b 4096 -ub 2048) first, from a cold page cache, then llama.cpp's default (-b 2048 -ub 512). Each rung reads
# ~3,000 tokens twice (the first request after start, then warm), ~48,000 and ~230,000 (three sealed codes).
set -u
F=<REDACTED_PATH>
export FN_ENV_FILE=$F/scripts/kfn_test.env
BASE=http://<LOCAL>
for rung in shipped_b4096_ub2048 default_b2048_ub512; do
  if [ "$rung" = default_b2048_ub512 ]; then export FN_BATCH=2048 FN_UBATCH=512; else unset FN_BATCH FN_UBATCH; fi
  pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is running"; exit 1; }
  echo "== $rung $(date +%T) · resident before start: $(python3 $F/scripts/resident.py <REDACTED_PATH>/*.gguf)"
  t0=$(date +%s)
  setsid bash $F/scripts/sfn_variant.sh > $F/logs/$rung.server.log 2>&1 & echo $! > $F/logs/$rung.pid
  until curl -s -m 2 $BASE/health | grep -q ok; do
    sleep 2; kill -0 $(cat $F/logs/$rung.pid) 2>/dev/null || { echo "DIED on load"; tail -5 $F/logs/$rung.server.log; exit 1; }
    [ $(( $(date +%s) - t0 )) -gt 900 ] && { echo "never healthy"; exit 1; }
  done
  echo "  healthy in $(( $(date +%s) - t0 )) s · VRAM $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · n_ctx $(curl -s $BASE/props | python3 -c 'import json,sys; print(json.load(sys.stdin)["default_generation_settings"]["n_ctx"])') · resident after load: $(python3 $F/scripts/resident.py <REDACTED_PATH>/*.gguf | python3 -c 'import json,sys; print(json.load(sys.stdin)["resident_gb"])') GB"
  grep -m3 -E "n_batch|n_ubatch" $F/logs/$rung.server.log | sed 's/^/  /'
  python3 $F/scripts/fn_reads.py --base $BASE --tag $rung --out $F/results/$rung.jsonl --sizes 3000,3000,48000,230000 --recall3 230000
  kill -TERM -- -$(cat $F/logs/$rung.pid) 2>/dev/null; sleep 5; pkill -TERM -x llama-server 2>/dev/null; sleep 3
  echo "  stopped $(date +%T) · VRAM $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"
done
echo RUN_FN_DONE
