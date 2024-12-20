class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_numbers = []

        columns = [list(column) for column in zip(*matrix)]


        for i in range(len(matrix)):
            for j in range(0, len(matrix[i])):
                if min(matrix[i]) == matrix[i][j] and max(columns[j]) == matrix[i][j]:
                    lucky_numbers.append(matrix[i][j])

        return lucky_numbers

#
# matrix = [[1, 10, 4,  2],
#           [9,  3,  8,  7],
#           [15,16,17,12]
#           ]
#
#
# lucky_numbers = []
#
# columns = [list(column) for column in zip(*matrix)]
#
#
#
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if min(matrix[i]) == matrix[i][j] and max(columns[j]) == matrix[i][j]:
#             lucky_numbers.append(matrix[i][j])
#
# print(lucky_numbers)
#
#
