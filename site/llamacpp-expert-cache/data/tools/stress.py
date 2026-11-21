#!/usr/bin/env python3
"""Reads of exact token counts around batch boundaries, then random sizes. Fails on any error, crash or empty reply. From <REDACTED_PATH>/stress_ubatch.py, without its 120K read: the depth proofs cover that. usage: stress.py URL LABEL"""
import glob,json,random,sys,time,urllib.request
U,L=sys.argv[1],sys.argv[2]
def post(p,b,t=1800):
    return json.load(urllib.request.urlopen(urllib.request.Request(U+p,json.dumps(b).encode(),{'Content-Type':'application/json'}),timeout=t))
txt=''.join(open(f,errors='replace').read() for f in sorted(glob.glob('<REDACTED_PATH>/*.cpp')+glob.glob('<REDACTED_PATH>/*.cpp')))
ids=post('/tokenize',{'content':txt})['tokens']
while len(ids)<130000: ids=ids+ids
random.seed(31007)
sizes=[64,512,2047,2048,2049,3007,4095,4096,4097,8191,8192,8193,8194,12000,16383,16384,16385,24576,24577]
sizes+=[random.randint(300,30000) for _ in range(5)]
res=[];fail=0
for n in sizes:
    start=random.randint(0,len(ids)-n-1);t=time.time()
    try:
        r=post('/v1/completions',{'prompt':ids[start:start+n],'max_tokens':6,'temperature':0.2,'cache_prompt':False})
        ok=bool(r['choices'][0].get('text') or r['choices'][0].get('finish_reason'))
    except Exception as e:
        ok=False;r={'err':str(e)[:200]}
    fail+=not ok
    res.append({'n':n,'ok':ok,'s':round(time.time()-t,1),'rate':round((r.get('timings') or {}).get('prompt_per_second',0)),'err':r.get('err')})
    if not ok:print(json.dumps(res[-1]),flush=True);break
json.dump(res,open(f'<REDACTED_PATH>/{L}.stress.json','w'))
print(f'STRESS {L}: {len(res)-fail} of {len(sizes)} reads ok, {sum(x["s"] for x in res):.0f} s',flush=True)
