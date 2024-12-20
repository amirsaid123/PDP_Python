def is_palindrom(word: str) -> bool:
    result = False
    clone = ""
    for letter in range (len(word) - 1, -1, -1):
        clone += word[letter]
    if clone == word:
        result = True

    return result


word = input('Enter a word: ')
print(is_palindrom(word))
