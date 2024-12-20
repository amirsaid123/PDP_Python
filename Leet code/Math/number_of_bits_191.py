class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        result = 0
        for i in binary:
            if i == '1':
                result += 1
        return result







n = 11
binary = str(bin(n))[2:]
result = 0
for i in binary:
    if i == '1':
        result += 1

print(result)