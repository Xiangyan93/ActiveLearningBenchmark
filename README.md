# ActiveLearningBenchmark

Reproducibility materials for the MolALKit active-learning benchmark study.
The repository contains the benchmark input splits, processed figure inputs,
and Jupyter notebooks used to generate the manuscript figures and supporting
statistics.

## Software

The benchmark used [MolALKit v0.10.1](https://pypi.org/project/molalkit/0.10.1/).
Install the analysis environment with:

```bash
python -m pip install -r requirements.txt
```

## Repository layout

- `datasets/`: benchmark input splits used in the included analyses.
- `data/processed/`: figure inputs and statistical-analysis tables.
- `figures/`: one notebook for each main and supplementary figure.
- `scripts/`: data validation and notebook-execution helpers.

## Data access

The four scenario-summary tables, `cv.csv`, and correlation summary tables are
included directly in `data/processed/`. The larger paired active-learning
tables, `al.csv` and `yol.csv`, are distributed through the companion Zenodo
source-data archive because they exceed GitHub's standard file-size limit.

After downloading and unpacking the Zenodo archive, place its contents in
`data/processed/`, then run:

```bash
python scripts/verify_data.py
```

The public Zenodo DOI will be added to this README with the paper release.

## Reproducing figures

Run the notebooks from the `figures/` directory so their relative data paths
resolve correctly. For example:

```bash
cd figures
jupyter nbconvert --to notebook --execute --inplace figure2.ipynb
```

To execute the complete figure set, run:

```bash
bash scripts/run_figures.sh
```

The notebooks retain the typography settings used for manuscript production.
If Arial font files are unavailable locally, configure a metric-compatible font
before executing notebooks that reference `figures/fonts/`.

## Scope

This release supports reproduction of the processed analyses, reported
statistics, and manuscript figures. The benchmark input datasets are included
here; original dataset sources should be cited as described in the manuscript.
