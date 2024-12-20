class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter

        counter = Counter(s)

        values = [val for val in counter.values()]
        values = set(values)

        return len(values) == 1



