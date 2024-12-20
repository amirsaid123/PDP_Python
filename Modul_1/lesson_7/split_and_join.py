def split_and_join(line):
    list = line.split(" ")
    line = "-".join(list)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)