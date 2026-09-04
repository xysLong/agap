"""Small helper package for the Algorithmic Generative Art course.

Only a handful of things live here, on purpose -- all the real code stays
visible in the notebooks:

- save_artwork(...)  saves a figure or an image array to assets/outputs/
- show(...)          displays an image array with the axes switched off
- PALETTES           named color palettes shared across all chapters
- PAPER              the warm paper-white ground all artworks sit on
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# assets/outputs/ located relative to this file, so it works from any notebook
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "outputs"

# artworks are saved at least this many pixels on the long side (print quality)
MIN_PIXELS = 2000

# soft warm off-white -- the ground for artwork figures (diagrams stay white)
PAPER = "#FAF7F0"

PALETTES = {
    # Bauhaus primaries: red, blue, yellow, near-black, warm paper white
    "bauhaus": ["#D02433", "#1B4B9B", "#F7C523", "#1A1A1A", "#F2EFE9"],
    # dark saturated tones after Mark Rothko's late paintings
    "rothko_dark": ["#3B0A0E", "#701C1C", "#A63A22", "#D96C3F", "#1E1420"],
    # soft pastel set
    "pastel": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#E3BAFF"],
    # monochrome ramp, near-black to near-white
    "monochrome": ["#111111", "#3D3D3D", "#6B6B6B", "#9C9C9C", "#CFCFCF", "#F5F5F5"],
    # perceptually uniform sets, sampled from matplotlib's viridis and magma
    "viridis": ["#440154", "#414487", "#2A788E", "#22A884", "#7AD151", "#FDE725"],
    "magma": ["#000004", "#3B0F70", "#8C2981", "#DE4968", "#FE9F6D", "#FCFDBF"],
    # bright spectrum after Ellsworth Kelly's chance color panels
    "kelly": ["#E4572E", "#F3A712", "#F5E960", "#76B041",
              "#17BEBB", "#3B28CC", "#9B5DE5", "#F15BB5"],
}


def save_artwork(fig_or_array, name, chapter):
    """Save a matplotlib figure or an image array to assets/outputs/ as a
    print-quality PNG (figures: at least MIN_PIXELS on the long side) and
    print where it went.

    Filename pattern: chXX_<name>.png
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = OUTPUT_DIR / f"ch{chapter:02d}_{name}.png"
    if isinstance(fig_or_array, plt.Figure):
        # pick the dpi that makes the long side reach MIN_PIXELS (never < 300)
        tight = fig_or_array.get_tightbbox()
        dpi = max(300, math.ceil(MIN_PIXELS / max(tight.width, tight.height)))
        fig_or_array.savefig(filename, dpi=dpi, bbox_inches="tight",
                             facecolor=fig_or_array.get_facecolor())
    else:
        plt.imsave(filename, np.asarray(fig_or_array))
    print(f"saved: {filename.relative_to(OUTPUT_DIR.parent.parent)}")
    return filename


def show(img_array, title=None, cmap=None):
    """Display an image array without axes -- for artwork, not diagrams."""
    plt.figure(figsize=(7, 7))
    plt.imshow(img_array, cmap=cmap)
    plt.axis("off")
    if title is not None:
        plt.title(title)
    plt.show()
