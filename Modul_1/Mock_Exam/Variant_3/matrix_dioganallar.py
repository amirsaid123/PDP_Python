import random
numbers = []
summa = 0
n = int(input("n:"))

for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0,9))
    numbers.append(row)


print("Bizning matrix:")
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end="  ")
    print()

print()
print("Dioganal matrix:")

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if (i == j) or (i + j == n-1):
            print(numbers[i][j], end="  ")
            summa += numbers[i][j]
        else:
            print("  ", end="  ")
    print()

print("Summa = ", summa)


