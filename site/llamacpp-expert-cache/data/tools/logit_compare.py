#!/usr/bin/env python3
"""Compare two logit_check.py results: greedy tokens the same, first parting token, and how far the top-5 probabilities moved while the two still agree. usage: logit_compare.py A B"""
import json,math,os,sys
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/results/'
a,b=[json.load(open(D+n+'.logits.json')) for n in sys.argv[1:3]]
same=tot=0;diffs=[];rows=[]
for x,y in zip(a,b):
    part=None;n=min(len(x['tokens']),len(y['tokens']))
    for i in range(n):
        tot+=1
        if x['tokens'][i][0]==y['tokens'][i][0]:
            same+=1
            if part is None:
                px=dict(x['tokens'][i][1]);py=dict(y['tokens'][i][1])
                for t in px:
                    if t in py:diffs.append(abs(math.exp(px[t])-math.exp(py[t])))
        elif part is None:part=i
    rows.append((x['prompt'][:34],part))
print(f'{sys.argv[1]} vs {sys.argv[2]}: {same} of {tot} greedy tokens the same; top-5 probability moved {sum(diffs)/max(len(diffs),1):.4f} on average, {max(diffs or [0]):.3f} at most, before each prompt parted')
for p,i in rows:print(f'  {p!r}: '+('same to the end' if i is None else f'parts at token {i}'))
