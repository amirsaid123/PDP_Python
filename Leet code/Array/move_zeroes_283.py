class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nums.sort(key=lambda x: x==0)



