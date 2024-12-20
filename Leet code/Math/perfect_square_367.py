class Solution:
    def isPerfectSquare(self, a: int) -> bool:
        for i in range(1, int(a**0.5)+1):
            if i * i == a:
                return True

        return False




obj = Solution()
print(obj.isPerfectSquare(14))

