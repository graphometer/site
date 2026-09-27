#!/usr/bin/env python3
"""Rebuild derived/runs.tsv and derived/strings_by_picture.tsv from this package (reads files only).

runs.tsv: one row per run. Request settings and timings come from results/<label>.json;
the thread count the server reported and the window it ran with come from the launch and
system_info lines in service-log/ollama_2026-09-20_excerpt.txt, matched to the run by time
(the first launch within 10 seconds after the run's "started" time). The picture folder is
not recorded in the result files: it is read from the label (px1536, px1024, hires_N), and
the prompt token counts agree with it. The default-thread CPU run left no JSON (it was
stopped after its first picture); its row is built from results/qwen3vl30b_cpu.log and the
service log, and marked so.

strings_by_picture.tsv: for every run and picture, the expected strings found and missed,
with score.py's matching rule.

Written 26 September 2026 for the page.   python3 tables.py
"""
import datetime as dt
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
truth = json.loads((HERE / "ground_truth.json").read_text())
LOG = (HERE / "service-log" / "ollama_2026-09-20_excerpt.txt").read_text().splitlines()


def norm(s):
    s = s.lower().replace("£", "").replace("$", "").replace(",", "")
    return re.sub(r"\s+", " ", s)


# launches: time, window, threads flag, gpu-layer flag; then the n_threads report that follows
launches = []
for line in LOG:
    m = re.match(r"(\S+) .*msg=\"starting llama-server\" cmd=\"(.*)\"", line)
    if m:
        t = dt.datetime.fromisoformat(m.group(1)).replace(tzinfo=None)
        cmd = m.group(2)
        c = re.search(r" -c (\d+)", cmd)
        th = re.search(r" -t (\d+)", cmd)
        launches.append({"time": t, "ctx": c.group(1) if c else "", "t_flag": th.group(1) if th else "none",
                         "ngl0": " -ngl 0" in cmd, "n_threads": None})
        continue
    m = re.search(r"system_info: n_threads = (\d+) \(n_threads_batch = (\d+)\) / (\d+)", line)
    if m and launches and launches[-1]["n_threads"] is None:
        launches[-1]["n_threads"] = f"{m.group(1)} of {m.group(3)}"


def launch_for(started):
    for L in launches:
        if started <= L["time"] <= started + dt.timedelta(seconds=10):
            return L
    return None


def folder(label):
    if "px1536" in label:
        return "images_1536"
    if "px1024" in label:
        return "images_1024"
    m = re.match(r"hires_30b_hires(?:_(\d+))?$", label)
    if m:
        return "hires" + (f"_{m.group(1)}" if m.group(1) else "")
    return "images"


def ps_fields(ps):
    line = ps.splitlines()[1] if ps and len(ps.splitlines()) > 1 else ""
    m = re.search(r"\s(\d+(?:\.\d+)? GB)\s+(.+?)\s{2,}(\d+)\s", line)
    return (m.group(1), m.group(2).strip(), m.group(3)) if m else ("", "", "")


cols = ["label", "model", "started", "card_allowed", "num_thread_requested", "threads_server_reported",
        "num_ctx_requested", "window_server", "think_off", "picture_folder", "pictures",
        "where_it_ran_ollama_ps", "ollama_ps_size", "card_mib_before", "card_mib_after_first",
        "first_picture", "first_wall_s", "first_load_s", "first_prompt_tokens", "first_prompt_s",
        "first_out_tokens", "first_out_s", "first_done", "warm_n", "warm_min_s", "warm_max_s",
        "score_py_warm_med_s", "strings_found", "strings_expected", "over_150_s"]
rows = []
pic_rows = []
for p in sorted((HERE / "results").glob("*.json")):
    d = json.loads(p.read_text())
    label = d["label"]
    started = dt.datetime.strptime(d["started"], "%Y-%m-%d %H:%M:%S")
    L = launch_for(started)
    runs = d["runs"]
    first = runs[0]
    warm = sorted(r["wall_s"] for r in runs[1:])
    size, where, ctx = ps_fields(first.get("ollama_ps", ""))
    got = need = late = 0
    for r in runs:
        exp = truth.get(r["file"], {}).get("expect", [])
        t = norm(r.get("text", ""))
        hit = [e for e in exp if norm(e) in t]
        miss = [e for e in exp if e not in hit]
        got += len(hit)
        need += len(exp)
        late += 0 if r.get("within_tool_deadline", True) else 1
        if exp:
            pic_rows.append([label, r["file"], str(len(hit)), str(len(exp)), " | ".join(miss)])
    rows.append([
        label, d["model"], d["started"], "no (num_gpu 0)" if d["cpu"] else "yes",
        str(d.get("num_thread", 0) or "not set"), L["n_threads"] if L else "", str(d["num_ctx"] or "not set"),
        L["ctx"] if L else "", str(d["think_off"]), folder(label), str(len(runs)), where, size,
        d["gpu_mib_before"], first.get("gpu_mib_loaded", ""), first["file"], str(first["wall_s"]),
        str(first["load_s"]), str(first["prompt_tokens"]), str(first["prompt_s"]), str(first["out_tokens"]),
        str(first["out_s"]), first["done_reason"], str(len(warm)), str(warm[0]) if warm else "",
        str(warm[-1]) if warm else "", str(warm[len(warm) // 2]) if warm else "",
        str(got), str(need), str(late),
    ])

# the default-thread CPU run: console log plus service log (no result JSON was written)
log = (HERE / "results" / "qwen3vl30b_cpu.log").read_text()
m = re.search(r"COLD wall=([\d.]+)s load=([\d.]+)s img\+prompt=(\d+)tok/([\d.]+)s out=(\d+)tok", log)
L = next((x for x in launches if x["time"].strftime("%H:%M:%S") == "08:20:56"), None)
ps = re.search(r"ps: (\S+) \S+ (\d+ GB) (100% CPU) (\d+)", log)
rows.append([
    "qwen3vl30b_cpu (console log only; stopped after one picture)", "qwen3-vl:30b-a3b-instruct",
    "2026-09-20 08:20 (launch 08:20:56 in the service log)", "no (num_gpu 0)", "not set",
    L["n_threads"] if L else "", "not set", L["ctx"] if L else "", "False", "images", "1",
    ps.group(3) if ps else "", ps.group(2) if ps else "", "", "1040", "01_nebula_large.jpg",
    m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), "17.36 (service log eval time)", "stop",
    "0", "", "", "", "not recorded", "2", "1",
])

out = HERE / "derived"
out.mkdir(exist_ok=True)
with open(out / "runs.tsv", "w") as f:
    f.write("\t".join(cols) + "\n")
    for r in sorted(rows, key=lambda r: r[2]):
        f.write("\t".join(r) + "\n")
with open(out / "strings_by_picture.tsv", "w") as f:
    f.write("label\tpicture\tfound\texpected\tmissed\n")
    for r in pic_rows:
        f.write("\t".join(r) + "\n")
print(f"runs.tsv: {len(rows)} rows; strings_by_picture.tsv: {len(pic_rows)} rows")
