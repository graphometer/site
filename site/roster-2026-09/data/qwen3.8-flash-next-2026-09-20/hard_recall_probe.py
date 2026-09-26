#!/usr/bin/env python3
"""hard_recall_probe.py — three graded questions over ONE long prompt, on one running llama-server.

Why this exists: the house's deep_recall_probe.py plants three sealed codes at 5/50/95 % and asks for
them back. Qwen's own tech report says single-fact retrieval (RULER) on this architecture stays above
93 all the way to a million tokens while multi-needle reasoning (MRCR) falls 93 -> 40 -> 26 across
256K/512K/1M. So a three-code needle PASSES at a window where the model can no longer think, and
tells you nothing about reasoning across the window. This probe keeps the three-code question
verbatim for comparability with the 2026-09-15 record, and adds two harder layers over the same text.

The three questions share one prefix, so only Q1 pays the prefill; llama.cpp's prompt cache answers
Q2 and Q3 in seconds. One long read therefore yields three graded results.

  Q1 RETRIEVE  three sealed codes at 5/50/95 % depth            (the house question, verbatim)
  Q2 MULTI     eight AUDIT MARK tallies, letters A-H, evenly spread, against thousands of
               confusable "<n> units" numbers in the filler                 (MRCR-shaped)
  Q3 INTEGRATE which AUDIT MARK holds the largest tally, AND the task named in the entry
               immediately after it — a max across eight scattered needles, then a local read

Usage:
  hard_recall_probe.py --server http://<LOCAL> --target 230000 --out-dir ./q \
      [--kwargs '{"enable_thinking": false}'] [--seed 20260915]
Writes q1.json/q2.json/q3.json plus meta.json, and prints one JSON line of metadata.
"""
import argparse
import json
import random
import urllib.request

# --- the house ledger, byte-for-byte from deep_recall_probe.py (seed 20260915) -------------------
CODES = ["AMBER-3172-WILLOW", "COBALT-5821-FERN", "ONYX-9044-HAZEL"]
TASKS = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks",
         "repair of the east sluice", "survey of the lower orchard", "restocking of the grain loft",
         "clearing of the north ditch", "rebuilding of the sheep fold", "tarring of the boat shed",
         "lining of the well shaft", "pruning of the hedgerow", "recutting of the mill race"]
VERBS = ["postponed", "recorded", "deferred", "measured", "approved", "completed", "inspected", "revised"]
ROLES = ["under-steward", "reeve", "bailiff", "clerk of works", "head carter", "warden"]
WEATHER = ["dry", "close", "wet", "unsettled", "cold", "mild"]
MATS = ["lime", "hurdles", "sand", "tallow", "slate", "rope", "pitch", "nails", "straw", "flint"]
JUDGE = ["sufficient", "thin", "adequate", "generous", "doubtful"]
PERIOD = ["quarter", "fortnight", "month", "season", "week"]

MARKS = "ABCDEFGH"

Q1 = ("\n\nQUESTION: Three sealed reference numbers are recorded in this ledger. Quote all three "
      "exactly as written, in the order they appear, separated by single spaces. Answer with the "
      "three reference numbers only.")
Q2 = ("\n\nQUESTION: This ledger contains eight lines beginning 'AUDIT MARK'. For each one, report its "
      "letter and its certified tally. Answer with exactly eight lines, each of the form 'A=1234', in "
      "alphabetical order, and nothing else.")
Q3 = ("\n\nQUESTION: Among the eight AUDIT MARK lines in this ledger, find the one with the largest "
      "certified tally. Answer with exactly one line of the form 'LETTER=TALLY|TASK', where TASK is "
      "the task named in the very next ENTRY after that audit mark. Answer with that one line only.")


def entry(i, rng):
    return (f"ENTRY {i:05d}. On the {rng.randint(1, 28)}th day of the {rng.randint(1, 12)}th month, the "
            f"{rng.choice(TASKS)} was {rng.choice(VERBS)} by the {rng.choice(ROLES)}, who noted that the "
            f"weather had been {rng.choice(WEATHER)} for {rng.randint(2, 30)} consecutive days and that the "
            f"reserve of {rng.choice(MATS)} stood at {rng.randint(3, 400)} units against an expected "
            f"requirement of {rng.randint(3, 400)}. The margin was judged {rng.choice(JUDGE)}, and a further "
            f"inspection was set for the following {rng.choice(PERIOD)}.")


