#!/usr/bin/env python3
# A real use of a running server: a tool round-trip, then a conversation of follow-up turns with the history kept.
# Prints one line per turn and appends the replies to results/LABEL.usable.jsonl. usage: usable_ml4.py URL LABEL [max_tokens]
import json,sys,time,urllib.request
url,label=sys.argv[1],sys.argv[2]; MAX=int(sys.argv[3]) if len(sys.argv)>3 else 700
D='<REDACTED_PATH>/results'
TOOLS=[{'type':'function','function':{'name':'get_weather','description':'Current weather for a city.',
  'parameters':{'type':'object','properties':{'city':{'type':'string'}},'required':['city']}}}]
def turn(msgs,tag,tools=None):
    body={'messages':msgs,'max_tokens':MAX,'stream':True,'stream_options':{'include_usage':True},'cache_prompt':True}
    if tools: body['tools']=tools
    req=urllib.request.Request(url+'/v1/chat/completions',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
    t0=time.time(); first_any=first_word=None; reason=''; text=''; calls={}; finish=None; tim={}
    with urllib.request.urlopen(req,timeout=3000) as r:
        for line in r:
            line=line.strip()
            if not line.startswith(b'data: ') or line==b'data: [DONE]': continue
            d=json.loads(line[6:])
            if d.get('timings'): tim=d['timings']
            for c in d.get('choices') or []:
                de=c.get('delta') or {}
                if c.get('finish_reason'): finish=c['finish_reason']
                if de.get('reasoning_content'):
                    first_any=first_any or time.time(); reason+=de['reasoning_content']
                if de.get('content'):
                    first_any=first_any or time.time(); first_word=first_word or time.time(); text+=de['content']
                for tc in de.get('tool_calls') or []:
                    first_any=first_any or time.time(); first_word=first_word or time.time()
                    e=calls.setdefault(tc.get('index',0),{'id':'','name':'','args':''})
                    e['id']=tc.get('id') or e['id']
                    f=tc.get('function') or {}
                    e['name']=f.get('name') or e['name']; e['args']+=f.get('arguments') or ''
    row=dict(label=label,tag=tag,wall_s=round(time.time()-t0,1),first_token_s=round((first_any or t0)-t0,1),first_word_s=round((first_word or t0)-t0,1),
             read_n=tim.get('prompt_n'),read_tps=round(tim.get('prompt_per_second') or 0,1),gen_n=tim.get('predicted_n'),gen_tps=round(tim.get('predicted_per_second') or 0,2),
             finish=finish,text=text,reasoning=reason,calls=list(calls.values()))
    open(D+label+'.usable.jsonl','a').write(json.dumps(row)+'\n')
    print({k:v for k,v in row.items() if k not in('text','reasoning')},repr(text[:160]),flush=True)
    return row
m=[{'role':'user','content':'What is the weather in Lisbon right now? Use the tool.'}]
r=turn(m,'tool-call',TOOLS)
ok=bool(r['calls']) and r['calls'][0]['name']=='get_weather' and 'isbon' in r['calls'][0]['args']
print('tool call:', 'PASS' if ok else 'FAIL', r['calls'],flush=True)
if ok:
    c=r['calls'][0]
    m.append({'role':'assistant','content':'','tool_calls':[{'id':c['id'] or 'abc123def','type':'function','function':{'name':c['name'],'arguments':c['args']}}]})
    m.append({'role':'tool','tool_call_id':c['id'] or 'abc123def','name':c['name'],'content':'{"city":"Lisbon","temp_c":17,"sky":"light rain"}'})
    r=turn(m,'tool-answer',TOOLS)
    print('tool answer:', 'PASS' if '17' in r['text'] and 'rain' in r['text'].lower() else 'FAIL',flush=True)
    m.append({'role':'assistant','content':r['text']})
else:
    m=[]
for i,q in enumerate(['I have 12 liters of water and two jugs, 8 and 5 liters. How do I measure exactly 6 liters? Keep it short.',
                      'Now write a Python function that checks that a list of steps like yours really works.',
                      'What was the temperature I asked about earlier, and in which city?' if ok else 'Which two jug sizes did I give you?',
                      'Give me a one-paragraph summary of everything we discussed.']):
    m.append({'role':'user','content':q})
    r=turn(m,f'turn{i+1}')
    m.append({'role':'assistant','content':r['text']})
