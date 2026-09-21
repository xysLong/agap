"""Build the landing-page hero image from the course showpieces.

One row per part of the book: the Prelude tile sits centered on top, and each
of Parts I-VI is a justified row (its tiles are scaled to a shared height so
the row fills the full hero width). Chapter 27 is excluded: its showpiece is
a composite of the other chapters' artworks. Re-run manually after a
showpiece changes:

    python assets/site/make_hero.py
"""

from pathlib import Path

from PIL import Image

SITE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SITE_DIR.parent / "outputs"

HERO_WIDTH = 2200     # total width in pixels (displayed at ~900 css px)
GAP = 24              # spacing between tiles and around the edge
PRELUDE_HEIGHT = 460  # the single chapter-0 tile, centered
JPEG_QUALITY = 85
BACKGROUND = (246, 243, 236)

ROWS = [
    [0],                    # Prelude
    [1, 2, 3, 4, 5],        # Part I - Foundations
    [6, 7, 8, 9],           # Part II - Growth and Iteration
    [10, 11, 12, 13, 14],   # Part III - Fields and Grids
    [15, 16, 17, 18],       # Part IV - The Image, Transformed
    [19, 20, 21, 22, 23],   # Part V - Agents and Complexity
    [24, 25, 26],           # Part VI - Coda (27 excluded: composite)
]


def load(chapter):
    return Image.open(OUTPUT_DIR / f"ch{chapter:02d}_showpiece.png").convert("RGB")


def main():
    rendered_rows = []
    for chapters in ROWS:
        images = [load(ch) for ch in chapters]
        aspects = [im.width / im.height for im in images]
        available = HERO_WIDTH - GAP * (len(images) + 1)
        if len(images) == 1:
            height = PRELUDE_HEIGHT
        else:
            height = int(available / sum(aspects))
        tiles = [
            im.resize((max(1, int(a * height)), height), Image.LANCZOS)
            for im, a in zip(images, aspects)
        ]
        rendered_rows.append(tiles)

    hero_height = GAP + sum(tiles[0].height + GAP for tiles in rendered_rows)
    hero = Image.new("RGB", (HERO_WIDTH, hero_height), BACKGROUND)

    y = GAP
    for tiles in rendered_rows:
        row_width = sum(t.width for t in tiles) + GAP * (len(tiles) - 1)
        x = (HERO_WIDTH - row_width) // 2
        for tile in tiles:
            hero.paste(tile, (x, y))
            x += tile.width + GAP
        y += tiles[0].height + GAP

    target = SITE_DIR / "hero.jpg"
    hero.save(target, quality=JPEG_QUALITY, progressive=True, optimize=True)
    count = sum(len(r) for r in rendered_rows)
    size_mb = target.stat().st_size / 1e6
    print(f"saved: {target} ({hero.width}x{hero.height}, {count} showpieces, {size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
