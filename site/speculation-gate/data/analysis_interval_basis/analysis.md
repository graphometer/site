# mtpsweep analysis

- metric: `decode_rate_tps_interval_basis` (higher_is_better)
- baseline treatment: `none`
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
| `gate_0.75` | 32 | 32 | 32 | 0 | 0 |
| `gate_0.90` | 32 | 32 | 32 | 0 | 0 |
| `ungated` | 32 | 32 | 32 | 0 | 0 |

A baseline cell with no treatment partner contributes to `baseline cells` and to no pair. Any non-zero entry in the last two columns means the grid is incomplete -- most often a session that did not finish.

## PROSE — paired vs `none`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 10.16 | 12.01 | 18.58% | [12.55%, 26.42%] |
| `gate_0.75` | 16 | 10.16 | 12.30 | 21.85% | [18.46%, 27.02%] |
| `gate_0.90` | 16 | 10.16 | 12.38 | 22.79% | [19.15%, 25.12%] |
| `ungated` | 16 | 10.16 | 8.08 | -19.78% | [-24.65%, -17.87%] |

- `gate_0.50` distribution of % change: min 7.30, p25 16.68, median 18.58, p75 21.64, max 32.38 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.75` distribution of % change: min 15.48, p25 20.43, median 21.85, p75 24.11, max 28.04 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min 17.83, p25 19.99, median 22.79, p75 24.19, max 29.71 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `ungated` distribution of % change: min -29.51, p25 -22.60, median -19.78, p75 -18.04, max -8.38 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## STRUCTURED — paired vs `none`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 9.96 | 13.77 | 38.41% | [32.40%, 51.76%] |
| `gate_0.75` | 16 | 9.96 | 14.61 | 47.02% | [27.09%, 59.32%] |
| `gate_0.90` | 16 | 9.96 | 14.69 | 47.72% | [40.27%, 72.42%] |
| `ungated` | 16 | 9.96 | 12.10 | 22.53% | [7.57%, 41.94%] |

- `gate_0.50` distribution of % change: min 11.34, p25 33.35, median 38.41, p75 48.93, max 77.44 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.75` distribution of % change: min 21.04, p25 38.14, median 47.02, p75 56.05, max 72.40 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min 29.71, p25 43.43, median 47.72, p75 60.40, max 79.93 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `ungated` distribution of % change: min -0.51, p25 11.83, median 22.53, p75 34.09, max 72.06 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## POOLED (read the two subsets above first)

| treatment | n pairs | median % change | 95% cluster CI |
|---|---|---|---|
| `gate_0.50` | 32 | 29.72% | [18.40%, 37.94%] |
| `gate_0.75` | 32 | 26.97% | [20.88%, 45.37%] |
| `gate_0.90` | 32 | 29.71% | [21.43%, 46.46%] |
| `ungated` | 32 | -4.44% | [-19.55%, 19.62%] |

## Output equivalence vs baseline

Temperatures seen: [0.0] — falsifiable invariant

Eligibility: 160 measurement observations, 0 excluded from analysis and therefore absent from every rate below.

| treatment | subset | normalised exact match | byte-identical |
|---|---|---|---|
| `gate_0.50` | prose | 0/16 | 0/16 |
| `gate_0.50` | structured | 10/16 | 10/16 |
| `gate_0.50` | pooled | 10/32 | 10/32 |
| `gate_0.75` | prose | 0/16 | 0/16 |
| `gate_0.75` | structured | 14/16 | 14/16 |
| `gate_0.75` | pooled | 14/32 | 14/32 |
| `gate_0.90` | prose | 0/16 | 0/16 |
| `gate_0.90` | structured | 14/16 | 14/16 |
| `gate_0.90` | pooled | 14/32 | 14/32 |
| `ungated` | prose | 0/16 | 0/16 |
| `ungated` | structured | 10/16 | 10/16 |
| `ungated` | pooled | 10/32 | 10/32 |

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
| `gate_0.50` | 1 | 12.69 | 12.60 | -0.68% |
| `gate_0.50` | 2 | 12.72 | 12.67 | -0.39% |
| `gate_0.75` | 1 | 12.74 | 12.86 | 0.98% |
| `gate_0.75` | 2 | 12.76 | 12.81 | 0.42% |
| `gate_0.90` | 1 | 12.96 | 12.60 | -2.74% |
| `gate_0.90` | 2 | 12.91 | 12.84 | -0.55% |
| `none` | 1 | 9.64 | 10.25 | 6.35% |
| `none` | 2 | 10.34 | 10.13 | -2.01% |
| `ungated` | 1 | 8.02 | 8.26 | 3.03% |
| `ungated` | 2 | 8.18 | 9.00 | 9.98% |

## Data quality by treatment

| treatment | n | failed | undefined rate | not chunked | coalesced reads | basis disagreement | hidden reasoning | truncated | spec counters | finish=length | model mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `gate_0.50` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 2 | 32 |
| `gate_0.75` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 0 | 32 |
| `gate_0.90` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 2 | 32 |
| `none` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 32 |
| `ungated` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 4 | 32 |
