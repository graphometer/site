#!/usr/bin/env python3
"""Qwen3.8-27B local reasoning_effort study, 2026-08-16.

Runs the pre-registered grid (RUN_LOG.md section 2) against the scratch b10453 build.
Every request and response is written to raw/ so every number traces to a file.

Reasoning/visible token counts are measured EXACTLY by posting the returned text back to
the server's own /tokenize endpoint -- not estimated from characters.
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error

BASE = os.environ.get("STUDY_BASE", "http://127.0.0.1:8196")
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
os.makedirs(RAW, exist_ok=True)

PROMPTS_DIR = "<VAULT>/work/qwen/instrument/prompts"

MARBLE = ("A bag holds 3 red, 4 blue and 5 green marbles. You draw three marbles without "
          "replacement. What is the probability that you draw exactly one of each colour? "
          "Give the answer as a reduced fraction, and show the count of favourable outcomes "
          "and the total number of outcomes.")


def read_prompt(name):
    with open(os.path.join(PROMPTS_DIR, name)) as f:
        return f.read()


PROMPT_SET = {
    "marble": MARBLE,
    "c6_toggle": read_prompt("c6_reasoning_toggle.txt"),
    "c5_budget": read_prompt("c5_thinking_budget.txt"),
}

EFFORTS = ["xhigh", "medium", "low", "absent"]
REPS = 3
MAX_TOKENS = 2000


def post(path, body, timeout=900):
    """POST json, return (http_status, parsed_or_text, error_str_or_None)."""
    url = BASE + path
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            txt = r.read().decode("utf-8", "replace")
            try:
                return r.status, json.loads(txt), None
            except Exception:
                return r.status, txt, None
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(txt), f"HTTPError {e.code}"
        except Exception:
            return e.code, txt, f"HTTPError {e.code}"
    except Exception as e:
        return None, None, f"{type(e).__name__}: {e}"


def ntok(text):
    """Exact token count via the server's own tokenizer. '' -> 0."""
    if not text:
        return 0
    st, body, err = post("/tokenize", {"content": text}, timeout=120)
    if err or not isinstance(body, dict):
        return None
    return len(body.get("tokens") or [])


def save(tag, obj):
    with open(os.path.join(RAW, f"{tag}.json"), "w") as f:
        json.dump(obj, f, indent=1)


def build_body(prompt_text, effort, path_mode):
    """path_mode: 'toplevel' | 'kwargs' | 'none'."""
    body = {
        "model": "qwen3.8-27b-study",
        "messages": [{"role": "user", "content": prompt_text}],
        "max_tokens": MAX_TOKENS,
        "temperature": 0,
        "seed": 42,
    }
    if effort != "absent":
        if path_mode == "toplevel":
            body["reasoning_effort"] = effort
        elif path_mode == "kwargs":
            body["chat_template_kwargs"] = {"reasoning_effort": effort}
    return body


# ---------------------------------------------------------------- phase 1: renders
def phase_renders():
    print("=== PHASE 1: /apply-template renders (the injection witness) ===", flush=True)
    rows = []
    cases = []
    for eff in EFFORTS:
        cases.append((f"render_toplevel_{eff}", eff, "toplevel"))
    for eff in ["xhigh", "medium", "low"]:
        cases.append((f"render_kwargs_{eff}", eff, "kwargs"))
    # special values, both paths
    for special in ["high", "none", "ultra"]:
        cases.append((f"render_toplevel_{special}", special, "toplevel"))
        cases.append((f"render_kwargs_{special}", special, "kwargs"))

    for tag, eff, mode in cases:
        body = build_body(MARBLE, eff, mode)
        body.pop("max_tokens", None)
        st, resp, err = post("/apply-template", body, timeout=120)
        prompt = resp.get("prompt") if isinstance(resp, dict) else None
        tk = ntok(prompt) if prompt else None
        rec = {"tag": tag, "effort": eff, "path": mode, "http_status": st,
               "error": err, "request": body, "response": resp,
               "prompt_chars": len(prompt) if prompt else None,
               "prompt_tokens_tokenize": tk}
        save(tag, rec)
        rows.append(rec)
        print(f"  {tag:28s} http={st} chars={rec['prompt_chars']} tok={tk} err={err}",
              flush=True)
    return rows


