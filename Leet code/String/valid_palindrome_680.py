class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                res = s[:l] + s[l+1:]
                res2 = s[:r] + s[r+1:]
                return res == res[::-1] or res2 == res2[::-1]

        return True






