from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:

        letter_counts = Counter("".join(words))


        x = len(words)
        for count in letter_counts.values():
            if count % x != 0:
                return False
        return True
