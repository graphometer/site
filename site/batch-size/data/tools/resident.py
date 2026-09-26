#!/usr/bin/env python3
"""resident.py FILE...: how much of each file sits in the page cache right now (mincore(2) via ctypes).
Prints one JSON line: {"t": ..., "files": {name: [resident_bytes, size]}, "resident_gb": ..., "size_gb": ...}.
Read-only: maps each file PROT_READ and asks the kernel which pages are resident; touches no page."""
import ctypes, ctypes.util, json, mmap, os, sys, time
libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
libc.mmap.restype = ctypes.c_void_p
libc.mmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_long]
libc.munmap.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
libc.mincore.argtypes = [ctypes.c_void_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_ubyte)]
PAGE = os.sysconf("SC_PAGE_SIZE")
out, tot_r, tot_s = {}, 0, 0
for path in sys.argv[1:]:
    size = os.path.getsize(path)
    fd = os.open(path, os.O_RDONLY)
    addr = libc.mmap(None, size, mmap.PROT_READ, mmap.MAP_SHARED, fd, 0)
    os.close(fd)
    if addr in (None, ctypes.c_void_p(-1).value):
        raise OSError(ctypes.get_errno(), "mmap failed")
    n = (size + PAGE - 1) // PAGE
    vec = (ctypes.c_ubyte * n)()
    if libc.mincore(ctypes.c_void_p(addr), size, vec) != 0:
        raise OSError(ctypes.get_errno(), "mincore failed")
    res = sum(1 for b in vec if b & 1) * PAGE
    libc.munmap(ctypes.c_void_p(addr), size)
    out[os.path.basename(path)] = [min(res, size), size]
    tot_r += min(res, size); tot_s += size
print(json.dumps({"t": time.strftime("%H:%M:%S"), "files": out,
                  "resident_gb": round(tot_r / 1e9, 2), "size_gb": round(tot_s / 1e9, 2)}))
