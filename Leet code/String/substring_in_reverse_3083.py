class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed = s[::-1]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i:j+1]
                if substring in reversed:
                    return True
        return False








s = "abcd"
j = "dcba"