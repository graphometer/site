import socket, sys, time
host, port, mode, total = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(float(sys.argv[4]))
s = socket.create_connection((host, port))
if mode == "send":
    buf = b"\0" * (1 << 20); sent = 0; t0 = time.time()
    while sent < total:
        s.sendall(buf); sent += len(buf)
    s.shutdown(socket.SHUT_WR); dt = time.time() - t0
    print(f"client send: sent {sent} bytes in {dt:.3f} s = {sent/dt/1e6:.1f} MB/s ({sent*8/dt/1e9:.2f} Gbit/s) to {host}")
else:
    n = 0; t0 = None
    while True:
        d = s.recv(4 << 20)
        if not d: break
        if t0 is None: t0 = time.time()
        n += len(d)
    dt = time.time() - t0
    print(f"client recv: received {n} bytes in {dt:.3f} s = {n/dt/1e6:.1f} MB/s ({n*8/dt/1e9:.2f} Gbit/s) from {host}")
s.close()
