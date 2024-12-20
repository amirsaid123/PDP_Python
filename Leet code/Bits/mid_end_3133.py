class Solution:
    def minEnd(self, n: int, x: int) -> int:
        y = [4]
        i = x + 1
        while True:
            y.extend([i])
            if len(y) == n:
                for i in range(len(y)-1):
                    if not y[i] & y[i+1] == x:
                        break
                else:
                    continue
            i += 1


        return y[-1]


n = 3
x = 4

y = [4]
i = x + 1
while True:
    y.extend([i])
    if len(y) == n:
        if (y[0] & y[1] & y[2]) == x:
            break
        else:
            i += 1

    i += 1


print(y[len(y) - 1])

