class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        nums = []
        for i, word in enumerate(words):
            if x in word:
                nums.append(i)
        return nums
