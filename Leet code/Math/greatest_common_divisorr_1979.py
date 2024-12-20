class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        minimum = min(nums)
        maximum = max(nums)
        result = gcd(minimum, maximum)
        return result
