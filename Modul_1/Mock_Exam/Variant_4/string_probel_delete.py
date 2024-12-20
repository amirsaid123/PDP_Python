def delete_space(string) -> str:
    words = string.split(' ')
    new_string = ''.join(words)
    return new_string

string = input("Enter a string: ")
print(delete_space(string))