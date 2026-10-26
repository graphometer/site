"""Stage 3: paired statistics from the derived tables written by stage 2 (no reply text is read here).

Unit: one scripted conversation, run once on each of the three snapshots. A conversation's value is the mean over its
model replies (or, for the rate measure, total count over total words). Pairs: conversations present on both
snapshots with no cut. Intervals: bootstrap over conversations. p-values: random sign flips of the paired differences
(the null that the snapshots are interchangeable), Holm-adjusted across the measures. dz = mean difference divided by
the standard deviation of the paired differences.
"""
import csv, json, math, os, random, statistics, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
from common import MEASURES, MKEYS, SNAPS, SHORT, LANE_NAME

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
ap.add_argument("--boot", type=int, default=5000)
ap.add_argument("--perm", type=int, default=5000)
args = ap.parse_args()
out = args.out
T = os.path.join(out, "tables")
SEED = 20261025

PAIRS = [(SNAPS[0], SNAPS[1]), (SNAPS[1], SNAPS[2]), (SNAPS[0], SNAPS[2])]
NUM = [k for k in MKEYS if k != "i_per100"] + ["i_count"]

rows = list(csv.DictReader(open(os.path.join(T, "reply_measures.csv"))))
for r in rows:
    r["turn_no"] = int(r["turn_no"]); r["cut"] = int(r["cut"])
    for k in NUM + ["words", "tokens_out"]:
        r[k] = float(r[k])

# ---------------------------------------------------------------- conversation-level values
convs = collections.defaultdict(list)
for r in rows:
    if r["cut"]:
        continue
    convs[(r["snapshot"], r["lane"], r["variant"], r["scenario_id"])].append(r)


def conv_value(rs, key, kind):
    if kind == "rate":
        tw = sum(x["words"] for x in rs)
        return 100.0 * sum(x["i_count"] for x in rs) / tw if tw else 0.0
    return sum(x[key] for x in rs) / len(rs)


val = {}   # (snap, lane, var, sid) -> {measure: value}
for k, rs in convs.items():
    val[k] = {key: conv_value(rs, key, kind) for key, _, kind in MEASURES}
keys_all = sorted({k[1:] for k in val})
complete = [k for k in keys_all if all((s,) + k in val for s in SNAPS)]

# first-reply values (turn 1) per conversation
first = {}
for r in rows:
    if r["cut"] or r["turn_no"] != 1:
        continue
    first[(r["snapshot"],) + (r["lane"], r["variant"], r["scenario_id"])] = {key: (100.0 * r["i_count"] / r["words"] if (kind == "rate" and r["words"]) else (0.0 if kind == "rate" else r[key])) for key, _, kind in MEASURES}


