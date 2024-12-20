import random
numbers = []

row = int(input("Qator: "))
col = int(input("Ustun: "))

for i in range(row):
    row = []
    for j in range(col):
        row.append(random.randint(0,10))
    numbers.append(row)


print("Bizning matrix:")
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end=" ")
    print()

max_freq = 0
number = 0
yangi_list = [num for row in numbers for num in row]

for num in yangi_list:
    count = yangi_list.count(num)
    if count > max_freq:
        max_freq = count
        number = num



print()
print("Son=", number, "Count=", max_freq)

