# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#



















class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        summa = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            summa = summa * 26 + value
        return summa

ob = Solution()
print(ob.titleToNumber('AAZY'))
