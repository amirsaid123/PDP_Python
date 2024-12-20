def find_max_from_list(numbers: list) -> int:
    max_number = numbers[0]
    for number in numbers:
        if number >= max_number:
            max_number = number

    return max_number