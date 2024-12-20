class Solution:
    def sumZero(self, n: int) -> list[int]:
        result = []

        if n % 2 == 0:
            i = 1
            while i <= n:
                result.append(i)
                result.append(-i)
                i += 2
        else:
            i = 1
            while i <= n-2:
                result.append(i)
                result.append(-i)
                i += 2
            result.append(0)

        return result


obj = Solution()
print(obj.sumZero(5))
