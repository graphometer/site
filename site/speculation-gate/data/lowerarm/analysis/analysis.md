# mtpsweep analysis

- metric: `decode_rate_tps_primary` (higher_is_better)
- baseline treatment: `none`
- model_id: `qwen3.5-397b` · ctx_size: `65536` · temperature: `0.0` · max_tokens: `256`
- prompt manifest sha256: `cefb4f1af76554643f4a94caaffba3f0fc608e8c18240d7dc2a71a7423de0a86` (canonical: True)
- records: 114 loaded, 96 eligible for this metric

## Exclusions

| reason | n |
|---|---|
| role=warmup | 6 |
| role=calibration_pre | 6 |
| role=calibration_post | 6 |

## Cell census (eligible prompt×cycle cells per group)

| treatment | baseline cells | treatment cells | pairs | treatment cells with no baseline | baseline cells with no pair |
|---|---|---|---|---|---|
| `gate_0.10` | 32 | 32 | 32 | 0 | 0 |
| `gate_0.25` | 32 | 32 | 32 | 0 | 0 |

A baseline cell with no treatment partner contributes to `baseline cells` and to no pair. Any non-zero entry in the last two columns means the grid is incomplete -- most often a session that did not finish.

## PROSE — paired vs `none`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.10` | 16 | 11.04 | 7.56 | -32.04% | [-38.58%, -27.37%] |
| `gate_0.25` | 16 | 11.04 | 8.47 | -23.73% | [-27.92%, -20.09%] |

- `gate_0.10` distribution of % change: min -40.41, p25 -35.59, median -32.04, p75 -28.07, max -20.26 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.25` distribution of % change: min -29.33, p25 -25.98, median -23.73, p75 -20.69, max -5.14 (n=16)
  - interval position: excludes 0 = True; entirely above +10.0% = False; entirely below -10.0% = True
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## STRUCTURED — paired vs `none`

| treatment | n pairs | baseline median | treatment median | median % change | 95% cluster CI |
|---|---|---|---|---|---|
| `gate_0.10` | 16 | 11.40 | 11.63 | 1.22% | [-9.84%, 24.71%] |
| `gate_0.25` | 16 | 11.40 | 12.41 | 5.61% | [-4.43%, 25.03%] |

- `gate_0.10` distribution of % change: min -12.91, p25 -6.44, median 1.22, p75 17.47, max 45.26 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters
- `gate_0.25` distribution of % change: min -7.04, p25 -2.05, median 5.61, p75 22.90, max 49.40 (n=16)
  - interval position: excludes 0 = False; entirely above +10.0% = False; entirely below -10.0% = False
  - CI caveat: percentile method without BCa correction; approximate with few clusters

## POOLED (read the two subsets above first)

| treatment | n pairs | median % change | 95% cluster CI |
|---|---|---|---|
| `gate_0.10` | 32 | -16.58% | [-31.87%, -0.28%] |
| `gate_0.25` | 32 | -6.58% | [-23.10%, 4.74%] |

## Output equivalence vs baseline

Temperatures seen: [0.0] — falsifiable invariant

Eligibility: 96 measurement observations, 0 excluded from analysis and therefore absent from every rate below.

| treatment | subset | normalised exact match | byte-identical |
|---|---|---|---|
| `gate_0.10` | prose | 0/16 | 0/16 |
| `gate_0.10` | structured | 10/16 | 10/16 |
| `gate_0.10` | pooled | 10/32 | 10/32 |
| `gate_0.25` | prose | 0/16 | 0/16 |
| `gate_0.25` | structured | 12/16 | 12/16 |
| `gate_0.25` | pooled | 12/32 | 12/32 |

## Structured validator pass rates

| treatment | n eligible | excluded | strict | lenient (fence stripped) | fenced |
|---|---|---|---|---|---|
| `gate_0.10` | 16 | 0 | 16/16 | 16/16 | 0 |
| `gate_0.25` | 16 | 0 | 16/16 | 16/16 | 0 |
| `none` | 16 | 0 | 16/16 | 16/16 | 0 |

`excluded` observations are absent from both the numerator and the denominator: a transport failure is not a model failure. `n eligible` minus the denominator is the count of eligible observations whose validator could not run at all.

## Calibration drift (same fixed prompt, start vs end of session)

| treatment | cycle | pre | post | % change |
|---|---|---|---|---|
| `gate_0.10` | 1 | 8.31 | 8.09 | -2.70% |
| `gate_0.10` | 2 | 7.49 | 7.96 | 6.23% |
| `gate_0.25` | 1 | 7.99 | 7.86 | -1.55% |
| `gate_0.25` | 2 | 7.72 | 7.71 | -0.21% |
| `none` | 1 | 11.38 | 11.27 | -1.02% |
| `none` | 2 | 11.25 | 11.11 | -1.24% |

## Data quality by treatment

| treatment | n | failed | undefined rate | not chunked | coalesced reads | basis disagreement | hidden reasoning | truncated | spec counters | finish=length | model mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `gate_0.10` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 4 | 32 |
| `gate_0.25` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 1 | 32 |
| `none` | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 32 |
