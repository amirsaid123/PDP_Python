class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = []
        s = s.split()
        for char in s:
            if char.isdigit():
                if int(char) not in numbers:
                    numbers.append(int(char))
                else:
                    return False

        return numbers == sorted(numbers)



obj = Solution()
print(obj.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))




#
# sentence = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# sentence = sentence.split()
# numbers = []
# for char in sentence:
#     if char.isdigit():
#         numbers.append(int(char))
#
# print(numbers)
# print(sorted(numbers))