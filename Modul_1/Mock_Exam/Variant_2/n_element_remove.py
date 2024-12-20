# Original list
my_list = [1, 2, 4, 'a', 'v', '@', '*', '', "hello", "world", 6, 5, 4, 'salom']


n = int(input("Enter a position: "))


reversed_list = my_list[::-1]


if 1 <= n <= len(reversed_list):
    item_to_remove = reversed_list[n-1]
    reversed_list.remove(item_to_remove)
else:
    print("Position is out of range")


my_list = reversed_list[::-1]

print(my_list)
