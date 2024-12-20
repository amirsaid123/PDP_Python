class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        result = ""
        maximum = max(len(num1), len(num2))

        for i in range(maximum):
            digi1 = int(num1[i]) if i < len(num1) else 0
            digi2 = int(num2[i]) if i < len(num2) else 0

            temp = digi1 + digi2 + carry

            result += str(temp % 10)
            carry = temp // 10


        if carry:
            result += str(carry)


        return result[::-1]






#
# num1 = "11"
# num2 = "123"
# carry = 0
# num1 = num1[::-1]
# num2 = num2[::-1]
#
# result = ""
# max_length = max(len(num1), len(num2))
#
# for i in range(max_length):
#     digit1 = int(num1[i]) if i < len(num1) else 0
#     digit2 = int(num2[i]) if i < len(num2) else 0
#
#
#     temp_sum = digit1 + digit2 + carry
#
#
#     result += str(temp_sum % 10)
#     carry = temp_sum // 10
#
#
# if carry:
#     result += str(carry)
#
#
# result = result[::-1]
# print(result)
