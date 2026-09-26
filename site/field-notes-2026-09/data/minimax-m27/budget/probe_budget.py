#!/usr/bin/env python3
"""M2.7 thinking-budget probe: short answer, tool call, 8K recall - reports reasoning chars, decode, wall, and the time before the
first answer token (wall minus the answer's own decode time). Usage: probe_budget.py [base] [tag]"""
import json, sys, time, urllib.request
base = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:<PORT>"; tag = sys.argv[2] if len(sys.argv) > 2 else ""
def chat(msgs, max_tokens, tools=None):
    body = {"model": "x", "messages": msgs, "max_tokens": max_tokens, "temperature": 1.0}
    if tools: body["tools"] = tools; body["tool_choice"] = "auto"
    req = urllib.request.Request(base + "/v1/chat/completions", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    t0 = time.time(); r = json.load(urllib.request.urlopen(req, timeout=36000)); return r, time.time() - t0
def rep(name, r, w):
    t = r.get("timings", {}); m = r["choices"][0]["message"]; txt = (m.get("content") or "").strip().replace("\n", " "); rl = len(m.get("reasoning_content") or ""); tc = m.get("tool_calls") or []
    n_out = t.get("predicted_n") or 0; tps = t.get("predicted_per_second") or 1.0; ans_tok = max(1, len(txt) // 4) if txt else 0
    first = w - (ans_tok / tps)
    print(f"[{tag} {name}] prompt {t.get('prompt_n')} tok | decode {n_out} tok = {tps:.2f} t/s | wall {w:.1f} s | thought {rl} chars | ~first answer token at {first:.0f} s | tool_calls {len(tc)} | finish {r['choices'][0].get('finish_reason')}", flush=True)
    print(f"        reply ({len(txt)} chars):", txt[:240], flush=True)
    if tc: print("        tool_call:", json.dumps(tc[0].get("function", tc[0]))[:200], flush=True)
    return txt
rep("short", *chat([{"role": "user", "content": "In two or three sentences, describe a harbour town at dawn and name one thing a visitor should do."}], 600))
rep("question", *chat([{"role": "user", "content": "A friend says they feel invisible at work. In four sentences, what would you say to them?"}], 600))
tools = [{"type": "function", "function": {"name": "get_weather", "description": "Current weather for a city", "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}}]
rep("tool", *chat([{"role": "user", "content": "What is the weather in Lisbon right now? Use the tool."}], 600, tools=tools))
para = ("The river keeps its own hours. Boats go out before the light and come back when the gulls decide. Nobody on the quay hurries, and the coffee is always slightly burnt. ")
n = 8000; parts = [para] * (n // 40); parts[len(parts)//2] = para + " The harbourmaster's code word today is TIDEWATER-7391. "
txt = rep("depth~8K", *chat([{"role": "user", "content": "".join(parts) + "\n\nQuestion: what is the harbourmaster's code word today? Answer with the code word only."}], 300))
print("        recall:", "OK" if "TIDEWATER-7391" in txt else "MISSED", flush=True)
