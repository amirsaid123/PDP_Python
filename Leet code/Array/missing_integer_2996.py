class Solution:
    def missingInteger(self, nums: list[int]) -> int:

        summa = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
               summa += nums[i]
            else:
                break


        while True:
            if summa not in nums:
                return summa
            else:
                summa += 1











