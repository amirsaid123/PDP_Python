string = input("Enter a string:")
words = string.split(" ")
words = words[::-1]
words_reversed = " ".join(words)
print(words_reversed)
