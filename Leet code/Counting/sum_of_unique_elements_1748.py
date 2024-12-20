class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        unique = [num for num in nums if nums.count(num) == 1]
        return sum(unique)