class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        from functools import reduce

        counters = [Counter(s) for s in words]

        common_chars = reduce(lambda x, y: x & y, counters)

        result = list(common_chars.elements())

        return result


