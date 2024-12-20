import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print()

summa = 0
for i in range(10):
    if numbers[i] % 2 != 0:
        summa += numbers[i]

print("O`rtacha = ", summa)
