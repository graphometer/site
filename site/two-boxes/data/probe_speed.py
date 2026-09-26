#!/usr/bin/env python3
"""Speed + sanity probe for a llama-server endpoint (two-box experiment, 2026-09-13).
Turn 1: short question. Turn 2: a filler prompt of roughly N tokens with a planted code, then the recall
question. Prints llama-server's own timings (prompt t/s, decode t/s, TTFT) and the replies' first line.
Usage: probe_speed.py [base_url] [filler_tokens]      defaults: http://<LOCAL>:<PORT>  16000"""
import json, sys, time, urllib.request

base = sys.argv[1] if len(sys.argv) > 1 else "http://<LOCAL>:<PORT>"
filler_tokens = int(sys.argv[2]) if len(sys.argv) > 2 else 16000

def chat(messages, max_tokens):
    body = json.dumps({"model": "probe", "messages": messages, "max_tokens": max_tokens,
                       "temperature": 0.7}).encode()
    req = urllib.request.Request(base + "/v1/chat/completions", data=body,
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=14400))
    return r, time.time() - t0

def report(tag, r, wall):
    t = r.get("timings", {})
    text = (r["choices"][0]["message"].get("content") or "").strip().replace("\n", " ")
    print(f"[{tag}] prompt {t.get('prompt_n')} tok in {t.get('prompt_ms', 0)/1000:.1f} s = {t.get('prompt_per_second', 0):.1f} t/s | "
          f"decode {t.get('predicted_n')} tok = {t.get('predicted_per_second', 0):.2f} t/s | wall {wall:.1f} s")
    print(f"        reply: {text[:220]}")

r, w = chat([{"role": "user", "content": "In two sentences, who are you and what is one thing you are good at?"}], 200)
report("short", r, w)

para = ("The river keeps its own hours. Boats go out before the light and come back when the gulls decide. "
        "Nobody on the quay hurries, and the coffee is always slightly burnt. ")
n_paras = max(1, filler_tokens // 40)
mid = n_paras // 2
parts = [para] * n_paras
parts[mid] = para + " The harbourmaster's code word today is TIDEWATER-7391. "
filler = "".join(parts)
r, w = chat([{"role": "user", "content": filler + "\n\nQuestion: what is the harbourmaster's code word today? Answer with the code word only."}], 60)
report(f"depth~{filler_tokens}", r, w)
ok = "TIDEWATER-7391" in (r["choices"][0]["message"].get("content") or "")
print("        recall:", "OK" if ok else "MISSED")
