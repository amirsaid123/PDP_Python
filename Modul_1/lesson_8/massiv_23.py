import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))
print(numbers)
print()

summa = 0

for i in range(10):
    if i % 2 == 0:
        summa += numbers[i]

for i in range(10):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i] / summa

print(numbers)