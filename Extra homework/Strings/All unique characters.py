
string = input("Enter a string: ")
counter = 0
unique = ""
for i in string:
    if i not in unique:
        counter += 1
        unique += i

print(counter)