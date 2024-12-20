class Solution:
    def mySqrt(self, x: int) -> int:
        from math import sqrt, floor
        result = sqrt(x)
        return floor(result)
