my_dict = {
    "a" : 1,
    "b" : 2,
    "c" : None,
    "d" : None,
    "e" : 8,
    "f" : None,
}

my_dict = {key: value for key, value in my_dict.items() if value is not None}

print(my_dict)