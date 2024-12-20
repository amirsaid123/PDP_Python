import os
from pathlib import Path
# current_dir =os.getcwd()
# print(current_dir)

# os.chdir('D:\PDP Python\Modul_2')

# files = os.listdir(".")
# print(files)

# os.mkdir("new_folder")

# path = Path(__file__).resolve()
# print(path)

# path = Path(__file__)
# absolute_path = Path(__file__).resolve()
# print(path)
# print(absolute_path)

from os.path import join

base_path = Path(__file__)
path = os.path.join(base_path, '..')
print(path)
path = Path().resolve()
print(path)