class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat

        from itertools import chain
        new_matrix = list(chain(*mat))
        shaped = []
        for i in range(r):
            row = new_matrix[i * c: (i + 1) * c]
            shaped.append(row)

#
# from itertools import chain
#
# matrix = [
#     [1,2],
#     [3,4]
# ]
#
# r = 1
# c = 4
#
# new_matrix = list(chain(*matrix))
# shaped = []
# for i in range(r):
#     row = new_matrix[i*c : (i+1)*c]
#     shaped.append(row)
#
# print(shaped)
