#!/usr/bin/env bash
# One Large 4 config: start, then the same questions as before. usage: run_config.sh NAME SERVE_SCRIPT [server flags]
T=<REDACTED_PATH>; cd $T; N=$1; SC=$2; shift 2
setsid nohup bash $SC "$@" > logs/$N.log 2>&1 < /dev/null &
sleep 5; P=$(pgrep -nx llama-server); echo $P > logs/server.pid
S=$(date +%s); until curl -s -m 3 http://127.0.0.1:<PORT>/health | grep -q '"ok"' || ! kill -0 $P 2>/dev/null || [ $(( $(date +%s)-S )) -gt 900 ]; do sleep 5; done
kill -0 $P 2>/dev/null || { echo "$N server died"; grep -E ' E |out of memory|failed' logs/$N.log | head -5 | cut -c1-170; exit 1; }
echo "$N pid $P ready after $(( $(date +%s)-S ))s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader)"
F='wall|prompt_n|prompt_tps|gen_n|gen_tps|major|drive|cpu_cores|finish'
ask(){ timeout $3 python3 -I probe.py http://127.0.0.1:<PORT> $P nvme0n1 $N-$1 $4 "$2" 2>&1 | grep -E "$F" | cut -c1-60 | tr -d '\n'; echo; }
ask short1 "What causes tides on Earth? Round 1: answer in two sentences." 600 250
ask short2 "What causes tides on Earth? Round 2: answer in two sentences." 600 250
ask long1 "Round 1. Explain how a refrigerator works, step by step, in about 300 words." 700 800
ask long2 "Round 2. Explain how a refrigerator works, step by step, in about 300 words." 700 800
ask read2k "$(head -c 9000 /usr/share/common-licenses/GPL-3)

Summarize the text above in two sentences." 1200 350
ask after "Name two moons of Jupiter." 600 250
free -g | sed -n 2p; nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv,noheader
