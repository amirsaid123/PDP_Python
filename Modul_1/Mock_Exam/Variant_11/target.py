numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
y = 0
target = int(input("Enter a number: "))

for i in range(len(numbers)-1):
    if numbers[i] + numbers[i+1] == target:
        x = i
        y = i + 1
        break
print(x, y)
