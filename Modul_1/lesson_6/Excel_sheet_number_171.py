letter = input('Enter the letters: ')
summa = 0

for char in letter:
    value = ord(char) - ord('A') + 1
    summa = summa * 26 + value





print(summa)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        summa = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            summa = summa * 26 + value
        return summa
