string = input("Enter a string: ")
new_string = ""
for i in range(len(string)):
    if not (string[i] == " " and string[i+1] == " "):
        new_string += string[i]

print(new_string)



