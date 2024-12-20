import random
from math import log
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print()

M = int(input("M:"))
summa = 1
for number in numbers:
    if number > M:
        print(number, end=" ")
        summa *= number
print()
print(round(log(summa), 2))