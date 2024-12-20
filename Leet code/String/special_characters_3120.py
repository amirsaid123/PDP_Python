class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        counter = 0


        if word.islower() or word.isupper():
            return 0


        seen_chars = set()


        for char in word:

            if char in seen_chars:
                continue


            if char.islower() and char.upper() in word:
                counter += 1
                seen_chars.add(char)
                seen_chars.add(char.upper())
            elif char.isupper() and char.lower() in word:
                counter += 1
                seen_chars.add(char)
                seen_chars.add(char.lower())

        return counter
