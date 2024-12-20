# class Solution:
#     def sumCounts(self, nums: list[int]) -> int:
#         n = len(nums)
#         res = 0
#         for i in range(n):
#             distinct = set()
#             for j in range(i, n):
#                 distinct.add(nums[j])
#                 res += len(distinct) ** 2
#         return res
#
#
#



#
from itertools import combinations, permutations, product
#
# nums = [1, 2, 1]
#
# combs = list(combinations(nums, 2))
# result = []
# for comb in combs:
#     for j in range(len(comb)-1):
#         if comb[j] != comb[j+1]:
#             result.append(comb)
#             break
#
# print(result)
#
#



nums = [1, 2, 1]
n = len(nums)
res = 0
for i in range(n):
    distinct = set()
    for j in range(i, n):
        distinct.add(nums[j])
        res += len(distinct) ** 2

print(res)