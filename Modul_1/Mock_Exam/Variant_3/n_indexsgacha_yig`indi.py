import random
numbers = []
n = int(input("Listning uzunligi:"))
for i in range(n):
    numbers.append(random.randint(1,100))

print("Bizning list:", numbers)

x = int(input("Index:"))
summa = 0

for i in range(x+1):
    summa += numbers[i]
print(summa)

