class Solution:
    def maximum69Number(self, num: int) -> int:
        maximum = num
        numbers = list(str(num))
        if "6" not in numbers:
            return maximum

        if numbers[0] == "6":
            numbers[0] = "9"
            return int("".join(numbers))
        else:
            for i in range(len(numbers)):
                if numbers[i] == "6":
                    numbers[i] = "9"
                    temp = "".join(numbers)
                    if int(temp) > maximum:
                        maximum = int(temp)
                        return int(maximum)









