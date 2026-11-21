import re,sys,os
E=sys.argv[1]
def phases(f):
    d={}
    for l in open(f):
        k,v=l.split(); d[k]=float(v)
    return d
for run,ph,files in [('both','phases.txt',['ph_g.txt','ph_cf.txt']),('wired','w_ph.txt',['w_g.txt','w_cf.txt','w_c.txt']),('restart','r_ph.txt',['r_g.txt','r_cf.txt','r_c.txt','r_gw.txt'])]:
    P=phases(os.path.join(E,ph))
    for f in files:
        rows=[]
        for l in open(os.path.join(E,f)):
            m=re.match(r'\[(\d+\.\d+)\] .*icmp_seq=(\d+)',l)
            if m: rows.append((float(m.group(1)),int(m.group(2))))
        t0=rows[0][0]-(rows[0][1]-1)*0.25
        recv=set(s for _,s in rows); maxs=max(recv)
        # sent seq i at approx t0+(i-1)*0.25
        out=[]
        names=['idle1','upload','idle2','download','idle3']
        bounds=[P[n] for n in names]+[P['end']]
        # ping started at phase script start? assume t0 = phase zero
        for i,n in enumerate(names):
            a,b=bounds[i],bounds[i+1]
            seqs=[s for s in range(1,maxs+1) if a<= (s-1)*0.25 < b]
            lost=sum(1 for s in seqs if s not in recv)
            out.append(f'{n} {lost}/{len(seqs)} {100*lost/max(1,len(seqs)):.1f}%')
        print(run,f,'max',maxs,'recv',len(recv),' | '.join(out))
