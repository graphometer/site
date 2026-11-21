#!/usr/bin/env python3
# One timed question: server speeds, page faults, drive reads, busy cores on P, E and the Z13 during the call. Appends one line to results/LABEL.jsonl
import json,sys,time,urllib.request,subprocess
url,pid,label,tag,maxt=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5]); q=sys.argv[6]
def faults():
    f=open(f'/proc/{pid}/stat').read().rsplit(')',1)[1].split(); return int(f[9])
def preempt():
    import glob
    n=0
    for f in glob.glob(f'/proc/{pid}/task/*/status'):
        try:
            for l in open(f):
                if l.startswith('nonvoluntary_ctxt_switches'): n+=int(l.split()[1])
        except OSError: pass
    return n
def disk():
    for l in open('/proc/diskstats'):
        p=l.split()
        if p[2]=='nvme0n1': return int(p[5])*512
    return 0
def stat(text):
    r={}
    for l in text.splitlines():
        p=l.split()
        if p and p[0].startswith('cpu') and p[0]!='cpu':
            v=list(map(int,p[1:9])); r[int(p[0][3:])]=(sum(v),v[3]+v[4])
    return r
def busy(a,b,cs):
    return round(sum(1-((b[c][1]-a[c][1])/max(b[c][0]-a[c][0],1)) for c in cs),2)
def z():
    try: return stat(subprocess.run(['ssh','-o','ConnectTimeout=4','<LAPTOP>','cat /proc/stat'],capture_output=True,text=True,timeout=8).stdout)
    except Exception: return {}
m0=faults();d0=disk();c0=preempt();s0=stat(open('/proc/stat').read());z0=z();t0=time.time()
b=json.dumps({'model':'mistral-large-4','messages':[{'role':'user','content':q}],'max_tokens':maxt,'stream':False,'seed':7}).encode()
r=json.load(urllib.request.urlopen(urllib.request.Request(url+'/v1/chat/completions',b,{'Content-Type':'application/json'}),timeout=3400))
t=time.time()-t0;m1=faults();d1=disk();c1=preempt();s1=stat(open('/proc/stat').read());z1=z()
ms=r['choices'][0]['message'];ti=r.get('timings',{})
o={'label':label,'tag':tag,'wall_s':round(t,1),'read_n':ti.get('prompt_n'),'read_tps':round(ti.get('prompt_per_second') or 0,2),'gen_n':ti.get('predicted_n'),'gen_tps':round(ti.get('predicted_per_second') or 0,2),
   'major_faults':m1-m0,'drive_gb':round((d1-d0)/1e9,1),'preempt_per_s':round((c1-c0)/max(t,1),1),'P_busy':busy(s0,s1,range(8)),'E_busy':busy(s0,s1,range(8,24)),'Z_busy':busy(z0,z1,range(32)) if z0 and z1 else None,'finish':r['choices'][0].get('finish_reason')}
print(json.dumps(o))
o['reasoning']=ms.get('reasoning_content') or '';o['answer']=ms.get('content') or ''
open(f'<REDACTED_PATH>}.jsonl','a').write(json.dumps(o,ensure_ascii=False)+'\n')
