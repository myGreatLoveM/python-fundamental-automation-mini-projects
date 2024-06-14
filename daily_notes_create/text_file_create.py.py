import os
import subprocess as sp
from datetime import datetime

def create_text_file():
    today = datetime.now()

    file_name = today.strftime("%d-%b-%y")

    BASE_DIR = os.getcwd()

    for file in os.listdir(BASE_DIR):
        filename, extension = os.path.splitext(file)
        if filename == file_name and extension == '.txt':
            print('file already exists')
            sp.Popen(['Notepad.exe', file])
            break

    with open(f'{file_name}.txt', 'w') as file:
        file.write('Write your bullet thoughts to get saved here')

if __name__ == '__main__':
    create_text_file()


