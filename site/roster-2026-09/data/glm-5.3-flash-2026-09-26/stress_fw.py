#!/usr/bin/env python3
"""stress_variant.py — crash-hunt one model configuration through a (staged) start script.

Adapted 2026-09-26 from <REDACTED_PATH>/stress_model.py, which only
exercised the READ path (max_tokens 32). Speculation (MTP / a draft model) lives in the WRITE path, and a
hybrid model's save points are exercised by a follow-up turn on a cached prefix, so each prompt here:
  1. reads real mixed text (llama.cpp's own public C/C++/markdown sources) of a length mostly around one and
     two ubatches, then writes ~150 tokens at the served temperature (speculation active);
  2. takes a follow-up turn on the same conversation (prefix reuse + checkpoint restore + speculation).
The very first prompt is a ~3,000-token seed-20260920 ledger — the same kind of repetitive input that crashed Ling
at -ub 4096 on 2026-09-21 (same generator; not guaranteed byte-identical to the saved crash input).
A crash (connection error) restarts the server and saves the prompt. Empty answers are counted separately.

  usage: stress_variant.py <tag> <start-script> <port> <n_prompts> <seed> [ubatch]
  env:   the start script's knobs (exported by the caller)
"""
import json, os, random, signal, subprocess, sys, time, urllib.request
from pathlib import Path

TAG, SCRIPT, PORT, N, SEED = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
UB = int(sys.argv[6]) if len(sys.argv) > 6 else 512
S = Path(os.environ["FW_DIR"])
OUT = S / "logs" / f"stress_{TAG}_s{SEED}"; OUT.mkdir(parents=True, exist_ok=True)
env = dict(os.environ)
if subprocess.run(["pgrep", "-x", "llama-server"], capture_output=True).returncode == 0:
    sys.exit("REFUSED: a llama-server is already running")

files = [p for ext in ("*.cpp", "*.h", "*.cu", "*.md", "*.py")
         for p in Path("<REDACTED_PATH>/<BUILD>").rglob(ext)
         if p.stat().st_size > 4000 and "/build" not in str(p)]
rng = random.Random(SEED); rng.shuffle(files)
BASE = None


def health(host):
    try:
        return b"ok" in urllib.request.urlopen(f"http://{host}:{PORT}/health", timeout=3).read()
    except Exception:
        return False


def start():
    global BASE
    log = open(OUT / "server.log", "a")
    p = subprocess.Popen(["bash", SCRIPT], stdout=log, stderr=subprocess.STDOUT, env=env, start_new_session=True)
    for _ in range(900):
        time.sleep(2)
        if p.poll() is not None:
            sys.exit("server died on load — see server.log")
        for h in ("127.0.0.1", "<LOCAL>"):
            if health(h):
                BASE = f"http://{h}:{PORT}"
                return p
    sys.exit("server never healthy")


def stop(p):
    try:
        os.killpg(p.pid, signal.SIGTERM)
    except Exception:
        pass
    try:
        p.wait(60)
    except Exception:
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except Exception:
            pass
    subprocess.run(["pkill", "-x", "llama-server"]); time.sleep(4)


def post(path, obj, timeout):
    r = urllib.request.Request(BASE + path, data=json.dumps(obj).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))


def ledger_3000():
    """The batch sweep's own seed-20260920 ledger, sized to ~3,000 tokens (the Ling crash input's shape)."""
    r = random.Random(20260920); code = "AMBER-3172-WILLOW"
    T = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks"]
    def body(n):
        ls = [(f"ENTRY {i:05d}. the {r.choice(T)} was recorded by the reeve; reserve "
               f"{r.randint(3,400)} units against {r.randint(3,400)}.") for i in range(1, n + 1)]
        ls[n // 2] = f"ENTRY {n//2:05d}. SEALED REFERENCE for this ledger is {code}. Quote it in full."
        return "\n".join(ls)
    n = 90
    for _ in range(4):
        r.seed(20260920); t = len(post("/tokenize", {"content": body(n)}, 300)["tokens"])
        if abs(t - 3000) < 60:
            break
        n = max(20, int(n * 3000 / t))
    r.seed(20260920)
    return body(n) + "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only."


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
    if u < 0.55:
        return rng.randint(max(300, UB // 2), UB + 64)
    if u < 0.85:
        return rng.randint(UB + 65, 2 * UB + 600)
    return rng.randint(300, 12000)


def turn(messages, max_tokens):
    d = post("/v1/chat/completions", {"messages": messages, "max_tokens": max_tokens, "temperature": 0.7,
                                      "seed": rng.randint(1, 10**6), "stream": False,
                                      "chat_template_kwargs": {"enable_thinking": False}}, 1800)
    m = d["choices"][0]["message"]
    return (m.get("content") or "").strip(), d.get("timings", {}) or {}


srv = start()
crashes, empties, done, t0 = 0, 0, 0, time.time()
with open(OUT / "results.jsonl", "a") as res:
    for i in range(N):
        rec = {"i": i}; q = None
        try:
            if i == 0:
                q = ledger_3000(); rec["target"] = "replay3000"
            else:
                L = pick_len(); rec["target"] = L
                q = make_prompt(L) + "\n\nIn two or three sentences: what is the text above mostly about?"
            msgs = [{"role": "user", "content": q}]
            a1, ti1 = turn(msgs, 160)
            msgs += [{"role": "assistant", "content": a1},
                     {"role": "user", "content": "And what is one specific detail you noticed? One sentence."}]
            a2, ti2 = turn(msgs, 80)
            rec.update(ok=True, prompt_n=ti1.get("prompt_n"), dec1=round(ti1.get("predicted_per_second", 0) or 0, 1),
                       n1=ti1.get("predicted_n"), prompt2_n=ti2.get("prompt_n"),
                       dec2=round(ti2.get("predicted_per_second", 0) or 0, 1), n2=ti2.get("predicted_n"),
                       draft_acc1=ti1.get("draft_n_accepted"), draft_n1=ti1.get("draft_n"),
                       empty=(not a1) or (not a2), code_ok=("AMBER-3172-WILLOW" in a1) if i == 0 else None)
            if rec["empty"]:
                empties += 1
        except Exception as e:
            time.sleep(3)
            log = (OUT / "server.log").read_text(errors="replace")[-30000:]
            rec.update(ok=False, err=type(e).__name__, illegal="illegal memory access" in log,
                       oom="out of memory" in log.lower())
            (OUT / f"crash_{i}_prompt.txt").write_text(q or "")
            crashes += 1
            print(f"#{i} target={rec.get('target')} CRASH illegal={rec['illegal']} oom={rec['oom']}", flush=True)
            stop(srv); (OUT / "server.log").rename(OUT / f"server_crash_{i}.log"); srv = start()
        done += 1; res.write(json.dumps(rec) + "\n"); res.flush()
stop(srv)
summary = {"tag": TAG, "seed": SEED, "prompts": done, "crashes": crashes, "empty_answers": empties,
           "minutes": round((time.time() - t0) / 60, 1)}
(OUT / "SUMMARY.json").write_text(json.dumps(summary)); print("SUMMARY", json.dumps(summary), flush=True)
