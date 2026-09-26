#!/usr/bin/env python3
"""Synthetic ledger probe; operational introduction withheld."""
import json, random, sys, time, urllib.request

BASE, MAXT, SIZES = sys.argv[1].rstrip("/"), int(sys.argv[2]), [int(x) for x in sys.argv[3:]]
CODE = "AMBER-3172-WILLOW"
T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]

def post(path, obj, timeout):
    r = urllib.request.Request(BASE + path, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))

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
        if abs(t - target) / target < 0.02: break
        n = max(50, int(n * target / t))
    q = body(n) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
    t0 = time.time()
    try:
        d = post("/v1/chat/completions", {"messages": [{"role": "user", "content": q}], "max_tokens": MAXT,
                                          "temperature": 0.0, "stream": False}, 7200)
    except Exception as e:
        print(json.dumps({"size": target, "error": f"{type(e).__name__}: {e}", "wall_s": round(time.time() - t0, 1)}), flush=True)
        continue
    m = d["choices"][0]["message"]; c = (m.get("content") or "").strip(); rsn = (m.get("reasoning_content") or "").strip()
    ti = d.get("timings", {})
    print(json.dumps({"size": target, "prompt_n": ti.get("prompt_n"), "prefill_tps": round(ti.get("prompt_per_second", 0) or 0, 1),
                      "decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2), "needle_in_answer": CODE in c,
                      "needle_found": CODE in (c + " " + rsn), "answer_head": c[:60], "wall_s": round(time.time() - t0, 1)}), flush=True)
