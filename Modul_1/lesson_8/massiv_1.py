import random

numbers = []
min_value = 1
max_value = 100


for i in range(10):
    numbers.append(random.randint(min_value, max_value))

print("Generated numbers:", numbers)


summa = sum(numbers)
middle = summa / len(numbers)

print("Average (middle):", middle)
print()


new_list = []
new_summa = 0
son = 0

for number in numbers:
    if number < middle:
        new_list.append(number)
        new_summa += number
        son += 1

print("Numbers less than the average:", new_list)
print()


if son > 0:
    print("Average of numbers less than the average:", new_summa / son)
else:
    print("No numbers less than the average.")
