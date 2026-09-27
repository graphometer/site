#!/usr/bin/env python3
"""Describer bake-off harness (stdlib only).

Sends each test picture to a local Ollama vision model with the prompt and
options of the describer settings we use [private wording removed from this
copy], and records time and text. One model + mode per run.

  python3 bakeoff.py --model qwen3-vl:30b-a3b-instruct --label qwen3vl30b_gpu
  python3 bakeoff.py --model qwen3-vl:30b-a3b-instruct --cpu --label qwen3vl30b_cpu
  python3 bakeoff.py --model qwen3.6:35b --think-off --label qwen36_35b_gpu

The first picture is a COLD call (model not loaded); the rest are warm.
The model is unloaded again at the end so the card is left free.
"""
import argparse
import base64
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLLAMA = "http://127.0.0.1:11434"
# The describer prompt. [Its wording comes from private code and is removed from
# this copy; data/README.md gives a paraphrase. Put your own prompt here.]
BASE_PROMPT = (
    "[prompt removed from this copy]"
)
TOOL_DEADLINE_S = 150.0   # the per-picture limit of the describer settings we use


def post(path, payload, timeout):
    req = urllib.request.Request(
        OLLAMA + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def sh(cmd):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception as e:  # noqa: BLE001
        return f"(failed: {type(e).__name__})"


def unload(model):
    try:
        post("/api/generate", {"model": model, "keep_alive": 0}, 60)
    except Exception:  # noqa: BLE001
        pass
    time.sleep(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--cpu", action="store_true", help="options.num_gpu = 0 (CPU only)")
    ap.add_argument("--think-off", action="store_true", help='send "think": false (thinking models)')
    ap.add_argument("--num-ctx", type=int, default=0, help="optional options.num_ctx")
    ap.add_argument("--num-thread", type=int, default=0, help="optional options.num_thread (CPU threads)")
    ap.add_argument("--images", default="", help="comma-separated filename prefixes; default all")
    ap.add_argument("--image-dir", default=str(HERE / "images"))
    ap.add_argument("--timeout", type=float, default=900.0)
    ap.add_argument("--keep", action="store_true", help="do not unload at the end")
    a = ap.parse_args()

    img_dir = Path(a.image_dir)
    files = sorted(p for p in img_dir.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"))
    if a.images:
        want = [w.strip() for w in a.images.split(",") if w.strip()]
        files = [p for p in files if any(p.name.startswith(w) for w in want)]
    if not files:
        sys.exit("no images selected")

    unload(a.model)
    gpu_before = sh("nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits")
    out = {"label": a.label, "model": a.model, "cpu": a.cpu, "think_off": a.think_off,
           "num_ctx": a.num_ctx, "num_thread": a.num_thread, "started": time.strftime("%Y-%m-%d %H:%M:%S"),
           "gpu_mib_before": gpu_before, "runs": []}
    print(f"== {a.label}: {a.model} cpu={a.cpu} think_off={a.think_off} ({len(files)} pictures)", flush=True)

    for i, p in enumerate(files):
        payload = {
            "model": a.model, "prompt": BASE_PROMPT,
            "images": [base64.b64encode(p.read_bytes()).decode()],
            "stream": False, "keep_alive": "60s",
            "options": {"num_predict": 2048},
        }
        if a.cpu:
            payload["options"]["num_gpu"] = 0
        if a.num_ctx:
            payload["options"]["num_ctx"] = a.num_ctx
        if a.num_thread:
            payload["options"]["num_thread"] = a.num_thread
        if a.think_off:
            payload["think"] = False
        t0 = time.monotonic()
        rec = {"file": p.name, "cold": i == 0}
        try:
            r = post("/api/generate", payload, a.timeout)
            wall = time.monotonic() - t0
            ns = 1e9
            rec.update({
                "wall_s": round(wall, 2),
                "load_s": round(r.get("load_duration", 0) / ns, 2),
                "prompt_tokens": r.get("prompt_eval_count"),
                "prompt_s": round(r.get("prompt_eval_duration", 0) / ns, 2),
                "out_tokens": r.get("eval_count"),
                "out_s": round(r.get("eval_duration", 0) / ns, 2),
                "done_reason": r.get("done_reason"),
                "within_tool_deadline": wall < TOOL_DEADLINE_S,
                "text": r.get("response", ""),
                "thinking_chars": len(r.get("thinking") or ""),
            })
        except Exception as e:  # noqa: BLE001
            rec.update({"wall_s": round(time.monotonic() - t0, 2), "error": f"{type(e).__name__}: {e}"[:300]})
        if i == 0:
            rec["ollama_ps"] = sh("ollama ps")
            rec["gpu_mib_loaded"] = sh("nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits")
        out["runs"].append(rec)
        tps = (rec.get("out_tokens") or 0) / rec["out_s"] if rec.get("out_s") else 0
        print(f"  {p.name:38s} {'COLD' if i == 0 else 'warm'} wall={rec.get('wall_s')}s load={rec.get('load_s')}s "
              f"img+prompt={rec.get('prompt_tokens')}tok/{rec.get('prompt_s')}s out={rec.get('out_tokens')}tok "
              f"({tps:.0f} t/s) {rec.get('done_reason', rec.get('error', ''))}", flush=True)
        if i == 0:
            for line in rec["ollama_ps"].splitlines()[1:]:
                print("     ps:", " ".join(line.split()), "| GPU MiB:", rec["gpu_mib_loaded"], flush=True)

    if not a.keep:
        unload(a.model)
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / f"{a.label}.json").write_text(json.dumps(out, indent=1))
    warm = [r["wall_s"] for r in out["runs"] if not r.get("cold") and "error" not in r]
    if warm:
        print(f"  -> warm median {sorted(warm)[len(warm)//2]}s, max {max(warm)}s; cold {out['runs'][0].get('wall_s')}s", flush=True)


if __name__ == "__main__":
    main()
