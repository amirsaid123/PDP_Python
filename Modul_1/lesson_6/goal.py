string = input("Enter a string: ")
new_string = ""
i = 0
while i < len(string):
    if string[i] == '(' and string[i+1] == ')':
        new_string += 'o'
        i += 2
    else:
        new_string += string[i]
        i += 1

print(new_string)
