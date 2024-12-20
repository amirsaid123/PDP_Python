def print_full_name(first, last):
    result = ""
    if len(first) and len(last) <= 10:
        result = f"Hello {first} {last}! You just delved into python."
        return result
    else:
        return 0


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))