a, b, c = map(int, input("Enter the numbers:").split())

if c <= b <= a:
    print("a = ", (a**2))
    print("b = ", (b**2))
    print("c = ", (c**2))
else:
    print("a = ", abs(a))
    print("b = ", abs(b))
    print("c = ", abs(c))
