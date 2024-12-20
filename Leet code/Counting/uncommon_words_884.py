class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1 = s1.split()
        s2 = s2.split()
        uncommon = []
        for word in s1:
            if word not in s2 and s1.count(word) == 1:
                uncommon.append(word)

        for word in s2:
            if word not in s1 and s2.count(word) == 1:
                uncommon.append(word)

        return uncommon


print(Solution().uncommonFromSentences('apple apple', 'banana'))
