#!/usr/bin/env bash
# One Large 4 config: worker up, server up, warm with two questions, then time it. usage: LAYOUT=.. Z=.. GPU_N=.. run_ml4.sh NAME [server flags]. Stops the server by PID; leaves the worker running for the next config.
S=<REDACTED_PATH>; D=$S/ml4; N=$1; shift
pgrep -x llama-server >/dev/null && { echo "REFUSED: a llama-server is running"; exit 3; }
ZB=${ZB:-<REDACTED_PATH>}; ZT=${ZT:-16}; ZC=${ZC:-0-15}
ssh <LAPTOP> "ss -ltn | grep -q ':<PORT> ' || (cd $ZB; ${ZENV:-} GOMP_CPU_AFFINITY=$ZC nohup setsid taskset -c $ZC ./ggml-rpc-server -H <LAPTOP> -p <PORT> -d CPU -t $ZT > <WORKER_LOG> 2>&1 < /dev/null & sleep 3)"
ssh <LAPTOP> "ss -ltn | grep -q ':<PORT> '" || { echo "$N: worker did not start"; ssh <LAPTOP> tail -3 <WORKER_LOG>; exit 5; }

python3 -I <CORE_LOGGER> $S/logs/$N.cores.log & C=$!; trap 'kill $C 2>/dev/null' EXIT
setsid nohup bash $D/serve_ml4.sh "$@" > $S/logs/$N.server.log 2>&1 < /dev/null &
sleep 4; P=$(pgrep -nx llama-server); [ -n "$P" ] || { echo "$N: no server"; tail -5 $S/logs/$N.server.log | cut -c1-200; exit 4; }
St=$(date +%s); until curl -s -m 3 http://127.0.0.1:${PORT:-<PORT>}/health | grep -q '"ok"' || ! kill -0 $P 2>/dev/null || [ $(( $(date +%s)-St )) -gt 1200 ]; do sleep 5; done
kill -0 $P 2>/dev/null || { echo "$N: server died"; grep -E ' E |out of memory|failed|Available' $S/logs/$N.server.log | head -6 | cut -c1-200; exit 1; }
echo "$N: pid $P ready after $(( $(date +%s)-St )) s, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader), Z13 $(ssh <LAPTOP> "free -g | awk '/^Mem:/{print \$3\" GiB used\"}'")"
U=http://127.0.0.1:${PORT:-<PORT>}
if [ "${LAYOUT:-front}" = front ]; then F=${Z:-26}; L=$((71-${GPU_N:-4})); else F=${GPU_N:-4}; L=$((71-${Z:-26})); fi
echo "huge pages: server $(awk '/^Rss:/{r=$2}/^AnonHuge/{h=$2}END{printf "%.1f of %.1f GiB",h/1048576,r/1048576}' /proc/$P/smaps_rollup), Z13 $(ssh <LAPTOP> "awk '/^AnonHuge/{printf \"%.1f GiB\",\$2/1048576}' /proc/meminfo")"
[ "${PREFETCH:-1}" = 1 ] && taskset -c 16-23 python3 -I $D/prefetch_ml4.py $F $L 6
ask(){ timeout 3300 python3 -I $D/probe_ml4.py $U $P $N "$1" "$3" "$2" 2>&1 | tail -1 | cut -c1-240; }
[ -n "${QUICK:-}" ] || { ask warm1 "What causes tides on Earth? Answer in two sentences." 150; ask warm2 "Name three moons of Jupiter." 150; }
ask w300a "Explain how a refrigerator works, step by step, in about 300 words." ${WT:-500}
[ -n "${QUICK:-}" ] || ask w300b "Explain how a bicycle stays upright, step by step, in about 300 words." ${WT:-500}
ask read2k "$(head -c ${RK:-9000} /usr/share/common-licenses/GPL-3)

Summarize the text above in two sentences." 300
ask final "Explain how a lock and key work, step by step, in about 200 words." ${WT:-500}
[ -n "${POST:-}" ] && (eval "$POST")
grep -m1 -E "graph splits" $S/logs/$N.server.log | cut -c1-120
kill $P; for i in $(seq 1 120); do kill -0 $P 2>/dev/null || break; sleep 1; done; kill -0 $P 2>/dev/null && { kill -9 $P; echo "needed kill -9"; }
sleep 4; echo "$N: stopped, card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader), load $(cut -d' ' -f1-3 /proc/loadavg)"
