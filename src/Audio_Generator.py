import numpy as np
from pydub import AudioSegment
from Composition import Composition

def generate_sine_wave(frequency: float, duration: float, sample_rate=44100, amplitude=0.5) -> AudioSegment:
    # распределённый диапазон точек от 0 до времени ноты в секундах. Кол-во точек выставляем в кол-во сэмплов на протяжении звука
    t = np.linspace(0, duration / 1000, int(sample_rate * (duration / 1000)), False)
    # формула синусоиды. Нормируем в диапазон от -1 до 1 с помощью sin, умножаем на амплитуду, чтобы отрегулировать высоту волны (громкость), и на 2*15 - 1, чтобы отмасштабировать волну, чтобы она подходила для 16 битного аудио
    wave = amplitude * np.sin(2 * np.pi * frequency * t) * (2**15 - 1)
    wave = wave.astype(np.int16)
    return AudioSegment(
        wave.tobytes(),
        frame_rate=sample_rate,
        # sample_width указывает на количество байтов, используемых для хранения каждого семпла
        # wave.dtype.itemsize возвращает размер в байтах одного элемента массива wave. Для 16-битного аудио это значение будет равно 2, поскольку каждый семпл занимает 2 байта
        sample_width=wave.dtype.itemsize,
        channels=1
    )

def composition_to_audio(composition: Composition, filename: str) -> None:
    # создаем пустой аудио-сегмен, с которого начинается композиция
    audio = AudioSegment.silent(duration=0)
    for note in composition.notes:
        note_audio = generate_sine_wave(note.freq, note.duration)
        audio += note_audio
    audio.export(filename, format="wav")