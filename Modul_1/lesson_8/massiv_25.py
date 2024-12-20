import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print()

a, b = map(int, input("Oraliq:").split())
summa = 0
for i in range(10):
    if a <= i <= b:
        summa += pow(numbers[i], 3)
print(summa)


