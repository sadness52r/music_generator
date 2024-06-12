import numpy as np
from pydub import AudioSegment
from Composition import Composition

def generate_sine_wave(frequency: float, duration: float, sample_rate=44100, amplitude=0.5) -> AudioSegment:
    t = np.linspace(0, duration / 1000, int(sample_rate * (duration / 1000)), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t) * (2**15 - 1)
    wave = wave.astype(np.int16)
    return AudioSegment(
        wave.tobytes(),
        frame_rate=sample_rate,
        sample_width=wave.dtype.itemsize,
        channels=1
    )

def composition_to_audio(composition: Composition, filename: str) -> None:
    audio = AudioSegment.silent(duration=0)
    for note in composition.notes:
        note_audio = generate_sine_wave(note.freq, note.duration)
        audio += note_audio
    audio.export(filename, format="wav")