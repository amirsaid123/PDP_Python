numbers = []
n = int(input("n:"))
for i in range(n):
    numbers.append(int(input("number:")))
print(numbers)
print()

a, b = map(int, input("Oraliqni kiriting:").split())
minimum = min(numbers)
new_list = []

for i in range(len(numbers)):
    if (a - 1) <= i <= b-1:
        new_list.append(numbers[i] / minimum)
    else:
        new_list.append(numbers[i])

print([round(num, 1) for num in new_list])