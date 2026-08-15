#!/usr/bin/env python3
"""First-load probe harness for Qwen3.8-27B. Every request/response is saved to raw/
so that every number in the findings traces to a file on disk."""
import json
import os
import sys
import time
import urllib.request

BASE = os.environ.get("PROBE_BASE", "http://127.0.0.1:8198/v1")
OUT = os.environ.get("PROBE_OUT", os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(OUT, "raw")
os.makedirs(RAW, exist_ok=True)


def call(tag, body, timeout=900):
    url = f"{BASE}/chat/completions"
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            resp = json.loads(r.read())
        err = None
    except Exception as e:
        resp, err = {}, f"{type(e).__name__}: {e}"
    dt = time.time() - t0
    rec = {"tag": tag, "wall_s": round(dt, 3), "request": body, "response": resp, "error": err}
    with open(os.path.join(RAW, f"{tag}.json"), "w") as f:
        json.dump(rec, f, indent=1)
    return rec


def summarize(rec):
    r = rec["response"]
    if rec["error"]:
        return {"tag": rec["tag"], "ERROR": rec["error"]}
    ch = (r.get("choices") or [{}])[0]
    msg = ch.get("message") or {}
    content = msg.get("content") or ""
    reasoning = msg.get("reasoning_content") or ""
    usage = r.get("usage") or {}
    tim = r.get("timings") or {}
    return {
        "tag": rec["tag"],
        "wall_s": rec["wall_s"],
        "finish": ch.get("finish_reason"),
        "content_chars": len(content),
        "content_empty": (len(content.strip()) == 0),
        "reasoning_chars": len(reasoning),
        "has_think_tag_in_content": ("<think>" in content),
        "tool_calls": len(msg.get("tool_calls") or []),
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "predicted_per_second": round(tim.get("predicted_per_second", 0), 2) or None,
        "prompt_per_second": round(tim.get("prompt_per_second", 0), 2) or None,
        "content_head": content.strip()[:220].replace("\n", " "),
    }


MODEL = "qwen3.8-27b"

PROBES = []

# P1 exact-phrase echo
PROBES.append(("p1_echo", {
    "model": MODEL, "max_tokens": 4096,
    "messages": [{"role": "user", "content":
                  "Reply with exactly this phrase and nothing else: The vault holds."}]}))

# P2 bare identity
PROBES.append(("p2_identity", {
    "model": MODEL, "max_tokens": 4096,
    "messages": [{"role": "user", "content": "Who are you? Answer in two sentences."}]}))

# P3 bat and ball
PROBES.append(("p3_batball", {
    "model": MODEL, "max_tokens": 4096,
    "messages": [{"role": "user", "content":
                  "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the "
                  "ball. How much does the ball cost?"}]}))

# P4 merge_intervals with executed asserts
PROBES.append(("p4_merge_intervals", {
    "model": MODEL, "max_tokens": 4096,
    "messages": [{"role": "user", "content":
                  "Write a Python function merge_intervals(intervals) that merges overlapping "
                  "intervals. Return ONLY a fenced python code block containing the function "
                  "and three assert statements that verify it."}]}))

# P5 tool shape
PROBES.append(("p5_tools", {
    "model": MODEL, "max_tokens": 4096,
    "messages": [{"role": "user", "content": "What is the weather in Reykjavik in Celsius?"}],
    "tools": [{"type": "function", "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "parameters": {"type": "object", "properties": {
            "city": {"type": "string"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}},
            "required": ["city", "unit"], "additionalProperties": False}}}]}))

# P6 thinking-budget map — the family trait, tested explicitly
for b in (60, 500, 2000, 4096):
    PROBES.append((f"p6_budget_{b}", {
        "model": MODEL, "max_tokens": b,
        "messages": [{"role": "user", "content":
                      "What is 17 * 24? Give the number."}]}))

# P7 reasoning toggle honesty
PROBES.append(("p7_think_off", {
    "model": MODEL, "max_tokens": 512,
    "chat_template_kwargs": {"enable_thinking": False},
    "messages": [{"role": "user", "content": "What is 17 * 24? Give the number."}]}))
PROBES.append(("p7_think_on", {
    "model": MODEL, "max_tokens": 4096,
    "chat_template_kwargs": {"enable_thinking": True},
    "messages": [{"role": "user", "content": "What is 17 * 24? Give the number."}]}))

# P8 reasoning_effort knob (template-level; xhigh|medium|low, anything else must raise)
for eff in ("low", "medium", "xhigh"):
    PROBES.append((f"p8_effort_{eff}", {
        "model": MODEL, "max_tokens": 4096,
        "chat_template_kwargs": {"reasoning_effort": eff},
        "messages": [{"role": "user", "content":
                      "A farmer has 17 sheep. All but 9 run away. How many are left? Explain briefly."}]}))
PROBES.append(("p8_effort_bogus", {
    "model": MODEL, "max_tokens": 256,
    "chat_template_kwargs": {"reasoning_effort": "ultra"},
    "messages": [{"role": "user", "content": "Hello."}]}))

if __name__ == "__main__":
    only = sys.argv[1:] or None
    results = []
    for tag, body in PROBES:
        if only and not any(o in tag for o in only):
            continue
        print(f"--- {tag} ...", flush=True)
        rec = call(tag, body)
        s = summarize(rec)
        results.append(s)
        print(json.dumps(s, indent=1), flush=True)
    with open(os.path.join(OUT, "probe_summary.json"), "w") as f:
        json.dump(results, f, indent=1)
