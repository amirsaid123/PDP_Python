import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))
print(numbers)
print()

summa = 1
summa_2 = 0
for number in numbers:
    summa += pow(number, 2)

middle = sum(numbers) / len(numbers)
print()
print("Summa = ", summa)
print("O`rta qiymat = ", middle)