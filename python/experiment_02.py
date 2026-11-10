"""Experiment 2: Quora Question Pair Similarity (TF-IDF + Linear SVM).
Put Kaggle's train.csv in data/quora/train.csv or set QUORA_TRAIN_CSV.
"""
import os, re
from pathlib import Path
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

csv_path = Path(os.getenv("QUORA_TRAIN_CSV", "data/quora/train.csv"))
if not csv_path.exists():
    raise FileNotFoundError(f"Missing {csv_path}. Download the Quora Question Pairs dataset; see datasets/README.md.")
for resource in ("punkt", "punkt_tab", "stopwords"):
    nltk.download(resource, quiet=True)
df = pd.read_csv(csv_path).dropna(subset=["question1", "question2", "is_duplicate"])
stop_words, stemmer = set(stopwords.words("english")), PorterStemmer()
def clean(text):
    words = word_tokenize(re.sub(r"[^a-zA-Z\\s]", " ", str(text).lower()))
    return " ".join(stemmer.stem(w) for w in words if w not in stop_words)
q1, q2 = df["question1"].map(clean), df["question2"].map(clean)
X = TfidfVectorizer(max_features=50000, ngram_range=(1, 2)).fit_transform(q1 + " " + q2)
y = df["is_duplicate"].astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
model = LinearSVC().fit(X_train, y_train)
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
