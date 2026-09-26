#!/usr/bin/env python3
"""Long-context recall probe: plant three codes at 5% / 50% / 95% depth and ask for them back.

This is the test that says whether a stretched context is *usable*, not merely *accepted*.
A model will happily run at 128K and quietly lose the middle; the 50% code is the one that
catches that.

Usage: recall_probe.py BASE_URL LABEL [target_tokens] [out_md]
"""
import json
import re
import sys
import time
import urllib.request

BASE = sys.argv[1]
LABEL = sys.argv[2]
TARGET = int(sys.argv[3]) if len(sys.argv) > 3 else 60000
OUT = sys.argv[4] if len(sys.argv) > 4 else None

CODES = {"5%": "ALPHA-7731", "50%": "MERIDIAN-4408", "95%": "COTTAGE-9152"}

# Filler that is bland but not repetitive enough to be trivially compressed.
SENT = ("The archivist walked the long corridor of the memory house, noting each room and the "
        "small light that marked a life still tended, and made a note of the date. ")
# ~34 tokens per sentence; aim a little over target, we measure the real count from the server.
n_sent = max(1, TARGET // 30)


def build():
    parts = []
    marks = {}
    for i in range(n_sent):
        frac = i / n_sent
        for depth, code in CODES.items():
            d = float(depth.rstrip("%")) / 100.0
            if depth not in marks and frac >= d:
                parts.append(f"\n\n>>> REMEMBER THIS: the {depth} codeword is {code}. <<<\n\n")
                marks[depth] = True
        parts.append(SENT)
    return "".join(parts)


body = build()
question = ("\n\nYou have just read a long document with three codewords planted in it.\n"
            "Repeat all three codewords exactly, one per line, in this format and nothing else:\n"
            "5% = <code>\n50% = <code>\n95% = <code>")

payload = {"messages": [{"role": "user", "content": body + question}],
           "max_tokens": 200, "temperature": 0.0}

req = urllib.request.Request(BASE + "/v1/chat/completions",
                             data=json.dumps(payload).encode(),
                             headers={"Content-Type": "application/json"})
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=3600) as r:
        d = json.load(r)
except Exception as e:
    print(f"{LABEL} recall: ERROR {e}")
    sys.exit(1)
wall = time.time() - t0

msg = d["choices"][0]["message"]
content = (msg.get("content") or "").strip()
u = d.get("usage", {})
ptok = u.get("prompt_tokens", 0)

found = {k: (v in content) for k, v in CODES.items()}
score = sum(found.values())

print(f"\n=== {LABEL} · recall at {ptok:,d} prompt tokens ===")
print(f"wall {wall:.1f}s · completion_tokens {u.get('completion_tokens')}")
for k, v in CODES.items():
    print(f"  {k:4s} {v:15s} {'FOUND' if found[k] else 'MISSING'}")
print(f"SCORE: {score}/3")
print("--- model's answer ---")
print(content[:600])

if OUT:
    with open(OUT, "a") as f:
        f.write(f"\n### {LABEL} - long-context recall\n")
        f.write(f"- prompt **{ptok:,d} tokens** · wall {wall:.1f}s · "
                f"**{score}/3** codes recalled "
                f"({', '.join(k for k in CODES if found[k]) or 'none'})\n")
        f.write(f"- answer: `{content[:200].replace(chr(10), ' / ')}`\n")
sys.exit(0 if score == 3 else 2)
