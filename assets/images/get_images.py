"""Download the public-domain input images used in weeks 5, 11, 12 and 13.

Run once after setting up the environment:

    python assets/images/get_images.py

All artworks are public domain, served by Wikimedia Commons. If a download
fails (no internet, changed URL), a synthetic stand-in image is generated
instead so that no notebook ever breaks offline. The poster `poster_demo.png`
(used in week 11) ships with the repository: it is a real conference poster
(the instructor's, ETRA 2026 doctoral consortium), downsampled until only the
title is readable. It cannot be regenerated here; if the file is missing, a
synthetic stand-in poster is drawn instead.
"""

import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

IMAGE_DIR = Path(__file__).resolve().parent

# filename -> Wikimedia Commons file (all public domain), fetched at width 1600 px
COMMONS_FILES = {
    "monet_waterlilies.jpg":
        "Claude Monet - Water Lilies - 1906, Ryerson.jpg",
    "seurat_grande_jatte.jpg":
        "Georges Seurat - A Sunday on La Grande Jatte -- 1884 - Google Art Project.jpg",
    "vermeer_pearl_earring.jpg":
        "1665 Girl with a Pearl Earring.jpg",
    "hokusai_wave.jpg":
        "Tsunami by hokusai 19th century.jpg",
}

USER_AGENT = "GenerativeArtCourse/1.0 (educational use)"


def commons_url(commons_name):
    """Stable Wikimedia Commons URL that redirects to the current file."""
    quoted = urllib.parse.quote(commons_name)
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{quoted}?width=1600"


def download(url, target):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        target.write_bytes(response.read())


def synthetic_standin(target, label):
    """Generate a gradient-plus-shapes placeholder so notebooks work offline."""
    rng = np.random.default_rng(abs(hash(label)) % (2**32))
    width, height = 1600, 1100
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    grid_x, grid_y = np.meshgrid(x, y)
    r = 0.2 + 0.6 * grid_x
    g = 0.3 + 0.5 * grid_y
    b = 0.7 - 0.4 * grid_x * grid_y
    array = np.stack([r, g, b], axis=-1)
    image = Image.fromarray((array * 255).astype(np.uint8))
    draw = ImageDraw.Draw(image)
    for _ in range(12):
        cx, cy = rng.integers(0, width), rng.integers(0, height)
        radius = int(rng.integers(40, 220))
        color = tuple(int(v) for v in rng.integers(0, 255, size=3))
        draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=color)
    draw.text((30, 30), f"synthetic stand-in for {label}", fill=(0, 0, 0))
    image.save(target, quality=90)


def make_poster_demo(target):
    """A fake conference poster: title block, two text columns, one figure box.

    Fallback only: the repository ships a real (downsampled) poster as
    poster_demo.png, the week 11 surface for simulated attention heatmaps.
    This stand-in keeps the notebook runnable if that file ever goes missing,
    but the fixation regions in the notebook are placed for the real poster.
    """
    width, height = 1200, 1600
    image = Image.new("RGB", (width, height), (245, 243, 238))
    draw = ImageDraw.Draw(image)
    # title block
    draw.rectangle([60, 50, width - 60, 200], fill=(27, 75, 155))
    draw.rectangle([90, 90, width - 400, 120], fill=(235, 235, 235))
    draw.rectangle([90, 140, width - 600, 165], fill=(200, 210, 230))
    # author line
    draw.rectangle([60, 220, 700, 250], fill=(120, 120, 120))
    # two text columns rendered as gray line strips
    rng = np.random.default_rng(11)
    for column_left in (60, 630):
        top = 300
        while top < 1150:
            line_width = int(rng.integers(380, 510))
            draw.rectangle([column_left, top, column_left + line_width, top + 14],
                           fill=(90, 90, 90))
            top += 30
            if rng.random() < 0.12:
                top += 25  # paragraph break
    # figure box, bottom center-left
    draw.rectangle([60, 1200, 700, 1540], outline=(30, 30, 30), width=4)
    draw.ellipse([150, 1270, 420, 1470], fill=(208, 36, 51))
    draw.rectangle([460, 1250, 650, 1500], fill=(247, 197, 35))
    # caption + logo box
    draw.rectangle([740, 1250, 1140, 1270], fill=(120, 120, 120))
    draw.rectangle([740, 1300, 1080, 1320], fill=(120, 120, 120))
    draw.rectangle([950, 1420, 1140, 1540], fill=(27, 75, 155))
    image.save(target)
    print(f"generated: {target.name}")


def main():
    for filename, commons_name in COMMONS_FILES.items():
        target = IMAGE_DIR / filename
        if target.exists():
            print(f"exists, skipping: {filename}")
            continue
        try:
            download(commons_url(commons_name), target)
            print(f"downloaded: {filename}")
        except Exception as error:
            print(f"download failed for {filename} ({error}); generating stand-in")
            synthetic_standin(target, filename)
    poster = IMAGE_DIR / "poster_demo.png"
    if not poster.exists():
        print("poster_demo.png missing (it ships with the repo); "
              "drawing the synthetic fallback")
        make_poster_demo(poster)
    else:
        print("exists, skipping: poster_demo.png")


if __name__ == "__main__":
    main()
