my_list = [[1], [2, 3], [13, 24, 56, 78, 98], [1], [2], [8], [1, 2, 3]]

maximum = my_list[0]
minimum = my_list[0]

for item in my_list:
    if isinstance(item, list):
        if len(item) > len(maximum):
            maximum = item
        elif len(item) < len(minimum):
            minimum = item

print("Maximum:", maximum)
print("Minimum:", minimum)

