a = input("Enter a string:")
b = input("Enter another string:")
new_string = ""
words = a.split(" ")

for word in words:
    if word == b:
        new_string += word[::-1] + " "
    else:
        new_string += word + " "
print(new_string)
