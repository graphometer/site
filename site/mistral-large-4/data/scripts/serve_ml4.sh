#!/usr/bin/env bash
# Large 4 across the desktop and the Z13 over Thunderbolt, on the installed b12015.
# LAYOUT=front: layers 0..Z-1 whole on the Z13 (no shared-KV crossing). LAYOUT=back: the last Z layers whole on the Z13 (the 10-31 shape).
# GPU_N whole layers on the card, the rest of the desktop's layers keep attention on the card and experts in RAM.
LAYOUT=${LAYOUT:-front}; Z=${Z:-26}; GPU_N=${GPU_N:-4}; N=72; PORT=${PORT:-<PORT>}; CPUS=${CPUS:-0-7}; T=${T:-8}; CTX=${CTX:-32768}; UB=${UB:-512}
M=${M:-<REDACTED_PATH>/Mistral-Large-4-1T-A52B-UD-IQ1_S-00001-of-00006.gguf}
B=${B:-<REDACTED_PATH>}; EP=<LAPTOP>; RPC="RPC0[$EP]"
L=""
if [ "$LAYOUT" = front ]; then
  # desktop layers are Z..71; the last GPU_N stay whole on the card, the ones before keep experts in RAM
  for ((i=Z; i<N-GPU_N; i++)); do L+="${L:+|}$i"; done
  DEV="RPC0,CUDA0"; SPLIT="$Z,$((N-Z))"
elif [ "$LAYOUT" = expz ]; then
  # all attention, shared experts and KV on the card; routed experts of the last Z layers on the Z13, the others in RAM, the first GPU_N whole on the card
  for ((i=GPU_N; i<N-Z; i++)); do L+="${L:+|}$i"; done
  R=""; for ((i=N-Z; i<N; i++)); do R+="${R:+|}$i"; done
  DEV="CUDA0,RPC0"; SPLIT="72,0"; EXTRA_OT=",blk\.($R)\.ffn_(up|down|gate)_exps=$RPC"
else
  for ((i=GPU_N; i<N-Z; i++)); do L+="${L:+|}$i"; done
  DEV="CUDA0,RPC0"; SPLIT="$((N-Z)),$Z"
fi
OT="blk\.($L)\.ffn_(up|down|gate)_exps=CPU,output\.weight=CUDA0${EXTRA_OT:-}"
export LD_LIBRARY_PATH=$B:<REDACTED_PATH> GOMP_SPINCOUNT=${SPIN:-10000000}
[ -n "${HUGE:-}" ] && export GLIBC_TUNABLES=glibc.malloc.hugetlb=1
exec taskset -c $CPUS $B/llama-server --model "$M" --alias mistral-large-4 --host 127.0.0.1 --port $PORT \
  --rpc "$EP" --device "$DEV" --tensor-split "$SPLIT" --n-gpu-layers 999 --override-tensor "$OT" --no-warmup \
  --load-mode mmap --lazy-mode on --parallel 1 --threads $T --threads-batch $T --ctx-size $CTX --batch-size 2048 --ubatch-size $UB \
  --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0 --jinja --timeout 3600 --chat-template-kwargs '{"reasoning_effort":"low"}' --fit off "$@"
