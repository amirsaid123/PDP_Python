# phrase = input('Enter a phrase: ')
# phrase = phrase.lower()
#
# first = ""
# second = ""
#
# result = False
# for letter in phrase:
#     if letter.isalpha():
#         first += letter
#
# second = first[::-1]
# if first == second:
#     result = True
#
# print(result)
#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        for letter in s:
            if letter.isalnum():
                temp += letter

        return temp == temp[::-1]

