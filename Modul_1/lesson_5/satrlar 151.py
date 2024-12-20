def is_unli (word:str) -> int:
    word = word.lower()
    counter = 0
    for letter in word:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            counter += 1
    return counter

word = input('Enter a word: ')
print(is_unli(word))

