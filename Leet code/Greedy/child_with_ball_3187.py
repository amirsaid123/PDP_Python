class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = [i for i in range(n)]

        full = 2 * (n - 1)

        k = k % full

        if k < n - 1:
            return children[k]
        else:
            return children[2 * (n - 1) - k]





#
# n = 5
# k = 6
#
# children = [i for i in range(n)]
#
# full = 2 * (n - 1)
#
#
# k = k % full
#
#
# if k < n - 1:
#     print(children[k])
# else:
#     print(children[2 * (n - 1) - k])

