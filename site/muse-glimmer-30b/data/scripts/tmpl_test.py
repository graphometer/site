#!/usr/bin/env python3
"""Does reasoning_strength survive a caller-supplied system message?

Documented template: injects 'Reasoning strength: <rs>.' into a caller's system
message when the caller has not written one.  Undocumented/unsloth template: does not.
Prediction: on Meta's documented file the high/low pair diverges WITH a system message;
on unsloth's file it does not.
"""
import json, os, sys, urllib.request

TAG = sys.argv[1]
URL = "http://127.0.0.1:8195/v1/chat/completions"
OUT = "<VAULT>/work/agent-staging/fable/2026-08-16_muse-glimmer/runs/study/tmpl"
os.makedirs(OUT, exist_ok=True)

Q = "How many R's are in the word strawberry? Answer with just the number."
SYS = "You are a careful assistant."


def go(name, msgs, rs):
    b = {"model": "muse-glimmer-30b", "messages": msgs, "max_tokens": 4000, "temperature": 0}
    if rs:
        b["chat_template_kwargs"] = {"reasoning_strength": rs}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        URL, json.dumps(b).encode(), {"Content-Type": "application/json"}), timeout=600))
    json.dump(r, open(f"{OUT}/{TAG}_{name}.json", "w"), indent=1)
    m = r["choices"][0]["message"]
    return (r["usage"]["prompt_tokens"], len(m.get("reasoning_content") or ""),
            r["usage"]["completion_tokens"], (m.get("content") or "")[:20])


print(f"--- {TAG} ---")
for label, msgs in [("nosys", [{"role": "user", "content": Q}]),
                    ("withsys", [{"role": "system", "content": SYS},
                                 {"role": "user", "content": Q}])]:
    res = {}
    for rs in ["high", "low"]:
        res[rs] = go(f"{label}_{rs}", msgs, rs)
        print(f"  {label:8s} rs={rs:5s} prompt_tok={res[rs][0]:4} reason_ch={res[rs][1]:5} "
              f"completion={res[rs][2]:4} content={res[rs][3]!r}")
    same = res["high"][1] == res["low"][1] and res["high"][2] == res["low"][2]
    print(f"  {label:8s} -> high/low IDENTICAL: {same}  "
          f"(lever {'DEAD' if same else 'LIVE'} on this path)")
