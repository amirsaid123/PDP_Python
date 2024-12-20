import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print()

minimum = min(numbers)
for i in range(len(numbers)):
    numbers[i] = numbers[i] / minimum
print([round(num,2) for num in numbers])