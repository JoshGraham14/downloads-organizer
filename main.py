import os

# Replace with absolute path to Downloads folder
BASE_PATH: str = './test_folder'

def main():
    os.chdir(BASE_PATH)
    if 'Recent' in os.listdir():
        print('Found the Recent folder')
    else:
        os.mkdir('Recent')
    print(os.listdir())

if __name__ == '__main__':
    main()