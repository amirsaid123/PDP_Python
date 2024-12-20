def isValid(s: str) -> bool:
    round_count = 0
    square_count = 0
    curly_count = 0

    for char in s:
        if char == '(':
            round_count += 1
        elif char == ')':
            round_count -= 1
        elif char == '[':
            square_count += 1
        elif char == ']':
            square_count -= 1
        elif char == '{':
            curly_count += 1
        elif char == '}':
            curly_count -= 1

        if round_count < 0 or square_count < 0 or curly_count < 0:
            return False

    return round_count == 0 and square_count == 0 and curly_count == 0


string = input("Enter parantheses:")
print(isValid(string))


