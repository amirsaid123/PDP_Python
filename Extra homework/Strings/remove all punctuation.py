string = input('Enter a string: ')


for ch in string:
    if ch == "," or ch == "." or ch == ":" or ch == ";" or ch == "'" or ch == '"':
        string = string.replace(ch, "")

print(string)