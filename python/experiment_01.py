"""Experiment 1: Steering Angle Prediction Using Deep Learning.
Dataset expected at data/driving_log.csv and data/IMG/.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

DATA = Path("data")
df = pd.read_csv(DATA / "driving_log.csv", header=None)
df.columns = ["center", "left", "right", "steering", "throttle", "brake", "speed"]
X, y = [], []
for _, row in df.iterrows():
    image_path = DATA / "IMG" / Path(str(row["center"])).name
    image = cv2.imread(str(image_path))
    if image is None:
        continue
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image[60:135], (200, 66))
    X.append(image.astype("float32") / 255.0)
    y.append(float(row["steering"]))
if not X:
    raise FileNotFoundError("No images loaded. Check data/driving_log.csv and data/IMG/.")
X, y = np.asarray(X), np.asarray(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Sequential([
    Conv2D(24, (5, 5), strides=2, activation="relu", input_shape=(66, 200, 3)),
    Conv2D(36, (5, 5), strides=2, activation="relu"),
    Flatten(), Dense(100, activation="relu"), Dense(1)
])
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1)
print("Test MSE:", model.evaluate(X_test, y_test))
model.save("car_model.keras")
