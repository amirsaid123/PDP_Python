x, y, z = map(float, input("Enter the numbers:").split())
minimum = min(x,y,z)
maximum = max(x,y,z)
middle = (x + y + z) - maximum - minimum
if x < 1 and y < 1 and z < 1:
    minimum = (maximum + middle) / 2

print(minimum, middle, maximum)
