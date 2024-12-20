class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summa = 0
        numbers = list(str(n))
        for number in numbers:
            product *= int(number)
            summa += int(number)


        return product - summa

