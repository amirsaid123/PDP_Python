def double_char(str):
    result = ""
    for letter in str:
        result += letter * 2
    return result




word = input("Enter a string: ")
print(double_char(word))