# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(total)

# for x in range(4):
#     for y in range(4):
#         print(f"({x}, {y})")


# numbers = [5, 2, 5, 2, 2]
#
# for number in numbers:
#     print("x" * number)

numbers = [5, 2, 5, 2, 2]

for number in numbers:
    for y in range(number):
        print("x", end="")
    print()