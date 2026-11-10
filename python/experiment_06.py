"""Experiment 6: Self-driving car baseline (dataset selection + CNN).
Uses the same Udacity-style driving_log.csv/images structure as Experiment 1.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

data = Path("data")
log = data / "driving_log.csv"
if not log.exists():
    raise FileNotFoundError("Expected data/driving_log.csv and data/IMG/. See datasets/README.md.")
df = pd.read_csv(log, header=None)
df.columns = ["center", "left", "right", "steering", "throttle", "brake", "speed"]
images, angles = [], []
for _, row in df.iterrows():
    path = data / "IMG" / Path(str(row["center"])).name
    img = cv2.imread(str(path))
    if img is None:
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img[60:135], (200, 66))
    images.append(img.astype("float32") / 255.0)
    angles.append(float(row["steering"]))
if not images:
    raise RuntimeError("No images found. Check image paths and dataset extraction.")
X_train, X_test, y_train, y_test = train_test_split(np.asarray(images), np.asarray(angles), test_size=0.2, random_state=42)
model = Sequential([Conv2D(24, 5, strides=2, activation="relu", input_shape=(66,200,3)), Conv2D(36,5,strides=2,activation="relu"), Flatten(), Dense(64,activation="relu"), Dense(1)])
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1)
print("Test MSE:", model.evaluate(X_test, y_test))
