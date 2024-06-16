from .Note import Note
import pickle


class Composition:
    def __init__(self, notes=None) -> None:
        if notes is None:
            notes = []
        self.notes = notes

    def add_note(self, note: Note) -> None:
        if not isinstance(note, Note):
            raise ValueError('Invalid argument type!')
        self.notes.append(note)

    def save(self, filename: str) -> None:
        with open(f'resources/{filename}', 'wb') as f:
            pickle.dump(self.notes, f)

    def load(self, filename: str) -> None:
        with open(f'resources/{filename}', 'rb') as f:
            self.notes = pickle.load(f)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Composition):
            raise TypeError("Операнд справа должен иметь тип Composition!")
        if len(self.notes) != len(other.notes):
            return False
        for i in range(len(self.notes)):
            if self.notes[i] != other.notes[i]:
                return False
        return True
