#!/usr/bin/env python3
"""THINKING OFF (chat_template_kwargs enable_thinking false), so short answers fit the token budget. Right or wrong, by machine, at the server's own sampling: the jug question 24 times, its steps followed by a small simulator, and eight short questions with one right answer, 5 seeds each. Near the start, then after about 97K tokens of public text.
Writes results/LABEL.qoff.json. usage: quality.py URL LABEL. With labels and no URL, quality.py --compare A B [C] judges the stored replies again and prints right answers side by side, and every wrong one."""
import glob,json,os,re,sys,urllib.request
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/runs/r3/results/'  # this package's layout
JUG='I have 12 liters of water and two jugs, 8 and 5 liters. How do I measure exactly 6 liters? Keep it short.'
Q=[('ball','A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost? Give only the amount.',r'(\b0?\.05\b|\b5 cents|\bfive cents)'),
   ('machines','If 5 machines take 5 minutes to make 5 widgets, how many minutes do 100 machines take to make 100 widgets? Give only the number.',r'(\D|^)5\D*$'),
   ('apples','I have 3 apples. I eat one, buy four more, then give half of what I have to a friend. How many apples do I have now? Give only the number.',r'(\D|^)3\D*$'),
   ('sum','What is 17 times 23, plus 19? Give only the number.',r'\b410\b'),
   ('sally','Sally has three brothers. Each brother has two sisters. How many sisters does Sally have? Give only the number.',r'(?i)^\D*\b1\b\D*$|\bone\b'),
   ('primes','List the prime numbers between 20 and 40, separated by commas, and nothing else.',r'^\D*23\D+29\D+31\D+37\D*$'),
   ('youngest','Alice is older than Bob. Carol is younger than Bob. Who is the youngest? One word.',r'(?i)\bcarol\b'),
   ('train','A train leaves at 14:40 and the trip takes 2 hours 35 minutes. When does it arrive? Give only the time as HH:MM.',r'\b17:15\b')]
def jug(t):
    """Follows the numbered steps and ignores what the model says about them. True, False, or None when a step cannot be read."""
    a={8:0,5:0};n=0
    for l in re.findall(r'(?m)^\s*(?:\*\*)?\d+\.\s*(?:\*\*)?(.+)$',t) or [x for x in t.splitlines() if x.strip()]:
        l=l.lower();w=re.match(r'[^a-z]*([a-z]+)',l);v=w.group(1) if w else ''
        s=[int(x) for x in re.findall(r'\b(8|5)\s*-?\s*(?:l\b|liter|litre)',l)]
        f=re.search(r'from (?:the )?(8|5)\s*-?\s*(?:l\b|liter|litre)',l);i=re.search(r'(?:in|on)?to (?:the )?(8|5)\s*-?\s*(?:l\b|liter|litre)',l)
        if v in('pour','transfer'):
            x=int(f.group(1)) if f else (s[0] if s else None);y=int(i.group(1)) if i else (s[1] if len(s)>1 else None)
            if not x or not y or x==y:return None
            m=min(a[x],y-a[y]);a[x]-=m;a[y]+=m;n+=1
        elif v in('fill',):
            if not s:return None
            a[s[0]]=s[0];n+=1
        elif v in('empty','dump','discard'):
            if not s:return None
            a[s[0]]=0;n+=1
    return (a[8]==6) if n else None
def jug2(t):
    """Second reader for the terse style Ornith writes with thinking off ('Pour 12→8', 'Fill 8', 'Empty 5'): three containers, the 12 holding 12 at the start, the 8 and 5 jugs empty.
    Used only when jug() cannot read the steps. Follows the steps and ignores what the model says about them. True, False, or None when a step cannot be read.
    After a restart marker ('let me redo', 'cleaner path', 'wait,') only the last attempt is followed."""
    t=t.replace('**','').replace('*','').lower()
    parts=re.split(r'let me redo|let me restart|redo cleanly|cleaner path|start over|\bwait,|\bhmm\b',t)
    t=parts[-1] if len(parts)>1 and re.search(r'(?m)^\s*\d+\.',parts[-1]) else t
    units=re.findall(r'(?m)^\s*\d+\.\s*(.+)$',t)
    if not units:return None
    cap={12:12,8:8,5:5};a={12:12,8:0,5:0};n=0
    num=r'(?:the\s+)?(12|8|5)\s*-?\s*(?:l\b|liters?|litres?)?(?:\s+jug)?'
    for u in units:
        u=u.strip()
        m=re.search(r'(?:pour|transfer)\s+(?:from\s+)?'+num+r'\s*(?:→|->|=>|into|to)\s*'+num,u)
        if m:
            x,y=int(m.group(1)),int(m.group(2))
            if x==y:return None
            mv=min(a[x],cap[y]-a[y]);a[x]-=mv;a[y]+=mv;n+=1;continue
        m=re.match(r'fill\s+'+num,u)
        if m:
            x=int(m.group(1))
            if x==12:return None
            mv=min(cap[x]-a[x],a[12]);a[12]-=mv;a[x]+=mv;n+=1;continue
        m=re.match(r'(?:empty|dump|discard)\s+'+num,u)
        if m:
            x=int(m.group(1))
            if x==12:return None
            a[12]+=a[x];a[x]=0;n+=1;continue
        return None
    return (6 in (a[8],a[12])) if n else None
