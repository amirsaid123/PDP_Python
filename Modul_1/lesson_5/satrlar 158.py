text = input("Enter a text: ")

words = text.split()
even = 0
odd = 0
for word in words:
    if len(word) % 2 == 0:
        even += 1
    else:
        odd += 1

result = odd * even
print(result)
