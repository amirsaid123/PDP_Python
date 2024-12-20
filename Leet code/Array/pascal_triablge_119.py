# class Solution:
#     def getRow(self, rowIndex: int) -> list[int]:
#         from math import factorial
#         numbers = []
#         for n in range(rowIndex+1):
#             row = []
#             for k in range(n + 1):
#                 temp = factorial(n) // (factorial(k) * (factorial(n - k)))
#                 row.append(temp)
#             numbers.append(row)
#
#         return numbers[rowIndex]
#
#
#

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        tmp = [1, 1]
        l = []
        while rowIndex-1 > 0:
            for i in range(len(tmp) - 1):
                l.append(tmp[i] + tmp[i + 1])
            tmp = [1] + l + [1]
            l = []
            rowIndex -= 1
        return tmp






obj = Solution()
print(obj.getRow(3))








