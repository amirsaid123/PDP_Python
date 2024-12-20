import random
numbers = []
n = int(input("Listning uzunligi:"))
multiplication = 1
for i in range(n):
    numbers.append(random.randint(1,10))
    multiplication *= numbers[i]


print("Bizning list:", numbers)
print("Ko`paytma = ", multiplication)




