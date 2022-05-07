import os

# Replace with absolute path to Downloads folder
BASE_PATH: str = 'test_folder'

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
    
    return needed_folders



def create_folders(needed_folders: list[str]) -> None:
    '''Creates the supplied folders in the current directory.'''
    for folder in needed_folders:
        os.mkdir(folder)


def main():
    print(os.listdir())
    os.chdir(BASE_PATH)
    needed_folders: list[str] = check_folders()
    create_folders(needed_folders)
    print(os.listdir())

if __name__ == '__main__':
    main()