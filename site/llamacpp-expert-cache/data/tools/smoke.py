#!/usr/bin/env python3
"""Light smoke test for one llama-server on loopback: correctness, a short coding check, tool round trips, speed at depth, memory.
usage: smoke.py --url http://127.0.0.1:8144 --label NAME [--depths 2000,20000,100000] [--max-tokens 1500] [--think off|on|default] [--pid N]
Public filler only (llama.cpp source and docs). Writes smoke/results/NAME.json and prints a summary."""
import argparse,glob,json,os,re,subprocess,sys,tempfile,threading,time,urllib.request
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a=argparse.ArgumentParser();a.add_argument('--url',required=True);a.add_argument('--label',required=True)
a.add_argument('--depths',default='2000,20000,100000');a.add_argument('--max-tokens',type=int,default=1500)
a.add_argument('--think',default='default');a.add_argument('--pid',type=int);a.add_argument('--skip-quick',action='store_true')
a=a.parse_args()
def post(path,body,timeout=3600):
    r=urllib.request.Request(a.url+path,json.dumps(body).encode(),{'Content-Type':'application/json'})
    return json.load(urllib.request.urlopen(r,timeout=timeout))
def chat(msgs,tools=None,max_tokens=None,temperature=0.2,cache=True):
    b={'messages':msgs,'max_tokens':max_tokens or a.max_tokens,'temperature':temperature,'cache_prompt':cache}
    if tools:b['tools']=tools
    if a.think=='off':b['chat_template_kwargs']={'enable_thinking':False}
    if a.think=='on':b['chat_template_kwargs']={'enable_thinking':True}
    t=time.time();r=post('/v1/chat/completions',b);r['_wall']=time.time()-t;return r
peak={'gpu_mib':0,'avail_min_gib':1e9,'rss_max_gib':0};stop=False
def sampler():
    while not stop:
        try:
            g=int(subprocess.check_output(['nvidia-smi','--query-gpu=memory.used','--format=csv,noheader,nounits'],timeout=5).split()[0]);peak['gpu_mib']=max(peak['gpu_mib'],g)
            av=[int(l.split()[1]) for l in open('/proc/meminfo') if l.startswith('MemAvailable')][0]/2**20;peak['avail_min_gib']=min(peak['avail_min_gib'],av)
            if a.pid:
                rss=[int(l.split()[1]) for l in open(f'/proc/{a.pid}/status') if l.startswith('VmRSS')][0]/2**20;peak['rss_max_gib']=max(peak['rss_max_gib'],rss)
        except Exception:pass
        time.sleep(2)
threading.Thread(target=sampler,daemon=True).start()
R={'label':a.label,'url':a.url,'started':time.strftime('%F %T'),'quick':[],'tools':[],'depth':[]}
try:R['props']={k:v for k,v in post.__globals__['json'].load(urllib.request.urlopen(a.url+'/props',timeout=10)).items() if k in('default_generation_settings','total_slots','model_alias','model_path','build_info')}
except Exception as e:R['props']=str(e)
def text(r):
    m=r['choices'][0]['message'];return m.get('content') or ''
if not a.skip_quick:
    Q=[('17*23 as a plain number, nothing else.',r'\b391\b'),('Capital of Australia? One word.',r'Canberra'),('Which is larger, 9.11 or 9.9? Answer with the number only.',r'\b9\.9\b'),
       ('What does the Python standard library function itertools.frobnicate do? If it does not exist, say so plainly in one sentence.',r"(?i)(not exist|does ?n.t exist|no such|isn.t a|not a (real|standard)|no function|not part|there is no)")]
    for q,p in Q:
        r=chat([{'role':'user','content':q}]);t=text(r);R['quick'].append({'q':q,'ok':bool(re.search(p,t)),'a':t[:200],'finish':r['choices'][0]['finish_reason'],'timings':r.get('timings')})
    q='Write a Python function merge_intervals(intervals) that takes a list of [start,end] pairs in any order and returns the merged, sorted list; touching intervals such as [1,2],[2,3] merge. Return only one python code block.'
    r=chat([{'role':'user','content':q}]);t=text(r);m=re.search(r'```(?:python)?\n(.*?)```',t,re.S);code=m.group(1) if m else t
    test=code+"\nassert merge_intervals([[1,3],[2,6],[8,10],[15,18]])==[[1,6],[8,10],[15,18]]\nassert merge_intervals([[5,6],[1,2],[2,3]])==[[1,3],[5,6]]\nassert merge_intervals([])==[]\nassert merge_intervals([[1,10],[2,3]])==[[1,10]]\nprint('OK')\n"
    with tempfile.TemporaryDirectory() as d:
        open(d+'/c.py','w').write(test)
        try:p=subprocess.run([sys.executable,'-I','c.py'],cwd=d,capture_output=True,text=True,timeout=15);ok=p.stdout.strip()=='OK'
        except Exception:ok=False
    R['quick'].append({'q':'merge_intervals code runs against 4 asserts','ok':ok,'timings':r.get('timings')})
    tools=[{'type':'function','function':{'name':'get_stock','description':'Stock count for a SKU','parameters':{'type':'object','properties':{'sku':{'type':'string'}},'required':['sku']}}},
           {'type':'function','function':{'name':'add','description':'Add two integers','parameters':{'type':'object','properties':{'a':{'type':'integer'},'b':{'type':'integer'}},'required':['a','b']}}}]
    for i,(sku,n) in enumerate([('AX-11',41),('BX-22',17),('CX-33',903),('DX-44',6),('EX-55',288)]):
        m=[{'role':'user','content':f'How many units of SKU {sku} are in stock? Use the tool, then state the number.'}]
        rec={'sku':sku,'called':False,'args_ok':False,'final_ok':False}
        try:
            r=chat(m,tools);ms=r['choices'][0]['message'];tc=ms.get('tool_calls') or []
            if tc:
                rec['called']=tc[0]['function']['name']=='get_stock'
                rec['args_ok']=json.loads(tc[0]['function']['arguments']).get('sku')==sku
                m+=[ms,{'role':'tool','tool_call_id':tc[0].get('id','1'),'content':json.dumps({'sku':sku,'stock':n})}]
                r2=chat(m,tools);rec['final_ok']=str(n) in text(r2);rec['timings']=r2.get('timings')
        except Exception as e:rec['err']=str(e)[:300]
        R['tools'].append(rec)
