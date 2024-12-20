string = input("Enter a string: ")
print(string)
print()
i = int(input("word: "))


result = string.split()

if 1 <= i <= len(string):
    i -= 1

result[i] = "TATU"

string = " ".join(result)

print(string)