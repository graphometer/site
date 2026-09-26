import struct, sys, os, glob, re
T = {0:'B',1:'b',2:'H',3:'h',4:'I',5:'i',6:'f',7:'?',10:'Q',11:'q',12:'d'}
SZ = {0:1,1:1,2:2,3:2,4:4,5:4,6:4,7:1,10:8,11:8,12:8}
WANT = re.compile(r'(general\.(name|architecture|size_label)|context_length|block_count|head_count|key_length|value_length|sliding_window|rope\.scaling|rope\.freq_base|expert_count|expert_used_count|full_attention|kv_lora_rank|embedding_length|split\.count|swa|nextn)')
def rstr(f):
    n = struct.unpack('<Q', f.read(8))[0]; return f.read(n).decode('utf-8','replace')
def rval(f, t):
    if t == 8: return rstr(f)
    if t == 9:
        et = struct.unpack('<I', f.read(4))[0]; n = struct.unpack('<Q', f.read(8))[0]
        if et == 8:
            out=[]; 
            for _ in range(n):
                s=rstr(f)
                if len(out)<4: out.append(s)
            return ('arr-str', n)
        if et == 9: raise ValueError('nested')
        data = f.read(SZ[et]*n)
        if n <= 256: return list(struct.unpack('<'+T[et]*n, data))
        return ('arr', n)
    return struct.unpack('<'+T[t], f.read(SZ[t]))[0]
def dump(path):
    with open(path,'rb') as f:
        if f.read(4) != b'GGUF': print('  not gguf'); return
        ver = struct.unpack('<I', f.read(4))[0]; tc, kc = struct.unpack('<QQ', f.read(16))
        out={}
        for _ in range(kc):
            k = rstr(f); t = struct.unpack('<I', f.read(4))[0]; v = rval(f, t)
            if WANT.search(k): out[k]=v
    for k,v in out.items():
        if isinstance(v,list) and len(v)>8:
            nz=sum(1 for x in v if x); v=f"per-layer[{len(v)}] uniq={sorted(set(v))} nonzero={nz}"
        print(f"  {k} = {v}")
dirs = sys.argv[1:]
for d in dirs:
    fs = sorted(p for p in glob.glob(os.path.join(d,'**','*.gguf'), recursive=True)
                if not re.search(r'mmproj|draft|dflash|DSpark|dspark|imatrix', p, re.I))
    firsts = [p for p in fs if re.search(r'00001-of', p)] or fs
    print(f"=== {d}"); 
    if not firsts: print('  (no gguf)'); continue
    print(f"  file: {os.path.relpath(firsts[0], d)}")
    try: dump(firsts[0])
    except Exception as e: print('  ERR', e)
