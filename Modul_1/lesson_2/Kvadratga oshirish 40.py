x, y, z = map(int, input("Enter the numbers:").split())
if x > 0:
    x **= 2
elif y > 0:
    y **= 2
elif z > 0:
    z **= 2

print(x, y, z)