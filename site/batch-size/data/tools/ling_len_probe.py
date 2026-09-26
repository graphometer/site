#!/usr/bin/env python3
"""ling_len_probe.py: is ling's crash a LENGTH rule? Sends raw token prompts of EXACT lengths through
/completion (no chat template, so the count is exact), one fresh server per crash, and records
crash/ok per length. Content = natural text (a llama.cpp source file), NOT the ledger, so a
length-only rule would show up on different content.

Hypothesis under test: ling's KDA layers scan in 64-token chunks; the crashing prompt was 3,007
tokens = 47*64 - 1. If the rule is "first ubatch with n = 63 mod 64", then e.g. 2047, 2111, 3007,
4031 crash on ANY content and 3006/3008 do not.

    ling_len_probe.py <ubatch> <len> [<len> ...]
"""
import json, os, signal, subprocess, sys, time, urllib.request
from pathlib import Path

UB = int(sys.argv[1]); LENS = [int(x) for x in sys.argv[2:]]
OUT = Path(f"<OUTPUT_DIR>/logs/lenprobe_ub{UB}")
OUT.mkdir(parents=True, exist_ok=True)
BIN = "<llama.cpp build d3146f2b5>/llama-server"
MODEL = "<MODEL_DIR>/Ling-3.0-flash/Ling-3.0-flash-Q4_K_M/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf"
ENV = dict(os.environ, LD_LIBRARY_PATH="<llama.cpp build d3146f2b5>:<CUDA 12.8 libraries>")
BASE = "http://127.0.0.1:8188"
TEXT = Path("<llama.cpp source at d3146f2b5>/ggml/src/ggml-cuda/ggml-cuda.cu").read_text(errors="replace")

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

srv = start()
toks = post("/tokenize", {"content": TEXT * 3}, 300)["tokens"]
for L in LENS:
    if srv.poll() is not None: srv = start()
    # fresh server state per length: erase the slot so every probe is a FIRST ubatch
    try: post("/slots/0?action=erase", {}, 30)
    except Exception: pass
    try:
        d = post("/completion", {"prompt": toks[:L], "n_predict": 2, "cache_prompt": False, "temperature": 0}, 900)
        n = d.get("timings", {}).get("prompt_n")
        print(f"len={L} (mod64={L % 64}) OK prompt_n={n}", flush=True)
    except Exception as e:
        time.sleep(2)
        ill = "illegal memory access" in (OUT / "server.log").read_text(errors="replace")[-20000:]
        print(f"len={L} (mod64={L % 64}) CRASH illegal={ill} ({type(e).__name__})", flush=True)
        if srv.poll() is None: srv.send_signal(signal.SIGTERM); srv.wait(30)
        (OUT / "server.log").rename(OUT / f"server_crash_len{L}.log")
        srv = start()
srv.send_signal(signal.SIGTERM)
try: srv.wait(30)
except Exception: srv.kill()
