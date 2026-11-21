#!/usr/bin/env python3
# DeepSeek V4.1 Flash 1017 GSQ-RCO IQ2_XXS + Engram, third attempt (2026-10-30). Replaces download_attempt2.sh: one curl per file
# ran about 2 MB/s a connection. Here each file is cut into 128 MiB pieces fetched by 16 workers; a finished piece is recorded in <name>.done,
# so a dropped connection costs one piece and a restart costs nothing. sha256 against the repo's LFS oid, then renamed.
import hashlib, os, sys, threading, time, urllib.request, queue
D = "<REDACTED_PATH>/DeepSeek-V4.1-Flash-1017-GSQ-RCO"
R = "ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF"
S = "<REDACTED_PATH>"
L = S + "/logs/download_log3.log"
PIECE = 128 << 20
WORKERS = 16


def log(msg):
    with open(L, "a") as f:
        f.write(time.strftime("%H:%M:%S ") + msg + "\n")


def fetch(url, start, end, fd):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}", "User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        if r.status != 206:
            raise RuntimeError(f"status {r.status}")
        pos = start
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            os.pwrite(fd, b, pos)
            pos += len(b)
    if pos != end + 1:
        raise RuntimeError(f"short read {pos} of {end + 1}")


def one(name, size, oid):
    final = f"{D}/{name}"
    if os.path.exists(final) and os.path.getsize(final) == size:
        log(f"have {name}")
        return True
    part, donef = final + ".part3", final + ".done"
    fd = os.open(part, os.O_RDWR | os.O_CREAT, 0o644)
    os.ftruncate(fd, size)
    done = set()
    if os.path.exists(donef):
        done = {int(x) for x in open(donef).read().split()}
    n = (size + PIECE - 1) // PIECE
    q = queue.Queue()
    for i in range(n):
        if i not in done:
            q.put(i)
    log(f"start {name}: {len(done)} of {n} pieces already here")
    url = f"https://huggingface.co/{R}/resolve/main/{name}"
    lock = threading.Lock()
    done_f = open(donef, "a")

    def work():
        while True:
            try:
                i = q.get_nowait()
            except queue.Empty:
                return
            start, end = i * PIECE, min((i + 1) * PIECE, size) - 1
            for attempt in range(1000):
                try:
                    fetch(url, start, end, fd)
                    break
                except Exception as e:
                    if attempt % 10 == 0:
                        log(f"{name} piece {i}: {type(e).__name__} {str(e)[:80]} (try {attempt + 1})")
                    time.sleep(min(5 + attempt * 5, 60))
            else:
                log(f"{name} piece {i}: gave up")
                return
            with lock:
                done_f.write(f"{i}\n")
                done_f.flush()
                done.add(i)
                if len(done) % 50 == 0:
                    log(f"{name}: {len(done)} of {n}")

    ts = [threading.Thread(target=work) for _ in range(WORKERS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    done_f.close()
    os.close(fd)
    if len(done) != n:
        log(f"BAD pieces {name}: {len(done)} of {n}")
        return False
    h = hashlib.sha256()
    with open(part, "rb") as f:
        for b in iter(lambda: f.read(1 << 24), b""):
            h.update(b)
    if h.hexdigest() != oid:
        log(f"BAD sha {name} {h.hexdigest()}")
        return False
    os.rename(part, final)
    os.unlink(donef)
    log(f"OK {name}")
    return True


ok = True
for line in open(S + "/expected-sha256.tsv"):
    name, size, oid = line.rstrip("\n").split("\t")
    ok = one(name, int(size), oid) and ok
link = f"{D}/DeepSeek-V4.1-Flash-1017-GSQ-RCO-IQ2_XXS-00006-of-00006.gguf"
if not os.path.islink(link):
    os.symlink("DeepSeek-V4.1-Flash-Engram-IQ4_NL.gguf", link)
log("SHA_ALL_OK" if ok else "SHA_FAILED")
log("DOWNLOAD_DONE")
