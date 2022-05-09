import os
import re

# Replace with absolute path to Downloads folder
BASE_PATH: str = 'test_folder'
IMG_FILE_TYPES: list[str] = ['png', 'jpg', 'jpeg', 'gif', 'raw', 'svg']
COMP_FILE_TYPES: list[str] = ['zip', 'rar', 'tar', '7z']


def check_folders() -> list[str]:
    '''Return a list of needed folders for the Downloads directory.'''
    needed_folders: list[str] = []
    directory: list[str] = os.listdir()
    if 'Recent' not in directory:
        needed_folders.append('Recent')
    if 'Images' not in directory:
        needed_folders.append('Images')
    if 'Executables' not in directory:
        needed_folders.append('Executables')
    if 'Zipped' not in directory:
        needed_folders.append('Zipped')
    if 'PDFs' not in directory:
        needed_folders.append('PDFs')

    return needed_folders


def create_folders(needed_folders: list[str]) -> None:
    '''Creates the supplied folders in the current directory.'''
    for folder in needed_folders:
        os.mkdir(folder)


def sort_files() -> None:
    directory: list[str] = os.listdir()
    print(f'\.({"|".join(IMG_FILE_TYPES)})$')
    for f in directory:
        if re.search(f'\.({"|".join(IMG_FILE_TYPES)})$', f.lower()):
            os.replace(f'{os.getcwd()}\{f}', f'{os.getcwd()}\Images\{f}')
        elif re.search(f'\.pdf$', f.lower()):
            os.replace(f'{os.getcwd()}\{f}', f'{os.getcwd()}\PDFs\{f}')
        elif re.search(f'\.({"|".join(COMP_FILE_TYPES)})$', f.lower()):
            os.replace(f'{os.getcwd()}\{f}', f'{os.getcwd()}\Zipped\{f}')


def main():
    os.chdir(BASE_PATH)
    needed_folders: list[str] = check_folders()
    create_folders(needed_folders)
    print(os.listdir())
    sort_files()


if __name__ == '__main__':
    main()
