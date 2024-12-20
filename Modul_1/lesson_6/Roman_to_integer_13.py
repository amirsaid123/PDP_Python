class Solution:
    def romanToInt(self, s: str) -> int:
        summa = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == 'I' and s[i + 1] == 'V':
                summa += 4
                i += 2
            elif i + 1 < len(s) and s[i] == 'I' and s[i + 1] == 'X':
                summa += 9
                i += 2
            elif s[i] == 'I':
                summa += 1
                i += 1
            elif s[i] == 'V':
                summa += 5
                i += 1
            elif i + 1 < len(s) and s[i] == 'X' and s[i + 1] == 'L':
                summa += 40
                i += 2
            elif i + 1 < len(s) and s[i] == 'X' and s[i + 1] == 'C':
                summa += 90
                i += 2
            elif s[i] == 'X':
                summa += 10
                i += 1
            elif s[i] == 'L':
                summa += 50
                i += 1
            elif i + 1 < len(s) and s[i] == 'C' and s[i + 1] == 'D':
                summa += 400
                i += 2
            elif i + 1 < len(s) and s[i] == 'C' and s[i + 1] == 'M':
                summa += 900
                i += 2
            elif s[i] == 'C':
                summa += 100
                i += 1
            elif s[i] == 'D':
                summa += 500
                i += 1
            elif s[i] == 'M':
                summa += 1000
                i += 1

        return summa
