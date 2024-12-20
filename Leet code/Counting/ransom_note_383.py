class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        new_string = ""
        for letter in ransomNote:
            if letter in magazine:
                new_string += letter
                magazine = magazine.replace(letter, "", 1)

        if new_string == ransomNote:
            result = True
        return result
