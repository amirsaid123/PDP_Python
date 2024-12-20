class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        letters = Counter(s)
        counter = 0
        has_odd = False
        for count in letters.values():
            if count % 2 == 0:
                counter += count
            else:
                has_odd = True
                counter += count - 1

        if has_odd:
            counter += 1

        return counter


# from collections import Counter
# s = "abccccdd"
#
# letters = Counter(s)
# counter = 0
#
# for count in letters.values():
#     if count % 2 == 0:
#         counter += count
#     else:
#         counter += count -1
#
#
#
#
#
#
# print(counter)
# print(letters)