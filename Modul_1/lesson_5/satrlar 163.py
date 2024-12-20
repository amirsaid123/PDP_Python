string = input("Enter a string: ")
words = string.split(" ")
maximum = ""
for word in words:
    if (len(word) > len(maximum)):
        maximum = word
print(maximum)