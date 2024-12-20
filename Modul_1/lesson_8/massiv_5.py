import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print()

a, b = map(int, input("Oraliq:").split())
new_numbers = []
for i in range(10):
    if a-1 <= i <= b-1:
        pass
    else:
        new_numbers.append(numbers[i])

print(new_numbers)
print("O`rta qiymat = ", sum(new_numbers) / len(new_numbers))
