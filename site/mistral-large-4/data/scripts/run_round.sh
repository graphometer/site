#!/usr/bin/env bash
# Quality round: Large 4 across both machines, then Large 3, then deepseek-v41-flash-ista, one at a time.
T=<REDACTED_PATH>; cd $T
wait_ok(){ S=$(date +%s); until curl -s -m 3 $1/health | grep -q '"ok"' || ! kill -0 $2 2>/dev/null || [ $(( $(date +%s)-S )) -gt 1200 ]; do sleep 5; done; curl -s -m 3 $1/health | grep -q '"ok"' && echo "ready $(( $(date +%s)-S ))s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"; }
stop_srv(){ kill $1; for i in $(seq 1 90); do kill -0 $1 2>/dev/null || break; sleep 1; done; kill -0 $1 2>/dev/null && { kill -9 $1; sleep 5; }; echo "stopped $1"; }
warm='{"messages":[{"role":"user","content":"Say hello in one short sentence."}],"max_tokens":120}'
echo "== Large 4 $(date +%T)"
ssh <LAPTOP> 'cd <REDACTED_PATH>; nohup setsid ./ggml-rpc-server -H <LAPTOP> -p <PORT> -d CPU -t 16 > <REDACTED_PATH>/rpc-b12015.log 2>&1 < /dev/null & sleep 4'
GPU_FULL=4 setsid nohup bash serve_split.sh --ctx-size 32768 --batch-size 2048 --ubatch-size 512 > logs/round-l4.log 2>&1 < /dev/null &
sleep 5; P=$(pgrep -nx llama-server); wait_ok http://127.0.0.1:<PORT> $P
curl -s -m 900 http://127.0.0.1:<PORT>/v1/chat/completions -H 'Content-Type: application/json' -d "$warm" > /dev/null
timeout 12000 python3 -I ask_round.py http://127.0.0.1:<PORT> large4 6000 1800
stop_srv $P; sleep 2
W=$(ssh <LAPTOP> 'ps -eo pid,args | grep "[p]c-server -H <LAPTOP> -p <PORT>"' | awk '{print $1}'); [ -n "$W" ] && ssh <LAPTOP> "kill $W"; echo "worker $W stopped"
echo "== Large 3 $(date +%T)"
setsid nohup bash <REDACTED_PATH>/start_server.sh > logs/round-l3.log 2>&1 < /dev/null &
sleep 8; P=$(pgrep -nx llama-server); wait_ok http://<LOCAL> $P
curl -s -m 900 http://<LOCAL>/v1/chat/completions -H 'Content-Type: application/json' -d "$warm" > /dev/null
timeout 3600 python3 -I ask_round.py http://<LOCAL> large3 3000 900
stop_srv $P; sleep 3
echo "== ista $(date +%T)"
setsid nohup bash <REDACTED_PATH>/serve_ista.sh --n-cpu-moe 36 --batch-size 2048 --ubatch-size 2048 > logs/round-ista.log 2>&1 < /dev/null &
sleep 8; P=$(pgrep -nx llama-server); U=http://127.0.0.1:$(grep -o -- '--port [0-9]*' <REDACTED_PATH>/serve_ista.sh | cut -d' ' -f2); wait_ok $U $P
timeout 3600 python3 -I ask_round.py $U deepseek-v41-flash-ista 8000 900 '{"chat_template_kwargs":{"enable_thinking":true}}'
stop_srv $P
echo "ROUND_DONE $(date +%T)"
