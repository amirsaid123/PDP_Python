r1 = int(input("Enter the first resistance: "))
r2 = int(input("Enter the second resistance: "))
r3 = int(input("Enter the third resistance: "))
total_resistance = r1 + r2 + r3
parallel = 1 / total_resistance
print(f"The total resistance in parallel is: {parallel:.2f}")