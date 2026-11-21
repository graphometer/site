# Answer key for the six questions (judge sees this, never the model names)

Judge the final answer. An empty answer or a `length` finish counts as no answer.

- q1-logic: Mon Cho fish; Tue Ada hen; Wed Ben dog; Thu Dia cat; Fri Eno owl. Unique. Corrected 2026-11-01 by brute force after the judge flagged it: clues 5 and 6 are each redundant (the solution stays unique without either one); the other six are needed. The Q1 block in verify.py still holds an older clue set and gives 0 solutions; the final clues were checked by a separate script, so do not cite verify.py for Q1.
- q2-probability: stop at 4 = 49/216; stop at 9 = 46369/279936 (about 0.1656).
- q3-code: four issues. `s <` must be `s <=` (touching intervals). `out[-1][1] = e` must be `max(out[-1][1], e)` (a contained interval shrinks). An empty list raises IndexError. `sorted` is shallow, so `out` holds the caller's inner lists and mutates them (copy them).
- q4-statistics: A overall 171/200 = 85.5%, B 135/200 = 67.5%, but B is better in both groups: mild A 94.1% vs B 96.7%, severe A 36.7% vs B 62.4% (Simpson's paradox, case mix). The newspaper is wrong. Choose B for severe; B narrowly or no clear difference for mild. Limits: small samples (B mild 30, A severe 30), severity definitions, other confounders.
- q5-premise: the protocol is fabricated. A good answer says it cannot verify or know of it and does not invent provisions.
- q6-decision: nightly window 180 GB is at least the daily change of 120 GB, fine. Initial seed about 33 nights. Full restore of 6 TB at 300 Mbit/s = 44.4 h, over the 24 h limit, so cloud-only fails. Recommend a local copy or NAS plus cloud (hybrid), or a seeded/shipped restore. State assumptions.
