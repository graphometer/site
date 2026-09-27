#!/usr/bin/env python3
"""Build the synthetic half of the describer bake-off picture set.

Every picture made here has a KNOWN ground truth (the strings and numbers
below), so reading accuracy can be scored objectively instead of by taste.
Run with an interpreter that has Pillow. Writes only into ./images.
"""
import json
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "images"
OUT.mkdir(exist_ok=True)
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
WALL = Path("<WALLPAPER_DIR>")  # folder holding the two NASA pictures and the logo (README)

truth = {}


def font(path, size):
    return ImageFont.truetype(path, size)


# 01 / 02: real photographs, large (3840x2160): tests big-image handling.
shutil.copyfile(WALL / "orion_nebula_nasa_heic0601a.jpg", OUT / "01_nebula_large.jpg")
truth["01_nebula_large.jpg"] = {
    "kind": "real photo, 3840x2160",
    "expect": ["nebula", "stars"],
    "notes": "Orion nebula (NASA/Hubble). Pink/red/orange gas clouds, dark space, many stars. No text.",
}
shutil.copyfile(WALL / "otherworldly_earth_nasa_ISS064-E-29444.jpg", OUT / "02_earth_from_orbit.jpg")
truth["02_earth_from_orbit.jpg"] = {
    "kind": "real photo, 3840x2160",
    "expect": ["earth"],
    "notes": "Earth seen from the ISS. See the picture for detail.",
}

# 03: poster with headline, medium and small text.
im = Image.new("RGB", (1200, 1600), (247, 238, 219))
d = ImageDraw.Draw(im)
d.rectangle([40, 40, 1160, 1560], outline=(122, 52, 28), width=10)
d.text((600, 210), "HARVEST SUPPER", font=font(BOLD, 110), fill=(122, 52, 28), anchor="mm")
d.text((600, 340), "A community evening of food and music", font=font(SERIF, 44), fill=(60, 40, 30), anchor="mm")
# a simple pumpkin so there is something to describe besides text
d.ellipse([400, 480, 800, 840], fill=(226, 122, 38), outline=(140, 70, 20), width=8)
for x in (480, 560, 640, 720):
    d.arc([x - 60, 480, x + 60, 840], 90, 270, fill=(170, 85, 25), width=5)
d.rectangle([580, 430, 620, 500], fill=(74, 110, 48))
d.text((600, 960), "Saturday 14 November · 6:30 pm", font=font(BOLD, 58), fill=(30, 30, 30), anchor="mm")
d.text((600, 1050), "Millbrook Grange Hall, 27 Orchard Lane", font=font(SANS, 46), fill=(30, 30, 30), anchor="mm")
d.text((600, 1230), "Bring a dish to share. Tickets $12 at the door.", font=font(SANS, 34), fill=(50, 50, 50), anchor="mm")
d.text((600, 1290), "Questions? Call Doreen on 555-0147.", font=font(SANS, 34), fill=(50, 50, 50), anchor="mm")
d.text((600, 1480), "Printed by Fernhill Press · job no. 48213", font=font(SANS, 20), fill=(90, 90, 90), anchor="mm")
im.save(OUT / "03_poster_text.png")
truth["03_poster_text.png"] = {
    "kind": "synthetic poster",
    "expect": ["HARVEST SUPPER", "14 November", "6:30", "Millbrook Grange Hall", "27 Orchard Lane",
               "$12", "555-0147", "Doreen", "Fernhill Press", "48213"],
    "notes": "Cream poster, brown border, an orange pumpkin with a green stem in the middle.",
}

# 04: a dense document page with small text and a table of amounts.
im = Image.new("RGB", (1240, 1754), (255, 255, 255))
d = ImageDraw.Draw(im)
d.text((90, 90), "Kestrel Bicycle Repair", font=font(BOLD, 46), fill=(0, 0, 0))
d.text((90, 150), "Unit 4, Tannery Yard, Ashby  ·  invoices@kestrelbikes.example", font=font(SANS, 22), fill=(40, 40, 40))
d.text((90, 240), "INVOICE No. KB-2291", font=font(BOLD, 30), fill=(0, 0, 0))
d.text((90, 285), "Date: 3 March 2026        Customer: M. Okafor", font=font(SANS, 24), fill=(0, 0, 0))
rows = [("Replace rear derailleur cable", "18.50"), ("New chain, 11-speed", "42.00"),
        ("True front wheel", "15.00"), ("Brake pads, pair", "12.75"), ("Labour, 1.5 hours", "67.50")]
y = 380
d.line([90, y - 10, 1150, y - 10], fill=(0, 0, 0), width=2)
for name, amt in rows:
    d.text((100, y), name, font=font(SANS, 24), fill=(0, 0, 0))
    d.text((1140, y), "£" + amt, font=font(SANS, 24), fill=(0, 0, 0), anchor="ra")
    y += 46
