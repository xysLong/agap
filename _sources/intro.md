# Algorithmic Generative Art with Python

**For art historians learning mathematics and coding by reimplementation.**

![Artworks generated in these notes, chapters 0 to 26](assets/site/hero.jpg)

:::{note}
This is the course book for <a href="https://ufind.univie.ac.at/en/course.html?lv=080120&amp;semester=2026W"><em>Algorithmic Generative Art with Python</em> (course 080120)</a> at the University of Vienna, taught in the winter semester 2026/27 in the Master's programme in Art History. It is a work in progress and will keep changing as the course runs; corrections, suggestions, and feedback of any kind are warmly welcome at <a href="mailto:xingyu.long@univie.ac.at">xingyu.long@univie.ac.at</a>.
:::

## Why rebuild what already exists

This text asks you to reimplement, from scratch, systems whose outputs already hang
in museums. That is a method, not a detour. Archaeologists learned long ago that some
knowledge only surfaces when you rebuild the thing: casting a bronze axe or raising a
megalith exposes decisions, constraints, and skills that no amount of looking at the
finished object can recover <a class="cite" href="#ref-coles1973">(Coles 1973)</a>,
a practice of testing what we think we know about how things were made, known
as *experimental archaeology* <a class="cite" href="#ref-outram2008">(Outram 2008)</a>.
Making as a mode of inquiry has the same standing closer to home: building a working
version of a concept is itself a way of thinking the concept through, what Ratto calls
*critical making* <a class="cite" href="#ref-ratto2011">(Ratto 2011)</a>. Media studies
has drawn the same lesson under the name *media archaeology*: the media of the past are
understood not from the standard histories alone, but by digging into the neglected
machines, formats, and practices themselves
<a class="cite" href="#ref-huhtamo2011">(Huhtamo and Parikka 2011)</a>. Early computer
art, drawn by plotters from code that often survives only in print, in fragments,
or not at all, is exactly such a site.

Recoding Georg Nees's *Schotter* or a Vera Molnár series works in much the same way. Every
parameter your version needs before it runs (how much disorder, which stopping rule,
what line weight) is a question the original artist once answered, and *reimplementation*
turns you from a viewer of the answer into a witness of the decision. The images this
text has you generate are side products in the best sense: what you are actually
building is an understanding of the systems behind them, precise enough to run.

**References**

