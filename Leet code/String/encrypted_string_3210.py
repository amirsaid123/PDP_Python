class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        new_string = ""
        for i in range(len(s)):
            index = (i+k) % len(s)
            new_string += s[index]
        return new_string


string = "dart"
k = 3

new_string = ""

for i in range(len(string)):
    index = (i + k) % len(string)
    new_string += string[index]

print(new_string)



