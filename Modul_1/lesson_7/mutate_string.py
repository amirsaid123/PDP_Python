def mutate_string (string: str, num: int, char: chr) -> str:
    if num > len(string)-1:
        return "Index out of range!"
    else:
        l = list(string)
        l[num] = char
        string = "".join(l)
        return string

word = input("Enter a string: ")
index = int(input("Enter the index: "))
character = input("Enter a character: ")
print(mutate_string(word, index, character))