text = input("Enter a text:")
words = text.split()
counter = 0
for word in words:
    if word.startswith('a') and word.endswith('b'):
        counter += 1
print(counter)