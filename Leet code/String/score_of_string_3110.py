class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i in range(len(s)-1):
            value = abs(ord(s[i]) - ord(s[i+1]))
            result += value
        return result













word = "hello"

result = 0

for i in range(len(word)-1):
    value = abs(ord(word[i]) - ord(word[i+1]))
    result += value

print(result)