#!/usr/bin/env bash
# Runner for the installed 4-bit preset, 2026-09-15. Heavily redacted: the service
# manager calls, the agent framework's container, the provider re-pointing and the
# residue check are replaced by markers, and every path, address and port is replaced.
# The shard byte-size check, the placement settings, the health poll and the speed
# probe call are unchanged.
# 
# The Q4_K_XL + DSpark preset on the two-machine server: wait for the file copy, the
# Thunderbolt link and a free card, set the preset, start the server, poll health, run
# the speed probe and the tool-and-recall check, then restore the 3-bit default.
set -uo pipefail
S=<REDACTED_PATH>; R=$S/q4-installed.md; H=<REDACTED_PATH>; REPO=<REDACTED_PATH>
ENVF=<REDACTED_PATH>; D=<REDACTED_PATH>
IQ3=<REDACTED_PATH>/DeepSeek-V4-Flash-0731-UD-IQ3_XXS-00001-of-00004.gguf
Q4=$D/DeepSeek-V4-Flash-0731-UD-Q4_K_XL-00001-of-00005.gguf
log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a $R; }
setenv() { python3 - "$@" <<'PY'
import re, sys; p="<REDACTED_PATH>"; s=open(p).read()
for kv in sys.argv[1:]:
    k,v=kv.split("=",1); s,n=re.subn(rf"^{k}=.*$", f"{k}={v}", s, flags=re.M)
    if n==0: s+=f"\n{k}={v}\n"
open(p,"w").write(s)
PY
}
log "=== Q4_K_XL + draft on the two-machine server , waiting for the copy, the Thunderbolt link, a free card ==="
until ! pgrep -x rsync >/dev/null && grep -a -q "to-chk=0/" <REDACTED_PATH> 2>/dev/null; do sleep 20; done; log "copy finished"
for pair in "00001:5257408" "00002:48935523072" "00003:48980787136" "00004:49999168416" "00005:7174505088"; do n=${pair%%:*}; want=${pair##*:}; f=$D/DeepSeek-V4-Flash-0731-UD-Q4_K_XL-${n}-of-00005.gguf; have=$(stat -c %s "$f" 2>/dev/null || echo 0); [ "$have" = "$want" ] || { log "shard $n wrong size ($have vs $want) , abort"; exit 2; }; done; log "5 shards byte-exact"
until ping -c 1 -W 1 <LAPTOP> >/dev/null 2>&1 && timeout 3 bash -c "echo > /dev/tcp/<LAPTOP>/<PORT>" 2>/dev/null; do sleep 15; done; log "Z13 worker reachable on the Thunderbolt link"
until ! pgrep -x llama-server >/dev/null; do sleep 15; done
cp -a $ENVF $S/<CONFIG_FILE>.before-q4-test
setenv MODEL_MODEL=$Q4 MODEL_DRAFT=1 MODEL_HOST_LAYERS=15 MODEL_GPU_FULL=2 MODEL_CTX=131072; log "env set: Q4 + draft, 2 card / 13 RAM / 28 Z13"
<REDACTED: start the model service>
t0=$(date +%s)
for i in $(seq 1 600); do curl -sf --max-time 2 <LOCAL>/health 2>/dev/null | grep -q '"ok"' && break; systemctl is-active --quiet <UNIT> || { sleep 5; systemctl is-active --quiet <UNIT> || { log "server not active , $(systemctl is-active <UNIT>)"; journalctl -u <UNIT> -n 8 --no-pager | cut -c1-200 | tee -a $R; break; }; }; sleep 2; done
if curl -sf --max-time 2 <LOCAL>/health | grep -q '"ok"'; then
  log "healthy after $(( $(date +%s) - t0 )) s · VRAM $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · Z13 RAM used $(ssh -o ConnectTimeout=5 <LAPTOP> 'free -g | awk "/^Mem:/{print \$3}"' 2>/dev/null) GB"
  grep -E "model buffer size|KV buffer size|draft" "$(journalctl -u <UNIT> -n 400 --no-pager -o cat 2>/dev/null | head -0; ls -t /dev/null)" 2>/dev/null; journalctl -u <UNIT> -n 400 --no-pager -o cat | grep -E "model buffer size|KV buffer size|spec|draft" | head -6 | cut -c1-140 | tee -a $R
  python3 $S/direct-probe.py <LOCAL> 8000 2>&1 | tee -a $R | cut -c1-240
<REDACTED: start the agent framework>
  <REDACTED: wait for the agent framework>
  <REDACTED: run the tool-and-recall check, writing q4-short-check.json>
  <REDACTED: copy the check verdict into the record>
<REDACTED: re-point the provider>
<REDACTED: residue check>
<REDACTED: stop the agent framework>
fi
<REDACTED: stop the model service, then wait for it to go down>
setenv MODEL_MODEL=$IQ3 MODEL_DRAFT=0 MODEL_HOST_LAYERS=18 MODEL_GPU_FULL=8 MODEL_CTX=131072; log "env restored to the IQ3 gated default"
log "Q4 TEST DONE · unit $(systemctl is-active <UNIT>) · card $(nvidia-smi --query-gpu=memory.used --format=csv,noheader) · <AGENT_FRAMEWORK> at rest"
