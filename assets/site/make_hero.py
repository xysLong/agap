"""Build the landing-page hero image from the course showpieces.

Chapters 0-26 in three justified rows of nine: each row's tiles share a
height chosen so the row fills the full hero width. Chapter 27 is excluded:
its showpiece is a composite of the other chapters' artworks. Re-run
manually after a showpiece changes:

    python assets/site/make_hero.py
"""

from pathlib import Path

from PIL import Image

SITE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SITE_DIR.parent / "outputs"

CHAPTERS = range(27)  # 27 excluded: composite of the others
PER_ROW = 9
HERO_WIDTH = 2200     # total width in pixels (displayed at ~900 css px)
GAP = 16              # spacing between tiles and around the edge
JPEG_QUALITY = 85
BACKGROUND = (246, 243, 236)


def load(chapter):
    return Image.open(OUTPUT_DIR / f"ch{chapter:02d}_showpiece.png").convert("RGB")


def main():
    rows = [CHAPTERS[start:start + PER_ROW] for start in range(0, len(CHAPTERS), PER_ROW)]

    rendered_rows = []
    for chapters in rows:
        images = [load(ch) for ch in chapters]
        aspects = [im.width / im.height for im in images]
        available = HERO_WIDTH - GAP * (len(images) + 1)
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
