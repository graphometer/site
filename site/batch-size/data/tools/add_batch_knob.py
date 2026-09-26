#!/usr/bin/env python3
"""add_batch_knob.py: give a roster start_server.sh a <PFX>_BATCH / <PFX>_UBATCH knob.

Behaviour-preserving: the defaults written are llama.cpp's own (-b 2048 -ub 512), so the script
serves exactly as before until a measured value replaces them. Refuses unless each anchor occurs
exactly once; writes <script>.bak-20260921-batch first (never overwrites an existing .bak); runs
`bash -n` on the result and restores the original if it fails.

    add_batch_knob.py <path/to/start_server.sh> <PFX> [--dry-run]
"""
import re, shutil, subprocess, sys
from pathlib import Path

path, pfx = Path(sys.argv[1]), sys.argv[2]
dry = "--dry-run" in sys.argv
src = path.read_text()
if f"{pfx}_UBATCH" in src:
    sys.exit(f"SKIP: {path} already has {pfx}_UBATCH")
if re.search(r"--ubatch-size|(^|\s)-ub\s", src.split("\nexec ")[-1]):
    sys.exit(f"REFUSE: {path} already passes a ubatch in its exec block: edit by hand")

exec_lines = [i for i, l in enumerate(src.splitlines()) if l.startswith("exec ")]
ctx_lines = [i for i, l in enumerate(src.splitlines())
             if re.search(r'--ctx-size "\$\{?CTX\}?"', l) and l.rstrip().endswith("\\")]
if len(exec_lines) != 1 or len(ctx_lines) != 1 or ctx_lines[0] < exec_lines[0]:
    sys.exit(f"REFUSE: anchors not unique (exec at {exec_lines}, ctx-size at {ctx_lines})")

knob = f'''# --- batch sizes ({pfx}_BATCH / {pfx}_UBATCH), knob added 2026-09-21 for the batch sweep ---------
# This script had never set them, so it ran llama.cpp's defaults (-b 2048 -ub 512). With experts
# CPU-side, prefill is op-offload bound: the CPU-held weights cross to the card ONCE PER UBATCH, so
# a larger ubatch is close to pure reading speed (2.5x-7.3x on the four models tuned 2026-09-20).
# The defaults below still EQUAL llama.cpp's until the sweep measures this
# model; a measured value replaces them with its numbers here. Keep batch >= ubatch.
{pfx}_BATCH="${{{pfx}_BATCH:-2048}}"; {pfx}_UBATCH="${{{pfx}_UBATCH:-512}}"
case "${pfx}_BATCH${pfx}_UBATCH" in *[!0-9]*) echo "ERROR: {pfx}_BATCH/{pfx}_UBATCH must be integers." >&2; exit 2 ;; esac
'''

lines = src.splitlines(keepends=True)
ctx_line = lines[ctx_lines[0]]
indent = re.match(r"\s*", ctx_line).group(0)
flag = f'{indent}--batch-size "${{{pfx}_BATCH}}" --ubatch-size "${{{pfx}_UBATCH}}" \\\n'
new = lines[:exec_lines[0]] + [knob] + lines[exec_lines[0]:ctx_lines[0] + 1] + [flag] + lines[ctx_lines[0] + 1:]
out = "".join(new)
if dry:
    import difflib
    sys.stdout.writelines(difflib.unified_diff(src.splitlines(True), out.splitlines(True), str(path), str(path) + " (new)"))
    sys.exit(0)
bak = path.with_name(path.name + ".bak-20260921-batch")
if bak.exists():
    sys.exit(f"REFUSE: {bak} already exists: not overwriting a backup")
shutil.copy2(path, bak)
path.write_text(out)
if subprocess.run(["bash", "-n", str(path)]).returncode != 0:
    shutil.copy2(bak, path)
    sys.exit(f"FAILED bash -n: original restored from {bak}")
print(f"OK {path} (+knob {pfx}_BATCH/{pfx}_UBATCH, backup {bak.name})")
