# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         from collections import Counter
#         ballon = "balon"
#         letters = ""
#         for letter in text:
#             if letter in ballon:
#                 letters += letter
#
#         letters = Counter(letters)
#         if len(letters) < 5:
#             return 0
#         letters['l'] //= 2
#         letters['o'] //= 2
#         return min(letters.values())
#
#


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counts = Counter(text)

        max_instances = min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )

        return max_instances







