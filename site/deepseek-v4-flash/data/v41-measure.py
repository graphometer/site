#!/usr/bin/env python3
# DeepSeek V4.1 probe: cold decode, the same prompt again, then prefill at growing
# sizes with planted-code recall. Unchanged apart from the sweep.
# 
"""V4.1 port measurement: cold decode, resident decode (same prompt again), prefill at growing sizes with planted-code
recall, first-token latency. Prints the server's own timings. Usage: v41-measure.py [base] [sizes csv e.g. 2000,8000,32000]"""
import json, sys, time, urllib.request
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8199"
sizes = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "2000,8000").split(",")]
def chat(msgs, max_tokens):
    body = json.dumps({"model": "x", "messages": msgs, "max_tokens": max_tokens, "temperature": 0.7, "chat_template_kwargs": {"enable_thinking": False}}).encode()
    req = urllib.request.Request(base + "/v1/chat/completions", data=body, headers={"Content-Type": "application/json"})
    t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=36000)); return r, time.time() - t0
def rep(tag, r, w):
    t = r.get("timings", {}); msg = r["choices"][0]["message"]; txt = (msg.get("content") or "").strip().replace("\n", " "); rl = len(msg.get("reasoning_content") or "")
    print(f"[{tag}] prompt {t.get('prompt_n')} tok {t.get('prompt_ms',0)/1000:.1f} s = {t.get('prompt_per_second',0):.1f} t/s | decode {t.get('predicted_n')} tok = {t.get('predicted_per_second',0):.2f} t/s | wall {w:.1f} s", flush=True)
    print(f"        reply ({'thought '+str(rl)+' chars, ' if rl else ''}{len(txt)} chars):", txt[:200], flush=True); return txt
q = [{"role": "user", "content": "In three sentences, describe a harbour town at dawn and name one thing a visitor should do."}]
r, w = chat(q, 200); rep("cold short", r, w)
r, w = chat(q, 200); rep("same again (resident?)", r, w)
para = ("The river keeps its own hours. Boats go out before the light and come back when the gulls decide. "
        "Nobody on the quay hurries, and the coffee is always slightly burnt. ")
for n in sizes:
    parts = [para] * max(1, n // 40); code = f"MARLIN-{n}-COBALT"
    parts[len(parts)//2] = para + f" The harbourmaster's code word today is {code}. "
    r, w = chat([{"role": "user", "content": "".join(parts) + "\n\nWhat is the harbourmaster's code word today? Answer with the code word only."}], 60)
    txt = rep(f"depth~{n}", r, w); print("        recall:", "OK" if code in txt else "MISSED", flush=True)
