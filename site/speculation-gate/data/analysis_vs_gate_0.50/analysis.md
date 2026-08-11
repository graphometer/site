# mtpsweep analysis

- metric: `decode_rate_tps_primary` (higher_is_better)
- baseline treatment: `gate_0.50`
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
| `gate_0.75` | 32 | 32 | 32 | 0 | 0 |
| `gate_0.90` | 32 | 32 | 32 | 0 | 0 |
| `none` | 32 | 32 | 32 | 0 | 0 |
| `ungated` | 32 | 32 | 32 | 0 | 0 |

A baseline cell with no treatment partner contributes to `baseline cells` and to no pair. Any non-zero entry in the last two columns means the grid is incomplete -- most often a session that did not finish.

## PROSE — paired vs `gate_0.50`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.75` | 16 | 12.06 | 12.35 | 2.17% | [-1.31%, 5.58%] |
| `gate_0.90` | 16 | 12.06 | 12.43 | 2.74% | [-2.11%, 6.66%] |
| `none` | 16 | 12.06 | 10.20 | -15.67% | [-20.79%, -11.14%] |
| `ungated` | 16 | 12.06 | 8.12 | -33.25% | [-37.87%, -27.90%] |

- `gate_0.75` distribution of % change: min -5.70, p25 -0.34, median 2.17, p75 3.95, max 12.43 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min -6.60, p25 0.75, median 2.74, p75 6.43, max 13.87 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `none` distribution of % change: min -24.42, p25 -17.79, median -15.67, p75 -14.30, max -6.81 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `ungated` distribution of % change: min -41.08, p25 -36.74, median -33.25, p75 -30.69, max -24.18 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## STRUCTURED — paired vs `gate_0.50`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.75` | 16 | 14.17 | 15.04 | 4.64% | [-3.42%, 12.25%] |
| `gate_0.90` | 16 | 14.17 | 15.25 | 8.85% | [-2.02%, 21.15%] |
| `none` | 16 | 14.17 | 10.25 | -27.75% | [-34.11%, -24.47%] |
| `ungated` | 16 | 14.17 | 12.69 | -13.02% | [-20.86%, 0.76%] |

- `gate_0.75` distribution of % change: min -19.69, p25 -2.32, median 4.64, p75 11.30, max 20.19 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.90` distribution of % change: min -14.53, p25 2.22, median 8.85, p75 15.63, max 28.97 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `none` distribution of % change: min -43.64, p25 -32.85, median -27.75, p75 -25.01, max -10.18 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `ungated` distribution of % change: min -27.96, p25 -19.86, median -13.02, p75 -0.18, max 9.39 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## POOLED (read the two subsets above first)

| treatment | n pairs | median % change | 95% cluster CI |
|---|---|---|---|
| `gate_0.75` | 32 | 3.00% | [-0.92%, 6.54%] |
| `gate_0.90` | 32 | 4.97% | [1.15%, 9.84%] |
| `none` | 32 | -22.89% | [-27.50%, -15.56%] |
| `ungated` | 32 | -24.49% | [-32.46%, -15.03%] |

## Output equivalence vs baseline

Temperatures seen: [0.0] — falsifiable invariant

Eligibility: 160 measurement observations, 0 excluded from analysis and therefore absent from every rate below.

| treatment | subset | normalised exact match | byte-identical |
|---|---|---|---|
| `gate_0.75` | prose | 0/16 | 0/16 |
| `gate_0.75` | structured | 12/16 | 12/16 |
| `gate_0.75` | pooled | 12/32 | 12/32 |
| `gate_0.90` | prose | 0/16 | 0/16 |
| `gate_0.90` | structured | 12/16 | 12/16 |
| `gate_0.90` | pooled | 12/32 | 12/32 |
| `none` | prose | 0/16 | 0/16 |
| `none` | structured | 10/16 | 10/16 |
| `none` | pooled | 10/32 | 10/32 |
| `ungated` | prose | 0/16 | 0/16 |
| `ungated` | structured | 16/16 | 16/16 |
| `ungated` | pooled | 16/32 | 16/32 |

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
