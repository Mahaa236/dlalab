"""Experiment 5: LSTM music generation from MIDI note pitches.
Place .mid files under data/midi_files/ before running.
"""
from pathlib import Path
import numpy as np
try:
    import pretty_midi
except ImportError as exc:
    raise SystemExit("Install pretty_midi first: pip install pretty_midi") from exc
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

notes = []
for file in Path("data/midi_files").glob("*.mid"):
    midi = pretty_midi.PrettyMIDI(str(file))
    for instrument in midi.instruments:
        notes.extend(note.pitch for note in instrument.notes)
if len(notes) <= 16:
    raise ValueError("Add MIDI files with more than 16 note events to data/midi_files/.")
seq_len = 16
X = np.asarray([notes[i:i+seq_len] for i in range(len(notes)-seq_len)], dtype=np.int32)
y = np.asarray([notes[i+seq_len] for i in range(len(notes)-seq_len)], dtype=np.int32)
model = Sequential([Embedding(128, 32), LSTM(64), Dense(128, activation="softmax")])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")
model.fit(X, y, epochs=10, verbose=1)
sequence, generated = list(notes[:seq_len]), []
for _ in range(100):
    p = model.predict(np.asarray([sequence]), verbose=0)[0]
    pitch = int(np.random.choice(128, p=p / p.sum()))
    generated.append(pitch)
    sequence = sequence[1:] + [pitch]
midi_out = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=0)
for i, pitch in enumerate(generated):
    instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=i*0.5, end=i*0.5+0.4))
midi_out.instruments.append(instrument)
midi_out.write("generated_midi.mid")
print("Wrote generated_midi.mid")
