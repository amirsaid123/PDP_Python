text = input("enter a text:")
result = ""
for letter in text:
    if letter.islower():
        letter = letter.upper()
        result += letter
    else:
        letter = letter.lower()
        result += letter
print(result)