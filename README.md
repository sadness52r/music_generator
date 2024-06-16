Приложение генерирует мелодию случайной длины из случайных нот.
При запуске программы можно ввести слово **GENERATE** и тогда автоматически сгенерируется случайная мелодия. Её можно будет сохранить, набрав в поле **YES**, и затем указать имя файла, в который желаем сохранить данную мелодию.
Также можно загрузить уже существующую мелодию, набрав **LOAD** (правда дальнейшее применение не придумано), или просто завершить программу, набрав в поле ввода что-то другое.

Основными единицами программы являются два класса:
# Класс Note
Этот класс по сути своей просто описывают ноту и не имеет методов:
```python
class Note:
    def __init__(self, name: str, duration: float, freq: float) -> None:
        self.name = name
        self.duration = duration
        self.freq = freq
```
# Класс Composition
Этот класс описывает композицию, состоящую из нот. Ноты хранятся в списке.
```python
class Composition:
    def __init__(self, notes=[]) -> None:
        self.notes = notes
```
Также этот класс имеет такие методы, как `save`, `load` и `add_note`.
Первые два метода нужны для сохранения композиции в файл и её загрузки из файла соответственно. Метод `add_note` позволяет добавить очередную ноту в список нот текущей композиции.
```python
import pickle
def add_note(self, note: Note) -> None:
        if not isinstance(note, Note.Note):
            raise ValueError('Invalid argument type!')
        self.notes.append(note)
  

    def save(self, filename: str) -> None:
        with open(f'resources/{filename}', 'wb') as f:
            pickle.dump(self.notes, f)

  
    def load(self, filename: str) -> None:
        with open(f'resources/{filename}', 'rb') as f:
            self.notes = pickle.load(f)
```
Для сериализации я использовал модуль *pickle*.
# Audio_Generator
В этом файле содержится набор методов, которые создают конкретную мелодию из списка нот. Для генерации мелодии из нот я использовал модуль *pydub*.
## Функция generate_sine_wave
Эта функция отвечает за создание синусоиды конкретной ноты. Так как мы хотим создать мелодию из набора нот, нам нужно знать, как описывать их формально. Для этого нота переводится в синусоиду. 
```python
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
```
## Функция composition_to_audio
Эта функция уже непосредственно перебирает все пришедшие ноты и создаёт для каждой синусоиду. Затем эта синусоида (обёрнутая в специальный объект `AudioSegment`) добавляется к общей мелодии и происходит создание `WAV` файла в папке `resources`. 
```python
def composition_to_audio(composition: Composition, filename: str) -> None:
    # создаем пустой аудио-сегмент, с которого начинается композиция
    audio = AudioSegment.silent(duration=0)
    for note in composition.notes:
        note_audio = generate_sine_wave(note.freq, note.duration)
        audio += note_audio
    audio.export(filename, format="wav")
```
# Composition_Generator
Этот файл отвечает за создание случайной композиции.
Я поместил сюда *словарь* со всеми значениями нот и частотами, на которых они адекватно звучат (спасибо [VolhvPorechja](https://github.com/VolhvPorechja)за предоставленную частотную карту из занятия по *numpy*).
## Функция generate_random_note
Данная функция генерирует случайную ноту (выбирает случайную из частотной карты), а также случайно выбирает длительность этой ноты (я ставлю от 1 до 8 секунд).
```python
def generate_random_note() -> Note:
    note_name = np.random.choice(list(notes_frequencies.keys()))
    note_freq = notes_frequencies[note_name]
    duration = np.random.uniform(1000, 8000)
    return Note.Note(note_name, duration, note_freq)
```
## Функция generate_random_composition
Заранее задаётся кол-во нот, которое мы хотим иметь в итоговой композиции, генерируется каждая нота случайно, и на основе этих нот строится новая композиция.
```python
def generate_random_composition(num_notes: int):
    composition = Composition.Composition()
    for _ in range(num_notes):
        composition.add_note(generate_random_note())
    return composition
```