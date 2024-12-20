class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        counter = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                counter += 1
        return counter


print(Solution().findNumbers([12,345,2,6,7896]))

