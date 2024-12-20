x, y, z = map(int, input("Enter the numbers:").split())

if (x + y) > z and (x + z) > y and (y + z) > x:
    print("Yes")
else:
    print("No")