class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        result = []
        i = 1
        for word in words:
            if word[0] in vowels:
                result.append(word[:] + "ma" + "a" * i)
                i += 1
            else:
                result.append(word[1:] + word[0] + "ma" + "a" * i)
                i += 1

        result = " ".join(result)
        return result









sentence = "I speak Goat Latin"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

words = sentence.split()
result = []
i = 1
for word in words:
    if word[0] in vowels:
        result.append(word[:] + "ma" + "a" * i)
        i += 1
    else:
        result.append(word[1:] + word[0] + "ma" + "a" * i)
        i += 1


result = " ".join(result)


print(result)