class Solution:
    def addDigits(self, num: int) -> int:
        if num >= 0 and num <= 9:
            return num

        while num > 9:
            num = num // 10 + num % 10

            if 0 <= num < 10:
                return num

