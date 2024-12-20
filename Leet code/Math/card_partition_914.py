class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        from functools import reduce
        numbers = Counter(deck)


        counter_values = list(numbers.values())

        GCD = reduce(gcd, counter_values)

        if GCD >= 2:
            return True
        else:
            return False

