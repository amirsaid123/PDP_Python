class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []

        for i, row in enumerate(mat):
            temp = [i, row.count(1)]
            result.append(temp)

        result = sorted(result, key=lambda x: x[1])
        final = [x[0] for x in result[:k]]

        return final




#
#
# mat = [
#  [1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]
#        ]
# k = 3
#
# result = []
#
# for i, row in enumerate(mat):
#     temp = [i, row.count(1)]
#     result.append(temp)
#
# print(result)
#
# result = sorted(result, key=lambda x: x[1])
# final = [x[0] for x in result[:k]]
# print(final)