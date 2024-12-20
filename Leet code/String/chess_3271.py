class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, f"f": 6, "g": 7, "h": 8}

        c1 = dict[coordinate1[0]] + coordinate1[1]
        c2 = dict[coordinate2[0]] + coordinate2[1]

        if c1 % 2 == 0 and c2 % 2 == 0 or c1 % 2 == 1 and c2 % 2 == 1:
            return True
        else:
            return False


