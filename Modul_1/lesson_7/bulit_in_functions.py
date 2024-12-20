if __name__ == '__main__':
    s = input()
    if 0 < len(s) < 1000:
        case_1 = False
        case_2 = False
        case_3 = False
        case_4 = False
        case_5 = False
        for i in s:
            if i.isalnum():
                case_1 = True
            if i.isalpha():
                case_2 = True
            if i.isdigit():
                case_3 = True
            if i.islower():
                case_4 = True
            if i.isupper():
                case_5 = True
print(case_1)
print(case_2)
print(case_3)
print(case_4)
print(case_5)
