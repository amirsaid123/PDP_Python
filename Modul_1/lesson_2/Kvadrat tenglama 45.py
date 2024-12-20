from math import sqrt

a, b, c = map(int, input("Enter the numbers: ").split())

discriminant = (b**2) - 4 * a * c

if discriminant < 0:
    print("No real solutions")
elif discriminant == 0:
    x1 = (-b) / (2 * a)
    print(f"x1 = x2 = {x1:.2f}")
else:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")

