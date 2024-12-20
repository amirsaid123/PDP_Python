class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = sorted(list("qwertyuiop"))
        row2 = sorted(list("asdfghjkl"))
        row3 = sorted(list("zxcvbn"))
        result = []
        for word in words:
            temp = word
            word = word.lower()
            word = set(word)
            if word.issubset(row1):
                result.append(temp)
            elif word.issubset(row2):
                result.append(temp)
            elif word.issubset(row3):
                result.append(temp)

        return result







row1 = sorted(list("qwertyuiop"))
row2 = sorted(list("asdfghjkl"))
row3 = sorted(list("zxcvbn"))


words = ["a", "b"]
result = []
trash = []
for word in words:
    temp = word
    word = word.lower()
    word = set(word)
    if word.issubset(row1):
        result.append(temp)
    elif word.issubset(row2):
        result.append(temp)
    elif word.issubset(row3):
        result.append(temp)
    else:
        trash.append(temp)


print(result)
print(trash)


