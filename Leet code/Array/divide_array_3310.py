class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        nums[:] = nums[1:]
        nums.sort()
        summa = first + nums[0] + nums[1]
        return summa
