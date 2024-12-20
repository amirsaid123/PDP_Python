a, b, c, d = map(float, input("Enter the numbers:").split())
minimum = min(a, b, c, d)
maximum = max(a, b, c, d)
if a <= b <= c <= d:
    a = maximum
    b = maximum
    c = maximum
    d = maximum
else:
    a = minimum
    b = minimum
    c = minimum
    d = minimum

print(a, b, c, d)