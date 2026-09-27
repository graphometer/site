#!/usr/bin/env python3
"""A 4K 'screenshot' with small text at four sizes, each line carrying a unique
code, to find where shrinking a picture starts to cost reading accuracy."""
import json, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
HERE = Path(__file__).resolve().parent
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
random.seed(7)
words = ["tangerine","harbour","kettle","lantern","meadow","pebble","quartz","ribbon","saffron","thimble","umber","violet","walnut","yarrow","zephyr","anchor","bramble","cobalt"]
im = Image.new("RGB", (3840, 2160), (250, 250, 250)); d = ImageDraw.Draw(im)
truth = {}; y = 60
for size in (28, 20, 16, 13):
    d.text((80, y), f"Section \u2014 {size} px text", font=ImageFont.truetype(SANS, size + 8), fill=(0, 0, 0)); y += size + 40
    codes = []
    for i in range(6):
        code = f"{random.choice('ABCDEFGHJK')}{random.randint(10,99)}-{random.choice(words)}-{random.randint(1000,9999)}"
        codes.append(code)
        d.text((120, y), f"Item {i+1}:  {code}   status ready   owner desk {random.randint(1,40)}", font=ImageFont.truetype(SANS, size), fill=(20, 20, 20)); y += int(size * 1.9)
    truth[str(size)] = codes; y += 50
im.save(HERE / "hires" / "08_screenshot_4k_small_text.png")
json.dump(truth, open(HERE / "hires_truth.json", "w"), indent=1)
from PIL import Image as I
for cap in (2560, 2048, 1536):
    out = HERE / f"hires_{cap}"; out.mkdir(exist_ok=True)
    c = im.copy(); c.thumbnail((cap, cap), I.LANCZOS); c.save(out / "08_screenshot_4k_small_text.png")
print(truth)
