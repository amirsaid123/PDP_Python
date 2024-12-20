string = input("Gapni kiriting: ")
words = string.split()
max_length_word = max(words, key=len)
print("Gapdagi eng uzun so`z:", max_length_word)