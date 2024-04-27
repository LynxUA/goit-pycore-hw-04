'''
Module that prints file structure
'''

import sys
from pathlib import Path
from colorama import Fore

def print_structure(path_str: str, shift=0):
    '''
    Recursive function that prints color file structure
    '''
    path = Path(path_str)
    if not path.is_dir():
        if not path.exists():
            print("Specified path doesn't exist")
        else:
            print(shift * " " + Fore.BLUE + path.name)
        return
    print(shift * " " + Fore.GREEN + path.name + "/")
    for subpath in path.iterdir():
        print_structure(subpath, shift + 3)

def main():
    '''
    Main function
    '''
    if len(sys.argv) != 2:
        print("The app should have only one argument (path)")
    print_structure(sys.argv[1])

if __name__ == "__main__":
    main()
