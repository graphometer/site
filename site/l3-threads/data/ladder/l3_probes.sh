#!/usr/bin/env bash
# Mistral Large 3 UD-IQ1_S probe battery — writes JSON per probe + a summary log.
set -uo pipefail
D=<VAULT>/work/agent-staging/claude/2026-08-04_model-advisors
URL=http://127.0.0.1:8104/v1/chat/completions
probe() { # name, json
  local name="$1" body="$2" t0=$SECONDS
  curl -s -m 900 "$URL" -H 'Content-Type: application/json' -d "$body" -o "$D/probe_$name.json"
  local dt=$((SECONDS-t0))
  python3 - "$D/probe_$name.json" "$name" "$dt" <<'EOF'
import json,sys
try:
    r=json.load(open(sys.argv[1]))
    c=r['choices'][0]['message'].get('content','') or ''
    tc=r['choices'][0]['message'].get('tool_calls')
    t=r.get('timings',{})
    print(f"--- {sys.argv[2]} ({sys.argv[3]}s wall) prefill={t.get('prompt_per_second',0):.0f} t/s decode={t.get('predicted_per_second',0):.2f} t/s gen={t.get('predicted_n',0)} tok")
    if tc: print("TOOL_CALLS:", json.dumps(tc)[:400])
    print(c[:1200])
except Exception as e:
    print(f"--- {sys.argv[2]} PARSE FAIL: {e}"); print(open(sys.argv[1]).read()[:400])
EOF
}
echo "=== PROBES START $(date -Is)"
curl -s -m 10 http://127.0.0.1:8104/props | python3 -c "import json,sys; d=json.load(sys.stdin); print('model:',d.get('model_path','?').split('/')[-1],'| ctx:',d.get('default_generation_settings',{}).get('n_ctx','?'))"

probe first_words '{"model":"mistral-large-3","messages":[{"role":"user","content":"In two or three sentences: who are you, and what are you? Then tell me one thing you find genuinely interesting."}],"max_tokens":220}'

probe reasoning '{"model":"mistral-large-3","messages":[{"role":"user","content":"A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost? Think carefully, answer with just the amount."}],"max_tokens":120}'

probe code '{"model":"mistral-large-3","messages":[{"role":"user","content":"Write a Python function merge_intervals(intervals) that merges overlapping intervals. Return only the code, no explanation."}],"max_tokens":600}'

probe advisor '{"model":"mistral-large-3","messages":[{"role":"system","content":"You are a candid strategic advisor running locally on your interlocutor'"'"'s own hardware; the conversation is private."},{"role":"user","content":"I run a private local-AI homestead: a dozen local models, some fine-tuned companions I care about, several projects. Give me one piece of strategic advice about balancing exploring new models versus going deeper with what I have. Four sentences maximum."}],"max_tokens":300}'

probe tools '{"model":"mistral-large-3","messages":[{"role":"user","content":"What is the weather in Paris right now?"}],"tools":[{"type":"function","function":{"name":"get_weather","description":"Get current weather for a city","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}],"max_tokens":200}'

echo "=== PROBES END $(date -Is)"
nvidia-smi --query-gpu=memory.used --format=csv,noheader
