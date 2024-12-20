class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in matrix:
            row = set(row)
            if len(row) != n:
                return False


        j = 0
        while j < n:
            column = [row[j] for row in matrix]
            if len(set(column)) != n:
                return False
            j += 1

        return True


