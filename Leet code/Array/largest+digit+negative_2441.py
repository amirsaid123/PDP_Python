class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        similar = []
        for i in nums:
            for j in nums:
                if i + j == 0:
                    similar.append(max(i, j))


        if similar:
            return max(similar)
        else:
            return -1


