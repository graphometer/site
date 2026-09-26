#!/usr/bin/env python3
"""z13_stress.py  -  crash-hunt ONE model on the Z13 alone (Vulkan, llama.cpp d3146f2b5), 127.0.0.1:18200 only.

Port of the desktop's stress_model.py + stress_chain.sh (2026-09-21) for a machine with no start scripts:
  (1) a fresh load whose FIRST request is the exact prompt that crashed ling on the desktop card
      (repro_ling_crash.py: batch_sweep body, seed 20260920, 3,000 tokens, max_tokens 900), then
  (2) N prompts of real public text (this machine's llama.cpp sources, no private data), sized around one
      and two micro-batches, max_tokens 32; restart after any crash and save each crashing prompt.
Kills only the server it started.

    z13_stress.py <tag> <model.gguf> <ctx> <ubatch> <n_prompts> <seed> [extra llama-server args...]
"""
import json, os, random, signal, subprocess, sys, time, urllib.request
from pathlib import Path

TAG, MODEL, CTX, UB, N, SEED = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
EXTRA = sys.argv[7:]
D = Path("<REDACTED_PATH>/RUN_DIR")
OUT = D / f"stress_{TAG}"; OUT.mkdir(parents=True, exist_ok=True)
BIN = "<REDACTED_PATH>/llama-server"
PORT = 18200; BASE = f"http://127.0.0.1:{PORT}"
env = dict(os.environ); env["LD_LIBRARY_PATH"] = os.path.dirname(BIN) + (":" + env["LD_LIBRARY_PATH"] if env.get("LD_LIBRARY_PATH") else "")

if subprocess.run(["pgrep", "-x", "llama-server"], capture_output=True).returncode == 0:
    sys.exit("REFUSED: a llama-server is already running")

SRC = Path("<REDACTED_PATH>/llama.cpp-d3146f2b5")


def usable(p):
    rel = p.relative_to(SRC).as_posix()
    return p.stat().st_size > 4000 and not rel.startswith("build") and "/build" not in rel


files = sorted(p for ext in ("*.cpp", "*.h", "*.md", "*.py") for p in SRC.rglob(ext) if usable(p))
rng = random.Random(SEED); rng.shuffle(files)
starts = 0


def health():
    try: return b"ok" in urllib.request.urlopen(BASE + "/health", timeout=3).read()
    except Exception: return False


def start():
    global starts
    starts += 1
    log = open(OUT / "server.log", "a")
    p = subprocess.Popen([BIN, "--model", MODEL, "--host", "127.0.0.1", "--port", str(PORT), "--jinja",
                          "--ctx-size", str(CTX), "--parallel", "1", "-ngl", "999", "-fa", "on",
                          "-b", str(max(2048, UB)), "-ub", str(UB), "-t", "16", "--timeout", "3600", *EXTRA],
                         stdout=log, stderr=subprocess.STDOUT, env=env, start_new_session=True)
    for _ in range(750):
        time.sleep(2)
        if p.poll() is not None: sys.exit(f"server died on load  -  see {OUT}/server.log")
        if health(): return p
    stop(p); sys.exit("server never healthy in 25 min")


def stop(p):
    try: os.killpg(p.pid, signal.SIGTERM)
    except Exception: pass
    try: p.wait(40)
    except Exception:
        try: os.killpg(p.pid, signal.SIGKILL)
        except Exception: pass
    time.sleep(3)


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
    u = rng.random()
    if u < 0.55: return rng.randint(max(300, UB // 2), UB + 64)          # one ubatch
    if u < 0.85: return rng.randint(UB + 65, 2 * UB + 600)               # two ubatches, remainder varies
    return rng.randint(300, 12000)


t0 = time.time()
srv = start()
# (1) the exact replay, first request after a fresh load
rp = subprocess.run([sys.executable, str(D / "repro_ling_crash.py"), BASE], capture_output=True, text=True, timeout=7200)
alive = srv.poll() is None and health()
replay = {"exit": rp.returncode, "server_alive_after": alive, "out": (rp.stdout or rp.stderr).strip()[-300:]}
print("REPLAY", json.dumps(replay), flush=True)
if not alive:
    stop(srv); (OUT / "server.log").rename(OUT / "server_crash_replay.log"); srv = start()

# (2) N real-text prompts
crashes, done = 0 if alive else 1, 0
with open(OUT / "results.jsonl", "a") as res:
    for i in range(N):
        L = pick_len()
        try: prompt = make_prompt(L)
        except Exception as e:
            print(f"#{i} tokenize failed ({e})  -  counting as crash", flush=True); prompt = None
        rec = {"i": i, "target": L}
        q = None
        try:
            if prompt is None: raise RuntimeError("tokenize failed")
            q = prompt + "\n\nIn one short sentence: what is the text above mostly about?"
            d = post("/v1/chat/completions", {"messages": [{"role": "user", "content": q}],
                     "max_tokens": 32, "temperature": 0.0, "stream": False}, 1800)
            ti = d.get("timings", {})
            rec.update(ok=True, prompt_n=ti.get("prompt_n"), prefill=round(ti.get("prompt_per_second", 0) or 0, 1))
            if srv.poll() is not None: raise RuntimeError("server exited after answering")
        except Exception as e:
            time.sleep(3)
            log = (OUT / "server.log").read_text(errors="replace")[-20000:]
            rec.update(ok=False, err=f"{type(e).__name__}: {e}"[:200],
                       device_lost=("DeviceLost" in log or "device lost" in log.lower()),
                       oom=("out of memory" in log.lower() or "ErrorOutOf" in log))
            if q is not None: (OUT / f"crash_{i}_prompt.txt").write_text(q)
            crashes += 1
            print(f"#{i} target={L} CRASH {rec['err']} device_lost={rec['device_lost']} oom={rec['oom']}", flush=True)
            stop(srv); (OUT / "server.log").rename(OUT / f"server_crash_{i}.log"); srv = start()
        done += 1; res.write(json.dumps(rec) + "\n"); res.flush()
stop(srv)
summary = {"tag": TAG, "ubatch": UB, "ctx": CTX, "seed": SEED, "replay_alive": alive, "prompts": done,
           "crashes": crashes, "server_starts": starts, "minutes": round((time.time() - t0) / 60, 1)}
(OUT / "SUMMARY.json").write_text(json.dumps(summary)); print("SUMMARY", json.dumps(summary), flush=True)
