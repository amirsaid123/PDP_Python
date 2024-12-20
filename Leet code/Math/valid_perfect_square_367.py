class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(num+1):
            if i * i == num:
                return True

        else:
            return False


n = 14
for i in range(1, n):
    if i * i == n:
        print(True)
        break
    else:
        print(False)
