class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word1 = s[0:len(s)//2]
        word2 = s[len(s)//2:]

        counter1 = 0
        counter2 = 0
        for i in range(len(word1)):
            if word1[i] in vowels:
                counter1 += 1

        for i in range(len(word2)):
            if word2[i] in vowels:
                counter2 += 1

        return counter1 == counter2
