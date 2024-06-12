import pickle
import Composition
from Audio_Generator import composition_to_audio
from Composition_Generator import generate_random_composition

print('Hey! Welcome to generator of random sounds!')
while True:
    print('Please, enter <GENERATE> to generate new random sound, <LOAD> to load the sound or something else to leave the program')
    command = input()
    if command == 'GENERATE':
        print('Your composition is preparing...')

        random_composition = generate_random_composition(10)
        composition_to_audio(random_composition, "resources/random_composition.wav")

        print('Your composition is ready! Enter <YES> if you want to save it')
        command_to_save = input()
        if command_to_save == 'YES':
            print('Please, enter the filename, where you want to save the audio')
            random_composition.save(input())
            print('Your audio saved!')
    elif command == 'LOAD':
        composition = Composition.Composition()

        print('Enter the filename with an audio, which you want to load')
        filename = input()
        try:
            composition.load(filename)
            print('File loaded!')
        except FileNotFoundError:
            print(f'File {filename} not found!')
        except pickle.UnpicklingError:
            print(f'Invalid format of file {filename}!')
    else:
        break
        