import random
n = int(input("n:"))
numbers = []

for i in range(n):
    numbers.append(random.randint(-100,100))

print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers[1])