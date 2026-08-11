# mtpsweep analysis

- metric: `decode_rate_tps_primary` (higher_is_better)
- baseline treatment: `ungated`
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
| `none` | 32 | 32 | 32 | 0 | 0 |

A baseline cell with no treatment partner contributes to `baseline cells` and to no pair. Any non-zero entry in the last two columns means the grid is incomplete -- most often a session that did not finish.

## PROSE — paired vs `ungated`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 8.12 | 12.06 | 49.82% | [38.86%, 60.94%] |
| `gate_0.75` | 16 | 8.12 | 12.35 | 53.12% | [49.28%, 62.26%] |
| `gate_0.90` | 16 | 8.12 | 12.43 | 52.65% | [47.08%, 63.58%] |
| `none` | 16 | 8.12 | 10.20 | 24.67% | [21.80%, 32.74%] |

- `gate_0.50` distribution of % change: min 31.90, p25 44.29, median 49.82, p75 58.08, max 69.73 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.75` distribution of % change: min 32.07, p25 49.90, median 53.12, p75 57.06, max 76.70 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min 34.04, p25 49.52, median 52.65, p75 58.41, max 72.62 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `none` distribution of % change: min 9.16, p25 22.02, median 24.67, p75 29.22, max 41.87 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = True; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## STRUCTURED — paired vs `ungated`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.50` | 16 | 12.69 | 14.17 | 15.07% | [-0.75%, 26.36%] |
| `gate_0.75` | 16 | 12.69 | 15.04 | 18.03% | [4.35%, 25.82%] |
| `gate_0.90` | 16 | 12.69 | 15.25 | 21.92% | [7.29%, 36.13%] |
| `none` | 16 | 12.69 | 10.25 | -18.38% | [-29.55%, -7.04%] |

- `gate_0.50` distribution of % change: min -8.59, p25 0.18, median 15.07, p75 24.79, max 38.82 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.75` distribution of % change: min -4.48, p25 10.89, median 18.03, p75 23.78, max 49.56 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min 1.20, p25 14.24, median 21.92, p75 29.62, max 46.40 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `none` distribution of % change: min -41.88, p25 -25.34, median -18.38, p75 -10.53, max 0.52 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## POOLED (read the two subsets above first)

| treatment | n pairs | median % change | 95% cluster CI |
|---|---|---|---|
| `gate_0.50` | 32 | 32.44% | [18.02%, 48.06%] |
| `gate_0.75` | 32 | 36.18% | [18.03%, 53.12%] |
| `gate_0.90` | 32 | 45.02% | [22.37%, 51.62%] |
| `none` | 32 | 4.84% | [-16.37%, 24.32%] |

## Output equivalence vs baseline

Temperatures seen: [0.0] — falsifiable invariant

Eligibility: 160 measurement observations, 0 excluded from analysis and therefore absent from every rate below.

| treatment | subset | normalised exact match | byte-identical |
|---|---|---|---|
| `gate_0.50` | prose | 0/16 | 0/16 |
| `gate_0.50` | structured | 16/16 | 16/16 |
| `gate_0.50` | pooled | 16/32 | 16/32 |
| `gate_0.75` | prose | 0/16 | 0/16 |
| `gate_0.75` | structured | 12/16 | 12/16 |
| `gate_0.75` | pooled | 12/32 | 12/32 |
| `gate_0.90` | prose | 0/16 | 0/16 |
| `gate_0.90` | structured | 12/16 | 12/16 |
| `gate_0.90` | pooled | 12/32 | 12/32 |
| `none` | prose | 0/16 | 0/16 |
| `none` | structured | 10/16 | 10/16 |
| `none` | pooled | 10/32 | 10/32 |

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
