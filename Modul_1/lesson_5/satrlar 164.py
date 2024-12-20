string = input("Enter a string: ")
L = int(input("Enter a start: "))
R = int(input("Enter a end: "))
result = ""
minimum = min(L, R)
maximum = max(L, R)

while minimum <= maximum:
    result += string[minimum]
    minimum += 1
print(result)

