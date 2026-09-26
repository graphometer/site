#!/usr/bin/env python3
# DeepSeek V4.1 real-prose probe. THIS SHIPPED COPY DIFFERS FROM THE ONE THAT PRODUCED
# THE 12.5 TOKENS A SECOND FIGURE: the original read about 120,000 characters of our own
# prose documentation straight off disk. That input is not public, so the shipped copy
# takes the text from a file named on the command line. Supply any prose of the same
# length to reproduce the shape of the measurement, not the figure itself.
# 
"""Realistic-text prefill: ~N tokens of real prose from a text file with a planted code, one question. Thinking off."""
import json, sys, time, urllib.request, re
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8199"; nchars = int(sys.argv[2]) if len(sys.argv) > 2 else 120000
src = sys.argv[3] if len(sys.argv) > 3 else "input.txt"   # public placeholder: the original read an internal prose document
txt = open(src, encoding="utf-8", errors="ignore").read()[:nchars]
mid = len(txt)//2; txt = txt[:mid] + "\n\n(Note for the reader: the archivist's code word for this document is HERON-2148-SAFFRON.)\n\n" + txt[mid:]
body = json.dumps({"model": "x", "messages": [{"role": "user", "content": txt + "\n\nWhat is the archivist's code word for this document? Code only."}], "max_tokens": 120, "temperature": 0.7, "chat_template_kwargs": {"enable_thinking": False}}).encode()
req = urllib.request.Request(base + "/v1/chat/completions", data=body, headers={"Content-Type": "application/json"})
t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=36000)); w = time.time() - t0
t = r["timings"]; a = (r["choices"][0]["message"].get("content") or "").strip().replace("\n", " ")
print(f"[realtext {nchars} chars] prompt {t['prompt_n']} tok {t['prompt_ms']/1000:.1f} s = {t['prompt_per_second']:.1f} t/s | decode {t['predicted_n']} tok = {t['predicted_per_second']:.2f} t/s | wall {w:.1f} s", flush=True)
print("        reply:", a[:120], "| recall:", "OK" if "HERON-2148-SAFFRON" in a else "MISSED", flush=True)
