# The Thunderbolt link, measured 2026-09-15

These files are the whole basis of the link figures in section 03 of the page. Nothing else on the page depends on
them, and no model server was running while they were taken.

## Method

- A direct Thunderbolt host-to-host cable between the desktop and the laptop. No switch, no router, no tunnel.
- `ping`, 30 packets, 0.2 s apart, desktop to laptop.
- A plain Python TCP socket test: `tcp_server.py` on the laptop, `tcp_client.py` on the desktop, one stream,
  1 MiB writes, 2 GB per run, two runs in each direction. Both connections were opened from the desktop.
- `iperf3` is installed on neither machine. These are therefore plain-socket numbers: **a lower bound on what the
  link carries, not a tuned benchmark.** A tuned multi-stream test would very likely read higher.
- The worker process on the laptop was idle, no model server was running on either machine, and the graphics card
  was not in use.

## Results, as the raw files report them

| reading | value |
|---|---|
| round trip, 30 packets | min 0.157 ms, avg 0.667 ms, max 0.820 ms, mdev 0.140 ms, 0% loss |
| desktop to laptop, run 1 | 2,093.9 MB/s sender, 2,092.5 MB/s receiver (16.75 / 16.74 Gbit/s) |
| desktop to laptop, run 2 | 2,120.3 MB/s sender, 2,117.0 MB/s receiver (16.96 / 16.94 Gbit/s) |
| laptop to desktop, run 1 | 1,106.5 MB/s receiver, 1,107.7 MB/s sender (8.85 / 8.86 Gbit/s) |
| laptop to desktop, run 2 | 1,109.5 MB/s receiver, 1,111.1 MB/s sender (8.88 / 8.89 Gbit/s) |

The page prints these as the bands 2,092 to 2,120 MB/s and 1,107 to 1,111 MB/s, which span both ends of both runs
in each direction. The direction asymmetry is roughly a factor of two and we did not chase it.

## Files

| file | what it is |
|---|---|
| `RUN_LOG.txt` | the whole session as it was recorded, in order |
| `ping.txt` | the ping summary |
| `tcp_up_run1.txt`, `tcp_up_run2.txt` | desktop to laptop, sender and receiver lines |
| `tcp_down_run1.txt`, `tcp_down_run2.txt` | laptop to desktop, sender and receiver lines |
| `tcp_client.py`, `tcp_server.py` | the two scripts, unmodified apart from the redaction below |

## Redactions

The two machines' addresses on the link are replaced with `<DESKTOP>` and `<LAPTOP>` everywhere they appear, and
the machines' internal short names are replaced with "desktop" and "laptop". Nothing that carries a measurement
was altered: every byte count, time and rate is as recorded.

If a number on the page disagrees with a file here, the file is right and the page is wrong.
