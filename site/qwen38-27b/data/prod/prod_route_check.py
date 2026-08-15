#!/usr/bin/env python3
"""Prove the PRODUCTION route (docker bridge <BRIDGE-IP>:8109) end to end, including a
two-hop tool round-trip — the shape any agent client needs."""
import json
import time
import urllib.request

BASE = "http://<BRIDGE-IP>:8109/v1"


def call(body):
    r = urllib.request.Request(BASE + "/chat/completions", data=json.dumps(body).encode(),
                               headers={"Content-Type": "application/json"})
    t = time.time()
    with urllib.request.urlopen(r, timeout=300) as f:
        d = json.loads(f.read())
    return d, time.time() - t


out = {}
d, dt = call({"model": "qwen3.8-27b", "max_tokens": 4096,
              "messages": [{"role": "user", "content": "Reply with exactly: bridge ok"}]})
m = d["choices"][0]["message"]
out["1_bridge"] = {"wall_s": round(dt, 2), "content": m["content"],
                   "tps": d["timings"]["predicted_per_second"]}
print("1. docker-bridge call  : %.2fs content=%r  %.1f t/s" % (dt, m["content"], out["1_bridge"]["tps"]))

tools = [{"type": "function", "function": {
    "name": "read_file", "description": "Read a file from disk.",
    "parameters": {"type": "object", "properties": {"path": {"type": "string"}},
                   "required": ["path"], "additionalProperties": False}}}]
msgs = [{"role": "user", "content": "Read the file nums.txt and tell me the sum of the numbers in it."}]
d, dt = call({"model": "qwen3.8-27b", "max_tokens": 4096, "messages": msgs, "tools": tools})
m = d["choices"][0]["message"]
tc = m.get("tool_calls")
out["2_tool_request"] = {"wall_s": round(dt, 2), "tool_calls": tc}
print("2. tool call requested : %s" % json.dumps(tc))

msgs.append({"role": "assistant", "content": m.get("content") or "", "tool_calls": tc})
msgs.append({"role": "tool", "tool_call_id": tc[0]["id"], "content": "12\n45\n7\n93\n28\n"})
d, dt = call({"model": "qwen3.8-27b", "max_tokens": 4096, "messages": msgs, "tools": tools})
m = d["choices"][0]["message"]
ok = "185" in (m["content"] or "")
out["3_tool_result_used"] = {"wall_s": round(dt, 2), "content": m["content"], "correct_185": ok}
print("3. tool result used    : %.2fs  %r" % (dt, (m["content"] or "")[:200]))
print("   correct sum is 185 ->", "CORRECT" if ok else "WRONG")

json.dump(out, open("raw/prod_route_check.json", "w"), indent=1)
