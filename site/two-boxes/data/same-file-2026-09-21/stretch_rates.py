#!/usr/bin/env python3
"""stretch_rates.py: tokens read per second over stretches of one long prompt, from llama-server's own
progress lines ("prompt processing, n_tokens = N, ..., t = S s"). Run it next to the two logs it names.
The stretches start and end on progress points present in both logs."""
import re

def points(fn):
    d = {0: 0.0}
    for line in open(fn):
        m = re.search(r'task 0 \| prompt processing, n_tokens =\s+(\d+), progress = [\d.]+, t =\s+([\d.]+) s', line)
        if m:
            d[int(m.group(1))] = float(m.group(2))
    return d

desk, pair = points('desktop-ub4096-150k.log'), points('pair-ub512-150k.log')
print('stretch of the 150,103-token prompt     desktop alone -ub 4096    the pair -ub 512')
for a, b in [(0, 4096), (40960, 49152), (90112, 98304), (139264, 143360)]:
    rd = (b - a) / (desk[b] - desk[a])
    rp = (b - a) / (pair[b] - pair[a])
    print(f'tokens {a:>7,} to {b:>7,}              {rd:10.1f}               {rp:10.1f}')
