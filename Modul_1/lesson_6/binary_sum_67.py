binary1 = input("Binary1: ")
binary2 = input("Binary2: ")

num1 = int(binary1, 2)
num2 = int(binary2, 2)
summa = num1 + num2
binary_sum = bin(summa)[2:]
print(binary_sum)

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = int(a, 2)
#         b = int(b, 2)
#         sum = a + b
#         sum = bin(sum)[2:]
#         return sum
#