string = input("Enter a string: ")
new_list = []

for item in string:
    if not item.isalnum() and item != " ":
        new_list.append(item)

print(sorted(new_list))