d.line([90, y, 1150, y], fill=(0, 0, 0), width=2)
d.text((100, y + 16), "TOTAL DUE", font=font(BOLD, 26), fill=(0, 0, 0))
d.text((1140, y + 16), "£155.75", font=font(BOLD, 26), fill=(0, 0, 0), anchor="ra")
para = ("Payment is due within 14 days. Bicycles left longer than 30 days after "
        "completion may incur a storage charge of £2 per day. All parts carry a "
        "twelve-month warranty; labour is guaranteed for ninety days.")
words, line, yy = para.split(), "", y + 120
for w in words:
    if d.textlength(line + " " + w, font=font(SANS, 18)) > 1040:
        d.text((100, yy), line, font=font(SANS, 18), fill=(30, 30, 30))
        yy += 28
        line = w
    else:
        line = (line + " " + w).strip()
d.text((100, yy), line, font=font(SANS, 18), fill=(30, 30, 30))
im.save(OUT / "04_invoice_small_text.png")
truth["04_invoice_small_text.png"] = {
    "kind": "synthetic document, small text",
    "expect": ["Kestrel Bicycle Repair", "KB-2291", "3 March 2026", "Okafor", "18.50", "42.00",
               "15.00", "12.75", "67.50", "155.75", "14 days", "£2 per day", "twelve-month"],
    "notes": "White invoice page; five line items and a total.",
}

# 05: bar chart with labelled values.
im = Image.new("RGB", (1400, 900), (255, 255, 255))
d = ImageDraw.Draw(im)
d.text((700, 60), "Rainfall by month (mm)", font=font(BOLD, 44), fill=(0, 0, 0), anchor="mm")
data = [("Jan", 42), ("Feb", 35), ("Mar", 58), ("Apr", 71), ("May", 64), ("Jun", 23)]
base, left = 780, 160
d.line([left - 20, base, 1320, base], fill=(0, 0, 0), width=3)
d.line([left - 20, 140, left - 20, base], fill=(0, 0, 0), width=3)
for i, (m, v) in enumerate(data):
    x0 = left + i * 190
    top = base - v * 8
    d.rectangle([x0, top, x0 + 120, base], fill=(44, 110, 170))
    d.text((x0 + 60, top - 28), str(v), font=font(BOLD, 30), fill=(0, 0, 0), anchor="mm")
    d.text((x0 + 60, base + 36), m, font=font(SANS, 30), fill=(0, 0, 0), anchor="mm")
im.save(OUT / "05_bar_chart.png")
truth["05_bar_chart.png"] = {
    "kind": "synthetic chart",
    "expect": ["Rainfall by month", "Jan", "Jun", "42", "35", "58", "71", "64", "23"],
    "notes": "Blue bars; April (71) is the tallest, June (23) the shortest.",
}

# 06: a scene with an obvious 'up', saved SIDEWAYS with an EXIF orientation
# tag that says how to stand it up. A describer that ignores the tag sees a
# house lying on its side and text running up the page.
scene = Image.new("RGB", (900, 1200), (150, 205, 245))
d = ImageDraw.Draw(scene)
d.rectangle([0, 900, 900, 1200], fill=(86, 160, 72))            # grass at the bottom
d.ellipse([640, 80, 820, 260], fill=(255, 214, 64))             # sun, top right
d.rectangle([250, 560, 650, 900], fill=(196, 84, 60))           # house
d.polygon([(210, 560), (450, 360), (690, 560)], fill=(96, 56, 40))  # roof
d.rectangle([410, 720, 490, 900], fill=(70, 44, 30))            # door
d.text((450, 1050), "GARDEN COTTAGE", font=font(BOLD, 64), fill=(255, 255, 255), anchor="mm")
sideways = scene.rotate(90, expand=True)     # pixels stored rotated 90° counter-clockwise
exif = Image.Exif()
exif[0x0112] = 6                              # "rotate 90° clockwise to display"
sideways.save(OUT / "06_cottage_exif_rotated.jpg", quality=92, exif=exif)
truth["06_cottage_exif_rotated.jpg"] = {
    "kind": "synthetic, stored sideways with EXIF Orientation=6",
    "expect": ["GARDEN COTTAGE", "house", "sun"],
    "notes": "Upright: red house, brown roof, sun top-right, grass below, white caption. "
             "A describer that ignores EXIF reports it rotated / text vertical.",
}

# 07: white logo on a TRANSPARENT background (alpha edge case).
# [Note added 26 September 2026: the file copied here has no transparent pixels. It is a dark
#  wordmark on an opaque light gray field; see data/README.md.]
shutil.copyfile(WALL / "COSMIC-logo-White.png", OUT / "07_logo_white_on_transparent.png")
truth["07_logo_white_on_transparent.png"] = {
    "kind": "real PNG with alpha, 3840x2160",
    "expect": ["COSMIC"],
    "notes": "White COSMIC wordmark on full transparency. On a white flatten it vanishes.",
}

(HERE / "ground_truth.json").write_text(json.dumps(truth, indent=1))
for p in sorted(OUT.iterdir()):
    with Image.open(p) as i:
        print(f"{p.name:40s} {i.size[0]}x{i.size[1]} {i.mode:5s} {p.stat().st_size/1024:8.0f} KB")
