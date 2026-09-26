#!/usr/bin/env python3
# DeepSeek V4.1 prefix-reuse probe. Unchanged apart from the sweep.
# 
"""Prefix-reuse test: a ~N-token conversation prefix, then the SAME prefix plus a new user turn. If the server reuses its
context, the second call's prompt_n is only the new tokens; if it re-reads, prompt_n ≈ N. Then a third turn. Thinking off."""
import json, sys, time, urllib.request
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8199"; n = int(sys.argv[2]) if len(sys.argv) > 2 else 30000
def chat(msgs, max_tokens=120):
    body = json.dumps({"model": "x", "messages": msgs, "max_tokens": max_tokens, "temperature": 0.7, "chat_template_kwargs": {"enable_thinking": False}}).encode()
    req = urllib.request.Request(base + "/v1/chat/completions", data=body, headers={"Content-Type": "application/json"})
    t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=36000)); return r, time.time() - t0
def rep(tag, r, w):
    t = r.get("timings", {}); txt = (r["choices"][0]["message"].get("content") or "").strip().replace("\n", " ")
    print(f"[{tag}] prompt {t.get('prompt_n')} tok {t.get('prompt_ms',0)/1000:.1f} s = {t.get('prompt_per_second',0):.1f} t/s | decode {t.get('predicted_n')} tok = {t.get('predicted_per_second',0):.2f} t/s | wall {w:.1f} s", flush=True)
    print("        reply:", txt[:160], flush=True); return txt
para = ("Granite steps lead down to the water where the ferries idle. A bell rings twice from the chapel on the hill, "
        "and the bakery's shutters go up before the mist has lifted from the moorings. ")
parts = [para] * max(1, n // 42); parts[len(parts)//2] = para + " The lighthouse keeper's password this morning is GRANITE-4406. "
history = [{"role": "system", "content": "You are a careful assistant. Keep answers short."},
           {"role": "user", "content": "Here is the town record:\n" + "".join(parts) + "\n\nAcknowledge in one sentence."}]
r, w = chat(history); a = rep(f"turn 1 (read ~{n})", r, w); history.append({"role": "assistant", "content": a})
history.append({"role": "user", "content": "What is the lighthouse keeper's password this morning? Code only."})
r, w = chat(history); a = rep("turn 2 (+1 question , reuse?)", r, w); print("        recall:", "OK" if "GRANITE-4406" in a else "MISSED", flush=True); history.append({"role": "assistant", "content": a})
history.append({"role": "user", "content": "Name the three things a visitor would notice first, one line each."})
r, w = chat(history, 160); rep("turn 3 (+1 more)", r, w)