files=sorted(glob.glob('<REDACTED_PATH>/*.cpp')+glob.glob('<REDACTED_PATH>/*.cpp')+glob.glob('<REDACTED_PATH>/*.md',recursive=True))
corpus=''.join(open(f,errors='replace').read() for f in files)
for depth in [int(x) for x in a.depths.split(',') if x]:
    ch=depth*3  # rough chars for this code-heavy text, then trim by token count
    body=corpus
    while len(body)<ch*2: body+=corpus
    n=len(post('/tokenize',{'content':body[:ch]})['tokens']);cut=int(ch*depth/n);body=body[:cut]
    codes=[f'{w}-{1000+7*depth%8999+i}' for i,w in enumerate(['HERON','QUARTZ','MAPLE'])]
    parts=[body[:cut//10],f'\n\n[SEALED NOTE ONE: the code is {codes[0]}.]\n\n',body[cut//10:cut//2],f'\n\n[SEALED NOTE TWO: the code is {codes[1]}.]\n\n',body[cut//2:cut*9//10],f'\n\n[SEALED NOTE THREE: the code is {codes[2]}.]\n\n',body[cut*9//10:]]
    msg=[{'role':'user','content':'Below is a long text with three sealed notes hidden in it.\n\n'+''.join(parts)+'\n\nQuote the three sealed codes in order, one per line, then in one or two sentences say what kind of text this is.'}]
    r=chat(msg,max_tokens=max(a.max_tokens,400),cache=False,temperature=0.2);t=text(r)
    d={'depth':depth,'prompt_n':r['timings'].get('prompt_n'),'read_tps':round(r['timings'].get('prompt_per_second',0),1),'read_s':round(r['timings'].get('prompt_ms',0)/1000,1),'gen_tps':round(r['timings'].get('predicted_per_second',0),1),'gen_n':r['timings'].get('predicted_n'),'codes':sum(c in t for c in codes),'finish':r['choices'][0]['finish_reason'],'a':t[:300]}
    # second turn: speaking speed with the cache in place
    msg+=[{'role':'assistant','content':t},{'role':'user','content':'Now write about 200 words on how a hash table works.'}]
    r=chat(msg,max_tokens=max(a.max_tokens,500),temperature=0.7);d['next_read_s']=round(r['timings'].get('prompt_ms',0)/1000,2);d['next_gen_tps']=round(r['timings'].get('predicted_per_second',0),1);d['next_gen_n']=r['timings'].get('predicted_n')
    R['depth'].append(d);print(json.dumps({k:v for k,v in d.items() if k!='a'}),flush=True)
stop=True;time.sleep(0.1);R['peak']=peak;R['ended']=time.strftime('%F %T')
os.makedirs(S+'/results',exist_ok=True);json.dump(R,open(f'{S}/results/{a.label}.json','w'),indent=1)
q=R['quick'];print(f"{a.label}: quick {sum(x['ok'] for x in q)}/{len(q)} | tools {sum(x['final_ok'] and x['args_ok'] for x in R['tools'])}/{len(R['tools'])} | peak card {peak['gpu_mib']} MiB, min available {peak['avail_min_gib']:.1f} GiB, RSS {peak['rss_max_gib']:.1f} GiB")
for x in q:
    if not x['ok']:print('  MISS:',x['q'][:60],'=>',str(x.get('a'))[:120])
