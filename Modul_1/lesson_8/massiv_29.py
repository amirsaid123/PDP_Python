import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Original numbers:", numbers)
print()

summa = 0
for number in numbers:
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        summa += number


print("Summa:", summa)
