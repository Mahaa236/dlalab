"""Download Kaggle datasets with kagglehub.

1. Accept Kaggle's terms and configure your Kaggle account/API credentials.
2. Find a dataset on kaggle.com/datasets/OWNER/SLUG.
3. Set the matching environment variable to OWNER/SLUG (not the full URL).
4. Run: python datasets/kaggle_download.py quora
   Or: python datasets/kaggle_download.py har
   Or: python datasets/kaggle_download.py driving
   Or: python datasets/kaggle_download.py midi

This uses kagglehub, which downloads into its cache. The script then copies files
into this repo's data/ folder so the experiment scripts can find them.
Only use datasets you have permission to download; review license and terms.
"""
import os, sys, shutil
from pathlib import Path
import kagglehub

ROOT = Path(__file__).resolve().parents[1]
DESTS = {
    "quora": ("KAGGLE_QUORA_DATASET", ROOT / "data" / "quora", "Quora Question Pairs dataset"),
    "har": ("KAGGLE_HAR_DATASET", ROOT / "data" / "UCI HAR Dataset", "UCI Human Activity Recognition dataset"),
    "driving": ("KAGGLE_DRIVING_DATASET", ROOT / "data" / "driving", "Udacity-style self-driving/driving log dataset"),
    "midi": ("KAGGLE_MIDI_DATASET", ROOT / "data" / "midi_files", "MIDI music dataset"),
}
def main():
    if len(sys.argv) != 2 or sys.argv[1] not in DESTS:
        print("Usage: python datasets/kaggle_download.py " + "|".join(DESTS))
        raise SystemExit(2)
    key = sys.argv[1]
    env, dest, label = DESTS[key]
    slug = os.getenv(env, "").strip()
    if not slug or "/" not in slug:
        print(f"Set {env} to OWNER/DATASET-SLUG from the Kaggle dataset URL.")
        print(f"Example format: {env}=owner/dataset-slug")
        raise SystemExit(2)
    print(f"Downloading {label}: {slug}")
    source = Path(kagglehub.dataset_download(slug))
    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for item in source.rglob("*"):
        if item.is_file():
            relative = item.relative_to(source)
            target = dest / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                shutil.copy2(item, target)
            count += 1
    print(f"Copied {count} files to {dest}")
    print("Check the extracted folder layout. Some Kaggle datasets package files in nested directories.")
if __name__ == "__main__":
    main()
