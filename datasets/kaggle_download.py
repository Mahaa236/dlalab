"""Download experiment datasets into this repository's data/ folder.

Quora: uses the official Kaggle competition download (requires accepting its rules):
    python datasets/kaggle_download.py quora

Other datasets: set an environment variable to a Kaggle dataset OWNER/SLUG first:
    KAGGLE_HAR_DATASET="owner/dataset-slug" python datasets/kaggle_download.py har
    KAGGLE_DRIVING_DATASET="owner/dataset-slug" python datasets/kaggle_download.py driving
    KAGGLE_MIDI_DATASET="owner/dataset-slug" python datasets/kaggle_download.py midi

Never commit Kaggle credentials or downloaded datasets to GitHub.
"""
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESTS = {
    "har": ("KAGGLE_HAR_DATASET", ROOT / "data" / "UCI HAR Dataset", "Human Activity Recognition"),
    "driving": ("KAGGLE_DRIVING_DATASET", ROOT / "data" / "driving", "Driving log/images"),
    "midi": ("KAGGLE_MIDI_DATASET", ROOT / "data" / "midi_files", "MIDI files"),
}

def copy_tree(source: Path, dest: Path) -> int:
    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for item in source.rglob("*"):
        if item.is_file():
            target = dest / item.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                shutil.copy2(item, target)
            count += 1
    return count

def download_quora(dest: Path) -> None:
    """Download the official Quora Question Pairs competition files."""
    if shutil.which("kaggle") is None:
        raise SystemExit("Kaggle CLI missing. Install it with: python -m pip install kaggle")
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["kaggle", "competitions", "download", "-c", "quora-question-pairs", "-p", str(dest)],
        check=True,
    )
    # Kaggle CLI saves train.csv.zip; extract it so experiment_02.py can read train.csv.
    for archive in dest.glob("*.zip"):
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(dest)
    if not (dest / "train.csv").exists():
        print(f"Download completed to {dest}, but train.csv was not found at the top level.")
        print("Inspect the downloaded files and move train.csv to data/quora/train.csv if needed.")
    else:
        print(f"Quora training data ready at {dest / 'train.csv'}")

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"quora", *DESTS.keys()}:
        print("Usage: python datasets/kaggle_download.py quora|har|driving|midi")
        raise SystemExit(2)

    key = sys.argv[1]
    if key == "quora":
        download_quora(ROOT / "data" / "quora")
        return

    env, dest, label = DESTS[key]
    slug = os.getenv(env, "").strip()
    if not slug or "/" not in slug:
        raise SystemExit(
            f"Set {env} to a real Kaggle dataset OWNER/SLUG first. "
            f"Open a dataset page at https://www.kaggle.com/datasets/ and copy its owner/slug."
        )

    try:
        import kagglehub
    except ImportError as exc:
        raise SystemExit("Install kagglehub first: python -m pip install kagglehub") from exc

    print(f"Downloading {label}: {slug}")
    source = Path(kagglehub.dataset_download(slug))
    count = copy_tree(source, dest)
    print(f"Copied {count} files to {dest}")
    print("Check the extracted layout; adjust experiment paths if this dataset uses nested folders.")

if __name__ == "__main__":
    main()
