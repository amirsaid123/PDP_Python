import random
numbers = []
l = int(input("Enter a number: "))

for i in range(l):
    numbers.append(random.randint(1,100))
print(numbers)

n = int(input("Enter a number: "))

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(sorted_numbers[n-1])

