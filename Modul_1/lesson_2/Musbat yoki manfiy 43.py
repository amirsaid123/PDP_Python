x, y = map(float, input("Enter the numbers:").split())

if x < 1 and y < 1:
    x = abs(x)
    y = abs(y)
elif x > 1 and y < 1:
    x *= 0.5
    y *= 0.5
elif x < 1 and y > 1:
    x *= 0.5
    y *= 0.5
else:
    pass

print(x, y)