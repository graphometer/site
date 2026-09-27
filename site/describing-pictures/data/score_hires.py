#!/usr/bin/env python3
"""Count the codes of the 4K small-text screenshot found in each recorded description.

score.py has no expected strings for this picture, so this script scores it against
hires_truth.json with score.py's own rule (lower case, pound and dollar signs and commas
removed, runs of whitespace collapsed, then a plain substring test).

For each code not found, it shows what the description wrote in that code's place. The
screenshot lists "Item 1" to "Item 6" under each of four headings, and every recorded
description contains one complete listing of all 24 items in that order (some repeat a
few items elsewhere, in a summary); the script takes the first complete listing and
compares it position by position.
Written 26 September 2026 for the page; reads files only.

  python3 score_hires.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
truth = json.loads((HERE / "hires_truth.json").read_text())
RUNS = (("hires_30b_hires", "none"), ("hires_30b_hires_2560", "2560"),
        ("hires_30b_hires_2048", "2048"), ("hires_30b_hires_1536", "1536"))
SIZES = ("28", "20", "16", "13")
ORDER = [(k, c) for k in SIZES for c in truth[k]]
ITEM = re.compile(r"Item\s*(\d)\s*:\s*\**\s*([A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+)")


def norm(s):
    s = s.lower().replace("£", "").replace("$", "").replace(",", "")
    return re.sub(r"\s+", " ", s)


def full_listing(text):
    items = ITEM.findall(text)
    want = [str(i) for i in range(1, 7)] * 4
    for start in range(len(items) - 23):
        if [n for n, _ in items[start:start + 24]] == want:
            return [c for _, c in items[start:start + 24]]
    return None


print(f"{'run':24s} {'cap':>5s} {'prompt tok':>10s} {'wall s':>7s} "
      + " ".join(f"{k + ' px':>6s}" for k in SIZES) + "  total")
notes = []
for label, cap in RUNS:
    r = json.loads((HERE / "results" / f"{label}.json").read_text())["runs"][0]
    text = r.get("text", "")
    t = norm(text)
    per = {k: sum(1 for c in truth[k] if norm(c) in t) for k in SIZES}
    print(f"{label:24s} {cap:>5s} {r['prompt_tokens']:>10d} {r['wall_s']:>7.2f} "
          + " ".join(f"{str(per[k]) + '/6':>6s}" for k in SIZES) + f"  {sum(per.values())}/24")
    listing = full_listing(text)
    for i, (k, c) in enumerate(ORDER):
        if norm(c) not in t:
            written = listing[i] if listing else "(no complete listing found)"
            notes.append(f"{label}: {k} px, item {i % 6 + 1}: expected {c}, written {written}")

print()
print("\n".join(notes) if notes else "every code found")
