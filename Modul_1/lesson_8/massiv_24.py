import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

print(numbers)
print()

maximum = max(numbers)
index = numbers.index(maximum)
k = int(input("k:"))
num = numbers[k-1]
numbers[k-1] = maximum
numbers[index] = num
print(numbers)
