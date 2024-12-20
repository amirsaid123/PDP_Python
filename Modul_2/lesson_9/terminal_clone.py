import os
from os.path import join
from pathlib import Path


while True:
    current_path = os.getcwd()
    command = input(f"{current_path}$ ").split()
    if len(command) > 1 and command[0] == "cd":
        os.chdir(join(current_path, command[1]))
    elif command[0] == "ls":
        print(*os.listdir(current_path), sep=" " * 5)
