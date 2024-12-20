class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        palindromes = []
        for word in words:
            if word == word[::-1]:
                palindromes.append(word)

        if palindromes:
            return palindromes[0]
        else:
            return ""











