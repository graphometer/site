#!/usr/bin/env python3
"""deep_recall_probe.py — build a deep three-code recall request sized for ONE running llama-server.

A synthetic field ledger (the 2026-09-12 context sweep's format, with unique numbers on every line)
carries three sealed reference numbers at ~5 %, ~50 % and ~95 % of its depth. The entry count is
fitted to --target tokens using the server's own /tokenize endpoint, so every body is measured with
its own tokenizer. Writes the chat-completions request JSON to --out and prints one JSON line of
metadata (entries, tokens, codes).

Usage:
  deep_recall_probe.py --server http://<LOCAL> --target 230000 --out req.json \
      [--kwargs '{"enable_thinking": false}'] [--max-tokens 160]
"""
import argparse
import json
import random
import urllib.request

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
QUESTION = ("\n\nQUESTION: Three sealed reference numbers are recorded in this ledger. Quote all three "
            "exactly as written, in the order they appear, separated by single spaces. Answer with the "
            "three reference numbers only.")


def entry(i, rng):
    return (f"ENTRY {i:05d}. On the {rng.randint(1, 28)}th day of the {rng.randint(1, 12)}th month, the "
            f"{rng.choice(TASKS)} was {rng.choice(VERBS)} by the {rng.choice(ROLES)}, who noted that the "
            f"weather had been {rng.choice(WEATHER)} for {rng.randint(2, 30)} consecutive days and that the "
            f"reserve of {rng.choice(MATS)} stood at {rng.randint(3, 400)} units against an expected "
            f"requirement of {rng.randint(3, 400)}. The margin was judged {rng.choice(JUDGE)}, and a further "
            f"inspection was set for the following {rng.choice(PERIOD)}.")


def build(n, seed=20260915):
    rng = random.Random(seed)
    marks = {max(2, round(n * 0.05)): 0, round(n * 0.50): 1, min(n - 1, round(n * 0.95)): 2}
    lines = ["FIELD LEDGER — NORTHFIELD HOLDING — TRANSCRIPTION FOR ARCHIVE", ""]
    for i in range(1, n + 1):
        if i in marks:
            k = marks[i]
            lines.append(f"ENTRY {i:05d}. SEALED REFERENCE {k + 1} OF 3 for this ledger is {CODES[k]}. "
                         f"Any clerk verifying this volume must quote it in full.")
        else:
            lines.append(entry(i, rng))
    return "\n".join(lines)


def ntok(server, text):
    req = urllib.request.Request(server.rstrip("/") + "/tokenize",
                                 data=json.dumps({"content": text}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return len(json.load(r)["tokens"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--server", required=True)
    ap.add_argument("--target", type=int, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--kwargs", default="")
    ap.add_argument("--max-tokens", type=int, default=160)
    a = ap.parse_args()

    per_entry = ntok(a.server, build(400)) / 400
    n = max(60, int(a.target / per_entry))
    tokens = ntok(a.server, build(n) + QUESTION)
    for _ in range(4):
        if abs(tokens - a.target) / a.target < 0.01:
            break
        n = max(60, int(n * a.target / tokens))
        tokens = ntok(a.server, build(n) + QUESTION)

    req = {"messages": [{"role": "user", "content": build(n) + QUESTION}],
           "max_tokens": a.max_tokens, "temperature": 0.0, "stream": False}
    if a.kwargs and a.kwargs != "-":
        req["chat_template_kwargs"] = json.loads(a.kwargs)
    with open(a.out, "w") as f:
        json.dump(req, f)
    print(json.dumps({"entries": n, "tokens": tokens, "codes": CODES}))


if __name__ == "__main__":
    main()
