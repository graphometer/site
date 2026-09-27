#!/usr/bin/env python3
"""Read GGUF metadata and tensor directories only, never tensor payloads.

Usage: python3 read_headers.py FILE.gguf [...] > header.json
No mmap, tensor library, network, model execution, or payload checksum.
Strings unrelated to architecture are consumed but not retained.
"""
import hashlib
import json
import math
import os
import struct
import sys

# GGML block element counts and stored bytes, including quantization scales.
TYPES = {
    0: ('F32',1,4), 1: ('F16',1,2), 2: ('Q4_0',32,18),
    3: ('Q4_1',32,20), 6: ('Q5_0',32,22), 7: ('Q5_1',32,24),
    8: ('Q8_0',32,34), 9: ('Q8_1',32,40), 10: ('Q2_K',256,84),
    11: ('Q3_K',256,110), 12: ('Q4_K',256,144), 13: ('Q5_K',256,176),
    14: ('Q6_K',256,210), 15: ('Q8_K',256,292), 16: ('IQ2_XXS',256,66),
    17: ('IQ2_XS',256,74), 18: ('IQ3_XXS',256,98), 19: ('IQ1_S',256,50),
    20: ('IQ4_NL',32,18), 21: ('IQ3_S',256,110), 22: ('IQ2_S',256,82),
    23: ('IQ4_XS',256,136), 24: ('I8',1,1), 25: ('I16',1,2),
    26: ('I32',1,4), 27: ('I64',1,8), 28: ('F64',1,8),
    29: ('IQ1_M',256,56), 30: ('BF16',1,2),
    39: ('MXFP4',32,17), 40: ('NVFP4',64,36),
}

def read_header(path):
    digest = hashlib.sha256()
    # Unbuffered so a header read cannot prefetch any weight bytes.
    with open(path, 'rb', buffering=0) as f:
        def read(n):
            if n < 0 or f.tell() + n > 64 * 1024 * 1024:
                raise ValueError('header safety limit')
            b = f.read(n)
            if len(b) != n:
                raise ValueError('short header')
            digest.update(b)
            return b
        def number(fmt):
            return struct.unpack('<' + fmt, read(struct.calcsize('<' + fmt)))[0]
        def string():
            return read(number('Q')).decode('utf-8')
        def value(kind, keep=True):
            if kind == 8:
                s = string()
                return s if keep else None
            if kind == 9:
                subtype, length = number('I'), number('Q')
                vals = []
                for _ in range(length):
                    v = value(subtype, keep)
                    if keep:
                        vals.append(v)
                return vals if keep else None
            fmt = {0:'B',1:'b',2:'H',3:'h',4:'I',5:'i',6:'f',7:'?',10:'Q',11:'q',12:'d'}[kind]
            v = number(fmt)
            return v if keep else None
        if read(4) != b'GGUF':
            raise ValueError('not GGUF')
        version, nt, nk = number('I'), number('Q'), number('Q')
        if version != 3:
            raise ValueError('expected GGUF v3')
        metadata = {}
        for _ in range(nk):
            key, kind = string(), number('I')
            keep = (key == 'general.architecture' or key == 'general.alignment'
                    or key.startswith('split.') or
                    (not key.startswith(('tokenizer.', 'general.')) and kind != 8))
            v = value(kind, keep)
            if keep:
                metadata[key] = v
        tensors = []
        for _ in range(nt):
            name = string()
            dims = [number('Q') for _ in range(number('I'))]
            kind, offset = number('I'), number('Q')
            label, block, size = TYPES[kind]
            assert dims[0] % block == 0
            nbytes = math.prod(dims) // block * size
            tensors.append(dict(name=name, dims=dims, type=label, type_id=kind,
                                offset=offset, bytes=nbytes))
        end = f.tell()
        alignment = metadata.get('general.alignment', 32)
        start = (end + alignment - 1) // alignment * alignment
        file_size = os.fstat(f.fileno()).st_size
        assert all(start + t['offset'] + t['bytes'] <= file_size for t in tensors)
    return dict(file=os.path.basename(path), file_size_bytes=file_size,
                header_bytes_read=end, tensor_data_offset=start,
                header_sha256=digest.hexdigest(), gguf_version=version,
                metadata=metadata, tensors=tensors)

if __name__ == '__main__':
    json.dump([read_header(p) for p in sys.argv[1:]], sys.stdout, indent=2)
    print()
