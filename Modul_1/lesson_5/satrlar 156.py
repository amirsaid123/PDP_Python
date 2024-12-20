string = input("Enter a string: ")
print(string)
print()
i = int(input("First word: "))
j = int(input("Second word: "))

result = string.split()

if 1 <= i <= len(string) and 1 <= j <= len(result):
    i -= 1
    j -= 1

result[i], result[j] = result[j], result[i]

string = " ".join(result)

print(string)