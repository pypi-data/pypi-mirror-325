Berni
=====

[![pypi](https://img.shields.io/pypi/v/berni.svg)](https://pypi.python.org/pypi/berni/)
[![version](https://img.shields.io/pypi/pyversions/berni.svg)](https://pypi.python.org/pypi/berni/)
[![license](https://img.shields.io/pypi/l/berni.svg)](https://en.wikipedia.org/wiki/GNU_General_Public_License)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fframagit.org%2Fcoslo%2Fberni/HEAD?labpath=docs%2Findex.ipynb)
[![pipeline](https://framagit.org/coslo/berni/badges/master/pipeline.svg)](https://framagit.org/coslo/berni/badges/master/pipeline.svg)
[![coverage report](https://framagit.org/coslo/berni/badges/master/coverage.svg?job=test:f90)](https://framagit.org/coslo/berni/-/commits/master)

A database of interaction models and trajectory samples for molecular dynamics and Monte Carlo simulations. Berni can export interaction models to a range of simulation backends, such as `atooms`, `LAMMPS`, `RUMD`.

Quick start
-----------

Get info on the available models
```python
import berni
for model in berni.models:
    print(f'- "{model["name"]}": {model["description"]}')
```
```
- "bernu_hiwatari_hansen_pastore": Binary soft-sphere mixture with size ratio of 1.4
- "coslovich_pastore": Short-ranged pairwise-additive model for silica
- "dellavalle_gazzillo_frattini_pastore": Binary Lennard-Jones mixture model for NiY alloys
- "gaussian_core": One-component Gaussian core model with long-range cutoff
- "grigera_cavagna_giardina_parisi": Binary soft-sphere mixture with size ratio of 1.2 and smooth cutoff
- "harmonic_spheres": Binary mixture of harmonic spheres with size ratio of 1.4
- "kob_andersen": Binary Kob-Andersen Lennard-Jones mixture
- "kob_andersen_2": Ternary Kob-Andersen Lennard-Jones mixture
- "lennard_jones": One-component Lennard-Jones model
- "roux_barrat_hansen": Binary soft-sphere mixture with size ratio of 1.2
- "roy_heyde_heuer-II": Variant of roy_heyde_heuer with optimized parameters               
- "roy_heyde_heuer": 2d model of a silica bilayer
- "wahnstrom": Binary Lennard-Jones mixture with size ratio of 1.2
```

Get a specific model as a dictionary in the default schema
```python
berni.models.get("lennard_jones")
```

Print the qualified names of the available samples
```python
for sample in berni.samples():
    print(sample["path"])
```
```
coslovich_pastore-488db481cdac35e599922a26129c3e35.xyz
lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz
roy_heyde_heuer-II-b8d70742799933357ea83314590d2b4d.xyz
lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz
kob_andersen-8f4a9fe755e5c1966c10b50c9a53e6bf.xyz
bernu_hiwatari_hansen_pastore-f61d7e58b9656cf9640f6e5754441930.xyz
grigera_cavagna_giardina_parisi-0ac97fa8c69c320e48bd1fca80855e8a.xyz

```

Get a local copy of a Lennard-Jones fluid sample
```python
local_file = berni.samples.get("lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz")
```

The `local_file` can then be used to start a simulation or further analysis.

Export a model for a simulation backend
```python
berni.models.export("kob_andersen", backend='lammps')
```
```
pair_style lj/cut 1.0
pair_coeff 1 1 1.0 1.0 2.5
pair_coeff 1 2 1.5 0.8 2.0
pair_coeff 2 2 0.5 0.88 2.2
pair_modify shift yes
```

Documentation
-------------
Check out the [documentation](https://coslo.frama.io/berni) for full details.

Installation
------------
Clone the code repository and install from source
```
git clone https://framagit.org/coslo/berni.git
cd sample
make install
```

Install `berni` with pip
```
pip install berni
```

Contributing
------------
Contributions to the project are welcome. If you wish to contribute, check out [these guidelines](https://framagit.org/coslo/berni/-/blob/master/CONTRIBUTING.md).

Authors
-------
Daniele Coslovich: https://www.units.it/daniele.coslovich/
