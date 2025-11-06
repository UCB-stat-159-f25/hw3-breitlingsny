[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wOo27OxG)

# HW 3: From Notebooks to Research Packages, Part II

_This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Fall 2025 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science](https://ucb-stat-159-f25.github.io/site/). Authorship of the original analysis code rests with the LIGO collaboration._

LIGO is an acronym for Laser Interferometer Gravitational-wave Observatory. This repository includes a tutorial for the detection of a gravitational wave signal using real data from LIGO detectors. All outputs are saved to the data, figures, and audio folder. This repository now also contains a bit more structure, tests, documentation, in comparison to the repository for Homework 2.

## Contents
- `LOSC_Event_tutorial.ipynb` — main notebook where all analysis is done. This notebook goes through some typical signal processing tasks on strain time-series data associated with the LIGO Event data releases.
- `ligotools/` — functions used for filtering, whitening, and plotting
    - `readligo.py` — This module provides tools for reading LIGO data files.
    - `utils.py` — This module provides additional functions for processing and plotting LIGO data
- `data/` — waveform data (downloaded or generated during the notebook)
    - The `.hdf5` files contains the LIGO data itself. H1 and L1 refer to the two main LIGO detectors. 
    - The `.json` file contains the event properties
- `figures/` — plots and output visualizations
- `audio/` — audio representations of the gravitational wave signal

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/hw3-breitlingsny/main)