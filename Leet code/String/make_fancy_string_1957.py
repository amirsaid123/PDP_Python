# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         words = list(s)
#         answer = []
#         for word in words:
#             if len(answer) > 1:
#                 if word == answer[-1] and word == answer[-2]:
#                     answer.pop()
#             answer.append(word)
#
#         word = "".join(answer)
#         return word
#
#
#

class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        for char in s:
            if result[-2:] == char + char:
                continue
            result += char
        return result


# s = "leetcode"
# result = ""
# for char in s:
#     if result[-2:] == char+char:
#         continue
#     result += char
#
# print(result)






