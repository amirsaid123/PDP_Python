import random
from math import log, isfinite


numbers = [random.randint(1, 100) for _ in range(10)]
print("Original numbers:", numbers)
print()

summa = 0
frequency = 0
for number in numbers:
    if number % 2 == 0:
        summa += number
        frequency += 1

print("O`rta qiymat = ", summa / frequency)