RX={k:p for k,_,p in Q}
def judge(r):
    if r['q']=='jug':
        v=jug(r['a'])
        return v if v is not None else jug2(r['a'])
    return bool(re.search(RX[r['q']],r['a'].strip()))
if sys.argv[1]=='--compare':
    L=sys.argv[2:];R={n:json.load(open(D+n+'.qoff.json'))['rows'] for n in L}
    for rows in R.values():
        for r in rows:r['ok']=judge(r)
    keys=[]
    for r in R[L[0]]:
        k=(r['depth'],r['q'])
        if k not in keys:keys.append(k)
    print('depth q '+' '.join(L))
    tot={n:[0,0,0] for n in L}
    for k in keys:
        c=[]
        for n in L:
            x=[r for r in R[n] if (r['depth'],r['q'])==k]
            g=sum(r['ok'] is True for r in x);u=sum(r['ok'] is None for r in x);c.append(f'{g}/{len(x)}'+(f' ({u} unread)' if u else ''));tot[n][0]+=g;tot[n][1]+=len(x);tot[n][2]+=u
        print(k[0],k[1],*c)
    print('all',*[f'{n}: {t[0]} of {t[1]} right, {t[2]} the simulator could not read' for n,t in tot.items()])
    for n in L:print(n,'jug answers that say 2L is left in the 8L jug, right or not, near the start / at 97K:',*[sum(r['q']=='jug' and r['depth']==d and bool(re.search(r'\b2\s*L left in (?:the )?8L|\b8L (?:now )?has 2L',r['a'])) for r in R[n]) for d in ('start','97K')])
    for n in L:
        for r in R[n]:
            if r['ok'] is not True:print(f"-- {n} depth {r['depth']} {r['q']} seed {r['seed']} {'unread' if r['ok'] is None else 'WRONG'}: {r['a'][:300]!r}")
    sys.exit(0)
U,L=sys.argv[1:3]
def post(path,body):
    return json.load(urllib.request.urlopen(urllib.request.Request(U+path,json.dumps(body).encode(),{'Content-Type':'application/json'}),timeout=3600))
files=sorted(glob.glob('<REDACTED_PATH>/docs/**/*.md',recursive=True)+glob.glob('<REDACTED_PATH>/src/*.cpp'))
corpus=''.join(open(f,errors='replace').read() for f in files)
depth=97000;ch=depth*3;body=corpus
while len(body)<ch*2:body+=corpus
n=len(post('/tokenize',{'content':body[:ch]})['tokens']);body=body[:int(ch*depth/n)]
deep=[{'role':'user','content':'Here is some reading to keep beside us. No need to comment on it.\n\n'+body},{'role':'assistant','content':'Thank you. I have it beside me.'}]
rows=[]
for name,base in (('start',[]),('97K',deep)):
    for s in range(1,25):
        t=post('/v1/chat/completions',{'messages':base+[{'role':'user','content':JUG}],'max_tokens':320,'chat_template_kwargs':{'enable_thinking':False},'seed':s,'cache_prompt':True})['choices'][0]['message'].get('content') or ''
        rows.append({'depth':name,'q':'jug','seed':s,'ok':jug(t),'a':t})
    for key,q,p in Q:
        for s in range(1,6):
            t=post('/v1/chat/completions',{'messages':base+[{'role':'user','content':q}],'max_tokens':160,'chat_template_kwargs':{'enable_thinking':False},'seed':s,'cache_prompt':True})['choices'][0]['message'].get('content') or ''
            rows.append({'depth':name,'q':key,'seed':s,'ok':bool(re.search(p,t.strip())),'a':t})
json.dump({'label':L,'rows':rows},open(D+L+'.qoff.json','w'),indent=1)
print(f"{L}: {sum(r['ok'] is True for r in rows)} of {len(rows)} right, {sum(r['ok'] is None for r in rows)} the simulator could not read")
