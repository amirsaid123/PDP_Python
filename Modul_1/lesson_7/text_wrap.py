import textwrap

def wrap(string, max_width):
    text = textwrap.wrap(string, max_width)
    return "\n".join(text)

if __name__ == '__main__':
    string = input("Enter a string: ")
    max_width = int(input("Enter a max width: "))
    result = wrap(string, max_width)
    print(result)
