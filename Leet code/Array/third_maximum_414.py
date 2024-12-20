class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]

