#!/usr/bin/env bash
# the test launcher <home-name> <switches|factory> <strace-log|-> [letta args...]
# COPY of the session's launcher for the 2026-10-12 network check: engine 0.34.10, throwaway home under <REDACTED_PATH>,
# local backend. "switches" sets the six privacy switches as the session's launcher does; "factory" sets none of them.
set -euo pipefail
F=<REDACTED_PATH>
name=$1; mode=$2; slog=$3; shift 3
case "$name" in <HOME>) ;; *) echo "refused: home name must start with <HOME>" >&2; exit 64;; esac
H=$F/$name; echo "HOME FOR THIS RUN: $(realpath -m "$H")" >&2
NODE_BIN=<REDACTED_PATH>
mkdir -p "$H/work"; cd "$H/work"
sw=()
[[ $mode == switches ]] && sw=(LETTA_LOCAL_BACKEND_DIR="$H/.letta/lc-local-backend" LETTA_CODE_TELEM=0 DO_NOT_TRACK=1 DISABLE_AUTOUPDATER=1 LETTA_CODE_OFFLINE=1 LETTA_DISABLE_LSP_DOWNLOAD=1 LETTA_DISABLE_MODS=1)
tr=()
[[ $slog != - ]] && tr=(strace -f -qq -e trace=connect,sendto,sendmmsg -s 300 -o "$slog")
exec env -i HOME="$H" PATH="$NODE_BIN:/usr/local/bin:/usr/bin:/bin" LANG=C.UTF-8 TERM="${TERM:-dumb}" USER=<USER> LOGNAME=<USER> SHELL=/bin/bash \
  "${sw[@]}" ${LF_EXTRA_ENV:-} \
  "${tr[@]}" node "$F/engine/0.34.10/node_modules/@letta-ai/letta-code/letta.js" --backend local "$@"
