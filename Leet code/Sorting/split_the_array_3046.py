class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        if len(nums) % 2 != 0:
            return False

        nums.sort()

        for num in nums:
            if nums.count(num) > 2:
                return False

        return True




print(Solution().isPossibleToSplit([1,1,1,1]))


