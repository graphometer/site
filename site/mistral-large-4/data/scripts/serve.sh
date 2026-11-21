#!/usr/bin/env bash
# Mistral Large 4 UD-IQ1_S on mainline b12015, loopback. Experts in RAM by default; extra flags go last and win.
export LD_LIBRARY_PATH=<REDACTED_PATH> GOMP_SPINCOUNT=10000000
exec taskset -c 0-7 <REDACTED_PATH> --model <REDACTED_PATH>/Mistral-Large-4-1T-A52B-UD-IQ1_S-00001-of-00006.gguf --alias mistral-large-4 --host 127.0.0.1 --port <PORT> \
  --n-gpu-layers 99 --load-mode mmap --lazy-mode on --parallel 1 --threads 8 --threads-batch 8 --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0 --jinja \
  --chat-template-kwargs '{"reasoning_effort":"low"}' --fit off "$@"
