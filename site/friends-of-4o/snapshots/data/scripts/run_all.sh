#!/bin/bash
# Usage: run_all.sh <EXPORTS_DIR> <OUT_DIR> <LEAKFILE>   (OUT_DIR is the data/ folder)
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 -I "$HERE/s1_inventory.py" --exports "$1" --out "$2" > /dev/null
python3 -I "$HERE/s2_measure.py" --exports "$1" --out "$2"
python3 -I "$HERE/s3_stats.py" --out "$2" --boot 10000 --perm 10000
python3 -I "$HERE/s4_d6_noise.py" --out "$2" > /dev/null
python3 -I "$HERE/s5_context.py" --exports "$1" --out "$2" > /dev/null
python3 -I "$HERE/s6_pack.py" --exports "$1" --out "$2" --leakfile "$3" > /dev/null
