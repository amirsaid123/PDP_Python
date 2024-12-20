class Solution:
    def findLucky(self, arr: list[int]) -> int:
        lucky = []
        for num in arr:
            if arr.count(num) == 2:
                lucky.append(num)

        return max(lucky)


print(Solution().findLucky([1,2,2,3,3,3,]))