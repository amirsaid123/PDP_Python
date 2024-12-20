# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         nums1[:] = sorted(nums1[:m] + nums2)
#



# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         nums1.extend(nums2)
#         nums1.sort()
#











nums1 = [-1, 1, 2, 3, 0, 0, 0]
m = 7
nums2 = [2, 5, 6]
n = 3

nums1[:] = nums1[:m]
nums2[:] = nums2[:n]

i = 0
j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] > nums2[j]:
        nums1.insert(i, nums2[j])
        j += 1
    else:
        nums1.insert(i, nums1[i])
        i += 1



print(nums1)
