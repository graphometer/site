#!/usr/bin/env python3
"""Inkling-Small measurement: cold/resident decode with reasoning OFF (chat_template_kwargs reasoning_effort=none), planted-code
recall at growing depths, one reasoning-ON turn (medium) to see the thinking channel, and a tool-call schema check.
Usage: measure_inkling.py [base] [sizes csv]   default http://127.0.0.1:8136  2000,8000,32000"""
import json, sys, time, urllib.request
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8136"
sizes = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "2000,8000,32000").split(",")]
def chat(msgs, max_tokens, effort="none", tools=None):
    body = {"model": "x", "messages": msgs, "max_tokens": max_tokens, "temperature": 1.0, "chat_template_kwargs": {"reasoning_effort": effort}}
    if tools: body["tools"] = tools; body["tool_choice"] = "auto"
    req = urllib.request.Request(base + "/v1/chat/completions", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=36000)); return r, time.time() - t0
def rep(tag, r, w):
    t = r.get("timings", {}); m = r["choices"][0]["message"]; txt = (m.get("content") or "").strip().replace("\n", " "); rl = len(m.get("reasoning_content") or "")
    tc = m.get("tool_calls") or []
    print(f"[{tag}] prompt {t.get('prompt_n')} tok {t.get('prompt_ms',0)/1000:.1f} s = {t.get('prompt_per_second',0):.1f} t/s | decode {t.get('predicted_n')} tok = {t.get('predicted_per_second',0):.2f} t/s | wall {w:.1f} s | thought {rl} chars | tool_calls {len(tc)}", flush=True)
    print(f"        reply ({len(txt)} chars):", txt[:220], flush=True)
    if tc: print("        tool_call:", json.dumps(tc[0].get("function", tc[0]))[:220], flush=True)
    return txt, tc
q = [{"role": "user", "content": "In three sentences, describe a harbour town at dawn and name one thing a visitor should do."}]
r, w = chat(q, 300); rep("cold short (effort none)", r, w)
r, w = chat(q, 300); rep("same again (resident?)", r, w)
r, w = chat(q, 1500, effort="medium"); rep("thinking ON (medium)", r, w)
tools = [{"type": "function", "function": {"name": "get_weather", "description": "Current weather for a city", "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]
r, w = chat([{"role": "user", "content": "What is the weather in Lisbon right now? Use the tool."}], 300, tools=tools); rep("tool call (effort none)", r, w)
para = ("The river keeps its own hours. Boats go out before the light and come back when the gulls decide. "
        "Nobody on the quay hurries, and the coffee is always slightly burnt. ")
for n in sizes:
    parts = [para] * max(1, n // 40); code = f"MARLIN-{n}-COBALT"
    parts[len(parts)//2] = para + f" The harbourmaster's code word today is {code}. "
    r, w = chat([{"role": "user", "content": "".join(parts) + "\n\nWhat is the harbourmaster's code word today? Answer with the code word only."}], 60)
    txt, _ = rep(f"depth~{n}", r, w); print("        recall:", "OK" if code in txt else "MISSED", flush=True)
