# Algorithmic Generative Art with Python

[![Read online](https://img.shields.io/badge/read-online-1B4B9B)](https://xyslong.github.io/generative-art-course/)
**Read this course as a website: <https://xyslong.github.io/generative-art-course/>**

A 15-week university course for art history students with no programming
background. Each 2-hour session pairs an art-historical framing with a
hands-on Python notebook that produces a visual artwork: you run the cells,
change the parameters, and take a finished image home. Sessions are ordered
by coding complexity — early weeks need only basic Python, later weeks build
on numpy, scipy, and image processing. The mathematics is always a means to
an aesthetic end.

## Syllabus

| Week | Title | Core method | Art anchor |
|-----:|-------|-------------|------------|
| 01 | Random Walks: The First Generative System | loops, randomness, plotting | Sol LeWitt, Georg Nees *Schotter*, Vera Molnár |
| 02 | Chance Operations and Controlled Randomness | distributions, seeding, weighted choice | Arp, Duchamp, Cage, Kelly, Richter |
| 03 | Geometric Patterns and Symmetry | trigonometry, rotation, tiling | Alhambra, girih tiles, Owen Jones, Escher |
| 04 | Recursion and Subdivision | recursive functions | Mondrian, De Stijl |
| 05 | Color: Spaces, Palettes, Extraction | RGB/HSV/LAB, k-means | Itten, Albers, Rothko |
| 06 | L-Systems and Botanical Form | string rewriting, turtle graphics | Merian, Besler, Haeckel, D'Arcy Thompson |
| 07 | Fractals: Infinite Detail | complex iteration, escape time | Mandelbrot, Hokusai, the Pollock controversy |
| 08 | Noise and Flow Fields | coherent noise, vector fields | Perlin, Tyler Hobbs *Fidenza* |
| 09 | Cellular Automata and Emergence | rule tables, Game of Life | Jacquard loom, Anni Albers, Conway |
| 10 | Reaction-Diffusion: Turing Patterns | Gray-Scott model | Turing 1952, Morris, Jugendstil ornament |
| 11 | Attention Made Visible: Gaussians, KDE, Heatmaps | kernel density estimation | Yarbus, museum eye tracking |
| 12 | Voronoi, Delaunay, and Stippling | tessellation, Lloyd relaxation | Seurat, mosaic, Secord stippling |
| 13 | Filters, Edges, and Dithering | convolution, Gabor, Floyd-Steinberg | Lichtenstein, halftone, glitch |
| 14 | Particles, Agents, and Flocking | Boids, simulation | Calder, Riley, teamLab, Reynolds 1987 |
| 15 | Synthesis: Systems, Authorship, Final Project | combining techniques | Boden, Molnár's late fame, the NFT arc |

## Setup

You need Python ≥ 3.10. Choose **one** of the three options below.

### Option A — conda (recommended)

```bash
conda env create -f environment.yml
conda activate genart
jupyter notebook
```

### Option B — plain pip

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

### Option C — Google Colab (no installation)

Every notebook also runs on [Google Colab](https://colab.research.google.com).
Open a notebook there and un-comment the first code cell, which clones this
repository and installs the two packages Colab is missing
(`opensimplex`, and `imageio` where needed).

## Input images (one-time step)

Weeks 5, 11, 12 and 13 work with real artworks. Nothing copyrighted is
stored in this repository; instead, a script downloads public-domain
paintings (Monet, Seurat, Vermeer, Hokusai) from Wikimedia Commons:

```bash
python assets/images/get_images.py
```

If you are offline, the script generates synthetic stand-in images so all
notebooks still run. It also generates `poster_demo.png`, the fake
conference poster used in week 11.

## How a session works

Open the week's notebook in `notebooks/` and run it top to bottom
(*Kernel → Restart & Run All* always works and takes under 5 minutes).
Each notebook follows the same arc: today's destination → art-historical
context → the mathematics, visualized → step-by-step build-up → a playground
of parameters → export your artwork → exercises.

Your exported images land in `assets/outputs/` — that folder is yours.

## Publishing (for the instructor)

The course is published as a [Jupyter Book](https://jupyterbook.org) on
GitHub Pages. Every push to `main` triggers the GitHub Action in
`.github/workflows/deploy.yml`: it installs the requirements, fetches the
input images, executes the notebooks (with an execution cache, so unchanged
notebooks are not re-run), builds the book, and deploys `_build/html` to the
`gh-pages` branch.

**To publish a new week:** add the notebook to `notebooks/`, uncomment its
line in `_toc.yml` (and its part caption, if the part is still commented),
run `python assets/site/make_hero.py` to refresh the landing-page hero, and
push.

**To build locally:**

```bash
pip install "jupyter-book>=1,<2"
jupyter-book build .
open _build/html/index.html
```

**Cell-tag convention:** a code cell that must not run during the site build
(e.g. a long render) gets the cell tag `skip-execution`. No cell in weeks
01–02 needs it; use it sparingly.

## License

Code is licensed under the MIT License. Text and teaching materials are
licensed under CC BY 4.0. Images generated by students belong to the
students who made them.
