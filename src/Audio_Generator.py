import numpy as np
from pydub import AudioSegment
from Composition import Composition
from config import DEFAULT_SAMPLE_RATE, DEFAULT_AMPLITUDE, MAX_INT16


def generate_sine_wave(frequency: float, duration: float, sample_rate=DEFAULT_SAMPLE_RATE, amplitude=DEFAULT_AMPLITUDE) -> AudioSegment:
    t = np.linspace(0, duration / 1000, int(sample_rate * (duration / 1000)), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t) * MAX_INT16
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
        audio += generate_sine_wave(note.freq, note.duration)
    audio.export(filename, format="wav")
