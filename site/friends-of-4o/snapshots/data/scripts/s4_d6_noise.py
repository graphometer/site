"""Stage 4: the short banter set, where every prompt was run three times at each of two temperatures on each snapshot.

That gives a run-to-run band for each snapshot: take run 1, run 2 and run 3 of the same prompt at the same
temperature, average each run over the 20 prompt-and-temperature cells, and look at how far two runs of the SAME
snapshot sit apart. Then compare with how far run k of one snapshot sits from run k of another snapshot.
Writes tables/d6_run_bands.csv and tables/d6_snapshot_gaps.csv.
"""
import csv, itertools, os, statistics, sys, collections, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script folder from the path
from common import MEASURES, MKEYS, SNAPS, SHORT

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
args = ap.parse_args()
T = os.path.join(args.out, "tables")

rows = list(csv.DictReader(open(os.path.join(T, "d6_measures.csv"))))
NUM = [k for k in MKEYS if k != "i_per100"] + ["i_count", "words"]
for r in rows:
    r["cut"] = int(r["cut"]); r["run_index"] = int(r["run_index"]); r["prompt_id"] = int(r["prompt_id"]); r["temperature"] = float(r["temperature"])
    for k in NUM:
        r[k] = float(r[k])


def runset_values(rs, key, kind):
    if not rs:
        return None
    if kind == "rate":
        tw = sum(x["words"] for x in rs)
        return 100.0 * sum(x["i_count"] for x in rs) / tw if tw else 0.0
    return sum(x[key] for x in rs) / len(rs)


def run_level(snap, run, include_cut, cells=None):
    """mean over the replies of run `run` of snapshot `snap` (cell means first, then mean over cells)."""
    by_cell = collections.defaultdict(list)
    for r in rows:
        if r["snapshot"] == snap and r["run_index"] == run and (include_cut or not r["cut"]):
            by_cell[(r["prompt_id"], r["temperature"])].append(r)
    return by_cell


out_bands, out_gaps = [], []
meta = {}
for include_cut in (False, True):
    tag = "cuts_honored" if not include_cut else "truncated_replies_kept"
    runs = {s: {k: run_level(s, k, include_cut) for k in (1, 2, 3)} for s in SNAPS}
    meta[tag] = {s: sum(len(v) for k in (1, 2, 3) for v in runs[s][k].values()) for s in SNAPS}

    def pair_gap(sa, ka, sb, kb, key, kind):
        ca, cb = runs[sa][ka], runs[sb][kb]
        common = sorted(set(ca) & set(cb))
        if not common:
            return None, 0
        # one value per cell for each side, then the mean over the common cells
        if kind == "rate":
            ra = [x for c in common for x in ca[c]]
            rb = [x for c in common for x in cb[c]]
            return runset_values(rb, key, kind) - runset_values(ra, key, kind), len(common)
        va = statistics.mean(runset_values(ca[c], key, kind) for c in common)
        vb = statistics.mean(runset_values(cb[c], key, kind) for c in common)
        return vb - va, len(common)

    for key, label, kind in MEASURES:
        within = {}
        for s in SNAPS:
            g = []
            for ka, kb in itertools.combinations((1, 2, 3), 2):
                d, n = pair_gap(s, ka, s, kb, key, kind)
                if d is not None:
                    g.append(abs(d))
            within[s] = g
            out_bands.append({"basis": tag, "snapshot": s, "measure": key, "label": label, "n_run_pairs": len(g), "median_abs_gap": statistics.median(g), "max_abs_gap": max(g)})
        for sa, sb in [(SNAPS[0], SNAPS[1]), (SNAPS[1], SNAPS[2]), (SNAPS[0], SNAPS[2])]:
            btw = []
            for k in (1, 2, 3):
                d, n = pair_gap(sa, k, sb, k, key, kind)
                if d is not None:
                    btw.append(d)
            mean_btw = statistics.mean(btw)
            band_max = max(max(within[sa]), max(within[sb]))
            band_med = statistics.mean([statistics.median(within[sa]), statistics.median(within[sb])])
            same_sign = all(x > 0 for x in btw) or all(x < 0 for x in btw)
            smallest = min(abs(x) for x in btw)
            out_gaps.append({"basis": tag, "pair": f"{SHORT[sa]} -> {SHORT[sb]}", "measure": key, "label": label,
                             "mean_gap_between_snapshots": mean_btw, "gap_run1": btw[0], "gap_run2": btw[1], "gap_run3": btw[2],
                             "typical_run_to_run_gap": band_med, "largest_run_to_run_gap": band_max,
                             "between_over_typical": (abs(mean_btw) / band_med if band_med > 0 else float("inf")),
                             "all_three_between_gaps_same_sign": same_sign,
                             "smallest_between_gap_beats_largest_run_to_run_gap": bool(same_sign and smallest > band_max)})

