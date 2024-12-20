class Solution:
    def clearDigits(self, s: str) -> str:
        result = []

        for i in range(len(s)):
            if s[i].isdigit():
                if result:  
                    result.pop()
            else:
                result.append(s[i])

        return ''.join(result)



