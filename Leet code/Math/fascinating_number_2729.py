class Solution:
    def isFascinating(self, n: int) -> bool:
        number = str(n)
        number += str(n * 2)
        number += str(n * 3)
        number = list(number)
        number.sort()
        return number == [str(i) for i in range(1, 10)]

print(Solution().isFascinating(111))