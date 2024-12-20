string = input("Enter a string: ")
words = string.strip().split(" ")
print(len(words[len(words) - 1]))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")
        return len(words[len(words)-1])
