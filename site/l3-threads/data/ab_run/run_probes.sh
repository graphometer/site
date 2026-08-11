#!/usr/bin/env bash
# run_probes.sh ARM — 4 identical probes vs the loopback scratch server + one nvidia-smi.
# Probe = exact ladder gen prompt (l3_tuning_ladder.sh line 43), max_tokens 200, temp 0.
set -uo pipefail
ARM="$1"
D=<VAULT>/work/agent-staging/fable/2026-08-11_l3-field-card/ab_run
URL=http://127.0.0.1:8104
BODY='{"messages":[{"role":"user","content":"In about 100 words, explain why running AI models on personal hardware matters."}],"max_tokens":200,"temperature":0}'
for i in 1 2 3 4; do
  T0=$(date +%s.%N)
  curl -s -m 1800 "$URL/v1/chat/completions" -H 'Content-Type: application/json' \
    -d "$BODY" > "$D/arm_${ARM}_probe${i}.json"
  T1=$(date +%s.%N)
  WALL=$(python3 -c "print(f'{$T1-$T0:.1f}')")
  python3 - "$D/arm_${ARM}_probe${i}.json" "$ARM" "$i" "$WALL" <<'EOF'
import json,sys
p,arm,i,wall=sys.argv[1:5]
d=json.load(open(p)); t=d.get('timings',{})
print(f"arm={arm} probe={i} wall={wall}s "
      f"prompt_n={t.get('prompt_n')} prefill={t.get('prompt_per_second',0):.2f} t/s "
      f"predicted_n={t.get('predicted_n')} decode={t.get('predicted_per_second',0):.3f} t/s")
EOF
done
nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits | tee "$D/arm_${ARM}_nvidia_smi.txt"
