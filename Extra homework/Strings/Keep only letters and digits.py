string = input("Enter a string: ")

for i in string:
    if not (i.isalpha() or i.isdigit()):
        string = string.replace(i, "")

print(string)