string = input("Gapni kiriting:")
vowels = ""
for letter in string:
    if letter in "aeiouAEIOU":
        vowels += letter

vowels = vowels[::-1]

i = 0
new_string = ""

for letter in string:
    if letter in vowels:
        new_string += vowels[i]
        i+=1
    else:
        new_string += letter

print(new_string)
