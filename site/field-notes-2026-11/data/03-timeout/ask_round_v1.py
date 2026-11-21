#!/usr/bin/env python3
# Quality round: the six questions to one server. Saves full answer, thinking and timings. usage: ask_round.py URL NAME MAX_TOKENS TIMEOUT [extra-json]
import json,sys,time,urllib.request
url,name,maxt,to=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
extra=json.loads(sys.argv[5]) if len(sys.argv)>5 else {}
base='<REDACTED_PATH>/quality'
for q in json.load(open(base+'/questions.json')):
    t0=time.time()
    b=dict(messages=[{'role':'user','content':q['q']}],max_tokens=maxt,stream=False,cache_prompt=False);b.update(extra)
    try:
        r=json.load(urllib.request.urlopen(urllib.request.Request(url+'/v1/chat/completions',json.dumps(b).encode(),{'Content-Type':'application/json'}),timeout=to))
        m=r['choices'][0]['message'];ti=r.get('timings',{})
        o=dict(id=q['id'],model=name,wall_s=round(time.time()-t0,1),gen_n=ti.get('predicted_n'),gen_tps=ti.get('predicted_per_second'),finish=r['choices'][0].get('finish_reason'),reasoning=m.get('reasoning_content') or '',answer=m.get('content') or '')
    except Exception as e:
        o=dict(id=q['id'],model=name,wall_s=round(time.time()-t0,1),error=str(e)[:200],answer='',reasoning='',finish='error')
    json.dump(o,open(f"{base}/answers/{name}-{q['id']}.json",'w'),ensure_ascii=False,indent=1)
    print(name,q['id'],o['wall_s'],'s',o.get('gen_n'),round(o.get('gen_tps') or 0,2),o['finish'],len(o['answer']),flush=True)
