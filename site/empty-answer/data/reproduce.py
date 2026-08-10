#!/usr/bin/env python3
"""reproduce.py: the budget-to-visible-answer curve, on your own route.

This is the script behind the tables on
https://graphometer.ai/empty-answer/ . It answers one question at each budget,
and it is deliberately the crude one rather than a quality question:

    did any visible answer come back at all?

Point it at any OpenAI-compatible /chat/completions route: a hosted aggregator,
a vendor endpoint, or your own llama.cpp / vLLM / Ollama server on loopback. Give
it the prompt you actually send in production, not a toy one -- the whole finding
on that page is that the floor moves with the task, so a floor measured on
someone else's prompt is not your floor.

USAGE

  # a local route, no key needed
  python3 reproduce.py \
      --base-url http://127.0.0.1:8080/v1 \
      --model my-model \
      --prompt-file ./my_real_prompt.txt \
      --out ./my-floor

  # a hosted route; the key is read from the environment ONLY
  export MY_API_KEY=...            # never pass a key as a flag
  python3 reproduce.py \
      --base-url https://openrouter.ai/api/v1 \
      --model qwen/qwen3.8-max \
      --key-env MY_API_KEY \
      --budget-cap-usd 0.25 \
      --out ./hosted-floor

OUTPUT

  <out>/curve.json          one row per budget, plus the prompt and the totals
  <out>/mt<N>.req.json      the exact request body sent at budget N
  <out>/mt<N>.resp.json     the exact response body received at budget N

Every number in the summary table comes out of those files, so anyone can
re-derive it without trusting the summary.

NOTES

  * Temperature is 0 by default so that repeated runs are comparable. That is a
    measurement choice, not a recommendation for production.
  * Cost is read from the response's own usage block when the route reports one.
    Routes that do not report cost simply leave it blank; the sweep still works.
  * The script never starts a server and never writes outside --out.
  * There is a spend cap. It is checked after each call against the cost the
    route itself reported, so it is a brake, not a guarantee. Set it low first.

Graphometer, 2026-08-09. Public domain -- copy it, change it, no attribution needed.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

DEFAULT_BUDGETS = [64, 128, 256, 512, 1024, 2048, 4096]

# The fixed prompt used for the three lanes on the page. Replace it with your own
# via --prompt-file; this one is here so the published curve can be re-run exactly.
PAGE_PROMPT = (
    "A bag holds 3 red, 4 blue and 5 green marbles. You draw three marbles without "
    "replacement. What is the probability that you draw exactly one of each colour? "
    "Give the answer as a reduced fraction, and show the count of favourable outcomes "
    "and the total number of outcomes."
)


def call(url, model, prompt, max_tokens, key, temperature, timeout, extra_body):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    body.update(extra_body)
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return body, json.load(r), round(time.time() - t0, 2), None
    except urllib.error.HTTPError as e:
        # the response body is echoed, never the request headers, which carry the key
        detail = e.read().decode("utf-8", "replace")[:400]
        return body, None, round(time.time() - t0, 2), f"HTTP {e.code}: {detail}"
    except Exception as e:  # noqa: BLE001
        return body, None, round(time.time() - t0, 2), f"{type(e).__name__}: {str(e)[:200]}"


def summarise(resp):
    """Pull the four fields that decide whether the caller got an answer."""
    ch = (resp.get("choices") or [{}])[0]
    msg = ch.get("message") or {}
    content = msg.get("content") or ""
    # different routes name the hidden trace differently; check both
    reasoning = msg.get("reasoning") or msg.get("reasoning_content") or ""
    usage = resp.get("usage") or {}
    details = usage.get("completion_tokens_details") or {}
    return {
        "finish_reason": ch.get("finish_reason"),
        "visible_answer_present": bool(content.strip()),
        "visible_chars": len(content),
        "hidden_reasoning_chars": len(reasoning),
        "reasoning_tokens": details.get("reasoning_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "prompt_tokens": usage.get("prompt_tokens"),
        "cost_usd": usage.get("cost"),
        "provider": resp.get("provider"),
        "response_id": resp.get("id"),
        "content_head": content[:120].replace("\n", " "),
    }


def main():
    ap = argparse.ArgumentParser(description="Measure a model's budget floor on your own prompt.")
    ap.add_argument("--base-url", required=True,
                    help="OpenAI-compatible base, e.g. http://127.0.0.1:8080/v1")
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", required=True, help="directory for the raw bodies and curve.json")
    ap.add_argument("--prompt-file", help="your real prompt; defaults to the page's marble prompt")
    ap.add_argument("--budgets", type=int, nargs="+", default=DEFAULT_BUDGETS)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--key-env", default=None,
                    help="name of the environment variable holding the API key. "
                         "The key itself is never accepted as a flag.")
    ap.add_argument("--budget-cap-usd", type=float, default=0.50,
                    help="stop the sweep once the route's own reported cost exceeds this")
    ap.add_argument("--extra-body", default="{}",
                    help='JSON merged into every request, e.g. \'{"reasoning":{"effort":"low"}}\'')
    args = ap.parse_args()

    key = None
    if args.key_env:
        key = os.environ.get(args.key_env)
        if not key:
            print(f"REFUSED: {args.key_env} is not set in the environment.", file=sys.stderr)
            return 2

    try:
        extra_body = json.loads(args.extra_body)
    except json.JSONDecodeError as e:
        print(f"--extra-body is not valid JSON: {e}", file=sys.stderr)
        return 2

    prompt = PAGE_PROMPT
    if args.prompt_file:
        with open(args.prompt_file) as fh:
            prompt = fh.read()

    url = args.base_url.rstrip("/") + "/chat/completions"
    os.makedirs(args.out, exist_ok=True)

    rows, total_cost = [], 0.0
    for mt in sorted(args.budgets):
        if total_cost > args.budget_cap_usd:
            print(f"STOPPING: reported spend ${total_cost:.4f} passed the cap "
                  f"${args.budget_cap_usd:.2f}", file=sys.stderr)
            break
        body, resp, elapsed, err = call(url, args.model, prompt, mt, key,
                                        args.temperature, args.timeout, extra_body)
        if err:
            row = {"max_tokens": mt, "error": err, "elapsed_s": elapsed}
        else:
            row = {"max_tokens": mt, "elapsed_s": elapsed}
            row.update(summarise(resp))
            total_cost += float(row.get("cost_usd") or 0.0)
            with open(os.path.join(args.out, f"mt{mt}.req.json"), "w") as fh:
                json.dump(body, fh, indent=1)
            with open(os.path.join(args.out, f"mt{mt}.resp.json"), "w") as fh:
                json.dump(resp, fh, indent=1)
        rows.append(row)
        print(json.dumps(row), flush=True)

    with open(os.path.join(args.out, "curve.json"), "w") as fh:
        json.dump({"base_url": args.base_url, "model": args.model, "prompt": prompt,
                   "temperature": args.temperature, "budgets": args.budgets,
                   "extra_body": extra_body, "rows": rows,
                   "total_reported_cost_usd": round(total_cost, 6)}, fh, indent=1)

    print("\n=== BUDGET TO VISIBLE ANSWER ===")
    print(f"{'max_tokens':>10} {'answer?':>8} {'vis_chars':>10} {'reason_tok':>11} "
          f"{'compl_tok':>10} {'finish':>10} {'secs':>8}")
    first_visible = first_complete = None
    for r in rows:
        if "error" in r:
            print(f"{r['max_tokens']:>10}  ERROR {r['error'][:60]}")
            continue
        print(f"{r['max_tokens']:>10} {str(r['visible_answer_present']):>8} "
              f"{r['visible_chars']:>10} {str(r['reasoning_tokens']):>11} "
              f"{str(r['completion_tokens']):>10} {str(r['finish_reason']):>10} "
              f"{r['elapsed_s']:>8}")
        if r["visible_answer_present"] and first_visible is None:
            first_visible = r["max_tokens"]
        if r["finish_reason"] == "stop" and first_complete is None:
            first_complete = r["max_tokens"]

    answered = [r for r in rows if "error" not in r]
    if not answered:
        print("\nEvery call errored. Nothing was measured; fix the route first.")
        print(f"reported spend          : ${total_cost:.5f}")
        return 1

    print(f"\nfirst visible answer at : {first_visible if first_visible else 'NOT REACHED'}")
    print(f"first complete answer at: {first_complete if first_complete else 'NOT REACHED'}")
    if first_complete is None:
        print("The floor for this prompt is above the largest budget you swept. "
              "Raise --budgets before drawing any conclusion.")
    print(f"reported spend          : ${total_cost:.5f}")
    print("\nThis floor belongs to THIS prompt on THIS route on THIS day. "
          "It is not a constant of the model.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
