class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                index = nums2.index(nums1[i])
                for j in nums2[index+1:]:
                    if nums1[i] < j:
                        result.append(j)
                        break
                else:
                    result.append(-1)

        return result