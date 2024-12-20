string = input("Enter a string: ")
result = True
for i in string:
    if not ( 'a' <= i <= 'z' or "A" <= i <= "Z" ):
        result = False
print(result)

