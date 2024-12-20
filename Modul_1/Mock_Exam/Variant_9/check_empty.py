lists_of_dicts = [{}, {}, {1:2}, {}]
result = True

for item in lists_of_dicts:
    if len(item) != 0:
        result = False
        break
print(result)