import pytest
from src.Note import Note
from src.config import TEST_DURATION
from src.Composition import Composition
from src.Composition_Generator import notes_frequencies

def test_eq_compositions():
    composition1 = Composition()
    for key, val in notes_frequencies.items():
        composition1.add_note(Note(key, TEST_DURATION, val))
    composition2 = Composition()
    for key, val in notes_frequencies.items():
        composition2.add_note(Note(key, TEST_DURATION, val))
    assert composition1 == composition2
