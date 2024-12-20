class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = ""
        for char in s:
            if char.isalpha():
                letters += char

        letters = letters[::-1]

        new_string = ""
        i = 0
        for char in s:
            if char.isalpha():
                new_string += letters[i]
            else:
                new_string += char
            i += 1

        return new_string
