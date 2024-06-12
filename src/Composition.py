import Note
from typing import List
import pickle

class Composition:
    def __init__(self, notes=[]) -> None:
        self.notes = notes

    
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
