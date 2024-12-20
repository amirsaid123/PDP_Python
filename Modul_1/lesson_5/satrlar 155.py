string  = input("Enter a string: ")
result = string.split()
counter = 0

for word in result:
    if word[0].isupper():
        counter += 1
print(counter)