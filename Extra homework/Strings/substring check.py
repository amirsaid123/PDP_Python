def isexist (stting: str, substring: str) -> bool:
    if substring in stting:
        return True
    else:
        return False



string = input("Enter a string: ")
substring = input("Enter a substring: ")

print(isexist(string, substring))