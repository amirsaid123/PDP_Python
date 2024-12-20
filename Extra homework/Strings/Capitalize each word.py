string = input("Enter a string: ")
words = string.split(" ")
for word in words:
    print(word.capitalize(), end=" ")