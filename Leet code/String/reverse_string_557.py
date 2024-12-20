class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        new = []
        for word in words:
            temp = word[::-1]
            new.append(temp)
        words = " ".join(new)
        return words













sentence = "Let's take LeetCode contest"

words = sentence.split()
new = []
for word in words:
    temp = word[::-1]
    new.append(temp)


words = " ".join(new)
print(words)