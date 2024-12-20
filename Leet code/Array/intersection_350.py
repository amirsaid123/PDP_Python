class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        common = []
        for num in nums1:
            if num in nums2:
                common.append(num)

        return common