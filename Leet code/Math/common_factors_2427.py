class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        maximum = max(a, b)

        for i in range(1, maximum + 1):
            if a % i == 0 and b % i == 0:
                counter += 1

        return counter
