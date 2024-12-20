import random
from math import sin
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print()


summa = 1
for number in numbers:
    if number % 2 == 0 and number % 2 == 5:
        print(number, end=" ")
        summa *= number
print()
print(sin(summa))