# Deep Learning Lab Experiments

Repository: https://github.com/Mahaa236/dlalab

This repository provides six Jupyter notebooks, six matching standalone Python scripts, and dataset download helpers.

## Jupyter notebooks
- [Experiment 1 — Steering Angle Prediction](notebooks/experiment_01.ipynb)
- [Experiment 2 — Quora Question Pair Similarity](notebooks/experiment_02.ipynb)
- [Experiment 3 — Human Activity Recognition](notebooks/experiment_03.ipynb)
- [Experiment 4 — Character-Level LSTM Music Generation (ABC)](notebooks/experiment_04.ipynb)
- [Experiment 5 — LSTM Music Generation from MIDI](notebooks/experiment_05.ipynb)
- [Experiment 6 — Self-Driving Car CNN Baseline](notebooks/experiment_06.ipynb)

## Standalone Python scripts
- [Experiment 1](python/experiment_01.py)
- [Experiment 2](python/experiment_02.py)
- [Experiment 3](python/experiment_03.py)
- [Experiment 4](python/experiment_04.py)
- [Experiment 5](python/experiment_05.py)
- [Experiment 6](python/experiment_06.py)

## Kaggle datasets
Read [dataset setup instructions](datasets/README.md) and use the [download helper](datasets/kaggle_download.py).

Install the dependencies:
```bash
python -m pip install -r requirements.txt
```

For Quora Question Pairs, first sign in to Kaggle, configure the Kaggle CLI, and accept the competition rules at https://www.kaggle.com/c/quora-question-pairs/data. Then run:
```bash
python datasets/kaggle_download.py quora
```

For HAR, driving, and MIDI datasets, choose a Kaggle dataset whose files match the experiment and set the corresponding environment variable to its real `OWNER/DATASET-SLUG`. Exact commands and expected file layouts are in [datasets/README.md](datasets/README.md). The downloader cannot safely guess the right dataset for you.

## Important
- Downloaded datasets are not committed to this repository; many are large and have separate terms/licenses.
- Never commit Kaggle credentials or API tokens.
- Check file layout and update paths after downloading.
- Model metrics and outputs are generated when you run each script; they are not guaranteed in advance.
