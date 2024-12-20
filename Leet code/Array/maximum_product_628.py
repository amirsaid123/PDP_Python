class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()

        maximum = nums[-1] * nums[-2] * nums[-3]
        maximum_2 = nums[0] * nums[1] * nums[-1]

        return max(maximum, maximum_2)
