x, y, z = map(int, input("Enter the numbers:").split())


if y > x and y > z:
    maximum = y
elif z > x and z > y:
    maximum = z
elif x > y and x > z:
    maximum = x
if x < y and x < z:
    minimum = x
elif y < z and y < x:
    minimum = y
elif z < x and z < y:
    minimum = z



print("Maximum is", maximum)
print("Minimum is", minimum)