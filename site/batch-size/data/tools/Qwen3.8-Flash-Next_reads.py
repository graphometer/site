#!/usr/bin/env python3
"""Qwen3.8-Flash-Next_reads.py: timed cold reads at chosen prompt sizes against a running llama-server, with a sealed-code check
and the model's page-cache residency before and after every read. Written 2026-09-26 for the Flash-Next
full-window batch comparison (graphometer.ai/batch-size/ section 04: why a 3,041-token read ran at 45.4 t/s at
262,144 while a 48K read ran at 511.7 at 131,072).

Each read is a fresh ledger document (a new seed, so nothing is reused from the prompt cache) with one sealed code at
50 % depth, or three codes at 5 / 50 / 95 % for the size given as --recall3, then "quote the code" with thinking off
and a small answer budget. [one sentence removed from this copy; it named an internal study]

usage: Qwen3.8-Flash-Next_reads.py --base http://<LOCAL> --tag T --out FILE.jsonl --sizes 3000,3000,48000,230000 --recall3 230000
"""
import argparse, json, random, subprocess, sys, time, urllib.request
from pathlib import Path

CODE = "AMBER-3172-WILLOW"
CODES3 = ["CEDAR-4418-HARBOR", "AMBER-3172-WILLOW", "SLATE-9051-MEADOW"]
TOPICS = ["drainage of the upper meadow", "insulation of the pump house", "seasoning of the oak planks",
          "mending of the north wall", "pruning of the orchard", "repair of the mill race"]
SYSTEM = "You are a careful clerk keeping an estate's records."
SHARDS = sorted(str(p) for p in Path("<MODEL_DIR>/Qwen3.8-Flash-Next").glob("*.gguf"))
HERE = Path(__file__).resolve().parent


def post(base, path, body, timeout=7200):
    r = urllib.request.Request(base + path, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=timeout))


def ntok(base, text):
    return len(post(base, "/tokenize", {"content": text}, timeout=900)["tokens"])


def ledger(n, seed, three=False):
    rng = random.Random(seed)
    ls = [(f"ENTRY {i:05d}. the {rng.choice(TOPICS)} was recorded by the reeve; reserve "
           f"{rng.randint(3, 400)} units against {rng.randint(3, 400)}.") for i in range(1, n + 1)]
    if three:
        for frac, code in zip((0.05, 0.50, 0.95), CODES3):
            k = int(n * frac)
            ls[k] = f"ENTRY {k:05d}. SEALED REFERENCE {CODES3.index(code) + 1} of 3 for this ledger is {code}. Quote it in full."
    else:
        ls[n // 2] = f"ENTRY {n // 2:05d}. SEALED REFERENCE for this ledger is {CODE}. Quote it in full."
    return "\n".join(ls)


def sized_ledger(base, target, seed, three=False):
    per = ntok(base, ledger(200, seed, three)) / 200
    n = max(20, int(target / per))
    for _ in range(3):
        t = ntok(base, ledger(n, seed, three))
        if abs(t - target) / target < 0.02:
            break
        n = max(20, int(n * target / t))
    return ledger(n, seed, three)


def resident():
    r = subprocess.run([sys.executable, str(HERE / "resident.py"), *SHARDS], capture_output=True, text=True)
    return json.loads(r.stdout)["resident_gb"] if r.returncode == 0 else None


def vram():
    r = subprocess.run(["nvidia-smi", "--query-gpu=memory.used", "--format=csv,noheader,nounits"], capture_output=True, text=True)
    return int(r.stdout.strip().splitlines()[0]) if r.returncode == 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sizes", default="3000,3000,48000,230000")
    ap.add_argument("--recall3", type=int, default=230000)
    a = ap.parse_args()
    for i, size in enumerate(int(x) for x in a.sizes.split(",") if x):
        three = size == a.recall3
        doc = sized_ledger(a.base, size, seed=20260926 + 1000 * i + size, three=three)
        q = ("\n\nQUESTION: quote all three sealed references exactly, in order (1, 2, 3), one per line. Answer with the codes only."
             if three else "\n\nQUESTION: quote the sealed reference exactly. Answer with the code only.")
        req = {"messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": doc + q}],
               "max_tokens": 120, "temperature": 0.0, "seed": 1, "stream": False, "cache_prompt": True,
               "chat_template_kwargs": {"enable_thinking": False}}
        r0 = resident()
        t0 = time.time()
        d = post(a.base, "/v1/chat/completions", req)
        wall = time.time() - t0
        r1 = resident()
        c = ((d["choices"][0]["message"].get("content")) or "").strip()
        ti = d.get("timings", {}) or {}
        row = {"tag": a.tag, "n": i + 1, "size_target": size, "prompt_n": ti.get("prompt_n"),
               "prompt_ms": round(ti.get("prompt_ms", 0) or 0), "prefill_tps": round(ti.get("prompt_per_second", 0) or 0, 1),
               "predicted_n": ti.get("predicted_n"), "decode_tps": round(ti.get("predicted_per_second", 0) or 0, 2),
               "wall_s": round(wall, 1), "resident_gb_before": r0, "resident_gb_after": r1, "vram_mib_after": vram(),
               "code_ok": (all(cd in c for cd in CODES3) if three else CODE in c),
               **({"codes3_hits": sum(cd in c for cd in CODES3)} if three else {}), "answer": c[-80:],
               "t_end": time.strftime("%H:%M:%S")}
        print(json.dumps(row), flush=True)
        with open(a.out, "a") as f:
            f.write(json.dumps(row) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}), flush=True)
        sys.exit(3)
