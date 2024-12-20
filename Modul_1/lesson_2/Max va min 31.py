x, y = map(int, input("Enter the numbers:").split())
maximum = minimum = 0
if x > y:
    maximum = x
    minimum = y
else:
    maximum = y
    minimum = x

print("Maximum = ", maximum)
print("Minimum = ", minimum)