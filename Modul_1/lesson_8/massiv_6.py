import random


list = []

for i in range(0,10):
    value = random.randint(0,100)
    list.append(value)
print(list)
print()
for j in range(len(list)):
    list[j] = pow(list[j], 2)

print(list)
print()
print("Summa = ", sum(list))
