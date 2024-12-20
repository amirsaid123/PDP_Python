import random
import string
from itertools import count

length = 100
random_string = ''.join(random.choices(string.ascii_letters, k=length))

print(random_string)

print("\n")

char = input("Enter a character: ")

print(random_string.count(char))
