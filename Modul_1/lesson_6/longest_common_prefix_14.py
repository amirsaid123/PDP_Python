# list = []
# number = int(input("Enter the length: "))
#
# for i in range(number):
#     word = input(f"Enter string {i + 1}: ")
#     list.append(word)
#
# print(list)
#


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ""
        j = 1
        minimum = min(strs, key=len)

        while j <= len(minimum):
            substring = minimum[0:j]
            all_contain = all(s[:j] == substring for s in strs)
            if all_contain:
                common = substring
            j += 1

        return common




# print("The longest common prefix is", common)




