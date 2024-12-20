class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for c in s:
            if s.count(c) > 1:
                if c not in seen:
                    seen.add(c)
                else:
                    return c
