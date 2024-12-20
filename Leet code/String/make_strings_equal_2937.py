class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1 == s2 == s3:
            return 0

        x = y = z = 0
        length = 0
        while x < len(s1) and y < len(s2) and z < len(s3) and s1[x] == s2[y] == s3[z]:
                x += 1
                y += 1
                z += 1
                length += 1

        if length == 0:
            return -1


        c1 = len(s1) - length
        c2 = len(s2) - length
        c3 = len(s3) - length


        return c1 + c2 + c3

