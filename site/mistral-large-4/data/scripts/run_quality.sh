#!/usr/bin/env bash
# Quality second pass, from the trial's run_round2.sh: Large 3 and deepseek-v41-flash-ista in full, Large 4 on the three questions it has not answered, at the best shape found on 2026-11-01.
# One server at a time, by PID. Answers go to quality/answers/.
S=<REDACTED_PATH>; T=<REDACTED_PATH>; cd $T
wait_ok(){ St=$(date +%s); until curl -s -m 3 $1/health | grep -q '"ok"' || [ $(( $(date +%s)-St )) -gt 1500 ]; do sleep 5; done; curl -s -m 3 $1/health | grep -q '"ok"' && echo "ready $(( $(date +%s)-St ))s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"; }
stop_srv(){ [ -n "$1" ] || { echo "no pid"; return; }; kill $1; for i in $(seq 1 90); do kill -0 $1 2>/dev/null || break; sleep 1; done; kill -0 $1 2>/dev/null && { kill -9 $1; sleep 5; }; echo "stopped $1"; }
warm='{"messages":[{"role":"user","content":"Say hello in one short sentence."}],"max_tokens":120}'
pgrep -x llama-server > /dev/null && { echo "REFUSED: a llama-server is running"; echo ROUND_DONE; exit 3; }
echo "== Large 3 $(date +%T)"
setsid nohup bash <LARGE3_START_SCRIPT> > $S/logs/q-large3.log 2>&1 < /dev/null &
wait_ok http://<LOCAL>; P=$(pgrep -nx llama-server)
curl -s -m 900 http://<LOCAL>/v1/chat/completions -H 'Content-Type: application/json' -d "$warm" > /dev/null
timeout 8000 python3 -I ask_round.py http://<LOCAL> large3 4000 1200
stop_srv $P; sleep 3
echo "== ista $(date +%T)"
setsid nohup bash <DEEPSEEK_START_SCRIPT> --n-cpu-moe 36 --batch-size 2048 --ubatch-size 2048 > $S/logs/q-ista.log 2>&1 < /dev/null &
U=http://127.0.0.1:$(grep -o -- '--port [0-9]*' <DEEPSEEK_START_SCRIPT> | cut -d' ' -f2); wait_ok $U; P=$(pgrep -nx llama-server)
curl -s -m 900 $U/v1/chat/completions -H 'Content-Type: application/json' -d "$warm" > /dev/null
timeout 11000 python3 -I ask_round.py $U deepseek-v41-flash-ista 12000 1800 '{"chat_template_kwargs":{"enable_thinking":true}}'
stop_srv $P; sleep 3
echo "== Large 4 $(date +%T)"
ssh <LAPTOP> "ss -ltn | grep -q ':<PORT> '" || { echo "Z13 worker is not up"; echo ROUND_DONE; exit 5; }
LAYOUT=expz Z=30 GPU_N=0 CTX=131072 UB=1024 CPUS=0-15 T=16 setsid nohup bash $S/ml4/serve_ml4.sh --load-mode dio > $S/logs/q-large4.log 2>&1 < /dev/null &
wait_ok http://127.0.0.1:<PORT>; P=$(pgrep -nx llama-server)
QIDS="q1-logic q2-probability q6-decision" timeout 16500 python3 -I ask_round.py http://127.0.0.1:<PORT> large4 10000 5400
stop_srv $P; sleep 3
echo "== Large 4, three experts $(date +%T)"
LAYOUT=expz Z=30 GPU_N=0 CTX=131072 UB=1024 CPUS=0-15 T=16 setsid nohup bash $S/ml4/serve_ml4.sh --load-mode dio --override-kv mistral-large4.expert_used_count=int:3 > $S/logs/q-large4-3experts.log 2>&1 < /dev/null &
wait_ok http://127.0.0.1:<PORT>; P=$(pgrep -nx llama-server)
timeout 16500 python3 -I ask_round.py http://127.0.0.1:<PORT> large4-3experts 10000 5400
stop_srv $P; sleep 2
echo "ROUND_DONE $(date +%T)"
