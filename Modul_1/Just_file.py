# numbers = [1, 2, 4, 5, 6, 7, 8, 9, 10]
# print(numbers, sep=" ", end=" ", file=open("numbers.txt", "w"))
from Modul_1.lesson_6.String import result


# class Solution:
#     def missingNumber(self, nums: list[int]) -> int:
#          for i in range(len(nums)+1):
#             if i not in nums:
#                 return i
#


# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         result = []
#         if len(nums1) != len(nums2):
#             maximum = max(nums1, nums2)
#             minimum = min(nums1, nums2)
#         else:
#             maximum = nums1
#             minimum = nums2
#         for num in minimum:
#             if num in maximum:
#                 result.append(num)
#                 maximum.remove(num)
#
#         return result


# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         maximum = max(nums1, nums2)
#         minimum = min(nums1, nums2)
#         lists = [item for item in minimum if item in maximum and maximum.remove(item) is None]
#         return lists




# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         maximum = max(nums1, nums2)
#         minimum = min(nums1, nums2)
#         lists = [item for item in minimum if item in maximum and maximum.remove(item) is None]
#         return lists


# class Solution:
#     def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
#         A = sum(aliceSizes)
#         B = sum(bobSizes)
#         T = (A + B )// 2
#         tmp = abs(sum(aliceSizes) - T)
#         for i in aliceSizes:
#             for j in bobSizes:
#                 if (i - j) == tmp:
#                     return [i, j]


# string = "Amirsaid"
#
# for letter in string:
#     print(letter)
















