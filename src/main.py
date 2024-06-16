import pickle
import Composition
import Commands
import help_funcs
from config import FILENAME

if __name__ == '__main__':
    print('Hey! Welcome to generator of random sounds!')
    while True:
        print('Please, enter <GENERATE> to generate new random sound, <LOAD> to load the sound or something else to leave the program')
        command = input()
        if command == str(Commands.Commands.GENERATE.name):
            random_composition = help_funcs.create_composition(FILENAME)
            print('Enter <SAVE> if you want to save it')
            command_to_save = input()
            if command_to_save == str(Commands.Commands.SAVE.name):
                print('Please, enter the filename, where you want to save the audio')
                random_composition.save(input())
                print('Your audio saved!')
        elif command == str(Commands.Commands.LOAD.name):
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
        

# тесты (при одинаковых нотах должна быть одинаковая композиция)