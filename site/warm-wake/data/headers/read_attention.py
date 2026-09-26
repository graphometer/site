#!/usr/bin/env python3
"""Read GGUF metadata only; never load tensors or start a model."""
import json
import struct
import sys
from pathlib import Path

def read_header(path):
    with open(path, 'rb') as f:
        def scalar(fmt):
            size=struct.calcsize('<'+fmt)
            return struct.unpack('<'+fmt, f.read(size))[0]
        def string():
            return f.read(scalar('Q')).decode('utf-8')
        def value(kind, keep=False):
            formats={0:'B',1:'b',2:'H',3:'h',4:'I',5:'i',6:'f',7:'?',10:'Q',11:'q',12:'d'}
            if kind in formats:
                return scalar(formats[kind])
            if kind==8:
                n=scalar('Q')
                if keep:return f.read(n).decode('utf-8')
                f.seek(n,1);return None
            if kind==9:
                elem=scalar('I');n=scalar('Q')
                for _ in range(n):value(elem)
                return None
            raise ValueError('Unsupported GGUF metadata type')
        assert f.read(4)==b'GGUF', 'Not a GGUF file'
        version=scalar('I');assert version in (2,3)
        scalar('Q');count=scalar('Q')
        found={}
        for _ in range(count):
            key=string();kind=scalar('I')
            keep=key=='general.architecture' or key.endswith('attention.sliding_window')
            val=value(kind,keep)
            if keep:found[key]=val
        return {'file':Path(path).name,'metadata_scanned':True,'fields':found,'sliding_window_present':any(k.endswith('attention.sliding_window') for k in found)}
if __name__=='__main__':
    print(json.dumps(read_header(sys.argv[1]),indent=2))
