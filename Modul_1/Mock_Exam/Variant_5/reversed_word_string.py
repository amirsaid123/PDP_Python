string = input("Enter a string: ")
words = string.split(" ")
print(words)
new_list = []
for word in words:
    new_list.append(word[::-1])

print(*new_list)