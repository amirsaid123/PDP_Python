def password_check(password):
    case_1 = False
    case_2 = False
    case_3 = False
    case_4 = False
    result = False

    if len(password) > 8:
        case_1 = True
    for letter in password:
        if letter.islower():
            case_2 = True
        if letter.isupper():
            case_3 = True
        if letter.isdigit():
            case_4 = True

    if case_1 and case_2 and case_3 and case_4:
        result = True

    return result

password = input("Enter a password: ")
print(password_check(password))
