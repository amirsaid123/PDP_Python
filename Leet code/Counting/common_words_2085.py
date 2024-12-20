# class Solution:
#     def countWords(self, words1: list[str], words2: list[str]) -> int:
#         common = []
#         dict1 = {}
#         dict2 = {}
#         for word in words1:
#             dict1[word] = words1.count(word)
#         for word in words2:
#             dict2[word] = words2.count(word)
#
#
#
#
# print(Solution().countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))

words1= ["leetcode","is","amazing","as","is"],
words2 = ["amazing","leetcode","is"]
common = []
dict1 = {}
dict2 = {}
for word in words1:
    dict1[word] = words1.count(word)
for word in words2:
    dict2[word] = words2.count(word)

print(dict1)
print(dict2)
