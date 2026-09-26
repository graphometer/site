if UBS != "skip":
    env[f"{PFX}_UBATCH"] = UBS; env[f"{PFX}_BATCH"] = str(max(int(UBS), 4096))
UB = int(UBS) if UBS != "skip" else None

def pick_len():
    ub = UB or 512
    u = rng.random()
    if u < 0.55: return rng.randint(max(300, ub // 2), ub + 64)          # one ubatch
    if u < 0.85: return rng.randint(ub + 65, 2 * ub + 600)               # two ubatches, remainder varies
    return rng.randint(300, 12000)
