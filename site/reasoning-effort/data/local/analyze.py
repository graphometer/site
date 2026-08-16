#!/usr/bin/env python3
"""Summarize the 2026-08-16 effort grid into a TSV + a determinism check."""
import json
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")

rows = []
for p in sorted(glob.glob(os.path.join(RAW, "grid_*.json"))):
    d = json.load(open(p))
    rows.append(d)

cols = ["prompt", "effort", "rep", "prompt_tokens", "reasoning_tokens", "visible_tokens",
        "completion_tokens", "reasoning_chars", "visible_chars", "finish_reason",
        "think_leak_in_content", "wall_s", "predicted_per_second"]

with open(os.path.join(HERE, "effort_grid.tsv"), "w") as f:
    f.write("\t".join(cols) + "\n")
    for r in rows:
        f.write("\t".join(str(r.get(c)) for c in cols) + "\n")

# determinism: are the 3 reps of each cell identical?
print("=== DETERMINISM CHECK (3 reps per cell) ===")
cells = {}
for r in rows:
    cells.setdefault((r["prompt"], r["effort"]), []).append(r)
n_ident = 0
for k, v in sorted(cells.items()):
    texts = {(x["response"]["choices"][0]["message"].get("content"),
              x["response"]["choices"][0]["message"].get("reasoning_content"))
             for x in v if isinstance(x.get("response"), dict)}
    ident = len(texts) == 1
    n_ident += ident
    print(f"  {k[0]:10s} {k[1]:7s} reps={len(v)} byte_identical={ident}")
print(f"  -> {n_ident}/{len(cells)} cells byte-identical across all reps")

print()
print("=== GRID (rep 1 shown; all reps identical where flagged above) ===")
print(f"{'prompt':11s} {'effort':7s} {'ptok':>5s} {'rtok':>5s} {'vtok':>5s} {'ctok':>5s} "
      f"{'rchar':>6s} {'vchar':>6s} {'finish':>7s}")
order = {"xhigh": 0, "medium": 1, "low": 2, "absent": 3}
for k in sorted(cells, key=lambda x: (x[0], order.get(x[1], 9))):
    r = cells[k][0]
    print(f"{k[0]:11s} {k[1]:7s} {r['prompt_tokens']:>5} {r['reasoning_tokens']:>5} "
          f"{r['visible_tokens']:>5} {r['completion_tokens']:>5} {r['reasoning_chars']:>6} "
          f"{r['visible_chars']:>6} {str(r['finish_reason']):>7s}")

print()
print("=== xhigh vs absent identity check (E1) ===")
for pname in sorted({r["prompt"] for r in rows}):
    a = cells.get((pname, "xhigh"), [None])[0]
    b = cells.get((pname, "absent"), [None])[0]
    if a and b:
        same_p = a["prompt_tokens"] == b["prompt_tokens"]
        same_r = a["reasoning_tokens"] == b["reasoning_tokens"]
        same_txt = (a["response"]["choices"][0]["message"].get("content") ==
                    b["response"]["choices"][0]["message"].get("content"))
        print(f"  {pname:11s} ptok_same={same_p} rtok_same={same_r} visible_identical={same_txt}")

print()
print("=== reasoning-token spend ordering per prompt ===")
for pname in sorted({r["prompt"] for r in rows}):
    vals = {e: cells[(pname, e)][0]["reasoning_tokens"] for e in EF
            if (pname, e) in cells} if False else {
        e: cells[(pname, e)][0]["reasoning_tokens"]
        for e in ["xhigh", "medium", "low", "absent"] if (pname, e) in cells}
    ranked = sorted(vals.items(), key=lambda kv: -kv[1])
    mono = vals.get("xhigh", 0) > vals.get("medium", 0) > vals.get("low", 0)
    print(f"  {pname:11s} {vals}  ordered_xhigh>medium>low={mono}  "
          f"ranked={' > '.join(f'{k}({v})' for k, v in ranked)}")
