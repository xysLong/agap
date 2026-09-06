# Algorithmic Generative Art with Python

**A hands-on book teaching mathematics and Python through the making of generative art, written for art history students.**

![Artworks generated in this book](assets/site/hero.png)

## Chapters

### Prelude

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 0 | [Warming Up: Python and Mathematics from Zero](notebooks/00-warming-up.ipynb) | Python basics, notation, first matplotlib | stripe painting: Stella, Davis, Riley, Buren |

### Part I · Foundations

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 1 | [Random Walks: The First Generative System](notebooks/01-random-walks.ipynb) | loops, randomness, plotting | Sol LeWitt, Georg Nees *Schotter*, Vera Molnár |
| 2 | [Chance Operations and Controlled Randomness](notebooks/02-chance-and-randomness.ipynb) | distributions, seeding, weighted choice | Arp, Duchamp, Cage, Kelly, Richter |
| 3 | [Geometric Patterns and Symmetry](notebooks/03-geometric-patterns.ipynb) | trigonometry, rotation, tiling | Alhambra, girih tiles, Owen Jones, Escher |
| 4 | [Truchet Tiles: Chance on a Grid](notebooks/04-truchet-tiles.ipynb) | grid randomness, tile sets | Truchet 1704, Douat, Smith, *10 PRINT* |
| 5 | [Recursion and Subdivision](notebooks/05-recursion-and-subdivision.ipynb) | recursive functions | Mondrian, De Stijl |
| 6 | [Color: Spaces, Palettes, Extraction](notebooks/06-color.ipynb) | RGB/HSV/LAB, k-means | Itten, Albers, Rothko |

### Part II · Growth and Iteration

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 7 | [L-Systems and Botanical Form](notebooks/07-l-systems.ipynb) | string rewriting, turtle graphics | Merian, Besler, Haeckel, D'Arcy Thompson |
| 8 | [Fractals: Infinite Detail](notebooks/08-fractals.ipynb) | complex iteration, escape time | Mandelbrot, Hokusai, the Pollock controversy |
| 9 | Strange Attractors: The Shape of Chaos *(in preparation)* | iterated 2D maps, density rendering | Lorenz, Gleick, Pickover, de Jong |

### Part III · Fields and Grids

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 10 | [Noise and Flow Fields](notebooks/10-noise-and-flow-fields.ipynb) | coherent noise, vector fields | Perlin, Tyler Hobbs *Fidenza* |
| 11 | Deeper Noise: Cells, Ridges, and Warped Space *(in preparation)* | Worley noise, ridged fbm, domain warping | Ebru marbling, Worley, Musgrave, Quilez |
| 12 | Curl and the Endless Loop: Fields in Motion *(in preparation)* | curl noise, seamless loops | Bridson, phenakistiscope, the GIF |
| 13 | [Cellular Automata and Emergence](notebooks/13-cellular-automata.ipynb) | rule tables, Game of Life | Jacquard loom, Anni Albers, Conway |
| 14 | [Reaction-Diffusion: Turing Patterns](notebooks/14-reaction-diffusion.ipynb) | Gray-Scott model | Turing 1952, Morris, Jugendstil ornament |

### Part IV · The Image, Transformed

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 15 | [Voronoi, Delaunay, and Stippling](notebooks/15-voronoi-and-stippling.ipynb) | tessellation, Lloyd relaxation | Seurat, mosaic, Secord stippling |
| 16 | [Filters, Edges, and Dithering](notebooks/16-filters-and-dithering.ipynb) | convolution, Gabor, Floyd-Steinberg | Lichtenstein, halftone, glitch |
| 17 | [Pixel Sorting: The Aesthetics of the Glitch](notebooks/17-pixel-sorting.ipynb) | sorting, masks, interval detection | Paik, Menkman, Asendorf |
| 18 | [Circle Packing: The Portrait in Dots](notebooks/18-circle-packing.ipynb) | collision tests, greedy growth | Kandinsky, Kusama, the Apollonian gasket |

### Part V · Agents and Complexity

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 19 | [Particles, Agents, and Flocking](notebooks/19-particles-and-flocking.ipynb) | Boids, simulation | Calder, Riley, teamLab, Reynolds 1987 |
| 20 | [Aggregation: Growth by Random Walk](notebooks/20-diffusion-limited-aggregation.ipynb) | diffusion-limited aggregation | Bentley, Lichtenberg figures, Witten & Sander |
| 21 | [Physarum: The Trail-Laying Swarm](notebooks/21-physarum.ipynb) | agents coupled to a field | slime mold, Tero, Barnett, Jenson |
| 22 | Differential Growth: The Restless Line *(in preparation)* | neighbor forces, node insertion | Nervous System, Anders Hoff, kale and coral |
| 23 | [Evolving Images: Breeding as Composition](notebooks/23-evolving-images.ipynb) | mutation, selection by eye | Dawkins, Latham, Sims |

### Part VI · Coda

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 24 | [Attention Made Visible: Gaussians, KDE, Heatmaps](notebooks/24-heatmaps.ipynb) | kernel density estimation | Yarbus, museum eye tracking |
| 25 | [The Sounding Image: From Pixels to Sound](notebooks/25-the-sounding-image.ipynb) | additive synthesis, spectrogram | Kandinsky, Fischinger, Xenakis |
| 26 | [The Plotted Line: Vector Graphics and the Machine's Hand](notebooks/26-the-plotted-line.ipynb) | SVG, line displacement, hatching | Molnár, Nake, the pulsar plot |
| 27 | [Synthesis: Systems, Authorship, and the Final Project](notebooks/27-synthesis.ipynb) | combining techniques | Boden, Molnár's late fame, the NFT arc |

## How to use this book

Every chapter is a fully executed notebook: all generated art is embedded,
and reading online requires no installation.

## How to cite

If you use this book in your research or teaching, please cite it as:

> Long, Xingyu. *Algorithmic Generative Art with Python.* 2026.
> https://xyslong.github.io/agap/

```bibtex
@book{long2026agap,
  author = {Long, Xingyu},
  title  = {Algorithmic Generative Art with Python},
  year   = {2026},
  url    = {https://xyslong.github.io/agap/}
}
```

---

Code is licensed under the MIT License; text under CC BY 4.0. Images
generated by students belong to the students who made them.
