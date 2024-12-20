my_list = [1, 2, 3, 'a', 'b', 'c', "hello", '@', '$', "world", [1, 2, 3], ['a', 'b', '*']]
result = False
for item in my_list:
    if isinstance(item, list):
        result = True

print(result)