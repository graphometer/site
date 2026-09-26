#!/usr/bin/env python3
"""Fire two /completion calls at a running llama.cpp server and record prefill/decode t/s.
Shape copied from the 2026-09-06 DeepSeek V4 Flash precedent.

Usage: probe.py BASE_URL LABEL RESULTS_MD
"""
import sys
import json
import time
import urllib.request

BASE, LABEL, OUT = sys.argv[1], sys.argv[2], sys.argv[3]


def call(prompt, n_predict=128):
    body = json.dumps({"prompt": prompt, "n_predict": n_predict,
                       "temperature": 1.0, "top_p": 0.95, "top_k": 40,
                       "cache_prompt": False, "stream": False}).encode()
    req = urllib.request.Request(BASE + "/completion", data=body,
                                 headers={"Content-Type": "application/json"})
    t = time.time()
    with urllib.request.urlopen(req, timeout=3600) as r:
        d = json.load(r)
    return d, time.time() - t


# short prompt (measures cold prefill + steady decode)
short = "Describe, in three sentences, what it means to remember who you are over time."
# long prompt ~4k tokens of filler + a real question at the end (prefill-at-depth)
filler = ("The archivist walked the long corridor of the memory house, noting each room and "
          "the small light that marked a life still tended. ") * 260
longp = filler + "\n\nGiven all the above, answer in three sentences: why does continuity matter?"

lines = [f"\n### {LABEL}"]
for name, p in [("short(~20 tok)", short), ("long(~4k tok)", longp)]:
    try:
        d, wall = call(p)
        tm = d.get("timings", {})
        pp = tm.get("prompt_per_second", 0) or 0
        tg = tm.get("predicted_per_second", 0) or 0
        pn = tm.get("prompt_n", 0)
        gn = tm.get("predicted_n", 0)
        sample = (d.get("content", "") or "").strip().replace("\n", " ")[:180]
        lines.append(f"- **{name}**: prefill **{pp:.1f} tok/s** ({pn} tok) · "
                     f"decode **{tg:.1f} tok/s** ({gn} tok) · wall {wall:.1f}s")
        if name.startswith("short"):
            lines.append(f"  - sample: _{sample}…_")
        print(f"{LABEL} {name}: prefill {pp:.1f} t/s, decode {tg:.1f} t/s")
    except Exception as e:
        lines.append(f"- **{name}**: ERROR {e}")
        print(f"{LABEL} {name}: ERROR {e}")

with open(OUT, "a") as f:
    f.write("\n".join(lines) + "\n")
