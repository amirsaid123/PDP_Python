class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = []

        for i in range(len(number)):
            if number[i] == digit:
                string = number[:i] + number[i + 1:]
                result.append(int(string))
        answer = str(max(result))

        return answer



# number = "1231"
# digit = "1"
# result = []
#
# for i in range(len(number)):
#     if number[i] == digit:
#         string = number[:i] + number[i+1:]
#         result.append(int(string))
#
# print(result)
# print(max(result))
#
#
#
#
#
