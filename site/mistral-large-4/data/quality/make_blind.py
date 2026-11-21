#!/usr/bin/env python3
# Blinds the finished answers for one judge: per question the contestants become A, B, C, D in a random order. The map stays outside the judge's folder.
import glob,json,os,random,re
T='<REDACTED_PATH>'; S='<REDACTED_PATH>'
J=S+'/judge/packet'; os.makedirs(J,exist_ok=True)
Q=json.load(open(T+'/questions.json')); names=['large4','large3','deepseek-v41-flash-ista','large4-3experts']
rng=random.SystemRandom(); M={}
for q in Q:
    order=names[:]; rng.shuffle(order); M[q['id']]={}
    lines=[f"# {q['id']}\n\n## Question\n\n{q['q']}\n"]
    for L,n in zip('ABCD',order):
        p=f"{T}/answers/{n}-{q['id']}.json"
        d=json.load(open(p)) if os.path.exists(p) else {}
        a=d.get('answer') or ''; f=d.get('finish')
        M[q['id']][L]=dict(model=n,gen_n=d.get('gen_n'),gen_tps=d.get('gen_tps'),finish=f,wall_s=d.get('wall_s'))
        lines.append(f"## Answer {L}\n\nFinish: {'complete' if f=='stop' else 'cut off or failed'}\n\n{a if a else '(no answer)'}\n")
    open(f"{J}/{q['id']}.md",'w').write('\n'.join(lines))
json.dump(M,open(S+'/judge-map.json','w'),indent=1)
print('blinded',len(Q),'questions')
