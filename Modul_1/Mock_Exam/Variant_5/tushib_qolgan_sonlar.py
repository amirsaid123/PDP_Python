import random
numbers = []
n = int(input("Listning uzunligi:"))
for i in range(n):
    numbers.append(random.randint(1,10))

print("Bizning list:", numbers)

new_list = []
maximum = max(numbers)
minimum = min(numbers)
for i in range(0,maximum+1):
    if i not in numbers:
        new_list.append(i)

print(new_list)
