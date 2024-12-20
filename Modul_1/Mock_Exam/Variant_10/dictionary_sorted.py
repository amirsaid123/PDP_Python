my_dict = {
    "f" : 1,
    "b" : 2,
    "a" : 3,
    "d" : 4,
    "c" : 8,
    "z" : 9,
}

sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}

print(sorted_dict)

