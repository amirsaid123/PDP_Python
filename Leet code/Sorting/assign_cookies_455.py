class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        counter = 0
        g.sort()
        s.sort()
        l1 = len(g)
        l2 = len(s)

        i = 0
        j = 0
        while i < l1 and j < l2:
            if g[i] <= s[j]:
                counter += 1
                i += 1
                j += 1
            else:
                j += 1

        return counter





print(Solution().findContentChildren([1,2, 3], [3]))