class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = []
        counter = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(counter)
                counter += 1
            matrix.append(row)

        position = [0, 0]
        for command in commands:
            if command == "DOWN":
                position[0] += 1
            elif command == "RIGHT":
                position[1] += 1
            elif command == "UP":
                position[0] -= 1
            elif command == "LEFT":
                position[1] -= 1


        return matrix[position[0]][position[1]]


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        position  = 0
        for x in commands:
            match x:
                case "RIGHT":
                    position += 1
                case "LEFT":
                    position -= 1
                case "DOWN":
                    position += n
                case "UP":
                    position -= n
        return position
# n = 2
# matrix = []
#
#
# counter = 0
#
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(counter)
#         counter += 1
#     matrix.append(row)
#
# for row in matrix:
#     print(row)
#
#
# commands = ["DOWN","RIGHT","LEFT"]
# position = [0, 0]
# for command in commands:
#     if command == "DOWN":
#         position[0] += 1
#     elif command == "RIGHT":
#         position[1] += 1
#     elif command == "UP":
#         position[0] -= 1
#     elif command == "LEFT":
#         position[1] -= 1
#
# print(matrix[position[0]][position[1]])