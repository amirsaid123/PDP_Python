x, y, z = map(int, input("Enter the numbers:").split())
res1 = max((x + y + z), x, y, z)
res2 =(min((x + y) / 2, x, y, z)) ** 2

print(res1, res2)