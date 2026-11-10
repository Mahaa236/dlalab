# Kaggle dataset setup

## 1. Install the downloader
Use Python 3.10–3.12 where supported by your TensorFlow version:

```bash
python -m pip install kagglehub
```

KaggleHub handles Kaggle authentication using your configured Kaggle credentials. If prompted, follow Kaggle's current authentication instructions. Do not commit API tokens, `kaggle.json`, passwords, or private credentials to GitHub.

## 2. Choose a dataset on Kaggle
Open Kaggle Datasets and select a dataset that actually contains the required files. The dataset URL usually looks like:

`https://www.kaggle.com/datasets/OWNER/DATASET-SLUG`

Use only `OWNER/DATASET-SLUG` in the environment variable. Dataset availability, licenses, file layouts, and terms may change, so inspect each dataset page before downloading.

Recommended file requirements:
- **Quora pairs:** `train.csv` with `question1`, `question2`, and `is_duplicate` columns.
- **Human Activity Recognition:** extracted UCI HAR layout containing `train/X_train.txt`, `train/y_train.txt`, `test/X_test.txt`, and `test/y_test.txt`.
- **Driving:** a Udacity-style `driving_log.csv` and matching image files, often under `IMG/`. After download, arrange these as `data/driving_log.csv` and `data/IMG/` for experiments 1 and 6.
- **MIDI:** one or more `.mid` files. Arrange them under `data/midi_files/`.

## 3. Set the dataset slug and download

Linux/macOS:
```bash
export KAGGLE_QUORA_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py quora

export KAGGLE_HAR_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py har

export KAGGLE_DRIVING_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py driving

export KAGGLE_MIDI_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py midi
```

Windows PowerShell:
```powershell
$env:KAGGLE_QUORA_DATASET="OWNER/DATASET-SLUG"
python datasets/kaggle_download.py quora
```
Repeat for the other environment variables and names shown above.

Install experiment dependencies as needed:
```bash
python -m pip install pandas numpy opencv-python scikit-learn nltk matplotlib seaborn tensorflow pretty_midi
```

**Important:** The downloader cannot guess which Kaggle dataset you intended. Replace each placeholder with a dataset slug you verified on Kaggle. After download, check file paths and terms. Large datasets should not be committed to this GitHub repository.
