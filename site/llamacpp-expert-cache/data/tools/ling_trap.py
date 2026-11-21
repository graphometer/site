#!/usr/bin/env python3
"""Ling's known killer on a running server: the exact 3,007-token ledger prompt (batch sweep, seed 20260920) that took the server down on an older build at -ub 4096, then 40 prompts of the same family.
Rebuilt the way <REDACTED_PATH>/ling_crash_diag.sh and ling_ledger_stress.py build them. A dead server or a wrong code is a failure. usage: ling_trap.py URL LABEL"""
import json, random, sys, time, urllib.request
BASE, L = sys.argv[1], sys.argv[2]
def post(path, obj, timeout):
    r = urllib.request.Request(BASE + path, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))
target = 3000; rng = random.Random(20260920); CODE = "AMBER-3172-WILLOW"
T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]
def line(i):
    return (f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve; reserve "
            f"{rng.randint(3,400)} units against {rng.randint(3,400)}.")
def body(n):
    ls = [line(i) for i in range(1, n + 1)]
    ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls)
def ntok(t):
    return len(post("/tokenize", {"content": t}, 900)["tokens"])
per = ntok(body(200)) / 200
n = max(50, int(target / per))
for _ in range(3):
    t = ntok(body(n))
    if abs(t - target) / target < 0.02: break
    n = max(50, int(n * target / t))
q = body(n) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
try:
    d = post("/v1/chat/completions", {"messages": [{"role": "user", "content": q}], "max_tokens": 900, "temperature": 0.0, "stream": False, "cache_prompt": False}, 3600)
    c = (d["choices"][0]["message"].get("content") or "").strip(); ti = d.get("timings", {})
    print(f"TRAP {L}: exact prompt prompt_n={ti.get('prompt_n')} read {round(ti.get('prompt_per_second', 0))} t/s code {'OK' if CODE in c else 'WRONG: ' + c[:80]}", flush=True)
except Exception as e:
    print(f"TRAP {L}: exact prompt NO ANSWER {type(e).__name__}", flush=True); sys.exit(1)
master = random.Random(4242); bad = 0; t0 = time.time(); N = 40
def ledger(seed, n):
    r = random.Random(seed)
    ls = [(f"ENTRY {i:05d}. the {r.choice(T)} was recorded by the reeve; reserve {r.randint(3,400)} units against {r.randint(3,400)}.") for i in range(1, n + 1)]
    ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."
for i in range(N):
    seed = master.randrange(10**9); lines = master.randint(60, 190)
    try:
        post("/v1/chat/completions", {"messages": [{"role": "user", "content": ledger(seed, lines)}], "max_tokens": 32, "temperature": 0.0, "stream": False, "cache_prompt": False}, 1800)
    except Exception as e:
        bad += 1; print(f"TRAP {L}: family prompt {i} seed {seed} lines {lines} NO ANSWER {type(e).__name__}", flush=True); break
print(f"TRAP {L}: family {N - bad} of {N} answered, {time.time() - t0:.0f} s", flush=True)
sys.exit(1 if bad else 0)
