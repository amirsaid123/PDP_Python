import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 5))
print(numbers)
print()

summa = 0
multi = 1
for i in range(10):
    if i % 2 == 0:
        summa += numbers[i]
    else:
        multi *= numbers[i]

print("Yig`indi = ", summa)
print("Ko`paytma = ", multi)