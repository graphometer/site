#!/usr/bin/env python3
"""Short speed screen of one running server: two prose runs, one code run, a long read with one sealed code, a next turn.
Counts hard page faults and drive reads for each step, so paging shows as numbers. Public text only.
usage: screen.py URL LABEL PID [--read 20000] [--reply 600]"""
import argparse,glob,json,os,subprocess,threading,time,urllib.request
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a=argparse.ArgumentParser();a.add_argument('url');a.add_argument('label');a.add_argument('pid',type=int);a.add_argument('--read',type=int,default=20000);a.add_argument('--reply',type=int,default=600)
a=a.parse_args()
def post(path,body):
    r=urllib.request.Request(a.url+path,json.dumps(body).encode(),{'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(r,timeout=5400))
def counters():
    st=open(f'/proc/{a.pid}/stat').read().rsplit(')',1)[1].split();maj=int(st[9])
    try:rb=int([l for l in open(f'/proc/{a.pid}/io') if l.startswith('read_bytes')][0].split()[1])
    except Exception:rb=0
    return maj,rb
peak={'gpu_mib':0,'avail_min_gib':1e9,'rss_max_gib':0,'swap_used_max_gib':0};stop=False
def sampler():
    while not stop:
        try:
            g=int(subprocess.check_output(['nvidia-smi','--query-gpu=memory.used','--format=csv,noheader,nounits'],timeout=5).split()[0]);peak['gpu_mib']=max(peak['gpu_mib'],g)
            m={l.split(':')[0]:int(l.split()[1]) for l in open('/proc/meminfo')}
            peak['avail_min_gib']=round(min(peak['avail_min_gib'],m['MemAvailable']/2**20),1);peak['swap_used_max_gib']=round(max(peak['swap_used_max_gib'],(m['SwapTotal']-m['SwapFree'])/2**20),1)
            peak['rss_max_gib']=round(max(peak['rss_max_gib'],[int(l.split()[1]) for l in open(f'/proc/{a.pid}/status') if l.startswith('VmRSS')][0]/2**20),1)
        except Exception:pass
        time.sleep(2)
threading.Thread(target=sampler,daemon=True).start()
R={'label':a.label,'started':time.strftime('%F %T'),'steps':[]}
try:R['props']={k:v for k,v in json.load(urllib.request.urlopen(a.url+'/props',timeout=10)).items() if k in('total_slots','model_alias','model_path','build_info')}
except Exception as e:R['props']=str(e)
def step(name,msgs,n,temp=0.15,cache=False):
    m0,b0=counters();t0=time.time()
    r=post('/v1/chat/completions',{'messages':msgs,'max_tokens':n,'temperature':temp,'top_p':1.0,'top_k':0,'seed':42,'cache_prompt':cache})
    m1,b1=counters();t=r['timings'];msg=r['choices'][0]['message']
    d={'step':name,'wall_s':round(time.time()-t0,1),'read_n':t.get('prompt_n'),'read_tps':round(t.get('prompt_per_second',0),1),'read_s':round(t.get('prompt_ms',0)/1000,1),'gen_n':t.get('predicted_n'),'gen_tps':round(t.get('predicted_per_second',0),2),
       'majflt':m1-m0,'drive_GB':round((b1-b0)/1e9,1),'finish':r['choices'][0]['finish_reason']}
    R['steps'].append(d);print(json.dumps(d),flush=True)
    return (msg.get('content') or ''),msg
Q='Write about 300 words on why tides happen, in plain flowing prose with no lists.'
step('prose1',[{'role':'user','content':Q}],420)
step('prose2',[{'role':'user','content':Q}],420)
src=open('<REDACTED_PATH>/convert_lora_to_gguf.py',errors='replace').read()[:9000]
step('code',[{'role':'user','content':'Rewrite the whole Python file below exactly as it is, adding only type hints to the function signatures. Output only the code.\n\n'+src}],700)
files=sorted(glob.glob('<REDACTED_PATH>/*.cpp')+glob.glob('<REDACTED_PATH>/*.cpp'))
corpus=''.join(open(f,errors='replace').read() for f in files)
ch=a.read*3;body=corpus
while len(body)<ch*2:body+=corpus
n=len(post('/tokenize',{'content':body[:ch]})['tokens']);cut=int(ch*a.read/n);body=body[:cut]
code=f'HERON-{1000+7*a.read%8999}'
msg=[{'role':'user','content':'Below is a long text with one sealed note hidden in it.\n\n'+body[:cut//2]+f'\n\n[SEALED NOTE: the code is {code}.]\n\n'+body[cut//2:]+'\n\nQuote the sealed code, then in one sentence say what kind of text this is.'}]
t,m=step('read',msg,a.reply,temp=0.2)
R['code_ok']=code in t
msg+=[{'role':'assistant','content':t},{'role':'user','content':'Now write about 200 words on how a hash table works.'}]
step('next',msg,300,temp=0.2,cache=True)
stop=True;time.sleep(0.1);R['peak']=peak;R['ended']=time.strftime('%F %T')
json.dump(R,open(f'{S}/results/{a.label}.screen.json','w'),indent=1)
s={x['step']:x for x in R['steps']}
print(f"{a.label}: prose {s['prose1']['gen_tps']} {s['prose2']['gen_tps']} code {s['code']['gen_tps']} | read {s['read']['read_n']} at {s['read']['read_tps']} ({s['read']['read_s']} s) code {'OK' if R['code_ok'] else 'MISS'} reply {s['read']['gen_tps']} | next {s['next']['read_s']} s, {s['next']['gen_tps']} | faults {sum(x['majflt'] for x in R['steps'])} drive {round(sum(x['drive_GB'] for x in R['steps']),1)} GB | card {peak['gpu_mib']} MiB RSS {peak['rss_max_gib']} GiB min avail {peak['avail_min_gib']} GiB swap {peak['swap_used_max_gib']} GiB")
