def reverse_string (word:str) -> str:
    result = ""
    for i in range(len(word)-1, -1, -1):
        result += word[i]
    return result


word = input('Enter a word: ')
print(reverse_string(word))