class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        counter = 0
        for word in words:
            if brokenLetters in word:
                word.replace(brokenLetters, "")
                counter += 1
        return counter




