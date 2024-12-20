# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 1:
#             return s
#
#         old = ""
#
#         for i in range(len(s)):
#             for j in range(i + 1, len(s) + 1):
#                 substring = s[i:j]
#                 if substring == substring[::-1] and len(substring) > len(old):
#                     old = substring
#                 if len(old) >= len(s) - i:
#                     break
#
#         return old

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        palindrome = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    palindrome.append(substring)

        if palindrome:
            longest = max(palindrome, key=len)
            return longest
        else:
            return s[0]
