#!/usr/bin/env bash
# Large 4 across the desktop and the Z13 over Thunderbolt RPC. Layers 0..GPU_FULL-1 whole on the 5090, then attention on the 5090 with experts in RAM up to DESKTOP_LAYERS-1, the rest whole on the Z13. Started by hand. Stop this server first, then the worker.
DESKTOP_LAYERS=${DESKTOP_LAYERS:-46}; GPU_FULL=${GPU_FULL:-6}; N_LAYERS=72; Z13=${Z13:-<LAPTOP>}
L=""; for ((i=GPU_FULL; i<DESKTOP_LAYERS; i++)); do L+="${L:+|}$i"; done
OT="blk\.($L)\.ffn_(up|down|gate)_exps=CPU,output\.weight=CUDA0"
export LD_LIBRARY_PATH=<REDACTED_PATH>/lib64 GOMP_SPINCOUNT=10000000
exec taskset -c 0-7 <REDACTED_PATH>/llama-server --model <REDACTED_PATH>/Mistral-Large-4-1T-A52B-UD-IQ1_S-00001-of-00006.gguf --alias mistral-large-4 --host 127.0.0.1 --port 8148 \
  --rpc "$Z13" --device CUDA0,RPC0 --tensor-split "$DESKTOP_LAYERS,$((N_LAYERS-DESKTOP_LAYERS))" --n-gpu-layers 999 --override-tensor "$OT" --no-warmup \
  --load-mode mmap --lazy-mode on --parallel 1 --threads 8 --threads-batch 8 --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0 --jinja --timeout 3600 \
  --chat-template-kwargs '{"reasoning_effort":"low"}' --fit off "$@"
