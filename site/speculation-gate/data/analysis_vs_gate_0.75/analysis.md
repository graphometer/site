# mtpsweep analysis

- metric: `decode_rate_tps_primary` (higher_is_better)
- baseline treatment: `gate_0.75`
- model_id: `qwen3.5-397b` · ctx_size: `65536` · temperature: `0.0` · max_tokens: `256`
- prompt manifest sha256: `cefb4f1af76554643f4a94caaffba3f0fc608e8c18240d7dc2a71a7423de0a86` (canonical: True)
- records: 190 loaded, 160 eligible for this metric

## Exclusions

| reason | n |
|---|---|
| role=warmup | 10 |
| role=calibration_pre | 10 |
| role=calibration_post | 10 |

## Cell census (eligible prompt×cycle cells per group)

| treatment | baseline cells | treatment cells | pairs | treatment cells with no baseline | baseline cells with no pair |
|---|---|---|---|---|---|
| `gate_0.50` | 32 | 32 | 32 | 0 | 0 |
| `gate_0.90` | 32 | 32 | 32 | 0 | 0 |
| `none` | 32 | 32 | 32 | 0 | 0 |
| `ungated` | 32 | 32 | 32 | 0 | 0 |

A baseline cell with no treatment partner contributes to `baseline cells` and to no pair. Any non-zero entry in the last two columns means the grid is incomplete -- most often a session that did not finish.

## PROSE — paired vs `gate_0.75`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 12.35 | 12.06 | -2.12% | [-5.26%, 1.34%] |
| `gate_0.90` | 16 | 12.35 | 12.43 | 0.51% | [-2.40%, 3.03%] |
| `none` | 16 | 12.35 | 10.20 | -17.94% | [-21.26%, -15.62%] |
| `ungated` | 16 | 12.35 | 8.12 | -34.69% | [-38.27%, -33.01%] |

- `gate_0.50` distribution of % change: min -11.05, p25 -3.80, median -2.12, p75 0.34, max 6.04 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min -4.00, p25 -2.37, median 0.51, p75 2.32, max 5.89 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `none` distribution of % change: min -21.87, p25 -19.43, median -17.94, p75 -16.97, max -13.39 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `ungated` distribution of % change: min -43.41, p25 -36.32, median -34.69, p75 -33.29, max -24.28 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## STRUCTURED — paired vs `gate_0.75`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 15.04 | 14.17 | -4.43% | [-10.77%, 3.55%] |
| `gate_0.90` | 16 | 15.04 | 15.25 | 6.19% | [-2.27%, 8.65%] |
| `none` | 16 | 15.04 | 10.25 | -31.98% | [-37.23%, -21.20%] |
| `ungated` | 16 | 15.04 | 12.69 | -15.27% | [-20.50%, -3.69%] |

- `gate_0.50` distribution of % change: min -16.80, p25 -10.16, median -4.43, p75 2.38, max 24.52 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min -13.26, p25 -1.37, median 6.19, p75 7.53, max 20.48 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `none` distribution of % change: min -42.00, p25 -35.91, median -31.98, p75 -27.57, max -17.38 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `ungated` distribution of % change: min -33.14, p25 -19.21, median -15.27, p75 -9.81, max 4.69 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## POOLED (read the two subsets above first)

| treatment | n pairs | median % change | 95% cluster CI |
|---|---|---|---|
| `gate_0.50` | 32 | -2.91% | [-6.13%, 0.93%] |
| `gate_0.90` | 32 | 1.70% | [-2.27%, 6.19%] |
| `none` | 32 | -21.23% | [-31.20%, -17.27%] |
| `ungated` | 32 | -26.55% | [-34.69%, -15.14%] |

## Output equivalence vs baseline

Temperatures seen: [0.0] — falsifiable invariant

Eligibility: 160 measurement observations, 0 excluded from analysis and therefore absent from every rate below.

| treatment | subset | normalised exact match | byte-identical |
|---|---|---|---|
| `gate_0.50` | prose | 0/16 | 0/16 |
| `gate_0.50` | structured | 12/16 | 12/16 |
| `gate_0.50` | pooled | 12/32 | 12/32 |
| `gate_0.90` | prose | 0/16 | 0/16 |
| `gate_0.90` | structured | 16/16 | 16/16 |
| `gate_0.90` | pooled | 16/32 | 16/32 |
| `none` | prose | 0/16 | 0/16 |
| `none` | structured | 14/16 | 14/16 |
| `none` | pooled | 14/32 | 14/32 |
| `ungated` | prose | 0/16 | 0/16 |
| `ungated` | structured | 12/16 | 12/16 |
| `ungated` | pooled | 12/32 | 12/32 |

## Structured validator pass rates

| treatment | n eligible | excluded | strict | lenient (fence stripped) | fenced |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 0 | 16/16 | 16/16 | 0 |
| `gate_0.75` | 16 | 0 | 16/16 | 16/16 | 0 |
| `gate_0.90` | 16 | 0 | 16/16 | 16/16 | 0 |
| `none` | 16 | 0 | 16/16 | 16/16 | 0 |
| `ungated` | 16 | 0 | 16/16 | 16/16 | 0 |

`excluded` observations are absent from both the numerator and the denominator: a transport failure is not a model failure. `n eligible` minus the denominator is the count of eligible observations whose validator could not run at all.

## Calibration drift (same fixed prompt, start vs end of session)

| treatment | cycle | pre | post | % change |
|---|---|---|---|---|
| `gate_0.50` | 1 | 12.80 | 12.71 | -0.68% |
| `gate_0.50` | 2 | 12.83 | 12.78 | -0.39% |
| `gate_0.75` | 1 | 12.85 | 12.98 | 0.99% |
| `gate_0.75` | 2 | 12.87 | 12.93 | 0.44% |
| `gate_0.90` | 1 | 13.08 | 12.72 | -2.74% |
| `gate_0.90` | 2 | 13.02 | 12.95 | -0.55% |
| `none` | 1 | 9.73 | 10.35 | 6.35% |
| `none` | 2 | 10.44 | 10.23 | -2.01% |
| `ungated` | 1 | 8.09 | 8.34 | 3.03% |
| `ungated` | 2 | 8.26 | 9.08 | 9.98% |

## Data quality by treatment

| treatment | n | failed | undefined rate | not chunked | coalesced reads | basis disagreement | hidden reasoning | truncated | spec counters | finish=length | model mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `gate_0.50` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 2 | 32 |
| `gate_0.75` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 0 | 32 |
| `gate_0.90` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 2 | 32 |
| `none` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 32 |
| `ungated` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 4 | 32 |
