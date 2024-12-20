class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        initial = money
        prices.sort()
        i = 0
        chocolate = 0
        while chocolate < 2:
            money -= prices[i]
            chocolate += 1
            i += 1

        if money >= 0:
            return money
        else:
            return initial
