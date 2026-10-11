"""Build the four explanatory figures of the introduction page.

    intro_numbers.png      a Vermeer detail as 12 x 12 gray pixels and as 144 numbers
    intro_information.png  stripes, a painting crop and random noise with their PNG sizes
    intro_chaos.png        the logistic map from two starting values 0.0001 apart
    intro_seeds.png        three random walks: seed 0, seed 0 again, seed 1

Re-run manually after changing anything here:

    python assets/site/make_intro_figures.py

Needs assets/images/vermeer_pearl_earring.jpg (fetched by assets/images/get_images.py).
"""

import io
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

SITE_DIR = Path(__file__).resolve().parent
VERMEER = SITE_DIR.parent / "images" / "vermeer_pearl_earring.jpg"

DPI = 200
BLUE = "#1A5FB4"
RED = "#D62828"
GRAY = "#555555"

plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.titlecolor"] = GRAY


def save(fig, name):
    target = SITE_DIR / name
    fig.savefig(target, dpi=DPI, bbox_inches="tight", pad_inches=0.1, facecolor="white")
    plt.close(fig)
    print(f"saved: {target} ({target.stat().st_size / 1e3:.0f} kB)")


# ---------- everything is numbers ----------

def make_numbers():
    im = Image.open(VERMEER).convert("RGB")
    cells = 12
    cell_px = 17                        # 12 cells of 17 px = a 204 px square on the original scan
    x0, y0 = 612, 770                   # the girl's left eye (viewer's left)
    size = cells * cell_px

    gray = np.asarray(im.convert("L"), dtype=float)
    patch = gray[y0:y0 + size, x0:x0 + size]
    # block average: one number per cell
    grid = patch.reshape(cells, cell_px, cells, cell_px).mean(axis=(1, 3)).round().astype(int)
    assert grid.shape == (cells, cells)

    fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(13.5, 5))

    ax0.imshow(im)
    ax0.add_patch(plt.Rectangle((x0, y0), size, size, fill=False, edgecolor=RED, linewidth=2))
    ax0.set_title("Vermeer, Girl with a Pearl Earring (c. 1665)")
    ax0.axis("off")

    ax1.imshow(grid, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    ax1.set_title(f"the red square, as {cells} × {cells} gray pixels")
    ax1.axis("off")

    ax2.imshow(np.ones_like(grid), cmap="gray", vmin=0, vmax=1, interpolation="nearest")
    for (r, c), v in np.ndenumerate(grid):
        ax2.text(c, r, str(v), ha="center", va="center", fontsize=8.5, family="monospace", color="#222222")
    ax2.set_xticks(np.arange(-0.5, cells, 1), minor=True)
    ax2.set_yticks(np.arange(-0.5, cells, 1), minor=True)
    ax2.grid(which="minor", color="#DDDDDD", linewidth=0.8)
    ax2.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
    for spine in ax2.spines.values():
        spine.set_edgecolor("#DDDDDD")
    ax2.set_title(f"the same {cells * cells} pixels as numbers (0 black, 255 white)")

    fig.tight_layout()
    save(fig, "intro_numbers.png")


# ---------- how much information is in a picture ----------

def png_size_kb(array):
    buffer = io.BytesIO()
    Image.fromarray(array).save(buffer, format="PNG", optimize=True)
    return buffer.tell() / 1e3


def make_information():
    n = 256
    palette = [(214, 40, 40), (26, 95, 180), (240, 192, 32), (34, 34, 34)]

    # stripes: 16 bands of 16 px, four colours repeating
    stripes = np.zeros((n, n, 3), dtype=np.uint8)
    for i in range(n // 16):
        stripes[:, i * 16:(i + 1) * 16] = palette[i % 4]

    # the painting: the face, resized to the same 256 x 256
    im = Image.open(VERMEER).convert("RGB")
    painting = np.asarray(im.crop((520, 560, 1220, 1260)).resize((n, n), Image.LANCZOS))

    # noise: three random bytes per pixel, from seed 42
    rng = np.random.default_rng(42)
    noise = rng.integers(0, 256, size=(n, n, 3), dtype=np.uint8)

    panels = [("stripes", stripes), ("a painting", painting), ("random noise (seed 42)", noise)]
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5))
    for ax, (title, array) in zip(axes, panels):
        ax.imshow(array, interpolation="nearest")
        ax.set_title(title)
        ax.set_xlabel(f"{n} × {n} pixels, saved as PNG: {png_size_kb(array):.1f} kB", color=GRAY)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor("#DDDDDD")
    fig.tight_layout()
    save(fig, "intro_information.png")


# ---------- deterministic is not predictable ----------

def logistic(x0, r=3.9, steps=60):
    xs = [x0]
    for _ in range(steps):
        xs.append(r * xs[-1] * (1 - xs[-1]))
    return xs


def make_chaos():
    fig, ax = plt.subplots(1, 1, figsize=(13.5, 4.2))
    for x0, color in [(0.3, BLUE), (0.3001, RED)]:
        ax.plot(logistic(x0), marker="o", markersize=3.5, linewidth=1.6, color=color, label=f"start at {x0}")
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("step")
    ax.set_ylabel("x")
    ax.set_title("the same rule, x → 3.9 · x · (1 − x), from two starting values that differ by 0.0001")
    ax.legend(loc="lower left", frameon=False)
    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "intro_chaos.png")


# ---------- where does a computer get randomness ----------

def random_walk(seed, steps=400):
    random.seed(seed)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    x, y = 0, 0
    xs, ys = [x], [y]
    for _ in range(steps):
        dx, dy = random.choice(directions)
        x, y = x + dx, y + dy
        xs.append(x)
        ys.append(y)
    return xs, ys


def make_seeds():
    walks = [(seed, color, random_walk(seed)) for seed, color in [(0, BLUE), (0, BLUE), (1, RED)]]
    # one square window for all three panels, so equal walks look equal
    span = max(max(max(xs) - min(xs), max(ys) - min(ys)) for _, _, (xs, ys) in walks) + 4

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5))
    for ax, (seed, color, (xs, ys)) in zip(axes, walks):
        ax.plot(xs, ys, color=color, linewidth=1.2)
        ax.plot(xs[0], ys[0], "o", color="#222222", markersize=6)
        ax.set_title(f"400 random steps, seed = {seed}")
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        ax.set_xlim(cx - span / 2, cx + span / 2)
        ax.set_ylim(cy - span / 2, cy + span / 2)
        for spine in ax.spines.values():
            spine.set_edgecolor("#DDDDDD")
    fig.tight_layout()
    save(fig, "intro_seeds.png")


if __name__ == "__main__":
    make_numbers()
    make_information()
    make_chaos()
    make_seeds()
