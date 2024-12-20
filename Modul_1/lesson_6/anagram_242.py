# word = input('Enter a word: ')
# another_word = input('Enter another word: ')
# result = False
# for letter in another_word:
#     if letter in word:
#         result = True
#     else:
#         result = False
#
# if result:
#     print("The word is a anagram.")
# else:
#     print("The word is not a anagram.")


def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
s = input("Enter a string: ")
t = input("Enter a string: ")
print(isAnagram(s, t))

