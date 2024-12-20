class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        from math import factorial
        numbers = []
        for n in range(numRows):
            row = []
            for k in range(n+1):
                temp = factorial(n) // (factorial(k) * (factorial(n - k)))
                row.append(temp)
            numbers.append(row)

        return numbers







