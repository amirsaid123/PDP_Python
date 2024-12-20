# string = input("Enter a string: ")
# words = string.split(" ")
# words.reverse()
# reversed_string = " ".join(words)
# print(reversed_string)

string = input("Enter a string: ")
words = string.split(" ")


words.reverse()

reversed_words = [word[::-1] for word in words]

reversed_string = ' '.join(reversed_words)

print(reversed_string)
