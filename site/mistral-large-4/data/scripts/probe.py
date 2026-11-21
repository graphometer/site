#!/usr/bin/env python3
# One timed question to the trial server, with major page faults, drive reads and CPU use for the server during the call.
import json,sys,time,urllib.request,threading
url,pid,dev,label,maxt=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5])
q=sys.argv[6]
def st():
    f=open(f'/proc/{pid}/stat').read().rsplit(')',1)[1].split()
    return int(f[9]),int(f[11])+int(f[12])
def dk():
    for l in open('/proc/diskstats'):
        p=l.split()
        if p[2]==dev: return int(p[5])*512
    return 0
m0,c0=st();d0=dk();t0=time.time()
b=json.dumps({'model':'mistral-large-4','messages':[{'role':'user','content':q}],'max_tokens':maxt,'stream':False}).encode()
r=json.load(urllib.request.urlopen(urllib.request.Request(url+'/v1/chat/completions',b,{'Content-Type':'application/json'}),timeout=3000))
t=time.time()-t0;m1,c1=st();d1=dk()
ms=r['choices'][0]['message'];ti=r.get('timings',{})
out={'label':label,'wall_s':round(t,1),'prompt_n':ti.get('prompt_n'),'prompt_tps':ti.get('prompt_per_second'),'gen_n':ti.get('predicted_n'),'gen_tps':ti.get('predicted_per_second'),'major_faults':m1-m0,'drive_read_gb':round((d1-d0)/1e9,1),'cpu_cores_avg':round((c1-c0)/100/t,1),'reasoning':ms.get('reasoning_content','')[:600],'answer':ms.get('content','')[:900],'finish':r['choices'][0].get('finish_reason')}
print(json.dumps(out,ensure_ascii=False,indent=0));open(f"results/{label}.json",'w').write(json.dumps(out,ensure_ascii=False,indent=1))