with open(os.path.join(T, "d6_run_bands.csv"), "w", newline="") as fh:
    cols = ["basis", "snapshot", "measure", "label", "n_run_pairs", "median_abs_gap", "max_abs_gap"]
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader()
    for x in out_bands:
        w.writerow({c: (round(x[c], 6) if isinstance(x[c], float) else x[c]) for c in cols})
with open(os.path.join(T, "d6_snapshot_gaps.csv"), "w", newline="") as fh:
    cols = ["basis", "pair", "measure", "label", "mean_gap_between_snapshots", "gap_run1", "gap_run2", "gap_run3", "typical_run_to_run_gap", "largest_run_to_run_gap",
            "between_over_typical", "all_three_between_gaps_same_sign", "smallest_between_gap_beats_largest_run_to_run_gap"]
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader()
    for x in out_gaps:
        w.writerow({c: (round(x[c], 6) if isinstance(x[c], float) else x[c]) for c in cols})
json.dump(meta, open(os.path.join(T, "d6_meta.json"), "w"), indent=1)

# plain print of the cuts-honored table
for x in out_gaps:
    if x["basis"] == "cuts_honored":
        print(f"{x['pair']:22s}{x['measure']:14s} gap={x['mean_gap_between_snapshots']:8.3f} typical_noise={x['typical_run_to_run_gap']:7.3f} max_noise={x['largest_run_to_run_gap']:7.3f} x={x['between_over_typical']:6.1f} beats_max={x['smallest_between_gap_beats_largest_run_to_run_gap']}")
print(meta)

# ---- plain per-snapshot means for the banter set: only the prompt-and-temperature cells that survive on all three snapshots
with open(os.path.join(T, "d6_snapshot_means.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["basis", "measure", "label"] + [f"mean_{SHORT[s]}" for s in SNAPS] + ["cells_on_all_three", "replies_May", "replies_Aug", "replies_Nov"])
    for include_cut in (False, True):
        tag = "cuts_honored" if not include_cut else "truncated_replies_kept"
        cellmaps = {}
        for s in SNAPS:
            by_cell = collections.defaultdict(list)
            for r in rows:
                if r["snapshot"] == s and (include_cut or not r["cut"]):
                    by_cell[(r["prompt_id"], r["temperature"])].append(r)
            cellmaps[s] = by_cell
        common = sorted(set(cellmaps[SNAPS[0]]) & set(cellmaps[SNAPS[1]]) & set(cellmaps[SNAPS[2]]))
        for key, label, kind in MEASURES:
            vals = []
            for s in SNAPS:
                if kind == "rate":
                    allr = [x for c in common for x in cellmaps[s][c]]
                    vals.append(runset_values(allr, key, kind))
                else:
                    vals.append(statistics.mean(runset_values(cellmaps[s][c], key, kind) for c in common))
            w.writerow([tag, key, label] + [round(v, 4) for v in vals] + [len(common)] + [sum(len(cellmaps[s][c]) for c in common) for s in SNAPS])
