# Deep Learning Lab Experiments

Repository: https://github.com/Mahaa236/dlalab

This repository provides **Jupyter notebooks** and matching **standalone Python scripts** for the six lab experiments, plus a configurable Kaggle dataset downloader.

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

## Kaggle dataset download
- [Kaggle setup and dataset requirements](datasets/README.md)
- [Download helper script](datasets/kaggle_download.py)

### Quick setup
```bash
python -m pip install -r requirements.txt
```

Choose a Kaggle dataset whose files match the experiment, accept its terms, and configure Kaggle authentication as described in `datasets/README.md`. Then set the appropriate environment variable to the dataset's `OWNER/DATASET-SLUG` and run, for example:

```bash
# Linux/macOS example
export KAGGLE_QUORA_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py quora
```

The placeholder must be replaced with a real dataset slug from Kaggle. The downloader does not choose or verify a specific dataset for you. Check the resulting file structure and update paths if the Kaggle dataset uses a different layout.

## Dataset notes
- Quora Question Pairs needs a `train.csv` with `question1`, `question2`, and `is_duplicate`.
- Human Activity Recognition needs the UCI HAR train/test text-file structure.
- Steering experiments need a compatible driving log and image set.
- MIDI generation needs `.mid` files.
- Datasets are not stored in this repository; avoid committing large datasets or credentials.

These are educational baselines. Model metrics and outputs are generated when you run the code and are not guaranteed in advance.
