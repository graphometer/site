#!/usr/bin/env python3
"""Ask the kernel to drop one model's clean file pages from the page cache, so a mapped start is a true cold start. Read-only: nothing is written, no root needed.
usage: evict.py FIRST_SHARD_OR_FILE"""
import glob,os,re,sys
m=sys.argv[1];f=re.sub(r'-00001-of-(\d{5})\.gguf$',r'-*-of-\1.gguf',m)
files=sorted(glob.glob(f)) if f!=m else [m]
for p in files:
    fd=os.open(os.path.realpath(p),os.O_RDONLY);os.posix_fadvise(fd,0,0,os.POSIX_FADV_DONTNEED);os.close(fd)
print(f'evicted {len(files)} file(s)')
