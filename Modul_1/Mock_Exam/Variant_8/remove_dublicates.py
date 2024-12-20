string = input("Enter a string: ")
unique = ""

for item in string:
    if item not in unique:
        unique += item
print(unique)