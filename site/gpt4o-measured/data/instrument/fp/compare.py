"""Compare — profiles on per-stimulus means, comparisons on the exact common stimulus set, units = the anchor's
run-split (generation-noise) p95, block-permutation p-values (Holm) per family. No single scalar."""
from __future__ import annotations
import statistics
from collections import defaultdict
from . import stats
from .features import FAMILIES, DISTANCE_EXCLUDE

MIN_STIMULI = 40

def build_profile(name: str, samples, scaler: stats.Scaler, n_splits: int = 200, kind: str = "batch") -> dict:
    rows = stats.feature_matrix(samples)
    groups = stats.by_stimulus(samples, rows)
    keys = list(scaler.center)
    means = stats.stimulus_means(groups, keys)
    prof = stats.profile_from_means(means, scaler)
    band_run = stats.run_split_band(groups, scaler, n_splits=n_splits)
    conv_of = {s.prompt_id: s.conv_id for s in samples}
    band_half = stats.split_half_band(groups, scaler, n_splits=n_splits, block_of=lambda pid: conv_of.get(pid, pid))
    by_cat = defaultdict(dict)
    for s in samples: by_cat[s.category or "all"][s.prompt_id] = means[s.prompt_id]
    raw_keys = sorted({k for r in rows for k in r})
    n_trunc = sum(1 for s in samples if (s.meta or {}).get("finish_reason") == "length")
    return {"name": name, "kind": kind, "n": len(samples), "n_groups": len(groups),
            "runs_per_stimulus": round(len(samples) / max(len(groups), 1), 2), "truncation_rate": round(n_trunc / max(len(samples), 1), 3),
            "models": sorted({s.model for s in samples}), "conditions": sorted({s.condition for s in samples}),
            "categories": sorted(by_cat), "mean": prof["mean"], "sd": prof["sd"],
            "band": band_run, "band_half": band_half,
            "stimulus_means": means,                                  # kept so comparisons can intersect exactly
            "stimulus_runs": {pid: [r for _, r in lst] for pid, lst in groups.items()},   # per-run rows, for bands on subsets
            "by_category": {c: stats.profile_from_means(m, scaler)["mean"] for c, m in by_cat.items() if len(m) >= 5},
            "raw_means": {k: statistics.mean(r.get(k, 0.0) for r in rows) for k in raw_keys}}

def compare(pa: dict, pb: dict, scaler: stats.Scaler | None = None, n_perm: int = 300) -> dict:
    """pa = anchor, pb = candidate. Distances on the COMMON stimuli only (same prompts, runs averaged)."""
    common = [pid for pid in pa["stimulus_means"] if pid in pb["stimulus_means"]]
    small = len(common) < MIN_STIMULI
    if scaler is None:
        scaler = stats.Scaler([{}]); scaler.center = {k: 0.0 for k in pa["mean"]}; scaler.scale = {k: 1.0 for k in pa["mean"]}
    A = {p: pa["stimulus_means"][p] for p in common}; B = {p: pb["stimulus_means"][p] for p in common}
    pA, pB = stats.profile_from_means(A, scaler), stats.profile_from_means(B, scaler)
    d = stats.family_distances(pA, pB) if common else {}
    # the anchor's generation-noise band recomputed on the COMMON stimuli (the comparison's own sample size)
    band = pa["band"]
    if pa.get("stimulus_runs") and common:
        sub = {pid: [(None, r) for r in pa["stimulus_runs"][pid]] for pid in common if pid in pa["stimulus_runs"]}
        b2 = stats.run_split_band(sub, scaler, n_splits=200)
        if all(b2[f]["p95"] == b2[f]["p95"] for f in b2): band = b2
    units, cand_units = {}, {}
    for fam in d:
        a95 = band.get(fam, {}).get("p95"); b95 = pb["band"].get(fam, {}).get("p95")
        units[fam] = (d[fam] / a95) if a95 and a95 == a95 and a95 > 0 else float("nan")
        cand_units[fam] = (d[fam] / b95) if b95 and b95 == b95 and b95 > 0 else float("nan")
    perm = stats.block_permutation_test(A, B, scaler, n_perm=n_perm) if (common and not small) else {}
    movers = stats.top_movers(pA, pB, 15) if common else []
    def verdict(f):
        if small: return "n/a (small common set)"
        u = units.get(f, float("nan")); p = perm.get(f, {}).get("p_holm", float("nan"))
        if u != u: return "n/a"
        sig = isinstance(p, float) and p == p and p < 0.05
        if u <= 1.0 and not sig: return "inside generation noise"
        if u <= 1.5 and not sig: return "at the edge of generation noise"
        if u <= 1.0: return "inside band but significant"
        return "beyond band" + (" (significant)" if sig else " (not significant)")
    return {"a": pa["name"], "b": pb["name"], "n_common_stimuli": len(common), "small_sample": small, "band_used": {f: band.get(f, {}).get("p95") for f in d},
            "truncation_rate_a": pa.get("truncation_rate", 0.0), "truncation_rate_b": pb.get("truncation_rate", 0.0),
            "family_distance": d, "band_units": units, "candidate_band_units": cand_units,
            "p_holm": {f: perm.get(f, {}).get("p_holm") for f in d}, "verdict_per_family": {f: verdict(f) for f in d},
            "top_movers": [{"feature": k, "a": round(x, 3), "b": round(y, 3), "delta": round(z, 3)} for k, x, y, z in movers]}

def render(cmp: dict) -> str:
    L = [f"## {cmp['a']} vs {cmp['b']} — {cmp['n_common_stimuli']} common stimuli", "",
         "| family | distance | ÷ anchor gen-noise p95 | ÷ candidate p95 | p (Holm) | reading |", "|---|---|---|---|---|---|"]
    for fam in FAMILIES:
        if fam in cmp["family_distance"]:
            p = cmp["p_holm"].get(fam); ps = f"{p:.3f}" if isinstance(p, float) else "–"
            L.append(f"| {fam} | {cmp['family_distance'][fam]:.3f} | {cmp['band_units'][fam]:.2f} | {cmp['candidate_band_units'][fam]:.2f} | {ps} | {cmp['verdict_per_family'][fam]} |")
    L += ["", "Biggest movers (standardised per-stimulus means, b − a):", ""]
    for m in cmp["top_movers"][:10]: L.append(f"- `{m['feature']}` {m['a']:+.2f} → {m['b']:+.2f} (Δ {m['delta']:+.2f})")
    return "\n".join(L)
