class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        numbers = set(nums)
        n = 1
        while n in numbers:
            n += 1
        return n





