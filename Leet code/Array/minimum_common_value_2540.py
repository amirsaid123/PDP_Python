# class Solution:
#     def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
#         common = []
#
#         if len(nums1) > len(nums2):
#             max_list = nums1
#             min_list = nums2
#         else:
#             max_list = nums2
#             min_list = nums1
#
#         for num in min_list:
#             if num in max_list:
#                 common.append(num)
#
#         if common:
#             minimum = min(common)
#         else:
#             return -1
#
#         return minimum
#



# class Solution:
#     def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
#         set1 = set(nums1)
#         set2 = set(nums2)
#         common = []
#         for num in set1:
#             if num in set2:
#                 common.append(num)
#         for num in set2:
#             if num in set1:
#                 common.append(num)
#         minimum = min(common)
#         return minimum


# def find_common_elements_sorted(list1, list2):
#     list1.sort()
#     list2.sort()
#
#     common_elements = []
#     i, j = 0, 0
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             i += 1
#         elif list1[i] > list2[j]:
#             j += 1
#         else:
#             common_elements.append(list1[i])
#             i += 1
#             j += 1
#
#     return min(common_elements)


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()

        common_elements = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                common_elements.append(nums1[i])
                i += 1
                j += 1

        if common_elements:
            minimum = min(common_elements)
            return minimum
        else:
            return -1


# class Solution:
#     def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
#         nums1.sort()
#         nums2.sort()
#
#