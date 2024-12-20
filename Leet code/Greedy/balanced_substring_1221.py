class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        for i in s:
            if i == "R":
                r += 1
            else:
                l += 1

            if l == r:
                counter += 1
                l = 0
                r = 0
        return counter


s = "RLRRRLLRLL"
counter = 0

l = 0
r = 0

for i in s:
    if i == "R":
        r += 1
    else:
        l += 1

    if l == r:
        counter += 1
        l = 0
        r = 0

print(counter)
