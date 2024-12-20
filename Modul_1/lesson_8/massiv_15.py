import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))
print(numbers)
print()

M = int(input("M:"))
summa = 1
for number in numbers:
    if number < M:
        print(number, end=" ")
        summa += pow(number, 2)
print()
print(summa)