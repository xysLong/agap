"""Download the public-domain input images used by the book's image chapters.

Run once after setting up the environment:

    python assets/images/get_images.py

All artworks are public domain, served by Wikimedia Commons. If a download
fails (no internet, changed URL), a synthetic stand-in image is generated
instead so that no notebook ever breaks offline. Chapter 24's pair of files
ships with the repository instead of being downloaded: the Kandinsky
reproduction `kandinsky_yellow_red_blue.jpg` and the fixation data
`assets/data/kandinsky_fixations.csv` are exact crops/slices of an
eye-tracking study's stimulus and recordings (Long et al. 2026, see the
chapter's references) and cannot be regenerated here.
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


if __name__ == "__main__":
    main()
