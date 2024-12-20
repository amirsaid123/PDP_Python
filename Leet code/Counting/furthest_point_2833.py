class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count("L")
        right = moves.count("R")
        under = moves.count("_")

        if left >= right:
            return left + under - right
        return right + under - left


print(Solution().furthestDistanceFromOrigin('"L_RL__R"'))












