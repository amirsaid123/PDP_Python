def count_unique (word: str) -> int:
    counter = 0
    clone = ""
    for letter in word:
        if letter not in clone:
            counter += 1
            clone += letter

    return counter

word = input('Enter a word: ')
print(count_unique(word))