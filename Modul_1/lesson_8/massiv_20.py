import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 20))
print(numbers)
print()

K = int(input("K:"))
M = int(input("M:"))
frequency = 0
for number in numbers:
    if not (K <= number <= M):
        frequency += 1

print(frequency)

