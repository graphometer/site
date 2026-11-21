#!/usr/bin/env python3
# How long the target takes to decode one batch of n tokens, which sets what guessing ahead can gain. usage: batch_scan.py URL LABEL
import json,statistics,sys,urllib.request
url,label=sys.argv[1],sys.argv[2]
def post(path,body):
    r=urllib.request.Request(url+path,data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(r,timeout=1800))
toks=post('/tokenize',{'content':open('/usr/share/common-licenses/GPL-3').read()})['tokens']
pos=100; out={}
for n in (1,2,4,8,16,32,64,128,256):
    ms=[]
    for rep in range(4):
        d=post('/completion',{'prompt':toks[pos:pos+n],'n_predict':1,'cache_prompt':False,'temperature':0})
        pos+=n+7; t=d['timings']; ms.append(t['prompt_ms'])
    out[n]=round(statistics.median(ms[1:]),1)
    print(f'{label} batch {n}: {out[n]} ms, {out[n]/n:.1f} ms per token, all {[round(x) for x in ms]}',flush=True)
open(f'<REDACTED_PATH>}.batch.json','w').write(json.dumps(out))
