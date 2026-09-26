#!/usr/bin/env python3
"""z13_probe.py  -  per size: a COLD sealed-code read, then a WARM follow-up on the same ledger.

Same ledger body and sealed code as models/batch_sweep.sh and needle_probe.py (lines "ENTRY nnnnn. ...",
code AMBER-3172-WILLOW at 50% depth, seed 20260920 + k, so no size shares a prefix with the one before).

  cold  ledger + "quote the sealed reference" (max_tokens as given, >= 900 for thinkers): reading speed,
        time to the answer, and whether the code came back exactly.
  warm  the SAME ledger + a different question asking for ~200 words, sent right after. The server can
        reuse the cached ledger, so this is a user next turn: warm_prompt_n / warm_read_s is what it
        had to re-read (on hybrid models that may be far more than the new question), warm_decode_tps
        is speaking at that depth over a few hundred tokens instead of a ten-token code.

    z13_probe.py <base_url> <max_tokens> <size> [<size> ...]
"""
import json, random, sys, time, urllib.request

BASE, MAXT, SIZES = sys.argv[1].rstrip("/"), int(sys.argv[2]), [int(x) for x in sys.argv[3:]]
WARM_MAXT = 400
CODE = "AMBER-3172-WILLOW"
T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]
Q_COLD = "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
Q_WARM = ("\n\nQUESTION: in about 200 words, describe what kinds of work this ledger records and how "
          "its entries are laid out. Do not quote the sealed reference.")


def post(path, obj, timeout):
    r = urllib.request.Request(BASE + path, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))


def ask(text, maxt):
    t0 = time.time()
    d = post("/v1/chat/completions", {"messages": [{"role": "user", "content": text}], "max_tokens": maxt,
                                      "temperature": 0.0, "stream": False}, 7200)
    m = d["choices"][0]["message"]
    return d.get("timings", {}), (m.get("content") or "").strip(), (m.get("reasoning_content") or "").strip(), time.time() - t0


for k, target in enumerate(SIZES, 1):
    rng = random.Random(20260920 + k)

    def line(i):
        return (f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve; reserve "
                f"{rng.randint(3,400)} units against {rng.randint(3,400)}.")

    def body(n):
        ls = [line(i) for i in range(1, n + 1)]
        ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
        return "\n".join(ls)

    ntok = lambda t: len(post("/tokenize", {"content": t}, 900)["tokens"])
    per = ntok(body(200)) / 200
    n = max(50, int(target / per))
    for _ in range(3):
        t = ntok(body(n))
        if abs(t - target) / target < 0.02:
            break
        n = max(50, int(n * target / t))
    # the body is built ONCE: rng is consumed by body(), so both questions must share this exact text
    ledger = body(n)
    out = {"size": target}
    try:
        ti, c, rsn, wall = ask(ledger + Q_COLD, MAXT)
        out.update({"prompt_n": ti.get("prompt_n"), "read_s": round((ti.get("prompt_ms") or 0) / 1000, 1),
                    "prefill_tps": round(ti.get("prompt_per_second", 0) or 0, 1),
                    "decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2), "gen_n": ti.get("predicted_n"),
                    "needle_in_answer": CODE in c, "needle_found": CODE in (c + " " + rsn),
                    "answer_head": c[:60], "wall_s": round(wall, 1)})
    except Exception as e:
        out.update({"error": f"cold {type(e).__name__}: {e}"})
        print(json.dumps(out), flush=True)
        continue
    try:
        ti, c, rsn, wall = ask(ledger + Q_WARM, WARM_MAXT)
        out.update({"warm_prompt_n": ti.get("prompt_n"), "warm_read_s": round((ti.get("prompt_ms") or 0) / 1000, 1),
                    "warm_decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2),
                    "warm_gen_n": ti.get("predicted_n"), "warm_words": len(c.split()),
                    "warm_leaked_code": CODE in c, "warm_wall_s": round(wall, 1)})
    except Exception as e:
        out.update({"warm_error": f"{type(e).__name__}: {e}"})
    print(json.dumps(out), flush=True)
