import random
numbers = []

n = int(input("Enter a number: "))
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0,9))
    numbers.append(row)


print("Original Matrix")
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end=" ")
    print()

print()
print()

print("Changed Matrix")
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if (i == 0 or i == n-1) or (j == 0 or j == n-1):
            print(numbers[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()






