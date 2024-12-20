import random


numbers = [random.randint(-100, 100) for _ in range(10)]
print("Original numbers:", numbers)
print()


minimum = min(numbers)

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = minimum

print("Updated numbers:", numbers)
