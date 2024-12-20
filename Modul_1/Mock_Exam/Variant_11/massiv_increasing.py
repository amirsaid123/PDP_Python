import random

numbers = []
n = int(input("Enter a number: "))

for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0, 10))
    numbers.append(row)


print("Original matrix:")
for row in numbers:
    print(" ".join(map(str, row)))


for col in range(n):

    column = [numbers[row][col] for row in range(n)]

    column.sort()

    for row in range(n):
        numbers[row][col] = column[row]


print("Matrix with columns sorted:")
for row in numbers:
    print(" ".join(map(str, row)))
