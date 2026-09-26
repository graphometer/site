"""Stats — per-family standardised distances, noise bands, and block permutation tests.

Rules (review round 2026-09-03 + Codex code review):
  * the scaler is FROZEN on a declared calibration population (the anchor's bare batch), saved and versioned,
    never fitted on the candidates being compared;
  * profiles are built on PER-STIMULUS MEANS (runs averaged first) so a 3-run prompt does not outweigh a 2-run one;
  * distance per FAMILY (mean |Δ standardised mean| over the family's features, Burrows' Delta style); no scalar;
  * the primary noise band is the RUN-SPLIT band: at the SAME stimulus set, the distance between two disjoint
    run-assignments of the same source (generation noise at the comparison's own sample size); the split-half band
    (prompt-mix noise, half the sample) is kept as a secondary, wider reference;
  * significance = block permutation: condition labels swapped WITHIN matched stimuli, Holm-corrected across
    families; "same" is an equivalence reading (inside the run-split band AND no significant family), not a proof.
"""
from __future__ import annotations
import math, random, statistics
from collections import defaultdict
from .features import sample_features, family, FAMILIES, DISTANCE_EXCLUDE

def feature_matrix(samples) -> list[dict]:
    return [sample_features(s.text, s.prompt) for s in samples]

class Scaler:
    """Robust per-feature scaler (median / MAD) frozen on a calibration population."""
    def __init__(self, rows: list[dict]):
        keys = sorted({k for r in rows for k in r if k not in DISTANCE_EXCLUDE})
        self.center, self.scale = {}, {}
        for k in keys:
            v = [r.get(k, 0.0) for r in rows]
            med = statistics.median(v); mad = statistics.median(abs(x - med) for x in v) * 1.4826
            if mad < 1e-9:
                sd = statistics.pstdev(v) if len(v) > 1 else 0.0
                mad = sd if sd > 1e-9 else 1.0
            self.center[k], self.scale[k] = med, mad
    def z(self, row: dict) -> dict:
        return {k: (row.get(k, 0.0) - self.center[k]) / self.scale[k] for k in self.center}
    def to_dict(self): return {"center": self.center, "scale": self.scale}
    @classmethod
    def from_dict(cls, d):
        sc = cls([{}]); sc.center, sc.scale = dict(d["center"]), dict(d["scale"]); return sc

# ---------------------------------------------------------------- per-stimulus aggregation
def by_stimulus(samples, rows) -> dict[str, list[tuple[object, dict]]]:
    g = defaultdict(list)
    for s, r in zip(samples, rows): g[s.prompt_id].append((s, r))
    return g

def stimulus_means(groups: dict, keys) -> dict[str, dict]:
    """prompt_id -> mean feature row over its runs."""
    return {pid: {k: statistics.mean(r.get(k, 0.0) for _, r in lst) for k in keys} for pid, lst in groups.items()}

def profile_from_means(means: dict[str, dict], scaler: Scaler) -> dict:
    zs = [scaler.z(r) for r in means.values()]
    keys = list(scaler.center)
    if not zs: return {"n": 0, "mean": {k: 0.0 for k in keys}, "sd": {k: 0.0 for k in keys}}
    return {"n": len(zs), "mean": {k: statistics.mean(z[k] for z in zs) for k in keys},
            "sd": {k: (statistics.pstdev([z[k] for z in zs]) if len(zs) > 1 else 0.0) for k in keys}}

def family_distances(pa: dict, pb: dict) -> dict[str, float]:
    out = {}
    for fam in FAMILIES:
        ks = [k for k in pa["mean"] if family(k) == fam]
        if ks: out[fam] = statistics.mean(abs(pa["mean"][k] - pb["mean"][k]) for k in ks)
    return out

def top_movers(pa: dict, pb: dict, n: int = 12):
    d = [(k, pa["mean"][k], pb["mean"][k], pb["mean"][k] - pa["mean"][k]) for k in pa["mean"]]
    d.sort(key=lambda x: -abs(x[3])); return d[:n]

# ---------------------------------------------------------------- noise bands
def _pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(q * (len(v) - 1)))]

