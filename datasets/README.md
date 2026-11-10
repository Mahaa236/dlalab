# Kaggle dataset setup

## Install tools
```bash
python -m pip install kaggle kagglehub
```

Configure Kaggle authentication using Kaggle's current account/API instructions. Never upload `kaggle.json`, API tokens, or credentials to GitHub.

## Experiment 2 — Quora Question Pairs
The official [Quora Question Pairs Kaggle competition](https://www.kaggle.com/c/quora-question-pairs/data) contains `train.csv` with `question1`, `question2`, and `is_duplicate`. You must sign in and accept the competition rules before downloading.

```bash
python datasets/kaggle_download.py quora
```

This uses the Kaggle CLI, downloads the competition archive to `data/quora/`, and extracts it. The file should end up at `data/quora/train.csv`, which is the default path for `python/experiment_02.py`.

## Experiments 1 and 6 — driving images and steering log
Choose a Kaggle dataset whose files include an Udacity-style `driving_log.csv` and matching center-camera images. The experiment code expects:
- `data/driving_log.csv`
- `data/IMG/`

Pick a dataset after checking its file layout and license. Then set the dataset's actual Kaggle owner/slug.

Linux/macOS:
```bash
export KAGGLE_DRIVING_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py driving
```

Windows PowerShell:
```powershell
$env:KAGGLE_DRIVING_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py driving
```

After download, move/rename files to the exact paths above if the dataset has nested folders.

## Experiment 3 — Human Activity Recognition
Choose a Kaggle dataset containing the original UCI HAR train/test files. The expected layout is `data/UCI HAR Dataset/train/X_train.txt`, `train/y_train.txt`, `test/X_test.txt`, and `test/y_test.txt`.

```bash
export KAGGLE_HAR_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py har
```

Verify the dataset contents before running. An official alternative is the [UCI HAR dataset page](https://archive.ics.uci.edu/dataset/240/human%2Bactivity%2Brecognition%2Busing%2Bsmartphones), but that is not a Kaggle URL.

## Experiment 5 — MIDI music
Choose a Kaggle dataset that contains `.mid` files, then set the actual dataset slug:

```bash
export KAGGLE_MIDI_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py midi
```

The downloader copies the downloaded files into `data/midi_files/`. If the MIDI files are nested inside folders, the experiment script currently searches only the top-level folder; move the MIDI files there or adjust the script to search recursively.

## Dependencies
Install the experiment libraries from the repository root:

```bash
python -m pip install -r requirements.txt
```

Some datasets are large and may require Kaggle account access or acceptance of terms. This repository deliberately does not store datasets. Dataset owner/slug placeholders must be replaced with a real Kaggle dataset you have checked; dataset contents, licensing, and layout vary.
