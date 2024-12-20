class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        i = 1
        while i < n:
            i *= 2

        return i == n
