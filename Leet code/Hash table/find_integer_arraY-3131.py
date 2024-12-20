class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()

        return nums2[0] - nums1[0]

