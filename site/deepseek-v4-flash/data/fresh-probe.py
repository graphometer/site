#!/usr/bin/env python3
# Fresh-prompt probe: a prompt the server has never seen, with a code planted at the
# midpoint, so the reading rate is not served from cache. Unchanged apart from the sweep.
# 
"""Warm-weights prefill measurement: a NEW ~N-token prompt (different text, so no prefix cache), then decode 120 tokens."""
import json, sys, time, urllib.request
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8199"
n = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
para = ("Granite steps lead down to the water where the ferries idle. A bell rings twice from the chapel on the hill, "
        "and the bakery's shutters go up before the mist has lifted from the moorings. ")
parts = [para] * max(1, n // 42)
parts[len(parts)//2] = para + " The lighthouse keeper's password this morning is GRANITE-4406. "
prompt = "".join(parts) + "\n\nWhat is the lighthouse keeper's password this morning, and then describe the town in three sentences?"
body = json.dumps({"model": "probe", "messages": [{"role": "user", "content": prompt}], "max_tokens": 400, "temperature": 0.7}).encode()
req = urllib.request.Request(base + "/v1/chat/completions", data=body, headers={"Content-Type": "application/json"})
t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=14400)); w = time.time() - t0
t = r["timings"]; txt = (r["choices"][0]["message"].get("content") or "").strip().replace("\n", " ")
print(f"[fresh~{n}] prompt {t['prompt_n']} tok in {t['prompt_ms']/1000:.1f} s = {t['prompt_per_second']:.1f} t/s | decode {t['predicted_n']} tok = {t['predicted_per_second']:.2f} t/s | wall {w:.1f} s")
print("        reply:", txt[:300]); print("        recall:", "OK" if "GRANITE-4406" in txt else "MISSED")