- <span id="ref-coles1973"></span>Coles, John M. *Archaeology by Experiment*. London: Hutchinson University Library, 1973.
- <span id="ref-huhtamo2011"></span>Huhtamo, Erkki, and Jussi Parikka, eds. *Media Archaeology: Approaches, Applications, and Implications*. Berkeley: University of California Press, 2011.
- <span id="ref-outram2008"></span>Outram, Alan K. "Introduction to Experimental Archaeology." *World Archaeology* 40, no. 1 (2008), 1-6. [doi:10.1080/00438240801889456](https://doi.org/10.1080/00438240801889456)
- <span id="ref-ratto2011"></span>Ratto, Matt. "Critical Making: Conceptual and Material Studies in Technology and Social Life." *The Information Society* 27, no. 4 (2011), 252-260. [doi:10.1080/01972243.2011.583819](https://doi.org/10.1080/01972243.2011.583819)

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
| 5 | [Color: Spaces, Palettes, Extraction](notebooks/05-color.ipynb) | RGB/HSV/LAB, k-means | Itten, Albers, Rothko |

### Part II · Growth and Iteration

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 6 | [Recursion and Subdivision](notebooks/06-recursion-and-subdivision.ipynb) | recursive functions | Mondrian, De Stijl |
| 7 | [L-Systems and Botanical Form](notebooks/07-l-systems.ipynb) | string rewriting, turtle graphics | Merian, Besler, Haeckel, D'Arcy Thompson |
| 8 | [Fractals: Infinite Detail](notebooks/08-fractals.ipynb) | complex iteration, escape time | Mandelbrot, Hokusai, the Pollock controversy |
| 9 | [Strange Attractors: The Shape of Chaos](notebooks/09-strange-attractors.ipynb) | iterated 2D maps, density rendering | Lorenz, Gleick, Pickover, de Jong |

### Part III · Fields and Grids

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 10 | [Noise and Flow Fields](notebooks/10-noise-and-flow-fields.ipynb) | coherent noise, vector fields | Perlin, Tyler Hobbs *Fidenza* |
| 11 | [Deeper Noise: Cells, Ridges, and Warped Space](notebooks/11-deeper-noise.ipynb) | Worley noise, ridged fbm, domain warping | Ebru marbling, Worley, Musgrave, Quilez |
| 12 | [Curl and the Endless Loop: Fields in Motion](notebooks/12-curl-and-loops.ipynb) | curl noise, seamless loops | Bridson, phenakistiscope, the GIF |
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
| 22 | [Differential Growth: The Restless Line](notebooks/22-differential-growth.ipynb) | neighbor forces, node insertion | Nervous System, Anders Hoff, kale and coral |
| 23 | [Evolving Images: Breeding as Composition](notebooks/23-evolving-images.ipynb) | mutation, selection by eye | Dawkins, Latham, Sims |

### Part VI · Coda

| Ch. | Title | Core method | Art anchor |
|----:|-------|-------------|------------|
| 24 | [Attention Made Visible: Gaussians, KDE, Heatmaps](notebooks/24-heatmaps.ipynb) | kernel density estimation | Yarbus, museum eye tracking |
| 25 | [The Sounding Image: From Pixels to Sound](notebooks/25-the-sounding-image.ipynb) | additive synthesis, spectrogram | Kandinsky, Fischinger, Xenakis |
| 26 | [The Plotted Line: Vector Graphics and the Machine's Hand](notebooks/26-the-plotted-line.ipynb) | SVG, line displacement, hatching | Molnár, Nake, the pulsar plot |
| 27 | [Synthesis: Systems, Authorship, and the Final Project](notebooks/27-synthesis.ipynb) | combining techniques | Boden, Molnár's late fame, the NFT arc |

## How to use these notes

Every chapter is a fully executed notebook: all generated art is embedded,
and reading online requires no installation.

Each chapter opens with a Context section on the artists and ideas behind its
technique and closes with further reading and references; these are reference
material, meant for reading the way you would read the wall texts of an exhibition.
The working core of a chapter (the mathematics, the code, the images, the exercises)
is sized for roughly one 90-minute session.

## How to cite

If you use these notes in your research or teaching, please cite them as:

> Long, Xingyu. *Algorithmic Generative Art with Python.* Lecture notes,
> University of Vienna, 2026. https://xyslong.github.io/agap/

```bibtex
@misc{long2026agap,
  author = {Long, Xingyu},
  title  = {Algorithmic Generative Art with Python},
  year   = {2026},
  url    = {https://xyslong.github.io/agap/}
}
```

---

Code is licensed under the [MIT License](https://opensource.org/license/mit), text under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quotations from other authors,
reproductions of artworks, and the eye-tracking data in `assets/data/` are excluded from
these licenses; the underlying dataset is published separately on
[Zenodo](https://doi.org/10.5281/zenodo.21983283) under CC BY 4.0.

Painting reproductions: Claude Monet, *Water Lilies* (1906), Art Institute of Chicago;
Georges Seurat, *A Sunday on La Grande Jatte* (1884-86), Art Institute of Chicago;
Johannes Vermeer, *Girl with a Pearl Earring* (c. 1665), Mauritshuis, The Hague;
Katsushika Hokusai, *The Great Wave off Kanagawa* (c. 1830-32), Metropolitan Museum of Art;
Wassily Kandinsky, *Yellow-Red-Blue* (1925), Centre Pompidou, Paris. All five works are in
the public domain; reproductions via Wikimedia Commons.
