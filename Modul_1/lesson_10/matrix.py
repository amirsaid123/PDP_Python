numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]


# for row in numbers:
#     for column in row:
#         print(column, end=' ')
#     print()

# for row in numbers:
#     for column in row:
#         if column not in range(1, 11):
#             print(column, end=" ")
#     print()

for i in range(0, len(numbers)):
    for j in range(0, len(numbers[i])):
        if numbers[i][j] % 2 == 0:
            print(numbers[i][j], end=" ")
    print()