def run_split_band(groups: dict, scaler: Scaler, n_splits: int = 200, seed: int = 0) -> dict[str, dict]:
    """PRIMARY band. For each split, every stimulus with ≥2 runs assigns its runs randomly to side A or side B
    (at least one each); stimuli with one run are dropped for that split. Distance(A-profile, B-profile) is the
    same-source generation noise at (almost) the full stimulus count. Returns per family {median,p90,p95,n_splits,
    n_stimuli, mc_se95} (mc_se95 = bootstrap SE of the p95 over the splits — the Monte Carlo uncertainty)."""
    rng = random.Random(seed); keys = list(scaler.center)
    multi = {pid: lst for pid, lst in groups.items() if len(lst) >= 2}
    if len(multi) < 10:
        return {fam: {"median": float("nan"), "p90": float("nan"), "p95": float("nan"), "n_splits": 0, "n_stimuli": len(multi), "mc_se95": float("nan")} for fam in FAMILIES}
    dists = defaultdict(list)
    for _ in range(n_splits):
        ma, mb = {}, {}
        for pid, lst in multi.items():
            rows = [r for _, r in lst]; rng.shuffle(rows); cut = rng.randint(1, len(rows) - 1)
            ma[pid] = {k: statistics.mean(r.get(k, 0.0) for r in rows[:cut]) for k in keys}
            mb[pid] = {k: statistics.mean(r.get(k, 0.0) for r in rows[cut:]) for k in keys}
        for fam, d in family_distances(profile_from_means(ma, scaler), profile_from_means(mb, scaler)).items(): dists[fam].append(d)
    out = {}
    for fam, v in dists.items():
        boots = [_pct([rng.choice(v) for _ in v], 0.95) for _ in range(100)]
        out[fam] = {"median": statistics.median(v), "p90": _pct(v, 0.9), "p95": _pct(v, 0.95), "n_splits": len(v),
                    "n_stimuli": len(multi), "mc_se95": statistics.pstdev(boots)}
    return out

def split_half_band(groups: dict, scaler: Scaler, n_splits: int = 200, seed: int = 0, block_of=None) -> dict[str, dict]:
    """SECONDARY band: distance between two random halves of the stimuli (prompt-mix noise at HALF the sample).
    `block_of(pid)` maps a stimulus to a block (e.g. conversation id) so blocks never straddle halves."""
    rng = random.Random(seed); keys = list(scaler.center)
    means = stimulus_means(groups, keys)
    blocks = defaultdict(list)
    for pid in means: blocks[block_of(pid) if block_of else pid].append(pid)
    bkeys = list(blocks)
    if len(bkeys) < 6: return {fam: {"median": float("nan"), "p90": float("nan"), "p95": float("nan"), "n_splits": 0} for fam in FAMILIES}
    dists = defaultdict(list)
    for _ in range(n_splits):
        rng.shuffle(bkeys); h = len(bkeys) // 2
        a = {pid: means[pid] for b in bkeys[:h] for pid in blocks[b]}; bb = {pid: means[pid] for b in bkeys[h:] for pid in blocks[b]}
        for fam, d in family_distances(profile_from_means(a, scaler), profile_from_means(bb, scaler)).items(): dists[fam].append(d)
    return {fam: {"median": statistics.median(v), "p90": _pct(v, 0.9), "p95": _pct(v, 0.95), "n_splits": len(v)} for fam, v in dists.items()}

# ---------------------------------------------------------------- block permutation test
def holm(pvals: dict[str, float]) -> dict[str, float]:
    items = sorted(pvals.items(), key=lambda kv: kv[1]); m = len(items); out = {}; running = 0.0
    for i, (k, p) in enumerate(items):
        adj = min(1.0, (m - i) * p); running = max(running, adj); out[k] = running
    return out

def block_permutation_test(means_a: dict, means_b: dict, scaler: Scaler, n_perm: int = 500, seed: int = 0) -> dict[str, dict]:
    """Condition labels are swapped WITHIN each matched stimulus (present in both), so the null keeps the prompt
    structure. Returns per family: observed distance, raw p (plus-one), Holm-adjusted p."""
    rng = random.Random(seed)
    common = [pid for pid in means_a if pid in means_b]
    if len(common) < 10: return {}
    A = {pid: means_a[pid] for pid in common}; B = {pid: means_b[pid] for pid in common}
    obs = family_distances(profile_from_means(A, scaler), profile_from_means(B, scaler))
    ge = defaultdict(int)
    for _ in range(n_perm):
        pa, pb = {}, {}
        for pid in common:
            if rng.random() < 0.5: pa[pid], pb[pid] = A[pid], B[pid]
            else: pa[pid], pb[pid] = B[pid], A[pid]
        d = family_distances(profile_from_means(pa, scaler), profile_from_means(pb, scaler))
        for fam in obs:
            if d.get(fam, 0.0) >= obs[fam]: ge[fam] += 1
    raw = {fam: (ge[fam] + 1) / (n_perm + 1) for fam in obs}; adj = holm(raw)
    return {fam: {"distance": obs[fam], "p": raw[fam], "p_holm": adj[fam], "n_stimuli": len(common)} for fam in obs}