# ---------------------------------------------------------------- phase 2: the grid
def phase_grid():
    print("=== PHASE 2: grid 3 prompts x 4 efforts x 3 reps (top-level field) ===",
          flush=True)
    rows = []
    for pname, ptext in PROMPT_SET.items():
        for eff in EFFORTS:
            for rep in range(1, REPS + 1):
                tag = f"grid_{pname}_{eff}_r{rep}"
                body = build_body(ptext, eff, "toplevel")
                t0 = time.time()
                st, resp, err = post("/v1/chat/completions", body)
                wall = round(time.time() - t0, 3)

                content = reasoning = ""
                finish = None
                usage = {}
                timings = {}
                if isinstance(resp, dict) and not err:
                    ch = (resp.get("choices") or [{}])[0]
                    msg = ch.get("message") or {}
                    content = msg.get("content") or ""
                    reasoning = msg.get("reasoning_content") or ""
                    finish = ch.get("finish_reason")
                    usage = resp.get("usage") or {}
                    timings = resp.get("timings") or {}

                rec = {
                    "tag": tag, "prompt": pname, "effort": eff, "rep": rep,
                    "path": "toplevel", "http_status": st, "error": err,
                    "wall_s": wall, "finish_reason": finish,
                    "prompt_tokens": usage.get("prompt_tokens"),
                    "completion_tokens": usage.get("completion_tokens"),
                    "total_tokens": usage.get("total_tokens"),
                    "reasoning_tokens": ntok(reasoning),
                    "visible_tokens": ntok(content),
                    "reasoning_chars": len(reasoning),
                    "visible_chars": len(content),
                    "think_leak_in_content": "<think>" in content,
                    "predicted_per_second": timings.get("predicted_per_second"),
                    "request": body, "response": resp,
                }
                save(tag, rec)
                rows.append(rec)
                print(f"  {tag:32s} ptok={rec['prompt_tokens']} rtok={rec['reasoning_tokens']}"
                      f" vtok={rec['visible_tokens']} ctok={rec['completion_tokens']}"
                      f" fin={finish} {wall}s", flush=True)
    return rows


# ---------------------------------------------------------------- phase 3: invalid
def phase_invalid():
    print("=== PHASE 3: invalid-effort probes ===", flush=True)
    rows = []
    cases = [
        ("invalid_toplevel_chat", "ultra", "toplevel", "/v1/chat/completions"),
        ("invalid_kwargs_chat", "ultra", "kwargs", "/v1/chat/completions"),
        ("invalid_toplevel_apply", "ultra", "toplevel", "/apply-template"),
        ("invalid_kwargs_apply", "ultra", "kwargs", "/apply-template"),
        ("none_toplevel_chat", "none", "toplevel", "/v1/chat/completions"),
        ("high_toplevel_chat", "high", "toplevel", "/v1/chat/completions"),
    ]
    for tag, eff, mode, path in cases:
        body = build_body("What is 17 * 24? Give the number.", eff, mode)
        if path == "/apply-template":
            body.pop("max_tokens", None)
        else:
            body["max_tokens"] = 2000
        t0 = time.time()
        st, resp, err = post(path, body, timeout=300)
        wall = round(time.time() - t0, 3)
        summary = None
        if path == "/v1/chat/completions" and isinstance(resp, dict) and not err:
            ch = (resp.get("choices") or [{}])[0]
            msg = ch.get("message") or {}
            summary = {
                "finish_reason": ch.get("finish_reason"),
                "prompt_tokens": (resp.get("usage") or {}).get("prompt_tokens"),
                "completion_tokens": (resp.get("usage") or {}).get("completion_tokens"),
                "reasoning_tokens": ntok(msg.get("reasoning_content") or ""),
                "visible_tokens": ntok(msg.get("content") or ""),
                "visible_head": (msg.get("content") or "")[:200],
            }
        rec = {"tag": tag, "effort": eff, "path": mode, "endpoint": path,
               "http_status": st, "error": err, "wall_s": wall,
               "summary": summary, "request": body, "response": resp}
        save(tag, rec)
        rows.append(rec)
        print(f"  {tag:26s} http={st} err={err} {json.dumps(summary)[:130] if summary else ''}",
              flush=True)
    return rows


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    out = {}
    if which in ("all", "renders"):
        out["renders"] = phase_renders()
    if which in ("all", "grid"):
        out["grid"] = phase_grid()
    if which in ("all", "invalid"):
        out["invalid"] = phase_invalid()
    with open(os.path.join(HERE, f"results_{which}.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("DONE", flush=True)
