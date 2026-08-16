#!/usr/bin/env python3
"""DFlash speed study — paired same-prompt design, one arm per process.

Usage: speed.py <arm-name>
Every prompt is used exactly ONCE per arm (no prompt reuse -> no prefix-cache reuse).
The same 12 prompts run in every arm, so the comparison is paired per prompt.
Greedy decoding + single request, matching the vendor's stated method.
"""
import json, os, sys, time, urllib.request

ARM = sys.argv[1]
URL = "http://127.0.0.1:8195/v1/chat/completions"
OUT = "<VAULT>/work/agent-staging/fable/2026-08-16_muse-glimmer/runs/study/speed"
os.makedirs(OUT, exist_ok=True)

PROSE = [
    "Write four paragraphs about why coastal fishing villages in Iceland declined in the twentieth century.",
    "Write four paragraphs explaining how a mechanical watch escapement works, for a curious adult.",
    "Write four paragraphs about the history of the Dutch windmill and its role in land reclamation.",
    "Write four paragraphs describing the life cycle of a monarch butterfly and its migration.",
    "Write four paragraphs on how sourdough starter cultures work biologically.",
    "Write four paragraphs about the invention and spread of the printing press in Europe.",
]
STRUCTURED = [
    "Write a Python class LRUCache with get and put, using a dict and a doubly linked list. Include docstrings. Output only code.",
    "Write a JSON array of 12 objects, each with keys id, name, country, founded_year, describing 12 European universities. Output only JSON.",
    "Write a Python module with five functions for vector math (add, sub, dot, norm, normalize) with full type hints and docstrings. Output only code.",
    "Write a JSON object mapping 15 chemical element symbols to objects with keys name, atomic_number, group. Output only JSON.",
    "Write a Python implementation of a binary search tree with insert, find, and in-order traversal, fully commented. Output only code.",
    "Write a markdown table with 15 rows comparing 15 programming languages across columns: language, year, paradigm, typing, main use.",
]
PROMPTS = [("prose", p) for p in PROSE] + [("structured", p) for p in STRUCTURED]


def call(prompt, max_tokens=900):
    body = {"model": "muse-glimmer-30b", "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens, "temperature": 0}
    req = urllib.request.Request(URL, json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    t0 = time.time()
    r = json.load(urllib.request.urlopen(req, timeout=900))
    return r, time.time() - t0


# warmup, discarded (never judge a cold first answer)
call("Say hello in one short sentence.", 200)
time.sleep(1)

rows, raws = [], []
for i, (kind, p) in enumerate(PROMPTS):
    r, wall = call(p)
    t = r.get("timings", {})
    u = r.get("usage", {})
    rows.append({
        "arm": ARM, "i": i, "kind": kind, "prompt": p[:60],
        "prompt_n": t.get("prompt_n"), "predicted_n": t.get("predicted_n"),
        "predicted_ms": round(t.get("predicted_ms", 0), 1),
        "decode_tps": round(t.get("predicted_per_second", 0), 2),
        "prefill_tps": round(t.get("prompt_per_second", 0), 2),
        "draft_n": t.get("draft_n"), "draft_n_accepted": t.get("draft_n_accepted"),
        "wall_s": round(wall, 2),
        "finish": r["choices"][0].get("finish_reason"),
        "completion_tokens": u.get("completion_tokens"),
    })
    raws.append(r)
    print(f"[{ARM}] {i:2d} {kind:10s} n={rows[-1]['predicted_n']:4} "
          f"decode={rows[-1]['decode_tps']:7.2f} t/s  draft={rows[-1]['draft_n']}/"
          f"{rows[-1]['draft_n_accepted']}")

json.dump(rows, open(f"{OUT}/{ARM}_rows.json", "w"), indent=1)
json.dump(raws, open(f"{OUT}/{ARM}_raw.json", "w"), indent=1)

for k in ("prose", "structured"):
    v = [r["decode_tps"] for r in rows if r["kind"] == k]
    v.sort()
    print(f"[{ARM}] {k:10s} median {v[len(v)//2]:.2f} t/s  min {v[0]:.2f}  max {v[-1]:.2f}")
print(f"[{ARM}] DONE")
