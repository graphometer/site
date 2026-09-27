#!/usr/bin/env python3
"""Make the 'normalised' twin of the picture set: EXIF orientation applied,
longest side capped. This is exactly the step proposed for the describers."""
import sys
from pathlib import Path
from PIL import Image, ImageOps
HERE = Path(__file__).resolve().parent
cap = int(sys.argv[1]) if len(sys.argv) > 1 else 1536
out = HERE / f"images_{cap}"; out.mkdir(exist_ok=True)
for p in sorted((HERE / "images").iterdir()):
    with Image.open(p) as im:
        im = ImageOps.exif_transpose(im)
        if max(im.size) > cap:
            im.thumbnail((cap, cap), Image.LANCZOS)
        if p.suffix.lower() in (".jpg", ".jpeg"):
            im.convert("RGB").save(out / p.name, quality=90)
        else:
            im.save(out / p.name)
        print(p.name, im.size, (out / p.name).stat().st_size // 1024, "KB")
