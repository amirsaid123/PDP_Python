class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        valid_count = 0

        for word in words:

            if any(char.isdigit() for char in word):
                continue

            if word.count('-') > 1:
                continue
            if '-' in word:
                hyphen_index = word.index('-')

                if not (0 < hyphen_index < len(word) - 1 and word[hyphen_index - 1].islower() and word[
                    hyphen_index + 1].islower()):
                    continue

            punctuation = "!.,"
            punct_count = sum(1 for char in word if char in punctuation)
            if punct_count > 1:
                continue
            if punct_count == 1 and word[-1] not in punctuation:
                continue
            if punct_count == 1 and any(char in punctuation for char in word[:-1]):
                continue

            valid_count += 1

        return valid_count
