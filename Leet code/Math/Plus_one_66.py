class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = ""
        result = []
        for dig in digits:
            number += str(dig)

        int_number = int(number) + 1
        number = str(int_number)

        for num in number:
            result.append(int(num))

        return result

