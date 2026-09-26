#!/usr/bin/env python3
"""ling_stress.py: how often does ling's CUDA 'illegal memory access' fire at a given ubatch?

Runs the ling binary with the exact exec flags of <MODEL_DIR>/Ling-3.0-flash/start_server.sh (as in
ling_crash_diag.sh) on scratch port 8188, sends N prompts built from REAL mixed text (llama.cpp's own
C/C++ sources and markdown docs from the llama.cpp source tree at d3146f2b5: public code, no private data), lengths
drawn mostly from the single-ubatch regime, restarts the server after every crash, and saves each
crashing prompt so it can be replayed. Prefill is the suspect, so max_tokens is small (32): a
crash is a dropped connection plus 'illegal memory access' in the server log.

    ling_stress.py <ubatch> <n_prompts> <seed>
"""
import json, os, random, signal, subprocess, sys, time, urllib.request
from pathlib import Path

UB, N, SEED = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
OUT = Path(f"<OUTPUT_DIR>/logs/stress_ub{UB}_s{SEED}")
OUT.mkdir(parents=True, exist_ok=True)
BIN = "<llama.cpp build d3146f2b5>/llama-server"
MODEL = "<MODEL_DIR>/Ling-3.0-flash/Ling-3.0-flash-Q4_K_M/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf"
ENV = dict(os.environ, LD_LIBRARY_PATH="<llama.cpp build d3146f2b5>:<CUDA 12.8 libraries>")
BASE = "http://127.0.0.1:8188"

# corpus: real text, public code/docs only
roots = [Path("<llama.cpp source tree at d3146f2b5>")]
files = []
for r in roots:
    for ext in ("*.cpp", "*.h", "*.cu", "*.md", "*.py"):
        files += [p for p in r.rglob(ext) if p.stat().st_size > 4000 and "/build" not in str(p)]
rng = random.Random(SEED)
rng.shuffle(files)
if len(files) < 50:
    sys.exit(f"corpus too small: {len(files)} files")

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

def make_prompt(target):
    parts, total = [], 0
    while total < target * 5:            # ~chars; trimmed by tokens below
        f = files[rng.randrange(len(files))]
        t = f.read_text(errors="replace")
        a = rng.randrange(max(1, len(t) - 3000))
        parts.append(f"\n\n=== {f.name} ===\n" + t[a:a + rng.randint(1500, 9000)])
        total = sum(len(x) for x in parts)
    text = "".join(parts)
    toks = post("/tokenize", {"content": text}, 300)["tokens"]
    toks = toks[:target]
    return post("/detokenize", {"tokens": toks}, 300)["content"]

def pick_len():
    u = rng.random()
    if u < 0.70: return rng.randint(2049, 4600)      # the single-ubatch regime where the crash lives
    if u < 0.85: return rng.randint(300, 2048)
    return rng.randint(4600, 16000)

srv = start()
crashes, done, t0 = 0, 0, time.time()
with open(OUT / "results.jsonl", "a") as res:
    for i in range(N):
        L = pick_len()
        try:
            prompt = make_prompt(L)
        except Exception as e:
            print(f"#{i} tokenize failed: {e}"); break
        q = prompt + "\n\nIn one short sentence: what is the text above mostly about?"
        body = {"messages": [{"role": "user", "content": q}], "max_tokens": 32, "temperature": 0.0, "stream": False}
        rec = {"i": i, "target": L}
        try:
            d = post("/v1/chat/completions", body, 1800)
            ti = d.get("timings", {})
            rec.update(ok=True, prompt_n=ti.get("prompt_n"), prefill=round(ti.get("prompt_per_second", 0) or 0, 1))
        except Exception as e:
            time.sleep(2)
            crashed = srv.poll() is not None
            log = (OUT / "server.log").read_text(errors="replace")[-20000:]
            rec.update(ok=False, err=type(e).__name__, server_dead=crashed, illegal="illegal memory access" in log)
            (OUT / f"crash_{i}_prompt.txt").write_text(q)
            crashes += 1
            print(f"#{i} target={L} CRASH dead={crashed} illegal={rec['illegal']}", flush=True)
            if srv.poll() is None:
                srv.send_signal(signal.SIGTERM); srv.wait(30)
            (OUT / "server.log").rename(OUT / f"server_crash_{i}.log")
            srv = start()
        done += 1
        res.write(json.dumps(rec) + "\n"); res.flush()
srv.send_signal(signal.SIGTERM)
try: srv.wait(30)
except Exception: srv.kill()
summary = {"ubatch": UB, "seed": SEED, "prompts": done, "crashes": crashes, "minutes": round((time.time() - t0) / 60, 1)}
(OUT / "SUMMARY.json").write_text(json.dumps(summary))
print("SUMMARY", json.dumps(summary), flush=True)
