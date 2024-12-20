string = input("Enter a string: ")
summa = 0
for i in range(len(string) - 1):
    summa += abs(ord(string[i]) - ord(string[i + 1]))
print(summa)
