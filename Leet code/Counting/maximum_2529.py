class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        return max(len(positives), len(negatives))

