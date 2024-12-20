import random
numbers = []
for i in range(10):
    numbers.append(random.randint(-100, 100))
print(numbers)
print()

summa = 0
new_list = []
for number in numbers:
    if number < 0:
        new_list.append(number)
        summa += number


print(summa / len(new_list))
