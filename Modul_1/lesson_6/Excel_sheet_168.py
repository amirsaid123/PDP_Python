number = int(input('Enter a number: '))
string = ""

while number > 0:
    number -= 1
    string = chr(number % 26 + ord('A')) + string
    number //= 26

print(string)


# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         string = ""
#
#         while columnNumber > 0:
#             columnNumber -= 1
#             string = chr(columnNumber % 26 + ord('A')) + string
#             columnNumber //= 26
#         return string
#
