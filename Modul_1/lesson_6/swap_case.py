string = input("Enter a string:")
for letter in string:
    if letter.islower():
        letter = letter.upper()
        print(letter, end="")
    else:
        letter = letter.lower()
        print(letter, end="")
