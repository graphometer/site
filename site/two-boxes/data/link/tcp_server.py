import socket, sys, time
host, port, mode, total = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(float(sys.argv[4]))
s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.bind((host, port)); s.listen(1)
c, a = s.accept()
if mode == "sink":
    n = 0; t0 = None
    while True:
        d = c.recv(4 << 20)
        if not d: break
        if t0 is None: t0 = time.time()
        n += len(d)
    dt = time.time() - t0
    print(f"server sink: received {n} bytes in {dt:.3f} s = {n/dt/1e6:.1f} MB/s ({n*8/dt/1e9:.2f} Gbit/s) from {a[0]}")
else:
    buf = b"\0" * (1 << 20); sent = 0; t0 = time.time()
    while sent < total:
        c.sendall(buf); sent += len(buf)
    c.shutdown(socket.SHUT_WR); dt = time.time() - t0
    print(f"server source: sent {sent} bytes in {dt:.3f} s = {sent/dt/1e6:.1f} MB/s ({sent*8/dt/1e9:.2f} Gbit/s) to {a[0]}")
c.close(); s.close()
