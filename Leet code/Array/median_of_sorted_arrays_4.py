# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         from statistics import median
#         merged = sorted(nums1 + nums2)
#
#         return median(merged)
#
#
#
#





class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) % 2 == 0:
            index_2 = len(merged) // 2
            index_1 = len(merged) // 2 - 1
            median = (merged[index_1] + merged[index_2]) / 2
            return median
        else:
            index_1 = len(merged) // 2
            return merged[index_1]










