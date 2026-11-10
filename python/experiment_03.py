"""Experiment 3: Human Activity Recognition using Random Forest and SVM.
Expected extracted folder: data/UCI HAR Dataset/{train,test}/...
"""
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

root = Path("data/UCI HAR Dataset")
def read_features(split):
    return pd.read_csv(root / split / f"X_{split}.txt", sep=r"\\s+", header=None)
X_train, X_test = read_features("train"), read_features("test")
y_train = pd.read_csv(root / "train/y_train.txt", header=None).values.ravel()
y_test = pd.read_csv(root / "test/y_test.txt", header=None).values.ravel()
rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)
rf_pred = rf.predict(X_test)
print("Random Forest accuracy:", accuracy_score(y_test, rf_pred))
svm = SVC().fit(X_train, y_train)
svm_pred = svm.predict(X_test)
print("SVM accuracy:", accuracy_score(y_test, svm_pred))
print(classification_report(y_test, svm_pred))
