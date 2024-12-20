def isanagram (string: str, word: str) -> bool:
    result = False
    string = string.replace(" ", "").lower()
    word = word.replace(" ", "").lower()

    if sorted(string) == sorted(word):
        result = True

    return result



string = input("Enter a string: ")
word = input("Enter a word: ")
print(isanagram(string, word))