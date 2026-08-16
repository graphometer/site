#!/usr/bin/env python3
"""The real documented-vs-undocumented template difference.

Documented template: normalizes a caller-written "Reasoning effort" line to
"Reasoning strength" AND suppresses its own injection when one is already present.
Undocumented template (= unsloth's file): no normalization, and it appends its own
default directive unconditionally -> a caller who writes their own gets TWO,
potentially contradictory, directives.

Measured signal: rendered prompt_tokens. Suppression => fewer tokens.
"""
import json, os, sys, urllib.request

TAG = sys.argv[1]
URL = "http://127.0.0.1:8195/v1/chat/completions"
OUT = "<VAULT>/work/agent-staging/fable/2026-08-16_muse-glimmer/runs/study/tmpl"
os.makedirs(OUT, exist_ok=True)
Q = "How many R's are in the word strawberry? Answer with just the number."

CASES = {
    "sys_plain":        "You are a careful assistant.",
    "sys_effort_low":   "You are a careful assistant.\nReasoning effort: low.",
    "sys_strength_low": "You are a careful assistant.\nReasoning strength: low.",
}
print(f"--- {TAG} ---")
for name, sys_txt in CASES.items():
    b = {"model": "muse-glimmer-30b",
         "messages": [{"role": "system", "content": sys_txt},
                      {"role": "user", "content": Q}],
         "max_tokens": 4000, "temperature": 0}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        URL, json.dumps(b).encode(), {"Content-Type": "application/json"}), timeout=600))
    json.dump(r, open(f"{OUT}/{TAG}_dedup_{name}.json", "w"), indent=1)
    m = r["choices"][0]["message"]
    print(f"  {name:17s} prompt_tok={r['usage']['prompt_tokens']:4} "
          f"reason_ch={len(m.get('reasoning_content') or ''):5} "
          f"completion={r['usage']['completion_tokens']:4}")
