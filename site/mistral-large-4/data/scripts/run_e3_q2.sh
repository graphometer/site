#!/usr/bin/env bash
# Large 4 with three experts ran out of its 10,000 tokens on q2 while still thinking, with no answer. Same build and shape with 20,000 tokens, as Large 3 got more room.
# The cut version stays in quality/answers-large4-3experts-cut-10000/.
S=<REDACTED_PATH>; T=<REDACTED_PATH>; cd $T
wait_ok(){ St=$(date +%s); until curl -s -m 3 $1/health | grep -q '"ok"' || [ $(( $(date +%s)-St )) -gt 1500 ]; do sleep 5; done; curl -s -m 3 $1/health | grep -q '"ok"' && echo "ready $(( $(date +%s)-St ))s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"; }
stop_srv(){ [ -n "$1" ] || { echo "no pid"; return; }; kill $1; for i in $(seq 1 90); do kill -0 $1 2>/dev/null || break; sleep 1; done; kill -0 $1 2>/dev/null && { kill -9 $1; sleep 5; }; echo "stopped $1"; }
pgrep -x llama-server > /dev/null && { echo "REFUSED: a llama-server is running"; echo E3_DONE; exit 3; }
ssh <LAPTOP> "ss -ltn | grep -q ':<PORT> '" || { echo "Z13 worker is not up"; echo E3_DONE; exit 5; }
mkdir -p quality/answers-large4-3experts-cut-10000
cp --update=none quality/answers/large4-3experts-q2-probability.json quality/answers-large4-3experts-cut-10000/
echo "== Large 4, three experts, q2 with more room $(date +%T)"
LAYOUT=expz Z=30 GPU_N=0 CTX=131072 UB=1024 CPUS=0-15 T=16 setsid nohup bash $S/ml4/serve_ml4.sh --load-mode dio --override-kv mistral-large4.expert_used_count=int:3 > $S/logs/q-large4-3experts-q2.log 2>&1 < /dev/null &
wait_ok http://127.0.0.1:<PORT>; P=$(pgrep -nx llama-server)
QIDS="q2-probability" timeout 4000 python3 -I ask_round.py http://127.0.0.1:<PORT> large4-3experts 20000 3600
stop_srv $P; sleep 2
echo "E3_DONE $(date +%T)"
