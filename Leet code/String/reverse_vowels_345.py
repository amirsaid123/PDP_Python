class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n = len(s)
        reversed = ""
        for i in range(n):
            if s[i] in vowels:
                reversed += s[i]

        reversed = reversed[::-1]
        new_string = ""
        j = 0
        for i in range(n):
            if s[i] not in vowels:
                new_string += s[i]
            else:
                new_string += reversed[j]
                j += 1

        return new_string





# s = "IceCreAm"
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# n = len(s)
# reversed = ""
#
# for i in range(n):
#     if s[i] in vowels:
#         reversed += s[i]
#
# reversed = reversed[::-1]
#
# new_string = ""
# j = 0
# for i in range(n):
#     if s[i] not in vowels:
#         new_string += s[i]
#     else:
#         new_string += reversed[j]
#         j += 1
#
#
# print(new_string)
#
#
