class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        summa = 0
        for i in range(k):
            summa += nums[i]

        return summa


# num1 = 3
# num0 = 2
# numneg = 0
# k = 4
#
# nums = [1] * num1 + [0] * num0 + [-1] * numneg
# summa = 0
# for i in range(k):
#     summa += nums[i]
#
# print(summa)