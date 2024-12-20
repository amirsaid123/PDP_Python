class Solution:
    def canAliceWin(self, n: int) -> bool:
        Alice = 10
        Bob = Alice - 1

        while n > 0:
            # Alice's turn
            if n >= Alice:
                n -= Alice  # Alice removes stones
            else:
                return False  # Alice can't remove enough stones, so Alice loses

            # Bob's turn
            if n >= Bob:
                n -= Bob  # Bob removes stones
            else:
                return True  # Bob can't remove enough stones, Alice wins

            # Decrement the number of stones to remove for both players
            Alice = Bob - 1
            Bob = Alice - 1 # Bob always removes 1 fewer stone than Alice

        return False  # In case the loop ends, Alice loses.

obj = Solution()
print(obj.canAliceWin(27))
#
# def canAliceWin(n: int) -> bool:
#     Alice = 10
#     Bob = Alice - 1
#
#     while n > 0:
#
#         if n >= Alice:
#             n -= Alice
#         else:
#             return False
#
#
#         if n >= Bob:
#             n -= Bob
#         else:
#             return True
#
#
#         Alice -= 1
#         Bob = Alice - 1
#
#     return False
#
#
#
# n = 27
# print(canAliceWin(n))
#
