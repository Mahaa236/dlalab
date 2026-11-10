"""Experiment 4: Character-level LSTM music generation in ABC notation."""
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

text = """X:1
T:Simple Tune
M:4/4
L:1/4
K:C
C D E F | G A B c |
c B A G | F E D C |
"""
chars = sorted(set(text))
to_id = {c: i for i, c in enumerate(chars)}
to_char = {i: c for c, i in to_id.items()}
seq_len = 20
encoded = [to_id[c] for c in text]
X, y = [], []
for i in range(len(encoded) - seq_len):
    X.append(encoded[i:i + seq_len])
    y.append(encoded[i + seq_len])
X, y = np.asarray(X), np.asarray(y)
model = Sequential([Embedding(len(chars), 32), LSTM(64), Dense(len(chars), activation="softmax")])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
model.fit(X, y, epochs=30, verbose=1)
sequence, generated = encoded[:seq_len], ""
for _ in range(200):
    probabilities = model.predict(np.asarray([sequence]), verbose=0)[0]
    nxt = int(np.random.choice(len(chars), p=probabilities / probabilities.sum()))
    generated += to_char[nxt]
    sequence = sequence[1:] + [nxt]
header = text[:text.find("C D E F")]
Path = __import__("pathlib").Path
Path("generated_music.abc").write_text(header + generated, encoding="utf-8")
print("Wrote generated_music.abc")
print("Optional MIDI conversion: abc2midi generated_music.abc -o generated_music.mid")
