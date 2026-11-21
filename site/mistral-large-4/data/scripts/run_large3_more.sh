#!/usr/bin/env bash
# Large 3's q1 and q2 stopped at the old plan's 4,000-token limit, before their answers. Same server and questions with 12,000 tokens, so the judge compares finished answers.
# The cut versions stay in quality/answers-large3-cut-4000/. Run only after run_quality.sh has finished.
S=<REDACTED_PATH>; T=<REDACTED_PATH>; cd $T
wait_ok(){ St=$(date +%s); until curl -s -m 3 $1/health | grep -q '"ok"' || [ $(( $(date +%s)-St )) -gt 1500 ]; do sleep 5; done; curl -s -m 3 $1/health | grep -q '"ok"' && echo "ready $(( $(date +%s)-St ))s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"; }
stop_srv(){ [ -n "$1" ] || { echo "no pid"; return; }; kill $1; for i in $(seq 1 90); do kill -0 $1 2>/dev/null || break; sleep 1; done; kill -0 $1 2>/dev/null && { kill -9 $1; sleep 5; }; echo "stopped $1"; }
warm='{"messages":[{"role":"user","content":"Say hello in one short sentence."}],"max_tokens":120}'
pgrep -x llama-server > /dev/null && { echo "REFUSED: a llama-server is running"; echo MORE_DONE; exit 3; }
mkdir -p quality/answers-large3-cut-4000
cp -n quality/answers/large3-q1-logic.json quality/answers/large3-q2-probability.json quality/answers-large3-cut-4000/
echo "== Large 3, more room $(date +%T)"
setsid nohup bash <REDACTED_PATH>/start_server.sh > $S/logs/q-large3-more.log 2>&1 < /dev/null &
wait_ok http://<LOCAL>; P=$(pgrep -nx llama-server)
curl -s -m 900 http://<LOCAL>/v1/chat/completions -H 'Content-Type: application/json' -d "$warm" > /dev/null
QIDS="q1-logic q2-probability" timeout 8000 python3 -I ask_round.py http://<LOCAL> large3 12000 3600
stop_srv $P
echo "MORE_DONE $(date +%T)"