def plan(n, seed):
    """Deterministic placement + answer key, independent of how the text is rendered."""
    rng = random.Random(seed)
    codes = {max(2, round(n * 0.05)): 0, round(n * 0.50): 1, min(n - 1, round(n * 0.95)): 2}
    # eight audit marks evenly spread over 8%..92%, never colliding with a code line or the last entry
    audit, tallies = {}, {}
    trng = random.Random(seed + 1)
    picked = trng.sample(range(1000, 9999), 8)          # 4-digit, distinct, unambiguous maxima
    for k, letter in enumerate(MARKS):
        i = round(n * (0.08 + k * (0.84 / 7)))
        while i in codes or i in audit or i >= n:       # keep i+1 readable
            i += 1
        audit[i] = letter
        tallies[letter] = picked[k]
    return rng, codes, audit, tallies


def build(n, seed=20260915):
    """Render the ledger and, in the same pass, capture the answer key for Q3."""
    rng, codes, audit, tallies = plan(n, seed)
    lines = ["FIELD LEDGER — NORTHFIELD HOLDING — TRANSCRIPTION FOR ARCHIVE", ""]
    follow_task = {}
    pending = None
    for i in range(1, n + 1):
        if i in codes:
            k = codes[i]
            lines.append(f"ENTRY {i:05d}. SEALED REFERENCE {k + 1} OF 3 for this ledger is {CODES[k]}. "
                         f"Any clerk verifying this volume must quote it in full.")
            pending = None
        elif i in audit:
            letter = audit[i]
            lines.append(f"ENTRY {i:05d}. AUDIT MARK {letter}: the tally for this volume was "
                         f"{tallies[letter]} units, certified by the {rng.choice(ROLES)}.")
            pending = letter
        else:
            text = entry(i, rng)
            if pending is not None:
                # the task is the phrase between "the " and " was <verb>"
                seg = text.split(", the ", 1)[1].split(" was ", 1)[0]
                follow_task[pending] = seg
                pending = None
            lines.append(text)
    key = {"codes": CODES, "tallies": tallies, "follow_task": follow_task}
    top = max(tallies, key=lambda L: tallies[L])
    key["q3"] = {"letter": top, "tally": tallies[top], "task": follow_task.get(top)}
    return "\n".join(lines), key


def ntok(server, text):
    req = urllib.request.Request(server.rstrip("/") + "/tokenize",
                                 data=json.dumps({"content": text}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=1800) as r:
        return len(json.load(r)["tokens"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--server", required=True)
    ap.add_argument("--target", type=int, required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--kwargs", default="")
    ap.add_argument("--seed", type=int, default=20260915)
    a = ap.parse_args()

    per_entry = ntok(a.server, build(400, a.seed)[0]) / 400
    n = max(60, int(a.target / per_entry))
    body, key = build(n, a.seed)
    tokens = ntok(a.server, body + Q1)
    for _ in range(4):
        if abs(tokens - a.target) / a.target < 0.01:
            break
        n = max(60, int(n * a.target / tokens))
        body, key = build(n, a.seed)
        tokens = ntok(a.server, body + Q1)

    kw = json.loads(a.kwargs) if a.kwargs and a.kwargs != "-" else None
    for name, q, mx in (("q1", Q1, 160), ("q2", Q2, 400), ("q3", Q3, 200)):
        req = {"messages": [{"role": "user", "content": body + q}],
               "max_tokens": mx, "temperature": 0.0, "stream": False, "cache_prompt": True}
        if kw:
            req["chat_template_kwargs"] = kw
        with open(f"{a.out_dir}/{name}.json", "w") as f:
            json.dump(req, f)
    key["entries"] = n
    key["tokens"] = tokens
    with open(f"{a.out_dir}/meta.json", "w") as f:
        json.dump(key, f, indent=1)
    print(json.dumps({"entries": n, "tokens": tokens, "q3": key["q3"]}))


if __name__ == "__main__":
    main()
