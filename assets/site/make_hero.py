"""Build the landing-page hero image by tiling the course showpieces.

Collects every assets/outputs/ch*_showpiece.png, scales them to a common
height, and arranges them in rows on a cream background. Re-run manually as
new chapters land:

    python assets/site/make_hero.py

Once chapter 20's contact sheet exists, this script can be retired and the
hero replaced by that image.
"""

import glob
from pathlib import Path

from PIL import Image

SITE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SITE_DIR.parent / "outputs"

TILE_HEIGHT = 800     # every showpiece is scaled to this height
GAP = 48              # spacing between tiles and around the edge
PER_ROW = 4           # tiles per row before wrapping
BACKGROUND = (246, 243, 236)


def main():
    paths = sorted(glob.glob(str(OUTPUT_DIR / "ch*_showpiece.png")))
    if not paths:
        raise SystemExit("no showpieces found in assets/outputs/ -- run the notebooks first")

    tiles = []
    for path in paths:
        image = Image.open(path).convert("RGB")
        width = int(image.width * TILE_HEIGHT / image.height)
        tiles.append(image.resize((width, TILE_HEIGHT), Image.LANCZOS))

    rows = []
    for start in range(0, len(tiles), PER_ROW):
        rows.append(tiles[start:start + PER_ROW])

    row_widths = []
    for row in rows:
        total = GAP
        for tile in row:
            total += tile.width + GAP
        row_widths.append(total)

    hero_width = max(row_widths)
    hero_height = GAP + len(rows) * (TILE_HEIGHT + GAP)
    hero = Image.new("RGB", (hero_width, hero_height), BACKGROUND)

    y = GAP
    for row, row_width in zip(rows, row_widths):
        x = (hero_width - row_width) // 2 + GAP   # center each row
        for tile in row:
            hero.paste(tile, (x, y))
            x += tile.width + GAP
        y += TILE_HEIGHT + GAP

    target = SITE_DIR / "hero.png"
    hero.save(target)
    print(f"saved: {target} ({hero.width}x{hero.height}, {len(tiles)} showpieces)")


if __name__ == "__main__":
    main()
