#!/usr/bin/env python3
# Fixed prompts, greedy, top-5 probabilities of every token, so two server shapes can be compared number by number. usage: logit_check.py URL LABEL
import json,sys,urllib.request
url,label=sys.argv[1],sys.argv[2]
gpl=open('/usr/share/common-licenses/GPL-3').read()[:1800]
P=['The capital of Australia is','Explain in one paragraph why the sky is blue.\n\nAnswer:','def fibonacci(n):\n    """Return the n-th Fibonacci number."""\n',gpl+'\n\nThe license above is called']
out=[]
for p in P:
    b={'prompt':p,'n_predict':48,'temperature':0,'n_probs':5,'cache_prompt':False,'seed':7}
    r=json.load(urllib.request.urlopen(urllib.request.Request(url+'/completion',json.dumps(b).encode(),{'Content-Type':'application/json'}),timeout=900))
    out.append(dict(prompt=p[:60],tokens=[[c['token'],[(t['token'],t['logprob']) for t in c['top_logprobs']]] for c in r['completion_probabilities']]))
    print(label,repr(r['content'][:70]),flush=True)
json.dump(out,open(f'<REDACTED_PATH>}.logits.json','w'))
