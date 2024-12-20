class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = 0
        seen = []
        for num in nums:
            n = nums.count(num)
            if n > 1 and num not in seen:
                counter += (n * (n-1)) // 2
                seen.append(num)

        return counter



print(Solution().numIdenticalPairs([1,2,3,1,1,3]))
