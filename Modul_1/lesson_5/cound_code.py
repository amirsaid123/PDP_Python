# def count_code(str):
#     counter = 0
#     for i in range(len(str)):
#         if str[i] == "c" and str[i+1] == "o" and str[i + 3] == "e":
#             counter += 1
#     return counter


def count_code2(s):
    return sum(s.count(f"co{ch}e") for ch in "abcdefghijklmnopqrstuvwxyz")

print(count_code2("codecampcolecomecope"))