def phi(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


def paired(d, rng, boot, perm):
    n = len(d)
    mean = sum(d) / n
    sd = statistics.pstdev(d) * math.sqrt(n / (n - 1)) if n > 1 else 0.0
    dz = mean / sd if sd > 0 else 0.0
    bs = []
    idx = range(n)
    for _ in range(boot):
        s = 0.0
        for i in rng.choices(idx, k=n):
            s += d[i]
        bs.append(s / n)
    bs.sort()
    lo, hi = bs[int(0.025 * boot)], bs[int(0.975 * boot) - 1]
    ge = 0
    am = abs(mean)
    for _ in range(perm):
        bits = rng.getrandbits(n)
        s = 0.0
        for i in idx:
            s += d[i] if (bits >> i) & 1 else -d[i]
        if abs(s / n) >= am - 1e-12:
            ge += 1
    p = (ge + 1) / (perm + 1)
    z = mean / (sd / math.sqrt(n)) if sd > 0 else 0.0
    p_norm = 2 * phi(abs(z))
    return mean, lo, hi, dz, p, p_norm


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj = [0.0] * len(ps)
    run = 0.0
    m = len(ps)
    for rank, i in enumerate(order):
        run = max(run, min(1.0, (m - rank) * ps[i]))
        adj[i] = run
    return adj


rng = random.Random(SEED)
res = []
for (a, b) in PAIRS:
    block = []
    for key, label, kind in MEASURES:
        d = [val[(b,) + k][key] - val[(a,) + k][key] for k in complete]
        ma = statistics.mean(val[(a,) + k][key] for k in complete)
        mb = statistics.mean(val[(b,) + k][key] for k in complete)
        mean, lo, hi, dz, p, p_norm = paired(d, rng, args.boot, args.perm)
        share_b_higher = sum(1 for x in d if x > 0) / len(d)
        share_a_higher = sum(1 for x in d if x < 0) / len(d)
        # first reply only
        d1 = [first[(b,) + k][key] - first[(a,) + k][key] for k in complete if (b,) + k in first and (a,) + k in first]
        m1 = sum(d1) / len(d1)
        sd1 = statistics.stdev(d1)
        dz1 = m1 / sd1 if sd1 > 0 else 0.0
        z1 = m1 / (sd1 / math.sqrt(len(d1))) if sd1 > 0 else 0.0
        block.append({"pair": f"{SHORT[a]} -> {SHORT[b]}", "snapshot_A": a, "snapshot_B": b, "measure": key, "label": label, "n_pairs": len(d),
                      "mean_A": ma, "mean_B": mb, "diff_B_minus_A": mean, "ci95_lo": lo, "ci95_hi": hi, "dz": dz,
                      "ratio_B_over_A": (mb / ma if ma else float("nan")),
                      "share_pairs_B_higher": share_b_higher, "share_pairs_A_higher": share_a_higher,
                      "p_signflip": p, "p_normal": p_norm,
                      "first_reply_n": len(d1), "first_reply_diff": m1, "first_reply_dz": dz1, "first_reply_p_normal": 2 * phi(abs(z1)),
                      "first_reply_same_direction": (m1 > 0) == (mean > 0)})
    adj = holm([x["p_signflip"] for x in block])
    for x, ad in zip(block, adj):
        x["p_holm"] = ad
    res.extend(block)

cols = ["pair", "snapshot_A", "snapshot_B", "measure", "label", "n_pairs", "mean_A", "mean_B", "diff_B_minus_A", "ci95_lo", "ci95_hi", "dz", "ratio_B_over_A",
        "share_pairs_B_higher", "share_pairs_A_higher", "p_signflip", "p_holm", "p_normal", "first_reply_n", "first_reply_diff", "first_reply_dz", "first_reply_p_normal", "first_reply_same_direction"]
with open(os.path.join(T, "paired_differences.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    for x in res:
        w.writerow({c: (round(x[c], 6) if isinstance(x[c], float) else x[c]) for c in cols})

# ---------------------------------------------------------------- snapshot means (pooled, cut applied) and reply-level counts
with open(os.path.join(T, "snapshot_means.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["measure", "label"] + [f"mean_{SHORT[s]}" for s in SNAPS] + ["paired_conversations", "model_replies_per_snapshot"])
    nrep = len([r for r in rows if not r["cut"] and r["snapshot"] == SNAPS[0]])
    for key, label, kind in MEASURES:
        w.writerow([key, label] + [round(statistics.mean(val[(s,) + k][key] for k in complete), 6) for s in SNAPS] + [len(complete), nrep])

# reply-level means (each reply counts once) for plain-speech numbers
rl = {}
for s in SNAPS:
    rs = [r for r in rows if r["snapshot"] == s and not r["cut"]]
    rl[s] = {"replies": len(rs), "words_total": sum(r["words"] for r in rs)}
    for key, _, kind in MEASURES:
        if kind == "rate":
            rl[s][key] = 100.0 * sum(r["i_count"] for r in rs) / sum(r["words"] for r in rs)
        else:
            rl[s][key] = sum(r[key] for r in rs) / len(rs)
    ws = sorted(r["words"] for r in rs)
    rl[s]["words_median"] = statistics.median(ws)
    rl[s]["words_p10"] = ws[int(0.1 * len(ws))]
    rl[s]["words_p90"] = ws[int(0.9 * len(ws))]
    rl[s]["tokens_out_mean"] = sum(r["tokens_out"] for r in rs) / len(rs)
json.dump(rl, open(os.path.join(T, "reply_level_means.json"), "w"), indent=1)

# first replies only (the reply that sees nothing but the scripted opening message and the system prompt)
with open(os.path.join(T, "first_reply_means.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["measure", "label"] + [f"mean_{SHORT[s]}" for s in SNAPS] + ["first_replies_per_snapshot"])
    for key, label, kind in MEASURES:
        w.writerow([key, label] + [round(statistics.mean(first[(s,) + k][key] for k in complete), 6) for s in SNAPS] + [len(complete)])

# reply-weighted table (each reply counts once): the figures the page prints, with numerators and denominators
with open(os.path.join(T, "reply_level_table.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["measure", "label", "kind"] + sum([[f"value_{SHORT[s]}", f"numerator_{SHORT[s]}", f"denominator_{SHORT[s]}"] for s in SNAPS], []))
    for key, label, kind in MEASURES:
        row = [key, label, kind]
        for s in SNAPS:
            rs = [r for r in rows if r["snapshot"] == s and not r["cut"]]
            if kind == "rate":
                num = sum(r["i_count"] for r in rs); den = sum(r["words"] for r in rs); v = 100.0 * num / den
            else:
                num = sum(r[key] for r in rs); den = len(rs); v = num / den
            row += [round(v, 6), int(num), den]
        w.writerow(row)

# ---------------------------------------------------------------- by lane
with open(os.path.join(T, "by_lane.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    hdr = ["lane", "variant", "plain_name", "paired_conversations"]
    show = ["words", "questions", "list_items", "emdash", "has_emdash", "exclaim", "feeling_named"]
    for m in show:
        hdr += [f"{m}_{SHORT[s]}" for s in SNAPS]
    w.writerow(hdr)
    lane_keys = sorted({(k[0], k[1]) for k in complete})
    for lk in lane_keys:
        ks = [k for k in complete if (k[0], k[1]) == lk]
        row = [lk[0], lk[1], LANE_NAME[lk], len(ks)]
        for m in show:
            for s in SNAPS:
                row.append(round(statistics.mean(val[(s,) + k][m] for k in ks), 4))
        w.writerow(row)

# ordering by lane for a few measures
order_summary = {}
for m in ["words", "questions", "emdash", "list_items", "bold", "exclaim", "has_list"]:
    c = collections.Counter()
    lane_keys = sorted({(k[0], k[1]) for k in complete})
    for lk in lane_keys:
        ks = [k for k in complete if (k[0], k[1]) == lk]
        means = {s: statistics.mean(val[(s,) + k][m] for k in ks) for s in SNAPS}
        order = " > ".join(SHORT[s] for s in sorted(SNAPS, key=lambda s: -means[s]))
        c[order] += 1
    order_summary[m] = dict(c)
    order_summary[m]["_lanes"] = len(lane_keys)
json.dump(order_summary, open(os.path.join(T, "lane_ordering.json"), "w"), indent=1)

# ---------------------------------------------------------------- direction inside each lane group, and a sensitivity run without the other-language lane
lane_keys = sorted({(k[0], k[1]) for k in complete})
with open(os.path.join(T, "lane_direction.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["pair", "measure", "label", "lane_groups", "groups_B_higher", "groups_A_higher", "groups_equal"])
    for (a, b) in PAIRS:
        for key, label, kind in MEASURES:
            hi = lo = eq = 0
            for lk in lane_keys:
                ks = [k for k in complete if (k[0], k[1]) == lk]
                ma = statistics.mean(val[(a,) + k][key] for k in ks)
                mb = statistics.mean(val[(b,) + k][key] for k in ks)
                if abs(mb - ma) < 1e-9: eq += 1
                elif mb > ma: hi += 1
                else: lo += 1
            w.writerow([f"{SHORT[a]} -> {SHORT[b]}", key, label, len(lane_keys), hi, lo, eq])
sens = []
for (a, b) in PAIRS:
    for key in ["words", "sentences", "questions", "has_emdash", "emdash", "list_items"]:
        for tag, excl in [("all lanes", set()), ("without the other-language lane", {"d2"}), ("without the two longest-output lanes (writing together, practical task help)", {"creative", "vignette/task"})]:
            ks = [k for k in complete if k[0] not in excl and (k[0] + "/" + k[1]) not in excl]
            d = [val[(b,) + k][key] - val[(a,) + k][key] for k in ks]
            sd = statistics.stdev(d)
            sens.append([f"{SHORT[a]} -> {SHORT[b]}", key, tag, len(ks), round(statistics.mean(val[(a,) + k][key] for k in ks), 4), round(statistics.mean(val[(b,) + k][key] for k in ks), 4), round(statistics.mean(d), 4), round(statistics.mean(d) / sd, 3) if sd > 0 else 0.0])
with open(os.path.join(T, "sensitivity.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["pair", "measure", "subset", "paired_conversations", "mean_A", "mean_B", "diff_B_minus_A", "dz"])
    w.writerows(sens)

# ---------------------------------------------------------------- words by turn position
tp = collections.defaultdict(list)
for r in rows:
    if not r["cut"]:
        tp[(min(r["turn_no"], 6), r["snapshot"])].append(r["words"])
with open(os.path.join(T, "words_by_turn_position.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["turn_position (6 = sixth or later)"] + [f"mean_words_{SHORT[s]}" for s in SNAPS] + [f"replies_{SHORT[s]}" for s in SNAPS])
    for t in range(1, 7):
        w.writerow([t] + [round(statistics.mean(tp[(t, s)]), 2) for s in SNAPS] + [len(tp[(t, s)]) for s in SNAPS])

# ---------------------------------------------------------------- the 142 house features
hf = list(csv.DictReader(open(os.path.join(T, "house_features_by_conversation.csv"))))
fcols = [c for c in hf[0].keys() if c not in ("snapshot", "lane", "variant", "scenario_id")]
hv = {(r["snapshot"], r["lane"], r["variant"], r["scenario_id"]): {c: float(r[c]) for c in fcols} for r in hf}
cuts_keys = set(complete)
DIST_EXCL = {"shape.chars", "shape.log_words", "shape.sentences", "markup.list_items", "markup.headings", "markup.bold", "markup.code_fences",
             "tone.emoji_per_reply", "think.questions_back", "think.options_offered", "think.verdict_markers"}
used = [c for c in fcols if c not in DIST_EXCL]
hres = []
for (a, b) in PAIRS:
    block = []
    for c in fcols:
        d = [hv[(b,) + k][c] - hv[(a,) + k][c] for k in complete]
        n = len(d)
        mean = sum(d) / n
        sd = statistics.stdev(d)
        dz = mean / sd if sd > 0 else 0.0
        z = mean / (sd / math.sqrt(n)) if sd > 0 else 0.0
        block.append({"pair": f"{SHORT[a]} -> {SHORT[b]}", "feature": c, "family": c.split(".")[0], "in_distance_set": c in used, "n_pairs": n,
                      "mean_A": statistics.mean(hv[(a,) + k][c] for k in complete), "mean_B": statistics.mean(hv[(b,) + k][c] for k in complete),
                      "diff": mean, "dz": dz, "p_normal": 2 * phi(abs(z))})
    # Holm across the features in the distance set
    idx = [i for i, x in enumerate(block) if x["in_distance_set"]]
    adj = holm([block[i]["p_normal"] for i in idx])
    for i, ad in zip(idx, adj):
        block[i]["p_holm"] = ad
    for x in block:
        x.setdefault("p_holm", "")
        x["moves"] = bool(x["in_distance_set"] and x["p_holm"] != "" and x["p_holm"] < 0.01 and abs(x["dz"]) >= 0.3)
    hres.extend(block)
hcols = ["pair", "feature", "family", "in_distance_set", "n_pairs", "mean_A", "mean_B", "diff", "dz", "p_normal", "p_holm", "moves"]
with open(os.path.join(T, "house_feature_pairs.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=hcols)
    w.writeheader()
    for x in hres:
        w.writerow({c: (round(x[c], 6) if isinstance(x[c], float) else x[c]) for c in hcols})
summ = collections.defaultdict(lambda: collections.Counter())
for x in hres:
    if x["in_distance_set"]:
        summ[x["pair"]]["features"] += 1
        summ[x["pair"]][x["family"] + "_total"] += 1
        if x["moves"]:
            summ[x["pair"]]["moves"] += 1
            summ[x["pair"]][x["family"] + "_moves"] += 1
json.dump({k: dict(v) for k, v in summ.items()}, open(os.path.join(T, "house_feature_summary.json"), "w"), indent=1)

meta = {"seed": SEED, "bootstrap_resamples": args.boot, "sign_flip_permutations": args.perm, "paired_conversations": len(complete),
        "scripted_conversations_in_full_run": 354, "scripted_conversations_dropped_by_the_cut": 354 - len(complete), "model_replies_per_snapshot_used": sum(1 for r in rows if not r["cut"] and r["snapshot"] == SNAPS[0]),
        "conversations_per_snapshot_used": len(complete)}
json.dump(meta, open(os.path.join(T, "stats_meta.json"), "w"), indent=1)
print(meta)
