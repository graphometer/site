#!/bin/bash
# 2026-10-17: the default (xet) hf path produced a corrupt Beam IQ2_M part 3 twice (sha256 mismatch, client hung at the end);
# plain curl ran at ~1 MB/s. Third way: hf with xet disabled (plain HTTP, its own checks), into a scratch dir, then our sha256 check.
set -u
D=<REDACTED_PATH>/unsloth
T=$D/part3-refetch
F=Beam-1.0-501B-A23B-UD-IQ2_M-00003-of-00005.gguf
mkdir -p $T
HF_HUB_DISABLE_XET=1 hf download unsloth/Beam-1.0-501B-A23B-GGUF UD-IQ2_M/$F --local-dir $T
s=$(sha256sum $T/UD-IQ2_M/$F | cut -c1-64)
if [ "$s" = 7478bfa738a5ab6240338b082fc0f31b7cf6a77815cef0bada541c7f3ca1fa66 ]; then mv $T/UD-IQ2_M/$F $D/UD-IQ2_M/$F && rm -rf $T && echo "PART3-VERIFIED $(date +%H:%M)"; else echo "PART3-MISMATCH $s"; fi
