#!/usr/bin/env python3
"""ling_ledger_stress.py: the TRIGGER family: highly repetitive ledger text (the batch-sweep body that
crashed ling at 3,007 tokens), many seeds and lengths, one server, restart after each crash.
Same exec flags as ling_crash_diag.sh. Real mixed text (ling_stress.py, 60 prompts) did not crash
at ub 4096; this asks whether repetitive input does, and whether ub 2048 avoids it.

    ling_ledger_stress.py <ubatch> <n_prompts> <seed>
"""
import json, os, random, signal, subprocess, sys, time, urllib.request
from pathlib import Path

UB, N, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
OUT = Path(f"<OUTPUT_DIR>/logs/ledger_ub{UB}_s{SEED}")
OUT.mkdir(parents=True, exist_ok=True)
BIN = "<llama.cpp build d3146f2b5>/llama-server"
MODEL = "<MODEL_DIR>/Ling-3.0-flash/Ling-3.0-flash-Q4_K_M/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf"
ENV = dict(os.environ, LD_LIBRARY_PATH="<llama.cpp build d3146f2b5>:<CUDA 12.8 libraries>")
BASE = "http://127.0.0.1:8188"
master = random.Random(SEED)

def start():
    log = open(OUT / "server.log", "a")
    p = subprocess.Popen([BIN, "--model", MODEL, "--host", "127.0.0.1", "--port", "8188", "--alias", "ling-3.0-flash",
        "--jinja", "--ctx-size", "262144", "--parallel", "1", "--batch-size", str(max(UB, 4096)), "--ubatch-size", str(UB),
        "--n-gpu-layers", "999", "-cmoe", "--fit", "off", "--threads", "24", "--threads-batch", "24",
        "--flash-attn", "auto", "--cors-origins", "localhost", "--timeout", "3600", "--top-p", "0.95", "--top-k", "20"],
        stdout=log, stderr=subprocess.STDOUT, env=ENV)
    for _ in range(200):
        time.sleep(2)
        if p.poll() is not None: sys.exit("server died on load")
        try:
            if b"ok" in urllib.request.urlopen(BASE + "/health", timeout=3).read(): return p
        except Exception: pass
    sys.exit("server never healthy")

def post(path, obj, timeout):
    r = urllib.request.Request(BASE + path, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))

T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]
def ledger(seed, n):
    rng = random.Random(seed)
    ls = [(f"ENTRY {i:05d}. the {rng.choice(T)} was recorded by the reeve; reserve "
           f"{rng.randint(3,400)} units against {rng.randint(3,400)}.") for i in range(1, n + 1)]
    ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is AMBER-3172-WILLOW. Quote it in full."
    return "\n".join(ls) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."

srv = start()
crashes = 0; t0 = time.time()
with open(OUT / "results.jsonl", "a") as res:
    for i in range(N):
        seed = master.randrange(10**9); lines = master.randint(60, 190)   # ~2,000-5,700 tokens
        q = ledger(seed, lines)
        rec = {"i": i, "seed": seed, "lines": lines}
        try:
            d = post("/v1/chat/completions", {"messages": [{"role": "user", "content": q}], "max_tokens": 32,
                                              "temperature": 0.0, "stream": False}, 1800)
            rec.update(ok=True, prompt_n=d.get("timings", {}).get("prompt_n"))
        except Exception as e:
            time.sleep(2)
            log = (OUT / "server.log").read_text(errors="replace")[-20000:]
            rec.update(ok=False, err=type(e).__name__, illegal="illegal memory access" in log)
            crashes += 1; print(f"#{i} seed={seed} lines={lines} CRASH illegal={rec['illegal']}", flush=True)
            if srv.poll() is None: srv.send_signal(signal.SIGTERM); srv.wait(30)
            (OUT / "server.log").rename(OUT / f"server_crash_{i}.log"); srv = start()
        res.write(json.dumps(rec) + "\n"); res.flush()
srv.send_signal(signal.SIGTERM)
try: srv.wait(30)
except Exception: srv.kill()
s = {"ubatch": UB, "seed": SEED, "prompts": N, "crashes": crashes, "minutes": round((time.time() - t0) / 60, 1)}
(OUT / "SUMMARY.json").write_text(json.dumps(s)); print("SUMMARY", json.dumps(s), flush=True)
