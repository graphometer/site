#!/usr/bin/env python3
"""stress_model.py: crash-hunt one roster model at a given batch setting, THROUGH ITS OWN start script.

Why: on 2026-09-21 ling's shipped -ub 4096 crashed the server (CUDA illegal memory access) on one
specific 3,007-token input while passing every other probe: a single sealed-code read cannot see a
rare input-specific crash. This sends N prompts of real mixed text (llama.cpp's own C/C++ sources and
markdown docs; public code, no private data), lengths mostly in the one-to-two-ubatch regime,
restarts the model through its start script after any crash, and saves each crashing prompt.

    stress_model.py <dir-under-gguf> <PFX> <port> <ubatch|skip> <n_prompts> <seed> [script args...]
"""
import json, os, random, signal, subprocess, sys, time, urllib.request
from pathlib import Path

DIR, PFX, PORT, UBS, N, SEED = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
SARGS = sys.argv[7:]
SCRIPT = f"<MODEL_DIR>/{DIR}/start_server.sh"
OUT = Path(f"<OUTPUT_DIR>/logs/stress_{DIR}_{UBS}_s{SEED}")
OUT.mkdir(parents=True, exist_ok=True)
env = dict(os.environ)
if UBS != "skip":
    env[f"{PFX}_UBATCH"] = UBS; env[f"{PFX}_BATCH"] = str(max(int(UBS), 4096))
UB = int(UBS) if UBS != "skip" else None
# [a block configuring a private companion process was removed from this copy; it does not touch the measurement]

if subprocess.run(["pgrep", "-x", "llama-server"], capture_output=True).returncode == 0:
    sys.exit("REFUSED: a llama-server is already running")

files = [p for ext in ("*.cpp", "*.h", "*.cu", "*.md", "*.py")
         for p in Path("<llama.cpp source tree at d3146f2b5>").rglob(ext)
         if p.stat().st_size > 4000 and "/build" not in str(p)]
rng = random.Random(SEED); rng.shuffle(files)
BASE = None

def health(host):
    try: return b"ok" in urllib.request.urlopen(f"http://{host}:{PORT}/health", timeout=3).read()
    except Exception: return False

def start():
    global BASE
    log = open(OUT / "server.log", "a")
    p = subprocess.Popen(["bash", SCRIPT, *SARGS], stdout=log, stderr=subprocess.STDOUT, env=env, start_new_session=True)
    for _ in range(600):
        time.sleep(2)
        if p.poll() is not None: sys.exit("server died on load: see server.log")
        for h in ("127.0.0.1", "<LOCAL>"):
            if health(h): BASE = f"http://{h}:{PORT}"; return p
    sys.exit("server never healthy")

def stop(p):
    try: os.killpg(p.pid, signal.SIGTERM)
    except Exception: pass
    try: p.wait(40)
    except Exception:
        try: os.killpg(p.pid, signal.SIGKILL)
        except Exception: pass
    subprocess.run(["pkill", "-x", "llama-server"]); time.sleep(4)

def post(path, obj, timeout):
    r = urllib.request.Request(BASE + path, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))

def make_prompt(target):
    parts, total = [], 0
    while total < target * 5:
        f = files[rng.randrange(len(files))]
        t = f.read_text(errors="replace"); a = rng.randrange(max(1, len(t) - 3000))
        parts.append(f"\n\n=== {f.name} ===\n" + t[a:a + rng.randint(1500, 9000)])
        total = sum(len(x) for x in parts)
    toks = post("/tokenize", {"content": "".join(parts)}, 300)["tokens"][:target]
    return post("/detokenize", {"tokens": toks}, 300)["content"]

def pick_len():
    ub = UB or 512
    u = rng.random()
    if u < 0.55: return rng.randint(max(300, ub // 2), ub + 64)          # one ubatch
    if u < 0.85: return rng.randint(ub + 65, 2 * ub + 600)               # two ubatches, remainder varies
    return rng.randint(300, 12000)

srv = start()
crashes, done, t0 = 0, 0, time.time()
with open(OUT / "results.jsonl", "a") as res:
    for i in range(N):
        L = pick_len()
        try: prompt = make_prompt(L)
        except Exception as e:
            print(f"#{i} tokenize failed ({e}): counting as crash", flush=True); L = -1; prompt = None
        rec = {"i": i, "target": L}
        try:
            if prompt is None: raise RuntimeError("tokenize failed")
            q = prompt + "\n\nIn one short sentence: what is the text above mostly about?"
            d = post("/v1/chat/completions", {"messages": [{"role": "user", "content": q}],
                     "max_tokens": 32, "temperature": 0.0, "stream": False}, 1800)
            ti = d.get("timings", {})
            rec.update(ok=True, prompt_n=ti.get("prompt_n"), prefill=round(ti.get("prompt_per_second", 0) or 0, 1))
        except Exception as e:
            time.sleep(3)
            log = (OUT / "server.log").read_text(errors="replace")[-30000:]
            rec.update(ok=False, err=type(e).__name__, illegal="illegal memory access" in log,
                       oom="out of memory" in log.lower())
            if prompt is not None: (OUT / f"crash_{i}_prompt.txt").write_text(q)
            crashes += 1
            print(f"#{i} target={L} CRASH illegal={rec['illegal']} oom={rec['oom']}", flush=True)
            stop(srv); (OUT / "server.log").rename(OUT / f"server_crash_{i}.log"); srv = start()
        done += 1; res.write(json.dumps(rec) + "\n"); res.flush()
stop(srv)
summary = {"model": DIR, "ubatch": UBS, "seed": SEED, "prompts": done, "crashes": crashes,
           "minutes": round((time.time() - t0) / 60, 1)}
(OUT / "SUMMARY.json").write_text(json.dumps(summary)); print("SUMMARY", json.dumps(summary), flush=True)
