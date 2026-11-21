#!/usr/bin/env python3
"""Fixed speed and behaviour checks for one Small 4 server on loopback. Public text only.
usage: extra.py URL LABEL"""
import json,os,sys,urllib.request,urllib.error
url,label=sys.argv[1],sys.argv[2]
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def post(b):
    r=urllib.request.Request(url+'/v1/chat/completions',json.dumps(b).encode(),{'Content-Type':'application/json'})
    try:
        return 200,json.load(urllib.request.urlopen(r,timeout=1800))
    except urllib.error.HTTPError as e:
        return e.code,{'error':e.read().decode(errors='replace')[:300]}
def speed(name,q,n):
    runs=[]
    for i in range(2):
        c,r=post({'messages':[{'role':'user','content':q}],'max_tokens':n,'temperature':0.15,'top_p':1.0,'top_k':0,'seed':42,'cache_prompt':False})
        if c!=200:
            runs.append({'status':c,'err':r});continue
        t=r['timings'];x=r['choices'][0]['message'].get('content') or ''
        runs.append({'gen_n':t.get('predicted_n'),'gen_tps':round(t.get('predicted_per_second',0),2),'read_tps':round(t.get('prompt_per_second',0),1),'draft_n':t.get('draft_n'),'draft_ok':t.get('draft_n_accepted'),'finish':r['choices'][0]['finish_reason'],'text':x})
    return {'name':name,'runs':runs}
src=open('<REDACTED_PATH>/convert_lora_to_gguf.py',errors='replace').read()[:9000]
R={'label':label,'speed':[
 speed('prose','Write about 300 words on why tides happen, in plain flowing prose with no lists.',420),
 speed('code','Rewrite the whole Python file below exactly as it is, adding only type hints to the function signatures. Output only the code.\n\n'+src,1400)]}
c,r=post({'messages':[{'role':'user','content':'What is 17*23? Answer briefly.'}],'max_tokens':900,'temperature':0.7,'chat_template_kwargs':{'reasoning_effort':'high'}})
m=(r.get('choices') or [{}])[0].get('message',{})
R['reasoning']={'status':c,'has_reasoning':bool(m.get('reasoning_content')),'content_clean':'[THINK]' not in (m.get('content') or ''),'has_391':'391' in (m.get('content') or ''),'answer':(m.get('content') or '')[:400],'finish':(r.get('choices') or [{}])[0].get('finish_reason')}
c,r=post({'messages':[{'role':'user','content':'Hello.'},{'role':'user','content':'Say hi.'}],'max_tokens':16})
R['two_users_status']=c
c,r=post({'messages':[{'role':'user','content':'Hello.'},{'role':'assistant','content':'Hi.'},{'role':'system','content':'Note.'},{'role':'user','content':'Say hi.'}],'max_tokens':16})
R['late_system_status']=c
json.dump(R,open(f'{S}/results/{label}.extra.json','w'),indent=1)
for s in R['speed']:
    print(label,s['name'],[ (x.get('gen_tps'),x.get('draft_n'),x.get('draft_ok')) if 'gen_tps' in x else x for x in s['runs']])
print(label,{k:v for k,v in R.items() if k not in('speed','label')})
