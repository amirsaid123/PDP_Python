class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_1 = 0
        sum_2 = 0
        for i in range(len(num)):
            if i % 2 == 0:
                sum_1 += num[i]
            else:
                sum_2 += num[i]

        return sum_1 == sum_2
