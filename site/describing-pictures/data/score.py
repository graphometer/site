#!/usr/bin/env python3
"""Score bake-off results against ground_truth.json (objective part only).

For every result file: how many of each picture's expected strings the
description actually contains (case-insensitive, whitespace- and
punctuation-tolerant), plus timing. Quality beyond string recall is judged
separately by reading the descriptions against the pictures.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
truth = json.loads((HERE / "ground_truth.json").read_text())


def norm(s):
    s = s.lower().replace("£", "").replace("$", "").replace(",", "")
    return re.sub(r"\s+", " ", s)


def recall(text, expected):
    t = norm(text)
    hit = [e for e in expected if norm(e) in t]
    return hit, [e for e in expected if e not in hit]


labels = sys.argv[1:] or sorted(p.stem for p in (HERE / "results").glob("*.json"))
rows = []
for label in labels:
    path = HERE / "results" / f"{label}.json"
    if not path.exists():
        continue
    data = json.loads(path.read_text())
    got = need = 0
    warm, cold, errs, late = [], None, 0, 0
    misses = {}
    for r in data["runs"]:
        if "error" in r:
            errs += 1
            continue
        if r.get("cold"):
            cold = r["wall_s"]
        else:
            warm.append(r["wall_s"])
        if not r.get("within_tool_deadline", True):
            late += 1
        exp = truth.get(r["file"], {}).get("expect", [])
        h, m = recall(r.get("text", ""), exp)
        got += len(h)
        need += len(exp)
        if m:
            misses[r["file"]] = m
    warm.sort()
    rows.append((label, cold, warm[len(warm) // 2] if warm else None, max(warm) if warm else None,
                 got, need, errs, late, misses))

print(f"{'config':34s} {'cold s':>7s} {'warm med':>9s} {'warm max':>9s} {'strings':>9s} {'err':>4s} {'>150s':>6s}")
for label, cold, med, mx, got, need, errs, late, misses in rows:
    print(f"{label:34s} {cold if cold is not None else '-':>7} {med if med is not None else '-':>9} "
          f"{mx if mx is not None else '-':>9} {str(got)+'/'+str(need):>9s} {errs:>4d} {late:>6d}")
if "-v" in sys.argv or len(labels) <= 3:
    for label, *_rest, misses in rows:
        for f, m in misses.items():
            print(f"   {label}: {f} missed {m}")
