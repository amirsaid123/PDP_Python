def love6(a, b):
    result = False
    if a == 6 or b == 6:
        result = True
    elif a + b == 6 or abs(a - b) == 6:
        result = True
    return result