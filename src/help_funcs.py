from Audio_Generator import composition_to_audio
from Composition_Generator import generate_random_composition
from Composition import Composition
from config import NOTES_NUMBER

def create_composition(filename: str) -> Composition:
    print('Your composition is preparing...')

    random_composition = generate_random_composition(NOTES_NUMBER)
    composition_to_audio(random_composition, "resources/{filename}")

    print('Your composition is ready!')
    return random_composition
