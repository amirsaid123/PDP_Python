class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = []
        for row in image:
            reversed_row = row[::-1]
            new_row = []
            for num in reversed_row:
                if num == 0:
                    new_row.append(1)
                else:
                    new_row.append(0)
            new_image.append(new_row)
        return new_image

#
# image = [
#     [1,1,0],
#     [1,0,1],
#     [0,0,0]
# ]
# new_image = []
# for row in image:
#     reversed_row = row[::-1]
#     new_row = []
#     for num in reversed_row:
#         if num == 0:
#             new_row.append(1)
#         else:
#             new_row.append(0)
#     new_image.append(new_row)
#
#
# print(image)
# print(new_image)