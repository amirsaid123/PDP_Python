string = input("Enter a string: ")
words = string.split(" ")

for i in range(len(words) - 1):
    if words[i] not in words[:i]:
        print(words[i], "frequency is", words.count(words[i]))



